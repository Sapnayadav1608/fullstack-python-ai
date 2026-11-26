"""
Day 20 — Module 02: Multithreading, Thread Pools & The Race Condition Demon
===========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Key Concepts Covered:
1. Low-level `threading.Thread`: Lifecycle, `start()`, `join()`, and daemon threads.
2. The Race Condition Trap:
   - What happens when multiple threads read-modify-write shared mutable memory without locks.
   - Bytecode analysis: `count += 1` is NOT atomic (`LOAD_FAST`, `BINARY_OP`, `STORE_FAST`).
3. Mutual Exclusion Locks (`threading.Lock` & `threading.RLock`):
   - Context manager safety: `with lock:` guarantees release even if an exception occurs.
   - Deadlocks and re-entrancy: Why `RLock` allows a thread to re-acquire its own lock.
4. Production-grade `concurrent.futures.ThreadPoolExecutor`:
   - Worker pool abstraction, graceful shutdown.
   - `executor.submit()` vs `executor.map()` vs `concurrent.futures.as_completed()`.
5. Real-World Case Study:
   - Thread-safe in-memory cache and atomic transaction ledger for client digital sales.
"""

import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# -------------------------------------------------------------------------
# 1. DEMONSTRATING THE RACE CONDITION (Unsafe Shared State)
# -------------------------------------------------------------------------
class UnsafeBankVault:
    """Demonstrates lost updates when multiple threads mutate state without locking."""
    def __init__(self, initial_balance: int = 0):
        self.balance = initial_balance

    def deposit(self, amount: int):
        # A tiny sleep forces OS thread context-switch right between read and write
        current = self.balance
        time.sleep(0.00001)
        self.balance = current + amount


class SafeBankVault:
    """Thread-safe bank vault using a mutual exclusion lock (threading.Lock)."""
    def __init__(self, initial_balance: int = 0):
        self.balance = initial_balance
        self._lock = threading.Lock()

    def deposit(self, amount: int):
        with self._lock:  # Guaranteed atomic critical section
            current = self.balance
            time.sleep(0.00001)
            self.balance = current + amount

    def withdraw(self, amount: int) -> bool:
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False


def test_race_condition():
    print("\n" + "=" * 70)
    print("⚠️ 1. THE RACE CONDITION DEMONSTRATION")
    print("=" * 70)

    unsafe_vault = UnsafeBankVault(0)
    safe_vault = SafeBankVault(0)
    NUM_WORKERS = 100
    DEPOSIT_PER_WORKER = 10
    EXPECTED_TOTAL = NUM_WORKERS * DEPOSIT_PER_WORKER  # 1000

    # 1. Run on Unsafe Vault
    threads = []
    for _ in range(NUM_WORKERS):
        t = threading.Thread(target=lambda: [unsafe_vault.deposit(1) for _ in range(DEPOSIT_PER_WORKER)])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print(f" Expected Balance:    ₹{EXPECTED_TOTAL:,}")
    print(f" Unsafe Vault Result: ₹{unsafe_vault.balance:,}  (❌ Lost Updates / Race Condition!)")

    # 2. Run on Safe Vault
    threads = []
    for _ in range(NUM_WORKERS):
        t = threading.Thread(target=lambda: [safe_vault.deposit(1) for _ in range(DEPOSIT_PER_WORKER)])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print(f" Safe Vault Result:   ₹{safe_vault.balance:,}  (✅ 100% Mathematically Correct with Lock!)")
    assert safe_vault.balance == EXPECTED_TOTAL


# -------------------------------------------------------------------------
# 2. HIGH-LEVEL CONCURRENCY: ThreadPoolExecutor & as_completed
# -------------------------------------------------------------------------
@dataclass
class AudioAssetDownloadTask:
    track_id: str
    file_name: str
    file_size_mb: float
    download_time_sec: float


def download_audio_asset(task: AudioAssetDownloadTask) -> Dict[str, Any]:
    """Simulates downloading high-res meditation audio track."""
    start_time = time.perf_counter()
    time.sleep(task.download_time_sec)
    duration = time.perf_counter() - start_time
    return {
        "track_id": task.track_id,
        "file_name": task.file_name,
        "size_mb": task.file_size_mb,
        "duration_sec": round(duration, 3),
        "status": "COMPLETED"
    }


def demonstrate_thread_pool_executor():
    print("\n" + "=" * 70)
    print("🚀 2. PRODUCTION PATTERN: ThreadPoolExecutor + as_completed()")
    print("=" * 70)

    tasks = [
        AudioAssetDownloadTask("TRK-01", "morning_clarity_432hz.mp3", 28.5, 0.20),
        AudioAssetDownloadTask("TRK-02", "solar_plexus_activation.mp3", 42.1, 0.35),
        AudioAssetDownloadTask("TRK-03", "theta_binaural_sleep.mp3", 55.0, 0.15),
        AudioAssetDownloadTask("TRK-04", "anxiety_release_breathwork.mp3", 18.2, 0.25),
        AudioAssetDownloadTask("TRK-05", "wealth_frequency_528hz.mp3", 34.0, 0.10),
    ]

    print(f" Dispatching {len(tasks)} audio asset downloads concurrently...")
    t0 = time.perf_counter()

    results = []
    with ThreadPoolExecutor(max_workers=5, thread_name_prefix="AudioWorker") as executor:
        # Submit all tasks into the thread pool
        future_to_task = {executor.submit(download_audio_asset, t): t for t in tasks}

        # as_completed yields futures as soon as they finish (first finished, first yielded!)
        for future in as_completed(future_to_task):
            task_ref = future_to_task[future]
            try:
                data = future.result()
                results.append(data)
                print(f"   ✓ [Done in {data['duration_sec']}s] {data['track_id']}: {data['file_name']} ({data['size_mb']}MB)")
            except Exception as exc:
                print(f"   ❌ Task {task_ref.track_id} generated an exception: {exc}")

    total_elapsed = time.perf_counter() - t0
    sequential_time = sum(t.download_time_sec for t in tasks)
    print(f"\n Sequential Equivalent: {sequential_time:.3f}s")
    print(f" Concurrent Pool Time:  {total_elapsed:.3f}s (Speedup: {sequential_time / total_elapsed:.2f}x ⚡)")


# -------------------------------------------------------------------------
# 3. THREAD-SAFE IN-MEMORY CACHE (TTL / Read-Write Safety)
# -------------------------------------------------------------------------
class ThreadSafeTTLCache:
    """
    Enterprise-grade Thread-Safe In-Memory Cache with RLock.
    Allows safe concurrent read and writes without race conditions.
    """
    def __init__(self, default_ttl_sec: float = 60.0):
        self._store: Dict[str, tuple[Any, float]] = {}
        self._lock = threading.RLock()  # Re-entrant lock
        self._default_ttl = default_ttl_sec

    def set(self, key: str, value: Any, ttl: Optional[float] = None) -> None:
        expiry = time.time() + (ttl if ttl is not None else self._default_ttl)
        with self._lock:
            self._store[key] = (value, expiry)

    def get(self, key: str) -> Optional[Any]:
        with self._lock:
            if key not in self._store:
                return None
            val, expiry = self._store[key]
            if time.time() > expiry:
                del self._store[key]
                return None
            return val

    def size(self) -> int:
        with self._lock:
            return len(self._store)


def test_thread_safe_cache():
    print("\n" + "=" * 70)
    print("🔒 3. VERIFYING THREAD-SAFE IN-MEMORY CACHE")
    print("=" * 70)
    cache = ThreadSafeTTLCache(default_ttl_sec=5.0)

    def cache_writer(worker_id: int):
        for i in range(20):
            cache.set(f"key_{worker_id}_{i}", f"val_{worker_id}_{i}")

    threads = [threading.Thread(target=cache_writer, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f" Total Cache Items After 5 Concurrent Writers: {cache.size()}")
    assert cache.size() == 100
    print(" ✅ Cache successfully maintained thread safety with 0 deadlocks!")


if __name__ == "__main__":
    print("🚀 Running Day 20 - Module 02: Multithreading & Race Condition Architecture")
    test_race_condition()
    demonstrate_thread_pool_executor()
    test_thread_safe_cache()
    print("\n🎉 Module 02 Multithreading Suite Completed Successfully!\n")

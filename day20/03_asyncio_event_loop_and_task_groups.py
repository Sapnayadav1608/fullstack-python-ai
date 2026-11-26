"""
Day 20 — Module 03: Asynchronous Programming, Event Loops & Python 3.11+ TaskGroups
==================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Key Concepts Covered:
1. Cooperative Multitasking vs Preemptive Multithreading:
   - Threads: OS kernel switches contexts unpredictably (preemptive).
   - AsyncIO: Coroutines explicitly yield control via `await` when waiting on I/O (cooperative).
2. The Event Loop Architecture:
   - Single-threaded reactor pattern (`selectors` module).
   - The Golden Rule: NEVER call blocking synchronous code (`time.sleep()`, `requests.get()`)
     inside an async coroutine without `asyncio.to_thread()`, or it freezes the entire event loop!
3. Concurrent Execution with `asyncio.gather()`:
   - Fanning out independent coroutines concurrently.
4. Python 3.11+ Structured Concurrency: `asyncio.TaskGroup`:
   - Why `asyncio.gather()` had flaws: If one task failed, orphaned tasks kept running.
   - `TaskGroup` context manager: Automatic cancellation of child tasks on failure and
     safe `ExceptionGroup` propagation.
5. Timeouts with Modern `asyncio.timeout()`:
   - Resilient network calls with guaranteed deadlines.
"""

import sys
import asyncio
import time
from typing import List, Dict, Any

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# -------------------------------------------------------------------------
# 1. UNDERSTANDING COROUTINES & THE EVENT LOOP
# -------------------------------------------------------------------------
async def fetch_meditation_metadata(track_id: str, delay: float) -> Dict[str, Any]:
    """
    Simulates non-blocking async network fetch.
    asyncio.sleep yields execution back to the event loop so other tasks can run!
    """
    # print(f"  [Start] Fetching {track_id} (will take {delay}s)...")
    await asyncio.sleep(delay)
    return {
        "track_id": track_id,
        "title": f"Binaural Beats {track_id}",
        "frequency_hz": 432 if "A" in track_id else 528,
        "status": "LOADED"
    }


async def demonstrate_gather():
    print("\n" + "=" * 70)
    print("⚡ 1. CONCURRENT FAN-OUT WITH asyncio.gather()")
    print("=" * 70)

    track_queries = [
        ("TRACK-A1", 0.20),
        ("TRACK-B2", 0.15),
        ("TRACK-C3", 0.30),
        ("TRACK-D4", 0.10)
    ]

    t0 = time.perf_counter()
    # Fan out all coroutines into the event loop concurrently
    results = await asyncio.gather(*(fetch_meditation_metadata(tid, delay) for tid, delay in track_queries))
    elapsed = time.perf_counter() - t0

    sequential_time = sum(d for _, d in track_queries)
    print(f" Fetched {len(results)} tracks concurrently in: {elapsed:.3f}s")
    print(f" Sequential Equivalent would take:         {sequential_time:.3f}s")
    print(f" Concurrency Speedup:                      {sequential_time / elapsed:.2f}x 🚀")
    for r in results:
        print(f"   ✓ {r['track_id']}: {r['title']} ({r['frequency_hz']}Hz)")


# -------------------------------------------------------------------------
# 2. PYTHON 3.11+ STRUCTURED CONCURRENCY: asyncio.TaskGroup
# -------------------------------------------------------------------------
async def flaky_api_worker(name: str, should_fail: bool, delay: float) -> str:
    await asyncio.sleep(delay)
    if should_fail:
        raise ValueError(f"CRITICAL: Service {name} failed with 503 Service Unavailable!")
    return f"Service {name} completed successfully."


async def demonstrate_task_group_success():
    print("\n" + "=" * 70)
    print("🛡️ 2. STRUCTURED CONCURRENCY: asyncio.TaskGroup (Clean Execution)")
    print("=" * 70)

    results = []
    # In Python 3.11+, TaskGroup is the recommended, leak-proof way to spawn tasks!
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_meditation_metadata("TG-01", 0.10))
        task2 = tg.create_task(fetch_meditation_metadata("TG-02", 0.15))
        task3 = tg.create_task(fetch_meditation_metadata("TG-03", 0.08))

    # Once the context manager exits, ALL tasks are guaranteed completed!
    results = [task1.result(), task2.result(), task3.result()]
    print(f" All {len(results)} TaskGroup tasks finished cleanly!")
    for r in results:
        print(f"   ✓ {r['track_id']} -> {r['status']}")


async def demonstrate_task_group_failure():
    print("\n" + "=" * 70)
    print("💥 3. TaskGroup AUTOMATIC CANCELLATION & ExceptionGroup")
    print("=" * 70)

    try:
        async with asyncio.TaskGroup() as tg:
            # Task 1 will take long
            tg.create_task(flaky_api_worker("PaymentGateway", should_fail=False, delay=1.0))
            # Task 2 fails quickly
            tg.create_task(flaky_api_worker("InventoryService", should_fail=True, delay=0.10))
            # Task 3 is also queued
            tg.create_task(flaky_api_worker("NotificationService", should_fail=False, delay=0.50))
    except* ValueError as eg:
        # Python 3.11+ except* syntax catches specific sub-exceptions from ExceptionGroup!
        print(" [CAUGHT BY except*]: Sub-exception cleanly intercepted!")
        for exc in eg.exceptions:
            print(f"   ❌ Caught Exception: {exc}")
        print(" ✅ Notice: Task 1 and Task 3 were automatically cancelled! Zero orphan tasks left behind.")


# -------------------------------------------------------------------------
# 3. MODERN ASYNC TIMEOUTS: asyncio.timeout()
# -------------------------------------------------------------------------
async def slow_upstream_database(delay: float) -> str:
    await asyncio.sleep(delay)
    return "Database query payload"


async def demonstrate_timeouts():
    print("\n" + "=" * 70)
    print("⏱️ 4. RESILIENT DEADLINES WITH asyncio.timeout()")
    print("=" * 70)

    # 1. Successful within deadline
    try:
        async with asyncio.timeout(0.5):
            res = await slow_upstream_database(delay=0.15)
            print(f" [1] Query succeeded within deadline: '{res}'")
    except TimeoutError:
        print(" [1] Query timed out!")

    # 2. Exceeding deadline
    try:
        async with asyncio.timeout(0.20):
            print(" [2] Querying slow upstream server with 200ms timeout...")
            await slow_upstream_database(delay=0.80)
    except TimeoutError:
        print(" [2] 🛡️ TimeoutError caught! Upstream query took >200ms. Fast failure guaranteed.")


# -------------------------------------------------------------------------
# 4. BRIDGING BLOCKING SYNCHRONOUS CODE: asyncio.to_thread()
# -------------------------------------------------------------------------
def heavy_legacy_crypto_calc(secret: str) -> str:
    """Synchronous CPU/disk function that blocks the thread."""
    time.sleep(0.10)
    return f"HASH_{abs(hash(secret)):x}"


async def demonstrate_to_thread():
    print("\n" + "=" * 70)
    print("🌉 5. BRIDGING BLOCKING SYNC CODE WITH asyncio.to_thread()")
    print("=" * 70)

    # Offloads heavy_legacy_crypto_calc to a background worker thread
    # so the async event loop NEVER freezes!
    t0 = time.perf_counter()
    hashed = await asyncio.to_thread(heavy_legacy_crypto_calc, "client_secret_key_12345")
    elapsed = time.perf_counter() - t0
    print(f" Non-blocking async bridge completed in {elapsed:.3f}s: {hashed}")


# -------------------------------------------------------------------------
# MAIN SUITE RUNNER
# -------------------------------------------------------------------------
async def main():
    print("🚀 Running Day 20 - Module 03: AsyncIO & Structured Concurrency")
    await demonstrate_gather()
    await demonstrate_task_group_success()
    await demonstrate_task_group_failure()
    await demonstrate_timeouts()
    await demonstrate_to_thread()
    print("\n🎉 Module 03 AsyncIO Architecture Suite Completed Successfully!\n")


if __name__ == "__main__":
    asyncio.run(main())

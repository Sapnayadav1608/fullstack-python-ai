"""
Day 20 — Module 01: Concurrency vs Parallelism & The CPython GIL Benchmark
==========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Key Concepts Covered:
1. Concurrency (interleaving tasks on 1 core) vs Parallelism (executing simultaneously on multiple cores).
2. The CPython Global Interpreter Lock (GIL):
   - What it is: A mutual exclusion lock that prevents multiple native threads from executing
     Python bytecodes at once.
   - Why it exists: CPython memory management is not thread-safe (reference counting `Py_INCREF`/`Py_DECREF`).
   - The Consequence: Threads DO NOT speed up CPU-bound tasks in standard CPython.
3. CPU-Bound Tasks vs I/O-Bound Tasks:
   - CPU-Bound: Number crunching, image processing, cryptography, ML tensor math.
     -> Solution: Multiprocessing (`ProcessPoolExecutor`) to bypass the GIL across CPU cores.
   - I/O-Bound: Network requests, disk I/O, database queries, LLM API streaming.
     -> Solution: Multithreading (`ThreadPoolExecutor`) or Asynchronous I/O (`asyncio`).
4. Live Benchmark & Verification:
   - Sequential vs Multi-threaded vs Multi-process execution comparison.
"""

import os
import sys
import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# -------------------------------------------------------------------------
# 1. CPU-BOUND WORKLOAD (Number Crunching)
# -------------------------------------------------------------------------
def heavy_cpu_task(n: int) -> int:
    """Simulates intensive CPU computation: finding count of primes up to n."""
    count = 0
    for i in range(2, n):
        is_prime = True
        limit = int(math.isqrt(i)) + 1
        for j in range(2, limit):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


# -------------------------------------------------------------------------
# 2. I/O-BOUND WORKLOAD (Simulated Network Latency / API Calls)
# -------------------------------------------------------------------------
def simulated_network_fetch(endpoint_id: int) -> dict:
    """
    Simulates fetching a meditation audio track from a cloud bucket.
    time.sleep releases the CPython GIL, allowing other threads to run!
    """
    time.sleep(0.15)  # 150ms simulated network RTT
    return {
        "track_id": endpoint_id,
        "title": f"Deep Delta Wave #{endpoint_id}",
        "status": 200,
        "duration": "15:00"
    }


# -------------------------------------------------------------------------
# 3. BENCHMARK RUNNERS
# -------------------------------------------------------------------------
def benchmark_cpu_bound():
    print("\n" + "=" * 70)
    print("🔥 BENCHMARK 1: CPU-BOUND WORKLOAD (Finding Primes)")
    print("=" * 70)
    targets = [35000, 35000, 35000, 35000]
    num_tasks = len(targets)

    # 1. Sequential Execution
    t0 = time.perf_counter()
    seq_results = [heavy_cpu_task(n) for n in targets]
    t_seq = time.perf_counter() - t0
    print(f" [1] Sequential Execution:        {t_seq:.4f}s  (Baseline 1x)")

    # 2. Multithreading (GIL Bottleneck!)
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=num_tasks) as pool:
        thread_results = list(pool.map(heavy_cpu_task, targets))
    t_thread = time.perf_counter() - t0
    slowdown_pct = ((t_thread - t_seq) / t_seq) * 100
    print(f" [2] Multithreading (4 Threads):    {t_thread:.4f}s  (GIL Overhead: {slowdown_pct:+.1f}%)")
    print("     ⚠️ Notice: Threads do NOT speed up CPU-bound code due to the CPython GIL!")

    # 3. Multiprocessing (Bypassing GIL via Separate OS Processes)
    t0 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=num_tasks) as pool:
        process_results = list(pool.map(heavy_cpu_task, targets))
    t_proc = time.perf_counter() - t0
    speedup = t_seq / max(t_proc, 0.0001)
    print(f" [3] Multiprocessing (4 Processes): {t_proc:.4f}s  (True Speedup: {speedup:.2f}x 🔥)")
    print("     ✅ True Parallelism across physical CPU cores!")

    assert seq_results == thread_results == process_results


def benchmark_io_bound():
    print("\n" + "=" * 70)
    print("🌐 BENCHMARK 2: I/O-BOUND WORKLOAD (Simulated Network Downloads)")
    print("=" * 70)
    task_ids = list(range(1, 9))  # 8 network calls, 150ms each

    # 1. Sequential Execution
    t0 = time.perf_counter()
    seq_res = [simulated_network_fetch(tid) for tid in task_ids]
    t_seq = time.perf_counter() - t0
    print(f" [1] Sequential I/O (8 requests):  {t_seq:.4f}s  (8 x 0.15s = ~1.2s)")

    # 2. Multithreaded Execution (GIL Released during I/O!)
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=8) as pool:
        thread_res = list(pool.map(simulated_network_fetch, task_ids))
    t_thread = time.perf_counter() - t0
    speedup = t_seq / max(t_thread, 0.0001)
    print(f" [2] Multithreaded I/O (8 workers): {t_thread:.4f}s  (Speedup: {speedup:.2f}x 🚀)")
    print("     ✅ Because I/O releases the GIL, threads provide massive concurrency speedup!")

    assert len(seq_res) == len(thread_res) == 8


# -------------------------------------------------------------------------
# 4. ARCHITECTURAL DECISION MATRIX
# -------------------------------------------------------------------------
def display_decision_matrix():
    print("\n" + "=" * 70)
    print("📋 ARCHITECTURAL DECISION MATRIX: THREADS vs PROCESSES vs ASYNCIO")
    print("=" * 70)
    matrix = [
        ("Task Type", "Primary Bottleneck", "Recommended Tool", "Memory Overhead", "GIL Impact"),
        ("Heavy Math / ML", "CPU Cores", "multiprocessing", "High (Forked RAM)", "Bypassed (True Parallel)"),
        ("File I/O / Legacy DB", "Disk / Driver", "ThreadPoolExecutor", "Medium (~8MB/thread)", "Released during I/O"),
        ("10K Web Requests / APIs", "Network Sockets", "asyncio (Event Loop)", "Ultra-Low (Bytes)", "Single-threaded reactor"),
        ("Full-Stack FastAPI Web", "I/O Concurrency", "async / await", "Minimal", "Non-blocking")
    ]
    for row in matrix:
        print(f" {row[0]:<23} | {row[1]:<16} | {row[2]:<21} | {row[3]:<17}")
    print("=" * 70)


if __name__ == "__main__":
    print("🚀 Running Day 20 - Module 01: GIL & Concurrency Architecture")
    display_decision_matrix()
    benchmark_cpu_bound()
    benchmark_io_bound()
    print("\n🎉 Module 01 Execution & Benchmarks Completed Successfully!\n")

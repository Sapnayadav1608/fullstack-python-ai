"""
Day 20: Concurrency, Threading & AsyncIO — Hands-on Practice Workbook
=====================================================================
30-Day Full Stack Python + AI Engineering Challenge

Complete all 6 challenges below. Each challenge is equipped with an automated
unit test to verify correctness, thread safety, and concurrency performance.

Run tests via:
    python my_practice.py
"""

import sys
import time
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Optional, AsyncGenerator

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# =========================================================================
# CHALLENGE 1: Thread-Safe Atomic Metrics Collector (threading.Lock)
# =========================================================================
class ThreadSafeMetrics:
    """
    Challenge 1:
    Implement a thread-safe metrics aggregator for tracking client web requests.
    Multiple threads will concurrently call increment(metric_name, value).
    You must protect the internal dictionary with a threading.Lock to eliminate race conditions.
    """
    def __init__(self):
        self._metrics: Dict[str, int] = {}
        self._lock = threading.Lock()

    def increment(self, metric_name: str, value: int = 1) -> None:
        """Atomically increments the given metric by value."""
        with self._lock:
            self._metrics[metric_name] = self._metrics.get(metric_name, 0) + value

    def get(self, metric_name: str) -> int:
        """Thread-safely returns the current count for metric_name (0 if non-existent)."""
        with self._lock:
            return self._metrics.get(metric_name, 0)

    def get_all(self) -> Dict[str, int]:
        """Returns a copy of all metrics."""
        with self._lock:
            return dict(self._metrics)


# =========================================================================
# CHALLENGE 2: Parallel I/O Asset Batch Downloader (ThreadPoolExecutor)
# =========================================================================
def mock_download_file(file_url: str, delay: float = 0.05) -> Dict[str, Any]:
    time.sleep(delay)
    return {"url": file_url, "size_kb": len(file_url) * 12, "status": "OK"}


def parallel_asset_downloader(file_urls: List[str], max_workers: int = 5) -> List[Dict[str, Any]]:
    """
    Challenge 2:
    Use concurrent.futures.ThreadPoolExecutor to download all file_urls concurrently.
    Preserve order or return list of all downloaded payloads.
    """
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(mock_download_file, url) for url in file_urls]
        for f in as_completed(futures):
            results.append(f.result())
    return sorted(results, key=lambda x: x["url"])


# =========================================================================
# CHALLENGE 3: Concurrent Async Fetcher (asyncio.gather)
# =========================================================================
async def async_fetch_track_info(track_id: str, delay: float = 0.05) -> Dict[str, Any]:
    await asyncio.sleep(delay)
    return {"track_id": track_id, "ready": True}


async def async_batch_metadata_fetcher(track_ids: List[str], delay_per_item: float = 0.05) -> List[Dict[str, Any]]:
    """
    Challenge 3:
    Use asyncio.gather() to fetch track info for all track_ids concurrently.
    All items must execute non-blockingly on the event loop.
    """
    tasks = [async_fetch_track_info(tid, delay=delay_per_item) for tid in track_ids]
    return await asyncio.gather(*tasks)


# =========================================================================
# CHALLENGE 4: Modern TaskGroup with Error Shielding (Python 3.11+)
# =========================================================================
async def flaky_worker(task_id: str, should_fail: bool) -> str:
    await asyncio.sleep(0.02)
    if should_fail:
        raise ValueError(f"Task {task_id} failed!")
    return f"Task {task_id} OK"


async def resilient_taskgroup_executor(task_specs: List[tuple[str, bool]]) -> Dict[str, Any]:
    """
    Challenge 4:
    Execute task_specs [(task_id, should_fail), ...] using asyncio.TaskGroup().
    Handle ExceptionGroup gracefully using except* or try/except ExceptionGroup
    and return a summary: {"succeeded": [...], "failed_errors": [...]}
    """
    succeeded = []
    failed_errors = []

    # To isolate failures inside a TaskGroup so one task doesn't cancel others,
    # wrap each task inside an inner safe executor
    async def safe_run(tid: str, fail: bool):
        try:
            res = await flaky_worker(tid, fail)
            succeeded.append(res)
        except Exception as e:
            failed_errors.append(str(e))

    async with asyncio.TaskGroup() as tg:
        for tid, fail in task_specs:
            tg.create_task(safe_run(tid, fail))

    return {
        "succeeded": sorted(succeeded),
        "failed_errors": sorted(failed_errors)
    }


# =========================================================================
# CHALLENGE 5: Async Token Stream Accumulator (async for)
# =========================================================================
async def mock_token_generator(tokens: List[str]) -> AsyncGenerator[str, None]:
    for t in tokens:
        await asyncio.sleep(0.01)
        yield t


async def async_stream_collector(token_stream: AsyncGenerator[str, None]) -> Dict[str, Any]:
    """
    Challenge 5:
    Consume an asynchronous generator using `async for`.
    Join all tokens into a single text string, count tokens, and return:
    {"full_text": str, "token_count": int}
    """
    collected = []
    async for token in token_stream:
        collected.append(token)
    return {
        "full_text": "".join(collected),
        "token_count": len(collected)
    }


# =========================================================================
# CHALLENGE 6: Concurrency Throttling with Semaphore (asyncio.Semaphore)
# =========================================================================
class ThrottledAPIClient:
    """
    Challenge 6:
    Implement an API client that uses an asyncio.Semaphore to guarantee that
    no more than max_concurrent requests are active at any single moment.
    """
    def __init__(self, max_concurrent: int):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.max_concurrent = max_concurrent
        self.current_active = 0
        self.max_seen_active = 0

    async def call_api(self, query: str) -> str:
        async with self.semaphore:
            self.current_active += 1
            if self.current_active > self.max_seen_active:
                self.max_seen_active = self.current_active

            # Artificial delay simulating API call
            await asyncio.sleep(0.03)

            self.current_active -= 1
            return f"Result for {query}"


# =========================================================================
# AUTOMATED TEST SUITE (6/6 TESTS)
# =========================================================================
def test_challenge_1():
    print("▶ Testing Challenge 1: Thread-Safe Metrics Collector...")
    metrics = ThreadSafeMetrics()
    NUM_THREADS = 50
    INCS_PER_THREAD = 100

    def worker():
        for _ in range(INCS_PER_THREAD):
            metrics.increment("page_views", 1)
            metrics.increment("audio_plays", 2)

    threads = [threading.Thread(target=worker) for _ in range(NUM_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert metrics.get("page_views") == NUM_THREADS * INCS_PER_THREAD
    assert metrics.get("audio_plays") == NUM_THREADS * INCS_PER_THREAD * 2
    assert metrics.get("non_existent") == 0
    print("  ✓ Challenge 1 Passed! Zero race conditions across 50 concurrent threads.")


def test_challenge_2():
    print("▶ Testing Challenge 2: Parallel Asset Downloader...")
    urls = [f"https://cdn.mindifestation.com/audio/track_{i}.mp3" for i in range(1, 9)]
    t0 = time.perf_counter()
    results = parallel_asset_downloader(urls, max_workers=4)
    elapsed = time.perf_counter() - t0

    assert len(results) == 8
    # 8 tasks with 0.05s delay on 4 workers should take ~0.10s, definitely < 0.25s
    assert elapsed < 0.30
    print(f"  ✓ Challenge 2 Passed! Parallel execution finished in {elapsed:.3f}s (<0.30s).")


def test_challenge_3():
    print("▶ Testing Challenge 3: Async Batch Metadata Fetcher...")
    track_ids = [f"TRK-{i:03d}" for i in range(1, 11)]

    async def run():
        t0 = time.perf_counter()
        res = await async_batch_metadata_fetcher(track_ids, delay_per_item=0.04)
        elapsed = time.perf_counter() - t0
        return res, elapsed

    results, elapsed = asyncio.run(run())
    assert len(results) == 10
    # 10 tasks of 0.04s executed concurrently should take ~0.04s - 0.08s (not 0.40s)
    assert elapsed < 0.15
    print(f"  ✓ Challenge 3 Passed! 10 async tasks finished in {elapsed:.3f}s (<0.15s).")


def test_challenge_4():
    print("▶ Testing Challenge 4: Modern TaskGroup with Error Shielding...")
    specs = [
        ("T1", False),
        ("T2", True),
        ("T3", False),
        ("T4", True),
        ("T5", False)
    ]
    summary = asyncio.run(resilient_taskgroup_executor(specs))
    assert len(summary["succeeded"]) == 3
    assert len(summary["failed_errors"]) == 2
    print("  ✓ Challenge 4 Passed! TaskGroup isolated failures and captured all errors cleanly.")


def test_challenge_5():
    print("▶ Testing Challenge 5: Async Token Stream Accumulator...")
    sample_tokens = ["Focus ", "your ", "mind, ", "expand ", "your ", "reality."]

    async def run():
        generator = mock_token_generator(sample_tokens)
        return await async_stream_collector(generator)

    result = asyncio.run(run())
    assert result["full_text"] == "Focus your mind, expand your reality."
    assert result["token_count"] == 6
    print("  ✓ Challenge 5 Passed! Streamed 6 tokens seamlessly via async for.")


def test_challenge_6():
    print("▶ Testing Challenge 6: Concurrency Throttling with Semaphore...")
    client = ThrottledAPIClient(max_concurrent=3)
    queries = [f"query_{i}" for i in range(9)]

    async def run():
        tasks = [client.call_api(q) for q in queries]
        return await asyncio.gather(*tasks)

    results = asyncio.run(run())
    assert len(results) == 9
    assert client.max_seen_active <= 3
    assert client.current_active == 0
    print(f"  ✓ Challenge 6 Passed! Peak concurrency never exceeded 3 (peak: {client.max_seen_active}).")


def run_all_tests():
    print("=" * 70)
    print("🧪 RUNNING DAY 20 AUTOMATED PRACTICE TEST SUITE")
    print("=" * 70)
    test_challenge_1()
    test_challenge_2()
    test_challenge_3()
    test_challenge_4()
    test_challenge_5()
    test_challenge_6()
    print("=" * 70)
    print("🎉 ALL 6/6 PRACTICE CHALLENGES PASSED WITH ZERO ERRORS!")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()

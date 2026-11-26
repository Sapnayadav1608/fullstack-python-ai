"""
Day 20 — Module 04: Advanced AsyncIO Patterns & Streaming AI Engineering
=======================================================================
30-Day Full Stack Python + AI Engineering Challenge

Key Concepts Covered:
1. Asynchronous Context Managers (`async with`):
   - Implementing `__aenter__` and `__aexit__` protocols.
   - Real-world case study: `AsyncDatabasePoolSession` for non-blocking database transactions.
2. Asynchronous Iterators & Generators (`async for`):
   - The foundation of LLM Token Streaming (e.g. Gemini, OpenAI, Claude streaming responses).
   - Memory efficiency: Processing infinite or massive token streams one chunk at a time.
3. Producer-Consumer Decoupled Architecture (`asyncio.Queue`):
   - Decoupling API ingestion from background worker processing.
   - Managing worker pools with `queue.put()`, `queue.get()`, `queue.task_done()`, and `queue.join()`.
4. Concurrency Throttling with `asyncio.Semaphore`:
   - Protecting third-party AI APIs from HTTP 429 "Too Many Requests".
   - Limiting concurrent requests to safe thresholds (e.g. max 3 concurrent calls).
"""

import sys
import asyncio
import time
import random
from typing import AsyncGenerator, List, Dict, Any

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# -------------------------------------------------------------------------
# 1. ASYNCHRONOUS CONTEXT MANAGERS: AsyncDatabaseSession
# -------------------------------------------------------------------------
class AsyncDatabaseSession:
    """
    Simulates a non-blocking asynchronous database connection pool session.
    Implements the __aenter__ and __aexit__ asynchronous context protocol.
    """
    def __init__(self, connection_id: str):
        self.connection_id = connection_id
        self.is_connected = False
        self.in_transaction = False

    async def __aenter__(self):
        # Simulate non-blocking socket acquisition
        await asyncio.sleep(0.05)
        self.is_connected = True
        self.in_transaction = True
        # print(f"    [Pool] Acquired connection {self.connection_id} and started transaction.")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Rollback transaction on failure
            await asyncio.sleep(0.02)
            self.in_transaction = False
            # print(f"    [Pool] ⚠️ Exception caught ({exc_type.__name__})! Rolled back transaction {self.connection_id}.")
        else:
            # Commit transaction on success
            await asyncio.sleep(0.02)
            self.in_transaction = False
            # print(f"    [Pool] ✓ Committed transaction {self.connection_id}.")
        self.is_connected = False
        return False  # Propagate exception if any

    async def execute_query(self, query: str) -> Dict[str, Any]:
        if not self.in_transaction:
            raise RuntimeError("Cannot execute query without active transaction!")
        await asyncio.sleep(0.05)
        return {"query": query, "status": "COMMITTED", "connection": self.connection_id}


async def test_async_context_manager():
    print("\n" + "=" * 70)
    print("🔒 1. ASYNCHRONOUS CONTEXT MANAGER (__aenter__ / __aexit__)")
    print("=" * 70)

    async with AsyncDatabaseSession("conn_pool_01") as session:
        result = await session.execute_query("SELECT * FROM meditation_tracks WHERE category = 'deep_sleep'")
        print(f" Session Query Execution Result: {result}")

    print(" ✅ Database connection automatically closed and committed!")


# -------------------------------------------------------------------------
# 2. ASYNC GENERATORS: LLM TOKEN STREAMING (AI FOUNDATION)
# -------------------------------------------------------------------------
async def stream_ai_affirmation_generator(prompt: str) -> AsyncGenerator[str, None]:
    """
    Simulates streaming tokens from an AI Language Model (Gemini / OpenAI).
    Yields tokens asynchronously with realistic token-per-second cadence.
    """
    sample_tokens = [
        "In ", "the ", "depths ", "of ", "silence, ",
        "you ", "find ", "infinite ", "strength. ",
        "Your ", "mind ", "is ", "calm, ",
        "your ", "purpose ", "is ", "clear, ",
        "and ", "abundance ", "flows ", "naturally. "
    ]
    for token in sample_tokens:
        await asyncio.sleep(0.06)  # ~16 tokens/sec LLM streaming delay
        yield token


async def test_async_streaming_generator():
    print("\n" + "=" * 70)
    print("🤖 2. ASYNC GENERATOR (LLM TOKEN STREAMING FOR AI APPLICATIONS)")
    print("=" * 70)
    print(" [AI Stream Prompt]: 'Generate daily morning affirmation'")
    sys.stdout.write(" [Live Stream Output]: ")
    sys.stdout.flush()

    token_count = 0
    t0 = time.perf_counter()
    async for token in stream_ai_affirmation_generator("daily_affirmation"):
        sys.stdout.write(token)
        sys.stdout.flush()
        token_count += 1
    total_time = time.perf_counter() - t0

    print(f"\n   ✓ Streamed {token_count} tokens in {total_time:.2f}s ({token_count / total_time:.1f} tokens/sec)")


# -------------------------------------------------------------------------
# 3. PRODUCER-CONSUMER QUEUE WITH asyncio.Queue
# -------------------------------------------------------------------------
async def payment_producer(queue: asyncio.Queue, count: int):
    """Generates client payment webhook events asynchronously."""
    for i in range(1, count + 1):
        event = {
            "order_id": f"ORD-2026-{1000 + i}",
            "amount_inr": 499.0 + (i * 100),
            "customer": f"user_{i}@mindifestation.com"
        }
        await queue.put(event)
        # print(f"  [Producer] Enqueued {event['order_id']}")
        await asyncio.sleep(0.02)


async def payment_consumer_worker(worker_id: str, queue: asyncio.Queue, processed_list: list):
    """Background worker processing payment verification & database writes."""
    while True:
        event = await queue.get()
        try:
            # Simulate I/O work (verifying UTR & activating subscription)
            await asyncio.sleep(0.05)
            processed_list.append(event["order_id"])
        finally:
            queue.task_done()


async def test_producer_consumer_queue():
    print("\n" + "=" * 70)
    print("📦 3. PRODUCER-CONSUMER QUEUE (asyncio.Queue Worker Pool)")
    print("=" * 70)

    queue = asyncio.Queue(maxsize=20)
    processed_orders = []
    TOTAL_ORDERS = 10
    NUM_WORKERS = 3

    # Launch consumer worker pool
    workers = []
    for i in range(NUM_WORKERS):
        w = asyncio.create_task(payment_consumer_worker(f"Worker-{i+1}", queue, processed_orders))
        workers.append(w)

    t0 = time.perf_counter()
    # Run producer to enqueue orders
    await payment_producer(queue, TOTAL_ORDERS)

    # Wait until all items in the queue have been fully processed
    await queue.join()
    elapsed = time.perf_counter() - t0

    # Cancel background daemon workers
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)

    print(f" Successfully processed {len(processed_orders)}/{TOTAL_ORDERS} orders across {NUM_WORKERS} workers in {elapsed:.3f}s!")
    assert len(processed_orders) == TOTAL_ORDERS


# -------------------------------------------------------------------------
# 4. CONCURRENCY THROTTLING: asyncio.Semaphore (Rate Limiter)
# -------------------------------------------------------------------------
async def call_external_ai_api(item_id: int, semaphore: asyncio.Semaphore, active_counter: list) -> str:
    """
    Simulates calling an expensive AI inference endpoint (Gemini / Anthropic).
    Uses a Semaphore to ensure no more than N concurrent calls hit the server.
    """
    async with semaphore:
        active_counter[0] += 1
        current_active = active_counter[0]
        # Invariant check: active calls must never exceed semaphore limit (3)
        assert current_active <= 3, f"Rate limit breach: {current_active} active!"
        # print(f"    [Semaphore] Acquired slot for item #{item_id} (Currently Active: {current_active})")
        await asyncio.sleep(0.08)  # Network latency
        active_counter[0] -= 1
        return f"AI_RESPONSE_{item_id}"


async def test_concurrency_semaphore():
    print("\n" + "=" * 70)
    print("🚥 4. RATE LIMITING WITH asyncio.Semaphore (Max 3 Concurrent API Calls)")
    print("=" * 70)

    MAX_CONCURRENT = 3
    TOTAL_REQUESTS = 9
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    active_tracker = [0]  # mutable integer wrapper for verification

    t0 = time.perf_counter()
    tasks = [call_external_ai_api(i, semaphore, active_tracker) for i in range(1, TOTAL_REQUESTS + 1)]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - t0

    print(f" Completed {len(results)} API calls with max 3 concurrent threads in {elapsed:.3f}s.")
    print(" ✅ Concurrency strictly respected: Zero 429 rate limit errors!")


# -------------------------------------------------------------------------
# MAIN SUITE RUNNER
# -------------------------------------------------------------------------
async def main():
    print("🚀 Running Day 20 - Module 04: Advanced Async Patterns & AI Streaming")
    await test_async_context_manager()
    await test_async_streaming_generator()
    await test_producer_consumer_queue()
    await test_concurrency_semaphore()
    print("\n🎉 Module 04 Advanced Async Suite Completed Successfully!\n")


if __name__ == "__main__":
    asyncio.run(main())

"""
Day 13: Python Iterators & The Iteration Protocol
Module 02: Generators, `yield`, and Memory Optimization (O(1) vs O(N) RAM)
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Generator Functions: How `yield` pauses execution and freezes stack frames.
2. Generator Lifecycle & CPython States (inspect.getgeneratorstate).
3. Generator Expressions `(...)` vs List Comprehensions `[...]`.
4. Live Memory Benchmark: 10,000,000 items (80+ Megabytes List vs 104 Bytes Generator).
5. Infinite Data Generators (Streaming Fibonacci & Sensor Streams).
6. Real-World AI Pattern: Chunked Big-Data Streaming to prevent OOM (Out Of Memory).
"""

import sys
import inspect
import tracemalloc
from typing import Generator, Iterator


# ============================================================================
# 1. HOW `yield` WORKS: SUSPENDING EXECUTION & FREEZING FRAMES
# ============================================================================
"""
REGULAR FUNCTION vs GENERATOR FUNCTION:
- Regular function: Uses `return`. When called, runs to completion, destroys its
  local stack frame, and returns a single value.
- Generator function: Contains the `yield` keyword. When called, does NOT execute!
  Instead, it immediately returns a `generator` object.
  Execution only starts when `next()` is called.
  When Python hits `yield x`, it returns `x`, FREEZES all local variables and the
  instruction pointer, and yields control back to the caller.
  Subsequent `next()` calls resume immediately from the exact instruction after `yield`.
"""

print("=" * 70)
print("1. GENERATOR FUNCTION STEP-BY-STEP EXECUTION")
print("=" * 70)

def step_by_step_generator() -> Generator[str, None, None]:
    print("  [Gen Engine] Start execution...")
    yield "Checkpoint Alpha"
    print("  [Gen Engine] Resuming between Alpha & Beta...")
    yield "Checkpoint Beta"
    print("  [Gen Engine] Resuming between Beta & Gamma...")
    yield "Checkpoint Gamma"
    print("  [Gen Engine] Finishing up...")

# Calling the function only creates the generator object
gen = step_by_step_generator()
print(f"Object created without running: {gen}")
print(f"Is generator an iterator? {isinstance(gen, Iterator)}")

print("\nCalling next():")
print(f"-> Returned: {next(gen)}")
print(f"-> Returned: {next(gen)}")
print(f"-> Returned: {next(gen)}")

try:
    print(f"-> Returned: {next(gen)}")
except StopIteration:
    print("-> Caught StopIteration! Generator has closed its frame.")


# ============================================================================
# 2. GENERATOR LIFECYCLE & CPYTHON INTERNAL STATES
# ============================================================================
"""
A generator object in CPython moves through 4 distinct states:
1. GEN_CREATED:   Created, but next() has never been called yet.
2. GEN_RUNNING:   Currently being executed by the Python interpreter.
3. GEN_SUSPENDED: Paused at a `yield` expression; frame frozen in memory.
4. GEN_CLOSED:    Finished (raised StopIteration) or closed explicitly via .close().
"""

print("\n" + "=" * 70)
print("2. CPYTHON GENERATOR STATE TRANSITIONS")
print("=" * 70)

def lifecycle_tracker() -> Generator[int, None, None]:
    yield 100
    yield 200

g = lifecycle_tracker()
print(f"1. Before first next(): {inspect.getgeneratorstate(g)}")   # GEN_CREATED

next(g)
print(f"2. Paused at yield:     {inspect.getgeneratorstate(g)}")   # GEN_SUSPENDED

next(g)
print(f"3. After final yield:   {inspect.getgeneratorstate(g)}")   # GEN_SUSPENDED

try:
    next(g)
except StopIteration:
    pass
print(f"4. Exhausted / Closed:  {inspect.getgeneratorstate(g)}")   # GEN_CLOSED


# ============================================================================
# 3. GENERATOR EXPRESSIONS VS LIST COMPREHENSIONS
# ============================================================================
"""
Syntax Difference:
- List Comprehension:   `[x * 2 for x in data]`  -> Computes eagerly, stores all in RAM.
- Generator Expression: `(x * 2 for x in data)`  -> Computes lazily, evaluates on demand.
"""

print("\n" + "=" * 70)
print("3. GENERATOR EXPRESSIONS: LAZY VS EAGER")
print("=" * 70)

limit = 10
eager_list = [x ** 2 for x in range(limit)]
lazy_gen = (x ** 2 for x in range(limit))

print(f"List Comprehension:   {eager_list}")
print(f"Generator Expression: {lazy_gen}")
print(f"First 3 from gen:     {[next(lazy_gen) for _ in range(3)]}")


# ============================================================================
# 4. LIVE MEMORY BENCHMARK: 10,000,000 ITEMS (O(1) VS O(N) RAM)
# ============================================================================
"""
Why does FAANG ask about Generators?
Because loading 10M records into memory will crash production microservices with
an Out-Of-Memory (OOM) error.
Generators process 10M records in constant O(1) RAM!
"""

print("\n" + "=" * 70)
print("4. LIVE MEMORY BENCHMARK: 10 MILLION ITEMS")
print("=" * 70)

N = 10_000_000

# 1. Inspect shallow object size with sys.getsizeof
gen_expr = (x * 2 for x in range(N))
print(f"Generator Expression sys.getsizeof: {sys.getsizeof(gen_expr)} bytes  (Constant O(1)!)")

# 2. Benchmark actual allocated heap memory using tracemalloc
print("\nMeasuring Heap Allocation for N = 1,000,000 integers:")
TEST_N = 1_000_000

# A. Measure List Memory
tracemalloc.start()
eager_data = [x * 2 for x in range(TEST_N)]
current, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()

# B. Measure Generator Memory
tracemalloc.start()
lazy_data = (x * 2 for x in range(TEST_N))
# Consume 10,000 elements to prove it's actively processing
sample_sum = sum(next(lazy_data) for _ in range(10_000))
current, peak_gen = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"  - List Comprehension Peak RAM: {peak_list / (1024 * 1024):.2f} MB")
print(f"  - Generator Expression Peak RAM: {peak_gen / 1024:.2f} KB")
ratio = peak_list / max(peak_gen, 1)
print(f"  ==> Generator uses ~{ratio:,.0f}x LESS RAM than List!")


# ============================================================================
# 5. INFINITE GENERATORS: MATHEMATICAL STREAMS
# ============================================================================
"""
Because generators are lazy, they can effortlessly represent INFINITE sequences!
A list cannot do this because it would take infinite memory and lock the computer.
"""

print("\n" + "=" * 70)
print("5. INFINITE FIBONACCI GENERATOR")
print("=" * 70)

def infinite_fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_stream = infinite_fibonacci()
first_12_fibs = [next(fib_stream) for _ in range(12)]
print(f"First 12 Fibonacci numbers generated on-demand: {first_12_fibs}")


# ============================================================================
# 6. PRODUCTION PATTERN: MASSIVE DATASET STREAMING (AI/DATA PIPELINES)
# ============================================================================
"""
Simulating reading a massive 50 GB log file or AI training corpus without
reading the entire file into memory at once.
"""

print("\n" + "=" * 70)
print("6. CHUNKED STREAMING AI LOG ANALYZER")
print("=" * 70)

def mock_ai_log_stream(total_records: int) -> Generator[dict, None, None]:
    """Generates synthetic high-volume inference logs one record at a time."""
    for record_id in range(1, total_records + 1):
        yield {
            "request_id": f"req_{record_id:06d}",
            "latency_ms": 15 + (record_id % 45),
            "status": "SUCCESS" if record_id % 7 != 0 else "ERROR_RATE_LIMIT"
        }

# Stream through 100,000 records, calculating error rates in O(1) memory!
error_count = 0
total_streamed = 0

for log in mock_ai_log_stream(100_000):
    total_streamed += 1
    if log["status"] != "SUCCESS":
        error_count += 1
    if total_streamed <= 5:
        # Show first 5 records as preview
        print(f"  Sample Log [{log['request_id']}]: latency={log['latency_ms']}ms, status={log['status']}")

print(f"\nStreamed {total_streamed:,} logs in O(1) RAM. Total Rate-Limit Errors: {error_count:,}")

print("\n" + "=" * 70)
print("DAY 13 MODULE 02: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

"""
Day 13: Python Iterators & The Iteration Protocol
Module 03: Advanced Generator Pipelines, `yield from`, and AI Token Streaming
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Composable Generator Pipelines (Unix pipe architecture in pure Python).
2. Sub-generator Delegation with `yield from` (Recursive flattening & delegation).
3. Coroutines & Bidirectional Generators: `.send()`, `.throw()`, and `.close()`.
4. Production AI Pattern: Live LLM Token Streaming Engine (Simulating ChatGPT/Gemini API).
"""

import time
from typing import Generator, Iterable, Any, List


# ============================================================================
# 1. COMPOSABLE GENERATOR PIPELINES (UNIX-STYLE DATA FLOW)
# ============================================================================
"""
In production backend engineering, we process massive streams of data without
ever storing intermediate steps in memory.
We chain generators together like Unix pipes:
    Raw Data Source -> Clean/Parse -> Filter -> Aggregate / Compute
Every single item flows through the entire pipeline individually in O(1) RAM!
"""

print("=" * 70)
print("1. COMPOSABLE GENERATOR PIPELINES")
print("=" * 70)

def generate_raw_sensor_readings(count: int) -> Generator[str, None, None]:
    """Stage 1: Producer - Generates raw CSV-like sensor lines."""
    for i in range(1, count + 1):
        temp = 20.0 + (i * 1.5) % 30
        status = "OK" if i % 4 != 0 else "MALFUNCTION"
        yield f"SENSOR_01,{temp:.1f},{status}"

def parse_sensor_data(lines: Iterable[str]) -> Generator[dict, None, None]:
    """Stage 2: Transformer - Parses raw strings into typed dictionaries."""
    for line in lines:
        sensor_id, temp_str, status = line.split(",")
        yield {"sensor": sensor_id, "temp": float(temp_str), "status": status}

def filter_valid_readings(records: Iterable[dict]) -> Generator[dict, None, None]:
    """Stage 3: Filter - Drops malfunctions and extreme anomalies."""
    for r in records:
        if r["status"] == "OK" and r["temp"] < 45.0:
            yield r

# Chaining the stages together (Lazy Pipeline - Nothing executes yet!)
raw_stream = generate_raw_sensor_readings(12)
parsed_stream = parse_sensor_data(raw_stream)
valid_stream = filter_valid_readings(parsed_stream)

print("Streaming through 3-stage pipeline:")
for record in valid_stream:
    print(f"  Valid Reading: Sensor={record['sensor']} | Temp={record['temp']}°C")


# ============================================================================
# 2. SUB-GENERATOR DELEGATION WITH `yield from`
# ============================================================================
"""
The `yield from <iterable>` syntax was introduced in PEP 380:
1. It delegates value generation directly to another iterable or sub-generator.
2. It replaces clumsy nested loops like:
       for item in sub_generator:
           yield item
   with a single clean line:
       yield from sub_generator
3. It creates a transparent bidirectional channel for `.send()` and exceptions.
"""

print("\n" + "=" * 70)
print("2. SUB-GENERATOR DELEGATION & RECURSIVE FLATTENING WITH `yield from`")
print("=" * 70)

def deep_flatten(nested_data: Any) -> Generator[Any, None, None]:
    """
    Recursively flattens arbitrarily nested lists/tuples of any depth
    using `yield from` in elegant O(1) auxiliary space!
    """
    if isinstance(nested_data, (list, tuple)):
        for element in nested_data:
            yield from deep_flatten(element)
    else:
        yield nested_data

nested_ai_weights = [1.0, [2.5, 3.2, [4.8, 5.1]], [[6.4, 7.7], 8.9], 9.0]
flat_weights = list(deep_flatten(nested_ai_weights))
print(f"Deeply Nested Input: {nested_ai_weights}")
print(f"Flattened Output:    {flat_weights}")


# ============================================================================
# 3. BIDIRECTIONAL COROUTINES: .send(), .throw(), AND .close()
# ============================================================================
"""
Generators are not just data producers — they can also be data CONSUMERS!
- `val = yield output`: Yields `output` to caller AND receives `val` from `.send()`.
- `g.send(data)`: Resumes generator and injects `data` into the yield expression.
- `g.throw(Exc)`: Raises an exception at the yield point inside the generator.
- `g.close()`: Raises GeneratorExit to shut down the coroutine gracefully.
"""

print("\n" + "=" * 70)
print("3. BIDIRECTIONAL GENERATOR COROUTINE: RUNNING AVERAGE TRACKER")
print("=" * 70)

def running_averager() -> Generator[float, float, None]:
    """
    A stateful coroutine that receives numbers via .send() and yields
    the live cumulative average in O(1) RAM.
    """
    total = 0.0
    count = 0
    average = 0.0
    while True:
        # yield average to caller and receive incoming value via .send()
        val = yield average
        if val is None:
            continue
        total += val
        count += 1
        average = total / count

avg_coroutine = running_averager()
# Prime the coroutine by advancing it to the first yield statement
next(avg_coroutine)

print(f"Sent 10.0 -> Live Cumulative Avg: {avg_coroutine.send(10.0)}")
print(f"Sent 20.0 -> Live Cumulative Avg: {avg_coroutine.send(20.0)}")
print(f"Sent 60.0 -> Live Cumulative Avg: {avg_coroutine.send(60.0)}")
print(f"Sent 70.0 -> Live Cumulative Avg: {avg_coroutine.send(70.0)}")

# Clean up
avg_coroutine.close()
print("Coroutine closed safely.")


# ============================================================================
# 4. PRODUCTION PATTERN: LLM STREAMING TOKEN ENGINE
# ============================================================================
"""
Modern AI applications (ChatGPT, Claude, Gemini APIs) do NOT wait for the entire
500-word response to finish before returning.
They yield tokens in real-time chunks via HTTP Server-Sent Events (SSE).
Here is how that streaming architecture is built in Python!
"""

print("\n" + "=" * 70)
print("4. PRODUCTION AI: LLM STREAMING TOKEN SIMULATOR")
print("=" * 70)

def mock_llm_stream_endpoint(prompt: str) -> Generator[str, None, dict]:
    """
    Simulates an OpenAI/Gemini streaming endpoint yielding tokens one by one.
    Also returns final token count metadata via return statement in Python 3.3+!
    """
    response_tokens = [
        "Decorators", " wrap", " functions,", " while", " Generators", " stream",
        " data", " lazily", " in", " O(1)", " memory.", " Combining", " both",
        " unlocks", " production-grade", " AI", " pipelines!"
    ]

    for token in response_tokens:
        # Simulate slight network jitter (5-10ms)
        time.sleep(0.02)
        yield token

    # A generator's `return` value is attached to StopIteration.value
    return {"prompt": prompt, "total_tokens": len(response_tokens), "model": "gemini-pro"}


def stream_client_consumer():
    print("User Prompt: 'Explain Python Generators in AI'")
    print("AI Response: ", end="", flush=True)

    stream = mock_llm_stream_endpoint("Explain Python Generators in AI")

    # Buffer for collecting full response while displaying live stream
    full_text = []
    metadata = None

    while True:
        try:
            chunk = next(stream)
            print(chunk, end="", flush=True)
            full_text.append(chunk)
        except StopIteration as e:
            # StopIteration.value contains the return value of the generator!
            metadata = e.value
            break

    print("\n\nStream Finished!")
    print(f"Metadata: Model={metadata['model']} | Tokens={metadata['total_tokens']}")

stream_client_consumer()

print("\n" + "=" * 70)
print("DAY 13 MODULE 03: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

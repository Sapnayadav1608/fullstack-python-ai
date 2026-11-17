"""
Day 13: Python Iterators, Generators & Context Managers
Student Practice Workbook & Automated Test Suite
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Instructions:
- Fill in the # TODO sections for each of the 6 challenges.
- Run this file: `python day13/my_practice.py`
- All automated unit tests must pass!
"""

from typing import Any, Generator, Iterable, Iterator, List, Tuple
from contextlib import contextmanager
import time


# ============================================================================
# TASK 1: CUSTOM CYCLIC ITERATOR
# ============================================================================
"""
Create a class `CyclicIterator` that takes an iterable and repeats its elements
a fixed `max_cycles` times before raising StopIteration.

Example:
    list(CyclicIterator(["A", "B"], max_cycles=2))
    -> ["A", "B", "A", "B"]
"""

class CyclicIterator:
    def __init__(self, data=None, max_cycles: int = 1) -> None:
        self.data = list(data) if data is not None else []
        self.max_cycles = max_cycles
        self.current_cycle = 0
        self.index = 0

    def __iter__(self) -> "CyclicIterator":
        # TODO: Implement __iter__
        return self

    def __next__(self) -> Any:
        # TODO: Implement __next__ logic.
        # Check if cycles exhausted, handle indexing, advance cycle count.
        raise NotImplementedError("TODO: Implement __next__")


# ============================================================================
# TASK 2: CUSTOM RANGE GENERATOR (my_range)
# ============================================================================
"""
Implement a generator function `my_range` that behaves like Python's built-in
`range()` function, supporting `start`, `stop`, and `step` (both positive and negative).

Examples:
    list(my_range(1, 5))       -> [1, 2, 3, 4]
    list(my_range(0, 10, 2))    -> [0, 2, 4, 6, 8]
    list(my_range(5, 0, -1))    -> [5, 4, 3, 2, 1]
"""

def my_range(start: int, stop: int = None, step: int = 1) -> Generator[int, None, None]:  # type: ignore
    # TODO: Implement my_range generator using `yield`
    raise NotImplementedError("TODO: Implement my_range")
    yield 0


# ============================================================================
# TASK 3: INFINITE PRIME STREAM GENERATOR
# ============================================================================
"""
Create an infinite generator `prime_stream()` that yields prime numbers
one-by-one indefinitely without storing past numbers in a massive list.

Example:
    p = prime_stream()
    [next(p) for _ in range(5)] -> [2, 3, 5, 7, 11]
"""

def prime_stream() -> Generator[int, None, None]:
    # TODO: Implement infinite prime generator using `yield`
    raise NotImplementedError("TODO: Implement prime_stream")
    yield 0


# ============================================================================
# TASK 4: COMPOSE A STREAMING DATA CLEANING PIPELINE
# ============================================================================
"""
Given an iterable of raw messy string records in the format:
    "  <name> , <age> , <status>  \n"

Write a generator function `clean_user_pipeline(stream: Iterable[str], min_age: int)`
that:
1. Strips leading/trailing whitespace.
2. Splits into name (str), age (int), and status (str.upper()).
3. Yields only records where status == "ACTIVE" and age >= min_age as a tuple: (name, age).
"""

def clean_user_pipeline(stream: Iterable[str], min_age: int) -> Generator[Tuple[str, int], None, None]:
    # TODO: Implement generator pipeline yielding (name, age)
    raise NotImplementedError("TODO: Implement clean_user_pipeline")
    yield ("", 0)


# ============================================================================
# TASK 5: RECURSIVE FLATTENER WITH `yield from`
# ============================================================================
"""
Implement `deep_flatten(data: Any)` using `yield from` that flattens any
arbitrarily nested list or tuple into a 1D sequence of leaf elements.

Example:
    list(deep_flatten([1, [2, [3, 4], 5], 6])) -> [1, 2, 3, 4, 5, 6]
"""

def deep_flatten(data: Any) -> Generator[Any, None, None]:
    # TODO: Implement recursive flattener with `yield from`
    raise NotImplementedError("TODO: Implement deep_flatten")
    yield 0


# ============================================================================
# TASK 6: EXECUTION TIMER CONTEXT MANAGER
# ============================================================================
"""
Implement a context manager `ExecutionTimer` (class or @contextmanager) that:
1. Records the elapsed time in milliseconds upon block completion.
2. Exposes an `elapsed_ms` float attribute.
3. Does NOT suppress exceptions raised inside the block.
"""

class ExecutionTimer:
    def __init__(self) -> None:
        self.elapsed_ms: float = 0.0
        self._start: float = 0.0

    def __enter__(self) -> "ExecutionTimer":
        # TODO: Implement __enter__
        raise NotImplementedError("TODO: Implement __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        # TODO: Implement __exit__
        raise NotImplementedError("TODO: Implement __exit__")


# ============================================================================
# AUTOMATED TEST SUITE
# ============================================================================

def run_tests():
    print("=" * 70)
    print("RUNNING AUTOMATED TEST SUITE FOR DAY 13 PRACTICE")
    print("=" * 70)
    score = 0
    total = 6

    # Test 1: CyclicIterator
    try:
        c = CyclicIterator(["X", "Y"], max_cycles=3)
        res = list(c)
        assert res == ["X", "Y", "X", "Y", "X", "Y"], f"Expected 6 items, got {res}"
        # Test empty
        assert list(CyclicIterator([], max_cycles=2)) == []
        print("✅ Task 1 Passed: CyclicIterator works correctly.")
        score += 1
    except Exception as e:
        print(f"❌ Task 1 Failed: {e}")

    # Test 2: my_range
    try:
        assert list(my_range(5)) == [0, 1, 2, 3, 4]
        assert list(my_range(2, 6)) == [2, 3, 4, 5]
        assert list(my_range(1, 10, 3)) == [1, 4, 7]
        assert list(my_range(10, 0, -2)) == [10, 8, 6, 4, 2]
        print("✅ Task 2 Passed: my_range behaves identical to built-in range.")
        score += 1
    except Exception as e:
        print(f"❌ Task 2 Failed: {e}")

    # Test 3: prime_stream
    try:
        p = prime_stream()
        first_6 = [next(p) for _ in range(6)]
        assert first_6 == [2, 3, 5, 7, 11, 13], f"Got {first_6}"
        print("✅ Task 3 Passed: prime_stream produces infinite primes lazily.")
        score += 1
    except Exception as e:
        print(f"❌ Task 3 Failed: {e}")

    # Test 4: clean_user_pipeline
    try:
        raw_data = [
            "  Alice , 28 , active \n",
            " Bob , 17 , active \n",
            " Charlie , 35 , INACTIVE \n",
            " Diana , 22 , Active \n"
        ]
        pipeline = list(clean_user_pipeline(raw_data, min_age=21))
        expected = [("Alice", 28), ("Diana", 22)]
        assert pipeline == expected, f"Got {pipeline}, expected {expected}"
        print("✅ Task 4 Passed: clean_user_pipeline correctly transforms and filters stream.")
        score += 1
    except Exception as e:
        print(f"❌ Task 4 Failed: {e}")

    # Test 5: deep_flatten
    try:
        nested = [1, (2, [3, (4, 5)], 6), [7, [8, [9]]]]
        flat = list(deep_flatten(nested))
        assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Got {flat}"
        print("✅ Task 5 Passed: deep_flatten with `yield from` flattens arbitrary depths.")
        score += 1
    except Exception as e:
        print(f"❌ Task 5 Failed: {e}")

    # Test 6: ExecutionTimer
    try:
        with ExecutionTimer() as timer:
            time.sleep(0.05)
        assert timer.elapsed_ms >= 45.0, f"Timer recorded {timer.elapsed_ms}ms"
        print("✅ Task 6 Passed: ExecutionTimer accurately tracks elapsed time.")
        score += 1
    except Exception as e:
        print(f"❌ Task 6 Failed: {e}")

    print("=" * 70)
    print(f"TEST SCORE: {score}/{total} PASSED")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

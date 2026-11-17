"""
Day 13: Python Iterators & The Iteration Protocol
Module 01: Iteration Protocol, Iterable vs Iterator, and Custom Iterators
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. The Core Iteration Protocol: __iter__() and __next__() dunder methods.
2. Iterable vs Iterator: Formal definitions and verification.
3. How Python's `for` Loop Works Under the Hood (CPython engine emulation).
4. The Iterator Exhaustion Trap (Why iterators can only be consumed once).
5. Two-Argument iter(callable, sentinel) for infinite stream reading.
6. Production Implementation: BatchDatasetIterator for AI mini-batch training.
"""

from typing import Any, List, Sequence
import collections.abc


# ============================================================================
# 1. ITERABLE VS ITERATOR: THE FORMAL DISTINCTION
# ============================================================================
"""
WHAT IS AN ITERABLE?
- Any Python object capable of returning its members one at a time.
- Must implement `__iter__()` OR `__getitem__()` with integer indices starting at 0.
- Examples: list, str, tuple, dict, set, range.
- An iterable does NOT track current position! It merely produces a new iterator.

WHAT IS AN ITERATOR?
- An object representing a stream of data that produces values one at a time.
- Must implement BOTH:
    1. `__iter__()`: Returns `self` (so iterators are also iterables!).
    2. `__next__()`: Returns the next item, or raises `StopIteration` when exhausted.
- Iterators DO track current position in memory!
"""

print("=" * 70)
print("1. ITERABLE VS ITERATOR VERIFICATION")
print("=" * 70)

sample_list = [10, 20, 30]

# Check types using collections.abc abstract base classes
print(f"Is list Iterable? {isinstance(sample_list, collections.abc.Iterable)}")  # True
print(f"Is list Iterator? {isinstance(sample_list, collections.abc.Iterator)}")  # False

# Obtain an iterator from an iterable using built-in iter()
list_iterator = iter(sample_list)
print(f"Is list_iterator Iterator? {isinstance(list_iterator, collections.abc.Iterator)}")  # True
print(f"Is list_iterator Iterable? {isinstance(list_iterator, collections.abc.Iterable)}")  # True


# ============================================================================
# 2. HOW PYTHON'S `for` LOOP WORKS UNDER THE HOOD
# ============================================================================
"""
When you write:
    for item in collection:
        process(item)

CPython bytecode actually executes:
    _iter = iter(collection)         # Calls collection.__iter__()
    while True:
        try:
            item = next(_iter)       # Calls _iter.__next__()
        except StopIteration:
            break                    # Graceful termination
        process(item)
"""

print("\n" + "=" * 70)
print("2. CPYTHON FOR-LOOP EMULATION")
print("=" * 70)

numbers = [100, 200, 300]

print("Standard for-loop:")
for n in numbers:
    print(f"  Item: {n}")

print("\nUnder-the-hood CPython emulation:")
manual_iterator = iter(numbers)
while True:
    try:
        n = next(manual_iterator)
        print(f"  Manual next() call: {n}")
    except StopIteration:
        print("  [StopIteration caught] -> Iterator safely exhausted.")
        break


# ============================================================================
# 3. THE ITERATOR EXHAUSTION TRAP
# ============================================================================
"""
CRITICAL GOTCHA:
Iterators are stateful, one-way streams. Once they reach the end, they stay
exhausted. You cannot reset an iterator or rewind it!
"""

print("\n" + "=" * 70)
print("3. THE ITERATOR EXHAUSTION TRAP")
print("=" * 70)

stream = iter(["alpha", "beta", "gamma"])

# First consumption
first_pass = list(stream)
print(f"First pass:  {first_pass}")

# Second consumption (Common beginner bug!)
second_pass = list(stream)
print(f"Second pass: {second_pass}  <-- EMPTY! The iterator is already exhausted!")


# ============================================================================
# 4. BUILDING CUSTOM ITERATORS FROM SCRATCH
# ============================================================================

class ReverseSequenceIterator:
    """
    Custom iterator that traverses any sequence in reverse without making
    a memory-heavy reversed copy of the sequence.
    """
    def __init__(self, data: Sequence[Any]) -> None:
        self._data = data
        self._index = len(data) - 1

    def __iter__(self) -> "ReverseSequenceIterator":
        # Rule of Python Iterators: __iter__() must return self
        return self

    def __next__(self) -> Any:
        if self._index < 0:
            raise StopIteration
        value = self._data[self._index]
        self._index -= 1
        return value


print("\n" + "=" * 70)
print("4. CUSTOM REVERSE ITERATOR DEMO")
print("=" * 70)

langs = ["Python", "Go", "Rust", "TypeScript"]
rev_iter = ReverseSequenceIterator(langs)

print("Traversing with custom ReverseSequenceIterator:")
for item in rev_iter:
    print(f"  Reversed: {item}")


# ============================================================================
# 5. PRODUCTION PATTERN: AI BATCH DATASET ITERATOR
# ============================================================================
"""
In Deep Learning and LLM fine-tuning, datasets (embeddings, prompt-response pairs)
cannot be fed all at once into GPU VRAM.
We need an iterator that slices batches on-the-fly with zero duplication.
"""

class BatchDatasetIterator:
    """
    Production-grade iterator for mini-batch generation in AI model training.
    """
    def __init__(self, dataset: List[Any], batch_size: int, drop_last: bool = False) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size must be positive.")
        self.dataset = dataset
        self.batch_size = batch_size
        self.drop_last = drop_last
        self.cursor = 0

    def __iter__(self) -> "BatchDatasetIterator":
        # Reset cursor when re-iterated
        self.cursor = 0
        return self

    def __len__(self) -> int:
        total = len(self.dataset)
        if self.drop_last:
            return total // self.batch_size
        return (total + self.batch_size - 1) // self.batch_size

    def __next__(self) -> List[Any]:
        if self.cursor >= len(self.dataset):
            raise StopIteration

        batch = self.dataset[self.cursor : self.cursor + self.batch_size]

        # Handle drop_last condition for incomplete final batch
        if self.drop_last and len(batch) < self.batch_size:
            raise StopIteration

        self.cursor += self.batch_size
        return batch


print("\n" + "=" * 70)
print("5. AI BATCH DATASET ITERATOR IN ACTION")
print("=" * 70)

synthetic_embeddings = [f"embed_{i:03d}" for i in range(1, 11)]
batch_iterator = BatchDatasetIterator(synthetic_embeddings, batch_size=3, drop_last=False)

print(f"Total Batches expected: {len(batch_iterator)}")
for step, batch in enumerate(batch_iterator, start=1):
    print(f"  Step {step}: Feeding Batch to Model VRAM -> {batch}")


# ============================================================================
# 6. TWO-ARGUMENT iter(callable, sentinel)
# ============================================================================
"""
Python has a lesser-known built-in signature:
    iter(callable, sentinel)
It repeatedly calls `callable()` with no arguments until it returns `sentinel`,
at which point it automatically raises `StopIteration`.
Super useful for reading network sockets, sensors, or rolling dice.
"""

print("\n" + "=" * 70)
print("6. TWO-ARGUMENT iter(callable, sentinel)")
print("=" * 70)

import random

# Roll a 6-sided die until we hit a 6 (sentinel)
die_roller = iter(lambda: random.randint(1, 6), 6)

print("Rolling die until first 6 appears (sentinel):")
rolls = list(die_roller)
print(f"  Rolls before 6: {rolls} (Terminated on sentinel=6)")

print("\n" + "=" * 70)
print("DAY 13 MODULE 01: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

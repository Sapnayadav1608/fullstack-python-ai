"""
Day 08: Tuples vs Lists - Memory Architecture, Speed Benchmarks & Hashability
=============================================================================
30-Day Full Stack Python + AI Engineering Challenge

Core Interview Question:
"Why do we need Tuples in Python when we already have Lists?"

Topics Covered:
1. Memory Architecture & Over-allocation Comparison (sys.getsizeof)
2. Performance Benchmark: Tuple vs List Creation & Iteration Speed
3. CPython Optimizations: Constant Folding & Free List Allocation
4. Hashability & The Dictionary Key Rule (List vs Tuple)
5. Practical AI / Data Science Application: Tensor Shapes & Coordinates
"""

import sys
import time

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 08 - TOPIC 02: TUPLES VS LISTS - MEMORY & PERFORMANCE]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. MEMORY EFFICIENCY COMPARISON
# -------------------------------------------------------------------------
print("\n--- 1. Memory Overhead: sys.getsizeof() Comparison ---")
# Lists require extra memory overhead for dynamic over-allocation.
# Tuples are allocated with the EXACT size needed — no wasted bytes!

sizes = [0, 1, 5, 10, 50, 100]
print(f"{'Item Count':<12} | {'List Memory':<15} | {'Tuple Memory':<15} | {'Saved Bytes'}")
print("-" * 60)

for count in sizes:
    sample_lst = list(range(count))
    sample_tup = tuple(range(count))
    lst_bytes = sys.getsizeof(sample_lst)
    tup_bytes = sys.getsizeof(sample_tup)
    diff = lst_bytes - tup_bytes
    print(f"{count:<12} | {lst_bytes:>6} bytes     | {tup_bytes:>6} bytes      | {diff:>4} bytes ({diff/lst_bytes*100:.1f}%)")

print(">> SUMMARY: Tuples consistently use less RAM because they are fixed-size arrays.")


# -------------------------------------------------------------------------
# 2. CREATION & ITERATION SPEED BENCHMARK
# -------------------------------------------------------------------------
print("\n--- 2. Performance Benchmark: Creation & Traversal Speed ---")
ITERATIONS = 10_000_000

# Benchmark 1: Literal List Creation
t0 = time.perf_counter()
for _ in range(ITERATIONS):
    _ = [1, 2, 3, 4, 5]
time_list = time.perf_counter() - t0

# Benchmark 2: Literal Tuple Creation
t0 = time.perf_counter()
for _ in range(ITERATIONS):
    _ = (1, 2, 3, 4, 5)
time_tuple = time.perf_counter() - t0

print(f"Creating {ITERATIONS:,} Lists  : {time_list:.4f} seconds")
print(f"Creating {ITERATIONS:,} Tuples : {time_tuple:.4f} seconds")
speedup = time_list / max(time_tuple, 1e-9)
print(f">> Tuples are approximately {speedup:.2f}x faster to create than lists!")
print("   Why? CPython optimizes tuples via 'Constant Folding' and 'Tuple Free Lists'.")


# -------------------------------------------------------------------------
# 3. HASHABILITY & DICTIONARY KEYS
# -------------------------------------------------------------------------
print("\n--- 3. Hashability: Using Tuples as Dictionary Keys ---")
# Python dictionaries and sets require keys to be HASHABLE (immutable).
# Lists are mutable, so hash(list) raises TypeError!
# Tuples are immutable, so hash(tuple) works as long as all elements are hashable.

# Example 1: Geographic coordinates as dictionary keys
geo_locations = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
    (12.9716, 77.5946): "Bengaluru"
}

mumbai_coords = (19.0760, 72.8777)
print(f"City at {mumbai_coords}: {geo_locations[mumbai_coords]}")

# Can we use a list as a dictionary key?
try:
    invalid_dict = {[1, 2]: "Invalid"}
except TypeError as e:
    print(f">> TypeError as expected: {e}")
    print("   Lists cannot be keys because their contents can mutate and invalidate hash buckets!")


# -------------------------------------------------------------------------
# 4. PRACTICAL AI APPLICATION: TENSOR SHAPES & RGB VALUES
# -------------------------------------------------------------------------
print("\n--- 4. Real-World AI Engineering Use Case: Tensor Dimensions ---")
# In Deep Learning (PyTorch, TensorFlow, NumPy), tensor dimensions are tuples:
# (Batch Size, Channels, Height, Width)

image_tensor_shape = (32, 3, 224, 224)
batch_size, channels, height, width = image_tensor_shape

print(f"PyTorch Image Tensor Shape : {image_tensor_shape}")
print(f"  Batch Size (Images)      : {batch_size}")
print(f"  Color Channels (RGB)     : {channels}")
print(f"  Resolution (H x W)       : {height}x{width}")
print(">> Why a tuple? A model's layer shape must remain immutable during training passes!")

print("\n" + "=" * 70)
print("[OK] Tuples vs Lists Performance & Architecture Module Completed!")
print("=" * 70)

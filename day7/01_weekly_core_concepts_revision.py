"""
Day 07: Week 01 Comprehensive Core Concepts Revision
=====================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. Python Memory Model & Object Identity (id, is vs ==, immutability)
2. String Slicing & Traversal Mechanics
3. Big O Complexity Golden Rules & Time/Space Trade-offs
4. Python List Memory Architecture (Referential Array, Dynamic Resizing)
5. Shallow Copy vs Deep Copy in Nested Structures
6. List Comprehension Optimization & Bytecode Advantages
"""

import sys
import copy
import time

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 07 - WEEK 1 COMPREHENSIVE REVISION]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. PYTHON OBJECT MODEL & IDENTITY: is vs ==
# -------------------------------------------------------------------------
print("\n--- 1. Memory Model: Value Equality (==) vs Identity (is) ---")

list_a = [10, 20, 30]
list_b = [10, 20, 30]
list_c = list_a  # Reference copy (both point to same memory location)

print(f"list_a: {list_a} (id: {id(list_a)})")
print(f"list_b: {list_b} (id: {id(list_b)})")
print(f"list_c: {list_c} (id: {id(list_c)})")

print(f"list_a == list_b : {list_a == list_b}  (Checks values -> TRUE)")
print(f"list_a is list_b : {list_a is list_b} (Checks memory addresses -> FALSE)")
print(f"list_a is list_c : {list_a is list_c}  (Same object in heap -> TRUE)")

# Immutability check: int, float, str, tuple are IMMUTABLE
msg = "Python"
old_id = id(msg)
msg += "3"
print(f"\nImmutable re-assignment: Old id={old_id}, New id={id(msg)} (New object created!)")

# -------------------------------------------------------------------------
# 2. STRING SLICING & STEP MECHANICS
# -------------------------------------------------------------------------
print("\n--- 2. String Slicing Formula & Step Direction ---")
text = "DEVELOPER"
# Indices:
# D  E  V  E  L  O  P  E  R
# 0  1  2  3  4  5  6  7  8
# -9 -8 -7 -6 -5 -4 -3 -2 -1

print(f"Original Text        : '{text}'")
print(f"text[0:4]            : '{text[0:4]}' (indices 0, 1, 2, 3)")
print(f"text[::2] (even step): '{text[::2]}'")
print(f"text[::-1] (reversed): '{text[::-1]}'")
print(f"text[6:1:-1]         : '{text[6:1:-1]}' (Starts at 6, steps backwards down to 2)")

# -------------------------------------------------------------------------
# 3. BIG O COMPLEXITY RECAP: O(1) vs O(N) vs O(N^2)
# -------------------------------------------------------------------------
print("\n--- 3. Big O Complexity Golden Rules ---")
print("""
Rule 1: Drop Constants      -> O(2N + 5) becomes O(N)
Rule 2: Drop Non-Dominant   -> O(N^2 + N + 100) becomes O(N^2)
Rule 3: Lookups             -> 'x in list' is O(N) linear search
                               'x in set' or 'x in dict' is O(1) hash lookup!
""")

# Quick lookup benchmark: list vs set
sample_list = list(range(100_000))
sample_set = set(sample_list)
target = 99_999

# Measure list lookup
t0 = time.perf_counter()
_ = target in sample_list
t_list = time.perf_counter() - t0

# Measure set lookup
t0 = time.perf_counter()
_ = target in sample_set
t_set = time.perf_counter() - t0

print(f"List Lookup (O(N))   : {t_list * 1000:.4f} ms")
print(f"Set Lookup  (O(1))   : {t_set * 1000:.4f} ms")
print(f"-> Set lookup is significantly faster for membership tests!")

# -------------------------------------------------------------------------
# 4. LIST MEMORY: REFERENTIAL ARRAY & RESIZING
# -------------------------------------------------------------------------
print("\n--- 4. Python Dynamic List Architecture ---")
dynamic_demo = []
print("Growth in byte size as elements are appended:")
prev_size = sys.getsizeof(dynamic_demo)
for i in range(12):
    dynamic_demo.append(i)
    curr_size = sys.getsizeof(dynamic_demo)
    if curr_size != prev_size or i == 0 or i == 11:
        print(f"  Length: {len(dynamic_demo):2d} items | Memory: {curr_size:3d} bytes (CPython over-allocation)")
        prev_size = curr_size

# -------------------------------------------------------------------------
# 5. SHALLOW COPY VS DEEP COPY RECAP
# -------------------------------------------------------------------------
print("\n--- 5. Shallow Copy vs Deep Copy in Nested Lists ---")
matrix_orig = [[1, 2], [3, 4]]
matrix_shallow = matrix_orig.copy()      # or matrix_orig[:]
matrix_deep = copy.deepcopy(matrix_orig)

# Modify inner element
matrix_orig[0][0] = 999

print(f"Original changed: {matrix_orig}")
print(f"Shallow copy    : {matrix_shallow} (AFFECTED because inner pointers are shared!)")
print(f"Deep copy       : {matrix_deep} (SAFE because inner lists were duplicated)")

# -------------------------------------------------------------------------
# 6. LIST COMPREHENSION: SPEED & READABILITY
# -------------------------------------------------------------------------
print("\n--- 6. List Comprehension Bytecode Efficiency ---")
evens_loop = []
for n in range(10):
    if n % 2 == 0:
        evens_loop.append(n)

evens_comp = [n for n in range(10) if n % 2 == 0]
print(f"Loop result : {evens_loop}")
print(f"Comp result : {evens_comp}")
print("Note: Comprehensions run at C-speed in CPython using LIST_APPEND opcode.")

print("\n" + "=" * 70)
print("[OK] Week 1 Core Concepts Revision Completed Successfully!")
print("=" * 70)

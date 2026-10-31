# =============================================================================
# DAY 06 - TOPIC 01: List Comprehension Fundamentals
# =============================================================================
# Traditional Loop vs List Comprehension: Syntax, Readability & Speed.
# =============================================================================

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 06 - TOPIC 01] List Comprehension Fundamentals")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. Traditional Loop vs List Comprehension
# -----------------------------------------------------------------------------
# Goal: 1 se 10 tak ke numbers ke squares ki list banana.

# Traditional Approach:
squares_loop = []
for x in range(1, 11):
    squares_loop.append(x ** 2)
print("Using traditional loop        :", squares_loop)

# List Comprehension Syntax: [expression for item in iterable]
squares_comp = [x ** 2 for x in range(1, 11)]
print("Using list comprehension      :", squares_comp)


# -----------------------------------------------------------------------------
# 2. Filtering with 'if' condition
# -----------------------------------------------------------------------------
# Syntax: [expression for item in iterable if condition]
# Goal: Sirf EVEN numbers filter karke unke squares nikaalna.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("\nEven squares with 'if' filter :", even_squares)


# -----------------------------------------------------------------------------
# 3. Transformation with 'if-else' (Ternary Expression)
# -----------------------------------------------------------------------------
# Note: Jab 'if-else' dono lagte hain, toh wo 'for' se PEHLE aate hain!
# Syntax: [val_if_true if condition else val_if_false for item in iterable]

grades = [85, 42, 90, 33, 76, 58]
status = ["Pass" if mark >= 40 else "Fail" for mark in grades]
print("\nPass/Fail status with if-else :", status)


# -----------------------------------------------------------------------------
# 4. Kyu List Comprehension Fast Hoti Hai? (Bytecode Optimization)
# -----------------------------------------------------------------------------
# List comprehension Python bytecode level par direct C-optimized instruction
# 'LIST_APPEND' use karti hai, jismein bar-bar .append() method call lookup
# nahi karna padta. Isliye yeh standard loop se ~25-35% faster hoti hai!

N = 5_000_000

t0 = time.perf_counter()
res1 = []
for i in range(N):
    res1.append(i * 2)
time_loop = time.perf_counter() - t0

t0 = time.perf_counter()
res2 = [i * 2 for i in range(N)]
time_comp = time.perf_counter() - t0

print(f"\n--- Performance Comparison (N = {N:,}) ---")
print(f"Traditional for-loop : {time_loop:.4f} seconds")
print(f"List Comprehension   : {time_comp:.4f} seconds")
print(f">> Comprehension is {((time_loop - time_comp) / time_loop) * 100:.1f}% faster!")

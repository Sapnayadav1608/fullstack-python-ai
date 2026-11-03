"""
Day 08: Tuple Operations, Advanced Unpacking & Namedtuples
==========================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. Tuple Operations (+, *, in, len, min, max, sum)
2. Why Tuples Only Have 2 Methods (.count() & .index())
3. Variable Swapping Without a Temp Variable (Tuple Magic)
4. Advanced Pythonic Unpacking with the Star (*) Operator
5. Throwaway Variables with Underscore (_)
6. collections.namedtuple: Clean, Self-Documenting Immutable Records
"""

import sys
from collections import namedtuple

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 08 - TOPIC 03: OPERATIONS, UNPACKING & NAMEDTUPLES]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. TUPLE OPERATIONS & BUILT-INS
# -------------------------------------------------------------------------
print("\n--- 1. Basic Tuple Operations ---")
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation (+) creates a BRAND NEW tuple
merged = t1 + t2
print(f"Concatenation (t1 + t2) : {merged} (id: {id(merged)})")

# Repetition (*)
repeated = ("AI",) * 3
print(f"Repetition (('AI',) * 3) : {repeated}")

# Membership & Built-ins
numbers = (45, 12, 89, 23, 67, 12)
print(f"\nNumbers Tuple: {numbers}")
print(f"Length   : {len(numbers)}")
print(f"Max / Min: {max(numbers)} / {min(numbers)}")
print(f"Sum      : {sum(numbers)}")
print(f"Sorted   : {sorted(numbers)} (Returns a sorted LIST)")


# -------------------------------------------------------------------------
# 2. WHY TUPLES ONLY HAVE 2 METHODS
# -------------------------------------------------------------------------
print("\n--- 2. Tuple Methods: .count() and .index() ---")
# Unlike lists (11 methods), tuples only have 2 methods:
# No append, extend, insert, pop, remove, sort, or reverse because tuples are immutable!

print(f"Frequency of 12 (numbers.count(12)) : {numbers.count(12)}")
print(f"First index of 89 (numbers.index(89)): {numbers.index(89)}")


# -------------------------------------------------------------------------
# 3. ADVANCED TUPLE UNPACKING (THE STAR * OPERATOR)
# -------------------------------------------------------------------------
print("\n--- 3. Advanced Tuple Unpacking ---")

# A. Basic Unpacking (Variables must match length)
rgb = (255, 128, 0)
r, g, b = rgb
print(f"RGB unpacked: Red={r}, Green={g}, Blue={b}")

# B. Variable Swapping (Under the hood, Python creates a tuple and unpacks it!)
x = 100
y = 200
print(f"\nBefore Swap: x={x}, y={y}")
x, y = y, x  # (y, x) packed into tuple -> unpacked into x, y
print(f"After Swap : x={x}, y={y} (Swapped without temp variable!)")

# C. Star (*) Extended Unpacking (PEP 3132)
data_stream = (10, 20, 30, 40, 50, 60, 70)

# Extract first, last, and gather the rest into a list
first, *middle, last = data_stream
print(f"\nData Stream  : {data_stream}")
print(f"  First item : {first}")
print(f"  Middle list: {middle} (Captured dynamically by *middle)")
print(f"  Last item  : {last}")

# D. Throwaway variables with underscore (_)
user_record = ("Sapna", 23, "Engineer", "Mumbai")
name, _, role, _ = user_record
print(f"\nDiscarded age & city with '_': Name='{name}', Role='{role}'")


# -------------------------------------------------------------------------
# 4. COLLECTIONS.NAMEDTUPLE (PRO PYTHON TOOL)
# -------------------------------------------------------------------------
print("\n--- 4. collections.namedtuple: Professional Data Containers ---")
# Problem with regular tuples:
# point = (12.5, 45.8) -> What is point[0]? Latitude? X coordinate?
# namedtuple provides field names with zero memory overhead!

Point2D = namedtuple("Point2D", ["x", "y"])
p1 = Point2D(x=10.5, y=25.2)

print(f"NamedTuple instance: {p1}")
print(f"Access by attribute: p1.x = {p1.x}, p1.y = {p1.y}")
print(f"Access by index    : p1[0] = {p1[0]}, p1[1] = {p1[1]}")
print(f"Is p1 a tuple?     : {isinstance(p1, tuple)}")

# Real Backend Example: Model Metric Report
Metric = namedtuple("Metric", ["epoch", "loss", "accuracy"])
epoch_result = Metric(epoch=1, loss=0.2314, accuracy=0.945)
print(f"\nAI Training Metric: Epoch={epoch_result.epoch}, Loss={epoch_result.loss:.4f}, Acc={epoch_result.accuracy*100:.1f}%")

print("\n" + "=" * 70)
print("[OK] Tuple Operations, Unpacking & Namedtuples Module Completed!")
print("=" * 70)

# =============================================================================
# DAY 05 - TOPIC 05: Shallow Copy vs Deep Copy in Python (The Bug Trap!)
# =============================================================================
# Assignment vs Shallow Copy vs Deep Copy
# =============================================================================

import sys
import copy

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 05 - TOPIC 05] Shallow Copy vs Deep Copy")
print("=" * 60)

# -----------------------------------------------------------------------------
# CASE 1: Simple Assignment (b = a) -> NOT a copy at all!
# -----------------------------------------------------------------------------
# 'b' sirf ek doosra label ban jaata hai usi same memory address par.
a = [1, 2, 3]
b = a
b.append(99)

print("--- Case 1: Simple Assignment (b = a) ---")
print(f"List a: {a}")
print(f"List b: {b}")
print(f"Did modifying 'b' change 'a'? {a is b} (Yes! Both share address: {id(a)})")


# -----------------------------------------------------------------------------
# CASE 2: Shallow Copy (a.copy() ya a[:])
# -----------------------------------------------------------------------------
# Outer list ka naya memory address banta hai.
# Simple 1D lists ke liye yeh bilkul safe hai:
c = [10, 20, 30]
d = c.copy()
d.append(100)

print("\n--- Case 2: Shallow Copy on 1D List ---")
print(f"List c: {c}")
print(f"List d: {d}")
print(f"Are addresses different? {c is not d} (Safe for 1D list!)")

# LEKIN NESTED LISTS MEIN SHALLOW COPY FAIL HO JAATA HAI!
nested_1 = [[1, 2], [3, 4]]
nested_2 = nested_1.copy()  # Shallow copy

# Modifying inner nested list:
nested_2[0].append(999)

print("\n--- The Shallow Copy Bug in Nested Lists! ---")
print(f"Original nested_1 : {nested_1}")
print(f"Copied nested_2   : {nested_2}")
print("Bug: Outer list alag hai, par inner list ka address SAME reh gaya!")


# -----------------------------------------------------------------------------
# CASE 3: Deep Copy (copy.deepcopy()) -> The True Independent Copy
# -----------------------------------------------------------------------------
# Recursively har ek level par nayi memory allocate karta hai:
clean_original = [[1, 2], [3, 4]]
independent_copy = copy.deepcopy(clean_original)

independent_copy[0].append(999)

print("\n--- Case 3: Deep Copy (copy.deepcopy()) ---")
print(f"Original clean_original : {clean_original} (Intact! No side-effects!)")
print(f"Independent copy         : {independent_copy}")
print(f"Are inner lists different? {clean_original[0] is not independent_copy[0]} (True!)")

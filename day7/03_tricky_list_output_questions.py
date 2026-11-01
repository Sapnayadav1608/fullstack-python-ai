"""
Day 07: Top Tricky Python List Interview Output Questions & Traps
==================================================================
30-Day Full Stack Python + AI Engineering Challenge

Top 7 Python List Interview Gotchas & Brain Teasers:
1. The Default Mutable Argument Trap (def func(lst=[]))
2. Modifying a List While Iterating Over It (Index skipping)
3. 2D List Multiplication Trap ([[0]*3]*3)
4. In-Place Addition (+=) vs Concatenation (+) with Aliases
5. Slice Assignment (a[:] = ...) vs Variable Reassignment (a = ...)
6. In-Place .sort() returning None vs sorted()
7. Boolean Identity & Equality inside Lists (True in [1, 2])
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[TOP TRICKY PYTHON LIST INTERVIEW QUESTIONS]")
print("=" * 70)


# -------------------------------------------------------------------------
# TRAP 1: DEFAULT MUTABLE ARGUMENT TRAP
# -------------------------------------------------------------------------
print("\n--- TRAP 1: The Default Mutable Argument Trap ---")

def buggy_append(item, storage=[]):
    storage.append(item)
    return storage

print("Calling buggy_append(1):", buggy_append(1))
print("Calling buggy_append(2):", buggy_append(2))
print("Calling buggy_append(3):", buggy_append(3))
print(">> EXPLANATION: Default arguments are evaluated ONCE at function definition time,")
print("   NOT each time the function is called! All calls share the SAME list object.")

def fixed_append(item, storage=None):
    if storage is None:
        storage = []
    storage.append(item)
    return storage

print("\nFixed version:")
print("Calling fixed_append(1):", fixed_append(1))
print("Calling fixed_append(2):", fixed_append(2))


# -------------------------------------------------------------------------
# TRAP 2: MODIFYING LIST WHILE ITERATING
# -------------------------------------------------------------------------
print("\n--- TRAP 2: Modifying List During Iteration ---")

numbers = [1, 2, 2, 3, 4, 4, 5]
# Goal: Remove all even numbers
print(f"Original numbers: {numbers}")

# Buggy attempt:
buggy_nums = [1, 2, 2, 3, 4, 4, 5]
for n in buggy_nums:
    if n % 2 == 0:
        buggy_nums.remove(n)
print(f"Buggy for-loop removal result : {buggy_nums} (Notice 2 and 4 are still left!)")
print(">> EXPLANATION: Removing an item shifts left indices, skipping the next element.")

# Safe Fix 1: Slicing copy iteration
safe_nums1 = [1, 2, 2, 3, 4, 4, 5]
for n in safe_nums1[:]:  # Iterate over shallow copy of list
    if n % 2 == 0:
        safe_nums1.remove(n)
print(f"Safe Fix 1 (Slice copy loop)   : {safe_nums1}")

# Safe Fix 2: List comprehension (Most pythonic)
safe_nums2 = [n for n in [1, 2, 2, 3, 4, 4, 5] if n % 2 != 0]
print(f"Safe Fix 2 (Comprehension)    : {safe_nums2}")


# -------------------------------------------------------------------------
# TRAP 3: 2D LIST MULTIPLICATION TRAP
# -------------------------------------------------------------------------
print("\n--- TRAP 3: 2D Matrix Multiplication Trap ---")

# Buggy 3x3 matrix
buggy_grid = [[0] * 3] * 3
buggy_grid[0][0] = 77
print(f"buggy_grid after modifying [0][0]: {buggy_grid}")
print(">> EXPLANATION: Outer * 3 duplicated references to the single inner list!")

# Safe 3x3 matrix
safe_grid = [[0] * 3 for _ in range(3)]
safe_grid[0][0] = 77
print(f"safe_grid after modifying [0][0] : {safe_grid}")


# -------------------------------------------------------------------------
# TRAP 4: += VS + ON LISTS WITH ALIASES
# -------------------------------------------------------------------------
print("\n--- TRAP 4: '+=' vs '+' Behavior with Multiple References ---")

list_one = [1, 2, 3]
alias_one = list_one
list_one += [4, 5]  # In-place mutation (__iadd__)
print(f"After 'list_one += [4, 5]':")
print(f"  list_one : {list_one}")
print(f"  alias_one: {alias_one} (CHANGED because += mutates in place!)")

list_two = [1, 2, 3]
alias_two = list_two
list_two = list_two + [4, 5]  # Creates NEW list object
print(f"\nAfter 'list_two = list_two + [4, 5]':")
print(f"  list_two : {list_two}")
print(f"  alias_two: {alias_two} (UNCHANGED because list_two was rebound!)")


# -------------------------------------------------------------------------
# TRAP 5: SLICE ASSIGNMENT VS VARIABLE REASSIGNMENT
# -------------------------------------------------------------------------
print("\n--- TRAP 5: Slice Assignment (a[:] = ...) vs Variable Reassignment ---")

orig_ref = [10, 20, 30]
alias_ref = orig_ref

# Slicing assignment mutates the existing memory buffer
orig_ref[:] = [99, 100]
print(f"After 'orig_ref[:] = [99, 100]':")
print(f"  orig_ref : {orig_ref}")
print(f"  alias_ref: {alias_ref} (UPDATED because slice assignment mutates in-place!)")


# -------------------------------------------------------------------------
# TRAP 6: .sort() VS sorted()
# -------------------------------------------------------------------------
print("\n--- TRAP 6: .sort() Return Value Gotcha ---")

raw_scores = [45, 12, 89, 32]
sort_res = raw_scores.sort()
print(f"raw_scores.sort() returned: {sort_res} (Always returns None!)")
print(f"raw_scores is now in-place: {raw_scores}")

fresh_scores = [45, 12, 89, 32]
sorted_res = sorted(fresh_scores)
print(f"sorted(fresh_scores) returned: {sorted_res}")
print(f"fresh_scores remained       : {fresh_scores}")


# -------------------------------------------------------------------------
# TRAP 7: BOOLEAN MEMBERSHIP IN LISTS
# -------------------------------------------------------------------------
print("\n--- TRAP 7: Boolean Identity & Equality in Lists ---")

test_list = [1, 2, 3]
print(f"test_list = {test_list}")
print(f"True in test_list  : {True in test_list}")
print(">> EXPLANATION: In Python, bool inherits from int (isinstance(True, int) is True).")
print(f"   Since 1 == True evaluates to True, 'True in [1, 2, 3]' returns True!")

print("\n" + "=" * 70)
print("[OK] Top 7 Tricky Python List Interview Traps Mastered!")
print("=" * 70)

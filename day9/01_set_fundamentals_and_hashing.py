"""
Day 09: Python Sets - Creation, Hashing Architecture & CRUD Operations
======================================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. What is a Set? (Unordered, Mutable, Unique, Hash-Table Backed)
2. The Classic Empty Set Trap: {} vs set()
3. Under the Hood: Hashing Architecture & The hash() Function
4. The Hashability Rule: Why Lists Cannot Be In Sets, but Tuples Can!
5. The Boolean Equality Trap: True == 1 and False == 0 Collisions
6. Set CRUD Operations: .add(), .update(), .remove() vs .discard(), .pop()
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 09 - TOPIC 01: SET FUNDAMENTALS & HASHING ARCHITECTURE]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. WHAT IS A SET? (AUTOMATIC DEDUPLICATION)
# -------------------------------------------------------------------------
print("\n--- 1. Set Creation & Automatic Deduplication ---")
# A Set is an unordered collection of UNIQUE elements.
# Duplicates are automatically removed at insertion time!

raw_languages = ["Python", "JavaScript", "Python", "Rust", "Go", "Rust"]
unique_languages = set(raw_languages)

print(f"Raw List with Duplicates : {raw_languages}")
print(f"Unique Set               : {unique_languages}")
print(f"Type                     : {type(unique_languages)}")
print(f"Length                   : {len(unique_languages)} (Duplicates purged!)")


# -------------------------------------------------------------------------
# 2. THE CLASSIC EMPTY SET TRAP (INTERVIEW GOTCHA!)
# -------------------------------------------------------------------------
print("\n--- 2. The Empty Set Trap ---")
# Question: Does empty_var = {} create an empty set?
# NO! It creates an empty dictionary (dict)!

empty_curly = {}
empty_constructor = set()

print(f"Expression: empty_curly = {{}}    -> Type: {type(empty_curly).__name__:<8} (A DICTIONARY!)")
print(f"Expression: empty_set = set()   -> Type: {type(empty_constructor).__name__:<8} (A REAL SET)")
print(">> GOLDEN RULE: To create an empty set, ALWAYS use set(), not {}!")


# -------------------------------------------------------------------------
# 3. HASH TABLE ARCHITECTURE: HOW SETS WORK INTERNALLY
# -------------------------------------------------------------------------
print("\n--- 3. Under the Hood: Hashing Architecture ---")
# Python Sets are implemented as open-addressing Hash Tables without values (keys only).
# When you add an item 'x', Python computes hash(x) to determine its memory bucket index.
# This gives Sets O(1) average lookup, insertion, and deletion time!

item_a = "Python"
item_b = 42
item_c = (1, 2, 3)

print(f"hash('{item_a}') : {hash(item_a)}")
print(f"hash({item_b})         : {hash(item_b)}")
print(f"hash({item_c})  : {hash(item_c)}")


# -------------------------------------------------------------------------
# 4. THE HASHABILITY RULE: MUTABLE VS IMMUTABLE
# -------------------------------------------------------------------------
print("\n--- 4. Hashability Rule: What Can Go Inside a Set? ---")
# Only IMMUTABLE (Hashable) objects can be set elements:
# Allowed   : int, float, str, tuple, frozenset, bool
# Disallowed: list, dict, set (because their contents can mutate!)

valid_set = {10, "AI", (1, 2)}  # Tuple is allowed
print(f"Valid Set with Tuple: {valid_set}")

try:
    # Attempting to store a mutable list in a set raises TypeError!
    invalid_set = {10, [1, 2]}
except TypeError as error:
    print(f">> TypeError as expected: {error}")
    print("   Explanation: Lists are mutable, so they lack a fixed hash() value!")


# -------------------------------------------------------------------------
# 5. THE BOOLEAN EQUALITY & HASH COLLISION TRAP
# -------------------------------------------------------------------------
print("\n--- 5. The Boolean Equality Trap ---")
# In Python, bool is a subclass of int:
# True == 1 and False == 0.
# Both hash(True) == hash(1) == 1, and True == 1 evaluates to True!
# Therefore, a Set treats 1 and True as the SAME element!

bool_trap_set = {1, True, "Python", 0, False}
print(f"Input elements : {{1, True, 'Python', 0, False}}")
print(f"Resulting Set  : {bool_trap_set}")
print(">> EXPLANATION: Since 1 == True and 0 == False, only the FIRST inserted item is kept!")


# -------------------------------------------------------------------------
# 6. SET CRUD OPERATIONS: ADDING & REMOVING
# -------------------------------------------------------------------------
print("\n--- 6. Set Mutation: Adding & Removing Elements ---")
tech_stack = {"Python", "FastAPI"}
print(f"Initial Set : {tech_stack}")

# .add() adds a single element
tech_stack.add("Docker")
print(f"After .add('Docker')              : {tech_stack}")

# .update() unpacks and adds multiple elements from any iterable
tech_stack.update(["PostgreSQL", "Redis", "Python"])  # 'Python' ignored (already present)
print(f"After .update([...])              : {tech_stack}")

# .remove() vs .discard():
# .remove(item) raises KeyError if item is missing!
# .discard(item) silently succeeds if item is missing (SAFE REMOVAL).
tech_stack.discard("Kubernetes")  # Missing item, no error raised!
print(f"After .discard('Kubernetes') (Safe): {tech_stack}")

tech_stack.remove("Redis")        # Item exists, removes cleanly
print(f"After .remove('Redis')             : {tech_stack}")

# .pop() removes and returns an ARBITRARY element
popped_item = tech_stack.pop()
print(f"Popped arbitrary item              : '{popped_item}'")
print(f"Final Set state                    : {tech_stack}")

print("\n" + "=" * 70)
print("[OK] Set Fundamentals & Hashing Module Executed Successfully!")
print("=" * 70)

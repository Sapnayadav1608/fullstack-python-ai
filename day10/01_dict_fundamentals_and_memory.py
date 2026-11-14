"""
Day 10: Python Dictionaries - Fundamentals, Key Constraints & Memory Architecture
==================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. What is a Dictionary? (Key-Value Hash Map, Mutable, O(1) Average Lookup)
2. 5 Ways to Create Dictionaries in Python
3. The Key Hashability Rule: What can and CANNOT be a dictionary key?
4. Under the Hood: CPython 3.6+ Compact Dictionary Architecture
5. Insertion Order Preservation (Python 3.7+ Guaranteed Feature)
6. Dynamic Resizing & Memory Footprint with sys.getsizeof()
"""

import sys

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 10 - TOPIC 01: DICTIONARY FUNDAMENTALS & COMPACT MEMORY ARCHITECTURE]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. WHAT IS A DICTIONARY?
# -------------------------------------------------------------------------
print("\n--- 1. Dictionary Definition ---")
# A Dictionary is an associative array (Hash Map) that stores Key-Value pairs.
# Keys are UNIQUE and HASHABLE; Values can be ANY Python object (even nested dicts!).

developer = {
    "name": "Alex",
    "role": "AI Engineer",
    "experience_years": 3,
    "skills": ["Python", "PyTorch", "FastAPI"],
    "is_active": True
}

print(f"Developer Dictionary : {developer}")
print(f"Type                 : {type(developer)}")
print(f"Total Key-Value pairs: {len(developer)}")
print(f"Accessing 'role'     : {developer['role']}")


# -------------------------------------------------------------------------
# 2. 5 WAYS TO CREATE A DICTIONARY
# -------------------------------------------------------------------------
print("\n--- 2. Five Ways to Create Dictionaries ---")

# Method A: Direct Curly Braces Literal (Fastest & Most Pythonic)
d_literal = {"a": 1, "b": 2}

# Method B: dict() constructor with Keyword Arguments (Keys must be valid identifiers)
d_kwargs = dict(a=1, b=2)

# Method C: dict() from List of (key, value) Tuples
d_tuples = dict([("a", 1), ("b", 2)])

# Method D: dict(zip(keys, values)) (Parallel arrays to dictionary)
keys = ["a", "b"]
values = [1, 2]
d_zipped = dict(zip(keys, values))

# Method E: dict.fromkeys() (Create dict with uniform default values)
d_fromkeys = dict.fromkeys(["server_1", "server_2", "server_3"], "RUNNING")

print(f"A. Literal      : {d_literal}")
print(f"B. dict(kwargs) : {d_kwargs}")
print(f"C. dict(tuples) : {d_tuples}")
print(f"D. dict(zip)    : {d_zipped}")
print(f"E. fromkeys()   : {d_fromkeys}")

# ⚠️ BEWARE: dict.fromkeys with a MUTABLE default object!
# All keys share the EXACT SAME object reference in memory!
buggy_dict = dict.fromkeys(["team_a", "team_b"], [])
buggy_dict["team_a"].append("Alice")
print(f"\n⚠️  Fromkeys Reference Bug: {buggy_dict}")
print("   Both teams got 'Alice' because both keys point to the SAME list in memory!")
print("   Fix: Use a dict comprehension instead: {k: [] for k in ['team_a', 'team_b']}")


# -------------------------------------------------------------------------
# 3. THE KEY HASHABILITY RULE: WHAT CAN BE A KEY?
# -------------------------------------------------------------------------
print("\n--- 3. Key Constraints & The Hashability Rule ---")
# To look up a key in O(1) time, Python must calculate hash(key).
# Therefore, Keys MUST be HASHABLE (Immutable).
# Allowed   : int, float, str, tuple (if contents are immutable), frozenset, bool
# Disallowed: list, dict, set (raises TypeError: unhashable type!)

valid_dict = {
    42: "Integer Key",
    "status": "String Key",
    (10, 20): "Tuple Key (Coordinates)",
    frozenset(["read", "write"]): "Frozenset Key (Permissions)"
}
print(f"Valid Dictionary with Multi-Type Keys:\n  {valid_dict}")

try:
    # Attempting to use a mutable list as a dictionary key:
    invalid_dict = {[1, 2, 3]: "User IDs"}
except TypeError as error:
    print(f"\n>> TypeError Caught: {error}")
    print("   Explanation: Lists can mutate in place, which would break the hash table index!")


# -------------------------------------------------------------------------
# 4. UNDER THE HOOD: CPYTHON 3.6+ COMPACT DICT ARCHITECTURE
# -------------------------------------------------------------------------
print("\n--- 4. CPython Compact Hash Table Architecture ---")
# Historical Context:
# In Python 3.5 and earlier, dicts used a large sparse array of 24-byte structs:
# [hash, key_ptr, value_ptr]. Lots of empty gaps wasted 30-40% of RAM!
#
# Since Python 3.6+ (Raymond Hettinger design), CPython split dicts into TWO tables:
# 1. Sparse Indices Table (tiny array of 1-byte integers): [ -1, 0, -1, 1, ... ]
# 2. Dense Entries Array (stores elements tightly in insertion order):
#    entries = [
#      [hash('a'), 'a', 1],
#      [hash('b'), 'b', 2]
#    ]
# Result: 20-25% memory savings AND automatic insertion order preservation!

print("Visualizing CPython Compact Dictionary:")
print("  Hash Index Table  : [ -1,  0, -1,  1, -1, -1,  2, -1 ]  <-- Small bytes")
print("  Dense Entries     : 0 -> ('name', 'Alex')")
print("                      1 -> ('role', 'AI Engineer')")
print("                      2 -> ('experience', 3)")
print("  >> Result: Zero memory wasted on empty 24-byte pointer slots!")


# -------------------------------------------------------------------------
# 5. INSERTION ORDER PRESERVATION (PYTHON 3.7+ GUARANTEE)
# -------------------------------------------------------------------------
print("\n--- 5. Guaranteed Insertion Order ---")
# Prior to Python 3.7, dictionaries had ARBITRARY order.
# Since Python 3.7, insertion order is an official LANGUAGE SPECIFICATION!

ordered_test = {}
ordered_test["first"] = 1
ordered_test["second"] = 2
ordered_test["third"] = 3
ordered_test["fourth"] = 4

print(f"Keys in exact insertion order: {list(ordered_test.keys())}")


# -------------------------------------------------------------------------
# 6. DYNAMIC RESIZING & MEMORY FOOTPRINT (sys.getsizeof)
# -------------------------------------------------------------------------
print("\n--- 6. Dynamic Resizing & Memory Growth ---")
# Dictionaries start with an internal table of size 8.
# When the load factor exceeds 2/3 (66%), CPython automatically doubles the table!

d_growth = {}
last_size = sys.getsizeof(d_growth)
print(f"Empty Dict Size: {last_size} bytes")

print("Tracking dictionary resizing during element insertions:")
for i in range(1, 25):
    d_growth[f"key_{i}"] = i
    curr_size = sys.getsizeof(d_growth)
    if curr_size != last_size:
        print(f"  Item Count: {i:2d} -> Memory jumped from {last_size:4d}B to {curr_size:4d}B (Table Resized!)")
        last_size = curr_size

print("\n[SUMMARY] Dictionaries are compact, insertion-ordered, O(1) hash maps!")

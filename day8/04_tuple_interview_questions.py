"""
Day 08: Top Tuple Interview Questions & Brain Teasers
=====================================================
30-Day Full Stack Python + AI Engineering Challenge

Interview Questions & Classic Gotchas:
1. The Infamous '+=' on a Tuple with a List Trap (TypeError yet mutated!)
2. Multi-Key Sorting of Tuples (Lambda custom comparator)
3. Deep Flattening of Arbitrarily Nested Tuples
4. Find Duplicates in a Tuple maintaining first-seen order
5. Graph Edge Representation: (u, v, weight)
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 08 - TOPIC 04: TOP TUPLE INTERVIEW QUESTIONS & GOTCHAS]")
print("=" * 70)


# =========================================================================
# QUESTION 1: THE INFAMOUS '+=' ON TUPLE WITH LIST TRAP (PYTHON TRIVIA KING!)
# =========================================================================
print("\n--- 1. The '+=' on Tuple with List Trap ---")
print("What happens when we do: t = (1, 2, [3, 4]); t[2] += [5]?")

t = (1, 2, [3, 4])
print(f"Initial tuple : {t}")

try:
    t[2] += [5]
except TypeError as e:
    print(f"Exception raised: {type(e).__name__} -> {e}")

print(f"Tuple AFTER exception: {t}")
print("""
>> WHY THIS HAPPENS (CPython Bytecode Explanation):
   Step 1: 't[2] += [5]' executes '__iadd__' on the inner list.
           The inner list mutates IN-PLACE to [3, 4, 5].
   Step 2: Python then attempts 'STORE_SUBSCR' to assign the result back to t[2].
           Since 't' is an immutable tuple, STORE_SUBSCR raises TypeError!
   Result: The mutation succeeded, BUT an error was still raised!
""")


# =========================================================================
# QUESTION 2: MULTI-KEY SORTING ON TUPLES
# =========================================================================
print("\n--- 2. Multi-Key Sorting of Tuples (Lambda Comparator) ---")
# Problem: Sort candidates by score descending.
# If scores are tied, sort by age ascending.
candidates = [
    ("Rohit", 85, 23),
    ("Sapna", 95, 21),
    ("Aman",  85, 20),
    ("Pooja", 95, 22),
    ("Vikas", 75, 24)
]

print("Original Candidates (Name, Score, Age):")
for c in candidates:
    print(f"  {c}")

# Multi-key sort using lambda: (-score, age)
# Negative score reverses sorting order for score only!
sorted_candidates = sorted(candidates, key=lambda item: (-item[1], item[2]))

print("\nSorted Candidates (Score DESC, Age ASC):")
for c in sorted_candidates:
    print(f"  {c}")


# =========================================================================
# QUESTION 3: DEEP FLATTENING OF ARBITRARILY NESTED TUPLES
# =========================================================================
print("\n--- 3. Deep Flattening of Arbitrarily Nested Tuples ---")

def flatten_tuple(nested: tuple) -> tuple:
    """
    Recursively flattens an arbitrarily nested tuple into a single flat tuple.
    Example: ((1, 2), (3, (4, 5)), 6) -> (1, 2, 3, 4, 5, 6)
    """
    flat = []
    for item in nested:
        if isinstance(item, tuple):
            flat.extend(flatten_tuple(item))
        else:
            flat.append(item)
    return tuple(flat)

nested_input = ((1, 2), (3, (4, 5)), 6, (7, (8, (9,))))
flattened_result = flatten_tuple(nested_input)

print(f"Nested Tuple   : {nested_input}")
print(f"Flattened Tuple: {flattened_result}")


# =========================================================================
# QUESTION 4: FIND DUPLICATES IN TUPLE MAINTAINING ORDER
# =========================================================================
print("\n--- 4. Find Duplicate Elements in a Tuple ---")

def find_tuple_duplicates(tup: tuple) -> tuple:
    """
    Returns unique duplicate elements in the order they first repeat.
    Time: O(N) using Hash Set | Space: O(N)
    """
    seen = set()
    duplicates = []
    
    for item in tup:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
        
    return tuple(duplicates)

raw_tuple = (10, 20, 30, 20, 40, 10, 50, 10)
dups = find_tuple_duplicates(raw_tuple)
print(f"Input Tuple     : {raw_tuple}")
print(f"Duplicate Items : {dups}")


# =========================================================================
# QUESTION 5: GRAPH / NETWORK EDGE REPRESENTATION
# =========================================================================
print("\n--- 5. AI & Graph Application: Weighted Edges as Tuples ---")
# Graphs and neural network architectures often represent directed edges
# as immutable tuples: (source_node, target_node, weight)

graph_edges = [
    ("User_A", "User_B", 0.85),
    ("User_B", "User_C", 0.40),
    ("User_A", "User_C", 0.92)
]

print("Graph Edge List (Source -> Target, Weight):")
for u, v, weight in graph_edges:
    print(f"  {u} --({weight})--> {v}")

print("\n" + "=" * 70)
print("[OK] Top Tuple Interview Questions Module Completed Successfully!")
print("=" * 70)

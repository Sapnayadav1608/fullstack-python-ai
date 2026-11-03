"""
Day 08: Python Tuples - Creation, Immutability & Memory Internals
================================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. What is a Tuple? (Ordered, Immutable, Heterogeneous Sequence)
2. Tuple Creation Variations (Literals, Constructor, Packing without Parentheses)
3. The Classic Single-Element Tuple Comma Trap: (42) vs (42,)
4. Indexing, Negative Indexing & Slicing [start:stop:step]
5. Immutability Proof & Object Identity
6. The Famous "Mutable Object inside an Immutable Tuple" Trap
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 08 - TOPIC 01: TUPLE FUNDAMENTALS & CREATION]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. WHAT IS A TUPLE?
# -------------------------------------------------------------------------
# A tuple is an ordered, immutable collection of elements in Python.
# Like lists, tuples can hold heterogeneous data types.
# Unlike lists, tuples CANNOT be modified after creation (read-only).

sample_tuple = (10, "AI Engineer", 3.14, True, [1, 2])
print("\n--- 1. Tuple Creation ---")
print(f"sample_tuple       : {sample_tuple}")
print(f"Type               : {type(sample_tuple)}")
print(f"Length             : {len(sample_tuple)}")

# Empty tuple
empty_tup = ()
empty_constructor = tuple()
print(f"Empty tuple        : {empty_tup} (len={len(empty_tup)})")

# Tuple packing without parentheses (Comma is what actually creates a tuple!)
packed_coords = 19.0760, 72.8777
print(f"Packed Coordinates : {packed_coords} | Type: {type(packed_coords)}")


# -------------------------------------------------------------------------
# 2. THE CLASSIC SINGLE-ELEMENT COMMA TRAP (INTERVIEW FAVORITE!)
# -------------------------------------------------------------------------
print("\n--- 2. Single-Element Tuple Comma Trap ---")
# If you write (42) without a trailing comma, Python treats parentheses as
# mathematical grouping, NOT as a tuple!

not_a_tuple = (42)
is_a_tuple = (42,)

print(f"Expression: (42)  -> Type: {type(not_a_tuple).__name__:<8} | Value: {not_a_tuple}")
print(f"Expression: (42,) -> Type: {type(is_a_tuple).__name__:<8} | Value: {is_a_tuple}")
print(">> GOLDEN RULE: In Python, it is the COMMA (,) that defines a tuple, not parentheses!")


# -------------------------------------------------------------------------
# 3. INDEXING & SLICING (Same as Lists & Strings)
# -------------------------------------------------------------------------
print("\n--- 3. Indexing & Slicing Mechanics ---")
tech_stack = ("Python", "FastAPI", "PostgreSQL", "Docker", "PyTorch", "LangChain")

# Positive & Negative Indexing
print(f"First element (tech_stack[0])   : {tech_stack[0]}")
print(f"Last element  (tech_stack[-1])  : {tech_stack[-1]}")

# Slicing: creates a NEW tuple subsegment
print(f"Backend slice (tech_stack[0:3]) : {tech_stack[0:3]}")
print(f"AI tools slice(tech_stack[4:])  : {tech_stack[4:]}")
print(f"Reversed tuple(tech_stack[::-1]): {tech_stack[::-1]}")


# -------------------------------------------------------------------------
# 4. IMMUTABILITY PROOF
# -------------------------------------------------------------------------
print("\n--- 4. Immutability Proof ---")
config = ("localhost", 8000, "production")
print(f"Initial config: {config}")

try:
    # Attempting to reassign an index raises TypeError
    config[1] = 9000
except TypeError as error:
    print(f">> TypeError caught successfully: {error}")
    print("   Explanation: Tuples are immutable! You cannot assign, add, or delete elements.")


# -------------------------------------------------------------------------
# 5. THE "MUTABLE OBJECT INSIDE IMMUTABLE TUPLE" TRAP
# -------------------------------------------------------------------------
print("\n--- 5. The Mutable Object inside Immutable Tuple Trap ---")
# Question: If a tuple contains a list, can you modify that list?
# YES! The tuple stores the reference (pointer) to the list.
# The pointer cannot be changed to another list, but the list itself can mutate!

nested_tup = ("Version 1.0", [10, 20, 30])
print(f"Before mutating inner list: {nested_tup}")
print(f"Tuple ID: {id(nested_tup)} | Inner List ID: {id(nested_tup[1])}")

# Modifying the list inside the tuple
nested_tup[1].append(40)
nested_tup[1][0] = 999

print(f"After mutating inner list : {nested_tup}")
print(f"Tuple ID: {id(nested_tup)} | Inner List ID: {id(nested_tup[1])}")
print(">> KEY TAKEAWAY: Tuple immutability protects reference pointers,")
print("   NOT the internal state of nested mutable objects!")

print("\n" + "=" * 70)
print("[OK] Tuple Fundamentals & Creation Module Executed Successfully!")
print("=" * 70)

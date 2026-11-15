# =============================================================================
# DAY 11 - MODULE 04: Lambdas, Functional Built-ins & Recursion Engineering
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Topics Covered:
# 1. Anonymous Lambda Functions (Syntax, Limitations & Key Extraction)
# 2. Multi-Key Sorting with Lambdas (Complex Dictionary & Object Ordering)
# 3. Functional Built-ins: map(), filter(), functools.reduce() vs Comprehensions
# 4. Recursion Architecture: Base Cases, Recursive Steps & Call Stack Memory Frames
# 5. Top Interview Problem: Recursive Nested JSON / Dictionary Flattener (ETL)
# =============================================================================

import sys
from functools import reduce
from typing import Dict, Any, List

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 11 - MODULE 04: LAMBDAS, FUNCTIONAL PATTERNS & RECURSION")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. ANONYMOUS LAMBDA FUNCTIONS
# -----------------------------------------------------------------------------
print("\n--- 1. Anonymous Lambda Functions ---")

# Syntax: lambda arg1, arg2, ... : expression
# Rules:
# - Can take any number of arguments.
# - Can only contain a SINGLE expression that is evaluated and returned automatically.
# - Cannot contain statements (no 'return', 'pass', 'assert', or variable assignments).

add = lambda a, b: a + b
print(f"Lambda add(15, 25) = {add(15, 25)}")

# Idiomatic Use: Inline throwaway functions
temperatures_c = [0, 20, 25, 30, 37, 100]
temperatures_f = list(map(lambda c: (c * 9/5) + 32, temperatures_c))
print("Temperatures in Celsius    :", temperatures_c)
print("Converted to Fahrenheit (F):", temperatures_f)


# -----------------------------------------------------------------------------
# 2. MULTI-KEY SORTING WITH LAMBDAS (INTERVIEW FAVORITE)
# -----------------------------------------------------------------------------
print("\n--- 2. Multi-Key Sorting with Lambdas ---")

developers = [
    {"name": "Alice",   "department": "AI",      "salary": 160000, "experience": 4},
    {"name": "Bob",     "department": "Backend", "salary": 140000, "experience": 6},
    {"name": "Charlie", "department": "AI",      "salary": 160000, "experience": 7},
    {"name": "Diana",   "department": "DevOps",  "salary": 150000, "experience": 5},
    {"name": "Ethan",   "department": "Backend", "salary": 140000, "experience": 3},
]

# Problem: Sort developers primarily by salary DESCENDING (-salary),
# and secondary by experience DESCENDING (-experience)!
sorted_devs = sorted(
    developers,
    key=lambda d: (-d["salary"], -d["experience"])
)

print("Sorted Developers (Salary DESC, Experience DESC):")
for dev in sorted_devs:
    print(f"  - {dev['name']:<8} | Dept: {dev['department']:<8} | ${dev['salary']:,} | Exp: {dev['experience']} yrs")


# -----------------------------------------------------------------------------
# 3. FUNCTIONAL BUILT-INS: map(), filter(), reduce()
# -----------------------------------------------------------------------------
print("\n--- 3. Functional Built-ins vs List Comprehensions ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(predicate_fn, iterable): Keeps items where predicate returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered Evens (filter) :", evens)

# map(transform_fn, iterable): Transforms every item
doubles = list(map(lambda x: x * 2, evens))
print("Doubled Evens (map)     :", doubles)

# functools.reduce(fn, iterable, [initial]): Cumulative folding of elements
# e.g. Compute product of all numbers: 1 * 2 * 3 * ... * 10
total_product = reduce(lambda acc, val: acc * val, numbers)
print("Factorial of 10 (reduce):", total_product)

# Pythonic Guideline:
# In modern Python, List Comprehensions are often preferred over simple map/filter
# because they are cleaner to read and compile to direct bytecode without function call overhead:
comp_equivalent = [x * 2 for x in numbers if x % 2 == 0]
print("List Comprehension Eq   :", comp_equivalent)


# -----------------------------------------------------------------------------
# 4. RECURSION ARCHITECTURE & CALL STACK
# -----------------------------------------------------------------------------
print("\n--- 4. Recursion Architecture & Stack Frame Dynamics ---")

# Recursion requires 2 critical components:
# 1. Base Case: Halting condition that returns without calling itself.
# 2. Recursive Step: Moves the input problem closer to the base case.

def factorial_with_trace(n: int, depth: int = 0) -> int:
    indent = "  " * depth
    print(f"{indent}--> Entering factorial({n}) [Stack Frame #{depth}]")
    
    # 1. Base Case
    if n <= 1:
        print(f"{indent}<-- Base Case reached: factorial(1) = 1 [Popping frame]")
        return 1
        
    # 2. Recursive Step
    result = n * factorial_with_trace(n - 1, depth + 1)
    print(f"{indent}<-- Returning: {n} * factorial({n-1}) = {result} [Popping frame]")
    return result

print("Tracing Factorial(4) Call Stack:")
fact_4 = factorial_with_trace(4)
print(f"Final Factorial(4) Result: {fact_4}")

# Recursion Limit Safety:
print(f"\nDefault CPython Recursion Limit: {sys.getrecursionlimit()} frames")


# -----------------------------------------------------------------------------
# 5. TOP INTERVIEW PROBLEM: RECURSIVE NESTED DICT FLATTENER (ETL)
# -----------------------------------------------------------------------------
print("\n--- 5. Top Interview Problem: Recursive Nested Dict Flattener ---")

# Problem: Convert an arbitrarily deep nested dictionary into a flattened
# dot-notation dictionary for JSON/Database processing.
nested_api_payload = {
    "user": {
        "id": 101,
        "profile": {
            "name": "Sapna Yadav",
            "socials": {
                "github": "Sapnayadav1608",
                "role": "AI Engineer"
            }
        }
    },
    "metadata": {
        "active": True,
        "tier": "Pro"
    },
    "version": 2.1
}

def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Recursively flattens nested dictionary keys with dot separator."""
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            # Recursive step: Flattens child dict and merges with update
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            # Base case: Primitive value is assigned
            items[new_key] = v
    return items

flattened_result = flatten_dict(nested_api_payload)
print("Flattened Dictionary (Dot-Notation):")
for flat_key, flat_val in flattened_result.items():
    print(f"  {flat_key:<28} -> {flat_val}")

print("\n" + "=" * 75)
print("✅ MODULE 04 COMPLETE: Lambdas, functional built-ins & recursion mastered!")
print("=" * 75)

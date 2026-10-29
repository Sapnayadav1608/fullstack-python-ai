# =============================================================================
# DAY 04 - TOPIC 04: Space Complexity & Memory Call Stack
# =============================================================================
# Program RAM (Memory) kitni consume karta hai as input grows.
# Space Complexity = Auxiliary Space (Extra space) + Input Space
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 04 - TOPIC 04] Space Complexity & Recursion Call Stack")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. O(1) Space vs O(N) Space:
# -----------------------------------------------------------------------------

# Case A: O(1) Auxiliary Space
# Chahe list mein 10 items hon ya 1 Crore, sirf 1 variable 'total' memory mein hai.
def sum_constant_space(numbers: list) -> int:
    total = 0  # O(1) space
    for n in numbers:
        total += n
    return total

# Case B: O(N) Auxiliary Space
# Naya list ya duplicate data structure create karna jo N size ka ho:
def square_all_numbers(numbers: list) -> list:
    squared_list = []  # O(N) space! N naye elements RAM mein store honge
    for n in numbers:
        squared_list.append(n * n)
    return squared_list

print("Case A: In-place accumulators / pointers -> O(1) Space")
print("Case B: New lists / dictionaries / sets -> O(N) Space")


# -----------------------------------------------------------------------------
# 2. Recursion Call Stack Memory:
# -----------------------------------------------------------------------------
# Jab bhi ek function doosre function ko call karta hai, Python RAM mein
# ek 'Stack Frame' banata hai.
# Agar recursion N depth tak jaati hai, toh Space Complexity O(N) hoti hai!

# Recursive Countdown: O(N) Time AND O(N) Space (Stack frames accumulate)
def recursive_countdown(n: int):
    if n <= 0:
        return
    recursive_countdown(n - 1)

# Iterative Countdown: O(N) Time BUT O(1) Space! (Zero extra stack frames)
def iterative_countdown(n: int):
    while n > 0:
        n -= 1

print("\nRecursion Memory Concept:")
print("- Iterative loop uses O(1) stack memory.")
print("- Recursive function of depth N uses O(N) stack memory.")
print("  (Python default recursion limit: 1,000 frames -> RecursionError!)")


# -----------------------------------------------------------------------------
# 3. String Traps in Space Complexity:
# -----------------------------------------------------------------------------
# s[::-1] creates a full new string in memory -> O(N) Space
# s.split() creates a list of all words in memory -> O(N) Space
# Two-pointer in-place traversal -> O(1) Space!
print("\nString Traps:")
print("- s[::-1] allocates O(N) new memory.")
print("- Two-Pointer comparison allocates O(1) memory.")

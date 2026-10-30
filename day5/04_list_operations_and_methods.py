# =============================================================================
# DAY 05 - TOPIC 04: List Operations & Sorting Methods
# =============================================================================
# Concatenation (+), Repetition (*), Membership (in),
# .sort() in-place vs sorted() function, custom key sorting.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 05 - TOPIC 04] List Operations & Sorting Methods")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. Operators on Lists (+, *, in)
# -----------------------------------------------------------------------------
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Concatenation (+) -> Returns a new combined list
combined = list_a + list_b
print(f"{list_a} + {list_b} = {combined}")

# Repetition (*)
zeroes = [0] * 5
print(f"[0] * 5 = {zeroes}")

# Membership (in, not in) -> O(N) linear search
print("3 in combined      ->", 3 in combined)       # True
print("10 not in combined ->", 10 not in combined)   # True


# -----------------------------------------------------------------------------
# 2. Searching & Counting (.index(), .count())
# -----------------------------------------------------------------------------
frameworks = ["FastAPI", "Django", "Flask", "FastAPI", "Tornado"]
print("\nFrameworks:", frameworks)
print("count('FastAPI') ->", frameworks.count("FastAPI"))  # 2
print("index('Django')  ->", frameworks.index("Django"))   # 1


# -----------------------------------------------------------------------------
# 3. .sort() vs sorted() (Classic Interview Distinction!)
# -----------------------------------------------------------------------------
# .sort():
# - List ka IN-PLACE method hai (original list badal deta hai).
# - Return 'None' karta hai! (Beginner mistake: s = my_list.sort() -> s is None!)
# - Algorithm: Timsort -> O(n log n) Time, O(n) Space.

nums = [45, 12, 89, 3, 27]
print(f"\nOriginal nums: {nums}")

sort_return = nums.sort()
print(f"nums.sort() modified nums to: {nums}")
print(f"nums.sort() returned        : {sort_return} (Always None!)")

# sorted(iterable):
# - Python ka global built-in function hai.
# - Original list ko touch NAHI karta, ek NAYI sorted list return karta hai.
original = [5, 2, 9, 1]
new_sorted = sorted(original, reverse=True)
print(f"\noriginal list intact : {original}")
print(f"sorted(reverse=True) : {new_sorted}")


# -----------------------------------------------------------------------------
# 4. Custom Key Sorting (Super Useful in Full Stack / Backend!)
# -----------------------------------------------------------------------------
users = [
    {"name": "Sapna", "tokens": 450},
    {"name": "Aman", "tokens": 120},
    {"name": "Pooja", "tokens": 890}
]

# Sort by tokens ascending:
users.sort(key=lambda u: u["tokens"])
print("\nUsers sorted by tokens:")
for u in users:
    print(f"  {u['name']:<8}: {u['tokens']} tokens")

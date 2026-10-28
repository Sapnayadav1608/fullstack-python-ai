# =============================================================================
# DAY 03 - PROBLEM 07: Tricky Python String Interview Questions & Outputs
# =============================================================================
# Interviews mein pooche jaane wale tricky output aur conceptual traps.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 03 - PROBLEM 07] Tricky String Interview Questions")
print("=" * 60)

# -----------------------------------------------------------------------------
# TRICK 1: Out of Bounds Indexing vs Slicing
# -----------------------------------------------------------------------------
s = "Python"
print("--- Trick 1: Indexing vs Slicing Boundary ---")
# print(s[10])   -> ❌ IndexError crash!
print("s[10:] ->", repr(s[10:]))  # ✔️ Empty string "" (Slicing never throws IndexError!)


# -----------------------------------------------------------------------------
# TRICK 2: Negative Step Slicing Trap
# -----------------------------------------------------------------------------
nums = "0123456789"
print("\n--- Trick 2: nums[7:2:-1] ka Output kya hoga? ---")
# Start = 7 ('7'), Stop = 2 (Excluded!), Step = -1 (Backwards)
# Characters: 7, 6, 5, 4, 3 (Index 2 par '2' hai jo EXCLUDE hoga)
print("nums[7:2:-1] ->", nums[7:2:-1])  # '76543'


# -----------------------------------------------------------------------------
# TRICK 3: Repetition with 0 or Negative numbers
# -----------------------------------------------------------------------------
print("\n--- Trick 3: String * 0 or negative ---")
print("'Python' * 0  ->", repr("Python" * 0))   # "" (Empty string)
print("'Python' * -2 ->", repr("Python" * -2))  # "" (Empty string, no error!)


# -----------------------------------------------------------------------------
# TRICK 4: Logical Operators ('and' / 'or') with Strings
# Python mein: Non-empty string is TRUTHY, Empty string is FALSY
# -----------------------------------------------------------------------------
print("\n--- Trick 4: Short-Circuit Logical Evaluation ---")
# 'and' pehla Falsy value return karta hai, ya fir aakhiri Truthy
print("'apple' and 'banana' ->", repr('apple' and 'banana'))  # 'banana'
print("'' and 'banana'      ->", repr('' and 'banana'))       # ''

# 'or' pehla Truthy value return karta hai
print("'apple' or 'banana'  ->", repr('apple' or 'banana'))   # 'apple'
print("'' or 'banana'       ->", repr('' or 'banana'))        # 'banana'


# -----------------------------------------------------------------------------
# TRICK 5: join() on Non-String Iterable (Common Bug)
# -----------------------------------------------------------------------------
print("\n--- Trick 5: .join() Trap ---")
numbers_list = [1, 2, 3, 4]
try:
    print("-".join(numbers_list))
except TypeError as e:
    print("[TypeError Caught]:", e)
    # Solution: List comprehension se pehle strings convert karein
    clean_joined = "-".join(str(n) for n in numbers_list)
    print("Sahi tareeqa     :", clean_joined)  # '1-2-3-4'


# -----------------------------------------------------------------------------
# TRICK 6: find() vs index() on missing substring
# -----------------------------------------------------------------------------
print("\n--- Trick 6: find() vs index() for missing character ---")
word = "Artificial"
print("word.find('z')  ->", word.find('z'))   # -1 (Safe, condition if idx != -1)
try:
    print("word.index('z') ->", word.index('z'))
except ValueError as e:
    print("word.index('z') -> Throws ValueError! Crash risk.")


# -----------------------------------------------------------------------------
# TRICK 7: String Interning 'is' vs '=='
# -----------------------------------------------------------------------------
print("\n--- Trick 7: String Interning ---")
# Identifiers without spaces/symbols are interned
x = "developer"
y = "developer"
print(f"'{x}' is '{y}'? {x is y}")  # True (Same memory address)

# Special characters ya dynamic strings hamesha intern nahi hoti
p = "full stack!"
q = "full stack!"
print(f"'{p}' == '{q}'? {p == q}")  # True (Value same hai)

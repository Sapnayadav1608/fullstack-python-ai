# =============================================================================
# DAY 02 - TOPIC 03: String Slicing Mastery
# =============================================================================
# Slicing Syntax: string[start : stop : step]
# - start: inclusion index (Default: 0 for positive step, -1 for negative step)
# - stop: EXCLUDED index (stop index se ek pehle tak chalta hai!)
# - step: jump size & direction (+ve = left to right, -ve = right to left)
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 03] String Slicing Mastery")
print("=" * 60)

text = "DataScience"
# Index:  D  a  t  a  S  c  i  e  n  c  e
# Pos:    0  1  2  3  4  5  6  7  8  9  10

# 1. Basic Slicing [start : stop]
print("text[0:4]   ->", text[0:4])   # 'Data' (0 se 3 tak)
print("text[4:11]  ->", text[4:11])  # 'Science' (4 se 10 tak)
print("text[:4]    ->", text[:4])    # Default start = 0 -> 'Data'
print("text[4:]    ->", text[4:])    # Default stop = end -> 'Science'
print("text[:]     ->", text[:])     # Poora string clone ho gaya

# 2. Step Slicing [start : stop : step]
alphabet = "ABCDEFGHIJ"
print("\nalphabet       :", alphabet)
print("alphabet[::2]  :", alphabet[::2])   # 'ACEGI' (2-2 ka jump)
print("alphabet[1::2] :", alphabet[1::2])  # 'BDFHJ' (Odd index wale)

# 3. Negative Step & Reverse Slicing (Interview Favorite)
# Jab step NEGATIVE hota hai, toh direction right-to-left ho jaati hai!
print("\n--- Negative Step Tricks ---")
print("alphabet[::-1]     ->", alphabet[::-1])     # Poora string reverse: 'JIHGFEDCBA'
print("alphabet[7:2:-1]   ->", alphabet[7:2:-1])   # Index 7 se 3 tak backwards: 'HGFED'
print("alphabet[::-2]     ->", alphabet[::-2])     # Peeche se alternate letters: 'JHFDB'

# 4. Slicing Kabhi IndexError Nahi Deta! (Safe Feature)
# Indexing mein out-of-range index error deta hai, lekin slicing gracefully handle karti hai:
print("\nSafe Slicing beyond length:")
print("text[4:100] ->", repr(text[4:100]))  # 'Science' (No crash!)

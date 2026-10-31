"""
=============================================================================
  DAY 06: LIST COMPREHENSIONS & NESTED LISTS (MY PRACTICE WORKBOOK)
=============================================================================
Name: Sapna Yadav
Topic: List Comprehensions, Nested Lists, Matrix Traversals & Practical Problems
Instructions:
- Har task ka concept samjhein aur niche diye gaye blank space mein KHUD code type karein.
- Terminal se run karke test karein: python day6/my_practice.py
=============================================================================
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("🚀 DAY 6: LIST COMPREHENSIONS HANDS-ON WORKBOOK")
print("=" * 60)


# -----------------------------------------------------------------------------
# TASK 1: Filter & Square Comprehension
# -----------------------------------------------------------------------------
# 1 se 20 tak ke numbers mein se sirf un numbers ke squares nikaalein jo 3 se
# divide hote hain (num % 3 == 0).
# Output expected: [9, 36, 81, 144, 225, 324]

print("\n--- [Task 1] Filter & Square ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 2: if-else Transformation
# -----------------------------------------------------------------------------
# Di gayi numbers ki list:
scores = [45, 92, 38, 77, 85, 29, 64]
# Agar score >= 50 hai toh "Pass", warna "Fail" store karein comprehension se:

print("\n--- [Task 2] if-else Transformation ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 3: Flatten a 2D Matrix
# -----------------------------------------------------------------------------
# Di gayi 2D list ko 1D list mein flatten karein:
grid = [
    ["Python", "FastAPI"],
    ["Docker", "Kubernetes"],
    ["PostgreSQL", "Redis"]
]
# Expected Output: ['Python', 'FastAPI', 'Docker', 'Kubernetes', 'PostgreSQL', 'Redis']

print("\n--- [Task 3] Flatten Matrix ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 4: Safe 2D Grid Creation (Avoid the [[0]*4]*4 Bug!)
# -----------------------------------------------------------------------------
# 1. List comprehension use karke ek 4x4 matrix banayein jismein '.' filled ho.
# 2. Position [0][0] par 'Q' (Queen) rakhein.
# 3. Print karke verify karein ki sirf ek hi position par 'Q' aaya hai, saari rows par nahi!

print("\n--- [Task 4] Safe Grid Creation ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 5: Real-World String Cleaning & Filtering
# -----------------------------------------------------------------------------
user_prompts = [
    "  explain transformer architecture  ",
    "",
    "hi",
    "   how to optimize postgresql queries?   ",
    "   ",
    "ok"
]
# Task: Strip spaces, aur sirf wahi prompts rakhein jinki length > 5 characters ho:

print("\n--- [Task 5] Prompt Cleaning & Length Filter ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 6: MINI CHALLENGE - Matrix Diagonal Sum
# -----------------------------------------------------------------------------
# Di gayi 3x3 square matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Task: List comprehension aur sum() use karke primary diagonal (1 + 5 + 9)
# ka total sum ek clean line mein calculate karein!
# Expected Output: 15

print("\n--- [Task 6] Mini Challenge: Diagonal Sum ---")
# TODO: Apna code yahan likhein:




print("\n" + "=" * 60)
print("🎉 Great Job! Day 6 Comprehension Practice Completed!")
print("=" * 60)

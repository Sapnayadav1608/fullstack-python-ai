"""
=============================================================================
  DAY 05: PYTHON LISTS (MY PRACTICE WORKBOOK)
=============================================================================
Name: Sapna Yadav
Topic: Python Lists — Memory Architecture, Operations, Methods & Slicing
Instructions:
- Har task ka concept samjhein aur niche diye gaye blank space mein KHUD code type karein.
- Terminal se run karke test karein: python day5/my_practice.py
=============================================================================
"""

import sys
import copy

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("🚀 DAY 5: PYTHON LISTS HANDS-ON WORKBOOK")
print("=" * 60)


# -----------------------------------------------------------------------------
# TASK 1: Referential Array & Memory Address Check
# -----------------------------------------------------------------------------
# 1. Ek list banayein jismein int, float, string aur boolean ho.
# 2. Loop chala kar har element ka value aur uska memory address (id) print karein.
# 3. List ka apna id() print karein aur verify karein ki list ek referential array hai.

print("\n--- [Task 1] Referential Memory Check ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 2: Slicing & Slice Assignment Mutation
# -----------------------------------------------------------------------------
# Di gayi list:
numbers = [10, 20, 30, 40, 50, 60, 70]

# 1. Slicing se list ke beech ke elements [30, 40, 50] ko [333, 444, 555] se replace karein.
# 2. Negative slicing use karke poori list ko reverse print karein.

print("\n--- [Task 2] Slice Assignment & Reverse ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 3: append() vs extend() Trap
# -----------------------------------------------------------------------------
# 1. Ek list 'cart' banayein: ['Laptop', 'Mouse']
# 2. Nayi items ki list ['Keyboard', 'Monitor'] ko .append() karke dekhein (kya output aaya?).
# 3. Phir usi list par .extend(['Headphones', 'Mic']) karke dekhein aur dono ka difference samjhein.

print("\n--- [Task 3] append vs extend ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 4: pop() vs remove() vs del
# -----------------------------------------------------------------------------
# Di gayi list:
tasks = ["Setup DB", "Write API", "Code Review", "Deploy", "Write API"]

# 1. .pop() se aakhiri task remove karein aur print karein.
# 2. .remove() se pehla "Write API" remove karein.
# 3. del keyword se index 0 wala item delete karein.

print("\n--- [Task 4] Removal Methods ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 5: The Shallow Copy Bug & Deep Copy Fix
# -----------------------------------------------------------------------------
# Di gayi nested list:
project_matrix = [["API", "Auth"], ["Frontend", "UI"]]

# 1. project_matrix ka ek shallow copy banayein (.copy()).
# 2. project_matrix ka ek deep copy banayein (copy.deepcopy()).
# 3. Dono copies ke inner item ko modify karke dekhein ki original par kya asar hota hai!

print("\n--- [Task 5] Shallow vs Deep Copy Experiment ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 6: Sorting with Custom Key Lambda
# -----------------------------------------------------------------------------
# Students data diya gaya hai:
students = [
    {"name": "Sapna", "score": 92},
    {"name": "Aman", "score": 78},
    {"name": "Pooja", "score": 95},
    {"name": "Karan", "score": 85}
]

# 1. Students ko unke score ke hisaab se DESCENDING (highest first) order mein sort karein.
# 2. Formatted output print karein.

print("\n--- [Task 6] Custom Key Sorting ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 7: MINI CHALLENGE - Rotate List by K Steps
# -----------------------------------------------------------------------------
# Problem: List ko K steps right side rotate karein slicing use karke!
# Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]
# Hint:   Slicing trick: nums[-k:] + nums[:-k]

print("\n--- [Task 7] Mini Challenge: List Rotation ---")
# TODO: Apna code yahan likhein:




print("\n" + "=" * 60)
print("🎉 Great Job! Day 5 List Practice Completed!")
print("=" * 60)

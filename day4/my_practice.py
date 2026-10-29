"""
=============================================================================
  DAY 04: TIME COMPLEXITY & BIG O (MY PRACTICE WORKBOOK)
=============================================================================
Name: Sapna Yadav
Topic: Big O Notation, Time & Space Complexity, Algorithm Optimization
Instructions:
- Har question ka code dekhein, uska Big O analyze karein aur TODO section mein answer likhein.
- Terminal se run karke test karein: python day4/my_practice.py
=============================================================================
"""

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("🚀 DAY 4: TIME & SPACE COMPLEXITY WORKBOOK")
print("=" * 60)


# -----------------------------------------------------------------------------
# TASK 1: Calculate Big O for this function
# -----------------------------------------------------------------------------
# Function:
def find_maximum(numbers: list):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# TODO: Niche likhein:
# Time Complexity  : O(?)
# Space Complexity : O(?)
# Explanation      : ?




# -----------------------------------------------------------------------------
# TASK 2: Calculate Big O for this Nested Loop
# -----------------------------------------------------------------------------
# Function:
def print_grid_pairs(n: int):
    for i in range(n):
        for j in range(n):
            print(f"({i}, {j})", end=" ")
        print()

# TODO: Niche likhein:
# Time Complexity  : O(?)
# Space Complexity : O(?)




# -----------------------------------------------------------------------------
# TASK 3: Tricky While Loop Analysis
# -----------------------------------------------------------------------------
# Function:
def divide_by_two_loop(n: int):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

# TODO: Niche likhein:
# Time Complexity  : O(?)
# Reason           : ?




# -----------------------------------------------------------------------------
# TASK 4: Code Optimization Challenge (Convert O(N^2) to O(N))
# -----------------------------------------------------------------------------
# Problem: Check if a list has any duplicates.
#
# Slow O(N^2) code:
def has_duplicates_slow(items: list) -> bool:
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            if items[i] == items[j]:
                return True
    return False

# TODO: Iska O(N) optimized version likhein (Hint: Use set):
def has_duplicates_fast(items: list) -> bool:
    # Apna code yahan likhein:
    pass




# -----------------------------------------------------------------------------
# TASK 5: Compare String Building Efficiency (String '+=' vs ''.join())
# -----------------------------------------------------------------------------
# 1. 50,000 numbers ko string mein convert karke jodiye (+= se).
# 2. Phir wahi 50,000 numbers ko list mein append karke ''.join() se jodiye.
# 3. time.perf_counter() se dono ka time difference measure karke print karein!

print("\n--- [Task 5] String Benchmark Challenge ---")
# TODO: Apna code yahan likhein:




print("\n" + "=" * 60)
print("🎉 Great Job! Day 4 Big O Practice Completed!")
print("=" * 60)

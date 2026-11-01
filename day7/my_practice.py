"""
Day 07: Hands-On Practice Workbook - List Interview Problems & Bug Fixes
========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Instructions for Sapna:
------------------------
1. Read the problem descriptions and requirements carefully.
2. Complete each function inside the '# TODO: Write your code here' sections.
3. Run the file: python day7/my_practice.py
4. Check the test assertions at the bottom to verify if all your solutions pass!
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[SAPNA'S DAY 07 PRACTICE WORKBOOK: LIST INTERVIEWS & REVISION]")
print("=" * 70)


# =========================================================================
# TASK 1: Two Sum with Hash Map [O(N) Time, O(N) Space]
# =========================================================================
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given a list of integers `nums` and an integer `target`, return indices
    of the two numbers such that they add up to target.
    
    Requirement: Must run in O(N) time using a dictionary/hash map.
    Example: nums = [2, 7, 11, 15], target = 9 -> returns [0, 1]
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 2: Move Zeroes In-Place [O(N) Time, O(1) Space]
# =========================================================================
def move_zeroes(nums: list[int]) -> list[int]:
    """
    Move all 0's to the end of nums while maintaining relative order of non-zero elements.
    
    Requirement: Modify nums IN-PLACE without creating a new copy!
    Example: [0, 1, 0, 3, 12] -> modifies to [1, 3, 12, 0, 0]
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 3: Maximum Subarray Sum (Kadane's Algorithm) [O(N) Time]
# =========================================================================
def max_sub_array(nums: list[int]) -> int:
    """
    Given an integer array `nums`, find the subarray with the largest sum,
    and return its sum.
    
    Requirement: Kadane's Algorithm in O(N) time and O(1) space.
    Example: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> returns 6 (from [4, -1, 2, 1])
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 4: Majority Element (Boyer-Moore Voting) [O(N) Time, O(1) Space]
# =========================================================================
def majority_element(nums: list[int]) -> int:
    """
    Given an array `nums` of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    
    Requirement: Use Boyer-Moore Voting algorithm for O(1) space.
    Example: [3, 2, 3] -> returns 3
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 5: Rotate Array by K Steps In-Place [O(N) Time, O(1) Space]
# =========================================================================
def rotate_array(nums: list[int], k: int) -> list[int]:
    """
    Rotate the array to the right by k steps, where k is non-negative.
    
    Requirement: In-place using the 3-step reversal algorithm.
    Example: nums = [1, 2, 3, 4, 5, 6, 7], k = 3 -> modifies to [5, 6, 7, 1, 2, 3, 4]
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 6: Fix the Default Mutable Argument Bug
# =========================================================================
def record_student_mark(student: str, marks_list=None) -> list[str]:
    """
    Fix the classic mutable default argument bug!
    If marks_list is not provided, initialize a fresh list for each call.
    Appends student to marks_list and returns it.
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 7: Safe Even Number Filter
# =========================================================================
def remove_evens_safe(nums: list[int]) -> list[int]:
    """
    Given a list of numbers, return a list containing only the odd numbers.
    Avoid the index skipping bug by using a list comprehension or safe iteration.
    Example: [1, 2, 2, 3, 4, 4, 5] -> returns [1, 3, 5]
    """
    # TODO: Write your code here
    pass


# =========================================================================
# AUTOMATED TEST SUITE (Run this file to verify your solutions!)
# =========================================================================
if __name__ == "__main__":
    print("\n--- Running Automated Verification Checks ---")
    passed = 0
    total = 7

    # Check Task 1
    try:
        t1 = two_sum([2, 7, 11, 15], 9)
        assert t1 == [0, 1] or t1 == [1, 0], f"Expected [0, 1], got {t1}"
        print("[PASS] Task 1: Two Sum with Hash Map")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 1 not yet completed: {e}")

    # Check Task 2
    try:
        t2_list = [0, 1, 0, 3, 12]
        move_zeroes(t2_list)
        assert t2_list == [1, 3, 12, 0, 0], f"Expected [1, 3, 12, 0, 0], got {t2_list}"
        print("[PASS] Task 2: Move Zeroes In-Place")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 2 not yet completed: {e}")

    # Check Task 3
    try:
        t3 = max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        assert t3 == 6, f"Expected 6, got {t3}"
        print("[PASS] Task 3: Kadane's Maximum Subarray")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 3 not yet completed: {e}")

    # Check Task 4
    try:
        t4 = majority_element([2, 2, 1, 1, 1, 2, 2])
        assert t4 == 2, f"Expected 2, got {t4}"
        print("[PASS] Task 4: Boyer-Moore Majority Element")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 4 not yet completed: {e}")

    # Check Task 5
    try:
        t5_list = [1, 2, 3, 4, 5, 6, 7]
        rotate_array(t5_list, 3)
        assert t5_list == [5, 6, 7, 1, 2, 3, 4], f"Expected [5, 6, 7, 1, 2, 3, 4], got {t5_list}"
        print("[PASS] Task 5: Rotate Array by K steps")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 5 not yet completed: {e}")

    # Check Task 6
    try:
        first_call = record_student_mark("Sapna")
        second_call = record_student_mark("Aman")
        assert first_call == ["Sapna"], f"Expected ['Sapna'], got {first_call}"
        assert second_call == ["Aman"], f"Expected ['Aman'], got {second_call}"
        print("[PASS] Task 6: Mutable Default Argument Bug Fixed")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 6 not yet completed: {e}")

    # Check Task 7
    try:
        t7 = remove_evens_safe([1, 2, 2, 3, 4, 4, 5])
        assert t7 == [1, 3, 5], f"Expected [1, 3, 5], got {t7}"
        print("[PASS] Task 7: Safe Even Number Filter")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 7 not yet completed: {e}")

    print("\n" + "=" * 70)
    print(f"Summary: {passed}/{total} Tasks Completed!")
    if passed == total:
        print("CONGRATULATIONS SAPNA! All Week 1 interview coding challenges passed!")
    else:
        print("Keep going! Open this file and write your logic inside each TODO function.")
    print("=" * 70)

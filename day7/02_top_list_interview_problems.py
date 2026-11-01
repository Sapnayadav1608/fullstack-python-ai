"""
Day 07: Top List Coding Interview Problems & Optimal Patterns
=============================================================
30-Day Full Stack Python + AI Engineering Challenge

Classic FAANG / Product-Company List Interview Questions:
1. Two Sum (LeetCode #1) - Hash Map Pattern [O(N) Time, O(N) Space]
2. Move Zeroes (LeetCode #283) - In-Place Two Pointers [O(N) Time, O(1) Space]
3. Maximum Subarray Sum (LeetCode #53) - Kadane's Algorithm [O(N) Time, O(1) Space]
4. Majority Element (LeetCode #169) - Boyer-Moore Voting Algorithm [O(N) Time, O(1) Space]
5. Rotate Array by K steps (LeetCode #189) - 3-Reversal Technique [O(N) Time, O(1) Space]
6. Merge Sorted Arrays in-place (LeetCode #88) - Three Pointers from End [O(M+N) Time, O(1) Space]
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[TOP LIST CODING INTERVIEW PATTERNS]")
print("=" * 70)


# =========================================================================
# PROBLEM 1: TWO SUM (LeetCode #1)
# =========================================================================
print("\n" + "=" * 50)
print("1. TWO SUM: Target Sum Pair")
print("=" * 50)

def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """Time: O(N^2) | Space: O(1)"""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_optimal(nums: list[int], target: int) -> list[int]:
    """Time: O(N) | Space: O(N) using Hash Map for O(1) lookups"""
    seen = {}  # complement -> index
    for current_idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], current_idx]
        seen[num] = current_idx
    return []

nums_1 = [2, 7, 11, 15]
target_1 = 9
print(f"Input: nums={nums_1}, target={target_1}")
print(f"Brute Force Result : {two_sum_brute_force(nums_1, target_1)} [O(N^2)]")
print(f"Optimal Hash Map   : {two_sum_optimal(nums_1, target_1)} [O(N)]")


# =========================================================================
# PROBLEM 2: MOVE ZEROES IN-PLACE (LeetCode #283)
# =========================================================================
print("\n" + "=" * 50)
print("2. MOVE ZEROES: In-Place Two Pointers")
print("=" * 50)

def move_zeroes(nums: list[int]) -> list[int]:
    """
    Moves all zeroes to end while maintaining order of non-zero elements.
    Time: O(N) | Space: O(1) in-place
    """
    last_non_zero_found_at = 0
    
    # Pass 1: Swap non-zero elements forward
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1
            
    return nums

nums_2 = [0, 1, 0, 3, 12]
print(f"Before move_zeroes : {nums_2}")
move_zeroes(nums_2)
print(f"After move_zeroes  : {nums_2} (Zeroes moved, non-zero order preserved)")


# =========================================================================
# PROBLEM 3: MAXIMUM SUBARRAY - KADANE'S ALGORITHM (LeetCode #53)
# =========================================================================
print("\n" + "=" * 50)
print("3. MAXIMUM SUBARRAY: Kadane's Algorithm")
print("=" * 50)

def max_sub_array_kadane(nums: list[int]) -> int:
    """
    Finds contiguous subarray with the largest sum.
    Time: O(N) | Space: O(1)
    
    Kadane's Decision at each element:
    Should I add the current number to the existing chain,
    OR should I start a fresh subarray from this number?
    """
    max_so_far = nums[0]
    current_max = nums[0]
    
    for num in nums[1:]:
        # If current_max becomes negative, starting fresh at 'num' is better
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
        
    return max_so_far

nums_3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Contiguous subarray with max sum is [4, -1, 2, 1] -> sum = 6
print(f"Input: {nums_3}")
print(f"Max Subarray Sum (Kadane): {max_sub_array_kadane(nums_3)}")


# =========================================================================
# PROBLEM 4: MAJORITY ELEMENT - BOYER-MOORE VOTING (LeetCode #169)
# =========================================================================
print("\n" + "=" * 50)
print("4. MAJORITY ELEMENT: Boyer-Moore Voting Algorithm")
print("=" * 50)

def majority_element(nums: list[int]) -> int:
    """
    Finds the element appearing > n/2 times.
    Time: O(N) | Space: O(1) (Better than Hash Map O(N) space!)
    """
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        
    return candidate

nums_4 = [2, 2, 1, 1, 1, 2, 2]
print(f"Input: {nums_4}")
print(f"Majority Element (> N/2 times): {majority_element(nums_4)}")


# =========================================================================
# PROBLEM 5: ROTATE ARRAY BY K POSITIONS (LeetCode #189)
# =========================================================================
print("\n" + "=" * 50)
print("5. ROTATE ARRAY: 3-Reversal In-Place Technique")
print("=" * 50)

def reverse_sublist(nums: list[int], start: int, end: int) -> None:
    """Helper to reverse a subsegment of a list in-place"""
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate_array(nums: list[int], k: int) -> list[int]:
    """
    Rotate array to right by k positions in-place.
    Time: O(N) | Space: O(1)
    
    Algorithm:
    1. k = k % n
    2. Reverse entire array
    3. Reverse first k elements
    4. Reverse remaining (n - k) elements
    """
    n = len(nums)
    k = k % n
    if k == 0:
        return nums
        
    # Step 1: Reverse full list
    reverse_sublist(nums, 0, n - 1)
    # Step 2: Reverse first k elements
    reverse_sublist(nums, 0, k - 1)
    # Step 3: Reverse the rest
    reverse_sublist(nums, k, n - 1)
    return nums

nums_5 = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f"Before rotation (k={k}): {nums_5}")
rotate_array(nums_5, k)
print(f"After 3-step reversal : {nums_5}")


# =========================================================================
# PROBLEM 6: MERGE SORTED ARRAY (LeetCode #88)
# =========================================================================
print("\n" + "=" * 50)
print("6. MERGE SORTED ARRAY: 3-Pointers from the Back")
print("=" * 50)

def merge_sorted_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merges nums2 into nums1 in-place.
    nums1 has length m + n, with last n elements initialized to 0.
    Time: O(M + N) | Space: O(1)
    """
    p1 = m - 1       # pointer for last valid element in nums1
    p2 = n - 1       # pointer for last element in nums2
    p_write = m + n - 1  # pointer for insertion at the back of nums1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p_write] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_write] = nums2[p2]
            p2 -= 1
        p_write -= 1
        
    # If any elements remain in nums2, copy them
    while p2 >= 0:
        nums1[p_write] = nums2[p2]
        p2 -= 1
        p_write -= 1

nums1_demo = [1, 2, 3, 0, 0, 0]
m_demo = 3
nums2_demo = [2, 5, 6]
n_demo = 3

print(f"nums1 before merge: {nums1_demo}")
print(f"nums2 to merge    : {nums2_demo}")
merge_sorted_arrays(nums1_demo, m_demo, nums2_demo, n_demo)
print(f"nums1 after merge : {nums1_demo} (Merged in O(M+N) time, O(1) space)")

print("\n" + "=" * 70)
print("[OK] All 6 Top List Interview Problems Executed Successfully!")
print("=" * 70)

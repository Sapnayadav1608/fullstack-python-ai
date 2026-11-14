"""
Day 10: Top FAANG Dictionary / Hash Map Interview Patterns
==========================================================
30-Day Full Stack Python + AI Engineering Challenge

Interview Patterns Covered:
1. Two Sum (LeetCode #1) [Single-Pass Hash Map in O(N) Time]
2. First Unique Character in a String (LeetCode #387) [Frequency Map in O(N)]
3. Group Anagrams (LeetCode #49) [Hash Map with Tuple Keys in O(N * K)]
4. Subarray Sum Equals K (LeetCode #560) [Prefix Sum Hash Map Pattern in O(N)]
"""

import sys

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 10 - TOPIC 04: TOP FAANG DICTIONARY & HASH MAP PATTERNS]")
print("=" * 70)


# =========================================================================
# PROBLEM 1: TWO SUM (LeetCode #1)
# =========================================================================
print("\n" + "=" * 55)
print("1. Two Sum (LeetCode #1) - Single-Pass Hash Map")
print("=" * 55)

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers `nums` and an integer `target`,
    return indices of the two numbers such that they add up to target.
    
    Complexity:
    - Brute Force: O(N^2) time with nested loops.
    - Hash Map   : O(N) linear time and O(N) space.
    """
    seen = {}  # {number: index}
    
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
        
    return []

sample_nums = [2, 7, 11, 15]
target_val = 9
result_indices = two_sum(sample_nums, target_val)
print(f"Array: {sample_nums} | Target: {target_val}")
print(f"Indices: {result_indices} (Values: {sample_nums[result_indices[0]]} + {sample_nums[result_indices[1]]} = {target_val})")


# =========================================================================
# PROBLEM 2: FIRST UNIQUE CHARACTER IN A STRING (LeetCode #387)
# =========================================================================
print("\n" + "=" * 55)
print("2. First Non-Repeating Character (LeetCode #387)")
print("=" * 55)

def first_unique_char(s: str) -> int:
    """
    Finds the first non-repeating character in a string and returns its index.
    If it doesn't exist, returns -1.
    
    Algorithm:
    1. Count frequencies using a dictionary in O(N).
    2. Iterate through string again to find the first char with count == 1.
    Total Time: O(N) | Space: O(1) (At most 26 lowercase English letters).
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    for idx, char in enumerate(s):
        if freq[char] == 1:
            return idx
            
    return -1

test_s1 = "leetcode"
test_s2 = "loveleetcode"
test_s3 = "aabb"

print(f"'{test_s1}' -> Index: {first_unique_char(test_s1)} (Char: '{test_s1[first_unique_char(test_s1)]}')")
print(f"'{test_s2}' -> Index: {first_unique_char(test_s2)} (Char: '{test_s2[first_unique_char(test_s2)]}')")
print(f"'{test_s3}' -> Index: {first_unique_char(test_s3)} (No unique character)")


# =========================================================================
# PROBLEM 3: GROUP ANAGRAMS (LeetCode #49)
# =========================================================================
print("\n" + "=" * 55)
print("3. Group Anagrams (LeetCode #49)")
print("=" * 55)

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups an array of strings into anagrams.
    
    Key Insight:
    Anagrams have the EXACT SAME sorted string!
    We use the sorted tuple as the hash map key!
    Time: O(N * K log K) where N = len(strs), K = max word length.
    """
    groups = {}  # {tuple_sorted_chars: [words]}
    
    for word in strs:
        key = tuple(sorted(word))  # Tuples are immutable and hashable!
        groups.setdefault(key, []).append(word)
        
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped = group_anagrams(words)
print(f"Input Words :\n  {words}")
print(f"Grouped Anagrams:\n  {grouped}")


# =========================================================================
# PROBLEM 4: SUBARRAY SUM EQUALS K (LeetCode #560)
# =========================================================================
print("\n" + "=" * 55)
print("4. Subarray Sum Equals K (LeetCode #560)")
print("=" * 55)

def subarray_sum(nums: list[int], k: int) -> int:
    """
    Finds the total number of continuous subarrays whose sum equals k.
    
    Algorithm (Prefix Sum + Hash Map):
    If current_prefix_sum - k has been seen before 'count' times,
    it means there are 'count' subarrays ending at the current index that sum to k!
    Time: O(N) Linear Time | Space: O(N)
    """
    prefix_counts = {0: 1}  # Base case: empty subarray sum is 0
    curr_sum = 0
    total_subarrays = 0
    
    for num in nums:
        curr_sum += num
        if (curr_sum - k) in prefix_counts:
            total_subarrays += prefix_counts[curr_sum - k]
            
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        
    return total_subarrays

arr = [1, 2, 3, -2, 1, 1, 1, 4]
target_k = 3
print(f"Array: {arr} | Target Sum: {target_k}")
print(f"Total Subarrays summing to {target_k}: {subarray_sum(arr, target_k)}")

print("\n[SUMMARY] Hash maps turn O(N^2) brute force problems into O(N) linear time!")

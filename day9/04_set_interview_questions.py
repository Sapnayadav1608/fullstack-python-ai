"""
Day 09: Top Set Interview Problems & LeetCode Patterns
======================================================
30-Day Full Stack Python + AI Engineering Challenge

Interview Patterns Covered:
1. Deduplication While Preserving Insertion Order [O(N) Time]
2. Longest Consecutive Sequence (LeetCode #128) [O(N) Time using Hash Set]
3. Find All Disappeared Numbers in Array [O(N) Time via Set Difference]
4. K-Way Intersection: Common Elements Across Multiple Lists
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 09 - TOPIC 04: TOP SET INTERVIEW PROBLEMS]")
print("=" * 70)


# =========================================================================
# PROBLEM 1: DEDUPLICATION PRESERVING ORIGINAL ORDER
# =========================================================================
print("\n" + "=" * 50)
print("1. Order-Preserving Deduplication")
print("=" * 50)

def deduplicate_preserve_order(items: list) -> list:
    """
    Standard set(items) scrambles order.
    This pattern keeps first appearance in original order in O(N) time.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

test_items = ["apple", "banana", "apple", "orange", "banana", "grape"]
print(f"Original List       : {test_items}")
print(f"Standard set(items) : {list(set(test_items))} (Order scrambled!)")
print(f"Order Preserved     : {deduplicate_preserve_order(test_items)} (Clean order kept!)")


# =========================================================================
# PROBLEM 2: LONGEST CONSECUTIVE SEQUENCE (LeetCode #128)
# =========================================================================
print("\n" + "=" * 50)
print("2. Longest Consecutive Sequence (LeetCode #128)")
print("=" * 50)

def longest_consecutive_sequence(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence.
    Requirement: Must run in O(N) time! (Sorting is O(N log N) - Not allowed!)
    
    Algorithm:
    1. Put all nums into a Hash Set for O(1) lookups.
    2. Only start counting sequence if (num - 1) is NOT in the set
       (this ensures 'num' is the START of a sequence).
    3. Count upwards: num + 1, num + 2...
    Each number is checked at most twice -> strictly O(N) Time!
    """
    if not nums:
        return 0
        
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Check if 'num' is the beginning of a sequence
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            # Count consecutive numbers
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak

nums_demo = [100, 4, 200, 1, 3, 2]
# Consecutive sequence is [1, 2, 3, 4] -> length 4
print(f"Input Array        : {nums_demo}")
print(f"Longest Sequence   : {longest_consecutive_sequence(nums_demo)} (Sequence: [1, 2, 3, 4])")


# =========================================================================
# PROBLEM 3: FIND DISAPPEARED NUMBERS IN ARRAY (LeetCode #448)
# =========================================================================
print("\n" + "=" * 50)
print("3. Find Disappeared Numbers in Array [1, N]")
print("=" * 50)

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """
    Given an array nums of n integers where nums[i] is in range [1, n],
    return an array of all the integers in the range [1, n] that do not appear in nums.
    Time: O(N) using Set Difference
    """
    n = len(nums)
    expected_set = set(range(1, n + 1))
    actual_set = set(nums)
    return sorted(list(expected_set - actual_set))

sample_nums = [4, 3, 2, 7, 8, 2, 3, 1]  # length 8, range [1, 8]
print(f"Input Array        : {sample_nums}")
print(f"Missing Numbers    : {find_disappeared_numbers(sample_nums)} (Missing: 5, 6)")


# =========================================================================
# PROBLEM 4: K-WAY INTERSECTION (COMMON ELEMENTS ACROSS ALL LISTS)
# =========================================================================
print("\n" + "=" * 50)
print("4. Common Elements Across Multiple Lists")
print("=" * 50)

def common_across_all(list_of_lists: list[list]) -> set:
    """Finds items present in EVERY provided list in O(N) time"""
    if not list_of_lists:
        return set()
    return set.intersection(*map(set, list_of_lists))

data_feeds = [
    ["user1", "user2", "user3", "user4"],
    ["user2", "user4", "user5"],
    ["user2", "user3", "user4", "user6"]
]

print("Data Feeds:")
for idx, feed in enumerate(data_feeds, 1):
    print(f"  Feed {idx}: {feed}")
print(f"Users in ALL Feeds : {common_across_all(data_feeds)}")

print("\n" + "=" * 70)
print("[OK] Top Set Interview Problems Executed Successfully!")
print("=" * 70)

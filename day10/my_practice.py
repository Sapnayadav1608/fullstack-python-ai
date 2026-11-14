"""
Day 10: Hands-On Practice Workbook - Python Dictionaries & Hash Maps
=====================================================================
30-Day Full Stack Python + AI Engineering Challenge

Instructions for Sapna:
------------------------
1. Complete each function inside the '# TODO: Write your code here' sections.
2. Run the file: python day10/my_practice.py
3. The automated test suite at the bottom will verify your solutions!
"""

import sys

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[SAPNA'S DAY 10 PRACTICE WORKBOOK: PYTHON DICTIONARIES & HASH MAPS]")
print("=" * 70)


# =========================================================================
# TASK 1: Safe Value Extractor with Default Fallback
# =========================================================================
def safe_get_value(data: dict, key: str, default_value: any) -> any:
    """
    Given a dictionary `data`, retrieve the value associated with `key`.
    If the key does not exist, return `default_value` without raising KeyError.
    
    Example:
    safe_get_value({'a': 10}, 'a', 0) -> 10
    safe_get_value({'a': 10}, 'b', 0) -> 0
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 2: Word Frequency Counter (Without collections.Counter)
# =========================================================================
def count_word_frequencies(words: list[str]) -> dict[str, int]:
    """
    Given a list of words, return a dictionary mapping each word to the
    number of times it appears in the list.
    Ignore case by converting all words to lowercase.
    
    Example:
    count_word_frequencies(['apple', 'Banana', 'apple', 'BANANA', 'cherry'])
    -> {'apple': 2, 'banana': 2, 'cherry': 1}
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 3: Invert a 1-to-1 Dictionary
# =========================================================================
def invert_dictionary(original: dict) -> dict:
    """
    Given a dictionary with unique values, return an inverted dictionary
    where values become keys and keys become values.
    Requirement: Use a Dictionary Comprehension!
    
    Example:
    invert_dictionary({'a': 1, 'b': 2, 'c': 3}) -> {1: 'a', 2: 'b', 3: 'c'}
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 4: Warehouse Inventory Merger
# =========================================================================
def merge_inventories(warehouse_a: dict[str, int], warehouse_b: dict[str, int]) -> dict[str, int]:
    """
    Given two inventory dictionaries where keys are item names and values
    are item counts, return a merged dictionary.
    If an item exists in both warehouses, sum their quantities!
    
    Example:
    warehouse_a = {'laptop': 5, 'mouse': 12}
    warehouse_b = {'mouse': 8, 'keyboard': 15}
    merge_inventories(warehouse_a, warehouse_b)
    -> {'laptop': 5, 'mouse': 20, 'keyboard': 15}
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 5: Two Sum in O(N) Linear Time (LeetCode #1)
# =========================================================================
def two_sum_hashmap(nums: list[int], target: int) -> list[int]:
    """
    Given an integer array `nums` and an integer `target`,
    return indices of the two numbers such that they add up to `target`.
    Requirement: Must run in O(N) linear time using a Hash Map!
    
    Example:
    two_sum_hashmap([2, 7, 11, 15], 9) -> [0, 1]
    two_sum_hashmap([3, 2, 4], 6)       -> [1, 2]
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 6: First Non-Repeating Character Index (LeetCode #387)
# =========================================================================
def first_unique_char_index(s: str) -> int:
    """
    Given a string `s`, find the first non-repeating character in it
    and return its 0-based index. If no unique character exists, return -1.
    Requirement: Must run in O(N) time using a frequency dictionary!
    
    Example:
    first_unique_char_index("leetcode")     -> 0
    first_unique_char_index("loveleetcode") -> 2
    first_unique_char_index("aabb")         -> -1
    """
    # TODO: Write your code here
    pass


# =========================================================================
# AUTOMATED TEST SUITE (DO NOT MODIFY BELOW THIS LINE)
# =========================================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("RUNNING AUTOMATED TEST SUITE FOR DAY 10...")
    print("=" * 50)

    tests_passed = 0
    total_tests = 6

    # Test 1
    try:
        assert safe_get_value({"a": 10}, "a", 0) == 10
        assert safe_get_value({"a": 10}, "b", 99) == 99
        print("✅ Task 1 (Safe Dict Getter)       : PASSED")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Task 1 (Safe Dict Getter)       : FAILED ({e})")

    # Test 2
    try:
        res2 = count_word_frequencies(["Python", "AI", "python", "fastapi", "ai"])
        assert res2 == {"python": 2, "ai": 2, "fastapi": 1}
        print("✅ Task 2 (Word Frequency Counter) : PASSED")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Task 2 (Word Frequency Counter) : FAILED ({e})")

    # Test 3
    try:
        res3 = invert_dictionary({"admin": 100, "editor": 200, "guest": 300})
        assert res3 == {100: "admin", 200: "editor", 300: "guest"}
        print("✅ Task 3 (Invert Dictionary)      : PASSED")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Task 3 (Invert Dictionary)      : FAILED ({e})")

    # Test 4
    try:
        w_a = {"laptop": 5, "mouse": 12, "desk": 2}
        w_b = {"mouse": 8, "keyboard": 15, "desk": 3}
        res4 = merge_inventories(w_a, w_b)
        assert res4 == {"laptop": 5, "mouse": 20, "desk": 5, "keyboard": 15}
        print("✅ Task 4 (Warehouse Inventory)    : PASSED")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Task 4 (Warehouse Inventory)    : FAILED ({e})")

    # Test 5
    try:
        assert two_sum_hashmap([2, 7, 11, 15], 9) == [0, 1]
        assert two_sum_hashmap([3, 2, 4], 6) == [1, 2]
        assert two_sum_hashmap([3, 3], 6) == [0, 1]
        print("✅ Task 5 (Two Sum O(N) Hash Map)  : PASSED")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Task 5 (Two Sum O(N) Hash Map)  : FAILED ({e})")

    # Test 6
    try:
        assert first_unique_char_index("leetcode") == 0
        assert first_unique_char_index("loveleetcode") == 2
        assert first_unique_char_index("aabb") == -1
        print("✅ Task 6 (First Unique Char #387) : PASSED")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Task 6 (First Unique Char #387) : FAILED ({e})")

    print("=" * 50)
    print(f"SCORE: {tests_passed} / {total_tests} Tests Passed!")
    if tests_passed == total_tests:
        print("🎉 CONGRATULATIONS SAPNA! All Day 10 tasks passed perfectly!")
    else:
        print("💡 Complete the '# TODO' blocks above and run again!")
    print("=" * 50)

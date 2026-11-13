"""
Day 09: Hands-On Practice Workbook - Python Sets & Operations
============================================================
30-Day Full Stack Python + AI Engineering Challenge

Instructions for Sapna:
------------------------
1. Complete each function inside the '# TODO: Write your code here' sections.
2. Run the file: python day9/my_practice.py
3. The automated test suite at the bottom will verify your solutions!
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[SAPNA'S DAY 09 PRACTICE WORKBOOK: PYTHON SETS]")
print("=" * 70)


# =========================================================================
# TASK 1: Safe Empty Set Creator & Deduplicator
# =========================================================================
def create_unique_word_set(words: list[str]) -> set:
    """
    Given a list of words, return a set containing all unique words.
    Remember: Start with an empty set (avoiding the {} dict trap!).
    Example: ['python', 'ai', 'python'] -> {'python', 'ai'}
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 2: Deduplication Preserving Original Insertion Order
# =========================================================================
def remove_duplicates_keep_order(items: list) -> list:
    """
    Standard set(items) loses the original order.
    Return a list of unique items in the EXACT order they first appeared.
    Requirement: Must use a Set to achieve O(N) linear time!
    Example: [3, 1, 3, 2, 1, 4] -> returns [3, 1, 2, 4]
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 3: RBAC (Role-Based Access Control) Permission Validator
# =========================================================================
def has_required_permissions(user_perms: set[str], required_perms: set[str]) -> bool:
    """
    Return True if user_perms contains ALL permissions listed in required_perms.
    Return False if any permission is missing.
    Hint: Use set subset method or comparison operator.
    Example: user={'read', 'write', 'delete'}, required={'read', 'write'} -> True
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 4: Set Comprehension - Unique File Extension Extractor
# =========================================================================
def extract_unique_extensions(filenames: list[str]) -> set[str]:
    """
    Given a list of filenames (some with uppercase extensions or leading spaces),
    return a set of unique, lowercased file extensions without the dot.
    Requirement: Use a Set Comprehension!
    Example: ['main.py', 'INDEX.HTML', 'style.css', 'app.PY'] -> {'py', 'html', 'css'}
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 5: Shared Keywords Across Two Sentences
# =========================================================================
def find_shared_words(sentence_a: str, sentence_b: str) -> set[str]:
    """
    Given two sentences, return a set of common words present in BOTH sentences.
    Ignore case (lowercase all words).
    Example: 'Python is fast', 'AI with Python' -> returns {'python'}
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 6: Longest Consecutive Sequence Length [O(N) Time - LeetCode #128]
# =========================================================================
def longest_consecutive(nums: list[int]) -> int:
    """
    Given an unsorted array of integers `nums`, return the length of the
    longest consecutive elements sequence.
    Requirement: Must run in O(N) time using a Hash Set!
    Example: [100, 4, 200, 1, 3, 2] -> returns 4 (sequence: [1, 2, 3, 4])
    """
    # TODO: Write your code here
    pass


# =========================================================================
# AUTOMATED TEST SUITE (Run this file to test your solutions!)
# =========================================================================
if __name__ == "__main__":
    print("\n--- Running Automated Verification Checks ---")
    passed = 0
    total = 6

    # Test Task 1
    try:
        t1 = create_unique_word_set(["python", "ai", "python"])
        assert isinstance(t1, set), f"Expected set, got {type(t1)}"
        assert t1 == {"python", "ai"}, f"Expected {{'python', 'ai'}}, got {t1}"
        print("[PASS] Task 1: Safe Set Creator & Deduplicator")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 1 not completed: {e}")

    # Test Task 2
    try:
        t2 = remove_duplicates_keep_order([3, 1, 3, 2, 1, 4])
        assert t2 == [3, 1, 2, 4], f"Expected [3, 1, 2, 4], got {t2}"
        print("[PASS] Task 2: Order-Preserving Deduplication")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 2 not completed: {e}")

    # Test Task 3
    try:
        u_perms = {"read:users", "write:users", "delete:users", "audit:logs"}
        req_perms = {"read:users", "write:users"}
        assert has_required_permissions(u_perms, req_perms) is True
        assert has_required_permissions({"read:users"}, req_perms) is False
        print("[PASS] Task 3: RBAC Permission Validator")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 3 not completed: {e}")

    # Test Task 4
    try:
        t4_files = ["main.py", "INDEX.HTML", "style.css", "app.PY", "data.json", "api.Py"]
        t4_res = extract_unique_extensions(t4_files)
        assert t4_res == {"py", "html", "css", "json"}, f"Expected {{'py', 'html', 'css', 'json'}}, got {t4_res}"
        print("[PASS] Task 4: Set Comprehension Extension Extractor")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 4 not completed: {e}")

    # Test Task 5
    try:
        t5_res = find_shared_words("Python is fast and powerful", "AI models love Python and GPUs")
        assert t5_res == {"python", "and"}, f"Expected {{'python', 'and'}}, got {t5_res}"
        print("[PASS] Task 5: Shared Keywords Across Sentences")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 5 not completed: {e}")

    # Test Task 6
    try:
        t6_res = longest_consecutive([100, 4, 200, 1, 3, 2])
        assert t6_res == 4, f"Expected 4, got {t6_res}"
        t6_edge = longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        assert t6_edge == 9, f"Expected 9, got {t6_edge}"
        print("[PASS] Task 6: Longest Consecutive Sequence (LeetCode #128)")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 6 not completed: {e}")

    print("\n" + "=" * 70)
    print(f"Summary: {passed}/{total} Tasks Completed!")
    if passed == total:
        print("CONGRATULATIONS SAPNA! All Day 9 practice exercises passed!")
    else:
        print("Keep going! Open this file and write your logic inside each TODO function.")
    print("=" * 70)

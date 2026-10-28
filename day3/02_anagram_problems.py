# =============================================================================
# DAY 03 - PROBLEM 02: Valid Anagram Detection (LeetCode #242)
# =============================================================================
# Anagram ka matlab: Do words jinme EXACT wahi characters aur count ho, bas order alag ho.
# Example: "anagram" aur "nagaram" -> Anagram hain!
# =============================================================================

import sys
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 03 - PROBLEM 02] Valid Anagram Detection")
print("=" * 60)

# -----------------------------------------------------------------------------
# APPROACH 1: Sorting Method
# Time Complexity: O(n log n) | Space Complexity: O(n)
# -----------------------------------------------------------------------------
def is_anagram_sorting(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print("\n--- Approach 1: Sorting ---")
print("('listen', 'silent') ->", is_anagram_sorting("listen", "silent"))  # True
print("('rat', 'car')       ->", is_anagram_sorting("rat", "car"))        # False


# -----------------------------------------------------------------------------
# APPROACH 2: Hash Map / Frequency Counting (Optimal Interview Solution!)
# Time Complexity: O(n) | Space Complexity: O(1) [Max 26 unique lowercase chars]
# -----------------------------------------------------------------------------
def is_anagram_hashmap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_counts = {}

    # s ke characters ka count badhao
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # t ke characters ka count ghatao
    for char in t:
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        if char_counts[char] < 0:
            return False

    return True

print("\n--- Approach 2: Hash Map Frequency Counter (O(n)) ---")
word1 = "anagram"
word2 = "nagaram"
print(f"'{word1}' and '{word2}' -> Anagram? {is_anagram_hashmap(word1, word2)}")  # True


# -----------------------------------------------------------------------------
# APPROACH 3: Pythonic One-Liner using collections.Counter
# -----------------------------------------------------------------------------
def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print("\n--- Approach 3: collections.Counter ---")
print("('triangle', 'integral') ->", is_anagram_counter("triangle", "integral"))  # True

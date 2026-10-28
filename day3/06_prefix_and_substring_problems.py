# =============================================================================
# DAY 03 - PROBLEM 06: Longest Common Prefix & Substrings
# =============================================================================
# LeetCode #14: Longest Common Prefix, Manual Substring Count & Pangrams
# =============================================================================

import sys
import string

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 03 - PROBLEM 06] Prefix & Substring Problems")
print("=" * 60)

# -----------------------------------------------------------------------------
# PROBLEM 1: Longest Common Prefix (LeetCode #14)
# Sabhi strings mein jo starting part common hai wo return karein.
# Example: ["flower", "flow", "flight"] -> "fl"
# -----------------------------------------------------------------------------
def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
        
    # Pehli string ko reference manenge
    prefix = strs[0]
    
    for word in strs[1:]:
        # Jab tak word prefix se start nahi hota, prefix ko ek character chhota karte jao
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
                
    return prefix

print("--- Problem 1: Longest Common Prefix ---")
list1 = ["flower", "flow", "flight"]
list2 = ["dog", "racecar", "car"]
list3 = ["interspecies", "interstellar", "interstate"]

print(f"{list1} -> LCP: '{longest_common_prefix(list1)}'")  # 'fl'
print(f"{list2} -> LCP: '{longest_common_prefix(list2)}'")  # ''
print(f"{list3} -> LCP: '{longest_common_prefix(list3)}'")  # 'inters'


# -----------------------------------------------------------------------------
# PROBLEM 2: Manual Substring Count (Without using .count())
# Concept: Sliding Window / Slicing Window
# -----------------------------------------------------------------------------
def manual_substring_count(text: str, target: str) -> int:
    if not text or not target or len(target) > len(text):
        return 0
        
    count = 0
    sub_len = len(target)
    
    for i in range(len(text) - sub_len + 1):
        if text[i : i + sub_len] == target:
            count += 1
            
    return count

print("\n--- Problem 2: Manual Substring Count ---")
haystack = "banana and banana on the bandana"
needle = "ana"
print(f"'{needle}' in '{haystack}' -> Count: {manual_substring_count(haystack, needle)}")


# -----------------------------------------------------------------------------
# PROBLEM 3: Pangram Checker
# Sentence jismein A se Z tak saare 26 alphabets kam se kam ek baar aate hon.
# -----------------------------------------------------------------------------
def is_pangram(sentence: str) -> bool:
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = set(sentence.lower())
    return alphabet_set.issubset(sentence_set)

print("\n--- Problem 3: Pangram Check ---")
p1 = "The quick brown fox jumps over the lazy dog"
p2 = "Hello World from Python Developer"

print(f"'{p1}'\n-> Is Pangram? {is_pangram(p1)}")  # True
print(f"'{p2}'\n-> Is Pangram? {is_pangram(p2)}")  # False

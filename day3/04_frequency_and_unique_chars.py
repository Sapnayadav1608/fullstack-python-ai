# =============================================================================
# DAY 03 - PROBLEM 04: Character Frequency & Unique Characters
# =============================================================================
# LeetCode #387: First Unique Character in a String & Frequency Analysis
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 03 - PROBLEM 04] Frequency & Unique Characters")
print("=" * 60)

# -----------------------------------------------------------------------------
# PROBLEM 1: First Non-Repeating (Unique) Character (LeetCode #387)
# Pehla aisa character dhoondhein jo poore string mein sirf EK baar aaya ho.
# Agar koi nahi hai toh -1 return karein.
# -----------------------------------------------------------------------------
def first_unique_char(s: str) -> int:
    # 1. Frequency count dictionary
    count_map = {}
    for ch in s:
        count_map[ch] = count_map.get(ch, 0) + 1
        
    # 2. Pehla index dhoondho jiska count 1 hai
    for index, ch in enumerate(s):
        if count_map[ch] == 1:
            return index
            
    return -1

print("--- Problem 1: First Unique Character Index ---")
test_cases = ["leetcode", "loveleetcode", "aabb"]
for t in test_cases:
    idx = first_unique_char(t)
    char_found = t[idx] if idx != -1 else "None"
    print(f"'{t}' -> Index: {idx} (Character: '{char_found}')")


# -----------------------------------------------------------------------------
# PROBLEM 2: Most Frequent (Highest Occurring) Character
# -----------------------------------------------------------------------------
def most_frequent_char(s: str) -> tuple:
    cleaned = s.replace(" ", "").lower()
    counts = {}
    for ch in cleaned:
        counts[ch] = counts.get(ch, 0) + 1
        
    max_char = max(counts, key=counts.get)
    return max_char, counts[max_char]

sample = "Full Stack Python Developer with AI"
ch, count = most_frequent_char(sample)
print("\n--- Problem 2: Most Frequent Character ---")
print(f"In: '{sample}'")
print(f"Most frequent character is '{ch}' (Appeared {count} times)")


# -----------------------------------------------------------------------------
# PROBLEM 3: Remove All Duplicates while PRESERVING Order
# Example: "banana" -> "ban"
# (set(s) se order destroy ho jaata hai, humein order preserve karna hai!)
# -----------------------------------------------------------------------------
def remove_duplicates_preserve_order(s: str) -> str:
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)

dup_string = "programming_principles"
print("\n--- Problem 3: Remove Duplicates Preserving Order ---")
print("Original:", dup_string)
print("Unique  :", remove_duplicates_preserve_order(dup_string))

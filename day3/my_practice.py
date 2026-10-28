"""
=============================================================================
  DAY 03: STRING CODING PROBLEMS & INTERVIEWS (MY PRACTICE WORKBOOK)
=============================================================================
Name: Sapna Yadav
Topic: String Problem Solving, LeetCode Classics & Interview Questions
Instructions:
- Har question ka logic samjhein aur niche diye gaye blank space mein KHUD code type karein.
- Terminal se run karke test karein: python day3/my_practice.py
=============================================================================
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("🚀 DAY 3: STRING INTERVIEW PROBLEMS WORKBOOK")
print("=" * 60)


# -----------------------------------------------------------------------------
# CHALLENGE 1: Valid Palindrome (Alphanumeric Only)
# -----------------------------------------------------------------------------
# Input:  "A man, a plan, a canal: Panama" -> Return True
# Input:  "race a car"                     -> Return False
# Hint:   Characters ko lowercase karein aur sirf .isalnum() wale characters rakhein.

print("\n--- [Challenge 1] Valid Palindrome ---")
def check_palindrome(text: str) -> bool:
    # TODO: Apna code yahan likhein:
    pass

# Test cases:
# print(check_palindrome("A man, a plan, a canal: Panama")) # Should be True
# print(check_palindrome("race a car"))                     # Should be False




# -----------------------------------------------------------------------------
# CHALLENGE 2: Valid Anagram Check (Do words mein same letters hain ya nahi)
# -----------------------------------------------------------------------------
# Input:  s = "listen", t = "silent" -> Return True
# Input:  s = "rat", t = "car"       -> Return False
# Hint:   Dono ko sorted() karke compare kar sakte hain ya dictionary bana sakte hain.

print("\n--- [Challenge 2] Valid Anagram ---")
def check_anagram(s1: str, s2: str) -> bool:
    # TODO: Apna code yahan likhein:
    pass

# Test cases:
# print(check_anagram("listen", "silent")) # True
# print(check_anagram("rat", "car"))       # False




# -----------------------------------------------------------------------------
# CHALLENGE 3: Reverse Words in a Sentence
# -----------------------------------------------------------------------------
# Input:  "  the sky   is blue  "
# Output: "blue is sky the"
# Hint:   .split() extra spaces ko automatically handle karta hai!

print("\n--- [Challenge 3] Reverse Words in Sentence ---")
def reverse_sentence_words(sentence: str) -> str:
    # TODO: Apna code yahan likhein:
    pass

# Test cases:
# print(reverse_sentence_words("  the sky   is blue  "))




# -----------------------------------------------------------------------------
# CHALLENGE 4: First Non-Repeating Character
# -----------------------------------------------------------------------------
# Ek string mein pehla character dhoondhein jo duplicate nahi hai.
# Input:  "loveleetcode"
# Output: 'v' (Index 2)
# Hint:   Dictionary se frequency count karein ya .count() karein.

print("\n--- [Challenge 4] First Non-Repeating Character ---")
def find_first_unique_char(s: str) -> str:
    # TODO: Apna code yahan likhein:
    pass

# Test cases:
# print(find_first_unique_char("loveleetcode")) # 'v'
# print(find_first_unique_char("aabbcc"))       # "None"




# -----------------------------------------------------------------------------
# CHALLENGE 5: Run-Length String Compression
# -----------------------------------------------------------------------------
# Consecutive same letters ko unke count ke sath compress karein.
# Input:  "aabcccccaaa"
# Output: "a2b1c5a3"
# Hint:   Loop mein current letter aur previous letter compare karein.

print("\n--- [Challenge 5] String Compression ---")
def run_length_compress(s: str) -> str:
    # TODO: Apna code yahan likhein:
    pass

# Test cases:
# print(run_length_compress("aabcccccaaa")) # "a2b1c5a3"




# -----------------------------------------------------------------------------
# CHALLENGE 6: Longest Common Prefix
# -----------------------------------------------------------------------------
# Strings ki list mein jo shuruat ka common part hai wo dhoondhein.
# Input:  ["flower", "flow", "flight"]
# Output: "fl"
# Hint:   Pehle word ko prefix mankar .startswith() check karein.

print("\n--- [Challenge 6] Longest Common Prefix ---")
def find_longest_prefix(words: list) -> str:
    # TODO: Apna code yahan likhein:
    pass

# Test cases:
# print(find_longest_prefix(["flower", "flow", "flight"])) # "fl"
# print(find_longest_prefix(["dog", "racecar", "car"]))     # ""




# -----------------------------------------------------------------------------
# CHALLENGE 7: Pangram Checker
# -----------------------------------------------------------------------------
# Check karein kya sentence mein A se Z tak saare 26 letters aate hain.
# Input:  "The quick brown fox jumps over the lazy dog" -> True
# Hint:   set() use karein!

print("\n--- [Challenge 7] Pangram Checker ---")
def check_pangram(sentence: str) -> bool:
    # TODO: Apna code yahan likhein:
    pass

# Test cases:
# print(check_pangram("The quick brown fox jumps over the lazy dog")) # True
# print(check_pangram("Hello World"))                                # False




print("\n" + "=" * 60)
print("🎉 Great Job! Day 3 Problem Solving Completed!")
print("=" * 60)

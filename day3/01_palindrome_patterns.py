# =============================================================================
# DAY 03 - PROBLEM 01: Palindrome Patterns & Two-Pointer Technique
# =============================================================================
# Interview Favorite: Palindrome check karne ke 3 standard levels.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 03 - PROBLEM 01] Palindrome Patterns (Two-Pointer)")
print("=" * 60)

# -----------------------------------------------------------------------------
# LEVEL 1: Basic Palindrome (Slicing Approach)
# Time Complexity: O(n) | Space Complexity: O(n) [Naya reverse string banta hai]
# -----------------------------------------------------------------------------
def is_basic_palindrome(s: str) -> bool:
    return s == s[::-1]

print("\n--- Level 1: Basic Palindrome ---")
print("'racecar' :", is_basic_palindrome("racecar"))  # True
print("'python'  :", is_basic_palindrome("python"))   # False


# -----------------------------------------------------------------------------
# LEVEL 2: Valid Palindrome (LeetCode #125)
# Ignore non-alphanumeric characters and case-sensitivity.
# Approach: Two-Pointer Technique (Left & Right pointers moving inwards)
# Time Complexity: O(n) | Space Complexity: O(1) [Zero extra memory!]
# -----------------------------------------------------------------------------
def is_valid_palindrome_two_pointer(s: str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Left pointer ko tab tak aage badhao jab tak alphanumeric na mile
        while left < right and not s[left].isalnum():
            left += 1
            
        # Right pointer ko tab tak peeche lao jab tak alphanumeric na mile
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Dono characters ko lowercase karke compare karo
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

print("\n--- Level 2: Valid Palindrome (Two-Pointer, O(1) Space) ---")
test1 = "A man, a plan, a canal: Panama"
test2 = "race a car"
test3 = "Was it a car or a cat I saw?"

print(f"'{test1}'\n-> Is Palindrome? {is_valid_palindrome_two_pointer(test1)}")  # True
print(f"'{test2}'\n-> Is Palindrome? {is_valid_palindrome_two_pointer(test2)}")  # False
print(f"'{test3}'\n-> Is Palindrome? {is_valid_palindrome_two_pointer(test3)}")  # True


# -----------------------------------------------------------------------------
# LEVEL 3: Valid Palindrome II (LeetCode #680)
# Kya hum zyada se zyada EK character delete karke palindrome bana sakte hain?
# -----------------------------------------------------------------------------
def valid_palindrome_almost(s: str) -> bool:
    def check_sub(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Ya toh left wala skip karo ya right wala skip karo
            return check_sub(left + 1, right) or check_sub(left, right - 1)
        left += 1
        right -= 1
    return True

print("\n--- Level 3: Almost Palindrome (Delete at most 1 char) ---")
print("'abca' (delete 'b' or 'c') ->", valid_palindrome_almost("abca"))  # True ('aba' ya 'aca')
print("'abcde'                     ->", valid_palindrome_almost("abcde")) # False

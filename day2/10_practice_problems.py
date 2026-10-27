# =============================================================================
# DAY 02 - TOPIC 10: Hands-On Practice Problems & Mini Challenges
# =============================================================================
# String methods aur slicing par real-world problem solving.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 10] Real-World String Practice Problems")
print("=" * 60)

# -----------------------------------------------------------------------------
# Problem 1: Robust Palindrome Checker
# Check karna ki string ulta aur seedha same hai ya nahi (spaces aur case ignore karke)
# -----------------------------------------------------------------------------
print("\n--- Problem 1: Palindrome Checker ---")
def is_palindrome(text: str) -> bool:
    # 1. Lowercase aur spaces remove karna
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    # 2. Slicing reverse comparison
    return cleaned == cleaned[::-1]

test_phrases = ["Radar", "A man a plan a canal Panama", "Python Coding", "Madam"]
for phrase in test_phrases:
    result = is_palindrome(phrase)
    print(f"'{phrase}' -> Palindrome? {result}")

# -----------------------------------------------------------------------------
# Problem 2: Sensitive Data Masker (Email Masker)
# sapnayadav1608@gmail.com -> s**********8@gmail.com
# -----------------------------------------------------------------------------
print("\n--- Problem 2: Email Address Masker ---")
def mask_email(email: str) -> str:
    username, domain = email.split("@")
    if len(username) <= 2:
        masked_user = username[0] + "*"
    else:
        masked_user = username[0] + ("*" * (len(username) - 2)) + username[-1]
    return f"{masked_user}@{domain}"

sample_email = "sapnayadav1608@gmail.com"
print("Original Email :", sample_email)
print("Masked Email   :", mask_email(sample_email))

# -----------------------------------------------------------------------------
# Problem 3: URL Slug Generator (Web Development Essential)
# Article title ko clean URL slug banana:
# "Day 2: Python Strings & Slicing in 2026!" -> "day-2-python-strings-slicing-in-2026"
# -----------------------------------------------------------------------------
print("\n--- Problem 3: URL Slug Generator ---")
def generate_slug(title: str) -> str:
    cleaned_chars = []
    for char in title.lower():
        if char.isalnum():
            cleaned_chars.append(char)
        elif char in " -_":
            cleaned_chars.append("-")
            
    slug = "".join(cleaned_chars)
    # Consecutive dashes ko single dash banana
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")

article_title = "Day 2: Python Strings & Slicing in 2026!"
print("Original Title :", article_title)
print("Generated Slug :", generate_slug(article_title))

# -----------------------------------------------------------------------------
# Problem 4: Word & Character Frequency Counter
# -----------------------------------------------------------------------------
print("\n--- Problem 4: Word Frequency Counter ---")
paragraph = "python is simple python is fast and python is versatile"
words = paragraph.split()
unique_words = sorted(set(words))

print(f"Total Words: {len(words)}")
print("Frequency Table:")
for w in unique_words:
    print(f"  {w:<10} : {words.count(w)} times")

print("\n" + "=" * 60)
print("[SUCCESS] All Day 2 String Practice Problems Executed!")
print("=" * 60)

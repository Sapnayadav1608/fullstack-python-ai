# =============================================================================
# DAY 03 - PROBLEM 03: Reverse & Transform Words in a Sentence
# =============================================================================
# LeetCode #151: Reverse Words in a String & Word Manipulations
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 03 - PROBLEM 03] Word Reversals & Sentence Transformations")
print("=" * 60)

# -----------------------------------------------------------------------------
# TASK 1: Reverse Words in a Sentence (LeetCode #151)
# Input:  "  the sky   is blue  "
# Output: "blue is sky the"
# Multiple spaces ko single space banana hai aur leading/trailing spaces hatani hain.
# -----------------------------------------------------------------------------
def reverse_words(sentence: str) -> str:
    # .split() bina argument ke kisi bhi number of whitespaces ko handle karta hai
    words = sentence.split()
    # Reversed list ko space se join karein
    return " ".join(words[::-1])

sample1 = "  the sky   is blue  "
sample2 = "a good   example"
print("--- Task 1: Reverse Words in Sentence ---")
print(f"Original: '{sample1}'")
print(f"Reversed: '{reverse_words(sample1)}'")

print(f"\nOriginal: '{sample2}'")
print(f"Reversed: '{reverse_words(sample2)}'")


# -----------------------------------------------------------------------------
# TASK 2: Reverse Each Individual Word (Sentence order wahi rahega)
# Input:  "Python Developer"
# Output: "nohtyP repoleveD"
# -----------------------------------------------------------------------------
def reverse_individual_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    return " ".join(reversed_words)

sample3 = "Full Stack Python Developer"
print("\n--- Task 2: Reverse Each Word Individually ---")
print("Original:", sample3)
print("Result  :", reverse_individual_words(sample3))


# -----------------------------------------------------------------------------
# TASK 3: Real Title Case (Interview Trap with .title())
# Problem with built-in .title(): "they're" ko "They'Re" bana deta hai (galat!)
# Sahi solution: Har word ka sirf pehla character uppercase karein.
# -----------------------------------------------------------------------------
def clean_title_case(sentence: str) -> str:
    words = sentence.split()
    proper_words = [w[0].upper() + w[1:].lower() if len(w) > 0 else "" for w in words]
    return " ".join(proper_words)

tricky_sentence = "they're learning artificial intelligence with python"
print("\n--- Task 3: Clean Title Case ---")
print("Built-in .title() result :", tricky_sentence.title())  # They'Re (Wrong apostrophe behavior)
print("Clean Custom Title Case  :", clean_title_case(tricky_sentence))  # They're (Correct!)

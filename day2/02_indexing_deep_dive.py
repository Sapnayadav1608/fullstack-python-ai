# =============================================================================
# DAY 02 - TOPIC 02: String Indexing Deep Dive
# =============================================================================
# String ke har character ki position ko Index kehte hain.
# Positive (0 se shuru: Left to Right)
# Negative (-1 se shuru: Right to Left)
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 02] String Indexing Deep Dive")
print("=" * 60)

word = "PYTHON"

# Visual Index Chart:
# Characters:   P    Y    T    H    O    N
# Positive:     0    1    2    3    4    5
# Negative:    -6   -5   -4   -3   -2   -1

print("Word:", word)
print("Length of word:", len(word))

# 1. Positive Indexing
print("\n--- Positive Indexing (0 to len - 1) ---")
print("word[0] ->", word[0])  # 'P'
print("word[2] ->", word[2])  # 'T'
print("word[5] ->", word[5])  # 'N'

# 2. Negative Indexing (Peeche se access karna)
print("\n--- Negative Indexing (-1 to -len) ---")
print("word[-1] ->", word[-1])  # 'N' (Aakhiri letter)
print("word[-2] ->", word[-2])  # 'O' (Second last)
print("word[-6] ->", word[-6])  # 'P' (Pehla letter)

# 3. IndexError Trap (Sabse common beginner mistake)
try:
    print(word[10])  # 10 index exist nahi karta
except IndexError as err:
    print(f"\n[Handled Error] word[10] nahi mila: {err}")

# 4. Negative Index to Positive Index Formula:
# positive_equivalent = len(word) + negative_index
# Example: len("PYTHON") + (-2) = 6 - 2 = 4 (which is 'O')
neg_index = -2
pos_equivalent = len(word) + neg_index
print(f"\nword[{neg_index}] ka positive equivalent index {pos_equivalent} hai: '{word[pos_equivalent]}'")

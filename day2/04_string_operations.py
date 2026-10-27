# =============================================================================
# DAY 02 - TOPIC 04: String Operations & Comparisons
# =============================================================================
# String par hone wale math aur logical operations.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 04] String Operations & Comparisons")
print("=" * 60)

# 1. Concatenation (+) -> Do ya do se zyada strings ko jodna
first_name = "Sapna"
last_name = "Yadav"
full_name = first_name + " " + last_name
print("Concatenation (+):", full_name)

# 2. Repetition (*) -> String ko multiple times repeat karna
divider = "-" * 40
print("\nRepetition (*):")
print(divider)
print("Coding! " * 3)
print(divider)

# 3. Membership Operators (in & not in) -> Substring dhoondhna
bio = "Full Stack Python Developer with AI Engineering"

print("\nMembership Operators:")
print("'Python' in bio      ->", "Python" in bio)       # True
print("'Java' in bio        ->", "Java" in bio)         # False
print("'Golang' not in bio  ->", "Golang" not in bio)   # True

# 4. String Comparison (Lexicographical / Dictionary Order)
# Python strings ko unki ASCII / Unicode value ke hisaab se compare karta hai:
# 'A' = 65, 'B' = 66 ... 'a' = 97, 'b' = 98 (Lowercase bade hote hain!)

print("\nString Comparisons:")
print("'apple' < 'banana' ->", "apple" < "banana")   # True ('a' comes before 'b')
print("'Apple' < 'apple'   ->", "Apple" < "apple")     # True (ASCII 65 < 97)
print("'Python' == 'python'->", "Python" == "python") # False (Case-sensitive)

# =============================================================================
# DAY 06 - TOPIC 04: Practical Data Problems with List Comprehensions
# =============================================================================
# Real-world data engineering & backend scenarios using clean Pythonic code.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 06 - TOPIC 04] Practical Real-World Data Problems")
print("=" * 60)

# -----------------------------------------------------------------------------
# PROBLEM 1: Data Cleaning & Normalization (Backend / API Input Pipeline)
# -----------------------------------------------------------------------------
# Raw strings from form/API contains dirty spaces, uppercase/lowercase, and empty strings.
raw_emails = [
    "  Sapna.Yadav@GMAIL.com  ",
    "",
    "   admin@COMPANY.ORG   ",
    "   ",
    "USER_TEST@domain.in  "
]

# Task: Strip spaces, lowercase everything, and filter out empty strings in ONE LINE:
cleaned_emails = [email.strip().lower() for email in raw_emails if email.strip()]
print("--- Problem 1: Data Cleaning ---")
print("Original Raw:", raw_emails)
print("Cleaned     :", cleaned_emails)


# -----------------------------------------------------------------------------
# PROBLEM 2: Filtering Complex JSON / Dictionary Records (Database Queries)
# -----------------------------------------------------------------------------
products = [
    {"id": 101, "name": "Mechanical Keyboard", "price": 3500, "in_stock": True},
    {"id": 102, "name": "USB-C Hub", "price": 850, "in_stock": False},
    {"id": 103, "name": "Gaming Mouse", "price": 1800, "in_stock": True},
    {"id": 104, "name": "27-inch 4K Monitor", "price": 28000, "in_stock": True},
    {"id": 105, "name": "Desk Mat", "price": 600, "in_stock": False}
]

# Task: Extract names of all products that are IN STOCK and cost UNDER Rs 5000:
budget_in_stock = [p["name"] for p in products if p["in_stock"] and p["price"] < 5000]
print("\n--- Problem 2: Filter Database Records ---")
print("In-stock budget items (< Rs 5000):", budget_in_stock)


# -----------------------------------------------------------------------------
# PROBLEM 3: Matrix Addition via Nested Comprehension
# -----------------------------------------------------------------------------
# C[i][j] = A[i][j] + B[i][j]
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [10, 20, 30],
    [40, 50, 60]
]

rows = len(matrix_a)
cols = len(matrix_a[0])

matrix_sum = [[matrix_a[r][c] + matrix_b[r][c] for c in range(cols)] for r in range(rows)]

print("\n--- Problem 3: Matrix Addition ---")
print("Matrix A   :", matrix_a)
print("Matrix B   :", matrix_b)
print("Matrix A+B :", matrix_sum)


# -----------------------------------------------------------------------------
# PROBLEM 4: Words Starting with Vowels Filter
# -----------------------------------------------------------------------------
sentence = "Artificial Intelligence and Machine Learning are transforming everyday software engineering"
words = sentence.split()

vowel_words = [w for w in words if w[0].lower() in "aeiou"]
print("\n--- Problem 4: Vowel Word Extractor ---")
print("Sentence   :", sentence)
print("Vowel Words:", vowel_words)

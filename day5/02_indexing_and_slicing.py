# =============================================================================
# DAY 05 - TOPIC 02: Indexing, Slicing & Slice Assignments in Lists
# =============================================================================
# Indexing, Negative Indices, Slicing, aur Slice Mutations.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 05 - TOPIC 02] List Indexing, Slicing & Slice Assignment")
print("=" * 60)

languages = ["Python", "JavaScript", "Go", "Rust", "C++", "Java"]

# -----------------------------------------------------------------------------
# 1. Positive & Negative Indexing
# -----------------------------------------------------------------------------
print("Original List:", languages)
print("languages[0]  ->", languages[0])    # 'Python'
print("languages[-1] ->", languages[-1])   # 'Java' (Last item)
print("languages[-2] ->", languages[-2])   # 'C++'  (Second last item)

# -----------------------------------------------------------------------------
# 2. Slicing Operations [start : stop : step]
# -----------------------------------------------------------------------------
print("\n--- Slicing Examples ---")
print("languages[1:4]   ->", languages[1:4])   # ['JavaScript', 'Go', 'Rust']
print("languages[:3]    ->", languages[:3])    # Shuru ke 3 items
print("languages[::2]   ->", languages[::2])   # Alternate items
print("languages[::-1]  ->", languages[::-1])  # List reversed!

# -----------------------------------------------------------------------------
# 3. Slice Assignment (List Mutation via Slicing)
# -----------------------------------------------------------------------------
# Strings mein assignment error deta hai, lekin Lists mein aap ek sath
# multiple elements ko slice ke through replace, shrink ya expand kar sakte hain!

scores = [10, 20, 30, 40, 50]
print(f"\nOriginal Scores: {scores}")

# Replace index 1 to 3 [20, 30] with [88, 99]:
scores[1:3] = [88, 99]
print(f"After scores[1:3] = [88, 99]: {scores}")

# Insert multiple elements without deleting:
scores[1:1] = [101, 102]
print(f"Insert at index 1 via slice  : {scores}")

# Delete multiple elements via empty slice assignment:
scores[1:3] = []
print(f"Delete slice via [] assignment: {scores}")

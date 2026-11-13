"""
Day 09: Set Performance Benchmarking, Set Comprehension & Frozenset
===================================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. Live Time Complexity Benchmark: List O(N) vs Set O(1) Search
2. Set Comprehension: Clean Pythonic Filtering & Normalization
3. What is frozenset? (Immutable Sets as Dictionary Keys)
4. AI / NLP Application: Unique Token Vocabulary & Stopword Removal
"""

import sys
import time

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 09 - TOPIC 03: SET PERFORMANCE, COMPREHENSION & FROZENSET]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. LIVE PERFORMANCE BENCHMARK: LIST O(N) VS SET O(1)
# -------------------------------------------------------------------------
print("\n--- 1. Live Benchmark: Membership Check (List vs Set) ---")
N = 1_000_000
target = -999  # Worst-case scenario: target is NOT present

sample_list = list(range(N))
sample_set = set(sample_list)

# Measure List search (O(N) - Linear Scan)
t0 = time.perf_counter()
_ = target in sample_list
t_list = time.perf_counter() - t0

# Measure Set search (O(1) - Hash Lookup)
t0 = time.perf_counter()
_ = target in sample_set
t_set = time.perf_counter() - t0

print(f"Searching in {N:,} elements for a missing item:")
print(f"  List Search (O(N)) : {t_list * 1000:>8.4f} ms")
print(f"  Set Search  (O(1)) : {t_set * 1000:>8.4f} ms")
speedup = t_list / max(t_set, 1e-9)
print(f">> Sets are approximately {speedup:,.0f}x faster for lookups!")
print("   Why? Sets compute hash(target) directly into a bucket without scanning!")


# -------------------------------------------------------------------------
# 2. SET COMPREHENSION
# -------------------------------------------------------------------------
print("\n--- 2. Set Comprehensions: Data Normalization ---")
# Syntax: {expr for item in iterable if condition}

raw_tags = ["  python ", "PYTHON", "fastapi", " AI ", "FastAPI", "pytorch", "AI"]
# Goal: Strip whitespace, lowercase, and deduplicate in ONE clean line!
normalized_tags = {tag.strip().lower() for tag in raw_tags}

print(f"Raw Tags (Dirty) : {raw_tags}")
print(f"Clean Unique Set : {normalized_tags}")


# -------------------------------------------------------------------------
# 3. WHAT IS FROZENSET? (IMMUTABLE SETS)
# -------------------------------------------------------------------------
print("\n--- 3. What is a frozenset? ---")
# A regular set is mutable, so it CANNOT be a dictionary key or in another set.
# frozenset is completely immutable and HASHABLE!

regular_set = {1, 2, 3}
frozen_a = frozenset([1, 2, 3])
frozen_b = frozenset(["admin", "read", "write"])

print(f"frozenset instance: {frozen_a} | Type: {type(frozen_a)}")

# Can frozenset be a Dictionary Key?
permission_roles = {
    frozenset(["read", "write"]): "Editor Role",
    frozenset(["read", "write", "delete"]): "Admin Role",
    frozenset(["read"]): "Viewer Role"
}

query_perms = frozenset(["read", "write"])
print(f"Role for permissions {query_perms}: '{permission_roles[query_perms]}'")

# Can frozenset be inside a set? YES! (Sets of sets!)
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Nested set using frozensets: {set_of_sets}")


# -------------------------------------------------------------------------
# 4. AI & NLP APPLICATION: VOCABULARY TOKENIZER & STOPWORDS
# -------------------------------------------------------------------------
print("\n--- 4. AI & NLP Case Study: Fast Stopword Removal ---")
corpus = "Artificial Intelligence and Machine Learning are transforming modern software and technology"
stopwords = {"and", "are", "the", "in", "to", "of", "a"}

tokens = corpus.lower().split()
# O(1) filtering per word using set lookup
filtered_tokens = [word for word in tokens if word not in stopwords]
vocabulary_set = set(filtered_tokens)

print(f"Original Text     : '{corpus}'")
print(f"Filtered Tokens   : {filtered_tokens}")
print(f"Unique Vocabulary : {vocabulary_set} (Vocabulary Size: {len(vocabulary_set)})")

print("\n" + "=" * 70)
print("[OK] Set Performance, Comprehension & Frozenset Module Completed!")
print("=" * 70)

# =============================================================================
# DAY 04 - TOPIC 02: The 6 Common Time Complexities in Python
# =============================================================================
# Order of Growth (Fastest to Slowest):
# O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 04 - TOPIC 02] Common Time Complexities Explained")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. O(1) - Constant Time (The Holy Grail)
# Input kitna bhi bada ho (10 ya 10 Crore), time bilkul constant lagta hai.
# -----------------------------------------------------------------------------
def get_first_item(items: list):
    return items[0] if items else None

def dictionary_lookup(data_dict: dict, key: str):
    return data_dict.get(key)  # Hash table lookup is O(1) on average!

print("1. O(1) Examples: List Indexing (items[0]), Dict Lookup (.get())")


# -----------------------------------------------------------------------------
# 2. O(log n) - Logarithmic Time (Super Fast!)
# Har step par problem ka size AADHA (divide by 2) ho jaata hai.
# Example: Binary Search in sorted list.
# 10 Lakh items mein sirf ~20 comparisons lagte hain! (log2(1,000,000) ≈ 20)
# -----------------------------------------------------------------------------
def binary_search(sorted_list: list, target: int) -> int:
    low = 0
    high = len(sorted_list) - 1
    steps = 0
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            print(f"   [O(log n)] Found {target} in only {steps} steps out of {len(sorted_list):,} items!")
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

sample_million = list(range(1, 1_000_001))
binary_search(sample_million, 786_432)


# -----------------------------------------------------------------------------
# 3. O(n) - Linear Time (Fair & Direct)
# Input jitna badhega, time bhi bilkul usi proportion mein badhega.
# Example: Single loop through a list, linear search, sum(), max().
# -----------------------------------------------------------------------------
def linear_search(items: list, target: int) -> bool:
    for item in items:  # N items -> N checks in worst case
        if item == target:
            return True
    return False

print("\n3. O(n) Examples: Single for-loop, min(), max(), 'item in list'")


# -----------------------------------------------------------------------------
# 4. O(n log n) - Linearithmic Time (Efficient Sorting)
# Almost all modern general-purpose sorting algorithms run in O(n log n).
# Example: Python's built-in sorted(), list.sort() (Timsort algorithm), Merge Sort.
# -----------------------------------------------------------------------------
def python_sorting_demo(items: list):
    return sorted(items)  # Timsort: O(n log n)

print("4. O(n log n) Examples: sorted(), list.sort(), Merge Sort, QuickSort average")


# -----------------------------------------------------------------------------
# 5. O(n^2) - Quadratic Time (Danger Zone for Big Data)
# Nested loops! Har 1 item ke liye baaki saare N items loop hote hain.
# N = 1,000  -> 1,000,000 operations (10 Lakh)
# N = 10,000 -> 100,000,000 operations (10 Crore - Browser/App hangs!)
# -----------------------------------------------------------------------------
def print_all_pairs(items: list):
    pairs_count = 0
    for i in items:
        for j in items:
            pairs_count += 1
    return pairs_count

print("5. O(n^2) Examples: Nested loops, Bubble Sort, checking all pairs")


# -----------------------------------------------------------------------------
# 6. O(2^n) - Exponential Time (Catastrophic)
# Input 1 badhane se operations DOUBLE ho jaate hain.
# Example: Recursive Fibonacci without memoization.
# N = 40 lene par hi normal computer 30 seconds tak freeze ho jaata hai!
# -----------------------------------------------------------------------------
def slow_recursive_fib(n: int) -> int:
    if n <= 1:
        return n
    return slow_recursive_fib(n - 1) + slow_recursive_fib(n - 2)

print("6. O(2^n) Examples: Naive recursive Fibonacci, generating all subsets")

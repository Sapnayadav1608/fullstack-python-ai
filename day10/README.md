# 📘 Day 10: Python Dictionaries — Hash Tables, Memory Architecture & O(1) Patterns

Welcome to **Day 10** of the **30-Day Full Stack Python + AI Engineering Challenge**!

Today we explore Python's foundational associative data structure: **The Dictionary (`dict`)**. Dictionaries power Python namespaces, class attributes, JSON payloads, and high-performance in-memory caching systems.

---

## 🎯 Day 10 Topics & Learning Roadmap

### [01_dict_fundamentals_and_memory.py](./01_dict_fundamentals_and_memory.py)
- **Key-Value Store:** Unordered by concept, but insertion-ordered by CPython specification (Python 3.7+).
- **5 Ways to Create Dictionaries:** Literal `{}` (fastest), `dict()`, `dict([tuples])`, `dict(zip())`, and `dict.fromkeys()`.
- **The Mutable Default Trap:** Why `dict.fromkeys(keys, [])` points all keys to the exact same list in memory.
- **The Hashability Rule:** Why Keys MUST be immutable (`str`, `int`, `tuple`, `frozenset`), and mutable types (`list`, `dict`) throw `TypeError: unhashable type`.
- **CPython Compact Hash Table (Python 3.6+):** Dense entries table + sparse indices table saving 20–25% memory.
- **Dynamic Resizing:** Measuring dictionary allocation growth using `sys.getsizeof()`.

### [02_dict_methods_and_crud.py](./02_dict_methods_and_crud.py)
- **Safe Key Retrieval:** Direct bracket `d[key]` (raises `KeyError`!) vs `d.get(key, default)` (safe fallback).
- **The `.setdefault()` Power Pattern:** Atomic lookup-and-initialize for grouping data without nested if-checks.
- **Python 3.9+ Dictionary Union:** Non-destructive merge `d1 | d2` and in-place update `d1 |= d2`.
- **Deletion Strategies:** `.pop(key, default)`, `.popitem()` (LIFO), `del`, and `.clear()`.
- **Dynamic View Objects:** `.keys()`, `.values()`, `.items()` and set-like operations (`keys_a & keys_b`).

### [03_dict_internals_and_performance.py](./03_dict_internals_and_performance.py)
- **Hash Table Bucket Math:** `bucket_index = hash(key) & (table_size - 1)`.
- **Collision Resolution:** Open Addressing with pseudo-random perturb probing formula:
  $$i = (5 \cdot i + 1 + (\text{perturb} \gg 5)) \ \& \ \text{mask}$$
- **Live 1,000,000 Elements Benchmark:**
  - Dict Hash Lookup: **~0.0090 ms** ($O(1)$)
  - List Linear Scan: **~44.87 ms** ($O(N)$)
  - **Result: Dictionaries are ~5,000x faster!**
- **Dictionary Comprehensions:** Fast filtering, data transformation, and dictionary inversion.
- **Real-World Backend System:** In-Memory TTL (Time-To-Live) Cache with automatic expiration.

### [04_dict_interview_questions.py](./04_dict_interview_questions.py)
- **LeetCode #1 (Two Sum):** Single-pass Hash Map reducing $O(N^2)$ brute force to $O(N)$ linear time.
- **LeetCode #387 (First Unique Character in String):** Two-pass frequency hash map in $O(N)$ time and $O(1)$ space.
- **LeetCode #49 (Group Anagrams):** Hash Map with sorted tuple keys in $O(N \cdot K \log K)$ time.
- **LeetCode #560 (Subarray Sum Equals K):** Prefix sum frequency hash map in $O(N)$ linear time.

---

## ⚡ Dictionary Operations Time Complexity

| Operation | Average Case | Worst Case (Extreme Collisions) | Description |
| :--- | :---: | :---: | :--- |
| **Get Item (`d[k]`)** | $O(1)$ | $O(N)$ | Direct hash bucket lookup |
| **Set Item (`d[k] = v`)** | $O(1)$ | $O(N)$ | Hash insert or overwrite |
| **Delete (`del d[k]` / `.pop()`)** | $O(1)$ | $O(N)$ | Hash remove with dummy marker |
| **Membership (`k in d`)** | $O(1)$ | $O(N)$ | Key hash presence check |
| **Merge (`d1 \| d2`)** | $O(N + M)$ | $O(N + M)$ | Combines both dictionaries |
| **Iterate (`for k in d:`)** | $O(N)$ | $O(N)$ | Scans compact dense entries array |

---

## 🧪 Hands-On Practice Workbook

Run the interactive test workbook:
```powershell
python day10/my_practice.py
```
Contains 6 hands-on challenges:
1. `safe_get_value()`: Safe dictionary accessor without KeyError.
2. `count_word_frequencies()`: Case-insensitive word frequency counter.
3. `invert_dictionary()`: Comprehension-based key-value swapper.
4. `merge_inventories()`: Multi-warehouse quantity aggregator.
5. `two_sum_hashmap()`: LeetCode #1 Two Sum in $O(N)$ linear time.
6. `first_unique_char_index()`: LeetCode #387 first non-repeating character.

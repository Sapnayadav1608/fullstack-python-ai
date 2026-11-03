# 📦 Day 08: Python Tuples — Immutability, Memory Architecture & Speed Benchmarks

30-Day Full Stack Python + AI Engineering Challenge | **Day 8: Week 2 Kick-Off — Tuples Deep Dive**

---

## 📚 Topics & Modules Covered Today

| # | File Name | Key Concepts & Patterns |
| :-: | :--- | :--- |
| **01** | [`01_tuple_fundamentals_and_creation.py`](./01_tuple_fundamentals_and_creation.py) | **Core Fundamentals:** Ordered immutable sequences, comma vs parentheses rule, the single-element comma trap `(42,)`, indexing & slicing, and the "mutable object inside immutable tuple" reference trap |
| **02** | [`02_tuples_vs_lists_memory_and_speed.py`](./02_tuples_vs_lists_memory_and_speed.py) | **Why Tuples when Lists exist?** Memory overhead comparison (`sys.getsizeof()`), dynamic over-allocation vs fixed size, creation speed benchmark (1.8x+ faster), CPython constant folding, and hashability for dictionary keys |
| **03** | [`03_tuple_operations_and_unpacking.py`](./03_tuple_operations_and_unpacking.py) | **Operations & Unpacking:** Why tuples have only 2 methods (`.count()` and `.index()`), variable swapping without temp variable, star `*` extended unpacking, throwaway `_`, and `collections.namedtuple` |
| **04** | [`04_tuple_interview_questions.py`](./04_tuple_interview_questions.py) | **Top Interview Gotchas:** The infamous `t[2] += [5]` trap (raises `TypeError` but still mutates inner list!), multi-key lambda sorting, recursive deep flattening, and graph weighted edges |
| **WORKBOOK** | [`my_practice.py`](./my_practice.py) | **Hands-On Student Workbook:** 6 Coding tasks with `# TODO` sections and automated test suite for self-coding |

---

## ⚡ Tuples vs Lists: Quick Reference Cheat-Sheet

| Feature | Python `list` | Python `tuple` |
| :--- | :---: | :---: |
| **Mutability** | Mutable (In-Place modification) | **Immutable** (Write-protected) |
| **Syntax** | Square brackets `[]` | Parentheses `()` or comma `,` |
| **Memory Allocation** | Dynamic over-allocation (extra capacity) | **Exact fixed size** (Less RAM) |
| **Creation Speed** | Slower (runtime `BUILD_LIST`) | **Faster** (Constant folding + free lists) |
| **Available Methods** | 11 methods (`append`, `pop`, `sort`...) | **Only 2 methods** (`count`, `index`) |
| **Dictionary Key?** | ❌ No (`TypeError: unhashable`) | ✅ **Yes** (If elements are hashable) |
| **AI / Real-World Use** | Dynamic datasets, stacks, queues | **Tensor shapes**, RGB colors, Lat/Lon |

---

## 🏃 How to Run Any File

Terminal / Command Prompt me run karein:

```powershell
# Tuple Fundamentals & Immutability
python day8\01_tuple_fundamentals_and_creation.py

# Tuples vs Lists Memory & Speed Benchmark
python day8\02_tuples_vs_lists_memory_and_speed.py

# Operations, Unpacking & Namedtuples
python day8\03_tuple_operations_and_unpacking.py

# Top Interview Questions & Gotchas
python day8\04_tuple_interview_questions.py

# Sapna's Practice Workbook
python day8\my_practice.py
```

# 📋 Day 05: Python Lists — Operations, Methods & Memory Behaviour

30-Day Full Stack + AI Engineering Challenge | **Day 5: Lists & Dynamic Referential Arrays**

---

## 📚 Topics Covered Today

| # | File Name | Key Concepts |
| :-: | :--- | :--- |
| **01** | [`01_list_creation_and_memory.py`](./01_list_creation_and_memory.py) | **Memory Architecture:** Referential arrays, individual item address (`id()`), in-place mutability, CPython dynamic resizing and over-allocation bytes benchmark |
| **02** | [`02_indexing_and_slicing.py`](./02_indexing_and_slicing.py) | Positive/negative indexing, reverse slicing `[::-1]`, and **Slice Assignments** (`scores[1:3] = [88, 99]`) |
| **03** | [`03_adding_and_removing_elements.py`](./03_adding_and_removing_elements.py) | **Adding:** `.append()` vs `.extend()` vs `.insert()` \| **Removing:** `.pop()` (returns item) vs `.remove()` (by value) vs `del` vs `.clear()` |
| **04** | [`04_list_operations_and_methods.py`](./04_list_operations_and_methods.py) | Concatenation (`+`), repetition (`*`), membership (`in`), `.count()`, `.index()`, and `.sort()` in-place vs `sorted()` with custom key lambda |
| **05** | [`05_shallow_vs_deep_copy.py`](./05_shallow_vs_deep_copy.py) | **The Classic Bug:** Assignment (`b = a`) vs Shallow Copy (`a.copy()`) vs Deep Copy (`copy.deepcopy()`) with nested lists |
| **06** | [`06_time_complexity_of_list_operations.py`](./06_time_complexity_of_list_operations.py) | **Big O of Lists:** Why `append()` is $O(1)$ and `insert(0)` is $O(N)$ with a live speed benchmark ($1,000\times$ difference!) |
| **WORKBOOK** | [`my_practice.py`](./my_practice.py) | **Hands-On Practice Workbook:** 7 coding tasks with `# TODO` sections for student self-coding |

---

## 🏃 How to Run Any File

Terminal mein run karein:

```powershell
python day5\01_list_creation_and_memory.py
python day5\06_time_complexity_of_list_operations.py
python day5\my_practice.py
```

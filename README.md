# 🚀 Full Stack Python Developer with AI

Welcome to my journey of mastering **Full Stack Python Development and AI Engineering**! 💻🤖

This repository documents my daily code, structured notes, logic exercises, and production-ready mini projects.

---

## 📌 Repository Roadmap

| Phase | Focus Area | Status |
| :--- | :--- | :---: |
| **Phase 1** | Python Fundamentals, Logic Building & Data Structures | 🟡 In Progress |
| **Phase 2** | Modern Full Stack Web (Frontend + FastAPI + Databases) | ⚪ Upcoming |
| **Phase 3** | AI Engineering (LLMs, LangChain, Vector DBs, Agents, RAG) | ⚪ Upcoming |
| **Phase 4** | End-to-End Capstone AI Projects & Cloud Deployment | ⚪ Upcoming |

---

## 📂 Daily Progress & Modules

### 📍 [Day 01: Complete Python Core Basics](./day1)
- **01:** Print statements, comments & variable naming rules
- **02:** Python data types (`int`, `float`, `str`, `bool`, `None`) & `type()`
- **03:** Type casting (implicit vs explicit) & truthy/falsy evaluation
- **04:** User input handling with `input()`
- **05:** Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- **06:** Comparison & logical operators (`and`, `or`, `not`)
- **07:** String indexing, positive/negative indices, and slicing `[::-1]`
- **08:** String methods (`.strip()`, `.replace()`, `.split()`) & formatted f-strings
- **09:** Conditionals (`if`, `elif`, `else`) and ternary operators
- **10:** `while` loops, infinite loop safety, `break` and `continue`
- **11:** `for` loops, `range()` function & string iteration
- **12:** **Mini Project:** Smart Restaurant Bill & Tip Splitter 🧾

### 📍 [Day 02: Python Strings in Depth](./day2)
- **01:** String creation, raw strings `r""`, memory address & immutability proof
- **02:** Indexing deep dive, negative index conversion formula, IndexError safety
- **03:** Slicing mastery `[start:stop:step]`, step direction & reverse slicing `[::-1]`
- **04:** Operations: Concatenation (`+`), repetition (`*`), membership & lexicographical comparison
- **05:** Case conversions (`.title()`, `.swapcase()`) & strip cleaning methods (`.removeprefix()`, `.removesuffix()`)
- **06:** Search & replace: `.find()` vs `.index()`, `.count()`, `.startswith()`, `.replace()`
- **07:** Splitting, partitioning (`.partition()`) & joining lists into strings (`.join()`)
- **08:** Validation methods (`.isalpha()`, `.isdigit()`, `.isalnum()`, `.isidentifier()`)
- **09:** Modern f-strings: padding, alignment (`<`, `>`, `^`), decimal precision `:.2f`, thousands separator `:,`
- **10:** **Practice Challenges:** Palindrome Checker, Email Masker, URL Slug Generator & Word Counter 🔤

### 📍 [Day 03: String Problems & Interview Questions](./day3)
- **01:** Valid Palindrome (LeetCode #125) with Two-Pointer technique & Almost Palindrome (#680)
- **02:** Valid Anagram (LeetCode #242) — Sorting vs Hash Map Frequency Counter $O(n)$
- **03:** Reverse words in string (LeetCode #151) & clean Title Case without `.title()`
- **04:** First unique character (LeetCode #387), most frequent char & deduplication
- **05:** String compression / Run-length encoding (LeetCode #443) & decompression
- **06:** Longest common prefix (LeetCode #14), sliding window substring count & Pangram check
- **07:** Top 7 Tricky Interview Output Traps: Slicing boundaries, negative step, short-circuiting
- **Workbook:** [`my_practice.py`](./day3/my_practice.py) — 7 Hands-on LeetCode style challenges for self-coding

### 📍 [Day 04: Time Complexity & Big O Fundamentals](./day4)
- **01:** Why seconds/stopwatch measurement is flawed, operations count as function of $N$, Big O, Big $\Omega$, Big $\Theta$
- **02:** The 6 Common Time Complexities: $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$, $O(2^n)$
- **03:** The 4 Golden Rules: Drop constants ($O(2N) \rightarrow O(N)$), drop non-dominant terms, Add ($O(A+B)$) vs Multiply ($O(A \times B)$)
- **04:** Space Complexity: Auxiliary Space vs Input Space, recursion call stack memory $O(N)$ vs iteration $O(1)$
- **05:** Case Study: Two Sum Problem ($O(N^2)$ brute-force vs $O(N)$ Hash Map optimization with live speed comparison)
- **06:** Live Benchmarking Tool: Visual ASCII performance table comparing $O(1)$, $O(\log N)$, $O(N)$, $O(N \log N)$, $O(N^2)$
- **07:** Top Tricky Interview Questions: $i *= 2$ loops, triangle loops, string concatenation $+=$ trap, `in list` vs `in set`
- **Workbook:** [`my_practice.py`](./day4/my_practice.py) — 5 Hands-on analysis and optimization tasks with TODO sections

### 📍 [Day 05: Python Lists — Operations, Methods & Memory Behaviour](./day5)
- **01:** Memory Architecture: Referential arrays, pointers, in-place mutability, dynamic resizing bytes demo
- **02:** Indexing, slicing, stepping, and in-place slice assignments (`scores[1:3] = [88, 99]`)
- **03:** Adding & removing: `.append()` vs `.extend()` vs `.insert()` \| `.pop()` vs `.remove()` vs `del` vs `.clear()`
- **04:** List operations: Concatenation (`+`), repetition (`*`), membership (`in`), `.sort()` in-place vs `sorted()` with custom key lambda
- **05:** Shallow vs Deep Copy: The classic bug trap with nested lists and `copy.deepcopy()`
- **06:** Time Complexity of Lists: Why `append()` is $O(1)$ and `insert(0)` is $O(N)$ with live speed comparison
- **Workbook:** [`my_practice.py`](./day5/my_practice.py) — 7 Hands-on practice tasks with TODO sections

### 📍 [Day 06: List Comprehensions, Nested Lists & Practical Problems](./day6)
- **01:** List Comprehension Basics: `if` filtering, `if-else` ternary transformation, and CPython bytecode speed benchmark
- **02:** Nested List Comprehensions: Double loops order rule, Cartesian products, matrix flattening & transposition
- **03:** 2D Lists & The Multiplication Bug: `[[0]*3]*3` reference trap vs comprehension fix, diagonal traversals
- **04:** Practical Data Problems: API input string cleaning, filtering dictionary database records, and matrix addition
- **Workbook:** [`my_practice.py`](./day6/my_practice.py) — 6 Hands-on tasks with `# TODO` sections for self-coding

### 📍 [Day 07: Week 01 Comprehensive Revision & List Interview Questions](./day7)
- **01:** Week 1 Core Foundations: Memory model, object identity (`is` vs `==`), string slicing mechanics, Big O rules, referential arrays & deep copy
- **02:** Top FAANG List Interview Problems: Two Sum (Hash Map $O(N)$), Move Zeroes (In-Place Two Pointers), Maximum Subarray (Kadane's Algorithm), Majority Element (Boyer-Moore Voting), Rotate Array (3-step reversal) & Merge Sorted Array
- **03:** Top 7 Python List Gotchas & Interview Traps: Mutable default arguments (`def f(l=[])`), Modifying list during iteration bug, `[[0]*3]*3` reference trap, `+=` vs `+` aliasing, slice assignment `a[:]`, `.sort()` vs `sorted()`, and boolean identity in lists
- **Workbook:** [`my_practice.py`](./day7/my_practice.py) — 7 Hands-on LeetCode & interview coding challenges with automated test suite for self-practice

### 📍 [Day 08: Python Tuples — Immutability, Memory Architecture & Speed Benchmarks](./day8)
- **01:** Tuple Fundamentals: Ordered immutable sequences, comma rule, the single-element comma trap `(42,)`, slicing & mutable object inside tuple trap
- **02:** Tuples vs Lists: Memory overhead comparison (`sys.getsizeof()`), dynamic over-allocation vs fixed size, creation speed benchmark (1.8x+ faster), constant folding & hashability for dictionary keys
- **03:** Operations & Unpacking: Why tuples have only 2 methods (`.count()`, `.index()`), variable swapping without temp variable, star `*` extended unpacking & `collections.namedtuple`
- **04:** Top Tuple Interview Questions: The infamous `t[2] += [5]` trap (raises `TypeError` but still mutates!), multi-key lambda sorting, recursive deep flattening & graph weighted edges
- **Workbook:** [`my_practice.py`](./day8/my_practice.py) — 6 Hands-on coding tasks with automated test suite for student self-practice

### 📍 [Day 09: Python Sets & Frozenset — Hashing Architecture, Set Theory & O(1) Lookups](./day9)
- **01:** Set Fundamentals & Hashing: Unique collections, Hash Table backend, the empty set trap (`{}` vs `set()`), hashability rule, boolean collision trap (`1 == True`), and `.add()`, `.update()`, `.remove()` vs `.discard()`
- **02:** Mathematical Set Operations: Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`), Subsets, Supersets, Disjoint sets, and real-world RBAC permission validator
- **03:** Set Performance & Frozenset: Live benchmark ($O(1)$ Hash lookup vs $O(N)$ linear scan — 4,000x+ faster), Set Comprehensions, and `frozenset` (immutable sets as dictionary keys) + NLP Tokenizer
- **04:** Top FAANG Set Interview Problems: Order-preserving deduplication, Longest Consecutive Sequence (LeetCode #128 in $O(N)$ time), Missing numbers $[1, N]$, and K-way list intersection
- **Workbook:** [`my_practice.py`](./day9/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

### 📍 [Day 10: Python Dictionaries — Hash Tables, Memory Architecture & O(1) Patterns](./day10)
- **01:** Dictionary Fundamentals: Key-Value mappings, 5 creation patterns, the mutable default reference trap in `fromkeys()`, key hashability rule, CPython 3.6+ compact table (indices + entries) & dynamic resizing
- **02:** Methods & CRUD: Safe access (`d.get()` vs `KeyError`), atomic `.setdefault()`, Python 3.9+ dictionary union (`|` and `|=`), deletion strategies (`.pop()`, `.popitem()`), and dynamic views with set operations
- **03:** Internals & Benchmarks: Hash bucket bitwise math `hash(k) & mask`, open addressing with perturb probing, live 1,000,000 items benchmark (Dict $O(1)$ ~5,000x faster than lists), comprehensions & In-Memory TTL Cache
- **04:** Top FAANG Hash Map Patterns: Two Sum (LeetCode #1 in $O(N)$), First Unique Character (LeetCode #387), Group Anagrams (LeetCode #49), and Subarray Sum Equals K (LeetCode #560)
- **Workbook:** [`my_practice.py`](./day10/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

### 📍 [Day 11: Python Functions Mastery — Arguments, Scopes (LEGB), Closures & Lambdas](./day11)
- **01:** Parameters & Signatures: Positional vs keyword arguments, the mutable default argument trap (`l=[]` vs `l=None`), `*args` tuple unpacking, `**kwargs` dict unpacking, Python 3.8+ positional-only (`/`) and keyword-only (`*`) markers
- **02:** Scopes & LEGB Rule: Local $\rightarrow$ Enclosing $\rightarrow$ Global $\rightarrow$ Built-in hierarchy, variable shadowing, architectural dangers of `global`, `nonlocal` for nested scopes, and UnboundLocalError compiler trap
- **03:** First-Class Functions & Closures: Functions as objects, dictionary dispatch routing table, custom Higher-Order Functions, lexical scope retention, `__closure__` cell introspection, function factories, and $O(1)$ memory moving average tracker
- **04:** Lambdas & Recursion: Anonymous lambda expressions, multi-key tuple sorting (`key=lambda x: (-x['salary'], x['age'])`), `map()`, `filter()`, `functools.reduce()`, Call Stack frame dynamics, and Recursive Nested Dict Flattener
- **Workbook:** [`my_practice.py`](./day11/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

---

## 🛠️ Tech Stack & Tools

- **Language:** Python 3.x
- **Editor:** Visual Studio Code / Antigravity IDE
- **Version Control:** Git & GitHub

---

## 🌟 Connect with Me

- **GitHub:** [@Sapnayadav1608](https://github.com/Sapnayadav1608)
- Following along? Feel free to ⭐ star this repository!

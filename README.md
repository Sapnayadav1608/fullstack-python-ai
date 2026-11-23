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

### 📍 [Day 12: Python Decorators Mastery — Wrappers, Chaining, Production Patterns & LRU Cache](./day12)
- **01:** Fundamentals & Wraps: First-principles of decorators, manual wrapping vs `@` syntax, universal template, metadata loss bug, and `@functools.wraps`
- **02:** Arguments & Chaining: 3-tier nested closures for decorators with arguments, stacking multiple decorators, and the Onion execution model (bottom-up wrapping, top-down execution)
- **03:** Production Patterns: Latency profiler (`@timer`), resilient network retry with exponential backoff (`@retry` for LLM APIs), and Role-Based Access Control (`@require_role`)
- **04:** Class Decorators & Caching: Classes as decorators (`__call__`), Class Decorators (model registry), custom memoization from scratch ($O(2^N) \rightarrow O(N)$), and `@functools.lru_cache`
- **Workbook:** [`my_practice.py`](./day12/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

### 📍 [Day 13: Python Iterators, Generators & Context Managers — Streaming & Memory Optimization](./day13)
- **01:** Iteration Protocol: Iterable vs Iterator, `__iter__()` and `__next__()`, CPython `for` loop emulation, exhaustion trap, and AI `BatchDatasetIterator`
- **02:** Generators & `yield`: Frame suspension, CPython lifecycle states, Generator expressions vs List comprehensions, live 10M item benchmark ($O(1)$ vs $O(N)$ RAM), and 50GB log streaming
- **03:** Pipelines & AI Streaming: Unix pipe generator chaining, `yield from` sub-generator delegation, recursive data flattener, bidirectional coroutine `.send()`, and LLM token streamer
- **04:** Context Managers & `with`: Resource leak prevention, class-based `__enter__`/`__exit__`, `@contextlib.contextmanager` generator bridge, and Atomic DB Transaction auto-rollback
- **Workbook:** [`my_practice.py`](./day13/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

### 📍 [Day 14: Object-Oriented Programming (OOP) Part 1 — Architecture & Encapsulation](./day14)
- **01:** Classes & `self`: Instantiation lifecycle (`__new__` vs `__init__`), desugaring `self` (`Class.fn(obj)`), `__str__` vs `__repr__`, and `LLMPromptTemplate`
- **02:** Namespaces & Variables: `__dict__` introspection, class vs instance state, the catastrophic mutable class variable bug, and `__slots__` 6x memory reduction
- **03:** Method Types: Instance (`self`), Class (`@classmethod` / `cls` factory constructors), Static (`@staticmethod` utilities), and `LLMClient` AI service
- **04:** Encapsulation: Public, protected (`_`), and private name mangling (`__`), `@property` getters, setters with validation, and `APIKeyManager`
- **Workbook:** [`my_practice.py`](./day14/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

### 📍 [Day 15: Object-Oriented Programming (OOP) Part 2 — Inheritance, MRO, Polymorphism & ABCs](./day15)
- **01:** Inheritance & `super()`: Single/multi-level inheritance, dynamic `super()` MRO proxy, state initialization, and `FineTunedGeminiClient` extending `AIModelClient`
- **02:** Multiple Inheritance & MRO: The Diamond Problem, C3 Linearization algorithm ($L[C]$ invariants), Mixin composition pattern, and `AIAgent` with serialization/rate-limiting mixins
- **03:** Polymorphism & Duck Typing: Method overriding, runtime polymorphic dispatch, Pythonic duck typing ("quacks like a duck"), structural subtyping with `typing.Protocol`, and multimodal ingestion pipeline
- **04:** Abstract Base Classes & Interfaces: `abc.ABC`, `@abstractmethod`, interface enforcement, instantiation prevention, and pluggable Vector Database architecture (`PineconeAdapter`, `ChromaDBAdapter`)
- **Workbook:** [`my_practice.py`](./day15/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

### 📍 [Day 16: Python Data Model & Magic Methods — Operator Overloading, Containers & Callables](./day16)
- **01:** Object Representation & String Protocols: `__repr__` vs `__str__` duality (`eval(repr(x)) == x`), custom f-string formatting (`__format__`), binary serialization (`__bytes__`), and truth value testing (`__bool__` vs `__len__`)
- **02:** Operator Overloading & Arithmetic Protocols: Mapping arithmetic symbols (`+`, `-`, `*`, `/`), the `NotImplemented` singleton dispatch rule, reflected operators (`__radd__`, `__rmul__`), in-place mutation (`__iadd__`), matrix multiplication (`@` / `__matmul__`), and `Tensor1D` vector algebra
- **03:** Rich Comparisons & Hashing Protocols: Full comparisons (`__eq__`, `__lt__`), eliminating boilerplate with `@functools.total_ordering`, the sacred hashability invariant ($a == b \implies \text{hash}(a) == \text{hash}(b)$), and RAG `DocumentChunk` deduplication & ranking
- **04:** Custom Containers, Sequence Protocols & Callables: Sequence methods (`__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__iter__`), slice object handling (`isinstance(key, slice)`), turning instances into stateful callable functions via `__call__` (PyTorch `nn.Module` foundation), and `PyTorchStyleDataset`
- **Workbook:** [`my_practice.py`](./day16/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

### 📍 [Day 17: Advanced Exception Handling, Custom Exception Hierarchies & Defensive AI Engineering](./day17)
- **01:** Exception Architecture & Lifecycle: CPython hierarchy (`BaseException` vs `Exception`), danger of bare `except: pass`, the complete 4-clause lifecycle (`try/except/else/finally`), why `else` prevents false positives, and `SafeModelCallWrapper` enterprise pattern
- **02:** Chaining, Context & Traceback Engineering: PEP 3134 mechanics, implicit context (`__context__`), explicit chaining (`raise ... from err`), context suppression (`raise ... from None`) for API security, programmatic root-cause resolver, and Resilient AI Gateway telemetry
- **03:** Custom Exception Hierarchies for AI: Enterprise taxonomy (`AIPlatformError` -> `AIClientError` [4xx] vs `AIServerError` [5xx]), `TokenLimitExceededError` with token counts, `RateLimitExceededError` with backoff hints, RFC 7807 problem details serialization, and dynamic HTTP factory
- **04:** Exception Groups & Resilient Architectures: Python 3.11+ `ExceptionGroup` and selective `except*` pattern matching for concurrent agent tools, Resilient Circuit Breaker state machine (Closed -> Open -> Half-Open), and Multi-Provider Fallback Router (Pro -> Flash -> Cache)
- **Workbook:** [`my_practice.py`](./day17/my_practice.py) — 6 Hands-on coding tasks with automated test suite for self-practice

---

## 🛠️ Tech Stack & Tools

- **Language:** Python 3.x
- **Editor:** Visual Studio Code / Antigravity IDE
- **Version Control:** Git & GitHub

---

## 🌟 Connect with Me

- **GitHub:** [@Sapnayadav1608](https://github.com/Sapnayadav1608)
- Following along? Feel free to ⭐ star this repository!

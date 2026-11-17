# 🚀 Day 13: Python Iterators, Generators & Context Managers

Welcome to **Day 13** of the 30-Day Full Stack Python + AI Engineering Track! 

Today we master the inner machinery that powers Python's data streaming and resource management: **The Iteration Protocol**, **Lazy Evaluation with Generators & `yield`**, **Sub-generators with `yield from`**, and **Deterministic Resource Management with Context Managers**.

---

## 📌 Day 13 Learning Objectives

```
           ┌────────────────────────────────────────────────────────┐
           │          THE PYTHON STREAMING & RESOURCE ENGINE        │
           └──────────────────────────┬─────────────────────────────┘
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         │                            │                            │
         ▼                            ▼                            ▼
┌─────────────────┐          ┌─────────────────┐          ┌─────────────────┐
│   ITERATORS     │          │   GENERATORS    │          │ CONTEXT MANAGERS│
│  Protocol &     │          │  Lazy Stream &  │          │ Resource Safety │
│  __next__()     │          │  O(1) RAM Engine│          │ & @contextmanager│
└────────┬────────┘          └────────┬────────┘          └────────┬────────┘
         │                            │                            │
         ▼                            ▼                            ▼
  Iterable vs Iterator       yield vs return            __enter__ & __exit__
  for loop under the hood    Frames & States (CPython)  try...finally automation
  BatchDataset for AI        LLM Token Streaming        Atomic DB Auto-Rollback
```

1. **The Core Iteration Protocol:** Master `__iter__()`, `__next__()`, and the exact CPython bytecode emulation of a `for` loop.
2. **Generators & `yield`:** Understand frame suspension, CPython generator states (`GEN_CREATED`, `GEN_SUSPENDED`, `GEN_CLOSED`), and how generators achieve $O(1)$ memory consumption.
3. **Advanced Pipelines & Coroutines:** Build Unix-style composable generator pipelines, sub-generator delegation with `yield from`, bidirectional `.send()` coroutines, and live LLM token streaming.
4. **Context Managers & `with` Statement:** Eliminate resource leaks (file descriptors, sockets, database locks), implement class-based `__enter__`/`__exit__`, and build function-based managers using `@contextlib.contextmanager`.

---

## 📂 Modules & Architecture

### 📍 [Module 01: Iteration Protocol, Iterable vs Iterator, and Custom Iterators](./01_iteration_protocol_and_custom_iterators.py)
- **Iterable vs Iterator:** An *Iterable* produces an iterator via `__iter__()`. An *Iterator* is a stateful stream producing values via `__next__()` and terminates with `StopIteration`.
- **Under-the-Hood `for` Loop:** How CPython translates `for item in collection:` into a `while True:` loop with `try/except StopIteration`.
- **The Exhaustion Trap:** Why iterators can only be consumed once and cannot be reset without re-instantiation.
- **Two-Argument `iter(callable, sentinel)`:** Reading streams, sockets, or sensors until a sentinel value is reached.
- **Production AI Pattern:** `BatchDatasetIterator` for streaming mini-batches of embeddings to GPU memory with zero dataset duplication.

---

### 📍 [Module 02: Generators, `yield`, and Memory Optimization (O(1) vs O(N) RAM)](./02_generators_yield_and_memory_optimization.py)
- **The Magic of `yield`:** Unlike `return` which destroys the local execution frame, `yield` pauses execution, freezes all local variables and instruction pointers, and returns control to the caller.
- **CPython Generator States:** Inspecting lifecycle transitions using `inspect.getgeneratorstate()`:
  - `GEN_CREATED` $\rightarrow$ `GEN_RUNNING` $\rightarrow$ `GEN_SUSPENDED` $\rightarrow$ `GEN_CLOSED`.
- **Generator Expressions `(...)` vs List Comprehensions `[...]`:** Lazy on-demand evaluation vs eager full-memory evaluation.
- **Live Memory Benchmark (10,000,000 Items):**

| Data Structure | Evaluation Strategy | 1M Elements Heap RAM | Time to First Item |
| :--- | :--- | :---: | :---: |
| **List Comprehension `[...]`** | Eager (stores all in RAM) | **~38.5 MB** | High (must compute all) |
| **Generator Expression `(...)`** | Lazy (computes on-demand) | **~0.87 KB** | **Instant (O(1) latency)** |
| **Efficiency Gain** | — | **~45,000x Less RAM** | **Zero Startup Lag** |

- **Production Pattern:** Streaming massive 50GB log files and AI training corpora without Out-Of-Memory (OOM) fatal crashes.

---

### 📍 [Module 03: Advanced Generator Pipelines, `yield from`, and AI Token Streaming](./03_advanced_generator_pipelines_and_streaming.py)
- **Composable Pipelines:** Chaining independent generators like Unix pipes:
  ```
  generate_raw_data() ──► parse_records() ──► filter_anomalies() ──► aggregate_metrics()
  ```
- **Sub-Generator Delegation (`yield from`):** Replaces clumsy nested loops and transparently handles bidirectional communication and exceptions.
- **Recursive Flattening:** Deeply flattening arbitrarily nested data structures with recursive `yield from`.
- **Bidirectional Coroutines:** Sending values into running generators using `g.send(val)`, injecting exceptions with `g.throw()`, and graceful shutdown with `g.close()`.
- **Production AI Architecture:** Live LLM Token Streaming engine simulating OpenAI/Gemini Server-Sent Events (SSE) with typing latency and metadata return via `StopIteration.value`.

---

### 📍 [Module 04: Context Managers, Resource Management & @contextlib.contextmanager](./04_context_managers_and_with_statement.py)
- **The Resource Leak Danger:** Unclosed files, unreleased DB pool connections, and hanging mutex locks.
- **The `with` Protocol:** `__enter__()` binds the resource; `__exit__(exc_type, exc_val, exc_tb)` guarantees deterministic teardown.
- **Exception Suppression:** Returning `True` from `__exit__` swallows specific anticipated exceptions safely.
- **Function-Based Context Managers:** The ultimate bridge between Decorators and Generators using `@contextlib.contextmanager`.
- **Production Backend Pattern:** Atomic Database Transaction Manager with automatic rollback upon network drops or logic exceptions.

---

## 🎯 Hands-On Student Workbook: `my_practice.py`

Test your mastery with 6 real-world challenges in [`my_practice.py`](./my_practice.py):

1. **Task 1: Custom Cyclic Iterator (`CyclicIterator`)** — Repeat sequence elements a fixed number of cycles.
2. **Task 2: Custom Range Generator (`my_range`)** — Emulate Python's built-in `range()` with positive and negative step sizes.
3. **Task 3: Infinite Prime Stream (`prime_stream`)** — Generate endless prime numbers lazily on-demand.
4. **Task 4: Multi-Stage Generator Pipeline (`clean_user_pipeline`)** — Clean, parse, and filter messy data streams.
5. **Task 5: Recursive Flattener (`deep_flatten`)** — Flatten arbitrary nested lists/tuples with `yield from`.
6. **Task 6: High-Precision Execution Timer (`ExecutionTimer`)** — Custom context manager recording execution latency in milliseconds.

### Running the Test Suite:
```bash
python day13/my_practice.py
```

---

## 💡 Top FAANG Interview Traps on Day 13 Concepts

1. **The Generator Exhaustion Trap:**
   ```python
   g = (x ** 2 for x in range(3))
   print(list(g))  # [0, 1, 4]
   print(list(g))  # []  <-- Empty! Iterators cannot be rewound!
   ```

2. **`isinstance(x, Iterator)` vs `isinstance(x, Iterable)`:**
   - Every Iterator is an Iterable, but **NOT** every Iterable is an Iterator! (A list is an Iterable, but NOT an Iterator).

3. **`yield` in `try...finally` within `@contextmanager`:**
   - Always wrap code after `yield` inside a `finally:` block in `@contextmanager`. If an exception occurs in the caller's `with` block, unhandled cleanup code after `yield` will never run unless protected by `finally:`.

---

⭐ **Keep building every single day! Tomorrow is Day 14!**

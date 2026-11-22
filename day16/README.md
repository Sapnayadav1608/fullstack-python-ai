# 🚀 Day 16: Python Data Model & Magic (Dunder) Methods Mastery

Welcome to **Day 16** of the 30-Day Full Stack Python + AI Engineering Track! 

After mastering OOP Part 1 (Classes, Encapsulation, Methods) on Day 14 and OOP Part 2 (Inheritance, MRO, Polymorphism, ABCs) on Day 15, **Day 16 completes the OOP Mastery Trilogy**. 

Today we master the inner engine of Python: **The Python Data Model & Special (Dunder) Methods**. In modern AI engineering, foundational libraries like **PyTorch** (`nn.Module.__call__`, `Dataset.__getitem__`, `Tensor.__matmul__` `@`), **NumPy**, **Pandas**, and **Pydantic** achieve their intuitive syntax through Python's dunder protocols!

---

## 📌 Day 16 Learning Objectives

```
           ┌────────────────────────────────────────────────────────┐
           │          THE PYTHON DATA MODEL & DUNDER METHODS        │
           └──────────────────────────┬─────────────────────────────┘
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         │                            │                            │
         ▼                            ▼                            ▼
┌─────────────────┐          ┌─────────────────┐          ┌─────────────────┐
│ OBJECT STRINGS  │          │    OPERATOR     │          │  CONTAINER &    │
│  & REPR / BOOL  │          │   OVERLOADING   │          │ CALLABLE (AI)   │
│ __repr__, __str_│          │ __add__, __eq__ │          │ __getitem__,    │
│ __format__, bool│          │ __matmul__ (@)  │          │ __len__, __call_│
└────────┬────────┘          └────────┬────────┘          └────────┬────────┘
         │                            │                            │
         ▼                            ▼                            ▼
  repr() for Devs             Vector Math & Dot Product    PyTorch Dataset Emulation
  str() for Users             __hash__ & __eq__ Contract   Callable AI Pipeline
  Truth Value Testing         @total_ordering              Slice Support [start:stop]
```

1. **The Representation Duality (`__repr__` vs `__str__`):** Understand why `repr()` is for developers (formal, reproducible via `eval(repr(x)) == x`) while `str()` is for end users, and how Python falls back gracefully.
2. **The `NotImplemented` Golden Rule:** Master why operator overloading methods (`__add__`, `__mul__`, `__matmul__`) MUST return `NotImplemented` instead of raising `TypeError` so Python can dispatch to reflected methods (`__radd__`, `__rmul__`).
3. **The Matrix Multiplication Protocol (`@` / `__matmul__`):** Leverage PEP 465 matrix multiplication for linear algebra, vector projections, and neural network layers.
4. **The Sacred Hashability Contract:** Learn why implementing `__eq__` automatically sets `__hash__ = None`, why mutable objects must never be hashed, and how to satisfy $a == b \implies \text{hash}(a) == \text{hash}(b)$.
5. **Sequence & Container Protocols:** Implement full indexing, negative indices, and slicing (`isinstance(key, slice)`) alongside $O(1)$ membership checking (`__contains__`).
6. **The Callable Protocol (`__call__`):** Transform class instances into stateful callable functions—the architectural foundation of PyTorch's `nn.Module`.

---

## 📂 Modules & Architecture

### 📍 [Module 01: Object Representation & String Protocols](./01_object_representation_and_string_dunders.py)
- **`__repr__` vs `__str__`:** Unambiguous developer logging vs user-facing display.
- **`__format__` Custom Specifiers:** Domain-specific f-string tokens (e.g. `f"{tokens:k}"` or `f"{metric:usd}"`).
- **Binary Protocol (`__bytes__`):** Raw byte serialization for network sockets and cryptographic hashing.
- **Truth Value Testing (`__bool__` vs `__len__`):** Python's evaluation hierarchy for boolean conditions.
- **Enterprise AI Pattern:** `LLMResponseEnvelope` with multi-format telemetry routing.

---

### 📍 [Module 02: Operator Overloading & Arithmetic Protocols](./02_operator_overloading_and_arithmetic_dunders.py)
- **Binary Arithmetic:** Mapping `+`, `-`, `*`, `/` to `__add__`, `__sub__`, `__mul__`, `__truediv__`.
- **The Reflected Protocol (`__radd__`, `__rmul__`):** Handling heterogeneous operands (e.g. `10.0 + vector`).
- **In-Place Mutation (`__iadd__`, `__imul__`):** Eliminating memory re-allocations in tight numerical loops.
- **Matrix Multiplication (`@` / `__matmul__`):** Dot product and linear projections (PEP 465).
- **Enterprise AI Pattern:** `Tensor1D` supporting broadcasting, Hadamard product, L2 Norm, and Cosine Similarity.

---

### 📍 [Module 03: Rich Comparisons & The Hashing Protocol](./03_rich_comparisons_and_hashing_contracts.py)
- **Rich Comparisons:** `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`.
- **Total Ordering:** Synthesizing all 6 comparisons from `__eq__` and `__lt__` using `@functools.total_ordering`.
- **The Hashability Invariant:** Why `__eq__` nullifies `__hash__` and how to safely implement immutable hashing.
- **Enterprise AI Pattern:** `DocumentChunk` with $O(1)$ set deduplication and top-$k$ similarity ranking for RAG pipelines.

---

### 📍 [Module 04: Custom Containers, Sequences & Callable Objects](./04_custom_containers_sequences_and_callables.py)
- **Sequence Protocol:** `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`.
- **Slicing Mechanics:** Distinguishing `int` from `slice` objects inside `__getitem__`.
- **The Callable Protocol (`__call__`):** Emulating PyTorch's `nn.Module.forward` with stateful inference objects.
- **Attribute Interception (`__getattr__`):** Dynamic dot-notation proxying for nested configuration stores.
- **Enterprise AI Pattern:** `PyTorchStyleDataset` supporting batch slicing and streaming data loaders.

---

## 🧪 Hands-On Practice Workbook

The companion workbook [`my_practice.py`](./my_practice.py) contains 6 hands-on engineering challenges with a built-in automated test suite:

1. **Task 1: Vector2D Representation & Truthiness** (`__repr__`, `__str__`, `__bool__`)
2. **Task 2: Money Arithmetic & Reflected Operators** (`__add__`, `__radd__`, `__mul__`, `__rmul__`, `NotImplemented`)
3. **Task 3: NeuralLinearLayer Matrix Multiplication** (`@` / `__matmul__`)
4. **Task 4: ModelArtifact Total Ordering** (`@functools.total_ordering`, `__lt__`, `__eq__`)
5. **Task 5: FeatureKey Hashing Contract** (`__eq__`, `__hash__`, `set()` deduplication)
6. **Task 6: TokenStream Sequence & Slicing** (`__len__`, `__getitem__` with `slice`, `__iter__`)

To run the automated test suite:
```bash
python day16/my_practice.py
```

---

## ⚡ Quick Reference: Python Dunder Methods Cheat Sheet

| Protocol | Dunder Methods | Invocation Syntax | Real-World AI Example |
| :--- | :--- | :--- | :--- |
| **String / Repr** | `__repr__`, `__str__` | `repr(x)`, `str(x)`, `f"{x}"` | Debugging model weights and prompt logs |
| **Formatting** | `__format__` | `f"{x:spec}"` | Displaying token counts (`:k`, `:m`, `:usd`) |
| **Truthiness** | `__bool__`, `__len__` | `bool(x)`, `if x:` | Validating if LLM response succeeded |
| **Arithmetic** | `__add__`, `__sub__`, `__mul__` | `a + b`, `a - b`, `a * b` | Tensor broadcasting and scalar scaling |
| **Reflected** | `__radd__`, `__rmul__` | `scalar + a`, `scalar * a` | Scaling embedding vectors by float factor |
| **MatMul** | `__matmul__`, `__rmatmul__` | `W @ x` | Neural linear layer forward projection |
| **Comparisons** | `__eq__`, `__lt__`, `__le__` | `a == b`, `a < b`, `a <= b` | Sorting retrieved RAG documents by score |
| **Hashing** | `__hash__` | `hash(x)`, `set()`, `dict[x]` | Deduplicating text chunks in vector stores |
| **Sequence** | `__len__`, `__getitem__` | `len(x)`, `x[i]`, `x[1:4]` | Slicing training datasets in mini-batches |
| **Callable** | `__call__` | `obj(*args, **kwargs)` | Executing PyTorch model or LLM pipeline |

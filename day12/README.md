# 🎯 Day 12: Python Decorators Mastery — Wrappers, Chaining, Production Patterns & LRU Cache

30-Day Full Stack Python + AI Engineering Challenge | **Day 12: Decorators & Metaprogramming**

---

## 📚 Topics & Modules Covered Today

| # | File Name | Key Concepts & Patterns |
| :-: | :--- | :--- |
| **01** | [`01_decorator_fundamentals_and_wraps.py`](./01_decorator_fundamentals_and_wraps.py) | **Core Mechanics:** First-principles of decorators, manual decoration vs `@` syntactic sugar, the universal `*args, **kwargs` template, the **Metadata Loss Bug**, and preserving introspection with `@functools.wraps` |
| **02** | [`02_decorators_with_arguments_and_chaining.py`](./02_decorators_with_arguments_and_chaining.py) | **Advanced Architectures:** 3-tier nested closures for decorators with arguments (`@repeat(num_times=3)`), Decorator Chaining/Stacking, and **The Onion Model** (Bottom-up wrapping vs Top-down execution) |
| **03** | [`03_production_backend_and_ai_decorators.py`](./03_production_backend_and_ai_decorators.py) | **Production Engineering:** High-precision latency profiler (`@timer`), resilient network retry with exponential backoff (`@retry` for LLMs), and Role-Based Access Control (`@require_role` 403 Forbidden) |
| **04** | [`04_class_decorators_and_lru_cache.py`](./04_class_decorators_and_lru_cache.py) | **Classes & Caching:** Classes as decorators via the `__call__` dunder method, Class Decorators (auto-registering AI models), custom memoization from scratch ($O(2^N) \rightarrow O(N)$), and Python's C-optimized `@functools.lru_cache` |
| **WORKBOOK** | [`my_practice.py`](./my_practice.py) | **Hands-On Student Workbook:** 6 Coding tasks with `# TODO` sections and automated test suite for self-practice |

---

## 🧅 The Onion Model: Decorator Chaining Order

When multiple decorators are stacked above a function, Python evaluates them as nested function calls:

```python
@decorator_A
@decorator_B
def target_function():
    pass

# Is equivalent to:
target_function = decorator_A(decorator_B(target_function))
```

```
┌──────────────────────────────────────────────────┐
│  @decorator_A (Runs First on Entry ➔ [1])        │
│  ┌────────────────────────────────────────────┐  │
│  │  @decorator_B (Runs Second ➔ [2])          │  │
│  │  ┌──────────────────────────────────────┐  │  │
│  │  │  target_function() [3 Core Executed] │  │  │
│  │  └──────────────────────────────────────┘  │  │
│  │  @decorator_B (Exits Third ➔ [4])          │  │
│  └────────────────────────────────────────────┘  │
│  @decorator_A (Exits Last ➔ [5])                 │
└──────────────────────────────────────────────────┘
```

- **Wrapping Order:** Bottom-to-Top (`decorator_B` wraps first, then `decorator_A` wraps `B`).
- **Execution Order:** Top-to-Bottom (`decorator_A` entry $\rightarrow$ `decorator_B` entry $\rightarrow$ target $\rightarrow$ `B` exit $\rightarrow$ `A` exit).

---

## ⚡ The 3-Tier Decorator with Arguments Blueprint

```python
import functools

def repeat(num_times: int = 3):
    """Tier 1: Receives decorator arguments."""
    def decorator(func):
        """Tier 2: Receives the target function."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Tier 3: Receives function runtime arguments."""
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

---

## 🏃 How to Run Any File

Terminal / Command Prompt me run karein:

```powershell
# Module 01: Decorator Fundamentals & @functools.wraps
python day12\01_decorator_fundamentals_and_wraps.py

# Module 02: Decorators with Arguments & Chaining
python day12\02_decorators_with_arguments_and_chaining.py

# Module 03: Production Backend & AI Decorators (@timer, @retry, @require_role)
python day12\03_production_backend_and_ai_decorators.py

# Module 04: Class Decorators, Memoization & @functools.lru_cache
python day12\04_class_decorators_and_lru_cache.py

# Sapna's Practice Workbook (6 Hands-on Tasks)
python day12\my_practice.py
```

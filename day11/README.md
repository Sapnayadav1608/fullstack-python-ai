# 🎯 Day 11: Python Functions Mastery — Arguments, Scopes (LEGB), Closures & Lambdas

30-Day Full Stack Python + AI Engineering Challenge | **Day 11: Functions & Advanced Execution Mechanics**

---

## 📚 Topics & Modules Covered Today

| # | File Name | Key Concepts & Patterns |
| :-: | :--- | :--- |
| **01** | [`01_function_parameters_and_signatures.py`](./01_function_parameters_and_signatures.py) | **Parameters & Signatures:** Positional vs keyword arguments, the **Mutable Default Argument Trap** (`l=[]` vs `l=None`), `*args` tuple unpacking, `**kwargs` dictionary unpacking, Python 3.8+ positional-only (`/`) and keyword-only (`*`) markers, and inspect reflection |
| **02** | [`02_scopes_and_legb_rule.py`](./02_scopes_and_legb_rule.py) | **Scope Resolution:** The **LEGB Rule** (Local $\rightarrow$ Enclosing $\rightarrow$ Global $\rightarrow$ Built-in), variable shadowing, why `global` is an architectural anti-pattern, `nonlocal` for nested scopes, and the **UnboundLocalError trap** |
| **03** | [`03_first_class_functions_and_closures.py`](./03_first_class_functions_and_closures.py) | **First-Class Citizens & Closures:** Functions as objects, dictionary dispatch routing table, custom Higher-Order Functions (`map`/`filter`), Lexical Scope Retention, `__closure__` cell introspection, Function Factories, and streaming moving average tracker ($O(1)$ space) |
| **04** | [`04_lambdas_functional_patterns_and_recursion.py`](./04_lambdas_functional_patterns_and_recursion.py) | **Lambdas, Functional Built-ins & Recursion:** Anonymous lambda expressions, multi-key tuple sorting (`key=lambda x: (-x['salary'], x['age'])`), `map()`, `filter()`, `functools.reduce()`, Call Stack frames visualization, and **Recursive Nested JSON Flattener** |
| **WORKBOOK** | [`my_practice.py`](./my_practice.py) | **Hands-On Student Workbook:** 6 Coding tasks with `# TODO` sections and automated test suite for self-practice |

---

## 🔍 The LEGB Scope Hierarchy

When Python resolves any variable name, it traverses through four distinct namespaces in this strict priority order:

```
┌─────────────────────────────────────────────────────────────┐
│  [B] BUILT-IN SCOPE                                         │
│  (len, range, print, sum, Exception, dir, ...)             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  [G] GLOBAL SCOPE                                     │  │
│  │  (Module-level variables, imports, top-level classes) │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  [E] ENCLOSING SCOPE (Non-local)                │  │  │
│  │  │  (Outer enclosing functions in nested closures) │  │  │
│  │  │  ┌───────────────────────────────────────────┐  │  │  │
│  │  │  │  [L] LOCAL SCOPE                          │  │  │  │
│  │  │  │  (Inside the currently executing function)│  │  │  │
│  │  │  └───────────────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚠️ The #1 Python Interview Trap: Mutable Default Arguments

```python
# ❌ DANGEROUS: Default list is created ONCE at compile-time and shared!
def append_to(item, target_list=[]):
    target_list.append(item)
    return target_list

print(append_to("A"))  # ['A']
print(append_to("B"))  # ['A', 'B']  <-- Shared state across calls!

# ✅ PYTHONIC FIX: Use None sentinel value
def append_to_safe(item, target_list=None):
    if target_list is None:
        target_list = []  # Brand new list created per invocation
    target_list.append(item)
    return target_list
```

---

## ⚡ Modern Python 3.8+ Parameter Syntax Cheat-Sheet

```python
def configure_endpoint(
    endpoint, method, /,          # Positional-Only (MUST NOT pass as keyword)
    timeout=30,                   # Standard (Positional OR Keyword)
    *,                            # Keyword-Only Marker
    auth_required=True,           # MUST pass as keyword
    cors_enabled=False            # MUST pass as keyword
):
    pass
```

---

## 🏃 How to Run Any File

Terminal / Command Prompt me run karein:

```powershell
# Module 01: Function Parameters & Mutable Default Trap
python day11\01_function_parameters_and_signatures.py

# Module 02: Scopes, LEGB Rule & UnboundLocalError
python day11\02_scopes_and_legb_rule.py

# Module 03: First-Class Functions & Closures
python day11\03_first_class_functions_and_closures.py

# Module 04: Lambdas, Functional Built-ins & Recursion
python day11\04_lambdas_functional_patterns_and_recursion.py

# Sapna's Practice Workbook (6 Hands-on Tasks)
python day11\my_practice.py
```

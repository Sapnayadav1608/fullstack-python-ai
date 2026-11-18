# 🚀 Day 14: Object-Oriented Programming (OOP) Part 1

Welcome to **Day 14** of the 30-Day Full Stack Python + AI Engineering Track! 

Today we cross a monumental milestone in Python: moving from procedural & functional scripts to **Enterprise Object-Oriented Programming (OOP)**. We unpack the inner machinery of Python classes, the `self` parameter, namespaces (`__dict__`), the three method types (`@classmethod`, `@staticmethod`), and data protection via **Encapsulation & `@property`**.

---

## 📌 Day 14 Learning Objectives

```
           ┌────────────────────────────────────────────────────────┐
           │        OBJECT-ORIENTED ARCHITECTURE & ENCAPSULATION    │
           └──────────────────────────┬─────────────────────────────┘
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         │                            │                            │
         ▼                            ▼                            ▼
┌─────────────────┐          ┌─────────────────┐          ┌─────────────────┐
│ CLASSES & SELF  │          │ METHOD FLAVORS  │          │  ENCAPSULATION  │
│  Instantiation  │          │ Instance, Class │          │ Name Mangling & │
│  & Lifecycle    │          │ & Static Math   │          │  @property      │
└────────┬────────┘          └────────┬────────┘          └────────┬────────┘
         │                            │                            │
         ▼                            ▼                            ▼
  __new__ vs __init__        self (Instance state)        _protected (Convention)
  self desugaring            @classmethod (cls factory)   __private (Mangled name)
  __str__ vs __repr__        @staticmethod (utility)      @property getter/setter
  __slots__ memory           LLMClient Architecture       Security Validation
```

1. **Classes, Objects & The `self` Mechanism:** Understand how CPython allocates memory (`__new__`), initializes state (`__init__`), and passes instances to unbound methods (`Class.method(obj)`).
2. **Namespace Introspection (`__dict__`):** Master the attribute lookup chain (`instance.__dict__` $\rightarrow$ `Class.__dict__`), avoid the catastrophic mutable class variable bug, and optimize memory with `__slots__`.
3. **The 3 Method Flavors:** Know exactly when to use regular instance methods, `@classmethod` alternative factory constructors (`from_json`, `from_polar`), and isolated `@staticmethod` utilities.
4. **Encapsulation & `@property`:** Replace clumsy Java-style getters/setters with idiomatic Python `@property` decorators, validate bounds, enforce read-only computed properties, and leverage name mangling (`__var`).

---

## 📂 Modules & Architecture

### 📍 [Module 01: Classes, Objects, The `self` Mechanism & Introspection](./01_classes_objects_and_self.py)
- **Class Blueprint vs Instance:** Objects as self-contained bundles of state and behavior.
- **The `self` Mechanism:** Proving that `dev.introduce()` is pure syntactic sugar for `Developer.introduce(dev)`.
- **The Instantiation Lifecycle:** `__new__(cls)` (raw memory allocation) vs `__init__(self)` (attribute initialization).
- **`__str__` vs `__repr__`:** Human-friendly display strings vs unambiguous developer debug representations.
- **Production AI Pattern:** `LLMPromptTemplate` class managing variable substitution, prompt schemas, and token estimation.

---

### 📍 [Module 02: Instance vs Class Variables, Namespaces & The Mutation Trap](./02_instance_vs_class_variables_and_namespace.py)
- **The `__dict__` Namespace:** How Python stores object state inside internal hash tables.
- **Attribute Lookup Order:** `instance.__dict__` $\rightarrow$ `Class.__dict__` $\rightarrow$ Base Classes $\rightarrow$ `AttributeError`.
- **The Mutable Class Variable Trap:** Why `class User: permissions = []` creates a massive security hole where mutating permissions on one user leaks to all users.
- **The Shadowing Trap:** Why `instance.class_var = val` creates an instance attribute instead of updating the class variable.
- **Memory Optimization with `__slots__`:** Slashing memory overhead from 344 bytes down to 56 bytes per instance (~6x reduction!) by eliminating `__dict__`.

---

### 📍 [Module 03: Instance Methods, @classmethod, and @staticmethod](./03_instance_class_and_static_methods.py)
- **The 3 Method Flavors:**

| Method Type | Decorator | First Arg | Access Level | Primary Use Case |
| :--- | :---: | :---: | :--- | :--- |
| **Instance Method** | None | `self` | Accesses & mutates instance & class | Normal object operations |
| **Class Method** | `@classmethod` | `cls` | Accesses & mutates class state only | Alternative Factory Constructors |
| **Static Method** | `@staticmethod` | None | Cannot access instance or class state | Independent utility math & logic |

- **Alternative Factory Constructors:** Using `Temperature.from_fahrenheit()` and `AIEmbeddingRecord.from_json()` instead of convoluted boolean flags inside `__init__`.
- **Production AI Pattern:** `LLMClient` with class-level model registries, instance-level inference queries, and static vector cosine similarity computation.

---

### 📍 [Module 04: Encapsulation, Name Mangling, and the @property Decorator](./04_encapsulation_and_property_decorators.py)
- **The 3 Privacy Conventions:**
  - `public`: Free for all callers.
  - `_protected`: Single underscore convention ("internal implementation detail").
  - `__private`: Double underscore triggering CPython **Name Mangling** (`_ClassName__var`).
- **The Pythonic `@property` Ecosystem:**
  - Getter: `@property def balance(self): ...`
  - Setter with Validation: `@balance.setter def balance(self, val): ...` (bounds checks, type guards).
  - Read-Only Computed Properties (e.g. `account_summary`).
- **Production Security Pattern:** `APIKeyManager` with masked secrets (`AIza****fXYZ`), format validation, and automated rotation timestamps.

---

## 🎯 Hands-On Student Workbook: `my_practice.py`

Test your mastery with 6 real-world challenges in [`my_practice.py`](./my_practice.py):

1. **Task 1: Book Class** — Implement formatted `__str__` and developer-grade `__repr__`.
2. **Task 2: StudentTracker** — Build class-level counter while isolating per-instance mutable lists.
3. **Task 3: Vector2D from_polar** — `@classmethod` converting polar coordinates to Cartesian coordinates.
4. **Task 4: PasswordPolicy** — `@staticmethod` evaluating password complexity.
5. **Task 5: SmartThermostat** — `@property` getter/setter validating temperature bounds $[10.0^\circ\text{C}, 35.0^\circ\text{C}]$.
6. **Task 6: SecureWallet** — Private attributes with name mangling, transaction ledger, and insufficient funds validation.

### Running the Test Suite:
```bash
python day14/my_practice.py
```

---

## 💡 Top FAANG Interview Traps on Python OOP

1. **The Mutable Class Variable Gotcha:**
   ```python
   class Dog:
       tricks = []  # Class variable shared by ALL dogs!
   d1 = Dog(); d2 = Dog()
   d1.tricks.append("fetch")
   print(d2.tricks)  # ['fetch']  <-- Both dogs now have it!
   ```

2. **The `self` Illusion:**
   - In Python, `self` is NOT a reserved keyword! You could technically name it `this` or `me` (though PEP 8 strictly forbids it). CPython binds it positionally as the first argument.

3. **Bypassing Name Mangling:**
   - Name mangling is **NOT** encryption or security protection! It simply prefixes the attribute with `_ClassName`. Anyone can still access `obj._ClassName__private_var`. It exists purely to prevent namespace clashes during subclass inheritance.

---

⭐ **Keep building every single day! Tomorrow is Day 15!**

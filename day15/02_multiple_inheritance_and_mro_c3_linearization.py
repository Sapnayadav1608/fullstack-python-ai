"""
Day 15: Advanced Object-Oriented Programming (OOP) Part 2
Module 02: Multiple Inheritance, The Diamond Problem & C3 Linearization (MRO)
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Multiple Inheritance: Syntax, power, and perils.
2. The Infamous Diamond Problem: Ambiguity in class hierarchies.
3. How Python Resolves It: C3 Linearization & Method Resolution Order (MRO).
4. Cooperative Multi-Inheritance: How `super()` visits siblings across the MRO.
5. The Mixin Design Pattern: Composable plug-in behaviors without fragile base classes.
6. Production Pattern: Composing an `AIAgent` with `JSONMixin`, `LoggerMixin` & `RateLimitMixin`.
"""

import json
import time
from typing import Dict, Any, List


# ============================================================================
# 1. THE DIAMOND PROBLEM IN MULTIPLE INHERITANCE
# ============================================================================
"""
WHAT IS THE DIAMOND PROBLEM?
Imagine this inheritance diamond:

           ┌──────────┐
           │ Class A  │  (Root)
           └────┬─────┘
                │
        ┌───────┴───────┐
        ▼               ▼
   ┌─────────┐     ┌─────────┐
   │ Class B │     │ Class C │  (Both override action())
   └────┬────┘     └────┬────┘
        │               │
        └───────┬───────┘
                ▼
           ┌──────────┐
           │ Class D  │  (class D(B, C): inherits from both)
           └──────────┘

When `d = D()` calls `d.action()`, which version executes? B's or C's?
- In C++, this causes ambiguity compiler errors.
- In Python, this is deterministically resolved using C3 LINEARIZATION!
"""

print("=" * 70)
print("1. THE DIAMOND PROBLEM & MRO RESOLUTION")
print("=" * 70)

class A:
    def ping(self) -> str:
        return "Ping from A"

class B(A):
    def ping(self) -> str:
        return f"B -> {super().ping()}"

class C(A):
    def ping(self) -> str:
        return f"C -> {super().ping()}"

class D(B, C):
    """Inherits from both B and C."""
    def ping(self) -> str:
        return f"D -> {super().ping()}"


d_instance = D()
print(f"Executing d.ping(): {d_instance.ping()}")
# Output: D -> B -> C -> Ping from A
# Notice: Even though B does not inherit from C, super() inside B called C!
# That is the power of cooperative MRO!

print("\nInspecting D.__mro__ (C3 Linearization Order):")
for idx, cls in enumerate(D.__mro__, start=1):
    print(f"  Step {idx}: {cls.__name__}")


# ============================================================================
# 2. C3 LINEARIZATION: THE 3 GOLDEN RULES
# ============================================================================
"""
CPython guarantees 3 invariants in any MRO:
1. Subclasses come BEFORE their parents. (D appears before B and C).
2. The order of base classes listed in the definition is preserved. (Since `class D(B, C)`, B comes before C).
3. Monotonicity: If Class X precedes Class Y in any base class's MRO, it MUST precede Y in all subclasses!
If an inheritance structure violates these rules, Python rejects it at compile time:
`TypeError: Cannot create a consistent method resolution order (MRO)`.
"""

print("\n" + "=" * 70)
print("2. MRO DETERMINISM VERIFICATION")
print("=" * 70)

mro_names = [cls.__name__ for cls in D.__mro__]
print(f"Class D resolution path: {' -> '.join(mro_names)}")
assert mro_names == ['D', 'B', 'C', 'A', 'object'], "MRO order mismatch!"
print("✅ C3 Linearization verified: D -> B -> C -> A -> object")


# ============================================================================
# 3. THE MIXIN DESIGN PATTERN (ENTERPRISE PYTHON ARCHITECTURE)
# ============================================================================
"""
WHAT IS A MIXIN?
- A lightweight class that provides a specific bundle of functionality to other classes.
- A mixin is NOT meant to be instantiated on its own!
- Does NOT participate in an "is-a" taxonomy; instead, it provides "can-do" capabilities.
- Golden Rules for Mixins:
    1. Name ends with `Mixin` (e.g., `JSONSerializableMixin`).
    2. Small, single-responsibility focus.
    3. Uses `super()` cooperatively if it overrides methods.
"""

print("\n" + "=" * 70)
print("3. PRODUCTION PATTERN: COMPOSING AN AI AGENT WITH MIXINS")
print("=" * 70)

class JSONSerializableMixin:
    """Mixin that equips any class with automatic JSON serialization."""
    def to_json(self) -> str:
        # Serializes all non-private attributes in __dict__
        clean_dict = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith("_")
        }
        return json.dumps(clean_dict, indent=2, default=str)


class AuditLoggerMixin:
    """Mixin that records timestamps and operation logs."""
    def log_event(self, action: str, details: str = "") -> None:
        timestamp = time.strftime("%H:%M:%S")
        print(f"  📝 [AUDIT {timestamp}] {self.__class__.__name__} -> Action: '{action}' | {details}")


class RateLimiterMixin:
    """Mixin that tracks call frequency to protect downstream APIs."""
    def __init__(self, *args, max_calls_per_minute: int = 60, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.max_calls_per_minute = max_calls_per_minute
        self._call_count = 0

    def check_rate_limit(self) -> bool:
        self._call_count += 1
        if self._call_count > self.max_calls_per_minute:
            raise RuntimeError(f"Rate limit exceeded! Max {self.max_calls_per_minute} calls/min.")
        return True


# Composing our Enterprise AI Agent using clean Mixins:
class AIAgent(JSONSerializableMixin, AuditLoggerMixin, RateLimiterMixin):
    """AI Agent composed with JSON export, audit logging, and rate limiting capabilities."""
    def __init__(self, agent_name: str, model_id: str, max_calls_per_minute: int = 5) -> None:
        super().__init__(max_calls_per_minute=max_calls_per_minute)
        self.agent_name = agent_name
        self.model_id = model_id
        self.status = "INITIALIZED"

    def execute_task(self, query: str) -> str:
        self.check_rate_limit()
        self.log_event("EXECUTE_QUERY", f"Query='{query}'")
        self.status = "RUNNING"
        result = f"Agent [{self.agent_name}] completed: '{query}' using {self.model_id}"
        self.status = "IDLE"
        return result


# Testing the composed agent
agent = AIAgent(agent_name="ResearchSynthesizer", model_id="gemini-1.5-pro", max_calls_per_minute=3)

# 1. Execute task (triggers RateLimiterMixin + AuditLoggerMixin)
response = agent.execute_task("Analyze Q3 earnings transcript")
print(f"Task Output: {response}\n")

# 2. Serialize agent state to JSON (triggers JSONSerializableMixin)
print("Agent JSON State (via JSONSerializableMixin):")
print(agent.to_json())

# 3. Check MRO of our composite class:
print(f"\nAIAgent MRO: {[cls.__name__ for cls in AIAgent.__mro__]}")

print("\n" + "=" * 70)
print("DAY 15 MODULE 02: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

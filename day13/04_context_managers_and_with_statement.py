"""
Day 13: Python Iterators & The Iteration Protocol
Module 04: Context Managers, Resource Management & @contextlib.contextmanager
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Why Resource Management Matters: Leaks, dangling sockets, uncommitted DB state.
2. The `with` Statement Protocol: __enter__() and __exit__().
3. Handling & Suppressing Exceptions inside __exit__().
4. Class-Based Context Manager: High-Precision Performance Profiler.
5. Function-Based Context Manager: @contextlib.contextmanager (The Generator Bridge!).
6. Production Pattern: Atomic Database Transaction Simulator with Auto-Rollback.
"""

import time
from typing import Optional, Type, Any
from types import TracebackType
from contextlib import contextmanager


# ============================================================================
# 1. WHY RESOURCE MANAGEMENT MATTERS (THE `try...finally` PROBLEM)
# ============================================================================
"""
Before Context Managers, developers wrote:
    resource = acquire_resource()
    try:
        do_work(resource)
    finally:
        resource.release()

Problems with this:
1. Repetitive boilerplate across the entire codebase.
2. Forgetting the `finally:` block causes socket, file descriptor, or DB lock leaks!
3. The `with` statement guarantees deterministic release, even on unexpected errors.
"""

print("=" * 70)
print("1. CLASS-BASED CONTEXT MANAGER: THE PROTOCOL")
print("=" * 70)

class PrecisionTimer:
    """
    A class-based context manager for measuring code execution latency.
    """
    def __init__(self, task_name: str) -> None:
        self.task_name = task_name
        self.start_time: float = 0.0
        self.elapsed_ms: float = 0.0

    def __enter__(self) -> "PrecisionTimer":
        """Called immediately upon entering the `with` block."""
        self.start_time = time.perf_counter()
        print(f"⏱️  [START] '{self.task_name}' context entered.")
        # The returned object is bound to the `as` variable: `with PrecisionTimer(...) as timer:`
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> bool:
        """
        Called when exiting the `with` block, even if an exception was raised!
        - exc_type: The exception class (or None if no error)
        - exc_val:  The exception instance (or None)
        - exc_tb:   The traceback object (or None)
        
        Returning True SUPPRESSES the exception.
        Returning False (or None) allows the exception to propagate normally.
        """
        self.elapsed_ms = (time.perf_counter() - self.start_time) * 1000
        print(f"⏱️  [DONE]  '{self.task_name}' finished in {self.elapsed_ms:.3f} ms")

        if exc_type is not None:
            print(f"⚠️  [ALERT] An exception occurred: {exc_type.__name__}: {exc_val}")
            # We return False so caller still sees the error
            return False
        return True


# Testing the Class-Based Context Manager
with PrecisionTimer("Matrix Multiplication Simulation") as timer:
    # Simulate computation
    total = sum(i * i for i in range(500_000))
    print(f"  Computation result: {total:,}")


# ============================================================================
# 2. EXCEPTION SUPPRESSION IN __exit__()
# ============================================================================
"""
Sometimes you WANT the context manager to swallow specific expected exceptions
(similar to `contextlib.suppress`).
"""

print("\n" + "=" * 70)
print("2. EXCEPTION SUPPRESSION IN ACTION")
print("=" * 70)

class SuppressErrors:
    """Context manager that safely suppresses specified exception types."""
    def __init__(self, *exceptions_to_catch: Type[BaseException]) -> None:
        self.exceptions_to_catch = exceptions_to_catch

    def __enter__(self) -> "SuppressErrors":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is not None and issubclass(exc_type, self.exceptions_to_catch):
            print(f"  🛡️  Safely suppressed expected error: {exc_type.__name__} ('{exc_val}')")
            return True  # Returning True swallows the exception!
        return False

# This ZeroDivisionError is safely handled without crashing the script
with SuppressErrors(ZeroDivisionError, KeyError):
    print("  Dividing 10 by 0...")
    result = 10 / 0
    print("  This line will not run.")

print("  Execution safely continued past suppressed error!")


# ============================================================================
# 3. FUNCTION-BASED CONTEXT MANAGERS WITH @contextlib.contextmanager
# ============================================================================
"""
THE GENERATOR BRIDGE:
Instead of writing a full class with `__enter__` and `__exit__`, Python's
`@contextlib.contextmanager` decorator turns a generator into a Context Manager!

Rule: The generator MUST yield exactly ONCE:
- Everything before `yield`: Runs during `__enter__()`.
- The yielded value: Becomes the target of the `as` clause.
- Everything after `yield` (in a `finally:` block): Runs during `__exit__()`.
"""

print("\n" + "=" * 70)
print("3. FUNCTION CONTEXT MANAGER VIA @contextlib.contextmanager")
print("=" * 70)

@contextmanager
def temporary_config_override(config: dict, key: str, temp_value: Any):
    """Temporarily overrides a configuration dictionary key and restores it upon exit."""
    old_value = config.get(key)
    config[key] = temp_value
    print(f"  [CONFIG] Overriding '{key}': {old_value} -> {temp_value}")
    try:
        yield temp_value  # Yield control to the `with` block body
    finally:
        # Guarantee restoration even if an exception is raised inside the block
        if old_value is None:
            config.pop(key, None)
        else:
            config[key] = old_value
        print(f"  [CONFIG] Restored '{key}' back to: {old_value}")


app_settings = {"ENVIRONMENT": "production", "DEBUG": False, "LOG_LEVEL": "WARNING"}
print(f"Initial Settings: {app_settings}")

with temporary_config_override(app_settings, "DEBUG", True):
    print(f"  Inside with-block: DEBUG is currently {app_settings['DEBUG']}")

print(f"After with-block:  DEBUG is restored to {app_settings['DEBUG']}")


# ============================================================================
# 4. PRODUCTION PATTERN: ATOMIC DATABASE TRANSACTION (AUTO-ROLLBACK)
# ============================================================================
"""
In web backends (FastAPI, Django, SQLAlchemy), a database transaction must be
ATOMIC (all succeed, or none succeed).
If any query fails inside the block, the entire transaction is rolled back!
"""

print("\n" + "=" * 70)
print("4. PRODUCTION PATTERN: ATOMIC TRANSACTION WITH AUTO-ROLLBACK")
print("=" * 70)

class MockDatabaseConnection:
    def __init__(self) -> None:
        self.state = {"user_balance": 1000, "merchant_balance": 500}
        self.in_transaction = False

    @contextmanager
    def transaction(self):
        """Atomic transaction context manager."""
        print("  [DB] BEGIN TRANSACTION")
        self.in_transaction = True
        # Take a snapshot for rollback
        snapshot = self.state.copy()
        try:
            yield self
            print("  [DB] COMMIT: All operations succeeded cleanly.")
        except Exception as e:
            print(f"  [DB] ROLLBACK: Exception detected ({e}). Restoring state snapshot.")
            self.state = snapshot
            raise  # Re-raise so the application logic knows it failed
        finally:
            self.in_transaction = False
            print("  [DB] TRANSACTION ENDED\n")


db = MockDatabaseConnection()

# Scenario A: Successful Transfer
print("--- SCENARIO A: Valid Transfer ---")
with db.transaction():
    db.state["user_balance"] -= 200
    db.state["merchant_balance"] += 200
    print(f"  Balances updated: User=${db.state['user_balance']}, Merchant=${db.state['merchant_balance']}")

print(f"Final DB State after Scenario A: {db.state}")

# Scenario B: Failed Transfer (Network/Validation Failure)
print("\n--- SCENARIO B: Faulty Transfer (Triggers Auto-Rollback) ---")
try:
    with db.transaction():
        db.state["user_balance"] -= 900
        # Simulate sudden crash before merchant credit
        raise ConnectionResetError("Payment Gateway Network Dropped!")
        db.state["merchant_balance"] += 900
except ConnectionResetError:
    print("  App Layer caught: Payment failed gracefully.")

print(f"Final DB State after Scenario B (Protected): {db.state}")

print("\n" + "=" * 70)
print("DAY 13 MODULE 04: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

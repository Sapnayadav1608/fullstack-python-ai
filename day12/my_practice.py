# =============================================================================
# DAY 12 - STUDENT WORKBOOK: Python Decorators Mastery
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Instructions:
# - Complete all 6 tasks below by replacing the 'pass' with your implementation.
# - Do NOT change the function signatures or test assertions.
# - Run this script in your terminal to verify your answers:
#       python day12/my_practice.py
# =============================================================================

import sys
import time
import functools
from typing import Callable, Any, Dict, Optional

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("🎯 DAY 12: STUDENT PRACTICE WORKBOOK — PYTHON DECORATORS MASTERY")
print("=" * 70)


# =============================================================================
# TASK 1: FIX METADATA LOSS WITH @functools.wraps
# =============================================================================
# Description:
# Write a decorator 'audit_logger' that:
# 1. Prints or logs that the function is being audited.
# 2. Calls the function and returns its result.
# 3. MUST use '@functools.wraps(func)' so the decorated function retains
#    its original '__name__' and '__doc__'.
# =============================================================================
def audit_logger(func: Callable) -> Callable:
    # TODO: Implement decorator with @functools.wraps
    pass


# =============================================================================
# TASK 2: DECORATOR WITH ARGUMENTS (@prefix_output)
# =============================================================================
# Description:
# Implement a 3-tier decorator 'prefix_output(prefix: str)' that accepts a string prefix.
# When applied to a function returning a string, it returns:
# f"{prefix}: {result}"
#
# Example:
# @prefix_output("[SUCCESS]")
# def get_msg(): return "Database connected"
# get_msg() -> "[SUCCESS]: Database connected"
# =============================================================================
def prefix_output(prefix: str) -> Callable:
    # TODO: Implement 3-tier closure decorator
    pass


# =============================================================================
# TASK 3: EXECUTION RATE LIMITER DECORATOR (@limit_calls)
# =============================================================================
# Description:
# Write a decorator 'limit_calls(max_calls: int)' that:
# - Tracks how many times the decorated function has been invoked.
# - If called more than 'max_calls', it raises a RuntimeError("Rate limit exceeded").
# - Otherwise, increments count and returns the function's result.
# =============================================================================
def limit_calls(max_calls: int) -> Callable:
    # TODO: Implement call limiter closure
    pass


# =============================================================================
# TASK 4: TYPE VALIDATION DECORATOR (@validate_string_args)
# =============================================================================
# Description:
# Write a decorator 'validate_string_args' that checks all positional arguments (*args).
# If ANY argument is NOT a string (isinstance(arg, str) is False),
# it must raise a TypeError("All arguments must be strings").
# Otherwise, it executes and returns the result.
# =============================================================================
def validate_string_args(func: Callable) -> Callable:
    # TODO: Implement type validator decorator
    pass


# =============================================================================
# TASK 5: IN-MEMORY CACHE DECORATOR (@simple_cache)
# =============================================================================
# Description:
# Write a custom '@simple_cache' decorator from scratch (do not use functools.lru_cache).
# - It must maintain an internal dictionary 'cache'.
# - The function arguments tuple '*args' acts as the cache key.
# - If key in cache, return cached result directly without calling func.
# - Otherwise, compute result, store in cache, and return it.
# - Attach the cache dictionary to the wrapper function as 'wrapper.cache'.
# =============================================================================
def simple_cache(func: Callable) -> Callable:
    # TODO: Implement custom memoization decorator
    pass


# =============================================================================
# TASK 6: DECORATOR STACKING / CHAINING
# =============================================================================
# Description:
# You are given two decorators: 'add_brackets' and 'to_uppercase'.
# Apply both decorators to 'format_title(title: str)' such that:
# format_title("python decorators") returns:
# "[PYTHON DECORATORS]"
#
# Remember the Onion Model:
# Bottom decorator wraps first, top decorator executes first!
# =============================================================================
def add_brackets(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return f"[{func(*args, **kwargs)}]"
    return wrapper

def to_uppercase(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return str(func(*args, **kwargs)).upper()
    return wrapper

# TODO: Apply @add_brackets and @to_uppercase in the correct stacking order!
def format_title(title: str) -> str:
    return title


# =============================================================================
# AUTOMATED TEST SUITE (DO NOT MODIFY)
# =============================================================================
def run_tests():
    passed = 0
    total = 6

    # Test 1
    print("\n[TEST 1] Testing audit_logger (@functools.wraps metadata preservation)...")
    try:
        @audit_logger
        def sensitive_calculation(x: int) -> int:
            """Multiplies input by 10."""
            return x * 10
        
        assert sensitive_calculation(5) == 50, "Calculation failed"
        assert sensitive_calculation.__name__ == "sensitive_calculation", f"Expected 'sensitive_calculation', got '{sensitive_calculation.__name__}'"
        assert sensitive_calculation.__doc__ == "Multiplies input by 10.", "Docstring was lost"
        print("  --> PASS: Function name and docstring preserved! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 2
    print("\n[TEST 2] Testing prefix_output (Decorator with arguments)...")
    try:
        @prefix_output("[INFO]")
        def get_db_status():
            return "Connected to PostgreSQL"
        
        res = get_db_status()
        assert res == "[INFO]: Connected to PostgreSQL", f"Got: '{res}'"
        print("  --> PASS: 3-tier decorator prefixed output correctly! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 3
    print("\n[TEST 3] Testing limit_calls (Rate limiting state)...")
    try:
        @limit_calls(max_calls=2)
        def call_ai_api():
            return "OK"
        
        assert call_ai_api() == "OK"
        assert call_ai_api() == "OK"
        try:
            call_ai_api()
            assert False, "Should have raised RuntimeError on 3rd call"
        except RuntimeError:
            pass  # Expected
        print("  --> PASS: Call limiter enforced max invocation limit! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 4
    print("\n[TEST 4] Testing validate_string_args (Type validation)...")
    try:
        @validate_string_args
        def concatenate_words(*words: str) -> str:
            return " ".join(words)
        
        assert concatenate_words("Hello", "World") == "Hello World"
        try:
            concatenate_words("Hello", 42)
            assert False, "Should have raised TypeError for non-string arg"
        except TypeError:
            pass  # Expected
        print("  --> PASS: Argument type validator rejected invalid types! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 5
    print("\n[TEST 5] Testing simple_cache (Custom Memoization)...")
    try:
        call_count = 0
        @simple_cache
        def expensive_cube(n: int) -> int:
            nonlocal call_count
            call_count += 1
            return n ** 3
        
        assert expensive_cube(4) == 64
        assert call_count == 1
        assert expensive_cube(4) == 64  # Cache hit
        assert call_count == 1, "Cache hit did not prevent function execution"
        assert expensive_cube(5) == 125  # Cache miss
        assert call_count == 2
        assert hasattr(expensive_cube, "cache") and len(expensive_cube.cache) == 2
        print("  --> PASS: Custom memoizer cached outputs in O(1) time! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 6
    print("\n[TEST 6] Testing format_title (Decorator Chaining Order)...")
    try:
        res = format_title("python decorators")
        assert res == "[PYTHON DECORATORS]", f"Expected '[PYTHON DECORATORS]', got '{res}'"
        print("  --> PASS: Decorators chained in exact execution order! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    print("\n" + "=" * 70)
    print(f"📊 FINAL SCORE: {passed}/{total} Tasks Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

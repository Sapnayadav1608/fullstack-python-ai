# =============================================================================
# DAY 12 - MODULE 01: Decorator Fundamentals, Closure Backing & @functools.wraps
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Topics Covered:
# 1. What is a Decorator? Extending Behavior Without Modifying Source Code
# 2. Manual Function Decoration vs The '@' Syntactic Sugar (Pie Syntax)
# 3. Universal Decorator Pattern (*args, **kwargs & Returning Values)
# 4. The Critical Metadata Loss Bug & How @functools.wraps Saves Introspection
# =============================================================================

import sys
import functools
from typing import Callable, Any

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 12 - MODULE 01: DECORATOR FUNDAMENTALS & @functools.wraps")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. WHAT IS A DECORATOR? (FIRST PRINCIPLES)
# -----------------------------------------------------------------------------
# A Decorator is simply a higher-order function that takes a function as an argument,
# wraps it with extra behavior, and returns the wrapped function.
# It is 100% powered by Closures and First-Class Functions from Day 11!

print("\n--- 1. Manual Decoration vs '@' Syntactic Sugar ---")

def my_logger(func: Callable) -> Callable:
    """Outer decorator function."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[LOG] Executing function: '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished '{func.__name__}' -> Returned: {result}")
        return result
    return wrapper

# Method A: Manual Assignment (Under the hood)
def calculate_tax(amount: float, tax_rate: float = 0.18) -> float:
    return amount * tax_rate

# Manually wrapping:
calculate_tax_decorated = my_logger(calculate_tax)
tax_result = calculate_tax_decorated(1000.0, tax_rate=0.18)
print("Tax Result:", tax_result)

# Method B: The Pythonic '@' Syntax (Syntactic Sugar)
# Writing '@my_logger' above a function is 100% equivalent to:
# process_payment = my_logger(process_payment)
@my_logger
def process_payment(user: str, amount: float) -> str:
    return f"Payment of ${amount:.2f} approved for {user}"

print("\nCalling @ decorated function:")
status = process_payment("Alice", 250.75)


# -----------------------------------------------------------------------------
# 2. THE UNIVERSAL DECORATOR TEMPLATE
# -----------------------------------------------------------------------------
print("\n--- 2. The Universal Decorator Template ---")

# Every production decorator must follow this 3-rule blueprint:
# 1. Accept '*args' and '**kwargs' in the inner wrapper to accept ANY signature.
# 2. Always capture the result of 'func(*args, **kwargs)'.
# 3. Always return that 'result' so the decorated function returns its data!

def uppercase_output(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_output
def get_system_status(service_name: str) -> str:
    return f"Service '{service_name}' is fully operational."

print("Uppercase Output Decorator:", get_system_status("PostgreSQL-Primary"))


# -----------------------------------------------------------------------------
# 3. THE CRITICAL FUNCTION METADATA LOSS BUG ⚠️
# -----------------------------------------------------------------------------
print("\n--- 3. Function Metadata Loss Bug (Interview Favorite) ---")

def bad_decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """I am the wrapper docstring!"""
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def fetch_user_data(user_id: int) -> dict:
    """Fetches user profile and permissions from the database."""
    return {"id": user_id, "name": "Sapna Yadav"}

# Notice what happened to fetch_user_data's identity:
print(f"Function Name     : {fetch_user_data.__name__}")  # Prints 'wrapper'! 😱
print(f"Function Docstring: {fetch_user_data.__doc__}")   # Prints 'I am the wrapper docstring!' 🤯
# ⚠️ WHY THIS IS DANGEROUS IN PRODUCTION:
# 1. Debuggers and stack traces show 'wrapper' instead of the actual function name!
# 2. Frameworks like FastAPI, Flask, and Sphinx documentation use __name__ and __doc__
#    to build automated OpenAPI documentation and route matching!


# -----------------------------------------------------------------------------
# 4. THE FIX: @functools.wraps TO THE RESCUE ✅
# -----------------------------------------------------------------------------
print("\n--- 4. The Pythonic Solution: @functools.wraps ---")

def clean_decorator(func: Callable) -> Callable:
    # @functools.wraps copies the original function's name, docstring,
    # annotations, and module identity onto the wrapper!
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return wrapper

@clean_decorator
def fetch_secure_token(client_id: str) -> str:
    """Generates an OAuth2 authentication bearer token for the client."""
    return f"tok_{client_id}_xyz999"

print(f"Function Name (Cleaned)     : {fetch_secure_token.__name__} ✅")  # 'fetch_secure_token'
print(f"Function Docstring (Cleaned): {fetch_secure_token.__doc__} ✅")   # Original docstring preserved!
print(f"Original Function Reference : {fetch_secure_token.__wrapped__}")  # Direct access to un-decorated fn!

print("\n" + "=" * 75)
print("✅ MODULE 01 COMPLETE: Decorators & @functools.wraps mastered!")
print("=" * 75)

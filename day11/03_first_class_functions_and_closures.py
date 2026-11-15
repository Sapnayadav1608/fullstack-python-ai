# =============================================================================
# DAY 11 - MODULE 03: First-Class Functions, Higher-Order Patterns & Closures
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Topics Covered:
# 1. Functions as First-Class Objects (Assignment, Passing, Returning & Tables)
# 2. Higher-Order Functions: Building Custom map() and filter() from Scratch
# 3. What is a Closure? Lexical Scope Retention & CPython __closure__ Inspection
# 4. Production Closure Patterns:
#    - Pattern A: Dynamic Function Factory (Custom Power & Tax Calculators)
#    - Pattern B: Streaming Cumulative Moving Average Engine (O(1) Memory)
# =============================================================================

import sys
from typing import Callable, List, Any, Dict

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 11 - MODULE 03: FIRST-CLASS CITIZENS, HIGHER-ORDER CODE & CLOSURES")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. FIRST-CLASS CITIZENS IN PYTHON
# -----------------------------------------------------------------------------
# In Python, functions are first-class citizens. They are objects of type 'function',
# just like integers, strings, or lists!
print("\n--- 1. Functions as First-Class Citizens ---")

def format_json_response(data: str) -> str:
    return f'{{"status": "success", "payload": "{data}"}}'

def format_xml_response(data: str) -> str:
    return f"<response><status>success</status><payload>{data}</payload></response>"

# A. Assigning function to a variable:
formatter = format_json_response
print(f"Assigned Function Object: {formatter} | Type: {type(formatter)}")
print(f"Calling via variable   : {formatter('User authenticated')}")

# B. Storing functions in a dictionary (Command Dispatcher / Router Pattern):
# This replaces messy if-elif-else chains with an O(1) dictionary dispatch table!
SERIALIZERS: Dict[str, Callable[[str], str]] = {
    "json": format_json_response,
    "xml": format_xml_response
}

def serialize_data(format_type: str, data: str) -> str:
    handler = SERIALIZERS.get(format_type)
    if not handler:
        raise ValueError(f"Unsupported serialization format: '{format_type}'")
    return handler(data)

print("Dispatch JSON:", serialize_data("json", "Alice (Admin)"))
print("Dispatch XML :", serialize_data("xml", "Bob (Engineer)"))


# -----------------------------------------------------------------------------
# 2. HIGHER-ORDER FUNCTIONS (PASSING & RETURNING FUNCTIONS)
# -----------------------------------------------------------------------------
print("\n--- 2. Higher-Order Functions from Scratch ---")

# Higher-order function: A function that takes another function as an argument
# OR returns a function as its result.

def custom_transformer(items: List[int], transform_fn: Callable[[int], int]) -> List[int]:
    """Applies a custom transformation function to every item in the list."""
    return [transform_fn(x) for x in items]

def square(n: int) -> int:
    return n * n

def cube(n: int) -> int:
    return n * n * n

nums = [1, 2, 3, 4, 5]
print("Original numbers :", nums)
print("Squared via HOF  :", custom_transformer(nums, square))
print("Cubed via HOF    :", custom_transformer(nums, cube))


# -----------------------------------------------------------------------------
# 3. WHAT IS A CLOSURE? (LEXICAL SCOPE RETENTION)
# -----------------------------------------------------------------------------
print("\n--- 3. Closures & Lexical Scope Retention ---")

# A CLOSURE is a function object that remembers values in enclosing scopes
# even if they are no longer present in memory (i.e. outer function has finished executing)!
#
# Three Rules of a Closure:
# 1. We must have a nested function.
# 2. The nested function must refer to a value defined in the enclosing function.
# 3. The enclosing function must RETURN the nested function object.

def make_multiplier(factor: int) -> Callable[[int], int]:
    """Outer function: Once it returns, its local stack frame is destroyed!"""
    def multiplier(number: int) -> int:
        # 'factor' is retained in the closure's hidden cell!
        return number * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print("double(10) =", double(10))  # 20
print("triple(10) =", triple(10))  # 30

# CPython Under the Hood: Inspecting the Closure Cell!
print("\nCPython Closure Cell Introspection:")
print(f"double.__closure__      : {double.__closure__}")
print(f"double cell value       : {double.__closure__[0].cell_contents}")  # 2
print(f"triple cell value       : {triple.__closure__[0].cell_contents}")  # 3
print("✨ The outer function is gone, but the inner function holds the cell alive in memory!")


# -----------------------------------------------------------------------------
# 4. REAL-WORLD PRODUCTION CLOSURE PATTERNS
# -----------------------------------------------------------------------------
print("\n--- 4. Real-World Production Patterns with Closures ---")

# Pattern A: Configurable Currency Formatter (Function Factory)
def create_currency_formatter(symbol: str, decimals: int = 2) -> Callable[[float], str]:
    """Generates localized price formatters without repeating configuration."""
    def formatter(amount: float) -> str:
        return f"{symbol}{amount:,.{decimals}f}"
    return formatter

format_usd = create_currency_formatter("$", 2)
format_inr = create_currency_formatter("₹", 2)
format_crypto = create_currency_formatter("₿", 6)

print("Product Price (USD)   :", format_usd(14999.50))
print("Product Price (INR)   :", format_inr(1249999.75))
print("Crypto Balance        :", format_crypto(0.0451299))


# Pattern B: Streaming Cumulative Moving Average Engine (O(1) Space!)
# Instead of storing millions of data points in a list (O(N) RAM),
# this closure tracks only running count and sum in O(1) space!
def create_moving_average_tracker() -> Callable[[float], float]:
    total_sum = 0.0
    count = 0
    
    def add_reading(value: float) -> float:
        nonlocal total_sum, count
        total_sum += value
        count += 1
        return total_sum / count
        
    return add_reading

sensor_avg = create_moving_average_tracker()
print("\nStreaming Sensor Moving Average:")
readings = [24.0, 26.0, 25.0, 28.0, 31.0]
for r in readings:
    current_avg = sensor_avg(r)
    print(f"  - New Reading: {r:.1f}°C | Current Average: {current_avg:.2f}°C")

print("\n" + "=" * 75)
print("✅ MODULE 03 COMPLETE: First-class functions, HOFs & closures mastered!")
print("=" * 75)

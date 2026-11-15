# =============================================================================
# DAY 11 - MODULE 02: Variable Scopes, LEGB Rule & The UnboundLocalError Trap
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Topics Covered:
# 1. The LEGB Scope Resolution Hierarchy (Local -> Enclosing -> Global -> Built-in)
# 2. Variable Shadowing: How local scopes protect outer namespaces
# 3. The 'global' Keyword: Modifying module-level state & why it's an anti-pattern
# 4. The 'nonlocal' Keyword: Mutating enclosing function scopes in nested closures
# 5. The Tricky UnboundLocalError Trap (CPython Compile-Time Local Detection)
# =============================================================================

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 11 - MODULE 02: SCOPES, LEGB HIERARCHY & UNBOUNDLOCALERROR TRAPS")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. THE LEGB RULE EXPLAINED VISUALLY
# -----------------------------------------------------------------------------
# When Python looks up a variable name, it searches in this exact strict order:
#   [L] Local     : Defined inside the current function body
#   [E] Enclosing : Defined in any outer enclosing functions (nested functions)
#   [G] Global    : Defined at the top-level of the module / script
#   [B] Built-in  : Built into Python language (len, sum, min, max, print, etc.)
# If not found in any of these 4, Python raises a NameError!

print("\n--- 1. LEGB Hierarchy in Action ---")

x_global = "I am GLOBAL [G]"

def outer_enclosing():
    x_enclosing = "I am ENCLOSING [E]"
    
    def inner_local():
        x_local = "I am LOCAL [L]"
        print(f"Inner function sees -> {x_local}")
        print(f"Inner function sees -> {x_enclosing}")
        print(f"Inner function sees -> {x_global}")
        print(f"Inner function sees -> {len([1, 2, 3])} (via BUILT-IN [B])")
        
    inner_local()

outer_enclosing()


# -----------------------------------------------------------------------------
# 2. VARIABLE SHADOWING (LOCAL PROTECTS GLOBAL)
# -----------------------------------------------------------------------------
print("\n--- 2. Variable Shadowing ---")

app_env = "production"

def set_test_mode():
    # Defining app_env here SHADOWS the global app_env locally.
    # It creates a brand-new local variable in the function's stack frame!
    app_env = "test_sandbox"
    print(f"Inside function (local shadowed) : {app_env}")

set_test_mode()
print(f"Outside function (global unchanged): {app_env} ✅")


# -----------------------------------------------------------------------------
# 3. THE 'global' KEYWORD & ARCHITECTURAL PITFALLS
# -----------------------------------------------------------------------------
print("\n--- 3. The 'global' Keyword ---")

request_counter = 0

def track_request_bad():
    # Attempting `request_counter += 1` directly without 'global' raises UnboundLocalError!
    # With 'global', Python binds this variable directly to the module namespace.
    global request_counter
    request_counter += 1
    return request_counter

print("Request 1:", track_request_bad())
print("Request 2:", track_request_bad())
print("Request 3:", track_request_bad())
print(f"Global request_counter is now: {request_counter}")

# ⚠️ WHY 'global' IS DANGEROUS IN PRODUCTION:
# 1. State pollution: Any function anywhere can silently mutate it.
# 2. Testing nightmare: Unit tests cannot run independently because state leaks.
# 3. Concurrency bugs: Multi-threaded web servers (FastAPI/Flask) experience race conditions!
# BEST PRACTICE: Pass parameters explicitly and return modified objects, or use Classes/Closures!


# -----------------------------------------------------------------------------
# 4. THE 'nonlocal' KEYWORD (BRIDGING ENCLOSING SCOPES)
# -----------------------------------------------------------------------------
print("\n--- 4. The 'nonlocal' Keyword (Nested Scopes) ---")

def create_rate_limiter(max_calls: int):
    """Factory function that creates a stateful rate limiter closure."""
    call_count = 0  # Enclosing scope variable [E]
    
    def attempt_request(client_ip: str) -> bool:
        nonlocal call_count  # Binds directly to 'call_count' in enclosing scope!
        
        if call_count < max_calls:
            call_count += 1
            print(f"[ALLOWED] IP: {client_ip} | Calls used: {call_count}/{max_calls}")
            return True
        else:
            print(f"[DENIED 429] IP: {client_ip} | Rate limit reached ({max_calls})!")
            return False
            
    return attempt_request

limiter = create_rate_limiter(max_calls=3)
limiter("192.168.1.10")  # Call 1: Allowed
limiter("192.168.1.10")  # Call 2: Allowed
limiter("192.168.1.10")  # Call 3: Allowed
limiter("192.168.1.10")  # Call 4: Denied! 429 Too Many Requests


# -----------------------------------------------------------------------------
# 5. THE TRICKY 'UnboundLocalError' INTERVIEW TRAP ⚠️
# -----------------------------------------------------------------------------
print("\n--- 5. The Infamous UnboundLocalError Trap ---")

counter = 100

def buggy_function():
    # If a variable is ASSIGNED anywhere inside a function, Python's compiler
    # flags it as a LOCAL variable for the ENTIRE function scope during compilation!
    #
    # Therefore, if you read it BEFORE the assignment line, Python will NOT fall
    # back to the global variable — it crashes with UnboundLocalError!
    try:
        # print("Value is:", counter)  # <-- If uncommented, crashes right here!
        # counter += 1                 # Assignment makes 'counter' local!
        raise UnboundLocalError("local variable 'counter' referenced before assignment")
    except UnboundLocalError as e:
        print(f"Caught classic bug: {e}")
        print("💡 Why? Because CPython flags 'counter' as LOCAL due to assignment later in function!")

buggy_function()

# Proper Fix 1: Pass as argument and return value
def clean_increment(val: int) -> int:
    return val + 1

counter = clean_increment(counter)
print(f"Clean functional increment without global bugs: {counter} ✅")

# Proper Fix 2: Explicit global declaration (if truly necessary)
def explicit_global_increment():
    global counter
    counter += 1

explicit_global_increment()
print(f"Explicit global increment: {counter} ✅")


# -----------------------------------------------------------------------------
# 6. BUILT-IN SHADOWING WARNING ⚠️
# -----------------------------------------------------------------------------
print("\n--- 6. Danger of Shadowing Built-In Functions ---")

# Beginners often name variables 'list', 'str', 'dict', 'sum', 'min', 'max'
# Example:
# list = [1, 2, 3]       # ❌ Shadows the built-in 'list' constructor!
# new_l = list((4, 5))   # TypeError: 'list' object is not callable!
#
# Always use descriptive names like 'items_list', 'num_sum', 'total_count'.

print("Current built-ins available in module scope:", dir(__builtins__)[:6], "...")

print("\n" + "=" * 75)
print("✅ MODULE 02 COMPLETE: LEGB rule, nonlocal closures & scope bugs mastered!")
print("=" * 75)

# =============================================================================
# DAY 12 - MODULE 02: Decorators with Arguments & Decorator Chaining
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Topics Covered:
# 1. Decorators with Arguments: The 3-Tier Nested Closure Architecture
# 2. Decorator Chaining / Stacking (Multiple @ Decorators on One Function)
# 3. Execution Order Deep Dive: Bottom-Up Wrapping vs Top-Down Execution (The Onion Model)
# 4. Real-World Demonstrator: Configurable HTML Tag Generators & Validation Pipeline
# =============================================================================

import sys
import functools
from typing import Callable, Any

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 12 - MODULE 02: DECORATORS WITH ARGUMENTS & CHAINING (ONION MODEL)")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. DECORATORS WITH ARGUMENTS (THE 3-TIER CLOSURE)
# -----------------------------------------------------------------------------
# If a decorator needs arguments (e.g. @repeat(num_times=3)), you need THREE levels:
# Level 1: Outer function that receives decorator arguments (e.g. num_times).
# Level 2: Middle function that receives the target function (func).
# Level 3: Inner wrapper that receives runtime arguments (*args, **kwargs).

print("\n--- 1. 3-Tier Nested Closure Decorator ---")

def repeat(num_times: int = 2):
    """Tier 1: Accepts decorator configuration arguments."""
    def decorator(func: Callable) -> Callable:
        """Tier 2: Receives the function to be decorated."""
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Tier 3: Executes at runtime with function arguments."""
            result = None
            for iteration in range(1, num_times + 1):
                print(f"[RETRY RUN {iteration}/{num_times}] Calling '{func.__name__}'...")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def ping_service(service_url: str) -> str:
    return f"200 OK from {service_url}"

print("Calling @repeat(num_times=3):")
final_response = ping_service("https://api.openai.com/v1/models")
print("Ping Result:", final_response)


# -----------------------------------------------------------------------------
# 2. DECORATOR CHAINING / STACKING (THE ONION MODEL) 🧅
# -----------------------------------------------------------------------------
# When multiple decorators are applied to a single function:
#
#   @decorator_a
#   @decorator_b
#   def greet(): ...
#
# Python evaluates this under the hood as:
#   greet = decorator_a(decorator_b(greet))
#
# 1. Wrapping Order : BOTTOM-TO-TOP (decorator_b wraps first, then decorator_a wraps b)
# 2. Execution Order: TOP-TO-BOTTOM  (decorator_a runs -> decorator_b runs -> greet runs)

print("\n--- 2. Decorator Chaining Order Demonstration ---")

def tag_bold(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print("  --> Entering @tag_bold")
        result = func(*args, **kwargs)
        print("  <-- Exiting @tag_bold")
        return f"<b>{result}</b>"
    return wrapper

def tag_italic(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print("  --> Entering @tag_italic")
        result = func(*args, **kwargs)
        print("  <-- Exiting @tag_italic")
        return f"<i>{result}</i>"
    return wrapper

# Stacking Bold over Italic:
@tag_bold
@tag_italic
def render_markdown(text: str) -> str:
    print(f"      [CORE FUNCTION] rendering text: '{text}'")
    return text

print("Calling Stacked Decorators @tag_bold then @tag_italic:")
html_output = render_markdown("Python Functions & Decorators")
print("\nFinal HTML Result:", html_output)
# Expected: <b><i>Python Functions & Decorators</i></b>


# -----------------------------------------------------------------------------
# 3. PRACTICAL COMBINATION: CONFIGURABLE TAG FACTORY
# -----------------------------------------------------------------------------
print("\n--- 3. Configurable Custom Tag Decorator Factory ---")

def html_tag(tag_name: str):
    """Generates arbitrary HTML tag wrapping decorators dynamically."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            res = func(*args, **kwargs)
            return f"<{tag_name}>{res}</{tag_name}>"
        return wrapper
    return decorator

@html_tag("div")
@html_tag("section")
@html_tag("h1")
def generate_hero_banner(title: str) -> str:
    return title

banner_html = generate_hero_banner("Mastering Full Stack AI in 30 Days")
print("Nested Dynamic Tags Result:")
print(banner_html)

print("\n" + "=" * 75)
print("✅ MODULE 02 COMPLETE: 3-Tier decorators & chaining order mastered!")
print("=" * 75)

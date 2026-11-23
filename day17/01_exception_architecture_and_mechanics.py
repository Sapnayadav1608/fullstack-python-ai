"""
================================================================================
DAY 17: ADVANCED EXCEPTION HANDLING & DEFENSIVE AI ARCHITECTURE
Module 01: Exception Architecture, Lifecycle & Anti-Patterns
================================================================================
Topics Covered:
  1. The CPython Exception Class Hierarchy (BaseException vs Exception)
  2. The 4-Clause Lifecycle: try / except / else / finally
  3. The Golden Role of 'else': Isolating Try blocks from False Positives
  4. Call Stack Unwinding & Exception Bubbling Dynamics
  5. The Deadly Anti-Patterns: 'except: pass', Catch-All Swallowing
  6. Diagnostic Introspection: sys.exc_info() & traceback.format_exc()
  7. Enterprise AI Pattern: SafeModelCallWrapper with Structured Diagnostics
================================================================================
"""

import sys
import traceback
from typing import Any, Dict, Optional, Callable


# ==============================================================================
# SECTION 1: CPYTHON EXCEPTION HIERARCHY — BaseException vs Exception
# ==============================================================================
# Python's built-in exceptions form an inheritance tree:
#
#   BaseException
#    ├── SystemExit             (raised by sys.exit())
#    ├── KeyboardInterrupt      (raised when user hits Ctrl+C)
#    ├── GeneratorExit          (raised when a generator closes)
#    └── Exception              (root of all application & library errors)
#         ├── ArithmeticError   (ZeroDivisionError, OverflowError)
#         ├── LookupError       (IndexError, KeyError)
#         ├── ValueError
#         ├── TypeError
#         └── RuntimeError
#
# CRITICAL RULE: NEVER catch BaseException! Catching BaseException intercepts
# KeyboardInterrupt and SystemExit, making your application impossible to terminate!
# Always derive your custom application exceptions from `Exception`, not `BaseException`.

def demonstrate_hierarchy_safety():
    print("=" * 75)
    print("SECTION 1: EXCEPTION HIERARCHY & BaseException DANGERS")
    print("=" * 75)

    # Proof: KeyError and IndexError both inherit from LookupError
    print(f"issubclass(KeyError, LookupError):       {issubclass(KeyError, LookupError)}")
    print(f"issubclass(IndexError, LookupError):     {issubclass(IndexError, LookupError)}")
    print(f"issubclass(ZeroDivisionError, ArithmeticError): {issubclass(ZeroDivisionError, ArithmeticError)}")
    print(f"issubclass(KeyboardInterrupt, Exception): {issubclass(KeyboardInterrupt, Exception)} (Inherits from BaseException!)")

    # Safe multi-exception handling using parent classes:
    def safe_lookup(collection: Any, key: Any) -> Any:
        try:
            return collection[key]
        except LookupError as err:
            # Handles BOTH IndexError (lists) and KeyError (dicts) cleanly!
            print(f"  [Handled LookupError] Failed access on {type(collection).__name__} for key={key!r}: {err}")
            return None

    safe_lookup(["token1", "token2"], 10)     # IndexError
    safe_lookup({"model": "gemini"}, "temp")  # KeyError


# ==============================================================================
# SECTION 2 & 3: THE 4-CLAUSE LIFECYCLE (try / except / else / finally)
# ==============================================================================
# The Python `else` clause in try-blocks is one of the most under-utilized features!
#   - `try`: Put ONLY the single risky operation that can raise the target error.
#   - `except`: Handles only the expected failure.
#   - `else`: Runs ONLY if the try block succeeded without exceptions!
#     Why not put it in `try`? If code in `else` raises the same error type,
#     putting it in `try` would cause your `except` to falsely catch its own downstream bugs!
#   - `finally`: Guaranteed execution in ALL cases (success, caught error, or unhandled crash).
#     Essential for closing network connections, releasing locks, and flushing buffers.

def parse_llm_hyperparameters(raw_payload: Dict[str, Any]) -> Dict[str, float]:
    """Demonstrates clean 4-clause lifecycle in payload parsing."""
    print("\n" + "=" * 75)
    print("SECTION 2 & 3: THE 4-CLAUSE LIFECYCLE (try / except / else / finally)")
    print("=" * 75)

    temp_val = None
    telemetry = {"status": "pending", "cleaned_temp": None}

    try:
        # Step 1: Risky operation ONLY inside try
        print("  1. [try] Extracting and casting temperature...")
        temp_val = float(raw_payload["temperature"])
    except KeyError:
        print("  2. [except] Missing 'temperature' key! Setting default 0.7")
        temp_val = 0.7
        telemetry["status"] = "default_fallback"
    except (ValueError, TypeError) as err:
        print(f"  2. [except] Invalid temperature format ({err})! Setting default 0.7")
        temp_val = 0.7
        telemetry["status"] = "coercion_fallback"
    else:
        # Step 3: Runs ONLY if try succeeded without any exceptions
        print(f"  3. [else] Successfully parsed raw temperature: {temp_val:.2f}")
        # Validate business bounds (clamping)
        temp_val = max(0.0, min(2.0, temp_val))
        telemetry["status"] = "validated_success"
    finally:
        # Step 4: Always runs (resource cleanup or telemetry logging)
        telemetry["cleaned_temp"] = temp_val
        print(f"  4. [finally] Telemetry emitted: {telemetry}")

    return {"temperature": temp_val}


# ==============================================================================
# SECTION 4 & 5: ANTI-PATTERNS & EXCEPTION SWALLOWING
# ==============================================================================
# ANTI-PATTERN 1: The "Pokemon Catch" / Bare Except:
#   try: ...
#   except: pass  <-- NEVER DO THIS! Silently ignores typos, Ctrl+C, memory errors!
#
# ANTI-PATTERN 2: Swallowing Tracebacks without Re-Raising:
#   try: ...
#   except Exception:
#       return None  <-- Bugs vanish into a black hole; production nightmare to debug!

def demonstrate_anti_patterns():
    print("\n" + "=" * 75)
    print("SECTION 4 & 5: DEADLY ANTI-PATTERNS & EXCEPTION SWALLOWING")
    print("=" * 75)

    def flawed_anti_pattern():
        try:
            # Subtle typo: calling math.sqrtt instead of math.sqrt
            import math
            return math.sqrtt(16)  # AttributeError!
        except:
            # Bare except swallows the typo! Developer thinks result was 0.0!
            return 0.0

    print(f"Flawed Bare Except Result: {flawed_anti_pattern()} (Hides typo AttributeError!)")

    # Correct Professional Pattern: Catch specific, log traceback, and re-raise or route
    def correct_diagnostic_pattern():
        try:
            import math
            return math.sqrtt(16)
        except AttributeError as e:
            # Capture complete stack trace
            exc_type, exc_val, exc_tb = sys.exc_info()
            tb_string = "".join(traceback.format_exception(exc_type, exc_val, exc_tb))
            print(f"  -> Properly caught & logged diagnostic: {e}")
            print(f"  -> Stack frame origin: {exc_tb.tb_frame.f_code.co_name} at line {exc_tb.tb_lineno}")
            return None

    correct_diagnostic_pattern()


# ==============================================================================
# SECTION 6: ENTERPRISE AI PATTERN — SafeModelCallWrapper
# ==============================================================================
class SafeModelCallWrapper:
    """
    Production AI Service wrapper that safely executes inference calls,
    records execution telemetry, and generates diagnostic error envelopes.
    """
    def __init__(self, service_name: str = "GeminiInferenceService"):
        self.service_name = service_name
        self.call_count = 0
        self.error_count = 0

    def execute(self, inference_fn: Callable[..., str], *args, **kwargs) -> Dict[str, Any]:
        """
        Executes an inference routine with guaranteed error isolation
        and diagnostic stack trace capture.
        """
        self.call_count += 1
        envelope = {
            "service": self.service_name,
            "success": False,
            "result": None,
            "error_type": None,
            "error_message": None,
            "traceback": None
        }

        try:
            raw_output = inference_fn(*args, **kwargs)
        except (ValueError, TypeError) as client_err:
            self.error_count += 1
            envelope["error_type"] = "ClientPayloadError"
            envelope["error_message"] = str(client_err)
            envelope["traceback"] = traceback.format_exc()
        except RuntimeError as runtime_err:
            self.error_count += 1
            envelope["error_type"] = "ProviderRuntimeError"
            envelope["error_message"] = str(runtime_err)
            envelope["traceback"] = traceback.format_exc()
        except Exception as unexpected_err:
            self.error_count += 1
            envelope["error_type"] = "UnexpectedSystemError"
            envelope["error_message"] = str(unexpected_err)
            envelope["traceback"] = traceback.format_exc()
        else:
            envelope["success"] = True
            envelope["result"] = raw_output
        finally:
            print(f"[{self.service_name}] Invocation #{self.call_count} | Success: {envelope['success']}")

        return envelope


def demonstrate_safe_wrapper():
    print("\n" + "=" * 75)
    print("SECTION 6: ENTERPRISE AI PATTERN — SafeModelCallWrapper")
    print("=" * 75)

    wrapper = SafeModelCallWrapper("GeminiFlashPipeline")

    # 1. Successful inference simulation
    def successful_prompt(prompt: str) -> str:
        return f"Generated response for: {prompt[:30]}"

    res1 = wrapper.execute(successful_prompt, "Explain Python Exception Groups.")
    print(f"Success Envelope: result={res1['result']!r}")

    # 2. Simulated client error (empty payload)
    def failing_prompt(prompt: str) -> str:
        if not prompt:
            raise ValueError("Prompt string cannot be empty or whitespace")
        return "Done"

    res2 = wrapper.execute(failing_prompt, "")
    print(f"Error Envelope:   type={res2['error_type']}, msg={res2['error_message']!r}")


if __name__ == "__main__":
    demonstrate_hierarchy_safety()
    parse_llm_hyperparameters({"temperature": "0.85"})
    parse_llm_hyperparameters({"temp_missing": 0.5})
    demonstrate_anti_patterns()
    demonstrate_safe_wrapper()

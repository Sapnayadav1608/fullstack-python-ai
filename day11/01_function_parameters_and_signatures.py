# =============================================================================
# DAY 11 - MODULE 01: Function Parameters, Signatures & The Mutable Default Trap
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Topics Covered:
# 1. Positional vs Keyword Arguments (Semantics & Ordering Rules)
# 2. The Infamous Mutable Default Argument Trap (CPython Bytecode & id() Proof)
# 3. Variable-Length Arguments (*args Tuple Unpacking & **kwargs Dict Unpacking)
# 4. Modern Python 3.8+ Parameter Markers: Positional-Only (/) & Keyword-Only (*)
# 5. Type Hints, Docstrings (__doc__) & Introspection (__name__, inspect module)
# =============================================================================

import sys
import inspect
from typing import List, Optional, Dict, Any

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 11 - MODULE 01: FUNCTION PARAMETERS, SIGNATURES & ARGUMENT TRAPS")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. POSITIONAL VS KEYWORD ARGUMENTS
# -----------------------------------------------------------------------------
print("\n--- 1. Positional vs Keyword Arguments ---")

def configure_server(host: str, port: int, debug: bool = False, timeout: int = 30) -> str:
    """Configures a backend server instance with custom networking options."""
    mode = "DEBUG" if debug else "PRODUCTION"
    return f"[{mode}] Server running on {host}:{port} (timeout={timeout}s)"

# Passing purely positional arguments (Order matters strictly)
res1 = configure_server("127.0.0.1", 8000)
print("Positional only      :", res1)

# Passing mixed: positional first, then keyword arguments
res2 = configure_server("0.0.0.0", 443, timeout=60, debug=True)
print("Mixed positional/kw  :", res2)

# RULE: Positional arguments CANNOT follow keyword arguments!
# SyntaxError: positional argument follows keyword argument
# configure_server(host="127.0.0.1", 8000)  # <-- INVALID!


# -----------------------------------------------------------------------------
# 2. THE INFAMOUS MUTABLE DEFAULT ARGUMENT TRAP ⚠️
# -----------------------------------------------------------------------------
print("\n--- 2. The Mutable Default Argument Trap (The #1 Python Interview Gotcha) ---")

# ❌ DANGEROUS PATTERN:
# In Python, default arguments are evaluated ONCE when the function definition is
# loaded into memory (compile-time), NOT each time the function is called!
def add_user_bad(user_id: int, user_list: List[int] = []) -> List[int]:
    user_list.append(user_id)
    return user_list

print("Call 1 (add 101):", add_user_bad(101))  # [101]
print("Call 2 (add 202):", add_user_bad(202))  # [101, 202] 😱 (Preserved from Call 1!)
print("Call 3 (add 303):", add_user_bad(303))  # [101, 202, 303] 🤯 (Shared list across calls!)

# Memory Proof: Look at the id of the default argument stored in the function object
print("Function __defaults__ id:", id(add_user_bad.__defaults__[0]))

# ✅ THE PYTHONIC FIX: Use 'None' as default sentinel value
def add_user_clean(user_id: int, user_list: Optional[List[int]] = None) -> List[int]:
    """Uses None as sentinel and creates a fresh empty list at runtime for each call."""
    if user_list is None:
        user_list = []  # Brand new list created in local scope per invocation
    user_list.append(user_id)
    return user_list

print("\nAfter Fix with None Sentinel:")
print("Call 1 (clean):", add_user_clean(101))  # [101]
print("Call 2 (clean):", add_user_clean(202))  # [202]  (Completely isolated! ✨)
print("Call 3 (clean):", add_user_clean(303))  # [303]  (Safe & deterministic! ✅)


# -----------------------------------------------------------------------------
# 3. VARIABLE-LENGTH ARGUMENTS: *args & **kwargs
# -----------------------------------------------------------------------------
print("\n--- 3. Variable-Length Arguments (*args & **kwargs) ---")

# *args gathers arbitrary positional arguments into a TUPLE
# **kwargs gathers arbitrary keyword arguments into a DICTIONARY
def build_ai_prompt(system_role: str, *context_docs: str, **model_params: Any) -> str:
    """Combines a system role, multiple context documents, and arbitrary LLM parameters."""
    print(f"\nSystem Role   : {system_role}")
    print(f"Context Docs  : {type(context_docs)} with {len(context_docs)} documents -> {context_docs}")
    print(f"Model Params  : {type(model_params)} -> {model_params}")
    
    # Prompt string generation
    joined_docs = "\n".join(f"- {doc}" for doc in context_docs)
    temp = model_params.get("temperature", 0.7)
    max_tokens = model_params.get("max_tokens", 1024)
    
    return (
        f"Prompt Configured [Temp={temp}, MaxTokens={max_tokens}]:\n"
        f"System: {system_role}\n"
        f"Knowledge Base:\n{joined_docs}"
    )

prompt_output = build_ai_prompt(
    "Senior Python & AI Architect",
    "Doc 1: Python Memory Model & GC",
    "Doc 2: CPython Hash Table Spec",
    "Doc 3: LangChain Vector Indexing",
    temperature=0.2,
    model_name="gemini-2.0-flash",
    max_tokens=4096,
    stream=True
)
print(prompt_output)

# Unpacking callers: Unpacking lists/tuples with * and dicts with **
extra_docs = ("Doc 4: FastAPI Microservices", "Doc 5: PostgreSQL Indexing")
extra_params = {"temperature": 0.0, "max_tokens": 8192}
unpacked_prompt = build_ai_prompt("DB Tuner", *extra_docs, **extra_params)
print("\nUnpacked caller output status: Successfully injected into prompt engine! ✅")


# -----------------------------------------------------------------------------
# 4. PYTHON 3.8+ MODERN PARAMETER MARKERS: / (Positional-Only) & * (Keyword-Only)
# -----------------------------------------------------------------------------
print("\n--- 4. Python 3.8+ Parameter Markers: '/' and '*' ---")

# Syntax:
# def f(pos_only_1, pos_only_2, /, standard_arg, *, kw_only_1, kw_only_2):
# - Everything BEFORE '/' MUST be passed positionally.
# - Everything AFTER '*' MUST be passed by keyword (named).
# - Everything between '/' and '*' can be passed either way.

def create_api_endpoint(
    path: str,
    method: str,
    /,                       # Positional-Only Marker
    rate_limit: int = 100,   # Standard (either positional or keyword)
    *,                       # Keyword-Only Marker
    auth_required: bool = True,
    cors_allow_all: bool = False
) -> Dict[str, Any]:
    return {
        "endpoint": f"{method.upper()} {path}",
        "rate_limit_rpm": rate_limit,
        "security": {"auth": auth_required, "cors": cors_allow_all}
    }

# Valid call:
ep1 = create_api_endpoint("/api/v1/users", "POST", 50, auth_required=True, cors_allow_all=False)
print("Valid API Endpoint Config:", ep1)

# Calling with keyword before '/' raises TypeError:
# create_api_endpoint(path="/api/v1/users", method="GET")
# -> TypeError: create_api_endpoint() got some positional-only arguments passed as keyword arguments: 'path, method'

# Calling positional after '*' raises TypeError:
# create_api_endpoint("/api/v1/users", "GET", 100, True)
# -> TypeError: create_api_endpoint() takes from 2 to 3 positional arguments but 4 were given


# -----------------------------------------------------------------------------
# 5. FUNCTION INTROSPECTION & METADATA
# -----------------------------------------------------------------------------
print("\n--- 5. Function Introspection & Signatures ---")

def calculate_discount(price: float, discount_percent: float = 10.0) -> float:
    """Calculates discounted final bill amount after applying percentage cut."""
    return price * (1.0 - discount_percent / 100.0)

print(f"Function Name     : {calculate_discount.__name__}")
print(f"Function Docstring: {calculate_discount.__doc__}")
print(f"Annotations       : {calculate_discount.__annotations__}")

# Inspect Module: Pythonic Signature Examination
sig = inspect.signature(calculate_discount)
print(f"Full Signature    : {sig}")
for param_name, param_obj in sig.parameters.items():
    print(f"  - Parameter '{param_name}': default={param_obj.default}, kind={param_obj.kind.name}")

print("\n" + "=" * 75)
print("✅ MODULE 01 COMPLETE: Parameter rules, *args/**kwargs & mutable default mastered!")
print("=" * 75)

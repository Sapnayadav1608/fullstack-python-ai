# =============================================================================
# DAY 12 - MODULE 03: Real-World Backend & AI Decorators
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Production Decorator Patterns:
# 1. @timer: High-Precision Latency Benchmark Profiler (Microseconds & MS)
# 2. @retry: Resilient LLM / Network Retry with Exponential Backoff
# 3. @require_role: Security & Role-Based Access Control (RBAC 403 Forbidden)
# =============================================================================

import sys
import time
import functools
from typing import Callable, Any, Dict, List

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 12 - MODULE 03: PRODUCTION BACKEND & AI ENGINEERING DECORATORS")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. THE PERFORMANCE & LATENCY PROFILER (@timer)
# -----------------------------------------------------------------------------
print("\n--- 1. @timer: High-Precision Latency Profiler ---")

def timer(func: Callable) -> Callable:
    """Measures precise execution latency of backend operations."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000.0
        print(f"⏱️  [PROFILER] '{func.__name__}' executed in {elapsed_ms:.4f} ms")
        return result
    return wrapper

@timer
def compute_vector_dot_product(vec_a: List[float], vec_b: List[float]) -> float:
    """Simulates AI vector embedding similarity calculation."""
    return sum(a * b for a, b in zip(vec_a, vec_b))

# Run vector calculation
v1 = [0.12, 0.45, 0.88, 0.23, 0.91] * 50_000
v2 = [0.99, 0.11, 0.33, 0.77, 0.44] * 50_000
dot_product = compute_vector_dot_product(v1, v2)
print(f"Vector Similarity Score: {dot_product:.2f}")


# -----------------------------------------------------------------------------
# 2. RESILIENT NETWORK RETRY WITH EXPONENTIAL BACKOFF (@retry)
# -----------------------------------------------------------------------------
# Essential for LLM API calls (Gemini, OpenAI, Anthropic) to survive
# transient HTTP 429 (Rate Limit) and HTTP 503 (Service Unavailable) errors.
print("\n--- 2. @retry: Exponential Backoff Retry Decorator ---")

def retry(max_attempts: int = 3, base_delay: float = 0.2):
    """Automatically retries a failing function with exponential delay."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    attempts += 1
                    return func(*args, **kwargs)
                except Exception as exc:
                    if attempts == max_attempts:
                        print(f"❌ [RETRY EXHAUSTED] '{func.__name__}' failed after {max_attempts} attempts: {exc}")
                        raise
                    
                    delay = base_delay * (2 ** (attempts - 1))
                    print(f"⚠️  [ATTEMPT {attempts}/{max_attempts} FAILED] {exc}. Backing off for {delay:.2f}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Simulated flaky LLM API call
call_counter = 0

@retry(max_attempts=3, base_delay=0.1)
def query_llm_inference(prompt: str) -> str:
    global call_counter
    call_counter += 1
    if call_counter < 3:
        raise ConnectionResetError(f"HTTP 503: Model server warming up (mock fail #{call_counter})")
    return f"LLM Response: Analysis complete for prompt -> '{prompt}'"

response = query_llm_inference("Explain CPython compact dictionary architecture")
print(f"✅ Final Success: {response}")


# -----------------------------------------------------------------------------
# 3. ROLE-BASED ACCESS CONTROL (@require_role)
# -----------------------------------------------------------------------------
print("\n--- 3. @require_role: Security & RBAC Decorator ---")

# Simulated Active User Context
CURRENT_USER_SESSION: Dict[str, Any] = {
    "username": "Sapna",
    "role": "engineer",  # Options: 'guest', 'engineer', 'admin'
    "authenticated": True
}

def require_role(allowed_role: str):
    """Enforces authorization boundaries on sensitive backend endpoints."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            user_role = CURRENT_USER_SESSION.get("role")
            if user_role != allowed_role:
                error_msg = f"403 Forbidden: User '{CURRENT_USER_SESSION.get('username')}' with role '{user_role}' cannot access '{func.__name__}'. Required: '{allowed_role}'."
                raise PermissionError(error_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role("engineer")
def view_codebase_metrics() -> str:
    return "Codebase Metrics: 100% Test Coverage, 0 Security Vulnerabilities."

@require_role("admin")
def delete_production_database() -> str:
    return "Database Purged."

# Test 1: Allowed call (Sapna is engineer)
print("Testing Access 1 (Engineer Role):")
print("  --> Result:", view_codebase_metrics())

# Test 2: Forbidden call (Admin role required)
print("\nTesting Access 2 (Admin Role):")
try:
    delete_production_database()
except PermissionError as err:
    print(f"  --> Blocked by Security Decorator: {err}")

print("\n" + "=" * 75)
print("✅ MODULE 03 COMPLETE: Production @timer, @retry & @require_role mastered!")
print("=" * 75)

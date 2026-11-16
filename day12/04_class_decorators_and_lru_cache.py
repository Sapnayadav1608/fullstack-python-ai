# =============================================================================
# DAY 12 - MODULE 04: Class Decorators, Memoization & @functools.lru_cache
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Topics Covered:
# 1. Classes as Decorators: Using the __call__ Dunder Method for Stateful Caching
# 2. Decorating Classes (Class Decorators): Metaprogramming & Auto-Registration
# 3. Custom Memoization from Scratch: Turning O(2^N) Fibonacci into O(N)
# 4. Built-in @functools.lru_cache: Cache Info Inspection, Maxsize & Eviction
# =============================================================================

import sys
import time
import functools
from typing import Callable, Any, Dict

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 75)
print("🚀 DAY 12 - MODULE 04: CLASS DECORATORS, MEMOIZATION & LRU CACHE")
print("=" * 75)


# -----------------------------------------------------------------------------
# 1. CLASSES AS DECORATORS (THE __call__ DUNDER METHOD)
# -----------------------------------------------------------------------------
# In Python, any object that implements the '__call__' method is callable like a function!
# A Class Decorator uses '__init__' to accept the function, and '__call__' as the wrapper.
print("\n--- 1. Class as a Decorator (__call__) ---")

class CallCounter:
    """Tracks invocation count across functions using instance state."""
    def __init__(self, func: Callable):
        self.func = func
        self.calls = 0
        functools.update_wrapper(self, func)  # Preserves metadata on class wrapper
        
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.calls += 1
        print(f"📊 [CALL #{self.calls}] '{self.func.__name__}' called.")
        return self.func(*args, **kwargs)

@CallCounter
def process_ai_job(job_id: str) -> str:
    return f"Job {job_id} completed successfully."

process_ai_job("JOB-101")
process_ai_job("JOB-102")
process_ai_job("JOB-103")
print(f"Total calls tracked on object instance: {process_ai_job.calls} calls ✅")


# -----------------------------------------------------------------------------
# 2. DECORATING CLASSES (CLASS DECORATORS)
# -----------------------------------------------------------------------------
print("\n--- 2. Class Decorators (Decorating a Class Definition) ---")

# A decorator can also accept a CLASS, modify its attributes/methods, and return it!
# This is how @dataclass, @pydantic, and ORMs operate.

AI_MODEL_REGISTRY: Dict[str, Any] = {}

def register_ai_model(model_family: str):
    """Class decorator that auto-registers AI models into a central backend hub."""
    def decorator(cls):
        AI_MODEL_REGISTRY[model_family] = cls
        cls.registered_family = model_family
        return cls
    return decorator

@register_ai_model("vision")
class VisionTransformer:
    def predict(self, img_path: str):
        return f"Detected objects in {img_path}"

@register_ai_model("nlp")
class LanguageModel:
    def generate(self, text: str):
        return f"Generated continuation for '{text}'"

print(f"Central Registry Models : {list(AI_MODEL_REGISTRY.keys())}")
print(f"Vision Transformer Type : {AI_MODEL_REGISTRY['vision']}")


# -----------------------------------------------------------------------------
# 3. MEMOIZATION FROM SCRATCH: O(2^N) -> O(N) SPEEDUP
# -----------------------------------------------------------------------------
print("\n--- 3. Custom Memoization Decorator (Fibonacci Speedup) ---")

def memoize(func: Callable) -> Callable:
    """Caches expensive recursive function outputs in a dictionary."""
    cache: Dict[Any, Any] = {}
    
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        # Args tuple acts as dictionary key
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache  # Expose cache for inspection
    return wrapper

@memoize
def fib_memoized(n: int) -> int:
    if n <= 1:
        return n
    return fib_memoized(n - 1) + fib_memoized(n - 2)

t0 = time.perf_counter()
fib_35 = fib_memoized(35)
t1 = time.perf_counter()

print(f"Fibonacci(35) = {fib_35}")
print(f"Computed in   : {(t1 - t0)*1000:.4f} ms (Instant linear O(N) time!)")
print(f"Cached items  : {len(fib_memoized.cache)} entries in memory dictionary")


# -----------------------------------------------------------------------------
# 4. BUILT-IN @functools.lru_cache (LEAST RECENTLY USED CACHING)
# -----------------------------------------------------------------------------
print("\n--- 4. Python Built-in @functools.lru_cache ---")

# Python includes an ultra-fast C-optimized LRU Cache:
# - maxsize: Max number of items before oldest entries are evicted.
# - typed: If True, fib(3) and fib(3.0) are cached separately.

@functools.lru_cache(maxsize=128)
def fetch_currency_rate(base: str, target: str) -> float:
    print(f"  [API NETWORK CALL] Fetching live rate for {base} -> {target}...")
    # Simulated API latency
    return 83.25 if target == "INR" else 1.08

print("First Call (Cache Miss):")
rate1 = fetch_currency_rate("USD", "INR")
print(f"Rate: {rate1}")

print("\nSecond Call (Cache Hit - Instant zero latency):")
rate2 = fetch_currency_rate("USD", "INR")
print(f"Rate: {rate2}")

# Cache Inspection:
info = fetch_currency_rate.cache_info()
print(f"\nCache Statistics : {info}")
print(f"Hits: {info.hits}, Misses: {info.misses}, Size: {info.currsize}/{info.maxsize}")

print("\n" + "=" * 75)
print("✅ MODULE 04 COMPLETE: Class decorators, memoization & LRU Cache mastered!")
print("=" * 75)

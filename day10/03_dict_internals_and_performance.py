"""
Day 10: Dictionary Internals, O(1) Speed Benchmark & In-Memory TTL Cache System
================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. Under the Hood: How CPython Computes Hash Table Buckets
2. Collision Resolution: Open Addressing & The Perturb Probing Formula
3. Live Benchmark: 1,000,000 Elements Key Lookup (Dict O(1) vs List O(N))
4. Dictionary Comprehensions: Filtering, Transformation & Inversion
5. Real-World Backend System: In-Memory TTL (Time-To-Live) Cache with Expiration
"""

import sys
import time

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 10 - TOPIC 03: DICT INTERNALS, BENCHMARKS & IN-MEMORY TTL CACHE]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. UNDER THE HOOD: HOW CPYTHON MAPS KEYS TO MEMORY BUCKETS
# -------------------------------------------------------------------------
print("\n--- 1. CPython Hash Table Mapping Formula ---")
# To find where a key goes in the internal table:
# Step 1: Calculate hash_code = hash(key)
# Step 2: Calculate bucket_index = hash_code & (table_size - 1)

table_size = 8  # Initial default table size in CPython
mask = table_size - 1

sample_keys = ["user_id", "session_token", "api_key", "timestamp"]
print(f"Table Size: {table_size} | Mask (Bitwise AND): {bin(mask)} ({mask})")
print(f"{'Key':<15} | {'hash(key)':<22} | {'Bucket Index (hash & mask)'}")
print("-" * 60)

for k in sample_keys:
    h = hash(k)
    idx = h & mask
    print(f"{k:<15} | {h:<22} | Bucket [{idx}]")


# -------------------------------------------------------------------------
# 2. COLLISION RESOLUTION: OPEN ADDRESSING WITH PERTURB PROBING
# -------------------------------------------------------------------------
print("\n--- 2. Collision Resolution Strategy ---")
# What if two different keys yield the SAME bucket index? (Hash Collision)
# CPython uses Open Addressing with a special pseudo-random probing formula:
#
#   perturb = hash_code
#   while bucket is occupied by another key:
#       perturb >>= 5
#       probe_idx = (5 * probe_idx + 1 + perturb) & mask
#
# This ensures every slot is explored uniformly without primary clustering!
print("CPython uses Open Addressing with Pseudo-Random Probing:")
print("  probe_next = (5 * probe + 1 + (perturb >> 5)) & mask")
print("  >> Guarantees O(1) average lookup without linked-list memory overhead!")


# -------------------------------------------------------------------------
# 3. LIVE PERFORMANCE BENCHMARK: DICT O(1) VS LIST O(N)
# -------------------------------------------------------------------------
print("\n--- 3. Live Benchmark: 1,000,000 Elements Lookup ---")
N = 1_000_000
missing_key = "non_existent_key_999999"

# Create a dictionary of 1,000,000 items
test_dict = {f"user_{i}": i * 10 for i in range(N)}

# Create a list of tuples containing the exact same data
test_list = [(f"user_{i}", i * 10) for i in range(N)]

# Benchmark Dict Search (O(1) Hash Table Lookup)
t0 = time.perf_counter()
_ = missing_key in test_dict
t_dict = time.perf_counter() - t0

# Benchmark List Search (O(N) Linear Scan)
t0 = time.perf_counter()
_ = any(k == missing_key for k, _ in test_list)
t_list = time.perf_counter() - t0

print(f"Searching for missing key in {N:,} elements:")
print(f"  Dictionary Lookup (O(1)) : {t_dict * 1000:>8.4f} ms")
print(f"  List of Tuples    (O(N)) : {t_list * 1000:>8.4f} ms")
speedup = t_list / max(t_dict, 1e-9)
print(f">> Dictionaries are ~{speedup:,.0f}x FASTER than linear lists!")


# -------------------------------------------------------------------------
# 4. DICTIONARY COMPREHENSIONS: DATA FILTERING & INVERSION
# -------------------------------------------------------------------------
print("\n--- 4. Dictionary Comprehensions ---")
# Syntax: {key_expr: val_expr for item in iterable if condition}

raw_salaries = {
    "Alice": 95000,
    "Bob": 45000,
    "Charlie": 120000,
    "David": 60000,
    "Eva": 140000
}

# 1. Filtering: High-earners (> 80k) with 10% bonus
high_earners = {name: int(salary * 1.10) for name, salary in raw_salaries.items() if salary > 80000}
print(f"High Earners (>80k + 10% bonus):\n  {high_earners}")

# 2. Dictionary Inversion: Swap Keys and Values (Values must be hashable & unique!)
country_codes = {"US": 1, "IN": 91, "UK": 44, "JP": 81}
inverted_codes = {code: country for country, code in country_codes.items()}
print(f"Original Codes : {country_codes}")
print(f"Inverted Codes : {inverted_codes}")


# -------------------------------------------------------------------------
# 5. REAL-WORLD SYSTEM: IN-MEMORY TTL CACHE (TIME-TO-LIVE)
# -------------------------------------------------------------------------
print("\n--- 5. Real-World Backend: In-Memory TTL Cache ---")

class SimpleTTLCache:
    """Production-style in-memory key-value cache with timestamp expiration."""
    def __init__(self):
        self._store = {}  # {key: (value, expiry_timestamp)}

    def set(self, key: str, value: any, ttl_seconds: float):
        """Sets a key with a time-to-live expiration."""
        expiry = time.time() + ttl_seconds
        self._store[key] = (value, expiry)

    def get(self, key: str, default=None):
        """Returns the value if not expired, else purges key and returns default."""
        if key not in self._store:
            return default
            
        value, expiry = self._store[key]
        if time.time() > expiry:
            del self._store[key]  # Expired -> Purge from memory
            return default
            
        return value

    def active_keys(self) -> list:
        now = time.time()
        return [k for k, (_, exp) in self._store.items() if exp > now]


# Demo the TTL Cache
cache = SimpleTTLCache()
cache.set("session_token_101", {"user": "Alice", "role": "admin"}, ttl_seconds=0.5)
cache.set("api_rate_limit_ip", 45, ttl_seconds=2.0)

print(f"Immediate Read  : {cache.get('session_token_101')}")
print(f"Active Keys     : {cache.active_keys()}")

print("Simulating sleep of 0.6 seconds...")
time.sleep(0.6)

print(f"After TTL Expiry: {cache.get('session_token_101')} (Successfully expired & purged!)")
print(f"Still Active    : {cache.active_keys()}")

print("\n[SUMMARY] Hash tables give dictionaries instant O(1) lookups and power backend caches!")

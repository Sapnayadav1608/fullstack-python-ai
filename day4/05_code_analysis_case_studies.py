# =============================================================================
# DAY 04 - TOPIC 05: Code Analysis Case Studies (Optimizing O(N^2) to O(N))
# =============================================================================
# Real interview optimization patterns: Bad Code vs Production Code.
# =============================================================================

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 04 - TOPIC 05] Code Optimization: O(N^2) -> O(N)")
print("=" * 60)

# -----------------------------------------------------------------------------
# CASE STUDY: Two Sum Problem (LeetCode #1)
# Do numbers dhoondho jinka sum 'target' ke barabar ho.
# -----------------------------------------------------------------------------

# APPROACH 1: Brute Force (Nested Loops)
# Time Complexity: O(N^2) | Space Complexity: O(1)
def two_sum_brute_force(nums: list, target: int):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# APPROACH 2: Hash Map (Dictionary Lookup)
# Time Complexity: O(N) | Space Complexity: O(N)
def two_sum_hash_map(nums: list, target: int):
    seen = {}  # number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:  # O(1) average lookup!
            return [seen[complement], i]
        seen[num] = i
    return []

# Live Comparison on N = 10,000 items:
test_nums = list(range(1, 10_001))
target_val = 19_999  # Aakhiri do numbers ka sum

print("Testing Two Sum on 10,000 numbers:\n")

# Benchmark Brute Force O(N^2)
t0 = time.perf_counter()
res_bf = two_sum_brute_force(test_nums, target_val)
t1 = time.perf_counter()
time_bf = t1 - t0

# Benchmark Hash Map O(N)
t2 = time.perf_counter()
res_hm = two_sum_hash_map(test_nums, target_val)
t3 = time.perf_counter()
time_hm = t3 - t2

print(f"Brute Force O(N^2) Time : {time_bf:.6f} seconds | Result: {res_bf}")
print(f"Hash Map O(N) Time    : {time_hm:.6f} seconds | Result: {res_hm}")
speedup = int(time_bf / max(time_hm, 1e-9))
print(f"\n>> Hash Map approach is {speedup}x FASTER on 10,000 items!")
print(">> On 10 Lakh items, O(N^2) would take hours, while O(N) takes ~0.05 seconds!")

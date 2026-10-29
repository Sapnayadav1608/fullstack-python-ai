# =============================================================================
# DAY 04 - TOPIC 03: The 4 Golden Rules for Calculating Big O
# =============================================================================
# Kisi bhi complex code ko dekh kar uska exact Big O kaise nikaalein?
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 04 - TOPIC 03] The 4 Golden Rules for Calculating Big O")
print("=" * 60)

# -----------------------------------------------------------------------------
# RULE 1: Drop the Constants! (Constants ko ignore karein)
# O(2N) -> O(N) | O(500) -> O(1) | O(N/2) -> O(N)
# -----------------------------------------------------------------------------
# Reason: Asymptotic analysis mein jab N 10 Lakh ya 1 Crore hota hai,
# tab 2x ya 3x se order of growth change nahi hota.

def rule_1_demo(items: list):
    # Loop 1: Find min (N operations)
    min_val = min(items)
    
    # Loop 2: Find max (N operations)
    max_val = max(items)
    
    # Total = N + N = 2N operations
    # Big O = O(N) (2 is dropped!)
    return min_val, max_val

print("Rule 1: O(2N) becomes O(N). Constant multipliers don't matter at infinity.")


# -----------------------------------------------------------------------------
# RULE 2: Drop the Non-Dominant Terms! (Chhote terms ko neglect karein)
# O(N^2 + N) -> O(N^2)
# O(N + log N) -> O(N)
# O(2^N + N^100) -> O(2^N)
# -----------------------------------------------------------------------------
# Example: Agar N = 10,000 hai:
# N^2 = 100,000,000 (10 Crore)
# N   = 10,000      (10 Hazaar)
# 10 Crore ke saamne 10 Hazaar negligible hai! Isliye chhote term ko drop karte hain.

def rule_2_demo(items: list):
    # Part 1: Nested loop -> O(N^2)
    for i in items:
        for j in items:
            pass
            
    # Part 2: Single loop -> O(N)
    for k in items:
        pass
        
    # Total = O(N^2 + N) -> Final Big O = O(N^2)

print("\nRule 2: Drop non-dominant terms. O(N^2 + N + 100) -> O(N^2)")


# -----------------------------------------------------------------------------
# RULE 3: Add vs Multiply (Sequential vs Nested)
# -----------------------------------------------------------------------------
# Case A: Sequential Steps -> ADD (+): O(A + B)
# Case B: Nested Steps     -> MULTIPLY (*): O(A * B)

def rule_3_demo(list_a: list, list_b: list):
    # Sequential: Loop through A, THEN loop through B
    # Complexity: O(len(A) + len(B))
    for x in list_a:
        pass
    for y in list_b:
        pass
        
    # Nested: For every item in A, loop through B
    # Complexity: O(len(A) * len(B))
    for x in list_a:
        for y in list_b:
            pass

print("\nRule 3: Sequential operations add -> O(A + B). Nested operations multiply -> O(A * B)")


# -----------------------------------------------------------------------------
# RULE 4: Different Inputs -> Different Variables!
# -----------------------------------------------------------------------------
# Interview Trap: Don't call everything 'N'!
# Agar function do alag lists le raha hai (list_a aur list_b):
# Nested loop ka complexity O(N^2) NAHI hoga, balki O(A * B) hoga!
# Kyunki list_a mein 5 items ho sakte hain aur list_b mein 10 lakh items!

def compare_two_lists(users: list, banned_ids: set):
    # users = U, banned_ids = B
    # Dict/Set lookup is O(1)
    # Total complexity: O(U * 1) = O(U)
    active_users = [u for u in users if u not in banned_ids]
    return active_users

print("\nRule 4: Use distinct variables for different inputs: O(A * B), not O(N^2)")

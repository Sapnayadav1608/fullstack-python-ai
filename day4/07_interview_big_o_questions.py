# =============================================================================
# DAY 04 - TOPIC 07: Tricky Big O Interview Questions
# =============================================================================
# Interviewers ke sabse favorite tricky code snippets jahan 90% candidates
# Big O galat calculate karte hain!
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 04 - TOPIC 07] Tricky Big O Interview Code Snippets")
print("=" * 60)

# -----------------------------------------------------------------------------
# TRICK 1: Loop where counter DOUBLES (i *= 2)
# -----------------------------------------------------------------------------
# Dekhne mein lagta hai O(N), lekin असल mein O(log N) hai!
# Kyunki i ki values: 1, 2, 4, 8, 16, 32... 2^k = N -> k = log2(N)
def trick_1(n: int):
    i = 1
    count = 0
    while i < n:
        count += 1
        i = i * 2
    return count

print("Trick 1 (i *= 2): Time Complexity is O(log N), NOT O(N)!")
print(f"N = 1,000,000 -> Total loop runs only {trick_1(1_000_000)} times!")


# -----------------------------------------------------------------------------
# TRICK 2: Triangle Nested Loop (j starts from i)
# -----------------------------------------------------------------------------
# i=0: N runs
# i=1: N-1 runs
# i=2: N-2 runs ...
# Total = N + (N-1) + (N-2) ... + 1 = N*(N+1)/2 = (N^2 + N)/2
# Dropping constants and non-dominant terms -> O(N^2)!
def trick_2(n: int):
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count

print("\nTrick 2 (Inner loop j starts from i): Time Complexity is STILL O(N^2)!")


# -----------------------------------------------------------------------------
# TRICK 3: String Concatenation Inside Loop (Python Trap!)
# -----------------------------------------------------------------------------
# Kyunki strings IMMUTABLE hoti hain, jab aap s += ch karte hain:
# Python har baar purani string ko naye memory mein copy karta hai:
# Step 1: 1 char copy
# Step 2: 2 chars copy
# Step 3: 3 chars copy ...
# Total = 1 + 2 + 3 + ... + N = O(N^2) Time! ❌
#
# SOLUTION: "".join(list_of_chars) -> O(N) Time! ✔️
print("\nTrick 3 (String '+=' inside loop):")
print("s += char inside loop takes O(N^2) time due to immutability!")
print("Always use ''.join(list) which runs in O(N) time!")


# -----------------------------------------------------------------------------
# TRICK 4: 'item in list' inside a loop
# -----------------------------------------------------------------------------
# if x in my_list:   -> O(N) linear search inside loop -> O(N * N) = O(N^2)
# if x in my_set:    -> O(1) hash lookup inside loop  -> O(N * 1) = O(N)
print("\nTrick 4 ('in' check inside loop):")
print("- 'item in list' inside for-loop: O(N^2)")
print("- 'item in set' inside for-loop : O(N)")

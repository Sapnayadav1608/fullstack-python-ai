# =============================================================================
# DAY 04 - TOPIC 01: Why Big O? Fundamentals of Algorithm Analysis
# =============================================================================
# Algorithm ki efficiency ko seconds mein kyu nahi naapte?
# Big O Notation ka real purpose kya hai?
# =============================================================================

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 04 - TOPIC 01] Why Big O? Algorithm Analysis Fundamentals")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. Problem with Measuring Time in Seconds:
# -----------------------------------------------------------------------------
# Agar hum stopwatch / time.time() use karein toh:
# - Wo aapke laptop ke hardware par depend karega (i3 vs i9 vs M3 chip)
# - Background mein chal rahe apps (Chrome, Spotify) speed badal denge
# - Programming language ka overhead time badal dega
#
# SOLUTION: "Count the number of basic operations as input size (N) grows!"
# Isi ko Asymptotic Analysis / Big O kehte hain.

# Demo: Sum of First N Numbers in 2 Different Ways:

# Approach A: Loop Approach (N operations -> O(n))
def sum_using_loop(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Approach B: Math Formula Approach (1 operation -> O(1))
def sum_using_formula(n: int) -> int:
    return n * (n + 1) // 2

N = 10_000_000

# Benchmark Approach A
start_a = time.perf_counter()
res_a = sum_using_loop(N)
end_a = time.perf_counter()
time_a = end_a - start_a

# Benchmark Approach B
start_b = time.perf_counter()
res_b = sum_using_formula(N)
end_b = time.perf_counter()
time_b = end_b - start_b

print(f"Calculating sum of first {N:,} numbers:\n")
print(f"Approach A (Loop / O(n))    : {time_a:.6f} seconds | Result: {res_a}")
print(f"Approach B (Formula / O(1)) : {time_b:.6f} seconds | Result: {res_b}")
print(f"\n>> Formula approach is approximately {int(time_a / max(time_b, 1e-9)):,}x faster!")

# -----------------------------------------------------------------------------
# 2. Asymptotic Notations:
# -----------------------------------------------------------------------------
# Big O (O)     : WORST CASE (Upper Bound) - Code isse bura perform nahi karega. (Industry Standard)
# Big Omega (Ω) : BEST CASE (Lower Bound)  - Code isse fast nahi chal sakta.
# Big Theta (Θ) : AVERAGE / TIGHT BOUND   - Average input par kaisa chalega.

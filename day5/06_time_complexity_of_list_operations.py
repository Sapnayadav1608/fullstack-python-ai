# =============================================================================
# DAY 05 - TOPIC 06: Time Complexity (Big O) of List Operations
# =============================================================================
# Connecting Day 4 (Big O) with Day 5 (Lists)!
# =============================================================================

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 05 - TOPIC 06] Big O Complexity of List Operations")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. Master Complexity Cheat Sheet for Python Lists:
# -----------------------------------------------------------------------------
# Operation                 | Big O Time   | Why?
# -----------------------------------------------------------------------------
# Index Access: my_list[i]  | O(1)         | Direct memory offset formula
# Length: len(my_list)      | O(1)         | CPython stores 'ob_size' in header
# Append: .append(x)        | O(1) amortized | Adds to end, over-allocated array
# Pop from end: .pop()      | O(1)         | Removes last item, no shifts needed
# Pop from front: .pop(0)   | O(N)         | Shifts remaining N-1 items left!
# Insert at front: .insert(0, x)| O(N)     | Shifts all N items right!
# Search: 'x in my_list'    | O(N)         | Checks items sequentially from start
# Delete: .remove(x)        | O(N)         | First searches O(N), then shifts O(N)
# Slicing: my_list[a:b]     | O(k)         | k = slice length (copies references)
# Sorting: .sort()          | O(N log N)   | Timsort algorithm
# Reverse: .reverse()       | O(N)         | Swaps elements in-place

print(f"{'Operation':<26} | {'Time Complexity':<16} | {'Reason'}")
print("-" * 65)
print(f"{'Index access (L[i])':<26} | {'O(1)':<16} | {'Instant memory pointer offset'}")
print(f"{'len(L)':<26} | {'O(1)':<16} | {'Stored in CPython header struct'}")
print(f"{'append(x)':<26} | {'O(1) amortized':<16} | {'Adds to tail of dynamic array'}")
print(f"{'pop() (end)':<26} | {'O(1)':<16} | {'No element shifting needed'}")
print(f"{'insert(0, x)':<26} | {'O(N) SLOW':<16} | {'Must shift all N elements right'}")
print(f"{'pop(0) (front)':<26} | {'O(N) SLOW':<16} | {'Must shift all N elements left'}")
print(f"{'x in list':<26} | {'O(N)':<16} | {'Linear search across elements'}")
print(f"{'sort()':<26} | {'O(N log N)':<16} | {'Timsort adaptive algorithm'}")


# -----------------------------------------------------------------------------
# 2. Live Speed Benchmark: append() vs insert(0)
# -----------------------------------------------------------------------------
N = 50_000

# Benchmark append() O(1)
t0 = time.perf_counter()
list_append = []
for i in range(N):
    list_append.append(i)
time_append = time.perf_counter() - t0

# Benchmark insert(0) O(N)
t0 = time.perf_counter()
list_insert = []
for i in range(N):
    list_insert.insert(0, i)  # Shifts everything on every single iteration!
time_insert = time.perf_counter() - t0

print(f"\n--- Live Benchmark on {N:,} operations ---")
print(f"append()  [O(1) amortized] : {time_append:.5f} seconds")
print(f"insert(0) [O(N) shifts]    : {time_insert:.5f} seconds")
print(f">> append() is {int(time_insert / max(time_append, 1e-9)):,}x FASTER than insert(0)!")
print(">> Tip: If you frequently insert/pop from the front, use 'collections.deque'!")

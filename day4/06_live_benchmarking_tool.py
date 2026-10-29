# =============================================================================
# DAY 04 - TOPIC 06: Live Big O Performance Benchmarking Tool
# =============================================================================
# Python mein N badhne par alag-alag complexities ka behavior live test karein.
# =============================================================================

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 04 - TOPIC 06] Live Big O Performance Benchmarker")
print("=" * 60)

def benchmark_complexities():
    input_sizes = [100, 1000, 5000]
    
    print(f"\n{'N (Size)':<10} | {'O(1)':<12} | {'O(log N)':<12} | {'O(N)':<12} | {'O(N log N)':<12} | {'O(N^2)':<12}")
    print("-" * 75)
    
    for n in input_sizes:
        data = list(range(n))
        target = n - 1
        
        # 1. O(1) - Index access
        t0 = time.perf_counter()
        _ = data[n // 2]
        t_o1 = time.perf_counter() - t0
        
        # 2. O(log N) - Binary Search
        t0 = time.perf_counter()
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] == target:
                break
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        t_ologn = time.perf_counter() - t0
        
        # 3. O(N) - Linear Loop
        t0 = time.perf_counter()
        _ = sum(data)
        t_on = time.perf_counter() - t0
        
        # 4. O(N log N) - Built-in sort
        unshuffled = list(range(n, 0, -1))
        t0 = time.perf_counter()
        _ = sorted(unshuffled)
        t_onlogn = time.perf_counter() - t0
        
        # 5. O(N^2) - Nested Loop
        t0 = time.perf_counter()
        count = 0
        for i in range(min(n, 3000)):
            for j in range(min(n, 3000)):
                count += 1
        t_on2 = time.perf_counter() - t0
        
        print(f"{n:<10} | {t_o1*1000:8.4f} ms | {t_ologn*1000:8.4f} ms | {t_on*1000:8.4f} ms | {t_onlogn*1000:8.4f} ms | {t_on2*1000:8.4f} ms")

benchmark_complexities()

print("\n" + "=" * 60)
print("Key Observation:")
print("- O(1) and O(log N) remain essentially instant even as N explodes.")
print("- O(N^2) time grows quadratically (10x input = 100x time!).")
print("=" * 60)

# =============================================================================
# DAY 05 - TOPIC 01: Python List Memory Architecture (CampusX Deep Dive)
# =============================================================================
# Python Lists dynamic referential arrays hoti hain.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 05 - TOPIC 01] List Memory Architecture & Dynamic Resizing")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. Referential Arrays Concept (Interview Gold!)
# -----------------------------------------------------------------------------
# C/C++ Arrays: Direct continuous values memory mein store hoti hain.
# Python Lists: "Referential Arrays" hoti hain.
# Matlab List ke andar actual values (1, 2, "hello") store NAHI hoti,
# balki unke MEMORY ADDRESSES (pointers) store hote hain!
#
# Yahi wajah hai ki Python list HETEROGENEOUS ho sakti hai (int, float, str mix):

mixed_list = [100, "Python", 3.14, True]

print("Elements and their individual memory addresses:")
for item in mixed_list:
    print(f"  Item: {repr(item):<10} | Type: {type(item).__name__:<6} | Address: {id(item)}")


# -----------------------------------------------------------------------------
# 2. Mutability Proof (In-Place Memory Modification)
# -----------------------------------------------------------------------------
# Strings immutable hoti hain, par Lists MUTABLE hoti hain!
# List modify hone par uska memory address change NAHI hota.

nums = [10, 20, 30]
print(f"\nOriginal List: {nums} | Address: {id(nums)}")

nums.append(40)
print(f"After append : {nums} | Address: {id(nums)} (Address remains SAME!)")


# -----------------------------------------------------------------------------
# 3. Dynamic Array & Over-Allocation (Memory Resizing)
# -----------------------------------------------------------------------------
# Jab list full ho jaati hai, Python CPython engine background mein
# purani memory se lagbhag DOUBLE size ki nayi memory allocate karta hai
# aur items ko copy karta hai. Isi wajah se append() amortized O(1) hota hai!

growth_list = []
print("\n--- CPython Dynamic Resizing Demo (Bytes allocated in RAM) ---")
prev_size = sys.getsizeof(growth_list)
print(f"Empty list size: {prev_size} bytes")

for i in range(20):
    growth_list.append(i)
    current_size = sys.getsizeof(growth_list)
    if current_size != prev_size:
        print(f"  Item count: {len(growth_list):<2} -> Memory Jumped to: {current_size} bytes (CPython resized memory!)")
        prev_size = current_size

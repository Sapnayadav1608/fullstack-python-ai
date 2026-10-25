# =============================================================================
# DAY 1 - TOPIC 11: for Loop & range() Function
# =============================================================================
# for loop sequence (jaise range, list, string) ke har item par bari-bari ghumta hai.
# =============================================================================

# 1. range(start, stop, step)
# NOTE: 'stop' number kabhi include nahi hota!

print("--- range(5) : 0 se 4 tak ---")
for i in range(5):
    print(i, end=" ")
print()

print("\n--- range(2, 7) : 2 se 6 tak ---")
for i in range(2, 7):
    print(i, end=" ")
print()

print("\n--- range(1, 10, 2) : 2-2 ke gap se (Odd numbers) ---")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# 2. String ke har letter par loop chalana
print("\n--- Loop over a String ---")
word = "PYTHON"
for letter in word:
    print(letter, end="-")
print()

# 3. Sum of First 10 Numbers (Simple Practical logic)
total_sum = 0
for num in range(1, 11):
    total_sum += num
print(f"\n1 se 10 tak ke numbers ka sum: {total_sum}")

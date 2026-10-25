# =============================================================================
# DAY 1 - TOPIC 10: Loops (while Loop, break, continue)
# =============================================================================
# while loop tab tak chalta rehta hai jab tak uski condition True rehti hai.
# =============================================================================

# 1. Basic while loop (Counting from 1 to 5)
print("--- Basic while loop ---")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # count = count + 1 (Increment karna zaroori hai, warna infinite loop ban jayega!)

# 2. 'break' statement (Loop ko beech mein hi rok dena)
print("\n--- break statement demo ---")
num = 1
while num <= 10:
    if num == 4:
        print("Breaking loop at num =", num)
        break
    print("Num:", num)
    num += 1

# 3. 'continue' statement (Current iteration ko skip karke agley round par chale jaana)
print("\n--- continue statement demo (Sirf Odd Numbers print honge) ---")
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:  # Agar number even hai toh skip karo
        continue
    print("Odd number:", i)

# =============================================================================
# DAY 1 - TOPIC 07: Strings Indexing & Slicing
# =============================================================================
# String ke har character ka ek index number hota hai (0 se start hota hai).
# Slicing se hum string ka ek tukda (sub-string) nikaal sakte hain.
# =============================================================================

language = "PYTHON"
#  P   Y   T   H   O   N
#  0   1   2   3   4   5  (Positive Indexing - Left to Right)
# -6  -5  -4  -3  -2  -1  (Negative Indexing - Right to Left)

# 1. Indexing (Single letter nikaalna)
print("First letter [0]   :", language[0])   # 'P'
print("Third letter [2]   :", language[2])   # 'T'
print("Last letter [-1]   :", language[-1])  # 'N'

# 2. String Length
print("Total length       :", len(language)) # 6

# 3. Slicing Syntax: string[start : stop : step]
# NOTE: 'stop' index include nahi hota (stop - 1 tak chalta hai)

course = "Learn Python Programming"

print("\n--- Slicing Examples ---")
print("course[0:5]    ->", course[0:5])     # 'Learn'
print("course[6:12]   ->", course[6:12])    # 'Python'
print("course[:5]     ->", course[:5])      # Shuru se lekar index 4 tak
print("course[13:]    ->", course[13:])     # Index 13 se lekar end tak

# Step Slicing
print("course[::2]    ->", course[::2])     # Ek-ek chhod kar

# Reverse a string (Sabse famous trick):
print("Reverse [::-1] ->", course[::-1])

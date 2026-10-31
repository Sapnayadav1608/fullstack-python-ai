# =============================================================================
# DAY 06 - TOPIC 03: Nested Lists & The Multiplication Bug Trap
# =============================================================================
# 2D Grids, Matrices, Indexing, and the Famous Reference Multiplication Trap.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 06 - TOPIC 03] Nested Lists & The Multiplication Bug Trap")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. 2D List (Matrix) Indexing
# -----------------------------------------------------------------------------
# matrix[row_index][column_index]
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "O", "X"]
]

print("Top-Left [0][0]     :", board[0][0])  # 'X'
print("Center [1][1]       :", board[1][1])  # 'X'
print("Bottom-Right [2][2] :", board[2][2])  # 'X'


# -----------------------------------------------------------------------------
# 2. THE INFAMOUS MULTIPLICATION BUG TRAP! (Asked in 9/10 Python Interviews)
# -----------------------------------------------------------------------------
# Problem: Humein ek 3x3 grid banani hai zeroes se filled.

# ❌ WRONG WAY (The Bug!):
buggy_grid = [[0] * 3] * 3

print("\n--- The Multiplication Trap ---")
print("Initial buggy grid:", buggy_grid)

# Ab sirf Row 0, Col 0 ko 1 karte hain:
buggy_grid[0][0] = 1

print("After buggy_grid[0][0] = 1:")
print(buggy_grid)
# WHAT?! [[1, 0, 0], [1, 0, 0], [1, 0, 0]] -> Saari rows ka pehla element 1 ho gaya!

# WHY DID THIS HAPPEN? (Memory Architecture):
# [[0] * 3] * 3 ne inner list ko 3 baar copy NAHI kiya,
# balki USI EK INNER LIST KE MEMORY ADDRESS ko 3 baar repeat kar diya!
print("\nProof (Memory addresses of each row in buggy_grid):")
for idx, r in enumerate(buggy_grid):
    print(f"  Row {idx} Address: {id(r)} (Same address!)")


# ✔️ THE RIGHT WAY (Using List Comprehension):
# Har iteration par ek nayi, independent inner list create hoti hai!
correct_grid = [[0] * 3 for _ in range(3)]

correct_grid[0][0] = 1
print("\n--- The Correct Comprehension Fix ---")
print("After correct_grid[0][0] = 1:")
for r in correct_grid:
    print(" ", r)

print("Proof (Memory addresses of each row in correct_grid):")
for idx, r in enumerate(correct_grid):
    print(f"  Row {idx} Address: {id(r)} (Unique address!)")


# -----------------------------------------------------------------------------
# 3. Matrix Traversal: Primary & Secondary Diagonals
# -----------------------------------------------------------------------------
sq_matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Primary Diagonal: elements where row == col -> [0][0], [1][1], [2][2]
n = len(sq_matrix)
primary_diag = [sq_matrix[i][i] for i in range(n)]

# Secondary Diagonal: elements where row + col == n - 1 -> [0][2], [1][1], [2][0]
secondary_diag = [sq_matrix[i][n - 1 - i] for i in range(n)]

print("\nSquare Matrix 3x3:")
for r in sq_matrix:
    print(" ", r)
print("Primary Diagonal   [10, 50, 90] :", primary_diag)
print("Secondary Diagonal [30, 50, 70] :", secondary_diag)

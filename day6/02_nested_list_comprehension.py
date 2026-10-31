# =============================================================================
# DAY 06 - TOPIC 02: Nested List Comprehensions
# =============================================================================
# Double loops, Cartesian products, and Matrix Transpositions.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 06 - TOPIC 02] Nested List Comprehensions")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. Double Loops inside List Comprehension
# -----------------------------------------------------------------------------
# Golden Rule: Comprehension mein loops ka order wahi rehta hai jo normal nested loops mein hota hai!

colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]

# Traditional nested loop:
pairs_loop = []
for c in colors:
    for s in sizes:
        pairs_loop.append((c, s))

# Nested comprehension:
pairs_comp = [(c, s) for c in colors for s in sizes]
print("Cartesian Product Pairs:\n", pairs_comp)


# -----------------------------------------------------------------------------
# 2. Flattening a 2D Matrix (2D to 1D)
# -----------------------------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# [element for row in matrix for element in row]
# Pehle outer loop: 'for row in matrix'
# Phir inner loop:  'for element in row'
flattened = [element for row in matrix for element in row]
print("\nOriginal 2D Matrix :", matrix)
print("Flattened 1D List  :", flattened)


# -----------------------------------------------------------------------------
# 3. Matrix Transposition (Rows become Columns)
# -----------------------------------------------------------------------------
# Given Matrix (3 rows x 2 cols):
grid = [
    [1, 2],
    [3, 4],
    [5, 6]
]
# Transposed should be (2 rows x 3 cols):
# [[1, 3, 5], [2, 4, 6]]

cols_count = len(grid[0])
transposed = [[row[i] for row in grid] for i in range(cols_count)]

print("\nOriginal Grid (3x2):", grid)
print("Transposed Grid (2x3):", transposed)


# -----------------------------------------------------------------------------
# 4. Nested Comprehension with Conditions
# -----------------------------------------------------------------------------
# Generate all coordinate pairs (x, y) where x != y:
coords = [(x, y) for x in range(3) for y in range(3) if x != y]
print("\nCoords where x != y:", coords)

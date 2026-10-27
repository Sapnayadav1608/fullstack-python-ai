# =============================================================================
# DAY 02 - TOPIC 09: Modern f-strings & Formatting Mastery
# =============================================================================
# Python 3.6+ mein f-strings string formatting ka sabse powerful aur fast tareeqa hai.
# =============================================================================

import sys
import math

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 09] f-strings & Formatting Mastery")
print("=" * 60)

# 1. Expressions inside f-strings
name = "sapna"
items_count = 5
unit_price = 149.99

print(f"User: {name.capitalize()} | Total: Rs {items_count * unit_price}")

# 2. Decimal Precision (Floating point round off)
pi = math.pi  # 3.141592653589793
print(f"\nPi full       : {pi}")
print(f"Pi (2 places) : {pi:.2f}")
print(f"Pi (4 places) : {pi:.4f}")

# 3. Thousands Separators (Large numbers reading)
annual_revenue = 1450000000
print(f"\nRevenue (Commas)     : Rs {annual_revenue:,}")
print(f"Revenue (Underscores): Rs {annual_revenue:_}")

# 4. Percentage Formatting (.1% ya .2%)
accuracy_score = 0.9458
print(f"\nModel Accuracy       : {accuracy_score:.2%}")   # 94.58%

# 5. Padding & Alignment (< left, > right, ^ center)
header = "REPORT"
print("\n--- Alignment & Padding Demo ---")
print(f"{header:-^35}")   # Centered in 35 characters with '-' filler
print(f"{'Product':<15} | {'Quantity':^8} | {'Price':>10}")
print("-" * 39)
print(f"{'Laptop':<15} | {'2':^8} | {'Rs 65,000':>10}")
print(f"{'Mechanical Key':<15} | {'5':^8} | {'Rs 3,200':>10}")
print(f"{'Type-C Cable':<15} | {'12':^8} | {'Rs 450':>10}")
print("-" * 39)

# 6. Zero Padding (Numbers formatting, jaise roll numbers / IDs)
user_id = 42
print(f"\nZero Padded ID (5 digits): {user_id:05d}")  # 00042

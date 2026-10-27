# =============================================================================
# DAY 1 - MINI PROJECT: Smart Restaurant Bill & Tip Splitter
# =============================================================================
# Yeh project aaj ke saare concepts ko jodta hai:
# - Variables & Data Types
# - Arithmetic Operators (+, *, /)
# - Type Casting (float, int)
# - Conditionals (if-elif-else)
# - Formatted f-strings
# =============================================================================

print("=" * 55)
print("     SMART RESTAURANT BILL & TIP SPLITTER (DAY 1)")
print("=" * 55)

# 1. Inputs (Sample values for automated execution, can also use input())
total_bill = float(input("Enter the total bill amount in Rs: "))        # Total bill amount in Rs
people_count = int(input("Enter the number of people: "))         # Kitne log split kar rahe hain
service_rating = input("Enter the service rating (excellent, good, average, poor): ").lower()    # Service rating: excellent, good, average, poor

# 2. Tip Percentage Calculation using if-elif-else
if service_rating == "excellent":
    tip_percent = 15  # 15% tip.
elif service_rating == "good":
    tip_percent = 10  # 10% tip
elif service_rating == "average":
    tip_percent = 5   # 5% tip
else:
    tip_percent = 0   # No tip for poor service

# 3. Calculations
tip_amount = total_bill * (tip_percent / 100)
grand_total = total_bill + tip_amount
amount_per_person = grand_total / people_count

# 4. Clean Receipt Output using f-strings
print("\n" + "-" * 40)
print("             PAYMENT SUMMARY")
print("-" * 40)
print(f"Original Bill Amount   : Rs {total_bill:.2f}")
print(f"Service Rating         : {service_rating.capitalize()} ({tip_percent}% Tip)")
print(f"Tip Amount             : Rs {tip_amount:.2f}")
print(f"Grand Total (Bill+Tip) : Rs {grand_total:.2f}")
print("-" * 40)
print(f"Total People           : {people_count}")
print(f"Each Person Pays       : Rs {amount_per_person:.2f}")
print("-" * 40)
print("Thank you for dining with us! Have a great day!")

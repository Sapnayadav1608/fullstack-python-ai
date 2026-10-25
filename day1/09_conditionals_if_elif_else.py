# =============================================================================
# DAY 1 - TOPIC 09: Conditionals (if, elif, else)
# =============================================================================
# Program ko decisions lene ke liye if-elif-else ka use kiya jaata hai.
# NOTE: Python mein Indentation (4 spaces ya 1 Tab) bohot zaroori hota hai!
# =============================================================================

# 1. Simple if-elif-else: Grading System
marks = 82

print("Marks:", marks)

if marks >= 90:
    print("Grade: A+ (Outstanding!)")
elif marks >= 80:
    print("Grade: A (Very Good!)")
elif marks >= 60:
    print("Grade: B (Good)")
elif marks >= 35:
    print("Grade: C (Pass)")
else:
    print("Grade: F (Fail - Try again!)")

# 2. Nested if (if ke andar doosra if)
age = 20
has_voter_card = True

print("\n--- Voter Check ---")
if age >= 18:
    if has_voter_card:
        print("Aap vote daal sakte hain!")
    else:
        print("Aapki age toh hai par Voter Card banana padega.")
else:
    print("Aap abhi 18 saal se chhote hain.")

# 3. Short-hand (Ternary Operator) - Ek line mein if-else likhna
balance = 150
status = "Sufficient" if balance >= 100 else "Low Balance"
print("\nBalance Status:", status)

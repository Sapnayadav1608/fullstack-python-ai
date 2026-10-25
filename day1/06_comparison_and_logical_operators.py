# =============================================================================
# DAY 1 - TOPIC 06: Comparison & Logical Operators
# =============================================================================
# Comparison operators check karte hain (Answer humesha True ya False hota hai).
# Logical operators multiple conditions ko jodne ke kaam aate hain.
# =============================================================================

# 1. Comparison Operators (==, !=, >, <, >=, <=)
x = 10
y = 20

print("x == y :", x == y)   # False (Barabar hai?)
print("x != y :", x != y)   # True  (Barabar nahi hai?)
print("x < y  :", x < y)    # True  (x chhota hai y se?)
print("x > y  :", x > y)    # False (x bada hai y se?)
print("x <= 10:", x <= 10)  # True  (x chhota ya barabar hai 10 ke?)

# 2. Logical Operators (and, or, not)

age = 22
has_id = True

# 'and' -> Dono conditions True honi chahiye
can_vote = (age >= 18) and has_id
print("\nCan vote (and demo):", can_vote)  # True

# 'or' -> Dono mein se koi EK bhi condition True ho toh kaam chal jayega
is_sunday = False
is_holiday = True
can_sleep_late = is_sunday or is_holiday
print("Can sleep late (or demo):", can_sleep_late)  # True

# 'not' -> Jo result hai uska ulta kar deta hai (True ko False, False ko True)
is_raining = False
print("Should take umbrella (not demo):", not is_raining)  # True

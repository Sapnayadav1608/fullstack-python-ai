# =============================================================================
# DAY 1 - TOPIC 04: Taking User Input with input()
# =============================================================================
# input() function terminal se user se type karwa kar data leta hai.
# IMPORTANT NOTE: input() humesha STRING return karta hai!
# =============================================================================

# 1. Basic Input
# Uncomment karke terminal mein run kar sakte hain:
# user_name = input("Apna naam enter karein: ")
# print("Namaste,", user_name)

# 2. Number Input lete waqt sabse badi galti:
# num1 = input("First number: ")  # agar user 5 dega toh wo "5" (string) banega
# num2 = input("Second number: ") # agar user 10 dega toh wo "10" banega
# print(num1 + num2)               # Output "510" aayega, 15 nahi!

# 3. Sahi Tareeqa: Input lete hi Type Cast karein (int() ya float())
# Example demo without stopping terminal:
age_str = "21"               # maan lijiye user ne 21 type kiya
age = int(age_str)           # int() mein convert kiya
print("Agley saal aapki age hogi:", age + 1)

# Real input lene ka syntax:
# user_age = int(input("Apni age enter karein: "))
# user_salary = float(input("Apni monthly salary enter karein: "))
# print("Age:", user_age, "| Salary:", user_salary)

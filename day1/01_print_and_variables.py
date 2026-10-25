# =============================================================================
# DAY 1 - TOPIC 01: Print Statement, Comments & Variables
# =============================================================================
# Python mein coding ki shuruat yahin se hoti hai!
# =============================================================================

# 1. Single-line comment (# se likhte hain, Python isse ignore karta hai)
"""
Multi-line comment (ya docstring)
Aap yahan multiple lines mein notes likh sakte hain.
"""

# 2. Print Statement
print("Hello, World!")
print("Welcome to Day 1 of Python Revision!")

# Print mein multiple cheezein ek sath print karna:
print("My name is", "Sapna", "and I am learning Python.")

# 3. Variables kya hote hain?
# Variable ek naam (label) hota hai jo kisi value ko store karta hai.
name = "Sapna"
age = 22
city = "Delhi"

print("Name:", name)
print("Age:", age)
print("City:", city)

# 4. Variable Naming Rules (Python ke niyam):
# - Variable ka naam letter ya underscore (_) se shuru hona chahiye (jaise: my_name, _count)
# - Number se shuru NAHI ho sakta (1name ❌ galat hai, name1 ✔️ sahi hai)
# - Spaces allow nahi hain (user name ❌ galat hai, user_name ✔️ sahi hai)
# - Python Case-Sensitive hai (age aur Age do alag variables hain)

user_name = "Rahul"
user_age = 25
print("User:", user_name, "| Age:", user_age)

# =============================================================================
# 5. Keywords & Identifiers (Core Concept)
# =============================================================================
# Keywords: Python ke reserved words jinka pehle se fixed meaning hota hai.
# Inhe hum variable name ke tor par use NAHI kar sakte.

import keyword

print("\n--- Python Keywords ---")
print("Total Keywords in Python:", len(keyword.kwlist))
print("Keywords List:", keyword.kwlist)

# Example:
# if = 100        # ❌ SyntaxError (Kyunki 'if' ek keyword hai)
# while = "loop"  # ❌ SyntaxError (Kyunki 'while' ek keyword hai)
my_if = 100       # ✔️ Sahi hai

# Identifiers kya hote hain?
# Kisi bhi variable, function ya class ke NAAM ko 'Identifier' kehte hain.
# Example: yahan 'score' ek identifier hai
score = 95
print("\nIdentifier example (score):", score)


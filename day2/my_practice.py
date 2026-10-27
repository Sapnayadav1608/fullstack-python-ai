"""
=============================================================================
  DAY 02: MY STRING PRACTICE WORKBOOK (Code Yourself Here!)
=============================================================================
Name: Sapna Yadav
Topic: Python Strings — Indexing, Slicing, Immutability & Methods
Instructions: 
- Video dekhte waqt har task ka code niche diye gaye space mein KHUD type karein.
- Terminal se run karke test karein: python day2/my_practice.py
=============================================================================
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("🚀 DAY 2: MY HANDS-ON STRING PRACTICE")
print("=" * 60)


# -----------------------------------------------------------------------------
# TASK 1: String Creation & Raw String
# -----------------------------------------------------------------------------
# 1. Ek normal string variable banayein jismein aapka roll/role ho.
# 2. Ek multi-line string banayein triple quotes (""") se apne 3 goals ke saath.
# 3. Ek Windows path ko raw string r"" use karke print karein (jaise: C:\new_folder\test)

print("\n--- [Task 1] String Creation ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 2: Immutability & Memory Check
# -----------------------------------------------------------------------------
# 1. Ek string banayein: lang = "Python"
# 2. id(lang) print karein.
# 3. Slicing aur '+' use karke lang ko "Jython" banayein aur naya id(lang) print karein.

print("\n--- [Task 2] Immutability & Memory Address ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 3: Indexing (Positive & Negative)
# -----------------------------------------------------------------------------
# Word diya gaya hai:
target_word = "ENGINEERING"

# 1. Pehla letter print karein (Positive index se).
# 2. Aakhiri letter print karein (Negative index se).
# 3. Middle letter print karein.

print("\n--- [Task 3] Indexing ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 4: Slicing Mastery (Crucial for Interviews!)
# -----------------------------------------------------------------------------
# Sentence diya gaya hai:
quote = "ArtificialIntelligence"

# 1. Shuru ke 10 letters slice karein ('Artificial').
# 2. Baaki bache hue letters slice karein ('Intelligence').
# 3. Har doosra letter slice karein [::2].
# 4. Poore quote ko REVERSE slice karein [::-1].

print("\n--- [Task 4] Slicing Tricks ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 5: String Operations (+, *, in)
# -----------------------------------------------------------------------------
# 1. Do strings ko jodkar ek poora sentence banayein (+ operator se).
# 2. Ek decorative line banayein ("=" * 40).
# 3. Check karein kya "Python" aapke sentence ke andar hai ya nahi ('in' operator se).

print("\n--- [Task 5] Operations ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 6: String Cleaning & Case Conversion
# -----------------------------------------------------------------------------
messy_input = "   \n\t  fULL sTaCK dEvELoPeR   \t\n  "

# 1. Extra spaces aur tabs hatayein (.strip() use karke).
# 2. Saare letters ko LOWERCASE karein.
# 3. Saare letters ko UPPERCASE karein.
# 4. Proper TITLE CASE mein convert karein (.title()).

print("\n--- [Task 6] Cleaning & Case Conversion ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 7: Search & Replace
# -----------------------------------------------------------------------------
sample_paragraph = "I love python because python is easy and python is powerful."

# 1. 'python' word kitni baar aaya count karein (.count()).
# 2. Pehli baar 'easy' kis index par aaya find karein (.find()).
# 3. Saare 'python' ko 'Python 3' se replace karein (.replace()).

print("\n--- [Task 7] Search & Replace ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 8: Split & Join (Data Processing)
# -----------------------------------------------------------------------------
skills_csv = "HTML,CSS,JavaScript,Python,FastAPI,SQL"

# 1. CSV string ko todkar list banayein (.split(',')).
# 2. Us list ko wapas jod kar " -> " ke sath print karein (.join()).

print("\n--- [Task 8] Split & Join ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 9: Modern f-string Formatting
# -----------------------------------------------------------------------------
item_name = "AI Developer Course"
original_cost = 4999.789
discount_percent = 20

# f-string use karke ek receipt print karein jismein:
# - Course name ho
# - Price decimal ke baad sirf 2 digits tak rounded ho (:.2f)

print("\n--- [Task 9] f-string Formatting ---")
# TODO: Apna code yahan likhein:




# -----------------------------------------------------------------------------
# TASK 10: MINI CHALLENGE - Palindrome Checker (Khud Banayein!)
# -----------------------------------------------------------------------------
# User se ek word input lein (ya hardcode karein, jaise "radar" ya "madam")
# Aur slicing [::-1] use karke check karein ki wo Palindrome hai ya nahi!
# If Palindrome, print: "It is a Palindrome!"
# Else, print: "Not a Palindrome!"

print("\n--- [Task 10] Mini Challenge: Palindrome ---")
# TODO: Apna code yahan likhein:




print("\n" + "=" * 60)
print("🎉 Great Job! Day 2 Practice Completed!")
print("=" * 60)

# =============================================================================
# DAY 02 - TOPIC 05: Case Conversion & Cleaning Methods
# =============================================================================
# Data cleaning aur user input validation ke liye sabse zaroori methods.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 05] Case Conversion & Cleaning Methods")
print("=" * 60)

raw_text = "   heLLo wOrLD! wELcOmE tO pYtHoN   "

# 1. Case Conversion Methods
print("Original Text      :", repr(raw_text))
print("upper()            :", raw_text.upper())        # Sabhi uppercase
print("lower()            :", raw_text.lower())        # Sabhi lowercase
print("capitalize()       :", raw_text.strip().capitalize())  # Sirf pehla letter capital
print("title()            :", raw_text.title())        # Har word ka pehla letter capital
print("swapcase()         :", raw_text.swapcase())     # Lower ko upper, upper ko lower

# 2. Whitespace Removal (Cleaning)
padded_code = "   \n\t def main():  \t\n  "
print("\n--- Whitespace Stripping ---")
print("strip()  (Both sides) :", repr(padded_code.strip()))
print("lstrip() (Left only)  :", repr(padded_code.lstrip()))
print("rstrip() (Right only) :", repr(padded_code.rstrip()))

# 3. Modern Prefix & Suffix Removal (Python 3.9+)
filename = "invoice_october_2026.pdf"
print("\n--- Prefix / Suffix Removal ---")
print("Original Filename      :", filename)
print("removeprefix('invoice_'):", filename.removeprefix("invoice_"))
print("removesuffix('.pdf')    :", filename.removesuffix(".pdf"))

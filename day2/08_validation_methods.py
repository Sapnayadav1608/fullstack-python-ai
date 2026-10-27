# =============================================================================
# DAY 02 - TOPIC 08: String Inspection & Validation Methods
# =============================================================================
# String ke characters ka nature check karne wale boolean methods (True/False).
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 08] String Validation Methods")
print("=" * 60)

# 1. isalpha() -> Kya saare characters sirf alphabets hain? (No numbers, no spaces)
print("'Python'.isalpha()       ->", "Python".isalpha())        # True
print("'Python 3'.isalpha()     ->", "Python 3".isalpha())      # False (Space aur number hai)

# 2. isdigit() vs isnumeric() vs isdecimal()
# - isdecimal(): Sirf 0-9 digits
# - isdigit(): Digits + Superscripts (jaise ² ya ³)
# - isnumeric(): Saare numeric representations (jaise fractions ½, Roman numerals)
pin_code = "110001"
print("\n'110001'.isdigit()      ->", pin_code.isdigit())        # True
print("'12.5'.isdigit()         ->", "12.5".isdigit())          # False (Decimal point is not a digit!)

# 3. isalnum() -> Alphanumeric (Letters ya Numbers, but NO special symbols)
user_id = "sapna1608"
print("\n'sapna1608'.isalnum()    ->", user_id.isalnum())         # True
print("'sapna_1608'.isalnum()   ->", "sapna_1608".isalnum())    # False ('_' special character hai)

# 4. isspace() -> Kya string mein sirf spaces/tabs/newlines hain?
empty_input = "   \t\n  "
print("\n'   \\t\\n  '.isspace()    ->", empty_input.isspace())     # True

# 5. isidentifier() -> Kya yeh string ek valid Python variable name ban sakti hai?
print("\n'my_var_1'.isidentifier()->", "my_var_1".isidentifier()) # True
print("'1_my_var'.isidentifier()->", "1_my_var".isidentifier()) # False (Cannot start with digit!)
print("'user name'.isidentifier()->", "user name".isidentifier())# False (Spaces not allowed!)

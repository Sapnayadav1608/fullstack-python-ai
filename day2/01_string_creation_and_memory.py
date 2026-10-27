# =============================================================================
# DAY 02 - TOPIC 01: String Creation, Memory & Immutability Deep Dive
# =============================================================================
# Strings Python mein immutable sequences of Unicode characters hoti hain.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 01] String Creation, Memory & Immutability")
print("=" * 60)

# 1. String Creation ke Tareeqe
single_quote = 'Python'
double_quote = "Full Stack Development"
triple_quote = """Yeh multi-line string hai.
Aap isme paragraphs ya docstrings
bina kisi syntax error ke likh sakte hain."""

# Raw Strings (r"...") -> Escape characters (jaise \n, \t) ko ignore karta hai
# Path aur Regular Expressions mein bohot use hota hai:
normal_path = "C:\new_folder\test"   # \n new line ban jayega aur \t tab ban jayega!
raw_path = r"C:\new_folder\test"      # Raw string se path safe rehta hai

print("Normal string with escapes:\n", repr(normal_path))
print("Raw string representation:\n", repr(raw_path))

# 2. Immutability ka Deep Concept (Memory Level)
# String ka koi bhi character aap directly change NAHI kar sakte!
message = "Python"
print(f"\nOriginal Message: '{message}' | Memory Address: {id(message)}")

# ❌ Niche wali line error degi (TypeError: 'str' object does not support item assignment)
# message[0] = "J"

# Agar hum modify karte hain, toh असल mein kya hota hai?
message = "J" + message[1:]  # Naya string "Jython" banaya
print(f"Modified Message: '{message}' | Memory Address: {id(message)} (Address badal gaya!)")

# 3. String Interning (CPython Optimization)
# Chhoti aur identifier-like strings ko Python memory mein intern (cache) kar leta hai
str1 = "hello_world"
str2 = "hello_world"
print(f"\nstr1 is str2? {str1 is str2} (Dono ka memory address same hai!)")

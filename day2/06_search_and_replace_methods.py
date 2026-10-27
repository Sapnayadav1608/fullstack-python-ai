# =============================================================================
# DAY 02 - TOPIC 06: Search & Replace String Methods
# =============================================================================
# Substring dhoondhna, index nikaalna aur replace karna.
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 06] Search & Replace Methods")
print("=" * 60)

sentence = "Python is awesome. Python is easy. Python is powerful."

# 1. find() vs index() (Bohot important interview difference!)
# - find(): Agar word milta hai toh index deta hai, NAHI milta toh -1 deta hai (No crash!)
# - index(): Agar word nahi milta toh ValueError dekar CRASH kar deta hai!

print("sentence.find('Python')    ->", sentence.find("Python"))     # 0 (Pehla occurrence)
print("sentence.rfind('Python')   ->", sentence.rfind("Python"))    # 35 (Aakhiri occurrence)
print("sentence.find('Java')      ->", sentence.find("Java"))       # -1 (Safe!)

try:
    print(sentence.index("Java"))  # Crash karega
except ValueError as err:
    print("[index() Error Caught]    :", err)

# 2. count() -> Kitni baar aaya
print("\nsentence.count('Python') ->", sentence.count("Python"))     # 3
print("sentence.count('is')     ->", sentence.count("is"))         # 3

# 3. startswith() and endswith() (Validation ke liye)
url = "https://github.com/Sapnayadav1608/fullstack-python-ai.git"

print("\n--- URL Check ---")
print("Starts with 'https://' :", url.startswith("https://"))  # True
print("Ends with '.git'       :", url.endswith(".git"))        # True

# 4. replace(old, new, count) -> String ke parts replace karna
# Ek naya string return karta hai (immutability rule)
clean_url = url.replace("https://", "").replace(".git", "")
print("Clean URL               :", clean_url)

# Count limit lagana (Sirf pehla replace karna):
demo_text = "cat bat rat mat cat"
print("replace only 1st 'cat' :", demo_text.replace("cat", "dog", 1))

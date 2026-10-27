# =============================================================================
# DAY 02 - TOPIC 07: Split, Partition & Join Methods
# =============================================================================
# Strings ko todna (Lists banana) aur Lists ko wapas jodna (String banana).
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 02 - TOPIC 07] Split, Partition & Join")
print("=" * 60)

# 1. split(separator, maxsplit) -> String to List
# Default separator: koi bhi whitespace (spaces, tabs, newlines)
log_entry = "2026-10-27 | ERROR | Database connection timeout"
parts = log_entry.split(" | ")
print("Log parts list:", parts)
print("Timestamp:", parts[0], "| Log Level:", parts[1], "| Message:", parts[2])

# maxsplit demonstration (Sirf pehle 2 splits):
csv_row = "Sapna,Engineer,Python,FastAPI,AI,Delhi"
print("\nmaxsplit=2 demo:", csv_row.split(",", 2))

# 2. join(iterable) -> List of strings ko wapas single string banana
# Syntax: "separator".join(list)
tech_stack = ["Python", "FastAPI", "React", "PostgreSQL", "Docker"]
tech_string = " -> ".join(tech_stack)
print("\nJoined String:\n", tech_string)

# 3. partition(separator) -> Humesha ek 3-element tuple return karta hai:
# (before_sep, separator, after_sep)
email = "sapnayadav@domain.com"
before, sep, after = email.partition("@")
print("\n--- partition() Demo ---")
print("Username :", before)
print("Separator:", sep)
print("Domain   :", after)

# 4. splitlines() -> Multiline text ko line-by-line list banana
multiline_code = """import os
import sys

def main():
    print('Hello')"""

lines = multiline_code.splitlines()
print("\nTotal lines of code:", len(lines))
for num, line in enumerate(lines, 1):
    print(f"Line {num}: {line}")

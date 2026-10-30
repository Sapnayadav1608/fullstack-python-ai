# =============================================================================
# DAY 05 - TOPIC 03: Adding & Removing Elements in Lists
# =============================================================================
# append() vs extend() vs insert()
# pop() vs remove() vs del vs clear()
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 05 - TOPIC 03] Adding & Removing Elements")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1. Adding Elements: append() vs extend() vs insert()
# -----------------------------------------------------------------------------
skills = ["Python", "Git"]

# .append(item): Adds single element at the very end -> O(1)
skills.append("SQL")
print("After append('SQL')    :", skills)

# Interview Trap: append with a list creates a nested list!
skills.append(["FastAPI", "Docker"])
print("append(['FastAPI'...]) :", skills)  # Nested list ban gayi!
skills.pop() # remove it back

# .extend(iterable): Unpacks and adds all items individually at the end -> O(k)
skills.extend(["FastAPI", "Docker"])
print("After extend([...])     :", skills)

# .insert(index, item): Inserts at a specific position -> O(N) slow!
# Baaki saare elements ko right shift karna padta hai
skills.insert(1, "VS Code")
print("insert(1, 'VS Code')    :", skills)


# -----------------------------------------------------------------------------
# 2. Removing Elements: pop() vs remove() vs del vs clear()
# -----------------------------------------------------------------------------
tools = ["VS Code", "Postman", "Git", "Docker", "Git", "Kubernetes"]
print("\nOriginal Tools:", tools)

# A. .pop(index): Index se item remove karta hai aur uski VALUE RETURN karta hai
# Default: Last item pop karta hai -> O(1)
popped_item = tools.pop()
print(f"tools.pop() -> Removed '{popped_item}', Tools now: {tools}")

# Specific index pop: tools.pop(0) -> O(N) slow (shifts everything left)
first_tool = tools.pop(0)
print(f"tools.pop(0) -> Removed '{first_tool}', Tools now: {tools}")

# B. .remove(value): VALUE ke basis par pehla matching item delete karta hai
# Return kuch nahi karta (None). Agar value nahi mili toh ValueError deta hai!
tools.remove("Git")  # Sirf pehla 'Git' remove karega
print("After remove('Git')     :", tools)

# C. del statement: Python ka universal keyword jo index ya slice delete karta hai
del tools[0]
print("After del tools[0]      :", tools)

# D. .clear(): List ko poori tarah khaali kar deta hai (in-place)
tools.clear()
print("After tools.clear()     :", tools)  # []

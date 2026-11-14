"""
Day 10: Dictionary CRUD Operations, Advanced Methods & Python 3.9+ Union (|)
=============================================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. Access: Square Brackets [] (KeyError trap) vs .get(key, default)
2. The .setdefault() Method: One-step read-or-initialize pattern
3. Dictionary Modification & Merging: .update() vs Python 3.9+ Union (| and |=)
4. Deletion Strategies: .pop(), .popitem() (LIFO), del, and .clear()
5. Dynamic Dictionary Views: .keys(), .values(), .items() & Set-Like Operations
6. Real-World Application: Nested Configuration Merger with Conflict Resolution
"""

import sys

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 10 - TOPIC 02: DICTIONARY METHODS, CRUD & PYTHON 3.9+ UNION OPERATORS]")
print("=" * 70)

# -------------------------------------------------------------------------
# 1. ACCESSING VALUES: [] VS .get() (AVOIDING CRASHES)
# -------------------------------------------------------------------------
print("\n--- 1. Safe Access: [] vs .get() ---")
user_profile = {"id": 101, "username": "codemaster", "tier": "PRO"}

# Direct Bracket Access
print(f"Direct access ['username'] : {user_profile['username']}")

try:
    # Accessing non-existent key with [] raises KeyError!
    missing_email = user_profile["email"]
except KeyError as err:
    print(f">> KeyError caught: Key {err} does not exist in dictionary!")

# Safe Access with .get(): Returns None (or custom fallback) instead of crashing!
email = user_profile.get("email", "support@system.internal")
country = user_profile.get("country", "Unknown")
print(f"Safe access .get('email')  : {email}")
print(f"Safe access .get('country'): {country}")


# -------------------------------------------------------------------------
# 2. THE .setdefault() METHOD: READ OR INITIALIZE
# -------------------------------------------------------------------------
print("\n--- 2. The .setdefault() Method ---")
# .setdefault(key, default_val) checks:
# - If key exists: returns its existing value.
# - If key MISSING: inserts key with default_val and returns it!

server_clusters = {
    "us-east": ["node-1", "node-2"]
}

# 'us-east' already exists -> returns existing list
res1 = server_clusters.setdefault("us-east", [])
res1.append("node-3")

# 'eu-west' does NOT exist -> inserts 'eu-west': [] and returns it
res2 = server_clusters.setdefault("eu-west", [])
res2.append("node-10")

print(f"Updated Clusters via setdefault:\n  {server_clusters}")


# -------------------------------------------------------------------------
# 3. MERGING DICTIONARIES: .update() VS PYTHON 3.9+ PIPE OPERATOR (|)
# -------------------------------------------------------------------------
print("\n--- 3. Merging Dictionaries (Python 3.9+ Union '|') ---")
default_config = {"theme": "dark", "font_size": 14, "auto_save": True}
user_overrides = {"font_size": 18, "debug_mode": True}

# Method A: Traditional .update() (MUTATES in-place)
config_copy = default_config.copy()
config_copy.update(user_overrides)
print(f"Method A (.update in-place) : {config_copy}")

# Method B: Python 3.9+ Union Operator '|' (Creates NEW dict, elegant & non-destructive!)
merged_config = default_config | user_overrides
print(f"Method B (default | user)   : {merged_config}")

# Method C: Python 3.9+ In-Place Merge '|='
default_config |= user_overrides
print(f"Method C (in-place '|=')    : {default_config}")


# -------------------------------------------------------------------------
# 4. DELETION STRATEGIES: .pop(), .popitem(), del, .clear()
# -------------------------------------------------------------------------
print("\n--- 4. Deletion Strategies ---")
inventory = {"apple": 10, "banana": 25, "cherry": 50, "date": 8}
print(f"Initial Inventory: {inventory}")

# 1. .pop(key, default): Removes key and returns its value
removed_bananas = inventory.pop("banana")
print(f"1. .pop('banana') -> Value: {removed_bananas} | Remaining: {inventory}")

# .pop with fallback prevents KeyError if missing:
missing_item = inventory.pop("mango", 0)
print(f"   Safe .pop('mango', 0) -> Value: {missing_item}")

# 2. .popitem(): Removes and returns the LAST inserted item (LIFO - Last In, First Out)
last_item = inventory.popitem()
print(f"2. .popitem() (LIFO) -> {last_item} | Remaining: {inventory}")

# 3. del: Statement deletion
del inventory["apple"]
print(f"3. del inventory['apple'] -> Remaining: {inventory}")

# 4. .clear(): Clears all items in place
inventory.clear()
print(f"4. inventory.clear() -> {inventory}")


# -------------------------------------------------------------------------
# 5. DYNAMIC DICTIONARY VIEWS & SET-LIKE OPERATIONS
# -------------------------------------------------------------------------
print("\n--- 5. Dynamic Views & Set-Like Operations ---")
# .keys(), .values(), .items() return dynamic VIEW objects.
# They are NOT static lists; they reflect changes immediately!

metrics = {"latency_ms": 42, "error_rate": 0.01, "cpu_load": 0.65}
keys_view = metrics.keys()
items_view = metrics.items()

print(f"Original Keys View : {keys_view}")
metrics["memory_load"] = 0.80  # Mutate metrics!
print(f"Live Updated View  : {keys_view} (Automatically reflected!)")

# Set-Like Operations on Dict Keys:
# Dict keys support set operations: & (intersection), | (union), - (difference)!
db_a_users = {"alex": 1, "bella": 2, "charlie": 3}
db_b_users = {"bella": 2, "charlie": 30, "david": 4}

common_users = db_a_users.keys() & db_b_users.keys()
only_in_a = db_a_users.keys() - db_b_users.keys()

print(f"\nCommon Usernames (Keys &)     : {common_users}")
print(f"Users only in DB A (Keys -)   : {only_in_a}")


# -------------------------------------------------------------------------
# 6. REAL-WORLD APPLICATION: MULTI-LEVEL CONFIGURATION RESOLVER
# -------------------------------------------------------------------------
print("\n--- 6. Real-World Backend: Config Resolver ---")

def resolve_service_config(base_cfg: dict, env_cfg: dict) -> dict:
    """Combines base config with environment overrides using Python 3.9+ union."""
    resolved = base_cfg | env_cfg
    # Normalize log level to uppercase
    resolved["log_level"] = resolved.get("log_level", "INFO").upper()
    return resolved

base_settings = {"port": 8000, "timeout": 30, "log_level": "info", "workers": 4}
prod_settings = {"port": 443, "timeout": 60, "workers": 16}

final_cfg = resolve_service_config(base_settings, prod_settings)
print(f"Resolved Production Config:\n  {final_cfg}")

print("\n[SUMMARY] Dictionary methods provide safe, atomic, and set-compatible CRUD!")

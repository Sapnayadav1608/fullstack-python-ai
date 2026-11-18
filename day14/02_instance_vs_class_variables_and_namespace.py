"""
Day 14: Object-Oriented Programming (OOP) Part 1
Module 02: Instance vs Class Variables, Namespaces, and the Mutation Trap
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Class Namespace vs Instance Namespace: Demystifying `__dict__`.
2. Class Variables (shared state) vs Instance Variables (unique to object).
3. The Catastrophic Mutable Class Variable Bug Trap.
4. Attribute Lookup Order: How Python searches for variables on objects.
5. Shadowing Class Variables via `self.var = ...`.
6. Memory Architecture: Slashing RAM with `__slots__`.
"""

import sys
from typing import List


# ============================================================================
# 1. CLASS VARIABLES VS INSTANCE VARIABLES
# ============================================================================
"""
INSTANCE VARIABLES:
- Defined inside methods (usually `__init__`) using `self.attribute`.
- Unique to EACH instance. Changing it on one object does not affect any other.

CLASS VARIABLES:
- Defined directly inside the class body, outside any method.
- Shared by ALL instances of the class. Useful for constants, counters, or global state.
"""

print("=" * 70)
print("1. CLASS VARIABLES VS INSTANCE VARIABLES")
print("=" * 70)

class DatabaseConnection:
    # Class Variable (Shared across all instances)
    DEFAULT_TIMEOUT_SEC: int = 30
    active_connection_count: int = 0

    def __init__(self, host: str, port: int) -> None:
        # Instance Variables (Unique to each connection)
        self.host = host
        self.port = port
        DatabaseConnection.active_connection_count += 1

    def close(self) -> None:
        DatabaseConnection.active_connection_count -= 1


db1 = DatabaseConnection("db.production.aws.com", 5432)
db2 = DatabaseConnection("db.staging.aws.com", 5432)

print(f"db1: {db1.host}:{db1.port} | Timeout: {db1.DEFAULT_TIMEOUT_SEC}s")
print(f"db2: {db2.host}:{db2.port} | Timeout: {db2.DEFAULT_TIMEOUT_SEC}s")
print(f"Total Active Connections: {DatabaseConnection.active_connection_count}")

db1.close()
print(f"After closing db1 -> Active Connections: {DatabaseConnection.active_connection_count}")


# ============================================================================
# 2. INTROSPECTION & THE NAMESPACE DICTIONARY: `__dict__`
# ============================================================================
"""
In Python, almost every object is secretly backed by a dictionary called `__dict__`!
- `instance.__dict__`: Stores the instance's unique attributes.
- `Class.__dict__`: Stores the class's methods and class variables.
"""

print("\n" + "=" * 70)
print("2. UNDER THE HOOD: `__dict__` NAMESPACE INTROSPECTION")
print("=" * 70)

print(f"db2.__dict__ (Instance Namespace): {db2.__dict__}")
# Notice that DEFAULT_TIMEOUT_SEC is NOT in db2.__dict__! It lives in the class namespace:
print(f"DEFAULT_TIMEOUT_SEC in db2.__dict__? {'DEFAULT_TIMEOUT_SEC' in db2.__dict__}")  # False
print(f"DEFAULT_TIMEOUT_SEC in DatabaseConnection.__dict__? {'DEFAULT_TIMEOUT_SEC' in DatabaseConnection.__dict__}")  # True


# ============================================================================
# 3. ATTRIBUTE LOOKUP CHAIN & THE SHADOWING TRAP
# ============================================================================
"""
ATTRIBUTE LOOKUP ORDER:
When you evaluate `obj.attr`:
1. Python checks `obj.__dict__` (instance namespace).
2. If NOT found, it checks `obj.__class__.__dict__` (class namespace).
3. If NOT found, it checks base classes (MRO - Method Resolution Order).
4. If nowhere to be found, it raises `AttributeError`.

THE SHADOWING TRAP:
If you do `obj.class_var = new_val`, you do NOT change the class variable!
You accidentally create a NEW instance variable with the same name inside `obj.__dict__`,
SHADOWING (masking) the class variable for that instance only!
"""

print("\n" + "=" * 70)
print("3. THE ATTRIBUTE SHADOWING TRAP")
print("=" * 70)

class ServerConfig:
    PORT = 8080

s1 = ServerConfig()
s2 = ServerConfig()

# Intent: change port for s1
s1.PORT = 9000  # Creates 'PORT' in s1.__dict__! Does NOT alter ServerConfig.PORT!

print(f"s1.PORT: {s1.PORT}  (Reads from s1.__dict__)")
print(f"s2.PORT: {s2.PORT}  (Reads from ServerConfig.__dict__)")
print(f"ServerConfig.PORT: {ServerConfig.PORT} (Unchanged!)")
print(f"s1.__dict__: {s1.__dict__}")
print(f"s2.__dict__: {s2.__dict__}")


# ============================================================================
# 4. THE CATASTROPHIC MUTABLE CLASS VARIABLE BUG TRAP
# ============================================================================
"""
FAANG INTERVIEW CLASSIC:
What happens if a class variable is MUTABLE (e.g. list, dict, set)?
Mutating it via ANY instance mutates the SHARED object for EVERY instance!
This causes silent, catastrophic security bugs (e.g., leaking user roles).
"""

print("\n" + "=" * 70)
print("4. THE CATASTROPHIC MUTABLE CLASS VARIABLE BUG TRAP")
print("=" * 70)

# --- BUGGY IMPLEMENTATION ---
class BuggyUser:
    permissions: List[str] = []  # MUTABLE CLASS VARIABLE! DANGER!

    def __init__(self, username: str) -> None:
        self.username = username

    def add_permission(self, perm: str) -> None:
        self.permissions.append(perm)

guest = BuggyUser("guest_user")
admin = BuggyUser("admin_user")

admin.add_permission("ADMIN_SUPERUSER_ACCESS")

print("Buggy Behavior:")
print(f"  Admin permissions: {admin.permissions}")
print(f"  Guest permissions: {guest.permissions}  <-- SECURITY BREACH! Guest has superuser access!")


# --- FIXED IMPLEMENTATION ---
class SecureUser:
    def __init__(self, username: str) -> None:
        self.username = username
        # Correct: Unique list created per instance inside __init__
        self.permissions: List[str] = []

    def add_permission(self, perm: str) -> None:
        self.permissions.append(perm)

sec_guest = SecureUser("guest_user")
sec_admin = SecureUser("admin_user")

sec_admin.add_permission("ADMIN_SUPERUSER_ACCESS")

print("\nFixed & Secure Behavior:")
print(f"  Secure Admin permissions: {sec_admin.permissions}")
print(f"  Secure Guest permissions: {sec_guest.permissions}  <-- Safe! Completely isolated.")


# ============================================================================
# 5. MEMORY OPTIMIZATION: `__slots__`
# ============================================================================
"""
Why does Python use so much RAM for small objects?
Because every instance dictionary `__dict__` consumes around 150-200 bytes of overhead!
When creating millions of objects (e.g., in AI vector search or financial trading),
defining `__slots__` tells CPython:
"Do not create a dynamic __dict__! Allocate a fixed, lightweight C array instead!"
"""

print("\n" + "=" * 70)
print("5. MEMORY OPTIMIZATION: `__slots__`")
print("=" * 70)

class StandardPoint:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

class SlottedPoint:
    __slots__ = ("x", "y", "z")  # Fixed attributes, eliminates __dict__
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

pt_std = StandardPoint(1.0, 2.0, 3.0)
pt_slot = SlottedPoint(1.0, 2.0, 3.0)

print(f"StandardPoint size (with __dict__): {sys.getsizeof(pt_std) + sys.getsizeof(pt_std.__dict__)} bytes")
print(f"SlottedPoint size  (zero __dict__): {sys.getsizeof(pt_slot)} bytes")
print(f"Has pt_slot got __dict__? {'__dict__' in dir(pt_slot)}")  # False

print("\n" + "=" * 70)
print("DAY 14 MODULE 02: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

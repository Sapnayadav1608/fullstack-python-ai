"""
Day 09: Mathematical Set Theory & Real-World Operations in Python
=================================================================
30-Day Full Stack Python + AI Engineering Challenge

Topics Covered:
1. Union (| / .union()): Combining all unique elements
2. Intersection (& / .intersection()): Finding common elements
3. Difference (- / .difference()): Elements in A not in B
4. Symmetric Difference (^ / .symmetric_difference()): Elements in either, but not both
5. In-Place Operator Variants: |=, &=, -=, ^=
6. Relational Checks: issubset(), issuperset(), isdisjoint()
7. Real-World Backend System: Role-Based Access Control (RBAC) Permission Validator
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[DAY 09 - TOPIC 02: MATHEMATICAL SET OPERATIONS & RBAC]")
print("=" * 70)

# Two sample engineering skillsets
backend_dev = {"Python", "FastAPI", "SQL", "Docker", "Git"}
ai_engineer = {"Python", "PyTorch", "Docker", "LangChain", "VectorDB"}

print(f"Backend Dev Skills : {backend_dev}")
print(f"AI Engineer Skills : {ai_engineer}")


# -------------------------------------------------------------------------
# 1. UNION (| / .union()): All Unique Elements
# -------------------------------------------------------------------------
print("\n--- 1. Union: Combining All Skills ---")
full_stack_ai = backend_dev | ai_engineer
# Equivalent to: backend_dev.union(ai_engineer)

print(f"Union (backend_dev | ai_engineer):")
print(f"  {full_stack_ai}")
print(f"  Total Unique Skills: {len(full_stack_ai)}")


# -------------------------------------------------------------------------
# 2. INTERSECTION (& / .intersection()): Common Elements
# -------------------------------------------------------------------------
print("\n--- 2. Intersection: Shared Common Skills ---")
shared_skills = backend_dev & ai_engineer
# Equivalent to: backend_dev.intersection(ai_engineer)

print(f"Intersection (backend_dev & ai_engineer):")
print(f"  {shared_skills} (Skills common to both roles)")


# -------------------------------------------------------------------------
# 3. DIFFERENCE (- / .difference()): A minus B
# -------------------------------------------------------------------------
print("\n--- 3. Difference: Skills in A that are NOT in B ---")
pure_backend = backend_dev - ai_engineer  # Skills in backend, not AI
pure_ai = ai_engineer - backend_dev       # Skills in AI, not backend

print(f"Backend ONLY (backend_dev - ai_engineer): {pure_backend}")
print(f"AI ONLY      (ai_engineer - backend_dev): {pure_ai}")


# -------------------------------------------------------------------------
# 4. SYMMETRIC DIFFERENCE (^ / .symmetric_difference())
# -------------------------------------------------------------------------
print("\n--- 4. Symmetric Difference: In Either Role, But NOT Both ---")
unshared_skills = backend_dev ^ ai_engineer
# Equivalent to: (backend_dev - ai_engineer) | (ai_engineer - backend_dev)

print(f"Symmetric Difference (backend_dev ^ ai_engineer):")
print(f"  {unshared_skills}")


# -------------------------------------------------------------------------
# 5. SUBSETS, SUPERSETS & DISJOINT
# -------------------------------------------------------------------------
print("\n--- 5. Subsets, Supersets & Disjoint Checks ---")
core_python = {"Python", "Git"}

print(f"core_python              : {core_python}")
print(f"Is subset of backend_dev : {core_python.issubset(backend_dev)} (core_python <= backend_dev)")
print(f"Is backend_dev superset  : {backend_dev.issuperset(core_python)} (backend_dev >= core_python)")

# Disjoint: True if two sets have NO elements in common
designer_skills = {"Figma", "Canva", "Photoshop"}
print(f"designer_skills          : {designer_skills}")
print(f"backend & designer disjoint? {backend_dev.isdisjoint(designer_skills)} (No common overlap)")


# -------------------------------------------------------------------------
# 6. REAL-WORLD BACKEND SYSTEM: ROLE-BASED ACCESS CONTROL (RBAC)
# -------------------------------------------------------------------------
print("\n--- 6. Real-World Backend System: RBAC Permission Validator ---")

# Define endpoint required permissions
endpoint_required_perms = {"read:users", "write:users", "delete:users"}

user_a_perms = {"read:users", "write:users", "delete:users", "export:reports"} # Admin
user_b_perms = {"read:users", "read:posts"}                                     # Guest

def check_access(user_name: str, user_permissions: set, required_permissions: set) -> bool:
    """
    Validates if a user has ALL required permissions using set subset check.
    Time Complexity: O(len(required_permissions)) -> Average O(1)!
    """
    has_access = required_permissions.issubset(user_permissions)
    status = "ALLOWED" if has_access else "DENIED (Missing: " + str(required_permissions - user_permissions) + ")"
    print(f"Access Check for '{user_name}': {status}")
    return has_access

check_access("User A (Admin)", user_a_perms, endpoint_required_perms)
check_access("User B (Guest)", user_b_perms, endpoint_required_perms)

print("\n" + "=" * 70)
print("[OK] Mathematical Set Operations & RBAC Module Completed Successfully!")
print("=" * 70)

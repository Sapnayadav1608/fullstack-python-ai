# =============================================================================
# DAY 11 - STUDENT WORKBOOK: Functions, Scopes & Closures
# =============================================================================
# 30-Day Full Stack Python + AI Engineering Challenge
#
# Instructions:
# - Complete all 6 tasks below by replacing the 'pass' with your implementation.
# - Do NOT change the function signatures or test assertions.
# - Run this script in your terminal to verify your answers:
#       python day11/my_practice.py
# =============================================================================

import sys
from typing import List, Dict, Any, Optional, Callable, Tuple

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("🎯 DAY 11: STUDENT PRACTICE WORKBOOK — FUNCTIONS, SCOPES & CLOSURES")
print("=" * 70)


# =============================================================================
# TASK 1: FIX THE MUTABLE DEFAULT ARGUMENT TRAP
# =============================================================================
# Description:
# The following function has a classic bug where 'tags' list is shared across calls.
# Fix it by using 'None' as default value and creating a fresh list inside the function.
# =============================================================================
def register_student(student_id: int, tags: Optional[List[str]] = None) -> List[str]:
    # TODO: Fix the mutable default argument bug here
    pass


# =============================================================================
# TASK 2: API QUERY URL BUILDER (*args & **kwargs)
# =============================================================================
# Description:
# Build a function that accepts:
# - base_url: str (e.g. "https://api.github.com")
# - *paths: str (arbitrary path segments, e.g. "users", "Sapnayadav1608", "repos")
# - **query_params: Any (key-value query parameters, e.g. sort="created", direction="desc")
#
# Returns a clean formatted URL:
# "https://api.github.com/users/Sapnayadav1608/repos?direction=desc&sort=created"
# Note: Sort query parameters alphabetically by key for deterministic output!
# If no query params are provided, omit the '?' part.
# =============================================================================
def build_api_url(base_url: str, *paths: str, **query_params: Any) -> str:
    # TODO: Implement URL path joining and query string formatting
    pass


# =============================================================================
# TASK 3: STATEFUL COUNTER CLOSURE WITH 'nonlocal'
# =============================================================================
# Description:
# Write a closure factory function 'create_counter(initial_value: int = 0, step: int = 1)'.
# It should return an inner function that:
# - Increments its internal value by 'step' on each call.
# - Returns the new incremented value.
# Must use 'nonlocal' and must NOT use any global variables.
# =============================================================================
def create_counter(initial_value: int = 0, step: int = 1) -> Callable[[], int]:
    # TODO: Implement the closure factory retaining state in lexical scope
    pass


# =============================================================================
# TASK 4: MODERN PARAMETER MARKERS (/ and *)
# =============================================================================
# Description:
# Implement 'generate_access_token':
# - 'user_id' and 'secret_key' MUST be Positional-Only (cannot be passed as keywords).
# - 'expiry_minutes' can be passed either positionally or by keyword (default = 60).
# - 'role' and 'is_admin' MUST be Keyword-Only (default role="user", is_admin=False).
#
# Return a dict:
# {"token": f"{user_id}:{secret_key}:{expiry_minutes}", "role": role, "is_admin": is_admin}
# =============================================================================
def generate_access_token(
    user_id: int,
    secret_key: str,
    /,
    expiry_minutes: int = 60,
    *,
    role: str = "user",
    is_admin: bool = False
) -> Dict[str, Any]:
    # TODO: Implement token dictionary generation
    pass


# =============================================================================
# TASK 5: MULTI-KEY SORTING WITH LAMBDA
# =============================================================================
# Description:
# Given a list of product dictionaries:
# [{"name": "Laptop", "category": "Electronics", "price": 1200, "rating": 4.8}, ...]
#
# Sort the products:
# 1. Primary: Category ASCENDING (alphabetical 'category')
# 2. Secondary: Rating DESCENDING (-rating)
# 3. Tertiary: Price ASCENDING (price)
#
# Return the sorted list of products.
# =============================================================================
def sort_inventory(products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # TODO: Use sorted() with lambda key tuple
    pass


# =============================================================================
# TASK 6: RECURSIVE DIRECTORY SIZE CALCULATOR
# =============================================================================
# Description:
# Given a nested file system dictionary where values are either file sizes (int)
# or subdirectories (dict):
# fs = {
#     "docs": {"resume.pdf": 150, "notes.txt": 50},
#     "projects": {"ai": {"model.pt": 500, "train.py": 100}, "readme.md": 20},
#     "config.json": 10
# }
# Total size should be 150 + 50 + 500 + 100 + 20 + 10 = 830 KB.
#
# Write a recursive function 'calculate_total_size(node: dict) -> int'
# =============================================================================
def calculate_total_size(node: Dict[str, Any]) -> int:
    # TODO: Recursively calculate total size of all integers in nested structure
    pass


# =============================================================================
# AUTOMATED TEST SUITE (DO NOT MODIFY)
# =============================================================================
def run_tests():
    passed = 0
    total = 6

    # Test 1
    print("\n[TEST 1] Testing register_student (Mutable Default Fix)...")
    try:
        s1 = register_student(101)
        s2 = register_student(202)
        assert s1 is not None and s2 is not None, "Functions returned None"
        assert s1 == [101], f"Expected [101], got {s1}"
        assert s2 == [202], f"Expected [202], got {s2} (Default argument is leaking across calls!)"
        print("  --> PASS: Mutable default bug successfully eliminated! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 2
    print("\n[TEST 2] Testing build_api_url (*args & **kwargs)...")
    try:
        url1 = build_api_url("https://api.github.com", "users", "Sapnayadav1608", "repos", sort="pushed", direction="desc")
        assert url1 == "https://api.github.com/users/Sapnayadav1608/repos?direction=desc&sort=pushed", f"Got: {url1}"
        url2 = build_api_url("https://example.com", "v1", "health")
        assert url2 == "https://example.com/v1/health", f"Got: {url2}"
        print("  --> PASS: URL path and query builder works cleanly! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 3
    print("\n[TEST 3] Testing create_counter (Closure with nonlocal)...")
    try:
        c1 = create_counter(initial_value=10, step=5)
        assert c1() == 15, "Expected 15"
        assert c1() == 20, "Expected 20"
        assert c1() == 25, "Expected 25"
        c2 = create_counter(initial_value=0, step=1)
        assert c2() == 1, "Expected independent counter c2 to start at 1"
        assert c1() == 30, "Expected c1 to continue at 30"
        print("  --> PASS: Closure retains isolated lexical scope! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 4
    print("\n[TEST 4] Testing generate_access_token (/ and * markers)...")
    try:
        tok = generate_access_token(505, "sec-key", 120, role="admin", is_admin=True)
        assert tok == {"token": "505:sec-key:120", "role": "admin", "is_admin": True}, f"Got: {tok}"
        # Verify positional-only requirement
        try:
            generate_access_token(user_id=505, secret_key="sec-key")
            assert False, "Should raise TypeError for positional-only argument passed as keyword"
        except TypeError:
            pass  # Expected
        print("  --> PASS: Positional-only & keyword-only markers validated! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 5
    print("\n[TEST 5] Testing sort_inventory (Multi-Key Lambda)...")
    try:
        items = [
            {"name": "Mouse", "category": "Tech", "price": 25, "rating": 4.5},
            {"name": "Monitor", "category": "Tech", "price": 250, "rating": 4.8},
            {"name": "Desk", "category": "Furniture", "price": 150, "rating": 4.2},
            {"name": "Chair", "category": "Furniture", "price": 180, "rating": 4.8},
            {"name": "Cable", "category": "Tech", "price": 10, "rating": 4.8},
        ]
        sorted_items = sort_inventory(items)
        names = [x["name"] for x in sorted_items]
        # Furniture first (Chair rating 4.8, Desk 4.2), then Tech (Monitor price 250 rating 4.8, Cable price 10 rating 4.8, Mouse rating 4.5)
        assert names == ["Chair", "Desk", "Cable", "Monitor", "Mouse"], f"Order was: {names}"
        print("  --> PASS: Multi-key lambda sorted inventory perfectly! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    # Test 6
    print("\n[TEST 6] Testing calculate_total_size (Recursive Flattener)...")
    try:
        fs = {
            "docs": {"resume.pdf": 150, "notes.txt": 50},
            "projects": {"ai": {"model.pt": 500, "train.py": 100}, "readme.md": 20},
            "config.json": 10
        }
        total_sz = calculate_total_size(fs)
        assert total_sz == 830, f"Expected 830, got {total_sz}"
        print("  --> PASS: Recursive directory traversal computed exact size! ✅")
        passed += 1
    except Exception as e:
        print(f"  --> FAIL: {e}")

    print("\n" + "=" * 70)
    print(f"📊 FINAL SCORE: {passed}/{total} Tasks Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

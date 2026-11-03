"""
Day 08: Hands-On Practice Workbook - Python Tuples
===================================================
30-Day Full Stack Python + AI Engineering Challenge

Instructions for Sapna:
------------------------
1. Complete each function inside the '# TODO: Write your code here' sections.
2. Run the file: python day8/my_practice.py
3. The automated test suite at the bottom will verify your solutions!
"""

import sys

# Ensure safe output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 70)
print("[SAPNA'S DAY 08 PRACTICE WORKBOOK: PYTHON TUPLES]")
print("=" * 70)


# =========================================================================
# TASK 1: Safe Single-Element Tuple Creator
# =========================================================================
def create_single_element_tuple(item):
    """
    Given any item, return a tuple containing exactly that single item.
    Remember the comma rule!
    Example: 42 -> returns (42,)
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 2: Variable Swap using Tuple Packing / Unpacking
# =========================================================================
def swap_pair(a, b):
    """
    Swap two values without using a temporary variable, using tuple unpacking.
    Return a tuple: (new_a, new_b)
    Example: a = "AI", b = "Python" -> returns ("Python", "AI")
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 3: Stream Summary using Star (*) Unpacking
# =========================================================================
def stream_summary(data: tuple) -> dict:
    """
    Given a tuple of numbers (length >= 3), use the star operator (*) to extract:
    - 'first': the first element
    - 'last': the last element
    - 'middle_avg': the average (mean) of all remaining middle elements
    
    Example: (10, 20, 30, 40, 50)
             first = 10, last = 50, middle = [20, 30, 40] -> avg = 30.0
             returns {'first': 10, 'last': 50, 'middle_avg': 30.0}
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 4: Multi-Key Employee Sorter
# =========================================================================
def sort_employees(employees: list[tuple]) -> list[tuple]:
    """
    Given a list of tuples: (name, department, salary)
    Sort the employees:
    1. Primary: By 'salary' in DESCENDING order (highest salary first)
    2. Secondary: If salaries are tied, by 'name' in ASCENDING alphabetical order
    
    Example: [("Aman", "IT", 60000), ("Sapna", "AI", 90000), ("Rohan", "HR", 60000)]
    Returns: [("Sapna", "AI", 90000), ("Aman", "IT", 60000), ("Rohan", "HR", 60000)]
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 5: Recursive Tuple Flattener
# =========================================================================
def flatten_nested_tuple(nested: tuple) -> tuple:
    """
    Recursively flattens an arbitrarily nested tuple into a single flat tuple.
    Example: ((1, 2), 3, (4, (5, 6))) -> returns (1, 2, 3, 4, 5, 6)
    """
    # TODO: Write your code here
    pass


# =========================================================================
# TASK 6: Filter Coordinate Sensors (Tuple Keys)
# =========================================================================
def filter_first_quadrant_sensors(sensor_readings: dict) -> list[tuple]:
    """
    Given a dictionary where keys are (x, y) coordinate tuples and values are temperatures:
    sensor_readings = {
        (10, 20): 28.5,
        (-5, 12): 22.0,
        (15, -4): 30.1,
        (0, 5): 26.0
    }
    Return a list of ((x, y), temp) tuples for all coordinates in the FIRST quadrant
    where x >= 0 and y >= 0.
    """
    # TODO: Write your code here
    pass


# =========================================================================
# AUTOMATED TEST SUITE (Run this file to test your solutions!)
# =========================================================================
if __name__ == "__main__":
    print("\n--- Running Automated Verification Checks ---")
    passed = 0
    total = 6

    # Test Task 1
    try:
        t1 = create_single_element_tuple("Python")
        assert isinstance(t1, tuple), f"Expected tuple, got {type(t1)}"
        assert len(t1) == 1 and t1[0] == "Python", f"Expected ('Python',), got {t1}"
        print("[PASS] Task 1: Single-Element Tuple Creator")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 1 not completed: {e}")

    # Test Task 2
    try:
        t2 = swap_pair(10, 20)
        assert t2 == (20, 10), f"Expected (20, 10), got {t2}"
        print("[PASS] Task 2: Variable Swap using Tuple Unpacking")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 2 not completed: {e}")

    # Test Task 3
    try:
        t3 = stream_summary((10, 20, 30, 40, 50))
        assert t3 == {"first": 10, "last": 50, "middle_avg": 30.0}, f"Expected correct summary, got {t3}"
        print("[PASS] Task 3: Stream Summary using Star (*) Unpacking")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 3 not completed: {e}")

    # Test Task 4
    try:
        emp_list = [("Aman", "IT", 60000), ("Sapna", "AI", 90000), ("Rohan", "HR", 60000)]
        sorted_res = sort_employees(emp_list)
        expected = [("Sapna", "AI", 90000), ("Aman", "IT", 60000), ("Rohan", "HR", 60000)]
        assert sorted_res == expected, f"Expected {expected}, got {sorted_res}"
        print("[PASS] Task 4: Multi-Key Employee Sorter")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 4 not completed: {e}")

    # Test Task 5
    try:
        nested_tup = ((1, 2), 3, (4, (5, 6)))
        flat = flatten_nested_tuple(nested_tup)
        assert flat == (1, 2, 3, 4, 5, 6), f"Expected (1, 2, 3, 4, 5, 6), got {flat}"
        print("[PASS] Task 5: Recursive Tuple Flattener")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 5 not completed: {e}")

    # Test Task 6
    try:
        sensors = {
            (10, 20): 28.5,
            (-5, 12): 22.0,
            (15, -4): 30.1,
            (0, 5): 26.0
        }
        filtered = filter_first_quadrant_sensors(sensors)
        assert ((10, 20), 28.5) in filtered and ((0, 5), 26.0) in filtered and len(filtered) == 2, f"Got {filtered}"
        print("[PASS] Task 6: Filter Coordinate Sensors (Tuple Keys)")
        passed += 1
    except Exception as e:
        print(f"[TODO] Task 6 not completed: {e}")

    print("\n" + "=" * 70)
    print(f"Summary: {passed}/{total} Tasks Completed!")
    if passed == total:
        print("CONGRATULATIONS SAPNA! All Day 8 practice exercises passed!")
    else:
        print("Keep going! Open this file and write your logic inside each TODO function.")
    print("=" * 70)

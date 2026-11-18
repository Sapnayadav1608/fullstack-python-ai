"""
Day 14: Object-Oriented Programming (OOP) Part 1
Student Practice Workbook & Automated Test Suite
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Instructions:
- Fill in the # TODO sections for each of the 6 challenges.
- Run this file: `python day14/my_practice.py`
- All automated unit tests must pass!
"""

import math
from typing import List, Any


# ============================================================================
# TASK 1: BOOK CLASS WITH __str__ AND __repr__
# ============================================================================
"""
Create a `Book` class that stores:
- `title` (str)
- `author` (str)
- `pages` (int)

Requirements:
- `__str__`: Returns f"{title} by {author} ({pages} pages)"
- `__repr__`: Returns f"Book(title={title!r}, author={author!r}, pages={pages})"
"""

class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        # TODO: Initialize attributes
        raise NotImplementedError("TODO: Implement Book.__init__")

    def __str__(self) -> str:
        # TODO: Implement __str__
        raise NotImplementedError("TODO: Implement Book.__str__")

    def __repr__(self) -> str:
        # TODO: Implement __repr__
        raise NotImplementedError("TODO: Implement Book.__repr__")


# ============================================================================
# TASK 2: CLASS VARIABLE COUNTER & AVOID MUTABLE BUG
# ============================================================================
"""
Create a `StudentTracker` class:
- Class variable `total_enrolled: int = 0` tracks total students ever instantiated.
- Each instance has:
  - `name` (str)
  - `courses` (List[str]): Must be a UNIQUE list per student (avoid mutable class variable bug!).
- Method `enroll(course: str)`: Appends course to student's course list.
"""

class StudentTracker:
    total_enrolled: int = 0

    def __init__(self, name: str) -> None:
        # TODO: Initialize instance variables and increment total_enrolled
        raise NotImplementedError("TODO: Implement StudentTracker.__init__")

    def enroll(self, course: str) -> None:
        # TODO: Add course to this student's courses list
        raise NotImplementedError("TODO: Implement StudentTracker.enroll")


# ============================================================================
# TASK 3: ALTERNATIVE FACTORY CONSTRUCTOR WITH @classmethod
# ============================================================================
"""
Create a `Vector2D` class:
- `__init__(x: float, y: float)`: Stores x and y coordinates.
- Class method `from_polar(cls, r: float, theta_deg: float) -> Vector2D`:
  Converts polar coordinates (radius and angle in degrees) to Cartesian:
    x = round(r * math.cos(math.radians(theta_deg)), 2)
    y = round(r * math.sin(math.radians(theta_deg)), 2)
  Returns a new Vector2D instance using `cls(x, y)`.
"""

class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def from_polar(cls, r: float, theta_deg: float) -> "Vector2D":
        # TODO: Implement alternative factory constructor from polar coordinates
        raise NotImplementedError("TODO: Implement Vector2D.from_polar")


# ============================================================================
# TASK 4: UTILITY SERVICE WITH @staticmethod
# ============================================================================
"""
Create a `PasswordPolicy` class with a `@staticmethod`:
- `is_strong(password: str) -> bool`:
  Returns True if and only if password satisfies ALL 3 conditions:
  1. Length is at least 8 characters.
  2. Contains at least one digit (0-9).
  3. Contains at least one uppercase letter (A-Z).
  Otherwise returns False.
"""

class PasswordPolicy:
    @staticmethod
    def is_strong(password: str) -> bool:
        # TODO: Implement static validation logic
        raise NotImplementedError("TODO: Implement PasswordPolicy.is_strong")


# ============================================================================
# TASK 5: ENCAPSULATED THERMOSTAT WITH @property
# ============================================================================
"""
Create a `SmartThermostat` class:
- Takes `initial_celsius: float` (default 21.0).
- Uses `@property` for `temperature`:
  - Getter: returns internal protected float `_celsius`.
  - Setter:
    - Validates that new temp is between 10.0 and 35.0 inclusive.
    - If outside bounds, raises `ValueError("Temperature out of bounds [10.0, 35.0]")`.
    - Otherwise updates `_celsius`.
- Read-only property `fahrenheit`:
  - Returns `(self._celsius * 9 / 5) + 32` (no setter).
"""

class SmartThermostat:
    def __init__(self, initial_celsius: float = 21.0) -> None:
        self._celsius: float = 0.0
        # Set via property setter to trigger validation
        self.temperature = initial_celsius

    @property
    def temperature(self) -> float:
        # TODO: Implement getter
        raise NotImplementedError("TODO: Implement SmartThermostat.temperature getter")

    @temperature.setter
    def temperature(self, value: float) -> None:
        # TODO: Implement setter with bounds validation [10.0, 35.0]
        raise NotImplementedError("TODO: Implement SmartThermostat.temperature setter")

    @property
    def fahrenheit(self) -> float:
        # TODO: Implement computed read-only property
        raise NotImplementedError("TODO: Implement SmartThermostat.fahrenheit")


# ============================================================================
# TASK 6: PRIVATE ATTRIBUTES & NAME MANGLING (SECURE WALLET)
# ============================================================================
"""
Create a `SecureWallet` class:
- Private balance: `__balance` (starts at `initial_balance`, default 0.0).
- Private ledger: `__ledger: List[str]`.
- Property `balance`: Read-only property returning current `__balance`.
- Method `deposit(amount: float)`:
  - If amount <= 0, raise ValueError.
  - Adds to `__balance` and records f"DEPOSIT: +${amount:.2f}" in `__ledger`.
- Method `withdraw(amount: float)`:
  - If amount <= 0, raise ValueError.
  - If amount > __balance, raise ValueError("Insufficient funds").
  - Deducts from `__balance` and records f"WITHDRAW: -${amount:.2f}" in `__ledger`.
- Method `get_transaction_count()`: Returns length of `__ledger`.
"""

class SecureWallet:
    def __init__(self, initial_balance: float = 0.0) -> None:
        # TODO: Initialize private __balance and __ledger
        raise NotImplementedError("TODO: Implement SecureWallet.__init__")

    @property
    def balance(self) -> float:
        # TODO: Return private balance
        raise NotImplementedError("TODO: Implement SecureWallet.balance")

    def deposit(self, amount: float) -> None:
        # TODO: Implement deposit with validation
        raise NotImplementedError("TODO: Implement SecureWallet.deposit")

    def withdraw(self, amount: float) -> None:
        # TODO: Implement withdraw with validation and insufficient funds check
        raise NotImplementedError("TODO: Implement SecureWallet.withdraw")

    def get_transaction_count(self) -> int:
        # TODO: Return number of ledger entries
        raise NotImplementedError("TODO: Implement SecureWallet.get_transaction_count")


# ============================================================================
# AUTOMATED TEST SUITE
# ============================================================================

def run_tests():
    print("=" * 70)
    print("RUNNING AUTOMATED TEST SUITE FOR DAY 14 PRACTICE")
    print("=" * 70)
    score = 0
    total = 6

    # Test 1: Book Class
    try:
        b = Book("Clean Code", "Robert C. Martin", 464)
        assert str(b) == "Clean Code by Robert C. Martin (464 pages)", f"str got: {str(b)}"
        assert repr(b) == "Book(title='Clean Code', author='Robert C. Martin', pages=464)", f"repr got: {repr(b)}"
        print("✅ Task 1 Passed: Book __str__ and __repr__ formatted correctly.")
        score += 1
    except Exception as e:
        print(f"❌ Task 1 Failed: {e}")

    # Test 2: StudentTracker
    try:
        StudentTracker.total_enrolled = 0  # reset for test
        s1 = StudentTracker("Alice")
        s2 = StudentTracker("Bob")
        s1.enroll("Python AI")
        assert StudentTracker.total_enrolled == 2, "Class counter failed"
        assert s1.courses == ["Python AI"], f"s1 courses: {s1.courses}"
        assert s2.courses == [], f"s2 leaked courses: {s2.courses}"
        print("✅ Task 2 Passed: Class counter works and mutable lists are properly isolated.")
        score += 1
    except Exception as e:
        print(f"❌ Task 2 Failed: {e}")

    # Test 3: Vector2D from_polar
    try:
        v = Vector2D.from_polar(10.0, 0.0)
        assert v.x == 10.0 and v.y == 0.0, f"Polar 0 deg: got x={v.x}, y={v.y}"
        v90 = Vector2D.from_polar(10.0, 90.0)
        assert v90.x == 0.0 and v90.y == 10.0, f"Polar 90 deg: got x={v90.x}, y={v90.y}"
        print("✅ Task 3 Passed: Vector2D @classmethod factory works accurately.")
        score += 1
    except Exception as e:
        print(f"❌ Task 3 Failed: {e}")

    # Test 4: PasswordPolicy
    try:
        assert PasswordPolicy.is_strong("Secr3tPass") is True
        assert PasswordPolicy.is_strong("weak") is False  # Too short
        assert PasswordPolicy.is_strong("NodigitsHere") is False  # No digit
        assert PasswordPolicy.is_strong("alllower123") is False  # No uppercase
        print("✅ Task 4 Passed: PasswordPolicy static validation works.")
        score += 1
    except Exception as e:
        print(f"❌ Task 4 Failed: {e}")

    # Test 5: SmartThermostat
    try:
        th = SmartThermostat(20.0)
        assert th.temperature == 20.0
        assert th.fahrenheit == 68.0
        th.temperature = 25.0
        assert th.temperature == 25.0
        try:
            th.temperature = 40.0  # Should fail
            assert False, "Should have raised ValueError"
        except ValueError:
            pass
        print("✅ Task 5 Passed: SmartThermostat @property getter/setter validated bounds.")
        score += 1
    except Exception as e:
        print(f"❌ Task 5 Failed: {e}")

    # Test 6: SecureWallet
    try:
        w = SecureWallet(100.0)
        assert w.balance == 100.0
        w.deposit(50.0)
        assert w.balance == 150.0
        w.withdraw(30.0)
        assert w.balance == 120.0
        assert w.get_transaction_count() == 2
        try:
            w.withdraw(500.0)
            assert False, "Should raise ValueError on insufficient funds"
        except ValueError:
            pass
        # Check name mangling
        assert "_SecureWallet__balance" in w.__dict__
        print("✅ Task 6 Passed: SecureWallet private attributes and name mangling protected.")
        score += 1
    except Exception as e:
        print(f"❌ Task 6 Failed: {e}")

    print("=" * 70)
    print(f"TEST SCORE: {score}/{total} PASSED")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

"""
Day 14: Object-Oriented Programming (OOP) Part 1
Module 04: Encapsulation, Name Mangling, and the @property Decorator
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Encapsulation: Why data hiding and boundary protection matter.
2. The 3 Levels of Visibility in Python:
   - Public: `name`
   - Protected: `_internal_state` (Convention for developers)
   - Private: `__secret` (CPython Name Mangling: `_Class__secret`)
3. The Java Getter/Setter Anti-Pattern vs The Pythonic `@property`.
4. Property Lifecycle: Getter, Setter with Validation, and Deleter.
5. Read-Only Computed Properties (`@property` without setter).
6. Production Security Pattern: `APIKeyManager` with masked secrets & access audits.
"""

from typing import Optional
import datetime


# ============================================================================
# 1. THE THREE VISIBILITY LEVELS & NAME MANGLING
# ============================================================================
"""
DOES PYTHON HAVE TRUE PRIVATE VARIABLES?
- No! Python follows the philosophy: "We are all consenting adults here."
- Python does not have compiler-enforced `private` keywords like C++ or Java.
- Instead, Python uses conventions and runtime NAME MANGLING:
    1. Public (`name`): Free for all callers to read and modify.
    2. Protected (`_name`): Single leading underscore. Signals: "Internal detail, do not touch outside the class!"
    3. Private (`__name`): Double leading underscore. CPython automatically transforms
       the identifier at compile time to:
           `_ClassName__name`
       This prevents accidental overriding in subclasses!
"""

print("=" * 70)
print("1. PUBLIC, PROTECTED, AND PRIVATE (NAME MANGLING)")
print("=" * 70)

class AccountSecurityDemo:
    def __init__(self, username: str, user_id: int, secret_token: str) -> None:
        self.username = username             # Public
        self._user_id = user_id             # Protected (Convention)
        self.__secret_token = secret_token   # Private (Name Mangled)

acc = AccountSecurityDemo("sapna_ai", 101, "tok_super_secret_994")

print(f"Public attribute:    acc.username = {acc.username}")
print(f"Protected attribute: acc._user_id = {acc._user_id} (Allowed, but frowned upon)")

# Trying to access __secret_token directly raises AttributeError:
try:
    print(acc.__secret_token)
except AttributeError as e:
    print(f"Direct Private access failed: AttributeError ('{e}')")

# Demystifying Name Mangling: CPython renamed it to `_AccountSecurityDemo__secret_token`
print(f"Mangled attribute in __dict__: {acc.__dict__.keys()}")
print(f"Accessing via mangled name:    {acc._AccountSecurityDemo__secret_token}")


# ============================================================================
# 2. THE PYTHONIC WAY: `@property` GETTERS & SETTERS
# ============================================================================
"""
THE OLD (JAVA-STYLE) WAY:
    class BankAccount:
        def get_balance(self): return self._balance
        def set_balance(self, value): ...
Ugly syntax: `account.set_balance(account.get_balance() + 100)`!

THE PYTHONIC WAY:
Use the `@property` decorator!
Allows callers to access methods with clean attribute syntax:
    account.balance += 100  # Looks like variable assignment, but triggers validation!
"""

print("\n" + "=" * 70)
print("2. THE `@property` GETTER AND SETTER WITH VALIDATION")
print("=" * 70)

class BankAccount:
    def __init__(self, owner: str, initial_deposit: float = 0.0) -> None:
        self.owner = owner
        self._balance: float = 0.0
        # Trigger validation through the setter
        self.balance = initial_deposit

    # 1. Getter
    @property
    def balance(self) -> float:
        """Returns the current account balance."""
        return self._balance

    # 2. Setter with strict business logic validation
    @balance.setter
    def balance(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a numerical value.")
        if amount < 0:
            raise ValueError(f"Insufficient funds or negative deposit: ${amount:.2f} rejected.")
        self._balance = float(amount)

    # 3. Read-Only Computed Property (No setter!)
    @property
    def account_summary(self) -> str:
        return f"Account[{self.owner}]: Balance = ${self._balance:,.2f}"


my_acc = BankAccount("Sapna", 500.0)
print(f"Initial: {my_acc.account_summary}")

# Clean attribute syntax triggers the setter method under the hood:
my_acc.balance = 750.50
print(f"Updated: Balance = ${my_acc.balance:.2f}")

# Attempting negative balance triggers validation exception:
try:
    my_acc.balance = -100.0
except ValueError as e:
    print(f"🛡️  Validation Guard Caught: {e}")

# Attempting to assign to a read-only property raises AttributeError:
try:
    my_acc.account_summary = "Hacked Summary"
except AttributeError as e:
    print(f"🛡️  Read-Only Guard Caught: Cannot overwrite computed property ('{e}')")


# ============================================================================
# 3. PRODUCTION PATTERN: SECURE API KEY MANAGER
# ============================================================================
"""
Production AI backend pattern: Managing sensitive credentials (OpenAI / Gemini API keys).
- Masking keys on output: `sk-****1234`
- Requiring valid prefixes (`sk-` or `AIza`)
- Audit timestamps for key rotations
"""

print("\n" + "=" * 70)
print("3. PRODUCTION SECURITY PATTERN: `APIKeyManager`")
print("=" * 70)

class APIKeyManager:
    """Manages sensitive API credentials with validation, masking, and audit trails."""
    def __init__(self, service_name: str, raw_key: str) -> None:
        self.service_name = service_name
        self._key: str = ""
        self._last_rotated: Optional[datetime.datetime] = None
        # Use property setter for initial validation
        self.key = raw_key

    @property
    def key(self) -> str:
        """Getter returns the masked key for safe logging and UI display."""
        if len(self._key) <= 8:
            return "********"
        return f"{self._key[:4]}****{self._key[-4:]}"

    def get_raw_key_for_authorization(self) -> str:
        """Explicit, auditable method for raw HTTP Authorization headers."""
        return self._key

    @key.setter
    def key(self, new_key: str) -> None:
        new_key = new_key.strip()
        if len(new_key) < 16:
            raise ValueError("API Key must be at least 16 characters long.")
        if not (new_key.startswith("sk-") or new_key.startswith("AIza")):
            raise ValueError("Invalid API Key format: must start with 'sk-' or 'AIza'.")

        self._key = new_key
        self._last_rotated = datetime.datetime.now()
        print(f"  🔐 [KEY ROTATED] Service='{self.service_name}' key updated at {self._last_rotated.strftime('%H:%M:%S')}")


# Usage
sec_key = APIKeyManager("Gemini-Production", "AIzaSyB1234567890abcdefXYZ")

print(f"Masked Key for display:     {sec_key.key}")
print(f"Raw Key for HTTP Request:   {sec_key.get_raw_key_for_authorization()[:10]}...")

try:
    sec_key.key = "weak_insecure_key"
except ValueError as err:
    print(f"  ❌ Invalid Key Rejected: {err}")

print("\n" + "=" * 70)
print("DAY 14 MODULE 04: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

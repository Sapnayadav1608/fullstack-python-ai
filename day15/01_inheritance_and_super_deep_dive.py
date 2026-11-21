"""
Day 15: Advanced Object-Oriented Programming (OOP) Part 2
Module 01: Inheritance Types, `super()` Under the Hood & Method Resolution
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Inheritance Fundamentals: DRY principle, 'is-a' relationships vs composition ('has-a').
2. Inheritance Varieties: Single, Multi-level, and Hierarchical.
3. Demystifying `super()`: Why it is NOT just "call parent", but an MRO proxy!
4. Cooperative Initialization using `super().__init__(*args, **kwargs)`.
5. Method Overriding & Extending Parent Functionality.
6. Production AI Example: Base `AIModelClient` extended into `FineTunedGeminiClient`.
"""

from typing import Dict, Any, List, Optional
import time


# ============================================================================
# 1. INHERITANCE FUNDAMENTALS: SINGLE & MULTI-LEVEL
# ============================================================================
"""
WHAT IS INHERITANCE?
- A mechanism where a child class (subclass) inherits attributes and methods
  from a parent class (superclass/base class).
- Models an "is-a" relationship: A `Developer` is a `Person`; a `GeminiModel` is an `AIModel`.
- Eliminates redundant code and establishes polymorphic contracts.
"""

print("=" * 70)
print("1. SINGLE & MULTI-LEVEL INHERITANCE WITH super()")
print("=" * 70)

class BaseEntity:
    """Root entity providing audit timestamps."""
    def __init__(self, entity_id: str) -> None:
        self.entity_id = entity_id
        self.created_at = time.strftime("%Y-%m-%d %H:%M:%S")

    def get_audit_info(self) -> str:
        return f"[ID: {self.entity_id} | Created: {self.created_at}]"


class User(BaseEntity):
    """Subclass inheriting from BaseEntity (Single Inheritance)."""
    def __init__(self, entity_id: str, username: str, email: str) -> None:
        # Delegate initialization to BaseEntity via super()
        super().__init__(entity_id=entity_id)
        self.username = username
        self.email = email

    def describe(self) -> str:
        return f"User '{self.username}' <{self.email}> - {self.get_audit_info()}"


class AdminUser(User):
    """Subclass inheriting from User (Multi-Level Inheritance: AdminUser -> User -> BaseEntity)."""
    def __init__(self, entity_id: str, username: str, email: str, access_tier: int = 1) -> None:
        super().__init__(entity_id=entity_id, username=username, email=email)
        self.access_tier = access_tier

    # Method Overriding: Extend parent describe() with admin privileges
    def describe(self) -> str:
        base_desc = super().describe()
        return f"🛡️  [ADMIN TIER {self.access_tier}] {base_desc}"


admin = AdminUser("usr_9901", "sapna_admin", "sapna@ai.org", access_tier=3)
print(admin.describe())
print(f"Is instance of AdminUser? {isinstance(admin, AdminUser)}")
print(f"Is instance of User?      {isinstance(admin, User)}")
print(f"Is instance of BaseEntity?{isinstance(admin, BaseEntity)}")


# ============================================================================
# 2. HOW `super()` WORKS UNDER THE HOOD
# ============================================================================
"""
COMMON MISCONCEPTION:
"super() simply calls the parent class." -> WRONG!
In Python 3, `super()` returns a proxy object that delegates attribute lookups
to the NEXT class in the Method Resolution Order (MRO) of the current instance!
Syntax: `super()` in Python 3 is equivalent to `super(CurrentClass, self)`.
"""

print("\n" + "=" * 70)
print("2. `super()` MRO PROXY DEMONSTRATION")
print("=" * 70)

print(f"AdminUser MRO: {[cls.__name__ for cls in AdminUser.__mro__]}")
# MRO: ['AdminUser', 'User', 'BaseEntity', 'object']
# When AdminUser calls super().describe(), it resolves to User.describe.
# When User calls super().__init__(), it resolves to BaseEntity.__init__.


# ============================================================================
# 3. PRODUCTION AI PATTERN: `AIModelClient` HIERARCHY
# ============================================================================
"""
Enterprise pattern in AI platforms:
- Base class manages authentication, HTTP session, and retry policies.
- Specialized subclasses configure model parameters, adapters, and prompt formats.
"""

print("\n" + "=" * 70)
print("3. PRODUCTION PATTERN: EXTENDING AI CLIENT ARCHITECTURE")
print("=" * 70)

class AIModelClient:
    """Base class for all remote LLM API providers."""
    def __init__(self, api_key: str, base_url: str, timeout_sec: int = 30) -> None:
        self._api_key = api_key
        self.base_url = base_url
        self.timeout_sec = timeout_sec

    def authenticate_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key[:4]}****{self._api_key[-4:]}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Base generation logic with logging."""
        print(f"  [API REQUEST] Sending prompt to {self.base_url} (timeout={self.timeout_sec}s)...")
        return {"status": "SUCCESS", "raw_output": f"Output for '{prompt}'"}


class FineTunedGeminiClient(AIModelClient):
    """Subclass specialized for fine-tuned LoRA Gemini endpoints with custom parameters."""
    def __init__(
        self,
        api_key: str,
        adapter_model_id: str,
        temperature: float = 0.2,
        top_p: float = 0.95
    ) -> None:
        # Initialize base AIModelClient with Gemini's base endpoint
        super().__init__(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta",
            timeout_sec=45
        )
        self.adapter_model_id = adapter_model_id
        self.temperature = temperature
        self.top_p = top_p

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Overrides base generate to inject adapter parameters and temperature."""
        print(f"  [FineTuned Adapter: {self.adapter_model_id}] Injecting temp={self.temperature}, top_p={self.top_p}")
        # Call base class generate logic
        response = super().generate(prompt, **kwargs)
        response["adapter_applied"] = self.adapter_model_id
        response["temperature"] = self.temperature
        return response


# Testing our production inheritance
gemini_finetuned = FineTunedGeminiClient(
    api_key="AIzaSyB1234567890abcdefXYZ",
    adapter_model_id="adapter-finance-lora-v2",
    temperature=0.1
)

print(f"Headers: {gemini_finetuned.authenticate_headers()}")
output = gemini_finetuned.generate("Summarize Q3 Financial Report")
print(f"Output payload: {output}")

print("\n" + "=" * 70)
print("DAY 15 MODULE 01: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

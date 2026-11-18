"""
Day 14: Object-Oriented Programming (OOP) Part 1
Module 01: Classes, Objects, The `self` Mechanism, and Introspection
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Procedural vs Object-Oriented Paradigm: Why OOP matters in production.
2. The Class Blueprint vs Object Instance in memory (`id()`, `type()`, `isinstance()`).
3. The Instantiation Lifecycle: `__new__` (allocator) vs `__init__` (initializer).
4. The `self` Parameter Demystified: How CPython translates `p.drive()` to `Car.drive(p)`.
5. Object String Representation: `__str__` (user) vs `__repr__` (developer debug).
6. Production AI Example: `LLMPromptTemplate` class managing variable substitution & token counts.
"""

from typing import Dict, Any, List


# ============================================================================
# 1. PROCEDURAL VS OBJECT-ORIENTED PROGRAMMING
# ============================================================================
"""
PROCEDURAL:
- Code is organized around functions that operate on separate data structures (dicts, tuples).
- High risk of data mutation from outside, loose contracts, difficult to scale.

OBJECT-ORIENTED PROGRAMMING (OOP):
- Bundles DATA (attributes) and BEHAVIOR (methods) together into a single unit called an OBJECT.
- Promotes modularity, reusability, and encapsulation.
"""

print("=" * 70)
print("1. CLASS BLUEPRINT VS OBJECT INSTANCE")
print("=" * 70)

class Developer:
    """Blueprint for creating software developer profiles."""
    def __init__(self, name: str, role: str, experience_years: int) -> None:
        # Attributes attached directly to this specific instance
        self.name = name
        self.role = role
        self.experience_years = experience_years

    def introduce(self) -> str:
        return f"Hi! I'm {self.name}, working as a {self.role} with {self.experience_years} years of experience."

# Instantiating objects (Instances of the Developer class)
dev1 = Developer("Sapna", "AI Engineer", 2)
dev2 = Developer("Alex", "Backend Architect", 6)

print(f"dev1 Object: {dev1}")
print(f"dev1 Memory Address (id): {hex(id(dev1))}")
print(f"dev2 Memory Address (id): {hex(id(dev2))}")
print(f"Type check: {type(dev1)} | Is instance of Developer? {isinstance(dev1, Developer)}")
print(f"Calling method: {dev1.introduce()}")


# ============================================================================
# 2. THE `self` PARAMETER DEMYSTIFIED
# ============================================================================
"""
WHAT IS `self`?
- In Python, `self` is NOT a keyword! (It is simply a universally accepted convention).
- `self` refers to the specific instance of the class that is invoking the method.
- When you call:
      dev1.introduce()
  CPython automatically transforms it behind the scenes into:
      Developer.introduce(dev1)
  The instance `dev1` is passed as the first argument!
"""

print("\n" + "=" * 70)
print("2. HOW CPYTHON HANDLES `self` UNDER THE HOOD")
print("=" * 70)

# Syntax A: Method call on instance (Syntactic sugar)
call_a = dev1.introduce()

# Syntax B: Unbound method call passing instance explicitly (CPython under-the-hood)
call_b = Developer.introduce(dev1)

print(f"Method via dev1.introduce():     {call_a}")
print(f"Method via Developer.introduce(dev1): {call_b}")
print(f"Are both calls 100% equivalent?  {call_a == call_b}")


# ============================================================================
# 3. OBJECT INSTANTIATION: `__new__` VS `__init__`
# ============================================================================
"""
Many beginners think `__init__` is the constructor. It is NOT!
- `__new__(cls, ...)`: The TRUE Constructor. Allocates raw memory and returns a new object instance.
- `__init__(self, ...)`: The Initializer. Takes the newly created instance and initializes its attributes.
"""

print("\n" + "=" * 70)
print("3. LIFECYCLE: `__new__` (ALLOCATION) VS `__init__` (INITIALIZATION)")
print("=" * 70)

class LifecycleDemo:
    def __new__(cls, *args, **kwargs):
        print("  1. [__new__] Allocating raw memory for new instance...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, label: str) -> None:
        print(f"  2. [__init__] Initializing attributes for {label}...")
        self.label = label

obj = LifecycleDemo("Service Alpha")
print(f"  3. Object fully initialized: label='{obj.label}'")


# ============================================================================
# 4. STRING REPRESENTATION: `__str__` VS `__repr__`
# ============================================================================
"""
GOLDEN RULE:
- `__str__`: Readable string for end users (`print(obj)`, `str(obj)`).
- `__repr__`: Unambiguous, technical developer string for debugging and REPL.
  Ideal goal: `eval(repr(obj)) == obj` (if practical).
- If `__str__` is not defined, Python automatically falls back to `__repr__`.
"""

print("\n" + "=" * 70)
print("4. `__str__` VS `__repr__`")
print("=" * 70)

class AIModelCard:
    def __init__(self, model_id: str, context_window: int, provider: str) -> None:
        self.model_id = model_id
        self.context_window = context_window
        self.provider = provider

    def __repr__(self) -> str:
        # Developer debug format (matches object reconstruction)
        return f"AIModelCard(model_id={self.model_id!r}, context_window={self.context_window}, provider={self.provider!r})"

    def __str__(self) -> str:
        # Pretty human-facing format
        return f"🤖 Model [{self.model_id}] by {self.provider} ({self.context_window:,} tokens context)"

gemini = AIModelCard("gemini-1.5-pro", 1_000_000, "Google DeepMind")

print(f"str(gemini):  {str(gemini)}")
print(f"repr(gemini): {repr(gemini)}")


# ============================================================================
# 5. PRODUCTION AI PATTERN: `LLMPromptTemplate` CLASS
# ============================================================================
"""
Real-world AI application: Encapsulating system instructions, prompt templates,
variable injection, and token estimation in a reusable class.
"""

print("\n" + "=" * 70)
print("5. PRODUCTION AI PATTERN: `LLMPromptTemplate`")
print("=" * 70)

class LLMPromptTemplate:
    """Encapsulates system instructions and variable templating for AI API calls."""
    def __init__(self, system_role: str, template: str) -> None:
        self.system_role = system_role.strip()
        self.template = template.strip()

    def format(self, **kwargs: Any) -> Dict[str, str]:
        """Substitutes variables into the prompt template safely."""
        try:
            formatted_user_prompt = self.template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required template parameter: {e}")

        return {
            "system": self.system_role,
            "user": formatted_user_prompt
        }

    def estimate_token_count(self, **kwargs: Any) -> int:
        """Approximates total token usage (rough rule: 1 token ~ 4 characters)."""
        payload = self.format(**kwargs)
        total_chars = len(payload["system"]) + len(payload["user"])
        return max(1, total_chars // 4)

    def __repr__(self) -> str:
        return f"LLMPromptTemplate(role={self.system_role[:20]!r}..., template_len={len(self.template)})"


# Using our AI class in practice
summarizer_template = LLMPromptTemplate(
    system_role="You are an expert full-stack code reviewer and AI engineer.",
    template="Please analyze the following {language} snippet for efficiency:\n\n```{language}\n{code}\n```"
)

ai_payload = summarizer_template.format(
    language="python",
    code="numbers = (x * 2 for x in range(100_000))"
)

tokens = summarizer_template.estimate_token_count(
    language="python",
    code="numbers = (x * 2 for x in range(100_000))"
)

print(f"System Message: {ai_payload['system']}")
print(f"User Prompt:\n{ai_payload['user']}")
print(f"Estimated Tokens: {tokens} tokens")

print("\n" + "=" * 70)
print("DAY 14 MODULE 01: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

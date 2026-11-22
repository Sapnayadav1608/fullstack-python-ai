"""
================================================================================
DAY 16: PYTHON DATA MODEL & MAGIC METHODS (PART 1)
Module 01: Object Representation & String Protocols
================================================================================
Topics Covered:
  1. The Fundamental Duality: __repr__ vs __str__ (Devs vs End-Users)
  2. The Fallback Mechanism & Golden Rule: eval(repr(obj)) == obj
  3. Custom Format Specifiers with __format__ (f-string customization)
  4. Binary Protocol with __bytes__ for Network & Hashing
  5. Truth Value Testing: __bool__ vs __len__ Fallback Hierarchy
  6. Enterprise AI Pattern: LLMResponseEnvelope with Custom String Protocols
================================================================================
"""

import datetime
from typing import Any, Dict, Optional


# ==============================================================================
# SECTION 1: THE FUNDAMENTAL DUALITY — __repr__ vs __str__
# ==============================================================================
# In Python's Data Model:
# - __repr__: Unambiguous, formal string. Aimed at developers, debuggers, and logs.
#   Ideal goal: eval(repr(obj)) == obj (can recreate the object).
# - __str__: Readable, user-friendly string. Aimed at UI, end users, or simple printing.
# - If __str__ is NOT implemented, Python automatically falls back to __repr__.
# - If __repr__ is NOT implemented, Python falls back to object.__repr__ (e.g., <... at 0x...>).

class ModelCheckpointWithoutDunders:
    """Class without custom string representations (ugly default behavior)."""
    def __init__(self, step: int, loss: float):
        self.step = step
        self.loss = loss


class ModelCheckpoint:
    """Production checkpoint with explicit, unambiguous representations."""
    def __init__(self, step: int, loss: float, model_name: str = "gemini-1.5-flash"):
        self.step = step
        self.loss = loss
        self.model_name = model_name
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)

    def __repr__(self) -> str:
        """Formal representation: looks like a valid Python constructor call."""
        return (
            f"ModelCheckpoint(step={self.step!r}, "
            f"loss={self.loss!r}, "
            f"model_name={self.model_name!r})"
        )

    def __str__(self) -> str:
        """User-friendly representation for terminal dashboards and progress logs."""
        return f"[{self.model_name}] Step {self.step:,} | Validation Loss: {self.loss:.4f}"


def demonstrate_repr_vs_str():
    print("=" * 70)
    print("SECTION 1: __repr__ vs __str__ DUALITY")
    print("=" * 70)

    raw = ModelCheckpointWithoutDunders(1000, 0.2451)
    print(f"Default str(raw):  {str(raw)}")
    print(f"Default repr(raw): {repr(raw)}")

    ckpt = ModelCheckpoint(15000, 0.0842, "llama-3-8b")
    print(f"\nCustom str(ckpt):  {str(ckpt)}")
    print(f"Custom repr(ckpt): {repr(ckpt)}")

    # Verification of eval(repr(obj)) == obj pattern:
    recreated = eval(repr(ckpt))
    print(f"\nRecreated via eval(repr()): {recreated}")
    print(f"Types match: {type(recreated) is type(ckpt)}")
    print(f"Attributes match: step={recreated.step}, loss={recreated.loss}")


# ==============================================================================
# SECTION 2: CUSTOM FORMAT SPECIFIERS WITH __format__
# ==============================================================================
# When you write f"{val:specifier}", Python calls type(val).__format__(val, specifier).
# By default, object.__format__ forwards to __str__. Overriding it enables custom
# domain-specific formatting syntax (e.g. currency, token stats, percentages).

class TokenMetric:
    """Tracks token consumption with domain-specific format specifiers."""
    def __init__(self, count: int, cost_per_1k: float = 0.002):
        self.count = count
        self.cost_per_1k = cost_per_1k

    @property
    def total_cost(self) -> float:
        return (self.count / 1000.0) * self.cost_per_1k

    def __format__(self, format_spec: str) -> str:
        """
        Supported format specifiers:
          - '' (empty): default count with comma separator
          - 'k': thousands notation (e.g., '12.5k')
          - 'm': millions notation (e.g., '1.20M')
          - 'usd': currency value formatted with dollar sign ($0.025)
          - 'inr': Indian rupee formatted (approx 84 INR/USD)
        """
        if not format_spec:
            return f"{self.count:,} tokens"
        
        spec = format_spec.strip().lower()
        if spec == "k":
            return f"{self.count / 1_000:.1f}k tokens"
        elif spec == "m":
            return f"{self.count / 1_000_000:.2f}M tokens"
        elif spec == "usd":
            return f"${self.total_cost:.4f} USD"
        elif spec == "inr":
            return f"₹{self.total_cost * 84.50:.2f} INR"
        else:
            # Fall back to standard numeric formatting on the count
            try:
                return format(self.count, format_spec)
            except ValueError:
                return f"{self.count} tokens (unknown spec: {format_spec})"


def demonstrate_format_protocol():
    print("\n" + "=" * 70)
    print("SECTION 2: CUSTOM FORMAT SPECIFIERS VIA __format__")
    print("=" * 70)

    metric = TokenMetric(count=1_450_800, cost_per_1k=0.0015)

    print(f"Default:        {metric}")
    print(f"Specifier ':k': {metric:k}")
    print(f"Specifier ':m': {metric:m}")
    print(f"Specifier ':usd': {metric:usd}")
    print(f"Specifier ':inr': {metric:inr}")
    print(f"Standard int ':012d': {metric:012d}")


# ==============================================================================
# SECTION 3: BINARY PROTOCOL VIA __bytes__
# ==============================================================================
# Python provides bytes(obj) which invokes __bytes__().
# Crucial for low-level socket transmissions, caching keys, or hashing payloads.

class SecureAPIKey:
    """Represents an API key with raw binary wire serialization."""
    def __init__(self, key_id: str, secret: str):
        self.key_id = key_id
        self.secret = secret

    def __bytes__(self) -> bytes:
        """Packs key_id and secret into UTF-8 encoded wire format."""
        raw_payload = f"{self.key_id}:{self.secret}"
        return raw_payload.encode("utf-8")

    def __repr__(self) -> str:
        # Never leak secrets in __repr__! Mask secret for security
        masked = self.secret[:4] + "*" * (len(self.secret) - 4) if len(self.secret) > 4 else "***"
        return f"SecureAPIKey(key_id={self.key_id!r}, secret={masked!r})"


def demonstrate_bytes_protocol():
    print("\n" + "=" * 70)
    print("SECTION 3: BINARY PROTOCOL VIA __bytes__")
    print("=" * 70)

    auth = SecureAPIKey("usr_prod_99", "sk_live_9876543210abcdef")
    print(f"Repr (Safe):  {auth}")
    
    wire_bytes = bytes(auth)
    print(f"Raw bytes:    {wire_bytes}")
    print(f"Byte Length:  {len(wire_bytes)} bytes")
    print(f"Decoded back: {wire_bytes.decode('utf-8')}")


# ==============================================================================
# SECTION 4: TRUTH VALUE TESTING — __bool__ vs __len__
# ==============================================================================
# In Python, an instance is evaluated in an if-statement using the following rule:
#   1. If __bool__() is defined, Python calls it (must return True or False).
#   2. If __bool__() is NOT defined, Python checks for __len__().
#      If __len__() returns 0, the object is Falsy; otherwise Truthy.
#   3. If neither is defined, the object is ALWAYS Truthy!

class ModelInferenceState:
    """Evaluates Truthiness based on whether inference generated an output."""
    def __init__(self, output: Optional[str] = None, error: Optional[str] = None):
        self.output = output
        self.error = error

    def __bool__(self) -> bool:
        """Truthy ONLY if inference succeeded without errors and produced text."""
        return bool(self.output and not self.error)


class TokenBuffer:
    """Evaluates Truthiness via __len__ fallback."""
    def __init__(self):
        self.tokens = []

    def __len__(self) -> int:
        return len(self.tokens)


def demonstrate_truth_value_testing():
    print("\n" + "=" * 70)
    print("SECTION 4: TRUTH VALUE TESTING (__bool__ vs __len__)")
    print("=" * 70)

    s1 = ModelInferenceState(output="Machine Learning is fascinating.", error=None)
    s2 = ModelInferenceState(output=None, error="RateLimitExceeded")
    s3 = ModelInferenceState(output="", error=None)

    print(f"s1 (Has text, no error): bool(s1) = {bool(s1)}")
    print(f"s2 (Error occurred):    bool(s2) = {bool(s2)}")
    print(f"s3 (Empty text):        bool(s3) = {bool(s3)}")

    # Verification in if conditionals:
    if s1:
        print("  -> s1 passed conditional check cleanly!")
    if not s2:
        print("  -> s2 cleanly evaluated to Falsy as expected!")

    # Fallback to __len__:
    buf = TokenBuffer()
    print(f"\nEmpty TokenBuffer: bool(buf) = {bool(buf)} (due to len={len(buf)})")
    buf.tokens.append("token_101")
    print(f"Populated TokenBuffer: bool(buf) = {bool(buf)} (due to len={len(buf)})")


# ==============================================================================
# SECTION 5: ENTERPRISE AI PATTERN — LLMResponseEnvelope
# ==============================================================================
class LLMResponseEnvelope:
    """
    Enterprise LLM API response container integrating all string & representation protocols:
      - __repr__: Full reproducible diagnostic dump.
      - __str__: Clean text output for chat display.
      - __format__: Precision routing ('tokens', 'cost', 'latency', 'json').
      - __bool__: Truthy only on HTTP 200 / successful completion.
    """
    def __init__(
        self,
        prompt: str,
        response_text: str,
        model: str,
        total_tokens: int,
        latency_ms: float,
        status_code: int = 200
    ):
        self.prompt = prompt
        self.response_text = response_text
        self.model = model
        self.total_tokens = total_tokens
        self.latency_ms = latency_ms
        self.status_code = status_code

    def __repr__(self) -> str:
        return (
            f"LLMResponseEnvelope("
            f"prompt={self.prompt!r}, "
            f"response_text={self.response_text[:30] + '...'!r}, "
            f"model={self.model!r}, "
            f"total_tokens={self.total_tokens!r}, "
            f"latency_ms={self.latency_ms!r}, "
            f"status_code={self.status_code!r})"
        )

    def __str__(self) -> str:
        return self.response_text

    def __format__(self, format_spec: str) -> str:
        spec = format_spec.strip().lower()
        if spec == "tokens":
            return f"{self.total_tokens:,} tokens"
        elif spec == "latency":
            return f"{self.latency_ms:.1f}ms"
        elif spec == "cost":
            cost = (self.total_tokens / 1000) * 0.0015
            return f"${cost:.5f}"
        elif spec == "summary":
            return f"[{self.model}] {self.total_tokens} toks in {self.latency_ms:.0f}ms (Status: {self.status_code})"
        return self.response_text

    def __bool__(self) -> bool:
        return self.status_code == 200 and bool(self.response_text.strip())


def demonstrate_enterprise_ai_envelope():
    print("\n" + "=" * 70)
    print("SECTION 5: ENTERPRISE AI PATTERN — LLMResponseEnvelope")
    print("=" * 70)

    envelope = LLMResponseEnvelope(
        prompt="Explain C3 Linearization in 2 sentences.",
        response_text="C3 Linearization guarantees deterministic Method Resolution Order (MRO) in Python. It enforces monotonicity and preserves local precedence order across multiple inheritance hierarchies.",
        model="claude-3-5-sonnet",
        total_tokens=142,
        latency_ms=342.8
    )

    print(f"[__str__ directly]:\n{envelope}\n")
    print(f"[__repr__ for logs]:\n{envelope!r}\n")
    print(f"[Formatted :tokens]:  {envelope:tokens}")
    print(f"[Formatted :latency]: {envelope:latency}")
    print(f"[Formatted :cost]:    {envelope:cost}")
    print(f"[Formatted :summary]: {envelope:summary}")
    print(f"[Truthy Check]:       Success = {bool(envelope)}")


if __name__ == "__main__":
    demonstrate_repr_vs_str()
    demonstrate_format_protocol()
    demonstrate_bytes_protocol()
    demonstrate_truth_value_testing()
    demonstrate_enterprise_ai_envelope()

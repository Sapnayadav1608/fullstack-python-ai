"""
===============================================================================
Day 17: Module 02 - Exception Chaining, Context & Traceback Engineering
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Mastering PEP 3134 (__cause__, __context__, and 'from None')
Architecture: Production-Grade Diagnostic Preserving for AI Systems
===============================================================================

In mission-critical AI backend pipelines, exceptions rarely happen in isolation.
When an LLM API call fails due to a network timeout, socket drop, or payload
decoding error, naive exception handling either:
  1. Leaks low-level socket details to the API consumer, exposing infrastructure.
  2. Or worse: completely erases the original traceback, leaving Sentry/Datadog
     engineers with zero clue why the upstream connection dropped.

PEP 3134 introduced Exception Chaining to solve this with mathematical elegance.
This module covers:
  1. Implicit Context (__context__): What happens when an exception occurs inside
     an except block.
  2. Explicit Chaining ('raise ... from original_error'): Setting __cause__ for
     unambiguous causality.
  3. Suppressing Context ('raise ... from None'): Eliminating noisy or sensitive
     internal tracebacks for clean, public-facing APIs.
  4. Programmatic Traceback Introspection: Inspecting the chain using the `traceback`
     module for telemetry and automated retry routing.
  5. Enterprise AI Gateway Pattern: Converting raw socket/HTTP failures into clean,
     domain-level AI exceptions while preserving debugging provenance.
"""

from __future__ import annotations
import json
import time
import traceback
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Optional


# ============================================================================
# SECTION 1: IMPLICIT EXCEPTION CONTEXT (__context__)
# ============================================================================
print("=" * 75)
print("SECTION 1: IMPLICIT CONTEXT (__context__) — ACCIDENTAL NESTING")
print("=" * 75)

def simulate_implicit_context_trap():
    """
    When an exception is raised while handling another exception, Python
    automatically sets `__context__` on the second exception to point to the first.
    Python displays: "During handling of the above exception, another exception occurred".
    """
    try:
        # Step 1: Low-level error occurs
        raw_config = '{"temperature": 0.7, "max_tokens": }'  # Invalid JSON
        json.loads(raw_config)
    except json.JSONDecodeError as err:
        # Step 2: While handling, a secondary error occurs (e.g. bad fallback logic)
        print(f"  [Implicit Context Demo] Caught initial JSONDecodeError: {err.msg}")
        try:
            # Bug: Trying to read an unset environment variable or missing dict key
            fallback_store: Dict[str, Any] = {}
            _ = fallback_store["default_config"]
        except KeyError as secondary_err:
            print(f"  [Secondary Error] Caught KeyError: {secondary_err}")
            print(f"  -> secondary_err.__context__ is original JSONDecodeError? "
                  f"{isinstance(secondary_err.__context__, json.JSONDecodeError)}")
            return secondary_err

implicit_err = simulate_implicit_context_trap()
assert implicit_err is not None and implicit_err.__context__ is not None


# ============================================================================
# SECTION 2: EXPLICIT CHAINING ('raise ... from err') & __cause__
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: EXPLICIT CHAINING ('raise ... from err') & __cause__")
print("=" * 75)

class AIInferenceError(Exception):
    """Domain-level error representing an AI model inference failure."""
    def __init__(self, message: str, model_id: str, latency_ms: float):
        super().__init__(message)
        self.model_id = model_id
        self.latency_ms = latency_ms


def call_upstream_provider_with_explicit_chain(model_id: str, timeout_sec: float) -> str:
    """
    Explicit chaining connects the high-level domain error to the low-level cause.
    Syntax: `raise HighLevelError(...) from low_level_error`
    Sets: high_level_error.__cause__ = low_level_error
          high_level_error.__suppress_context__ = False
    Python displays: "The above exception was the direct cause of the following exception:"
    """
    start_time = time.perf_counter()
    try:
        # Simulate a low-level socket/connection timeout
        time.sleep(0.01)
        raise TimeoutError(f"TCP socket timed out after {timeout_sec}s connecting to api.provider.ai:443")
    except TimeoutError as low_level_err:
        elapsed = (time.perf_counter() - start_time) * 1000
        # Explicitly chain!
        raise AIInferenceError(
            message=f"Model '{model_id}' failed to respond within latency SLA",
            model_id=model_id,
            latency_ms=elapsed
        ) from low_level_err


try:
    call_upstream_provider_with_explicit_chain("gemini-1.5-pro", timeout_sec=2.0)
except AIInferenceError as exc:
    print(f"  Caught AIInferenceError: {exc}")
    print(f"  -> exc.__cause__: {type(exc.__cause__).__name__} -> {exc.__cause__}")
    print(f"  -> exc.__suppress_context__: {exc.__suppress_context__}")
    assert isinstance(exc.__cause__, TimeoutError)


# ============================================================================
# SECTION 3: SUPPRESSING CONTEXT ('raise ... from None')
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 3: SUPPRESSING CONTEXT ('raise ... from None') — API SANITIZATION")
print("=" * 75)

class PublicAPIKeyInvalidError(ValueError):
    """Clean public-facing exception without internal db/connection traces."""
    pass


def authenticate_user_request(api_key: str):
    """
    Security Best Practice:
    Never leak internal database connection strings, schema names, or driver
    tracebacks to external clients or client-facing logs.
    Using `raise CleanError(...) from None` sets:
      __cause__ = None
      __suppress_context__ = True
    This stops Python from displaying "During handling of the above exception..."!
    """
    try:
        # Simulate internal database/vault driver failure
        if not api_key.startswith("sk-live-"):
            raise ConnectionRefusedError(
                "Internal DB error: host=postgresql://admin:super_secret@10.0.4.12:5432/creds"
            )
    except ConnectionRefusedError:
        # Scrub the internal connection failure completely from public view
        raise PublicAPIKeyInvalidError(
            "Authentication failed: Invalid API Key format or credentials rejected."
        ) from None


try:
    authenticate_user_request("invalid_key_123")
except PublicAPIKeyInvalidError as sanitized_err:
    print(f"  Caught Sanitized Error: {sanitized_err}")
    print(f"  -> sanitized_err.__cause__: {sanitized_err.__cause__}")
    print(f"  -> sanitized_err.__suppress_context__: {sanitized_err.__suppress_context__}")
    # Formatted traceback will NOT display the postgres credentials!
    tb_str = "".join(traceback.format_exception(sanitized_err))
    assert "postgresql://admin:super_secret" not in tb_str
    print("  -> Security Verification: Database credentials successfully scrubbed from traceback!")


# ============================================================================
# SECTION 4: PROGRAMMATIC TRACEBACK INTROSPECTION & ROOT-CAUSE RESOLUTION
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 4: PROGRAMMATIC ROOT-CAUSE RESOLVER FOR INCIDENT RESPONSE")
print("=" * 75)

def get_root_cause(exc: BaseException) -> BaseException:
    """
    Traverse an exception chain all the way to its originating root cause.
    Follows `__cause__` first (explicit chaining), then `__context__` (implicit).
    Prevents cyclic reference infinite loops.
    """
    visited = set()
    current = exc
    while current is not None:
        visited.add(id(current))
        next_cause = current.__cause__ if current.__cause__ is not None else current.__context__
        if next_cause is None or id(next_cause) in visited:
            return current
        current = next_cause
    return exc


# Build a 3-layer deep nested exception chain
try:
    try:
        try:
            # Layer 0: Root cause
            raise ConnectionResetError("Remote peer forcibly closed socket fd=42")
        except ConnectionResetError as l0_err:
            # Layer 1: Network transport wrapper
            raise IOError("HTTP/2 stream dropped abruptly during model streaming") from l0_err
    except IOError as l1_err:
        # Layer 2: Domain gateway wrapper
        raise AIInferenceError("Gemini streaming session interrupted", "gemini-1.5-pro", 142.5) from l1_err
except AIInferenceError as top_level_err:
    root = get_root_cause(top_level_err)
    print(f"  Top-Level Exception: {type(top_level_err).__name__}: {top_level_err}")
    print(f"  Preserved Layer 1:   {type(top_level_err.__cause__).__name__}: {top_level_err.__cause__}")
    print(f"  Origin Root Cause:   {type(root).__name__}: {root}")
    assert isinstance(root, ConnectionResetError)


# ============================================================================
# SECTION 5: ENTERPRISE AI GATEWAY PATTERN — ROBUST CAUSE PRESERVATION
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 5: ENTERPRISE RESILIENT AI GATEWAY TRANSLATION")
print("=" * 75)

@dataclass
class GatewayTelemetry:
    request_id: str
    model: str
    original_error_class: str
    domain_error_class: str
    chain_type: str
    root_cause_message: str


class AIGateway:
    """
    Translates arbitrary low-level vendor errors (urllib, requests, httpx, socket)
    into standard domain exceptions while recording structured telemetry.
    """
    def __init__(self, model: str):
        self.model = model

    def execute_prompt(self, prompt: str, vendor_callable: Callable[[], str]) -> str:
        try:
            return vendor_callable()
        except TimeoutError as err:
            # Explicit chaining preserves latency SLA diagnosis
            raise AIInferenceError(
                f"Gateway timeout: Provider failed for model '{self.model}'",
                model_id=self.model,
                latency_ms=5000.0
            ) from err
        except PermissionError as err:
            # Sanitize security violation from internal logs
            raise PublicAPIKeyInvalidError("Gateway authorization rejected") from None
        except Exception as generic_err:
            # Wrap unknown exceptions preserving exact context
            raise AIInferenceError(
                f"Unexpected gateway failure while executing prompt: {str(generic_err)}",
                model_id=self.model,
                latency_ms=0.0
            ) from generic_err


gateway = AIGateway(model="gemini-1.5-pro")

# Test 1: Timeout with explicit cause
def failing_vendor_call():
    raise TimeoutError("Read timeout while streaming chunk #45")

try:
    gateway.execute_prompt("Analyze quarterly earnings", failing_vendor_call)
except AIInferenceError as e:
    telemetry = GatewayTelemetry(
        request_id="req_981a_23b",
        model=e.model_id,
        original_error_class=type(e.__cause__).__name__,
        domain_error_class=type(e).__name__,
        chain_type="explicit_cause (__cause__)",
        root_cause_message=str(e.__cause__)
    )
    print("  Emitted Telemetry Envelope:")
    print(f"  {json.dumps(telemetry.__dict__, indent=4)}")
    assert telemetry.original_error_class == "TimeoutError"

print("\n" + "=" * 75)
print("Module 02 Complete: Exception Chaining & Traceback Engineering Mastered!")
print("=" * 75)

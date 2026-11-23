"""
===============================================================================
Day 17: Hands-On Practice Workbook & Automated Test Suite
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Advanced Exception Handling, Custom Hierarchies & Defensive AI
6 Rigorous Challenges with Automated Self-Testing Runner
===============================================================================
"""

from __future__ import annotations
import sys
import time
from typing import Any, Callable, Dict, List, Optional, Tuple


# ============================================================================
# CHALLENGE 1: HIERARCHY CLASSIFIER
# ============================================================================
def classify_exception_category(exc: BaseException) -> str:
    """
    Classify an exception instance based on Python's exception inheritance tree.
    Returns:
      - "lookup"            if LookupError (KeyError, IndexError)
      - "arithmetic"        if ArithmeticError (ZeroDivisionError, OverflowError)
      - "system"            if (KeyboardInterrupt, SystemExit)
      - "generic_exception" if Exception (standard application errors)
      - "base_other"        for any other BaseException
    """
    if isinstance(exc, (KeyboardInterrupt, SystemExit)):
        return "system"
    elif isinstance(exc, LookupError):
        return "lookup"
    elif isinstance(exc, ArithmeticError):
        return "arithmetic"
    elif isinstance(exc, Exception):
        return "generic_exception"
    else:
        return "base_other"


# ============================================================================
# CHALLENGE 2: 4-CLAUSE LIFECYCLE (try / except / else / finally)
# ============================================================================
def safe_prompt_pipeline(raw_prompt: Any, max_chars: int) -> Dict[str, Any]:
    """
    Executes a defensive prompt validation pipeline using the full 4-clause lifecycle:
      - try: validates type and length.
      - except TypeError: sets status="type_error".
      - except ValueError: sets status="length_error".
      - else: sets status="ok" and calculates word_count.
      - finally: always sets pipeline_finalized=True and records completion timestamp.
    """
    envelope: Dict[str, Any] = {
        "status": "pending",
        "word_count": 0,
        "error_message": None,
        "pipeline_finalized": False,
    }

    try:
        if not isinstance(raw_prompt, str):
            raise TypeError(f"Prompt must be a string, received {type(raw_prompt).__name__}")
        if len(raw_prompt) > max_chars:
            raise ValueError(f"Prompt length {len(raw_prompt)} exceeds maximum {max_chars}")
    except TypeError as te:
        envelope["status"] = "type_error"
        envelope["error_message"] = str(te)
    except ValueError as ve:
        envelope["status"] = "length_error"
        envelope["error_message"] = str(ve)
    else:
        envelope["status"] = "ok"
        envelope["word_count"] = len(raw_prompt.split())
    finally:
        envelope["pipeline_finalized"] = True
        envelope["finalized_at"] = time.time()

    return envelope


# ============================================================================
# CHALLENGE 3: CUSTOM AI EXCEPTION HIERARCHY
# ============================================================================
class AIPlatformException(Exception):
    """Root base for all AI platform domain exceptions."""
    status_code: int = 500
    retryable: bool = False

    def __init__(self, message: str, request_id: str):
        super().__init__(message)
        self.message = message
        self.request_id = request_id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "status_code": self.status_code,
            "retryable": self.retryable,
            "request_id": self.request_id,
        }


class TokenQuotaExceeded(AIPlatformException):
    """Client error (400) raised when token threshold is passed."""
    status_code = 400
    retryable = False

    def __init__(self, current_tokens: int, max_tokens: int, request_id: str):
        self.current_tokens = current_tokens
        self.max_tokens = max_tokens
        self.overflow = current_tokens - max_tokens
        msg = f"Token count {current_tokens} exceeds quota {max_tokens} (+{self.overflow})"
        super().__init__(msg, request_id)

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["current_tokens"] = self.current_tokens
        data["max_tokens"] = self.max_tokens
        data["overflow"] = self.overflow
        return data


class RateLimitBackoff(AIPlatformException):
    """Server error (429) indicating client should back off and retry."""
    status_code = 429
    retryable = True

    def __init__(self, retry_after_sec: float, request_id: str):
        self.retry_after_sec = retry_after_sec
        msg = f"Rate limit reached. Back off for {retry_after_sec:.1f} seconds."
        super().__init__(msg, request_id)

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["retry_after_sec"] = self.retry_after_sec
        return data


# ============================================================================
# CHALLENGE 4: TRACEBACK SANITIZATION ('raise ... from None')
# ============================================================================
class PublicAPIError(Exception):
    """Sanitized public exception with zero internal credentials leaked."""
    pass


def sanitize_db_call(internal_func: Callable[[], Any]) -> Any:
    """
    Executes internal_func. If ConnectionError or PermissionError is raised,
    suppresses context and raises PublicAPIError from None.
    """
    try:
        return internal_func()
    except (ConnectionError, PermissionError):
        raise PublicAPIError("Sanitized API error: Service authentication failed.") from None


# ============================================================================
# CHALLENGE 5: EXPLICIT CAUSALITY PRESERVATION ('raise ... from err')
# ============================================================================
class GatewayInferenceError(Exception):
    """High-level gateway error that preserves underlying network failure."""
    def __init__(self, message: str, model_name: str):
        super().__init__(message)
        self.model_name = model_name


def wrap_llm_call(model_name: str, llm_func: Callable[[], str]) -> str:
    """
    Executes llm_func. If any Exception occurs, chains it explicitly
    into GatewayInferenceError setting __cause__.
    """
    try:
        return llm_func()
    except Exception as err:
        raise GatewayInferenceError(
            f"Gateway execution failed for model '{model_name}': {err}",
            model_name=model_name
        ) from err


# ============================================================================
# CHALLENGE 6: MULTI-PROVIDER FAILOVER WITH ExceptionGroup
# ============================================================================
def execute_waterfall(providers: List[Callable[[], str]]) -> str:
    """
    Tries each provider callable in sequential waterfall order.
    Returns the first successful response.
    If ALL providers fail, collects every individual exception and
    raises an ExceptionGroup("All providers failed", collected_errors).
    """
    errors: List[Exception] = []
    for provider in providers:
        try:
            return provider()
        except Exception as exc:
            errors.append(exc)

    raise ExceptionGroup(f"All {len(providers)} providers failed", errors)


# ============================================================================
# AUTOMATED TEST RUNNER
# ============================================================================
def run_tests():
    print("=" * 70)
    print("RUNNING DAY 17 AUTOMATED TEST SUITE — EXCEPTION ENGINEERING")
    print("=" * 70)

    # Test 1: Hierarchy Classifier
    assert classify_exception_category(KeyError("k")) == "lookup"
    assert classify_exception_category(IndexError("i")) == "lookup"
    assert classify_exception_category(ZeroDivisionError("z")) == "arithmetic"
    assert classify_exception_category(KeyboardInterrupt()) == "system"
    assert classify_exception_category(RuntimeError("r")) == "generic_exception"
    print("  [PASS] Challenge 1: classify_exception_category handles all branches")

    # Test 2: 4-Clause Lifecycle
    res_ok = safe_prompt_pipeline("Hello AI World", max_chars=50)
    assert res_ok["status"] == "ok" and res_ok["word_count"] == 3 and res_ok["pipeline_finalized"] is True

    res_type = safe_prompt_pipeline(12345, max_chars=50)
    assert res_type["status"] == "type_error" and res_type["pipeline_finalized"] is True

    res_len = safe_prompt_pipeline("A" * 100, max_chars=50)
    assert res_len["status"] == "length_error" and res_len["pipeline_finalized"] is True
    print("  [PASS] Challenge 2: safe_prompt_pipeline 4-clause lifecycle verified")

    # Test 3: Custom AI Exception Hierarchy
    tok_err = TokenQuotaExceeded(current_tokens=1500, max_tokens=1000, request_id="req_001")
    assert tok_err.status_code == 400
    assert tok_err.retryable is False
    assert tok_err.overflow == 500
    assert tok_err.to_dict()["overflow"] == 500

    rate_err = RateLimitBackoff(retry_after_sec=3.5, request_id="req_002")
    assert rate_err.status_code == 429
    assert rate_err.retryable is True
    assert rate_err.retry_after_sec == 3.5
    assert rate_err.to_dict()["retry_after_sec"] == 3.5
    print("  [PASS] Challenge 3: Custom AI Exception Hierarchy & serialization verified")

    # Test 4: Sanitization with 'from None'
    def leaky_db_call():
        raise ConnectionError("host=postgresql://admin:secret@10.0.0.1:5432/creds")

    try:
        sanitize_db_call(leaky_db_call)
        assert False, "Should have raised PublicAPIError"
    except PublicAPIError as sanitized:
        assert sanitized.__cause__ is None
        assert sanitized.__suppress_context__ is True
        print("  [PASS] Challenge 4: Traceback sanitization with 'from None' verified")

    # Test 5: Explicit Provenance with 'from err'
    def faulty_network_call():
        raise TimeoutError("Socket fd=7 dropped after 2.0s")

    try:
        wrap_llm_call("gemini-1.5-pro", faulty_network_call)
        assert False, "Should have raised GatewayInferenceError"
    except GatewayInferenceError as gw_err:
        assert isinstance(gw_err.__cause__, TimeoutError)
        assert gw_err.model_name == "gemini-1.5-pro"
        print("  [PASS] Challenge 5: Explicit chaining and __cause__ provenance verified")

    # Test 6: Multi-Provider Failover with ExceptionGroup
    # Subtest 6A: First provider succeeds
    p1 = lambda: "p1_success"
    p2 = lambda: "p2_success"
    assert execute_waterfall([p1, p2]) == "p1_success"

    # Subtest 6B: All fail -> ExceptionGroup
    def fail_timeout(): raise TimeoutError("P1 timeout")
    def fail_quota(): raise PermissionError("P2 quota exceeded")

    try:
        execute_waterfall([fail_timeout, fail_quota])
        assert False, "Should have raised ExceptionGroup"
    except* TimeoutError as timeouts:
        assert len(timeouts.exceptions) == 1
    except* PermissionError as perms:
        assert len(perms.exceptions) == 1
    print("  [PASS] Challenge 6: Multi-provider failover and ExceptionGroup/except* verified")

    print("\n" + "=" * 70)
    print("ALL 6/6 CHALLENGES PASSED! EXCEPTION ENGINEERING CERTIFIED!")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

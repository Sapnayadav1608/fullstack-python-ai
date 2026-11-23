"""
===============================================================================
Day 17: Module 03 - Custom Exception Hierarchies for Enterprise AI Systems
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Designing Scalable, Typed, Self-Describing Exception Trees
Architecture: Clean Architecture Separation of Client (4xx) & Server (5xx)
===============================================================================

In production AI platforms (serving LLMs, RAG pipelines, or vision models),
raising raw generic `Exception` or `ValueError` produces brittle, unmaintainable code.
Downstream microservices and API gateways need to make intelligent runtime decisions:
  - Should the request be retried with exponential backoff? (RateLimit, ServerTimeout)
  - Should the user be charged, or told to shorten their prompt? (TokenLimitExceeded)
  - Should security incident response be alerted immediately? (PromptInjection)

To achieve this, we design a polymorphic exception hierarchy that:
  1. Carries rich diagnostic metadata (status_code, request_id, retryable, latency).
  2. Implements serialization (`to_dict()` / `to_api_response()`) for FastAPI/Flask.
  3. Enables precise multi-catch blocks without brittle string parsing.
  4. Supports dynamic error dispatch via factory patterns.
"""

from __future__ import annotations
import json
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


# ============================================================================
# SECTION 1: THE ROOT DOMAIN EXCEPTION (AIPlatformError)
# ============================================================================
print("=" * 75)
print("SECTION 1: THE ROOT DOMAIN EXCEPTION & METADATA ENVELOPE")
print("=" * 75)

class AIPlatformError(Exception):
    """
    Root base exception for all AI platform operations.
    Every platform error carries structured metadata for observability & Sentry.
    """
    error_code: str = "ERR_INTERNAL_AI_PLATFORM"
    status_code: int = 500
    retryable: bool = False

    def __init__(
        self,
        message: str,
        *,
        request_id: Optional[str] = None,
        model_id: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(message)
        self.message = message
        self.request_id = request_id or f"req_{int(time.time() * 1000)}"
        self.model_id = model_id or "unknown-model"
        self.details = details or {}
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Serialize into standard RFC 7807 Problem Details JSON envelope."""
        return {
            "error": {
                "code": self.error_code,
                "message": self.message,
                "status_code": self.status_code,
                "retryable": self.retryable,
                "model_id": self.model_id,
                "request_id": self.request_id,
                "timestamp": self.timestamp,
                "details": self.details,
            }
        }

    def __str__(self) -> str:
        return f"[{self.error_code}] (Status {self.status_code}) {self.message} (req={self.request_id})"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(error_code={self.error_code!r}, "
            f"status_code={self.status_code}, message={self.message!r})"
        )


# ============================================================================
# SECTION 2: CLIENT-SIDE ERROR BRANCH (4xx - Callers Must Fix Payload)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: CLIENT ERROR BRANCH (4xx Family - Non-Retryable)")
print("=" * 75)

class AIClientError(AIPlatformError):
    """Base class for caller mistakes (invalid inputs, prompt issues, bad tokens)."""
    error_code = "ERR_AI_CLIENT_FAULT"
    status_code = 400
    retryable = False


class TokenLimitExceededError(AIClientError):
    """Raised when user prompt exceeds model's context window length."""
    error_code = "ERR_TOKEN_LIMIT_EXCEEDED"
    status_code = 400

    def __init__(
        self,
        current_tokens: int,
        max_context_tokens: int,
        model_id: str,
        request_id: Optional[str] = None
    ):
        overflow = current_tokens - max_context_tokens
        msg = (
            f"Prompt length of {current_tokens:,} tokens exceeds maximum context "
            f"window of {max_context_tokens:,} tokens for model '{model_id}' (overflow: +{overflow:,})"
        )
        super().__init__(
            msg,
            request_id=request_id,
            model_id=model_id,
            details={
                "current_tokens": current_tokens,
                "max_context_tokens": max_context_tokens,
                "overflow": overflow,
                "recommendation": "Truncate conversation history or use 1M context Gemini Pro",
            }
        )
        self.current_tokens = current_tokens
        self.max_context_tokens = max_context_tokens
        self.overflow = overflow


class PromptInjectionDetectedError(AIClientError):
    """Raised when an adversarial injection attempt is detected in user input."""
    error_code = "ERR_SECURITY_PROMPT_INJECTION"
    status_code = 403

    def __init__(
        self,
        risk_score: float,
        detected_patterns: List[str],
        request_id: Optional[str] = None
    ):
        msg = f"Security Violation: Prompt injection heuristic triggered (risk score: {risk_score:.2f})"
        super().__init__(
            msg,
            request_id=request_id,
            details={
                "risk_score": risk_score,
                "detected_patterns": detected_patterns,
                "action": "Request logged and blocked at perimeter gateway",
            }
        )
        self.risk_score = risk_score
        self.detected_patterns = detected_patterns


class ModelNotFoundError(AIClientError):
    """Raised when requested model ID is not registered in the catalog."""
    error_code = "ERR_MODEL_NOT_FOUND"
    status_code = 404

    def __init__(self, requested_model: str, available_models: List[str], request_id: Optional[str] = None):
        msg = f"Model '{requested_model}' not found in active catalog. Available: {available_models}"
        super().__init__(
            msg,
            request_id=request_id,
            details={"requested": requested_model, "available": available_models}
        )


# ============================================================================
# SECTION 3: SERVER-SIDE ERROR BRANCH (5xx - Platform/Upstream Failures)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 3: SERVER ERROR BRANCH (5xx Family - Safe to Retry)")
print("=" * 75)

class AIServerError(AIPlatformError):
    """Base class for backend, infrastructure, or third-party API provider failures."""
    error_code = "ERR_AI_SERVER_FAULT"
    status_code = 500
    retryable = True


class RateLimitExceededError(AIServerError):
    """Raised when token bucket or TPM (Tokens Per Minute) quota is exhausted."""
    error_code = "ERR_RATE_LIMIT_EXCEEDED"
    status_code = 429
    retryable = True

    def __init__(
        self,
        retry_after_seconds: float,
        quota_tier: str,
        request_id: Optional[str] = None
    ):
        msg = f"Quota exceeded for tier '{quota_tier}'. Back off for {retry_after_seconds:.1f}s."
        super().__init__(
            msg,
            request_id=request_id,
            details={
                "retry_after_seconds": retry_after_seconds,
                "quota_tier": quota_tier,
                "header_hint": f"Retry-After: {int(retry_after_seconds)}"
            }
        )
        self.retry_after_seconds = retry_after_seconds
        self.quota_tier = quota_tier


class ProviderOutageError(AIServerError):
    """Raised when an external LLM vendor returns 502/503/504 Bad Gateway."""
    error_code = "ERR_PROVIDER_OUTAGE"
    status_code = 502
    retryable = True

    def __init__(self, provider_name: str, upstream_status: int, request_id: Optional[str] = None):
        msg = f"Upstream provider '{provider_name}' reported outage with HTTP {upstream_status}."
        super().__init__(
            msg,
            request_id=request_id,
            details={"provider": provider_name, "upstream_status": upstream_status}
        )
        self.provider_name = provider_name
        self.upstream_status = upstream_status


# ============================================================================
# SECTION 4: DYNAMIC ERROR DISPATCH FACTORY
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 4: DYNAMIC HTTP-TO-DOMAIN EXCEPTION FACTORY")
print("=" * 75)

def map_http_response_to_exception(
    status_code: int,
    payload: Dict[str, Any],
    request_id: str
) -> AIPlatformError:
    """
    Factory that converts raw vendor HTTP response envelopes into typed
    Python domain exceptions with rich semantic attributes.
    """
    err_message = payload.get("message", "Unknown error from upstream LLM provider")

    if status_code == 429:
        retry_after = float(payload.get("retry_after", 3.0))
        return RateLimitExceededError(retry_after_seconds=retry_after, quota_tier="enterprise", request_id=request_id)
    elif status_code == 400 and "token" in err_message.lower():
        return TokenLimitExceededError(
            current_tokens=payload.get("tokens", 132000),
            max_context_tokens=128000,
            model_id=payload.get("model", "gpt-4o"),
            request_id=request_id
        )
    elif status_code == 403:
        return PromptInjectionDetectedError(
            risk_score=0.94,
            detected_patterns=["ignore previous instructions", "system prompt override"],
            request_id=request_id
        )
    elif status_code in (502, 503, 504):
        return ProviderOutageError(provider_name="Anthropic", upstream_status=status_code, request_id=request_id)
    else:
        return AIPlatformError(message=err_message, request_id=request_id)


# Verify Dynamic Factory
sample_429 = {"message": "TPM limit reached", "retry_after": 5.5}
mapped_err = map_http_response_to_exception(429, sample_429, "req_alpha_99")
print(f"  Mapped HTTP 429 -> {type(mapped_err).__name__}")
print(f"  Retryable: {mapped_err.retryable} | Retry After: {mapped_err.retry_after_seconds}s")
assert isinstance(mapped_err, RateLimitExceededError)


# ============================================================================
# SECTION 5: ENTERPRISE DISPATCH PIPELINE DEMONSTRATION
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 5: ENTERPRISE POLYMORPHIC ERROR DISPATCH")
print("=" * 75)

def simulate_llm_request(scenario: str):
    """Simulates triggering various failure modes."""
    if scenario == "token_overflow":
        raise TokenLimitExceededError(current_tokens=145000, max_context_tokens=128000, model_id="gemini-1.5-flash")
    elif scenario == "rate_limit":
        raise RateLimitExceededError(retry_after_seconds=4.2, quota_tier="pro-tier")
    elif scenario == "injection":
        raise PromptInjectionDetectedError(risk_score=0.98, detected_patterns=["DAN prompt", "jailbreak"])
    elif scenario == "outage":
        raise ProviderOutageError("GoogleCloudAI", upstream_status=503)
    return "SUCCESS: 200 OK"


for scenario in ["token_overflow", "rate_limit", "injection", "outage"]:
    print(f"\n--- Testing Scenario: '{scenario}' ---")
    try:
        simulate_llm_request(scenario)
    except AIClientError as client_err:
        # 4xx family: Caller is responsible; do not retry
        print(f"  [4xx Handled] Client Error: {client_err}")
        print(f"  -> Action: Send HTTP {client_err.status_code} with Problem JSON:")
        print(f"     {json.dumps(client_err.to_dict()['error'], indent=6)}")
    except AIServerError as server_err:
        # 5xx family: Platform is responsible; initiate backoff or switch vendor
        print(f"  [5xx Handled] Server Error: {server_err}")
        if isinstance(server_err, RateLimitExceededError):
            print(f"  -> Action: Initiating automated jittered backoff ({server_err.retry_after_seconds}s)...")
        elif isinstance(server_err, ProviderOutageError):
            print(f"  -> Action: Tripping circuit breaker and routing to fallback provider!")

print("\n" + "=" * 75)
print("Module 03 Complete: Custom AI Exception Hierarchies Fully Operational!")
print("=" * 75)

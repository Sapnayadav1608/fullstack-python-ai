"""
===============================================================================
Day 17: Module 04 - Exception Groups, except* & Resilient AI Architectures
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Modern Python 3.11+ ExceptionGroup, except*, Circuit Breakers & Failover
Architecture: Fault-Tolerant Concurrent Multi-Agent & Multi-LLM Systems
===============================================================================

In distributed AI systems (e.g. concurrent tool execution, multi-agent swarms,
or parallel model ensembles), multiple operations run concurrently. If 3 out of
5 parallel tools fail, traditional Python exception handling could only raise ONE
exception, completely dropping the other two into the void!

Python 3.11 introduced PEP 654: Exception Groups and `except*`:
  1. `ExceptionGroup`: Bundles multiple arbitrary exceptions into a single tree.
  2. `except*`: Selectively catches specific exception types from a group without
     swallowing the rest, allowing remaining exceptions to bubble up.
  3. Production Pattern 1: Circuit Breaker (Closed, Open, Half-Open).
  4. Production Pattern 2: Multi-Provider Fallback Router (Pro -> Flash -> Cache).
"""

from __future__ import annotations
import enum
import time
from typing import Any, Callable, Dict, List, Optional, Tuple


# ============================================================================
# SECTION 1: ExceptionGroup FUNDAMENTALS (Python 3.11+)
# ============================================================================
print("=" * 75)
print("SECTION 1: ExceptionGroup ANATOMY & TREE STRUCTURE")
print("=" * 75)

# Simulate 3 concurrent tool errors in an AI Agent
tool_errors = [
    TimeoutError("Tool 'web_search' timed out after 3.0s"),
    ValueError("Tool 'code_interpreter' rejected unsafe import 'os'"),
    KeyError("Tool 'vector_retrieval' missing collection index 'finance_v2'"),
]

agent_task_group_error = ExceptionGroup("Agent multi-tool execution failed", tool_errors)

print(f"ExceptionGroup message:    {agent_task_group_error.message}")
print(f"Number of sub-exceptions:  {len(agent_task_group_error.exceptions)}")
for i, sub_err in enumerate(agent_task_group_error.exceptions, 1):
    print(f"  [{i}] {type(sub_err).__name__}: {sub_err}")

# Inspecting subgroups
lookup_subgroup = agent_task_group_error.subgroup(lambda e: isinstance(e, LookupError))
print(f"\nSubgroup of LookupErrors: {lookup_subgroup}")
assert lookup_subgroup is not None and len(lookup_subgroup.exceptions) == 1


# ============================================================================
# SECTION 2: THE `except*` SYNTAX (Selective Concurrent Handling)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: MODERN `except*` PATTERN MATCHING")
print("=" * 75)

def simulate_concurrent_agent_dispatch():
    """
    Simulates throwing an ExceptionGroup and catching individual slices
    using the `except*` syntax introduced in Python 3.11.
    """
    try:
        raise ExceptionGroup(
            "Agent Workflow Errors",
            [
                TimeoutError("Vector DB cluster unreachable"),
                ValueError("Embedding dimension mismatch: expected 1536, got 768"),
                TimeoutError("LLM Gateway latency threshold exceeded"),
            ]
        )
    except* TimeoutError as timeouts:
        # Matches all TimeoutErrors in the group!
        print(f"  [except* TimeoutError] Caught {len(timeouts.exceptions)} timeout failures:")
        for t in timeouts.exceptions:
            print(f"    -> Timeout detail: {t}")
    except* ValueError as val_errors:
        # Matches all ValueErrors in the group!
        print(f"  [except* ValueError] Caught {len(val_errors.exceptions)} validation failures:")
        for v in val_errors.exceptions:
            print(f"    -> Validation detail: {v}")


simulate_concurrent_agent_dispatch()


# ============================================================================
# SECTION 3: ENTERPRISE RESILIENCY PATTERN 1 — THE CIRCUIT BREAKER
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 3: PRODUCTION CIRCUIT BREAKER (Closed -> Open -> Half-Open)")
print("=" * 75)

class CircuitState(enum.Enum):
    CLOSED = "CLOSED"        # Normal operation: requests pass through
    OPEN = "OPEN"            # Tripped: fast-fail immediately without calling provider
    HALF_OPEN = "HALF_OPEN"  # Testing recovery: allow one canary request


class CircuitBreakerOpenException(Exception):
    """Raised when request is rejected fast by the Circuit Breaker."""
    def __init__(self, service_name: str, cooldown_remaining: float):
        super().__init__(
            f"Circuit Breaker for '{service_name}' is OPEN. "
            f"Fast-failing request. Cooldown remaining: {cooldown_remaining:.2f}s"
        )
        self.service_name = service_name
        self.cooldown_remaining = cooldown_remaining


class CircuitBreaker:
    """
    Prevents cascading service failures by failing fast when an external
    dependency is suffering prolonged outages.
    """
    def __init__(
        self,
        service_name: str,
        failure_threshold: int = 3,
        recovery_timeout_sec: float = 1.0
    ):
        self.service_name = service_name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout_sec
        self.failure_count = 0
        self.last_state_change = time.time()
        self.state = CircuitState.CLOSED

    def execute(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        now = time.time()

        # Check state transition from OPEN to HALF_OPEN
        if self.state == CircuitState.OPEN:
            elapsed = now - self.last_state_change
            if elapsed >= self.recovery_timeout:
                print(f"  [{self.service_name} Circuit] Cooldown elapsed -> Transitioning to HALF_OPEN")
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerOpenException(self.service_name, self.recovery_timeout - elapsed)

        try:
            result = func(*args, **kwargs)
            # If successful in HALF_OPEN, reset back to CLOSED
            if self.state == CircuitState.HALF_OPEN:
                print(f"  [{self.service_name} Circuit] Canary succeeded -> Resetting to CLOSED")
                self.state = CircuitState.CLOSED
                self.failure_count = 0
            return result
        except Exception as err:
            self.failure_count += 1
            print(f"  [{self.service_name} Circuit] Failure #{self.failure_count}: {err}")
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
                self.last_state_change = time.time()
                print(f"  [{self.service_name} Circuit] Threshold reached -> Tripping to OPEN!")
            raise


# Test Circuit Breaker Simulation
cb = CircuitBreaker("GeminiUltraEndpoint", failure_threshold=2, recovery_timeout_sec=0.2)

def unstable_endpoint():
    raise ConnectionResetError("503 Service Unavailable")

# Trip the breaker with 2 consecutive failures
for attempt in range(1, 3):
    try:
        cb.execute(unstable_endpoint)
    except ConnectionResetError:
        pass

# 3rd attempt: Circuit is OPEN -> Fast-fails with CircuitBreakerOpenException!
try:
    cb.execute(unstable_endpoint)
except CircuitBreakerOpenException as cbe:
    print(f"  [Fast-Fail Confirmed] {cbe}")
    assert cb.state == CircuitState.OPEN


# ============================================================================
# SECTION 4: ENTERPRISE RESILIENCY PATTERN 2 — MULTI-PROVIDER FALLBACK
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 4: MULTI-PROVIDER AI ROUTER WITH ExceptionGroup AGGREGATION")
print("=" * 75)

class AIProvider:
    def __init__(self, name: str, should_fail: bool, failure_exc: Exception, response: str = ""):
        self.name = name
        self.should_fail = should_fail
        self.failure_exc = failure_exc
        self.response = response

    def generate(self, prompt: str) -> str:
        if self.should_fail:
            raise self.failure_exc
        return f"[{self.name}] {self.response}"


class ResilientAIRouter:
    """
    Tries a waterfall sequence of model providers:
    Primary -> Secondary -> Tertiary
    If all fail, collects every individual exception and raises an ExceptionGroup!
    """
    def __init__(self, providers: List[AIProvider]):
        self.providers = providers

    def route_prompt(self, prompt: str) -> Tuple[str, str]:
        collected_errors: List[Exception] = []

        for provider in self.providers:
            try:
                print(f"  -> Attempting Provider: '{provider.name}'...")
                res = provider.generate(prompt)
                print(f"     Success on provider '{provider.name}'!")
                return provider.name, res
            except Exception as exc:
                print(f"     Failed on '{provider.name}': {type(exc).__name__} ({exc})")
                collected_errors.append(exc)

        # All providers failed! Raise an ExceptionGroup
        raise ExceptionGroup(
            f"All {len(self.providers)} AI providers failed for prompt execution",
            collected_errors
        )


# Scenario A: Primary fails (RateLimit), Secondary succeeds (Gemini Flash)
providers_a = [
    AIProvider("Gemini-1.5-Pro", should_fail=True, failure_exc=TimeoutError("Deadline exceeded")),
    AIProvider("Gemini-1.5-Flash", should_fail=False, failure_exc=Exception(), response="AI Summary ready"),
]
router_a = ResilientAIRouter(providers_a)
success_prov, response_a = router_a.route_prompt("Summarize document")
print(f"  Outcome: Provider={success_prov} | Response={response_a}\n")
assert success_prov == "Gemini-1.5-Flash"

# Scenario B: All providers fail -> Aggregated into ExceptionGroup
providers_b = [
    AIProvider("Gemini-1.5-Pro", should_fail=True, failure_exc=TimeoutError("HTTP 504 Gateway Timeout")),
    AIProvider("Gemini-1.5-Flash", should_fail=True, failure_exc=PermissionError("HTTP 403 Quota Depleted")),
    AIProvider("Local-Ollama-Fallback", should_fail=True, failure_exc=ConnectionRefusedError("Port 11434 Closed")),
]
router_b = ResilientAIRouter(providers_b)

try:
    router_b.route_prompt("Generate unit tests")
except* TimeoutError as timeouts:
    print(f"  [Handled Timeouts in Group] Count: {len(timeouts.exceptions)}")
except* (PermissionError, ConnectionRefusedError) as fatal_errs:
    print(f"  [Handled Auth/Connection in Group] Count: {len(fatal_errs.exceptions)}")

print("\n" + "=" * 75)
print("Module 04 Complete: Exception Groups & Resilient Architectures Mastered!")
print("=" * 75)

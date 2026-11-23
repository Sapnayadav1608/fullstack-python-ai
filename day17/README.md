# 📍 Day 17: Advanced Exception Handling, Custom Exception Hierarchies & Defensive AI Engineering

Welcome to **Day 17** of the **30-Day Full Stack Python + AI Engineering Challenge**! Today, we transition from writing code that works in happy-path scenarios to engineering **fault-tolerant, resilient, production-grade distributed AI systems**.

In enterprise AI engineering (serving LLMs, RAG pipelines, or autonomous agents), exceptions are inevitable: upstream providers experience 504 timeouts, context windows get exceeded, rate limits trip, and network sockets drop. Writing naive `except Exception: pass` hides critical bugs and causes cascading microservice outages. Today, we master the full architectural mechanics of CPython exceptions, traceback engineering, custom domain hierarchies, and Python 3.11+ concurrent exception groups.

---

## 🏗️ CPython Exception Architecture

```
BaseException
 ├── SystemExit                   # Direct exit (never catch in app code)
 ├── KeyboardInterrupt            # User Ctrl+C (never swallow!)
 └── Exception                    # Safe application root
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      └── AIPlatformError (Custom Enterprise Root)
           ├── AIClientError (HTTP 4xx - Non-Retryable)
           │    ├── TokenLimitExceededError
           │    └── PromptInjectionDetectedError
           └── AIServerError (HTTP 5xx - Retryable / Circuit Breaker)
                ├── RateLimitExceededError (with backoff hints)
                └── ProviderOutageError
```

---

## 📚 What We Built & Explored

### 1. `01_exception_architecture_and_mechanics.py`
- **CPython Inheritance Hierarchy:** The difference between `BaseException` and `Exception`. Why catching `BaseException` or writing bare `except:` prevents users from terminating stuck models with `Ctrl+C`.
- **The 4-Clause Lifecycle (`try/except/else/finally`):**
  - `try`: Minimal blast-radius block.
  - `except`: Handles only anticipated, specific exception types.
  - `else`: Runs *only* when no exceptions occurred in `try`. Prevents catching bugs in downstream code accidentally.
  - `finally`: Deterministic cleanup guaranteed to execute (closing DB connections, releasing GPU memory, recording latency telemetry).
- **The Deadly Anti-Patterns:**
  - Bare `except:` and `except: pass` (swallowing typos, `AttributeError`, and system halts).
  - Catching `BaseException` vs `Exception`.
- **Enterprise Pattern:** `SafeModelCallWrapper` returning standardized `{success, result, error}` execution envelopes.

### 2. `02_exception_chaining_and_context.py`
- **PEP 3134 Mechanics:**
  - **Implicit Context (`__context__`):** Automatically recorded when an error triggers during exception handling.
  - **Explicit Chaining (`raise ... from original_err`):** Sets `__cause__` to explicitly link domain errors to low-level socket/timeout roots.
  - **Context Suppression (`raise ... from None`):** Sanitizes public API tracebacks to prevent leaking database credentials, internal IPs, or proprietary schema secrets.
- **Traceback Introspection:** Building programmatic root-cause resolvers using `traceback` and recursive causality traversal (`__cause__` / `__context__`).
- **Resilient AI Gateway Pattern:** Preserving upstream vendor failure provenance while emitting structured Datadog/Sentry telemetry.

### 3. `03_custom_exception_hierarchies_for_ai.py`
- **Enterprise Exception Taxonomy:** Clean architectural separation of:
  - `AIClientError` (HTTP 400/403/404): Non-retryable caller mistakes (`TokenLimitExceededError`, `PromptInjectionDetectedError`, `ModelNotFoundError`).
  - `AIServerError` (HTTP 429/502/503): Retryable platform outages (`RateLimitExceededError` with `retry_after_seconds`, `ProviderOutageError`).
- **Structured Metadata Envelopes:** Attaching `error_code`, `status_code`, `request_id`, `timestamp`, and `details` to every exception.
- **Serialization (`to_dict()`):** RFC 7807 Problem Details serialization ready for FastAPI, Flask, and microservice meshes.
- **Dynamic HTTP-to-Domain Factory:** Centralized error mapper translating raw vendor HTTP codes into typed Python exceptions.

### 4. `04_exception_groups_and_resilient_pipelines.py`
- **Python 3.11+ `ExceptionGroup`:** Bundling multiple concurrent errors from parallel AI agent tools or asyncio task groups into a single structured tree.
- **Modern `except*` Syntax:** Selectively catching specific slices (`except* TimeoutError`, `except* ValueError`) while letting remaining unhandled branches bubble up.
- **Resiliency Pattern 1 (The Circuit Breaker):** State machine (`CLOSED` $\rightarrow$ `OPEN` $\rightarrow$ `HALF_OPEN`) with fast-failure rejection (`CircuitBreakerOpenException`) to protect overwhelmed LLM backends.
- **Resiliency Pattern 2 (Multi-Provider Fallback Router):** Waterfall execution (Gemini Pro $\rightarrow$ Gemini Flash $\rightarrow$ Cache) that aggregates total systemic failures into an `ExceptionGroup`.

### 5. `my_practice.py` (Automated Test Suite)
- **6 Challenging Hands-on Tasks:**
  1. Hierarchy Classifier (`classify_exception_category`)
  2. Defensive 4-Clause Pipeline (`safe_prompt_pipeline`)
  3. Custom AI Exception Hierarchy with metadata serialization
  4. Traceback Sanitization (`sanitize_db_call` with `from None`)
  5. Explicit Provenance Chaining (`wrap_llm_call` with `from err`)
  6. Multi-Provider Failover Router raising `ExceptionGroup` and handled via `except*`
- **100% Automated Test Coverage:** Automated verification with 6/6 test assertions passing.

---

## ⚡ Exception Handling Cheat Sheet

| Syntax / Pattern | Purpose | When to Use |
| :--- | :--- | :--- |
| `try ... except ... else ... finally` | Full 4-clause lifecycle | Production pipelines needing guaranteed cleanup and isolated blast radius |
| `raise DomainError(...) from err` | Explicit Chaining (`__cause__`) | Preserving low-level network/socket provenance in domain wrappers |
| `raise PublicError(...) from None` | Context Suppression (`__cause__ = None`) | Public API boundaries to prevent security and credential leaks |
| `class MyError(Exception): pass` | Custom typed domain error | Downstream routing, structured error handling, and Sentry alerts |
| `ExceptionGroup("msg", [e1, e2])` | Concurrent error bundling | Asyncio `TaskGroup` or multi-agent parallel tool execution |
| `except* ErrorType as eg:` | Selective group matching | Handling partial failures across concurrent background workers |

---

## 🧪 Running the Code & Test Suite

```powershell
# Run individual modules
python day17/01_exception_architecture_and_mechanics.py
python day17/02_exception_chaining_and_context.py
python day17/03_custom_exception_hierarchies_for_ai.py
python day17/04_exception_groups_and_resilient_pipelines.py

# Run hands-on practice test suite
python day17/my_practice.py
```

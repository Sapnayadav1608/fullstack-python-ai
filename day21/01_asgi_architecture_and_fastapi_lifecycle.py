"""
Day 21 — Module 01: ASGI vs WSGI Architecture & The Modern FastAPI Lifespan
===========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Phase 2 Grand Kickoff: Modern Full Stack Web Development!

Key Concepts Covered:
1. WSGI (Synchronous) vs ASGI (Asynchronous Server Gateway Interface):
   - WSGI (Flask / Django): One thread per request, blocking I/O, no native WebSockets or async.
   - ASGI (FastAPI / Starlette / Uvicorn): Asynchronous event-loop driven, cooperative multitasking,
     handles 10,000+ concurrent connections with ultra-low memory footprint.
2. Modern Lifespan Protocol (`@asynccontextmanager`):
   - Python 3.10+ replacement for legacy `@app.on_event("startup")` and `@app.on_event("shutdown")`.
   - Guaranteed resource initialization (DB connection pools, AI model weights) and graceful teardown.
3. Custom Middleware Pipeline:
   - Request timing (`X-Process-Time-Ms`), security headers, and CORS handling.
4. Live Verification via `TestClient`:
   - Testing ASGI applications in-memory without spawning network sockets.
"""

import sys
import time
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# -------------------------------------------------------------------------
# 1. APPLICATION LIFESPAN CONTEXT (STARTUP & SHUTDOWN)
# -------------------------------------------------------------------------
# In modern FastAPI, application state (database pools, caches) is managed
# via an async context manager rather than legacy event decorators.
mock_database_pool: Dict[str, Any] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager:
    - Code BEFORE yield runs at startup.
    - Code AFTER yield runs at shutdown.
    """
    print("\n[Lifespan] 🚀 Connecting to Zero-Cost JSON Database Pool...")
    mock_database_pool["active"] = True
    mock_database_pool["initialized_at"] = time.time()
    mock_database_pool["connection_count"] = 10

    yield  # The application serves requests while yielded

    print("[Lifespan] 🛑 Draining connection pool and closing server gracefully...")
    mock_database_pool["active"] = False
    mock_database_pool.clear()


# -------------------------------------------------------------------------
# 2. FASTAPI ASGI APPLICATION INITIALIZATION
# -------------------------------------------------------------------------
app = FastAPI(
    title="Mindifestation Sanctuary ASGI API",
    description="High-performance asynchronous backend for meditation audio streaming and zero-fee checkouts.",
    version="1.0.0",
    lifespan=lifespan
)

# Cross-Origin Resource Sharing (CORS) Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://mindifestation.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------------------------------
# 3. CUSTOM MIDDLEWARE: PROCESS TIME INTERCEPTOR
# -------------------------------------------------------------------------
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Measures latency of every incoming HTTP request and appends response header."""
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time_ms = (time.perf_counter() - start_time) * 1000.0
    response.headers["X-Process-Time-Ms"] = f"{process_time_ms:.2f}"
    return response


# -------------------------------------------------------------------------
# 4. CORE ASGI ENDPOINTS
# -------------------------------------------------------------------------
@app.get("/health", tags=["System"])
async def health_check():
    """Returns application health status and database pool readiness."""
    return {
        "status": "HEALTHY",
        "asgi_server": "Uvicorn",
        "framework": "FastAPI",
        "database_connected": mock_database_pool.get("active", False),
        "active_connections": mock_database_pool.get("connection_count", 0)
    }


@app.get("/api/v1/system/info", tags=["System"])
async def system_architecture_info():
    """Returns architectural comparison between ASGI and WSGI."""
    return {
        "architecture": "ASGI (Asynchronous Server Gateway Interface)",
        "concurrency_model": "Non-blocking Event Loop (AsyncIO)",
        "benchmark_advantages": [
            "Up to 10x higher concurrent request throughput than WSGI",
            "Native asynchronous database driver support without thread-pool exhaustion",
            "Zero memory overhead for idle keep-alive connections"
        ]
    }


# -------------------------------------------------------------------------
# 5. VERIFICATION SUITE VIA TESTCLIENT
# -------------------------------------------------------------------------
def verify_asgi_application():
    print("=" * 70)
    print("🌐 VERIFYING DAY 21 - MODULE 01: ASGI & FASTAPI LIFESPAN")
    print("=" * 70)

    # TestClient invokes the ASGI application through Starlette's mock transport
    with TestClient(app) as client:
        # 1. Health check test
        res = client.get("/health")
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        data = res.json()
        assert data["status"] == "HEALTHY"
        assert data["database_connected"] is True
        assert "X-Process-Time-Ms" in res.headers
        print(f" ✓ /health endpoint passed! Latency: {res.headers['X-Process-Time-Ms']}ms")
        print(f"   Payload: {data}")

        # 2. System info test
        res_info = client.get("/api/v1/system/info")
        assert res_info.status_code == 200
        print(" ✓ /api/v1/system/info endpoint passed! ASGI architecture verified.")

    print("\n✅ Module 01 Lifespan & ASGI Lifecycle Verified Successfully!\n")


if __name__ == "__main__":
    verify_asgi_application()

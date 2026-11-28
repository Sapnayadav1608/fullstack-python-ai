"""
Day 21: FastAPI, ASGI & Dependency Injection — Hands-on Practice Workbook
========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Phase 2: Modern Full Stack Web Development

Complete all 6 challenges below. Each challenge is verified with an automated
TestClient test suite testing routing, validation, status codes, and dependencies.

Run tests via:
    python my_practice.py
"""

import sys
from typing import List, Dict, Any, Optional, Generator
from fastapi import FastAPI, APIRouter, Path, Query, Header, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr
from fastapi.testclient import TestClient

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# =========================================================================
# CHALLENGE 1: Path & Query Parameter Validation (ProductCatalogApp)
# =========================================================================
# Task: Create an app with an endpoint:
# GET /catalog/{department}
# Query params:
#   - max_price: float (must be >= 0.0, default 1000.0)
#   - min_rating: float (must be >= 1.0 and <= 5.0, default 4.0)
#   - limit: int (must be >= 1 and <= 50, default 10)
app_c1 = FastAPI()

MOCK_CATALOG = [
    {"id": 1, "department": "meditation", "name": "Binaural Bell", "price": 499.0, "rating": 4.8},
    {"id": 2, "department": "meditation", "name": "Zafu Cushion", "price": 1299.0, "rating": 4.9},
    {"id": 3, "department": "books", "name": "Manifestation Guide", "price": 299.0, "rating": 4.5},
]


@app_c1.get("/catalog/{department}")
async def get_catalog_products(
    department: str = Path(..., min_length=2),
    max_price: float = Query(1000.0, ge=0.0),
    min_rating: float = Query(4.0, ge=1.0, le=5.0),
    limit: int = Query(10, ge=1, le=50)
):
    results = [
        item for item in MOCK_CATALOG
        if item["department"] == department.lower()
        and item["price"] <= max_price
        and item["rating"] >= min_rating
    ]
    return results[:limit]


# =========================================================================
# CHALLENGE 2: Pydantic V2 Request & Response Filtering (MemberRegistrationApp)
# =========================================================================
# Task: User registration endpoint POST /register
# Request Body schema: username, email, raw_password
# Response Model schema: user_id, username, email, is_active
# CRITICAL: raw_password must NEVER be exposed in the response!
app_c2 = FastAPI()


class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    raw_password: str = Field(..., min_length=8)


class UserRegisterResponse(BaseModel):
    user_id: str
    username: str
    email: EmailStr
    is_active: bool


@app_c2.post("/register", response_model=UserRegisterResponse, status_code=status.HTTP_201_CREATED)
async def register_member(payload: UserRegisterRequest):
    return {
        "user_id": f"USR_{abs(hash(payload.username)):x}",
        "username": payload.username,
        "email": payload.email,
        "is_active": True,
        "hashed_password_internal": "bcrypt$2b$12$securehash12345"
    }


# =========================================================================
# CHALLENGE 3: Custom Exception Handler (ResilientAPIApp)
# =========================================================================
# Task: Create a custom ItemNotFoundException.
# Register an exception handler that formats the error into RFC 7807 problem details:
# {"type": "error:not_found", "title": "Resource Not Found", "status": 404, "item_id": ...}
app_c3 = FastAPI()


class ItemNotFoundException(Exception):
    def __init__(self, item_id: str):
        self.item_id = item_id


@app_c3.exception_handler(ItemNotFoundException)
async def item_not_found_handler(request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "type": "error:not_found",
            "title": "Resource Not Found",
            "status": 404,
            "item_id": exc.item_id,
            "message": f"Requested item {exc.item_id} does not exist in sanctuary."
        }
    )


@app_c3.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id != "item_42":
        raise ItemNotFoundException(item_id=item_id)
    return {"item_id": item_id, "name": "Golden Singing Bowl"}


# =========================================================================
# CHALLENGE 4: Modular APIRouter Composition (MultiServiceApp)
# =========================================================================
# Task: Construct two APIRouters:
#   1. inventory_router: prefix="/inventory", tags=["Inventory"], GET /stock
#   2. orders_router: prefix="/orders", tags=["Orders"], GET /recent
# Include both under root app with prefix="/api/v1"
app_c4 = FastAPI()

inventory_router = APIRouter(prefix="/inventory", tags=["Inventory"])


@inventory_router.get("/stock")
async def get_inventory_stock():
    return {"total_skus": 142, "in_stock": True}


orders_router = APIRouter(prefix="/orders", tags=["Orders"])


@orders_router.get("/recent")
async def get_recent_orders():
    return [{"order_id": "ORD-101", "total_inr": 499.0}]


v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(inventory_router)
v1_router.include_router(orders_router)
app_c4.include_router(v1_router)


# =========================================================================
# CHALLENGE 5: Dependency with Yield Lifecycle (TransactionalApp)
# =========================================================================
# Task: Create a mock database transaction session dependency with yield.
# When entering the route, session.is_active = True.
# When leaving the route (in finally clause), session.is_active = False, session.is_committed = True.
app_c5 = FastAPI()


class TransactionSession:
    def __init__(self):
        self.is_active = False
        self.is_committed = False


SESSION_REFS = []


def get_transaction_session() -> Generator[TransactionSession, None, None]:
    session = TransactionSession()
    session.is_active = True
    SESSION_REFS.append(session)
    try:
        yield session
    finally:
        session.is_active = False
        session.is_committed = True


@app_c5.post("/payments/process")
async def process_payment(session: TransactionSession = Depends(get_transaction_session)):
    return {
        "status": "PROCESSED",
        "session_active_during_route": session.is_active
    }


# =========================================================================
# CHALLENGE 6: API Key Security & Dependency Override (SecureVaultApp)
# =========================================================================
# Task: Implement an endpoint GET /vault/secrets protected by
# dependency get_vault_key(x_vault_key: str = Header(...))
# If key is valid, return secret.
# In the test suite, demonstrate using app.dependency_overrides to bypass security!
app_c6 = FastAPI()


def verify_vault_key(x_vault_key: str = Header(...)):
    if x_vault_key != "super_secure_vault_pass_99":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access Denied: Invalid Vault Key"
        )
    return x_vault_key


@app_c6.get("/vault/secrets")
async def get_vault_secrets(key: str = Depends(verify_vault_key)):
    return {"confidential": "Quantum Manifestation Audio Masters", "authorized_by": key}


# =========================================================================
# AUTOMATED TEST SUITE (6/6 TESTS)
# =========================================================================
def test_challenge_1():
    print("▶ Testing Challenge 1: Path & Query Parameter Validation...")
    client = TestClient(app_c1)

    # Valid request
    res = client.get("/catalog/meditation?max_price=600&min_rating=4.5&limit=5")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 1
    assert data[0]["name"] == "Binaural Bell"

    # Query param bounds failure (min_rating > 5.0 -> 422)
    res_bad = client.get("/catalog/meditation?min_rating=6.5")
    assert res_bad.status_code == 422

    print("  ✓ Challenge 1 Passed! Path coercion and query boundary validation verified.")


def test_challenge_2():
    print("▶ Testing Challenge 2: Pydantic V2 Request & Response Sanitization...")
    client = TestClient(app_c2)

    payload = {
        "username": "sapna_yadav",
        "email": "sapna@mindifestation.com",
        "raw_password": "super_secret_password_123"
    }
    res = client.post("/register", json=payload)
    assert res.status_code == 201
    data = res.json()
    assert data["username"] == "sapna_yadav"
    assert data["is_active"] is True
    # CRITICAL SECURITY CHECK: Password must not be leaked!
    assert "raw_password" not in data
    assert "hashed_password_internal" not in data

    print("  ✓ Challenge 2 Passed! Pydantic V2 response model sanitized sensitive credentials.")


def test_challenge_3():
    print("▶ Testing Challenge 3: Custom Exception Handler (RFC 7807)...")
    client = TestClient(app_c3)

    # Valid item
    res_ok = client.get("/items/item_42")
    assert res_ok.status_code == 200
    assert res_ok.json()["name"] == "Golden Singing Bowl"

    # Missing item triggers custom exception handler
    res_err = client.get("/items/unknown_99")
    assert res_err.status_code == 404
    err_data = res_err.json()
    assert err_data["type"] == "error:not_found"
    assert err_data["item_id"] == "unknown_99"

    print("  ✓ Challenge 3 Passed! Custom exception transformed into RFC 7807 problem details.")


def test_challenge_4():
    print("▶ Testing Challenge 4: Modular APIRouter Composition...")
    client = TestClient(app_c4)

    # Test inventory router
    res_inv = client.get("/api/v1/inventory/stock")
    assert res_inv.status_code == 200
    assert res_inv.json()["total_skus"] == 142

    # Test orders router
    res_ord = client.get("/api/v1/orders/recent")
    assert res_ord.status_code == 200
    assert len(res_ord.json()) == 1

    print("  ✓ Challenge 4 Passed! APIRouters modularly composed under /api/v1 namespace.")


def test_challenge_5():
    print("▶ Testing Challenge 5: Dependency with Yield Lifecycle...")
    client = TestClient(app_c5)

    res = client.post("/payments/process")
    assert res.status_code == 200
    assert res.json()["session_active_during_route"] is True

    # Check teardown executed in finally block
    last_session = SESSION_REFS[-1]
    assert last_session.is_active is False
    assert last_session.is_committed is True

    print("  ✓ Challenge 5 Passed! Yield dependency guaranteed automatic cleanup and commit.")


def test_challenge_6():
    print("▶ Testing Challenge 6: API Key Security & Dependency Overrides...")
    client = TestClient(app_c6)

    # 1. Unauthorized request
    res_unauth = client.get("/vault/secrets")
    assert res_unauth.status_code in (401, 422)

    # 2. Authorized request
    res_auth = client.get("/vault/secrets", headers={"X-Vault-Key": "super_secure_vault_pass_99"})
    assert res_auth.status_code == 200
    assert "confidential" in res_auth.json()

    # 3. Dependency Override in Automated Testing
    app_c6.dependency_overrides[verify_vault_key] = lambda: "MOCK_TEST_KEY"
    res_overridden = client.get("/vault/secrets")
    assert res_overridden.status_code == 200
    assert res_overridden.json()["authorized_by"] == "MOCK_TEST_KEY"
    app_c6.dependency_overrides.clear()

    print("  ✓ Challenge 6 Passed! Security enforced and dependency_overrides demonstrated.")


def run_all_tests():
    print("=" * 70)
    print("🧪 RUNNING DAY 21 AUTOMATED FASTAPI PRACTICE TEST SUITE")
    print("=" * 70)
    test_challenge_1()
    test_challenge_2()
    test_challenge_3()
    test_challenge_4()
    test_challenge_5()
    test_challenge_6()
    print("=" * 70)
    print("🎉 ALL 6/6 FASTAPI PRACTICE CHALLENGES PASSED WITH ZERO ERRORS!")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()

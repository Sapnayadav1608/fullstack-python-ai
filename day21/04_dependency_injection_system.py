"""
Day 21 — Module 04: The Dependency Injection Engine & Production Security
========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Key Concepts Covered:
1. Inversion of Control & `fastapi.Depends`:
   - Why Dependency Injection is FastAPI's killer feature: Clean separation of concerns,
     testability, and reusability across endpoints.
2. Dependencies with `yield` (Resource Lifecycle Management):
   - Opens connection pool / transaction -> yields to endpoint -> cleans up/commits in `finally`.
3. Chained Multi-Tier Dependencies:
   - `Request Header -> Validate JWT / Token -> Query Current User -> Check Role / Permissions`.
4. Mocking & Dependency Overrides for Testing (`app.dependency_overrides`):
   - How to test protected endpoints in automated CI/CD without real databases or authentication servers.
"""

import sys
from typing import Dict, Any, Generator
from fastapi import FastAPI, Depends, Header, HTTPException, status
from pydantic import BaseModel
from fastapi.testclient import TestClient

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

app = FastAPI(title="Dependency Injection & Security Engine", version="1.0.0")


# -------------------------------------------------------------------------
# 1. DATABASE SESSION DEPENDENCY WITH YIELD (RESOURCE LIFECYCLE)
# -------------------------------------------------------------------------
class MockDatabaseSession:
    """Simulates a transactional database session."""
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.is_open = True
        self.committed = False

    def query_user(self, user_id: str) -> Dict[str, Any]:
        users = {
            "USR-101": {"id": "USR-101", "name": "Sapna Yadav", "role": "admin", "is_active": True},
            "USR-102": {"id": "USR-102", "name": "Priyanka Chaudhary", "role": "creator", "is_active": True},
            "USR-103": {"id": "USR-103", "name": "Banned User", "role": "student", "is_active": False}
        }
        return users.get(user_id, None)


def get_db_session() -> Generator[MockDatabaseSession, None, None]:
    """
    Dependency with yield:
    - Setup: Instantiates a mock database session.
    - Yield: Passes session to the endpoint handler.
    - Teardown: Guaranteed cleanup execution even if route raises an exception!
    """
    session = MockDatabaseSession("session_txn_789")
    try:
        # Code before yield runs before endpoint
        yield session
    finally:
        # Code after yield runs after endpoint returns (or raises error)
        session.is_open = False
        session.committed = True


# -------------------------------------------------------------------------
# 2. HIERARCHICAL SECURITY DEPENDENCIES (CHAINING)
# -------------------------------------------------------------------------
class CurrentUser(BaseModel):
    id: str
    name: str
    role: str
    is_active: bool


async def get_api_key_header(x_api_key: str = Header(..., description="API Security Key")):
    """Tier 1: Validates that the client passed a recognized API key."""
    if x_api_key != "secret_mindifestation_token_2026":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-API-Key header"
        )
    return x_api_key


async def get_authenticated_user(
    x_user_id: str = Header(..., description="User ID Header"),
    api_key: str = Depends(get_api_key_header),
    db: MockDatabaseSession = Depends(get_db_session)
) -> CurrentUser:
    """
    Tier 2: Depends on Tier 1 (API key) and Database Session.
    Retrieves user record and verifies active status.
    """
    user_record = db.query_user(x_user_id)
    if not user_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {x_user_id} does not exist in sanctuary database."
        )
    if not user_record["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is suspended or deactivated."
        )
    return CurrentUser(**user_record)


async def require_admin_role(current_user: CurrentUser = Depends(get_authenticated_user)) -> CurrentUser:
    """Tier 3: Higher-order dependency requiring admin authorization."""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Requires Administrator privileges."
        )
    return current_user


# -------------------------------------------------------------------------
# 3. ENDPOINTS UTILIZING DEPENDENCY INJECTION
# -------------------------------------------------------------------------
@app.get("/api/v1/user/profile", response_model=CurrentUser, tags=["User"])
async def get_user_profile(user: CurrentUser = Depends(get_authenticated_user)):
    """Protected endpoint: Any valid active user can view their profile."""
    return user


@app.get("/api/v1/admin/analytics", tags=["Admin"])
async def get_sanctuary_analytics(admin: CurrentUser = Depends(require_admin_role)):
    """Restricted endpoint: Only administrators can access revenue analytics."""
    return {
        "authorized_admin": admin.name,
        "daily_active_meditators": 4820,
        "total_upi_revenue_inr": 184500.0,
        "gateway_fees_saved_inr": 3690.0,
        "status": "TOP_SECRET_REVENUE_METRICS"
    }


# -------------------------------------------------------------------------
# 4. VERIFICATION & DEPENDENCY OVERRIDE TESTING
# -------------------------------------------------------------------------
def verify_dependency_injection():
    print("=" * 70)
    print("💉 VERIFYING DAY 21 - MODULE 04: DEPENDENCY INJECTION SYSTEM")
    print("=" * 70)

    client = TestClient(app)

    # 1. Missing API Key Header -> 422/401
    res_no_key = client.get("/api/v1/user/profile", headers={"X-User-Id": "USR-101"})
    assert res_no_key.status_code in (401, 422)
    print(" ✓ Unauthenticated request rejected by header dependency.")

    # 2. Invalid API Key -> 401
    res_bad_key = client.get("/api/v1/user/profile", headers={
        "X-API-Key": "wrong_key",
        "X-User-Id": "USR-101"
    })
    assert res_bad_key.status_code == 401
    print(" ✓ Invalid API Key rejected with 401 Unauthorized.")

    # 3. Valid User Profile (/api/v1/user/profile)
    headers_creator = {
        "X-API-Key": "secret_mindifestation_token_2026",
        "X-User-Id": "USR-102"
    }
    res_profile = client.get("/api/v1/user/profile", headers=headers_creator)
    assert res_profile.status_code == 200
    assert res_profile.json()["name"] == "Priyanka Chaudhary"
    print(f" ✓ Authenticated user dependency passed: {res_profile.json()['name']} ({res_profile.json()['role']})")

    # 4. Creator attempting to access Admin Analytics -> 403 Forbidden
    res_forbidden = client.get("/api/v1/admin/analytics", headers=headers_creator)
    assert res_forbidden.status_code == 403
    print(f" ✓ Role-Based Authorization caught non-admin access: {res_forbidden.json()['detail']}")

    # 5. Admin accessing Admin Analytics -> 200 OK
    headers_admin = {
        "X-API-Key": "secret_mindifestation_token_2026",
        "X-User-Id": "USR-101"
    }
    res_admin = client.get("/api/v1/admin/analytics", headers=headers_admin)
    assert res_admin.status_code == 200
    assert res_admin.json()["total_upi_revenue_inr"] == 184500.0
    print(f" ✓ Admin dependency authorized: {res_admin.json()['authorized_admin']}")

    # 6. TESTING FASTAPI'S KILLER FEATURE: app.dependency_overrides
    print("\n [Testing Dependency Overrides in CI/CD]:")
    # Simulate an automated test where we bypass auth headers entirely!
    def mock_override_admin():
        return CurrentUser(id="MOCK-001", name="Automated Bot Admin", role="admin", is_active=True)

    app.dependency_overrides[require_admin_role] = mock_override_admin
    res_mocked = client.get("/api/v1/admin/analytics")
    assert res_mocked.status_code == 200
    assert res_mocked.json()["authorized_admin"] == "Automated Bot Admin"
    print(" ✓ app.dependency_overrides seamlessly swapped production security for unit testing!")

    # Clean up overrides
    app.dependency_overrides.clear()

    print("\n✅ Module 04 Dependency Injection Suite Passed Successfully!\n")


if __name__ == "__main__":
    verify_dependency_injection()

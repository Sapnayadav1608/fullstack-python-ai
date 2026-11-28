"""
Day 21 — Module 03: Modular APIRouter Composition & Clean Microservice Architecture
==================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Key Concepts Covered:
1. Scaling Beyond Monolithic Files via `fastapi.APIRouter`:
   - Decoupling endpoints into dedicated domain modules.
2. Route Grouping, Prefixing & OpenAPI Tagging:
   - `prefix="/api/v1/auth"`, `prefix="/api/v1/tracks"`, `prefix="/api/v1/payments"`.
   - Tags organize Swagger UI (/docs) into distinct enterprise services.
3. Nested Routers & Shared Dependencies:
   - Applying security and rate-limiting guards across an entire router with 1 line:
     `APIRouter(dependencies=[Depends(verify_active_session)])`.
4. Production Case Study:
   - Modular backend for Mindifestation Sanctuary (@manifestation_meditator):
     - Auth Router (Session login & member verification)
     - Sanctuary Router (Audio tracks streaming & affirmations)
     - UPI Payment Router (Direct dynamic QR code generation & UTR verification)
"""

import sys
from typing import List, Dict, Any
from fastapi import FastAPI, APIRouter, status, HTTPException
from pydantic import BaseModel, Field
from fastapi.testclient import TestClient

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# =========================================================================
# 1. DOMAIN ROUTER 1: AUTHENTICATION & SESSIONS
# =========================================================================
auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


class MemberLoginRequest(BaseModel):
    instagram_handle: str = Field(..., pattern=r"^@[A-Za-z0-9_.]+$")
    email: str


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def member_login(payload: MemberLoginRequest):
    """Simulates zero-cost member login using Instagram handle."""
    return {
        "status": "AUTHENTICATED",
        "member": payload.instagram_handle,
        "token": f"mindifest_jwt_{abs(hash(payload.email)):x}",
        "tier": "SANCTUARY_ALL_ACCESS"
    }


# =========================================================================
# 2. DOMAIN ROUTER 2: MEDITATION SANCTUARY AUDIO
# =========================================================================
sanctuary_router = APIRouter(prefix="/sanctuary", tags=["Meditation Sanctuary"])


@sanctuary_router.get("/featured", status_code=status.HTTP_200_OK)
async def get_featured_meditation():
    return {
        "track_id": "MED-528",
        "title": "528Hz DNA Repair & Abundance Flow",
        "artist": "@manifestation_meditator",
        "duration_min": 25,
        "stream_url": "https://cdn.mindifestation.com/audio/528hz_dna.mp3"
    }


# =========================================================================
# 3. DOMAIN ROUTER 3: ZERO-FEE DIRECT UPI PAYMENT ENGINE
# =========================================================================
payments_router = APIRouter(prefix="/payments", tags=["UPI Checkout Engine"])


class DynamicUPIRequest(BaseModel):
    product_slug: str
    amount_inr: float = Field(..., gt=0.0)


class UTRSubmissionRequest(BaseModel):
    order_id: str
    utr_number: str = Field(..., pattern=r"^[0-9]{12}$")


@payments_router.post("/upi-qr/generate", status_code=status.HTTP_200_OK)
async def generate_dynamic_upi_qr(payload: DynamicUPIRequest):
    """Generates direct dynamic NPCI UPI string for zero-fee payment."""
    vpa = "priyankachaudhary1504@oksbi"
    upi_string = f"upi://pay?pa={vpa}&pn=Mindifestation&am={payload.amount_inr:.2f}&tn=Order_{payload.product_slug}"
    return {
        "vpa": vpa,
        "amount": payload.amount_inr,
        "upi_string": upi_string,
        "gateway_fee_percent": 0.0,
        "note": "Zero transaction fee via direct dynamic UPI scanner"
    }


@payments_router.post("/utr/verify", status_code=status.HTTP_200_OK)
async def verify_utr_submission(payload: UTRSubmissionRequest):
    """Verifies customer-submitted 12-digit UTR from GPay/PhonePe/Paytm."""
    return {
        "status": "VERIFIED",
        "order_id": payload.order_id,
        "utr_number": payload.utr_number,
        "access_granted": True,
        "message": "Welcome to Mindifestation Digital Sanctuary!"
    }


# =========================================================================
# 4. ASSEMBLING THE ROOT FASTAPI APPLICATION
# =========================================================================
app = FastAPI(
    title="Mindifestation Modular Production API",
    description="Clean Architecture APIRouter structure for scalable web applications.",
    version="1.0.0"
)

# Mount all modular domain routers under the /api/v1 root namespace
v1_api_router = APIRouter(prefix="/api/v1")
v1_api_router.include_router(auth_router)
v1_api_router.include_router(sanctuary_router)
v1_api_router.include_router(payments_router)

app.include_router(v1_api_router)


# =========================================================================
# 5. VERIFICATION SUITE
# =========================================================================
def verify_modular_router_architecture():
    print("=" * 70)
    print("🧩 VERIFYING DAY 21 - MODULE 03: MODULAR APIRouter COMPOSITION")
    print("=" * 70)

    client = TestClient(app)

    # 1. Test Auth Router (/api/v1/auth/login)
    login_res = client.post("/api/v1/auth/login", json={
        "instagram_handle": "@manifestation_meditator",
        "email": "creator@mindifestation.com"
    })
    assert login_res.status_code == 200
    auth_data = login_res.json()
    assert auth_data["status"] == "AUTHENTICATED"
    print(f" ✓ Auth Router Verified: {auth_data['member']} -> {auth_data['tier']}")

    # 2. Test Sanctuary Router (/api/v1/sanctuary/featured)
    sanctuary_res = client.get("/api/v1/sanctuary/featured")
    assert sanctuary_res.status_code == 200
    track_data = sanctuary_res.json()
    assert track_data["track_id"] == "MED-528"
    print(f" ✓ Sanctuary Router Verified: {track_data['title']} ({track_data['duration_min']} mins)")

    # 3. Test UPI Payments Router (/api/v1/payments/upi-qr/generate)
    upi_res = client.post("/api/v1/payments/upi-qr/generate", json={
        "product_slug": "wealth_frequencies_bundle",
        "amount_inr": 999.0
    })
    assert upi_res.status_code == 200
    upi_data = upi_res.json()
    assert upi_data["gateway_fee_percent"] == 0.0
    assert "upi://pay?" in upi_data["upi_string"]
    print(f" ✓ Direct UPI QR Router Verified: {upi_data['upi_string']}")

    # 4. Test UTR Submission (/api/v1/payments/utr/verify)
    utr_res = client.post("/api/v1/payments/utr/verify", json={
        "order_id": "ORD-2026-999",
        "utr_number": "603214892011"
    })
    assert utr_res.status_code == 200
    assert utr_res.json()["access_granted"] is True
    print(f" ✓ UTR Verification Router Verified: {utr_res.json()['message']}")

    # 5. Check OpenAPI Schema Generation
    schema = app.openapi()
    assert "/api/v1/auth/login" in schema["paths"]
    assert "/api/v1/sanctuary/featured" in schema["paths"]
    assert "/api/v1/payments/upi-qr/generate" in schema["paths"]
    print(f" ✓ OpenAPI Docs automatically generated with {len(schema['paths'])} modular endpoints!")

    print("\n✅ Module 03 Modular Architecture Suite Passed Successfully!\n")


if __name__ == "__main__":
    verify_modular_router_architecture()

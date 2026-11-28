"""
Day 21 — Module 02: Request-Response Lifecycle, Parameters & Pydantic V2 Validation
===================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Key Concepts Covered:
1. Path Parameters with Automatic Type Casting & Path Constraints:
   - Typing `/tracks/{track_id: int}` ensures automatic 422 Unprocessable Entity on invalid input.
2. Query Parameters with Defaults, Pagination & Field Validation:
   - `Query(default=10, ge=1, le=100)` enforces bounds without manual `if` statements.
3. Request Body Validation via Pydantic V2 Schemas:
   - Nested models, custom field validators, and regex constraints.
4. Response Models (`response_model=...`):
   - Strict data shaping: Prevents accidental data leaks (passwords, internal secret keys).
   - `response_model_exclude_unset=True` for compact JSON responses.
5. HTTP Status Codes & Error Handling:
   - Using `status.HTTP_201_CREATED`, `status.HTTP_404_NOT_FOUND`, and raising `HTTPException`.
"""

import sys
from typing import List, Optional
from datetime import datetime

from fastapi import FastAPI, Query, Path, status, HTTPException
from pydantic import BaseModel, Field, field_validator
from fastapi.testclient import TestClient

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

app = FastAPI(title="Pydantic V2 Validation & Parameters Engine", version="1.0.0")


# -------------------------------------------------------------------------
# 1. PYDANTIC V2 SCHEMAS (REQUEST & RESPONSE MODELS)
# -------------------------------------------------------------------------
class MeditationTrackCreate(BaseModel):
    """Incoming payload schema for creating a meditation track."""
    title: str = Field(..., min_length=3, max_length=100, description="Title of the track")
    category: str = Field(..., pattern=r"^(sleep|focus|breathwork|manifestation)$")
    duration_seconds: int = Field(..., gt=0, le=7200, description="Duration in seconds (max 2 hours)")
    audio_cdn_url: str = Field(..., pattern=r"^https://cdn\.mindifestation\.com/.*\.mp3$")
    price_inr: float = Field(default=0.0, ge=0.0, description="0.0 indicates free track")

    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        cleaned = v.strip().title()
        if len(cleaned) < 3:
            raise ValueError("Title must contain at least 3 non-whitespace characters")
        return cleaned


class MeditationTrackResponse(BaseModel):
    """Outgoing response schema (Notice: internal database metadata is omitted or filtered)."""
    id: int
    title: str
    category: str
    duration_seconds: int
    audio_cdn_url: str
    price_inr: float
    is_premium: bool
    created_at: datetime


# -------------------------------------------------------------------------
# 2. IN-MEMORY DATABASE STORE
# -------------------------------------------------------------------------
TRACKS_DATABASE: List[dict] = [
    {
        "id": 1,
        "title": "Deep Delta Sleep 432Hz",
        "category": "sleep",
        "duration_seconds": 1800,
        "audio_cdn_url": "https://cdn.mindifestation.com/sleep_432.mp3",
        "price_inr": 0.0,
        "is_premium": False,
        "secret_admin_notes": "Mastered at SoundStudio Mumbai",
        "created_at": datetime(2026, 11, 25, 10, 0, 0)
    },
    {
        "id": 2,
        "title": "Quantum Manifestation Frequency",
        "category": "manifestation",
        "duration_seconds": 1200,
        "audio_cdn_url": "https://cdn.mindifestation.com/manifest_528.mp3",
        "price_inr": 499.0,
        "is_premium": True,
        "secret_admin_notes": "Exclusive track for workshop members",
        "created_at": datetime(2026, 11, 26, 12, 0, 0)
    }
]


# -------------------------------------------------------------------------
# 3. REST ENDPOINTS DEMONSTRATING PARAMETERS & VALIDATION
# -------------------------------------------------------------------------
@app.get(
    "/api/v1/tracks",
    response_model=List[MeditationTrackResponse],
    status_code=status.HTTP_200_OK,
    tags=["Tracks"]
)
async def list_tracks(
    category: Optional[str] = Query(None, description="Filter tracks by category"),
    max_price: Optional[float] = Query(None, ge=0.0, description="Filter tracks by maximum price"),
    limit: int = Query(10, ge=1, le=50, description="Pagination limit"),
    offset: int = Query(0, ge=0, description="Pagination offset")
):
    """Query parameter filtering with strict bounds and pagination."""
    results = TRACKS_DATABASE
    if category:
        results = [t for t in results if t["category"] == category.lower()]
    if max_price is not None:
        results = [t for t in results if t["price_inr"] <= max_price]
    return results[offset : offset + limit]


@app.get(
    "/api/v1/tracks/{track_id}",
    response_model=MeditationTrackResponse,
    status_code=status.HTTP_200_OK,
    tags=["Tracks"]
)
async def get_track_by_id(
    track_id: int = Path(..., ge=1, description="Unique integer ID of the meditation track")
):
    """Path parameter with automatic integer coercion and 404 handling."""
    for track in TRACKS_DATABASE:
        if track["id"] == track_id:
            return track
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Meditation track with ID {track_id} not found."
    )


@app.post(
    "/api/v1/tracks",
    response_model=MeditationTrackResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Tracks"]
)
async def create_track(payload: MeditationTrackCreate):
    """Request body validation via Pydantic V2 schema."""
    new_id = len(TRACKS_DATABASE) + 1
    new_track = {
        "id": new_id,
        "title": payload.title,
        "category": payload.category,
        "duration_seconds": payload.duration_seconds,
        "audio_cdn_url": payload.audio_cdn_url,
        "price_inr": payload.price_inr,
        "is_premium": payload.price_inr > 0.0,
        "secret_admin_notes": "Created via API Endpoint",
        "created_at": datetime.now()
    }
    TRACKS_DATABASE.append(new_track)
    return new_track


# -------------------------------------------------------------------------
# 4. VERIFICATION SUITE
# -------------------------------------------------------------------------
def verify_validation_and_parameters():
    print("=" * 70)
    print("🔍 VERIFYING DAY 21 - MODULE 02: PYDANTIC V2 VALIDATION & PARAMS")
    print("=" * 70)

    client = TestClient(app)

    # 1. Test Query Parameters & Pagination
    res = client.get("/api/v1/tracks?category=sleep&limit=5")
    assert res.status_code == 200
    tracks = res.json()
    assert len(tracks) == 1
    assert tracks[0]["category"] == "sleep"
    # Verify response model excluded internal 'secret_admin_notes'
    assert "secret_admin_notes" not in tracks[0]
    print(f" ✓ Query filtering & response model serialization passed: {tracks[0]['title']}")

    # 2. Test Path Parameter & 404 error
    res_404 = client.get("/api/v1/tracks/999")
    assert res_404.status_code == 404
    print(f" ✓ Path parameter 404 handled cleanly: {res_404.json()['detail']}")

    # 3. Test Invalid Path Parameter (type failure -> automatic 422)
    res_422 = client.get("/api/v1/tracks/abc")
    assert res_422.status_code == 422
    print(" ✓ Automatic 422 Unprocessable Entity generated for string track_id!")

    # 4. Test Valid POST Request Body
    valid_payload = {
        "title": "  morning breathwork focus  ",
        "category": "breathwork",
        "duration_seconds": 600,
        "audio_cdn_url": "https://cdn.mindifestation.com/breathwork_01.mp3",
        "price_inr": 199.0
    }
    res_create = client.post("/api/v1/tracks", json=valid_payload)
    assert res_create.status_code == 201
    created_data = res_create.json()
    assert created_data["title"] == "Morning Breathwork Focus"  # Cleaned by field_validator
    assert created_data["is_premium"] is True
    print(f" ✓ POST creation passed with Pydantic V2 cleaning: {created_data['title']}")

    # 5. Test Invalid POST Request Body (Regex / category mismatch -> 422)
    bad_payload = {
        "title": "Bad Track",
        "category": "rock_and_roll",  # invalid category
        "duration_seconds": -50,       # invalid duration
        "audio_cdn_url": "http://insecure.com/track.mp3"
    }
    res_bad = client.post("/api/v1/tracks", json=bad_payload)
    assert res_bad.status_code == 422
    errors = res_bad.json()["detail"]
    print(f" ✓ Pydantic V2 caught {len(errors)} validation errors automatically!")

    print("\n✅ Module 02 Parameters & Validation Suite Passed Successfully!\n")


if __name__ == "__main__":
    verify_validation_and_parameters()

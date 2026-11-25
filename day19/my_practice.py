"""
===============================================================================
Day 19: Hands-On Practice Workbook & Automated Test Suite
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Type Hints, Generics, Dataclasses & Pydantic V2 for AI & Client Systems
6 Rigorous Challenges with Automated Self-Testing Runner
===============================================================================
"""

from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Any, Callable, Dict, Generic, List, Literal, Optional, Protocol, Tuple, TypeVar, runtime_checkable
from pydantic import BaseModel, Field, field_validator, model_validator


# ============================================================================
# CHALLENGE 1: STRUCTURAL PROTOCOL VERIFICATION
# ============================================================================
@runtime_checkable
class IPlayableMedia(Protocol):
    """Protocol for playable audio/video tracks in the Mindifestation library."""
    title: str
    duration_sec: int

    def play(self) -> str: ...


def verify_playable_media(obj: Any) -> bool:
    """Returns True if obj conforms structurally to IPlayableMedia, False otherwise."""
    return isinstance(obj, IPlayableMedia)


# ============================================================================
# CHALLENGE 2: SLOTTED DATACLASS WITH POST-INIT INVARIANTS
# ============================================================================
@dataclass(slots=True)
class MeditationSession:
    """
    Slotted domain entity representing a guided session.
    Automatically generates clean lowercase slug in __post_init__.
    Raises ValueError if duration_sec <= 0 or price_inr < 0.
    """
    title: str
    slug: str
    duration_sec: int
    price_inr: float = 0.0

    def __post_init__(self):
        if self.duration_sec <= 0:
            raise ValueError(f"Duration must be positive, got {self.duration_sec}")
        if self.price_inr < 0.0:
            raise ValueError(f"Price cannot be negative, got {self.price_inr}")
        clean_slug = re.sub(r"[^a-z0-9\-]", "", self.slug.lower().strip().replace(" ", "-"))
        object.__setattr__(self, "slug", clean_slug)


# ============================================================================
# CHALLENGE 3: PYDANTIC V2 PRODUCT VALIDATOR
# ============================================================================
class ClientProductSchema(BaseModel):
    """
    Validates a product upload for the client's store.
    - title: 3 to 100 characters, automatically capitalized.
    - category: Literal['Meditation', 'Sound Bath', 'Manifestation']
    - price_inr: float >= 0.0
    - is_free: bool
    - Cross-validation: If is_free is True, price_inr MUST be 0.0.
    """
    title: str = Field(min_length=3, max_length=100)
    category: Literal["Meditation", "Sound Bath", "Manifestation"]
    price_inr: float = Field(ge=0.0)
    is_free: bool = Field(default=False)

    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        return v.strip().title()

    @model_validator(mode="after")
    def check_pricing_rules(self) -> ClientProductSchema:
        if self.is_free and self.price_inr > 0.0:
            raise ValueError("Free products cannot have a price greater than 0")
        if not self.is_free and self.price_inr == 0.0:
            self.is_free = True
        return self


# ============================================================================
# CHALLENGE 4: RAZORPAY WEBHOOK PARSER
# ============================================================================
class PaymentEntity(BaseModel):
    id: str = Field(pattern=r"^pay_[a-zA-Z0-9]+$")
    amount: int = Field(gt=0)
    status: Literal["captured", "authorized", "failed"]


class RazorpayPayload(BaseModel):
    event: str
    payload: Dict[str, Any]


def parse_captured_payment(webhook_json: Dict[str, Any]) -> Tuple[str, float]:
    """
    Parses a webhook dictionary.
    Returns (payment_id, amount_in_inr).
    Raises ValueError if event is not 'payment.captured' or status is not 'captured'.
    """
    model = RazorpayPayload.model_validate(webhook_json)
    if model.event != "payment.captured":
        raise ValueError(f"Ignored non-captured event: {model.event}")

    payment_data = model.payload.get("payment", {}).get("entity", {})
    entity = PaymentEntity.model_validate(payment_data)
    if entity.status != "captured":
        raise ValueError(f"Payment is not captured: {entity.status}")

    amount_inr = entity.amount / 100.0
    return entity.id, amount_inr


# ============================================================================
# CHALLENGE 5: GENERIC IN-MEMORY REPOSITORY
# ============================================================================
T = TypeVar("T")
K = TypeVar("K")

class GenericInMemoryRepo(Generic[T, K]):
    """Generic in-memory CRUD repository."""
    def __init__(self, key_selector: Callable[[T], K]):
        self._items: Dict[K, T] = {}
        self._key_selector = key_selector

    def add(self, item: T) -> None:
        self._items[self._key_selector(item)] = item

    def get(self, key: K) -> Optional[T]:
        return self._items.get(key)

    def list_all(self) -> List[T]:
        return list(self._items.values())

    def delete(self, key: K) -> bool:
        if key in self._items:
            del self._items[key]
            return True
        return False


# ============================================================================
# CHALLENGE 6: CATALOG AGGREGATOR SERVICE
# ============================================================================
def aggregate_catalog_metrics(sessions: List[MeditationSession], min_duration_sec: int) -> Dict[str, Any]:
    """
    Filters sessions with duration >= min_duration_sec.
    Returns:
      {
        'count': int,
        'total_value_inr': float,
        'avg_duration_sec': float
      }
    """
    filtered = [s for s in sessions if s.duration_sec >= min_duration_sec]
    if not filtered:
        return {"count": 0, "total_value_inr": 0.0, "avg_duration_sec": 0.0}

    total_val = sum(s.price_inr for s in filtered)
    avg_dur = sum(s.duration_sec for s in filtered) / len(filtered)
    return {
        "count": len(filtered),
        "total_value_inr": total_val,
        "avg_duration_sec": avg_dur
    }


# ============================================================================
# AUTOMATED TEST RUNNER
# ============================================================================
def run_tests():
    print("=" * 70)
    print("RUNNING DAY 19 AUTOMATED TEST SUITE — TYPE SYSTEMS & CLIENT BACKENDS")
    print("=" * 70)

    # Test 1: Structural Protocol Verification
    class AudioTrack:
        def __init__(self, title: str, duration_sec: int):
            self.title = title
            self.duration_sec = duration_sec
        def play(self) -> str: return "Playing"

    class Book:
        def __init__(self, title: str):
            self.title = title

    assert verify_playable_media(AudioTrack("432Hz Sleep", 1800)) is True
    assert verify_playable_media(Book("Manifestation Workbook")) is False
    print("  [PASS] Challenge 1: verify_playable_media verifies structural subtyping")

    # Test 2: Slotted Dataclass
    s = MeditationSession("Morning Presence", "Morning Presence 2026!", 900, 299.0)
    assert s.slug == "morning-presence-2026"
    assert not hasattr(s, "__dict__")

    try:
        MeditationSession("Bad", "bad", -10, 0)
        assert False, "Should raise ValueError for negative duration"
    except ValueError:
        pass
    print("  [PASS] Challenge 2: MeditationSession dataclass invariants verified")

    # Test 3: Pydantic Product Validator
    prod = ClientProductSchema(title="  432hz sound bath  ", category="Sound Bath", price_inr=399.0)
    assert prod.title == "432Hz Sound Bath"
    assert prod.is_free is False

    try:
        ClientProductSchema(title="Bad Free", category="Meditation", price_inr=100.0, is_free=True)
        assert False, "Should fail free pricing rule"
    except Exception:
        pass
    print("  [PASS] Challenge 3: ClientProductSchema validates client product uploads")

    # Test 4: Razorpay Webhook Parser
    wh_data = {
        "event": "payment.captured",
        "payload": {
            "payment": {
                "entity": {"id": "pay_test12345", "amount": 49900, "status": "captured"}
            }
        }
    }
    pid, amt = parse_captured_payment(wh_data)
    assert pid == "pay_test12345"
    assert amt == 499.0
    print("  [PASS] Challenge 4: parse_captured_payment handles Razorpay webhooks")

    # Test 5: Generic In-Memory Repository
    repo = GenericInMemoryRepo[MeditationSession, str](key_selector=lambda x: x.slug)
    s1 = MeditationSession("Track 1", "track-1", 600, 199.0)
    s2 = MeditationSession("Track 2", "track-2", 1200, 299.0)
    repo.add(s1)
    repo.add(s2)
    assert repo.get("track-1") == s1
    assert len(repo.list_all()) == 2
    assert repo.delete("track-1") is True
    assert repo.get("track-1") is None
    print("  [PASS] Challenge 5: GenericInMemoryRepo manages typed entities")

    # Test 6: Catalog Aggregator
    sessions = [
        MeditationSession("Short", "s", 300, 0.0),
        MeditationSession("Med 1", "m1", 900, 299.0),
        MeditationSession("Med 2", "m2", 1200, 399.0),
    ]
    res = aggregate_catalog_metrics(sessions, min_duration_sec=600)
    assert res["count"] == 2
    assert res["total_value_inr"] == 698.0
    assert res["avg_duration_sec"] == 1050.0
    print("  [PASS] Challenge 6: aggregate_catalog_metrics aggregates business metrics")

    print("\n" + "=" * 70)
    print("ALL 6/6 CHALLENGES PASSED! TYPE SYSTEMS & CLIENT ARCHITECTURE CERTIFIED!")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

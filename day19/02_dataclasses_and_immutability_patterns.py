"""
===============================================================================
Day 19: Module 02 - Dataclasses, Immutability & Domain Modeling
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: High-Performance Data Modeling with PEP 557 @dataclass & slots=True
Case Study: Mindifestation Meditation Products & Client Website Proposal
===============================================================================

In enterprise backend engineering, writing repetitive boilerplate for `__init__`,
`__repr__`, `__eq__`, and hashing wastes developer time and invites subtle bugs.
Python's `@dataclass` (introduced in Python 3.7 and supercharged in 3.10 with `slots=True`)
provides a declarative, high-performance way to define typed domain entities.

This module explores:
  1. `@dataclass` Anatomy: Automated constructor, equality, and representations.
  2. The `slots=True` Supercharger: Eliminating `__dict__` overhead for 4x less RAM
     and faster attribute lookup.
  3. Immutable Domain Models with `frozen=True` & `__post_init__` validation.
  4. The Mutable Default Trap & `field(default_factory=list)`.
  5. Real-World Client Modeling: Domain schemas for the Mindifestation meditation platform.
"""

from __future__ import annotations
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4


# ============================================================================
# SECTION 1: DATACLASS WITH SLOTS & POST-INIT VALIDATION
# ============================================================================
print("=" * 75)
print("SECTION 1: HIGH-PERFORMANCE DATACLASS WITH SLOTS=TRUE & VALIDATION")
print("=" * 75)

@dataclass(slots=True)
class MeditationTrack:
    """
    Core audio entity for the Mindifestation digital sanctuary.
    Using slots=True eliminates instance __dict__ memory overhead.
    """
    id: UUID
    title: str
    slug: str
    duration_seconds: int
    audio_url: str
    category: str
    price_inr: float = 0.0
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self):
        """Domain invariant validation executed immediately after __init__."""
        if self.duration_seconds <= 0:
            raise ValueError(f"Duration must be strictly positive, got {self.duration_seconds}s")
        if self.price_inr < 0:
            raise ValueError(f"Price cannot be negative, got {self.price_inr}")
        # Clean slug formatting
        clean_slug = re.sub(r"[^a-z0-9\-]", "", self.slug.lower().replace(" ", "-"))
        object.__setattr__(self, "slug", clean_slug)

    @property
    def formatted_duration(self) -> str:
        mins = self.duration_seconds // 60
        secs = self.duration_seconds % 60
        return f"{mins} min {secs} sec" if secs else f"{mins} min"


track1 = MeditationTrack(
    id=uuid4(),
    title="Chakra Balancing & 432Hz Sound Bath",
    slug="Chakra Balancing 432Hz",
    duration_seconds=1200,
    audio_url="https://cdn.mindifestation.com/tracks/chakra_432.mp3",
    category="Meditation",
    price_inr=299.0,
    tags=["chakra", "sound bath", "432hz"]
)

print(f"Instantiated Track: {track1.title}")
print(f"Generated Clean Slug: {track1.slug}")
print(f"Formatted Duration:   {track1.formatted_duration}")
print(f"Has __dict__?:        {hasattr(track1, '__dict__')} (slots=True active!)")
assert not hasattr(track1, "__dict__")


# ============================================================================
# SECTION 2: IMMUTABLE DOMAIN ENTITIES (frozen=True)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: IMMUTABLE DOMAIN VALUE OBJECTS (frozen=True)")
print("=" * 75)

@dataclass(frozen=True, slots=True)
class DailyAffirmation:
    """
    Immutable value object for the Mindifestation Daily Reminder feature.
    Being frozen makes it naturally hashable, so it can be stored in sets or as dict keys.
    """
    id: str
    quote: str
    category: str
    anchor_phrase: str

    def __post_init__(self):
        if not self.quote.strip():
            raise ValueError("Affirmation quote cannot be empty or whitespace")


aff1 = DailyAffirmation(
    id="aff_01",
    quote="I release the need to control. Everything is unfolding in divine timing.",
    category="Surrender",
    anchor_phrase="I am grounded and patient."
)

print(f"Daily Affirmation: \"{aff1.quote}\"")
print(f"Is hashable?:       {isinstance(hash(aff1), int)}")

# Attempting mutation raises FrozenInstanceError
try:
    aff1.category = "New Category"
except Exception as err:
    print(f"  [Immutability Guaranteed] Mutation blocked: {type(err).__name__}")


# ============================================================================
# SECTION 3: CLIENT PROPOSAL DOMAIN MODEL
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 3: CLIENT PROPOSAL DOMAIN ENTITY (Mindifestation Project Pitch)")
print("=" * 75)

@dataclass(slots=True)
class ClientProposal:
    """Captures the project scope and deliverables for the meditation website client."""
    client_name: str
    brand_name: str
    instagram_handle: str
    target_launch_weeks: int
    deliverables: List[str]
    total_quote_inr: float
    status: str = "PITCHED"

    def summary(self) -> Dict[str, Any]:
        return asdict(self)


mindifestation_pitch = ClientProposal(
    client_name="Pooja Sharma",
    brand_name="MINDIFESTATION",
    instagram_handle="@manifestation_meditator",
    target_launch_weeks=3,
    deliverables=[
        "Next.js 15 Warm Minimalist Digital Sanctuary UI",
        "Guided Meditation & 432Hz Audio Web Streaming Player",
        "Digital Downloadable PDF Workbooks & Affirmations",
        "Supabase PostgreSQL Database & Razorpay Checkout Integration",
        "Creator Admin Portal for Product & Content Management"
    ],
    total_quote_inr=65000.0,
    status="APPROVED_IN_PROGRESS"
)

print(f"Client: {mindifestation_pitch.client_name} | Brand: {mindifestation_pitch.brand_name}")
print(f"Status: {mindifestation_pitch.status} | Quote: ₹{mindifestation_pitch.total_quote_inr:,.0f}")
print("Deliverables:")
for item in mindifestation_pitch.deliverables:
    print(f"  ✓ {item}")

print("\n" + "=" * 75)
print("Module 02 Complete: Dataclasses & Domain Modeling Mastered!")
print("=" * 75)

"""
===============================================================================
Day 19: Module 01 - Modern Type Systems, Generics & Protocols
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Static Typing with TypeVar, Generic[T], and Structural Protocols
Case Study: Modeling Client Audio Streaming for 'Mindifestation' Platform
===============================================================================

In enterprise full-stack development and AI engineering, dynamic typing allows
rapid prototyping, but introduces silent runtime bugs when scaling up client
APIs. Python 3.10+ and PEP 544 (Protocols) introduced a modern, robust type system
that combines the flexibility of Python's duck typing with the safety of static
compile-time analysis (MyPy, Pyright, VS Code Pylance).

Today, we also integrate a real-world client project pitch:
Building 'MINDIFESTATION' (A digital sanctuary & meditation audio platform).
This module covers:
  1. Modern Type Annotations: Python 3.10+ union syntax (`A | B`), `Optional[T]`.
  2. Generic Classes & Functions (`TypeVar`, `Generic[T]`): Building reusable
     type-safe data structures.
  3. Structural Subtyping with `typing.Protocol` (Compile-time Duck Typing).
  4. Runtime Protocol Verification with `@runtime_checkable`.
  5. Client Architecture: Defining the `IAudioStreamable` and `IMediaResource`
     interfaces for Mindifestation guided meditation tracks.
"""

from __future__ import annotations
from typing import Any, Callable, Dict, Generic, List, Optional, Protocol, TypeVar, runtime_checkable


# ============================================================================
# SECTION 1: MODERN TYPE HINTING & PARAMETERIZED GENERICS
# ============================================================================
print("=" * 75)
print("SECTION 1: MODERN TYPE HINTS & GENERICS (PEP 484 & PEP 604)")
print("=" * 75)

# Python 3.10+ pipe syntax for unions instead of typing.Union
def parse_client_frequency(freq_input: int | float | str) -> float:
    """Converts diverse frequency representations (e.g. '432Hz', 432, 432.0) to float."""
    if isinstance(freq_input, str):
        cleaned = freq_input.lower().replace("hz", "").strip()
        return float(cleaned)
    return float(freq_input)

print(f"Parsed '432Hz' frequency: {parse_client_frequency('432Hz')} Hz")
print(f"Parsed 528 int frequency: {parse_client_frequency(528)} Hz")

# Type Variables for Generic Types
T = TypeVar("T")
PayloadT = TypeVar("PayloadT", bound=Dict[str, Any])

class APIEnvelope(Generic[T]):
    """
    Standard generic API response envelope used across FastAPI and client endpoints.
    guarantees type safety for arbitrary data payloads (T).
    """
    def __init__(self, status: str, data: T, error: Optional[str] = None):
        self.status = status
        self.data = data
        self.error = error

    def is_success(self) -> bool:
        return self.status == "success" and self.error is None

    def __repr__(self) -> str:
        return f"APIEnvelope(status={self.status!r}, data={self.data!r})"


# Example usage with string payload and dictionary payload
envelope_str = APIEnvelope[str](status="success", data="Session initialized")
envelope_dict = APIEnvelope[Dict[str, int]](status="success", data={"active_meditators": 1420})

print(f"String Envelope: {envelope_str}")
print(f"Dict Envelope:   {envelope_dict}")
assert envelope_str.is_success()


# ============================================================================
# SECTION 2: STRUCTURAL SUBTYPING WITH PROTOCOLS (PEP 544)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: STRUCTURAL SUBTYPING (typing.Protocol)")
print("=" * 75)

# In Nominal subtyping (like abc.ABC), a class MUST explicitly inherit: class Track(ABC).
# In Structural subtyping (Protocol), a class matches IF IT HAS THE RIGHT SHAPE!
# "If it walks like a duck and quacks like a duck, it IS a duck."

@runtime_checkable
class IAudioStreamable(Protocol):
    """Protocol for any digital media that can be streamed on the Mindifestation web player."""
    title: str
    duration_seconds: int
    audio_url: str

    def get_stream_manifest(self) -> Dict[str, Any]:
        """Returns metadata envelope required by the client audio player."""
        ...


class GuidedMeditationTrack:
    """Independent concrete class — DOES NOT inherit from IAudioStreamable explicitly!"""
    def __init__(self, title: str, duration_sec: int, audio_url: str, instructor: str):
        self.title = title
        self.duration_seconds = duration_sec
        self.audio_url = audio_url
        self.instructor = instructor

    def get_stream_manifest(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "duration": f"{self.duration_seconds // 60}m {self.duration_seconds % 60}s",
            "url": self.audio_url,
            "instructor": self.instructor,
            "format": "audio/mp3",
        }


class BinauralSleepFrequency:
    """Another independent concrete class matching the same protocol shape."""
    def __init__(self, hertz: float, duration_sec: int, audio_url: str):
        self.title = f"Deep Sleep {hertz}Hz Delta Wave"
        self.duration_seconds = duration_sec
        self.audio_url = audio_url
        self.hertz = hertz

    def get_stream_manifest(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "frequency_hz": self.hertz,
            "url": self.audio_url,
            "format": "audio/wav",
        }


# Polymorphic dispatcher accepting ANY object satisfying IAudioStreamable
def play_in_web_sanctuary(item: IAudioStreamable) -> None:
    manifest = item.get_stream_manifest()
    print(f"  [Sanctuary Player] Streaming '{manifest['title']}' from {manifest['url']}")


track = GuidedMeditationTrack(
    title="Morning Presence & Alignment",
    duration_sec=900,
    audio_url="https://cdn.mindifestation.com/audio/morning_alignment.mp3",
    instructor="Sapna Yadav"
)

sound_bath = BinauralSleepFrequency(
    hertz=432.0,
    duration_sec=3600,
    audio_url="https://cdn.mindifestation.com/audio/432hz_sleep.wav"
)

# Runtime verification with @runtime_checkable
print(f"Does GuidedMeditationTrack satisfy IAudioStreamable? {isinstance(track, IAudioStreamable)}")
print(f"Does BinauralSleepFrequency satisfy IAudioStreamable? {isinstance(sound_bath, IAudioStreamable)}")
assert isinstance(track, IAudioStreamable)
assert isinstance(sound_bath, IAudioStreamable)

play_in_web_sanctuary(track)
play_in_web_sanctuary(sound_bath)

print("\n" + "=" * 75)
print("Module 01 Complete: Modern Type Hints, Generics & Protocols Mastered!")
print("=" * 75)

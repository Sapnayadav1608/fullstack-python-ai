"""
Day 15: Advanced Object-Oriented Programming (OOP) Part 2
Student Practice Workbook & Automated Test Suite
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Instructions:
- Fill in the # TODO sections for each of the 6 challenges.
- Run this file: `python day15/my_practice.py`
- All automated unit tests must pass!
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable, List, Dict, Any
import time


# ============================================================================
# TASK 1: MULTI-LEVEL INHERITANCE & super() CHAINING
# ============================================================================
"""
Create a 3-tier inheritance hierarchy:
1. `Vehicle`:
   - `__init__(make: str, model: str)`
   - `drive() -> str`: Returns f"{make} {model} driving on road."
2. `ElectricVehicle(Vehicle)`:
   - `__init__(make: str, model: str, battery_kwh: float)`: uses super()
   - `drive() -> str`: Calls super().drive() and appends f" [Battery: {battery_kwh} kWh]"
3. `AutonomousTesla(ElectricVehicle)`:
   - `__init__(model: str, battery_kwh: float, autopilot_version: str)`:
     make is hardcoded to "Tesla".
   - `drive() -> str`: Calls super().drive() and appends f" [Autopilot v{autopilot_version} Active]"
"""

class Vehicle:
    def __init__(self, make: str, model: str) -> None:
        # TODO: Implement Vehicle.__init__
        raise NotImplementedError("TODO: Implement Vehicle.__init__")

    def drive(self) -> str:
        # TODO: Implement Vehicle.drive
        raise NotImplementedError("TODO: Implement Vehicle.drive")


class ElectricVehicle(Vehicle):
    def __init__(self, make: str, model: str, battery_kwh: float) -> None:
        # TODO: Implement ElectricVehicle.__init__ using super()
        raise NotImplementedError("TODO: Implement ElectricVehicle.__init__")

    def drive(self) -> str:
        # TODO: Implement ElectricVehicle.drive using super()
        raise NotImplementedError("TODO: Implement ElectricVehicle.drive")


class AutonomousTesla(ElectricVehicle):
    def __init__(self, model: str, battery_kwh: float, autopilot_version: str) -> None:
        # TODO: Implement AutonomousTesla.__init__ using super()
        raise NotImplementedError("TODO: Implement AutonomousTesla.__init__")

    def drive(self) -> str:
        # TODO: Implement AutonomousTesla.drive using super()
        raise NotImplementedError("TODO: Implement AutonomousTesla.drive")


# ============================================================================
# TASK 2: DIAMOND PROBLEM & COOPERATIVE MRO
# ============================================================================
"""
Build a classic diamond hierarchy demonstrating cooperative `super()` calls:
- Class `Base`: `process() -> str`: Returns "Base"
- Class `Left(Base)`: `process() -> str`: Returns f"Left -> {super().process()}"
- Class `Right(Base)`: `process() -> str`: Returns f"Right -> {super().process()}"
- Class `Diamond(Left, Right)`: `process() -> str`: Returns f"Diamond -> {super().process()}"

Requirement:
Calling `Diamond().process()` MUST return:
"Diamond -> Left -> Right -> Base"
"""

class Base:
    def process(self) -> str:
        # TODO: Implement Base.process
        raise NotImplementedError("TODO: Implement Base.process")

class Left(Base):
    def process(self) -> str:
        # TODO: Implement Left.process with super()
        raise NotImplementedError("TODO: Implement Left.process")

class Right(Base):
    def process(self) -> str:
        # TODO: Implement Right.process with super()
        raise NotImplementedError("TODO: Implement Right.process")

class Diamond(Left, Right):
    def process(self) -> str:
        # TODO: Implement Diamond.process with super()
        raise NotImplementedError("TODO: Implement Diamond.process")


# ============================================================================
# TASK 3: REUSABLE MIXIN DESIGN (TimestampMixin & DictExportMixin)
# ============================================================================
"""
Create two pluggable mixins:
1. `TimestampMixin`:
   - `__init__(*args, **kwargs)`: attaches `self.created_timestamp = 1700000000` (or time.time())
2. `DictExportMixin`:
   - `to_dict() -> Dict[str, Any]`: returns dictionary of all non-callable,
     non-private (doesn't start with '_') attributes in `self.__dict__`.
3. Class `UserAccount(TimestampMixin, DictExportMixin)`:
   - `__init__(username: str, email: str)`: calls `super().__init__()` and sets attributes.
"""

class TimestampMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # TODO: Assign self.created_timestamp
        raise NotImplementedError("TODO: Implement TimestampMixin")

class DictExportMixin:
    def to_dict(self) -> Dict[str, Any]:
        # TODO: Filter self.__dict__ for public attributes
        raise NotImplementedError("TODO: Implement DictExportMixin.to_dict")

class UserAccount(TimestampMixin, DictExportMixin):
    def __init__(self, username: str, email: str) -> None:
        # TODO: Initialize mixins & set username and email
        raise NotImplementedError("TODO: Implement UserAccount.__init__")


# ============================================================================
# TASK 4: DUCK TYPING (POLYMORPHIC MEDIA STREAMER)
# ============================================================================
"""
Create a duck-typed streaming audio controller function:
`play_audio_stream(source: Any) -> str`
- Checks if `source` has a callable `.get_pcm_bytes()` method.
- If it does, calls it and returns f"PLAYING {len(source.get_pcm_bytes())} BYTES"
- If it does NOT have `.get_pcm_bytes()`, raises `TypeError("Invalid audio source")`.
- Test with two unrelated classes: `MicrophoneStream` and `MP3FileStream`.
"""

class MicrophoneStream:
    def get_pcm_bytes(self) -> bytes:
        return b"\x00\x01\x02\x03" * 256

class MP3FileStream:
    def get_pcm_bytes(self) -> bytes:
        return b"\xAA\xBB\xCC\xDD" * 512

class VideoStreamWithoutAudio:
    pass

def play_audio_stream(source: Any) -> str:
    # TODO: Implement duck-typed audio player
    raise NotImplementedError("TODO: Implement play_audio_stream")


# ============================================================================
# TASK 5: STRUCTURAL SUBTYPING WITH typing.Protocol
# ============================================================================
"""
Define a Protocol `AIModelProtocol`:
- Property `model_name -> str`
- Method `predict(prompt: str) -> str`

Implement two classes that satisfy this protocol WITHOUT inheriting from it:
1. `AnthropicClaude`:
   - `model_name = "claude-3-5-sonnet"`
   - `predict(prompt)` -> f"[Claude]: {prompt}"
2. `OpenAIGPT`:
   - `model_name = "gpt-4o"`
   - `predict(prompt)` -> f"[GPT]: {prompt}"
"""

@runtime_checkable
class AIModelProtocol(Protocol):
    @property
    def model_name(self) -> str:
        ...
    def predict(self, prompt: str) -> str:
        ...

class AnthropicClaude:
    # TODO: Implement Claude satisfying AIModelProtocol
    pass

class OpenAIGPT:
    # TODO: Implement GPT satisfying AIModelProtocol
    pass


# ============================================================================
# TASK 6: ABSTRACT BASE CLASS (BasePaymentGateway)
# ============================================================================
"""
Create an Abstract Base Class `BasePaymentGateway(ABC)`:
- `@property @abstractmethod def gateway_name(self) -> str`: ...
- `@abstractmethod def charge(self, amount: float, currency: str) -> Dict[str, Any]`: ...
- Concrete method `format_receipt(amount: float, currency: str) -> str`:
  Returns f"Receipt: {currency} {amount:.2f} via {self.gateway_name}"

Implement concrete class `StripeGateway(BasePaymentGateway)`:
- `gateway_name`: Returns "Stripe Payments"
- `charge(amount, currency)`: Returns `{"status": "PAID", "receipt": self.format_receipt(amount, currency)}`
"""

class BasePaymentGateway(ABC):
    @property
    @abstractmethod
    def gateway_name(self) -> str:
        pass

    @abstractmethod
    def charge(self, amount: float, currency: str) -> Dict[str, Any]:
        pass

    def format_receipt(self, amount: float, currency: str) -> str:
        # TODO: Implement format_receipt
        raise NotImplementedError("TODO: Implement BasePaymentGateway.format_receipt")

class StripeGateway(BasePaymentGateway):
    # TODO: Implement StripeGateway inheriting from BasePaymentGateway
    pass


# ============================================================================
# AUTOMATED TEST SUITE
# ============================================================================

def run_tests():
    print("=" * 70)
    print("RUNNING AUTOMATED TEST SUITE FOR DAY 15 PRACTICE")
    print("=" * 70)
    score = 0
    total = 6

    # Test 1: Multi-level inheritance
    try:
        t = AutonomousTesla("Model S", 100.0, "12.5")
        res = t.drive()
        expected = "Tesla Model S driving on road. [Battery: 100.0 kWh] [Autopilot v12.5 Active]"
        assert res == expected, f"Expected '{expected}', got '{res}'"
        print("✅ Task 1 Passed: 3-tier Vehicle inheritance & super() chaining works.")
        score += 1
    except Exception as e:
        print(f"❌ Task 1 Failed: {e}")

    # Test 2: Diamond Problem & MRO
    try:
        d = Diamond()
        res = d.process()
        expected = "Diamond -> Left -> Right -> Base"
        assert res == expected, f"Expected '{expected}', got '{res}'"
        assert [cls.__name__ for cls in Diamond.__mro__] == ['Diamond', 'Left', 'Right', 'Base', 'object']
        print("✅ Task 2 Passed: Diamond problem cooperative MRO resolves in C3 order.")
        score += 1
    except Exception as e:
        print(f"❌ Task 2 Failed: {e}")

    # Test 3: Mixins
    try:
        acc = UserAccount("alice_ai", "alice@deepmind.com")
        d = acc.to_dict()
        assert d["username"] == "alice_ai"
        assert d["email"] == "alice@deepmind.com"
        assert "created_timestamp" in d
        print("✅ Task 3 Passed: Pluggable mixins compose into UserAccount cleanly.")
        score += 1
    except Exception as e:
        print(f"❌ Task 3 Failed: {e}")

    # Test 4: Duck Typing
    try:
        mic = MicrophoneStream()
        mp3 = MP3FileStream()
        no_audio = VideoStreamWithoutAudio()
        assert "1024 BYTES" in play_audio_stream(mic)
        assert "2048 BYTES" in play_audio_stream(mp3)
        try:
            play_audio_stream(no_audio)
            assert False, "Should raise TypeError for non-quacking object"
        except TypeError:
            pass
        print("✅ Task 4 Passed: Duck typing audio player works without inheritance.")
        score += 1
    except Exception as e:
        print(f"❌ Task 4 Failed: {e}")

    # Test 5: Protocol
    try:
        c = AnthropicClaude()
        g = OpenAIGPT()
        assert isinstance(c, AIModelProtocol), "Claude does not satisfy AIModelProtocol"
        assert isinstance(g, AIModelProtocol), "GPT does not satisfy AIModelProtocol"
        assert c.predict("test") == "[Claude]: test"
        print("✅ Task 5 Passed: AIModelProtocol structural subtyping verified.")
        score += 1
    except Exception as e:
        print(f"❌ Task 5 Failed: {e}")

    # Test 6: ABC
    try:
        # Verify direct instantiation fails
        try:
            BasePaymentGateway()
            assert False, "Should have raised TypeError"
        except TypeError:
            pass
        stripe = StripeGateway()
        res = stripe.charge(99.0, "USD")
        assert res["status"] == "PAID"
        assert "USD 99.00 via Stripe Payments" in res["receipt"]
        print("✅ Task 6 Passed: BasePaymentGateway ABC and StripeGateway work.")
        score += 1
    except Exception as e:
        print(f"❌ Task 6 Failed: {e}")

    print("=" * 70)
    print(f"TEST SCORE: {score}/{total} PASSED")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

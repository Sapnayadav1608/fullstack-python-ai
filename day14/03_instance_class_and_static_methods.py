"""
Day 14: Object-Oriented Programming (OOP) Part 1
Module 03: Instance Methods, @classmethod, and @staticmethod
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. The Three Method Flavors in Python:
   - Instance Methods (`self`): Bound to the specific instance.
   - Class Methods (`@classmethod` / `cls`): Bound to the class blueprint.
   - Static Methods (`@staticmethod`): Independent utility functions.
2. The Primary Use-Case for `@classmethod`: Alternative Factory Constructors.
3. The Primary Use-Case for `@staticmethod`: Isolated utility/helper logic.
4. Production AI Pattern: `LLMClient` with config loading, inference & cosine math.
"""

import json
import math
from typing import List, Dict, Any, Optional


# ============================================================================
# 1. THE 3 METHOD TYPES: ANATOMY & COMPARISON
# ============================================================================
"""
COMPARISON MATRIX:

| Method Type       | Decorator       | First Argument | Access Scope                          | Typical Use Case                |
| :---------------- | :-------------- | :------------- | :------------------------------------ | :------------------------------ |
| **Instance**      | None            | `self`         | Can access & mutate instance & class  | Normal object behavior & state  |
| **Class Method**  | `@classmethod`  | `cls`          | Can access & mutate class state only  | Factory constructors, registries|
| **Static Method** | `@staticmethod` | None (normal)  | Cannot access instance or class state | Independent pure utility math   |
"""

print("=" * 70)
print("1. THE THREE METHOD TYPES DEMO")
print("=" * 70)

class Temperature:
    # Class attribute: absolute zero in Kelvin
    ABSOLUTE_ZERO_K = 0.0

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    # 1. Instance Method (Operates on self)
    def to_fahrenheit(self) -> float:
        return (self.celsius * 9 / 5) + 32

    # 2. Class Method: Alternative Factory Constructor (Operates on cls)
    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        """Factory constructor that builds a Temperature object from Fahrenheit."""
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @classmethod
    def from_kelvin(cls, kelvin: float) -> "Temperature":
        """Factory constructor from Kelvin with physical validation."""
        if kelvin < cls.ABSOLUTE_ZERO_K:
            raise ValueError(f"Temperature cannot be below Absolute Zero ({cls.ABSOLUTE_ZERO_K}K).")
        celsius = kelvin - 273.15
        return cls(celsius)

    # 3. Static Method: Isolated Utility Function (No self, no cls)
    @staticmethod
    def is_freezing(celsius: float) -> bool:
        """Pure utility function logically grouped inside Temperature namespace."""
        return celsius <= 0.0

    def __repr__(self) -> str:
        return f"Temperature(celsius={self.celsius:.2f}°C, fahrenheit={self.to_fahrenheit():.2f}°F)"


# Testing the 3 methods:
t1 = Temperature(25.0)                                    # Standard __init__
t2 = Temperature.from_fahrenheit(98.6)                    # @classmethod factory
t3 = Temperature.from_kelvin(300.0)                       # @classmethod factory

print(f"t1 (from Celsius 25°C):       {t1}")
print(f"t2 (from Fahrenheit 98.6°F):  {t2}")
print(f"t3 (from Kelvin 300K):        {t3}")

# Static method called on both Class and Instance
print(f"Is -5°C freezing? (Static via Class):    {Temperature.is_freezing(-5.0)}")
print(f"Is 25°C freezing? (Static via Instance): {t1.is_freezing(t1.celsius)}")


# ============================================================================
# 2. WHY `@classmethod` FACTORIES BEAT MULTIPLE `__init__` SIGNATURES
# ============================================================================
"""
In languages like Java or C++, you have constructor overloading (`Temperature(float c)` vs
`Temperature(float f, bool is_f)`).
In Python, a class can have only ONE `__init__` method!
Instead of ugly boolean flags inside `__init__`, Python idiomatic code uses
`@classmethod` factory constructors with expressive names (`from_json`, `from_dict`, `from_csv`).
"""

print("\n" + "=" * 70)
print("2. PRODUCTION FACTORY PATTERN: `from_dict` & `from_json`")
print("=" * 70)

class AIEmbeddingRecord:
    def __init__(self, record_id: str, vector: List[float], metadata: Dict[str, Any]) -> None:
        self.record_id = record_id
        self.vector = vector
        self.metadata = metadata

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AIEmbeddingRecord":
        """Instantiates record from an API response dictionary."""
        return cls(
            record_id=data["id"],
            vector=data["embedding"],
            metadata=data.get("metadata", {})
        )

    @classmethod
    def from_json(cls, json_str: str) -> "AIEmbeddingRecord":
        """Instantiates record from raw JSON payload."""
        parsed = json.loads(json_str)
        return cls.from_dict(parsed)

    def __repr__(self) -> str:
        return f"AIEmbeddingRecord(id={self.record_id!r}, dims={len(self.vector)}, meta={self.metadata})"

sample_json = '{"id": "doc_8841", "embedding": [0.12, 0.94, -0.33], "metadata": {"source": "arxiv"}}'
record = AIEmbeddingRecord.from_json(sample_json)
print(f"Instantiated via @classmethod from_json:\n  {record}")


# ============================================================================
# 3. PRODUCTION AI CLIENT ARCHITECTURE: `LLMClient`
# ============================================================================
"""
A production-grade AI model service orchestrating:
1. Regular instance method: API inference query.
2. Class method: Factory loading pre-configured models (`gpt-4o`, `gemini-1.5-pro`).
3. Static method: Pure mathematical vector cosine similarity comparison.
"""

print("\n" + "=" * 70)
print("3. PRODUCTION AI CLIENT ARCHITECTURE")
print("=" * 70)

class LLMClient:
    # Class registry of default endpoints
    PROVIDER_ENDPOINTS = {
        "gemini": "https://generativelanguage.googleapis.com/v1beta",
        "openai": "https://api.openai.com/v1"
    }

    def __init__(self, model_name: str, api_key: str, endpoint: str, temperature: float = 0.7) -> None:
        self.model_name = model_name
        self.api_key = api_key
        self.endpoint = endpoint
        self.temperature = temperature

    # 1. Instance Method
    def query(self, prompt: str) -> str:
        """Simulates querying the configured LLM."""
        return f"[{self.model_name} @ temp={self.temperature}] Response to: '{prompt}'"

    # 2. Class Method Factory
    @classmethod
    def create_gemini_client(cls, api_key: str, temperature: float = 0.2) -> "LLMClient":
        """Factory specifically configured for Gemini models."""
        return cls(
            model_name="gemini-1.5-pro",
            api_key=api_key,
            endpoint=cls.PROVIDER_ENDPOINTS["gemini"],
            temperature=temperature
        )

    # 3. Static Method Utility
    @staticmethod
    def cosine_similarity(v1: List[float], v2: List[float]) -> float:
        """Computes cosine similarity between two embedding vectors in [-1.0, 1.0]."""
        if len(v1) != len(v2):
            raise ValueError("Vectors must have identical dimensions.")
        dot_product = sum(a * b for a, b in zip(v1, v2))
        norm_a = math.sqrt(sum(a * a for a in v1))
        norm_b = math.sqrt(sum(b * b for b in v2))
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot_product / (norm_a * norm_b)


# Instantiating client using factory method
ai_client = LLMClient.create_gemini_client(api_key="sk-mock-key-12345")
print(f"Client Created: {ai_client.model_name} -> {ai_client.endpoint}")
print(f"Inference Query: {ai_client.query('Explain OOP in Python')}")

# Performing vector similarity using static utility
emb_query = [0.8, 0.6, 0.0]
emb_doc   = [0.6, 0.8, 0.0]
similarity = LLMClient.cosine_similarity(emb_query, emb_doc)
print(f"Cosine Similarity (Static Math): {similarity:.4f} (High semantic match!)")

print("\n" + "=" * 70)
print("DAY 14 MODULE 03: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

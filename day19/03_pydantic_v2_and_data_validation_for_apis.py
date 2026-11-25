"""
===============================================================================
Day 19: Module 03 - Pydantic V2 & Production API Data Validation
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Modern Data Parsing with Pydantic V2, Field & Model Validators
Case Study: Mindifestation Checkout Webhook & Audio Manifest Schemas
===============================================================================

In modern AI APIs (FastAPI, Instructor, LangChain Structured Outputs) and client
e-commerce backends (e.g. Razorpay webhook verification, user access grants),
relying on manual `if/else` dictionary checks leads to security vulnerabilities,
type injection bugs, and malformed database inserts.

Pydantic V2 (re-written in Rust with `pydantic-core`) is the industry standard
for high-speed data validation and serialization in Python.
This module covers:
  1. Pydantic V2 `BaseModel` & `Field()` constraints (ranges, regex, defaults).
  2. Custom `@field_validator`: Validating audio durations, handles, and frequencies.
  3. Cross-Field `@model_validator(mode="after")`: Enforcing complex business rules
     (e.g. if `is_free=True`, then `price_inr` MUST be 0.0).
  4. High-Speed Serialization: `.model_dump()` & `.model_dump_json()`.
  5. Client Real-World Integration: Razorpay payment webhook schema validation for
     the Mindifestation digital sanctuary.
"""

from __future__ import annotations
import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field, field_validator, model_validator


# ============================================================================
# SECTION 1: PYDANTIC V2 BASE MODEL & FIELD CONSTRAINTS
# ============================================================================
print("=" * 75)
print("SECTION 1: PYDANTIC V2 BASE MODEL & FIELD METADATA")
print("=" * 75)

class MeditationProductSchema(BaseModel):
    """
    Validates digital meditation product uploads from the creator admin panel.
    """
    title: str = Field(min_length=3, max_length=120, description="Clean public title")
    slug: str = Field(pattern=r"^[a-z0-9\-]+$", description="URL-safe slug")
    category: Literal["Meditation", "Manifestation", "Affirmations", "Workbooks", "Sound Bath"]
    duration_minutes: int = Field(gt=0, le=360, description="Session length in minutes")
    price_inr: float = Field(ge=0.0, description="Price in Indian Rupees")
    is_free: bool = Field(default=False)
    audio_sample_url: Optional[str] = Field(default=None)
    tags: List[str] = Field(default_factory=list)

    @field_validator("title")
    @classmethod
    def strip_and_capitalize(cls, v: str) -> str:
        return v.strip().title()

    @model_validator(mode="after")
    def verify_free_price_consistency(self) -> MeditationProductSchema:
        """Business Rule: A free resource cannot charge money, and paid cannot be marked free."""
        if self.is_free and self.price_inr > 0.0:
            raise ValueError(f"Product marked as 'is_free=True' but has price of ₹{self.price_inr}")
        if not self.is_free and self.price_inr == 0.0:
            # Auto-correct or flag
            self.is_free = True
        return self


# Test Valid Product
valid_payload = {
    "title": "  divine alignment 432hz sound bath  ",
    "slug": "divine-alignment-432hz",
    "category": "Sound Bath",
    "duration_minutes": 45,
    "price_inr": 499.0,
    "tags": ["432hz", "alignment", "sleep"]
}

product = MeditationProductSchema.model_validate(valid_payload)
print(f"Validated Product: {product.title}")
print(f"Serialized JSON:  {product.model_dump_json(indent=2)}")
assert product.title == "Divine Alignment 432Hz Sound Bath"

# Test Invalidation (Business rule violation)
try:
    MeditationProductSchema.model_validate({
        "title": "Free Morning Guide",
        "slug": "free-morning-guide",
        "category": "Workbooks",
        "duration_minutes": 15,
        "price_inr": 199.0,
        "is_free": True  # Conflict!
    })
except Exception as err:
    print(f"\nCaught Expected Validation Error:\n{err}")


# ============================================================================
# SECTION 2: CLIENT PAYMENT WEBHOOK VALIDATION (Razorpay Schema)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: REAL-WORLD RAZORPAY PAYMENT WEBHOOK SCHEMA (Mindifestation)")
print("=" * 75)

class RazorpayPaymentEntity(BaseModel):
    id: str = Field(pattern=r"^pay_[a-zA-Z0-9]+$")
    amount: int = Field(gt=0, description="Amount in paise (1 INR = 100 paise)")
    currency: Literal["INR", "USD"] = "INR"
    status: Literal["captured", "authorized", "failed"]
    email: str
    contact: str
    order_id: Optional[str] = None


class RazorpayWebhookPayload(BaseModel):
    event: Literal["payment.captured", "payment.failed", "order.paid"]
    created_at: int
    payload: Dict[str, Any]

    def extract_payment(self) -> RazorpayPaymentEntity:
        payment_dict = self.payload.get("payment", {}).get("entity", {})
        return RazorpayPaymentEntity.model_validate(payment_dict)


# Simulate incoming webhook from Razorpay after customer buys guided meditation
sample_webhook = {
    "event": "payment.captured",
    "created_at": 1732529400,
    "payload": {
        "payment": {
            "entity": {
                "id": "pay_O8xK9Z9vY2QxLt",
                "amount": 29900,  # ₹299.00
                "currency": "INR",
                "status": "captured",
                "email": "customer@gmail.com",
                "contact": "+919876543210",
                "order_id": "order_EKfLwp8Cmq0w2P"
            }
        }
    }
}

webhook = RazorpayWebhookPayload.model_validate(sample_webhook)
payment = webhook.extract_payment()

print(f"Received Webhook Event: {webhook.event}")
print(f"Payment ID:             {payment.id}")
print(f"Customer Email:         {payment.email}")
print(f"Captured Amount:        ₹{payment.amount / 100:.2f} {payment.currency}")
assert payment.status == "captured"
assert payment.amount / 100 == 299.0

print("\n" + "=" * 75)
print("Module 03 Complete: Pydantic V2 & Production API Validation Mastered!")
print("=" * 75)

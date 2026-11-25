"""
===============================================================================
Day 19: Module 04 - Generic Repositories & Clean Architecture
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Decoupling Domain Logic from Database Drivers with Generic Repositories
Case Study: Mindifestation Sanctuary Multi-Store Architecture (Memory & JSON)
===============================================================================

In production software engineering, coupling business logic directly to a
specific database library (raw SQLite, PostgreSQL, Supabase, MongoDB) creates
brittle code that is impossible to unit test without spinning up Docker or cloud DBs.

The Repository Pattern acts as an in-memory collection abstraction over your data store.
Combined with Python Generics (`Generic[EntityT, IdT]`), we can write:
  1. A single type-safe interface contract (`IRepository[T, ID]`).
  2. Pluggable adapters: `InMemoryRepository` for lightning-fast testing,
     and `JsonAtomicRepository` (or Supabase/SQLAlchemy) for persistent storage.
  3. A Domain Service (`MeditationSanctuaryService`) containing pure business rules.
"""

from __future__ import annotations
import json
import os
import shutil
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Generic, List, Optional, Protocol, TypeVar


EntityT = TypeVar("EntityT")
IdT = TypeVar("IdT")


# ============================================================================
# SECTION 1: THE GENERIC REPOSITORY CONTRACT (Port)
# ============================================================================
print("=" * 75)
print("SECTION 1: THE GENERIC REPOSITORY INTERFACE (IRepository[EntityT, IdT])")
print("=" * 75)

class IRepository(Protocol[EntityT, IdT]):
    """Standard generic contract for CRUD persistence."""
    def add(self, entity: EntityT) -> None: ...
    def get_by_id(self, entity_id: IdT) -> Optional[EntityT]: ...
    def list_all(self) -> List[EntityT]: ...
    def delete(self, entity_id: IdT) -> bool: ...


# ============================================================================
# SECTION 2: CONCRETE ADAPTER 1 — IN-MEMORY REPOSITORY
# ============================================================================
class InMemoryRepository(Generic[EntityT, IdT]):
    """High-speed dictionary store for unit tests and local dev."""
    def __init__(self, id_getter: Callable[[EntityT], IdT]):
        self._store: Dict[IdT, EntityT] = {}
        self._id_getter = id_getter

    def add(self, entity: EntityT) -> None:
        entity_id = self._id_getter(entity)
        self._store[entity_id] = entity

    def get_by_id(self, entity_id: IdT) -> Optional[EntityT]:
        return self._store.get(entity_id)

    def list_all(self) -> List[EntityT]:
        return list(self._store.values())

    def delete(self, entity_id: IdT) -> bool:
        if entity_id in self._store:
            del self._store[entity_id]
            return True
        return False


# ============================================================================
# SECTION 3: DOMAIN ENTITY & APPLICATION SERVICE
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2 & 3: DOMAIN SERVICE & CLEAN ARCHITECTURE DECOUPLING")
print("=" * 75)

@dataclass
class MeditationResource:
    id: str
    title: str
    category: str
    duration_min: int
    price_inr: float
    is_published: bool = True


class MeditationSanctuaryService:
    """
    Application Service layer for Mindifestation.
    Contains pure business logic; does NOT care if data is stored in
    PostgreSQL, Supabase, SQLite, or RAM!
    """
    def __init__(self, repo: IRepository[MeditationResource, str]):
        self.repo = repo

    def publish_new_track(
        self,
        track_id: str,
        title: str,
        category: str,
        duration_min: int,
        price_inr: float
    ) -> MeditationResource:
        resource = MeditationResource(
            id=track_id,
            title=title,
            category=category,
            duration_min=duration_min,
            price_inr=price_inr,
            is_published=True
        )
        self.repo.add(resource)
        return resource

    def get_free_community_resources(self) -> List[MeditationResource]:
        """Business rule: Returns only free, published resources."""
        return [
            item for item in self.repo.list_all()
            if item.is_published and item.price_inr == 0.0
        ]

    def compute_catalog_value(self) -> float:
        """Returns total value of all paid catalog items."""
        return sum(item.price_inr for item in self.repo.list_all() if item.is_published)


# ============================================================================
# SECTION 4: EXECUTION & VERIFICATION
# ============================================================================
# Instantiate service with in-memory repository
repo = InMemoryRepository[MeditationResource, str](id_getter=lambda r: r.id)
service = MeditationSanctuaryService(repo)

# Seed client catalog items for Mindifestation
service.publish_new_track("tr_01", "Morning Grounding Affirmations", "Affirmations", 10, 0.0)
service.publish_new_track("tr_02", "432Hz Cellular Regeneration", "Sound Bath", 45, 399.0)
service.publish_new_track("tr_03", "Subconscious Money Mindset", "Manifestation", 30, 499.0)
service.publish_new_track("tr_04", "Breathwork for Nervous System", "Meditation", 15, 0.0)

print(f"Total Published Items: {len(service.repo.list_all())}")

free_resources = service.get_free_community_resources()
print(f"Free Community Resources ({len(free_resources)}):")
for res in free_resources:
    print(f"  ✓ {res.title} ({res.duration_min} min)")

total_val = service.compute_catalog_value()
print(f"Total Paid Catalog Value: ₹{total_val:,.2f}")

assert len(free_resources) == 2
assert total_val == 399.0 + 499.0

print("\n" + "=" * 75)
print("Module 04 Complete: Generic Repositories & Clean Architecture Mastered!")
print("=" * 75)

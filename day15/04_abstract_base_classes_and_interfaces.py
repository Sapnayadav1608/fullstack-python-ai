"""
Day 15: Advanced Object-Oriented Programming (OOP) Part 2
Module 04: Abstract Base Classes (ABCs), Interfaces & Design Patterns
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Abstract Base Classes (ABCs): Enforcing contracts and architectural boundaries.
2. The `abc` standard library module: `ABC` and `@abstractmethod`.
3. Instantiation Prevention: Why Python raises TypeError for incomplete classes.
4. Abstract Properties: Combining `@property` with `@abstractmethod`.
5. ABCs vs Protocols: Nominal inheritance vs Structural duck typing.
6. Production Pattern: Pluggable AI Vector Database Adapter Architecture (Pinecone & ChromaDB).
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import math


# ============================================================================
# 1. ABSTRACT BASE CLASSES & THE @abstractmethod CONTRACT
# ============================================================================
"""
WHY DO WE NEED ABCs?
In large enterprise systems, you want to guarantee that ANY developer who builds
a plugin or database adapter implements all mandatory methods.
Without ABCs, missing methods cause sudden 3:00 AM production crashes (`AttributeError`)!
With `abc.ABC`, Python halts object creation at instantiation time if any abstract
method is missing!
"""

print("=" * 70)
print("1. THE ABC CONTRACT & INSTANTIATION PREVENTION")
print("=" * 70)

class BaseVectorDatabase(ABC):
    """Abstract interface defining required behavior for any Vector DB provider."""

    def __init__(self, index_name: str, dimension: int) -> None:
        self.index_name = index_name
        self.dimension = dimension

    # Abstract Property: All subclasses must expose an engine name
    @property
    @abstractmethod
    def engine_name(self) -> str:
        """Returns the brand name of the vector database engine."""
        pass

    # Abstract Method 1: Vector insertion
    @abstractmethod
    def upsert(self, vector_id: str, vector: List[float], metadata: Dict[str, Any]) -> bool:
        """Inserts or updates an embedding vector."""
        pass

    # Abstract Method 2: Vector similarity search
    @abstractmethod
    def query(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """Searches for top_k most similar vectors."""
        pass

    # Concrete Helper Method (Shared by all subclasses!)
    def validate_dimension(self, vector: List[float]) -> bool:
        if len(vector) != self.dimension:
            raise ValueError(f"Vector dim {len(vector)} does not match index dim {self.dimension}.")
        return True


# Attempting to instantiate the Abstract Base Class directly raises TypeError!
try:
    base_db = BaseVectorDatabase("test_index", 1536) # type: ignore
except TypeError as e:
    print(f"🛡️  Direct Instantiation Guard: {e}")


# ============================================================================
# 2. CONCRETE IMPLEMENTATION: PINECONE ADAPTER
# ============================================================================

class PineconeAdapter(BaseVectorDatabase):
    """Concrete production adapter for Pinecone Cloud Vector DB."""

    def __init__(self, index_name: str, dimension: int, environment: str = "us-east-1") -> None:
        super().__init__(index_name, dimension)
        self.environment = environment
        self._in_memory_store: Dict[str, Dict[str, Any]] = {}

    @property
    def engine_name(self) -> str:
        return f"Pinecone Cloud [{self.environment}]"

    def upsert(self, vector_id: str, vector: List[float], metadata: Dict[str, Any]) -> bool:
        self.validate_dimension(vector)
        self._in_memory_store[vector_id] = {"vector": vector, "metadata": metadata}
        print(f"  🌲 [{self.engine_name}] Upserted '{vector_id}' into '{self.index_name}'")
        return True

    def query(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        self.validate_dimension(query_vector)
        print(f"  🌲 [{self.engine_name}] Querying top {top_k} nearest neighbors...")
        # Simulate similarity match
        results = []
        for vid, data in list(self._in_memory_store.items())[:top_k]:
            results.append({"id": vid, "score": 0.98, "metadata": data["metadata"]})
        return results


# ============================================================================
# 3. CONCRETE IMPLEMENTATION: CHROMADB LOCAL ADAPTER
# ============================================================================

class ChromaDBAdapter(BaseVectorDatabase):
    """Concrete production adapter for local embedded ChromaDB."""

    def __init__(self, index_name: str, dimension: int, persist_directory: str = "./chroma_db") -> None:
        super().__init__(index_name, dimension)
        self.persist_directory = persist_directory
        self._in_memory_store: Dict[str, Dict[str, Any]] = {}

    @property
    def engine_name(self) -> str:
        return f"ChromaDB Embedded ({self.persist_directory})"

    def upsert(self, vector_id: str, vector: List[float], metadata: Dict[str, Any]) -> bool:
        self.validate_dimension(vector)
        self._in_memory_store[vector_id] = {"vector": vector, "metadata": metadata}
        print(f"  🌈 [{self.engine_name}] Upserted '{vector_id}'")
        return True

    def query(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        self.validate_dimension(query_vector)
        print(f"  🌈 [{self.engine_name}] Performing HNSW index scan for top {top_k}...")
        return [{"id": vid, "score": 0.94, "metadata": data["metadata"]} for vid, data in self._in_memory_store.items()][:top_k]


# ============================================================================
# 4. TESTING THE PLUGGABLE VECTOR DATABASE ARCHITECTURE
# ============================================================================

print("\n" + "=" * 70)
print("2. PLUGGABLE VECTOR DB ADAPTERS IN ACTION")
print("=" * 70)

# The client application only relies on BaseVectorDatabase:
def run_ai_rag_pipeline(vector_db: BaseVectorDatabase) -> None:
    print(f"\n🚀 Running RAG Search Pipeline with Engine: {vector_db.engine_name}")
    mock_vector = [0.15, -0.42, 0.88]
    vector_db.upsert("doc_001", mock_vector, {"title": "Python OOP Guide", "author": "DeepMind"})
    matches = vector_db.query(mock_vector, top_k=1)
    print(f"   Top Match: {matches}")

# Switch between cloud Pinecone and local ChromaDB with ZERO code change!
pinecone = PineconeAdapter("production-embeddings", dimension=3)
chroma = ChromaDBAdapter("local-embeddings", dimension=3)

run_ai_rag_pipeline(pinecone)
run_ai_rag_pipeline(chroma)

print("\n" + "=" * 70)
print("DAY 15 MODULE 04: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

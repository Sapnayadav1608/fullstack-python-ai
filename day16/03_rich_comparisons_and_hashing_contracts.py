"""
================================================================================
DAY 16: PYTHON DATA MODEL & MAGIC METHODS (PART 3)
Module 03: Rich Comparisons & The Hashing Protocol
================================================================================
Topics Covered:
  1. Rich Comparisons: __eq__, __ne__, __lt__, __le__, __gt__, __ge__
  2. Eliminating Boilerplate with @functools.total_ordering
  3. The Sacred Python Contract: The Hashability Invariant (a == b => hash(a) == hash(b))
  4. Why Implementing __eq__ Automatically Sets __hash__ = None
  5. The Mutable Hash Trap: Why mutable objects MUST NOT be hashable
  6. Enterprise AI Pattern: DocumentChunk with Deduplication & Similarity Ranking
================================================================================
"""

import functools
from typing import Any, Tuple, Optional


# ==============================================================================
# SECTION 1 & 2: RICH COMPARISONS & @functools.total_ordering
# ==============================================================================
# Implementing all 6 comparison methods (__eq__, __ne__, __lt__, __le__, __gt__, __ge__)
# involves significant repetitive boilerplate.
#
# Standard Library Solution: @functools.total_ordering
#   - You implement __eq__ and EXACTLY ONE of: __lt__, __le__, __gt__, or __ge__.
#   - The decorator automatically synthesizes the other 4 comparison operators!

@functools.total_ordering
class ModelBenchmarkScore:
    """Benchmark evaluation score with total ordering support."""
    def __init__(self, model_name: str, mmlu_score: float, latency_ms: float):
        self.model_name = model_name
        self.mmlu_score = float(mmlu_score)
        self.latency_ms = float(latency_ms)

    def __repr__(self) -> str:
        return f"Score({self.model_name}: MMLU={self.mmlu_score:.1f}%, {self.latency_ms:.0f}ms)"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ModelBenchmarkScore):
            return NotImplemented
        # Two models are considered equal in ranking if MMLU score and latency match
        return (self.mmlu_score, self.latency_ms) == (other.mmlu_score, other.latency_ms)

    def __lt__(self, other: Any) -> bool:
        """
        Custom AI Ordering Logic:
          Higher MMLU score wins. If tied, lower latency wins!
        """
        if not isinstance(other, ModelBenchmarkScore):
            return NotImplemented
        if self.mmlu_score != other.mmlu_score:
            # We want higher score to be 'greater than', so self < other means lower MMLU:
            return self.mmlu_score < other.mmlu_score
        # Tie breaker: lower latency is better (greater), so higher latency is 'less than':
        return self.latency_ms > other.latency_ms


def demonstrate_total_ordering():
    print("=" * 70)
    print("SECTION 1 & 2: RICH COMPARISONS VIA @functools.total_ordering")
    print("=" * 70)

    gpt4 = ModelBenchmarkScore("GPT-4o", 88.5, 420.0)
    claude = ModelBenchmarkScore("Claude-3.5", 88.5, 380.0)  # Same MMLU, lower latency (better!)
    gemini = ModelBenchmarkScore("Gemini-Flash", 78.9, 150.0)

    print(f"gpt4:   {gpt4}")
    print(f"claude: {claude}")
    print(f"gemini: {gemini}")

    # Total ordering synthesis tests:
    print(f"\ngpt4 == claude: {gpt4 == claude} (Different latency)")
    print(f"gpt4 < claude:  {gpt4 < claude}  (Claude has lower latency, so Claude > GPT-4o)")
    print(f"gpt4 > gemini:  {gpt4 > gemini}  (Synthesized by @total_ordering)")
    print(f"gemini <= gpt4: {gemini <= gpt4} (Synthesized by @total_ordering)")

    # Natural sorting via Python's timsort:
    leaderboard = [gpt4, claude, gemini]
    leaderboard.sort(reverse=True)  # Best first
    print("\n--- AI Leaderboard (Sorted with total ordering) ---")
    for rank, model in enumerate(leaderboard, start=1):
        print(f"  #{rank}: {model}")


# ==============================================================================
# SECTION 3, 4 & 5: THE SACRED HASHABILITY CONTRACT
# ==============================================================================
# The Python Data Model Rule (PEP 3119 & Language Ref):
#   1. If a class does NOT define __eq__, it inherits object.__eq__ (identity `is`)
#      and object.__hash__ (derived from memory address id()).
#   2. As soon as you define __eq__, Python AUTOMATICALLY sets `__hash__ = None`!
#      Attempting hash(instance) or placing it in a set/dict raises:
#      TypeError: unhashable type: 'YourClass'
#   3. THE GOLDEN INVARIANT:
#      If a == b is True, then hash(a) == hash(b) MUST be True!
#      (The reverse is NOT required due to hash collisions, but desirable for O(1)).
#   4. MUTABILITY TRAP:
#      If an object's hash changes after it is inserted into a hash table (set or dict),
#      it will remain trapped in the wrong hash bucket and becomes impossible to find!
#      Therefore: ONLY HASH IMMUTABLE ATTRIBUTES.

class UnhashableByDefault:
    def __init__(self, val: int):
        self.val = val

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, UnhashableByDefault) and self.val == other.val
    # Note: __hash__ is NOT defined here. Python sets __hash__ = None automatically!


class ProperlyHashableEntity:
    """An immutable entity that correctly participates in set/dict hashing."""
    def __init__(self, entity_id: str, namespace: str):
        self._entity_id = entity_id
        self._namespace = namespace

    @property
    def entity_id(self) -> str:
        return self._entity_id

    @property
    def namespace(self) -> str:
        return self._namespace

    def __repr__(self) -> str:
        return f"Entity({self._namespace}:{self._entity_id})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ProperlyHashableEntity):
            return NotImplemented
        return (self._entity_id, self._namespace) == (other._entity_id, other._namespace)

    def __hash__(self) -> int:
        """Hash must be derived from the EXACT SAME fields used in __eq__!"""
        return hash((self._entity_id, self._namespace))


def demonstrate_hashing_contracts():
    print("\n" + "=" * 70)
    print("SECTION 3 & 4: THE HASHABILITY CONTRACT & THE __hash__ = None TRAP")
    print("=" * 70)

    # 1. Unhashable error demonstration
    obj1 = UnhashableByDefault(42)
    obj2 = UnhashableByDefault(42)
    print(f"obj1 == obj2: {obj1 == obj2}")
    try:
        hash(obj1)
    except TypeError as e:
        print(f"Caught expected TypeError on hash(obj1): {e}")

    # 2. Properly hashable entity demonstration
    e1 = ProperlyHashableEntity("chunk_1001", "rag_docs")
    e2 = ProperlyHashableEntity("chunk_1001", "rag_docs")  # Duplicate
    e3 = ProperlyHashableEntity("chunk_1002", "rag_docs")

    print(f"\ne1 == e2: {e1 == e2}")
    print(f"hash(e1) == hash(e2): {hash(e1) == hash(e2)} (Hash: {hash(e1)})")

    # Set deduplication:
    entity_set = {e1, e2, e3}
    print(f"Set length after inserting e1, e2 (duplicate), e3: {len(entity_set)}")
    print(f"Deduplicated set contents: {entity_set}")

    # Dictionary key lookup:
    cache = {e1: "Vector embedding cached"}
    print(f"Cache lookup using e2 (equal key): {cache[e2]}")


# ==============================================================================
# SECTION 6: ENTERPRISE AI PATTERN — DocumentChunk
# ==============================================================================
# In Retrieval-Augmented Generation (RAG) pipelines:
#   - Document chunks must be deduplicated in O(1) time using sets/dicts.
#   - Chunks must be sorted by cosine similarity relevance score.

@functools.total_ordering
class DocumentChunk:
    """
    Production RAG Document Chunk:
      - Hashable by immutable chunk_id & doc_hash (for O(1) set deduplication)
      - Orderable by similarity score (for top-k ranking)
    """
    __slots__ = ("_chunk_id", "_text", "_doc_hash", "similarity_score")

    def __init__(self, chunk_id: str, text: str, similarity_score: float = 0.0):
        self._chunk_id = chunk_id
        self._text = text
        self._doc_hash = hash(text)
        self.similarity_score = float(similarity_score)

    @property
    def chunk_id(self) -> str:
        return self._chunk_id

    @property
    def text(self) -> str:
        return self._text

    def __repr__(self) -> str:
        snippet = self._text[:35] + ("..." if len(self._text) > 35 else "")
        return f"DocumentChunk(id={self._chunk_id!r}, score={self.similarity_score:.3f}, text={snippet!r})"

    def __eq__(self, other: Any) -> bool:
        """Identity & deduplication equality: matching chunk_id and text hash."""
        if not isinstance(other, DocumentChunk):
            return NotImplemented
        return (self._chunk_id, self._doc_hash) == (other._chunk_id, other._doc_hash)

    def __hash__(self) -> int:
        """Enables O(1) set storage and dict lookups in vector retrieval deduplicators."""
        return hash((self._chunk_id, self._doc_hash))

    def __lt__(self, other: Any) -> bool:
        """Sorting comparison: higher similarity score ranks higher."""
        if not isinstance(other, DocumentChunk):
            return NotImplemented
        return self.similarity_score < other.similarity_score


def demonstrate_rag_chunk_pattern():
    print("\n" + "=" * 70)
    print("SECTION 6: ENTERPRISE AI PATTERN — RAG DocumentChunk")
    print("=" * 70)

    c1 = DocumentChunk("c_01", "Python descriptors power the property decorator under the hood.", 0.88)
    c2 = DocumentChunk("c_02", "Vector databases index embeddings using HNSW graphs.", 0.94)
    c3 = DocumentChunk("c_01", "Python descriptors power the property decorator under the hood.", 0.88)  # Duplicate!
    c4 = DocumentChunk("c_03", "C3 Linearization guarantees deterministic MRO.", 0.72)

    raw_retrieved = [c1, c2, c3, c4]
    print(f"Raw chunks retrieved: {len(raw_retrieved)}")

    # O(1) Set Deduplication
    unique_chunks = list(set(raw_retrieved))
    print(f"Unique chunks after set() deduplication: {len(unique_chunks)}")

    # Top-K Ranking (Sorted highest score first)
    unique_chunks.sort(reverse=True)
    print("\n--- Top-K RAG Search Results (Ranked) ---")
    for rank, chunk in enumerate(unique_chunks, start=1):
        print(f"  Rank #{rank}: {chunk}")


if __name__ == "__main__":
    demonstrate_total_ordering()
    demonstrate_hashing_contracts()
    demonstrate_rag_chunk_pattern()

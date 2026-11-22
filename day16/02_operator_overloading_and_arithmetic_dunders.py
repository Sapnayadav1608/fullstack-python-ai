"""
================================================================================
DAY 16: PYTHON DATA MODEL & MAGIC METHODS (PART 2)
Module 02: Operator Overloading & Arithmetic Protocols
================================================================================
Topics Covered:
  1. Operator Overloading Fundamentals: Mapping Symbols to Dunder Methods
  2. The NotImplemented Golden Rule: Why you must never raise TypeError directly
  3. Reflected / Reversed Operators (__radd__, __rmul__) for Heterogeneous Math
  4. In-Place Arithmetic (__iadd__, __imul__) for In-Memory Mutation
  5. The Modern Matrix Multiplication Protocol (@ / __matmul__ - PEP 465)
  6. Unary Operators: __neg__, __pos__, __abs__
  7. Production AI Class: Tensor1D supporting Vector math, Scaling, and Dot Product
================================================================================
"""

import math
from typing import List, Union, Sequence


# ==============================================================================
# SECTION 1 & 2: THE NotImplemented SINGLETON & REFLECTED OPERATORS
# ==============================================================================
# The Python Dispatch Algorithm for `a + b`:
#   1. Call type(a).__add__(a, b).
#   2. If it returns a result (not NotImplemented), that is returned.
#   3. If it returns NotImplemented (or isn't implemented):
#      Python calls type(b).__radd__(b, a) (the Reflected / Reversed method!).
#   4. If type(b).__radd__ also returns NotImplemented, Python raises TypeError:
#      "unsupported operand type(s) for +: 'type(a)' and 'type(b)'".
#
# RULE: If your method doesn't support the right-hand operand, return NotImplemented.
# Raising TypeError directly aborts the dispatch algorithm and prevents the right-hand
# operand from attempting its __radd__!

class Budget:
    """Represents a financial compute allocation in USD."""
    def __init__(self, amount: float):
        self.amount = float(amount)

    def __repr__(self) -> str:
        return f"Budget(${self.amount:.2f})"

    def __add__(self, other: Any) -> "Budget":
        if isinstance(other, Budget):
            return Budget(self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Budget(self.amount + other)
        # CRITICAL: Return NotImplemented so Python tries other.__radd__!
        return NotImplemented

    def __radd__(self, other: Any) -> "Budget":
        # Supports `100 + Budget(50)` where left operand is int/float!
        return self.__add__(other)


def demonstrate_not_implemented_and_radd():
    print("=" * 70)
    print("SECTION 1 & 2: THE NotImplemented SINGLETON & REFLECTED OPERATORS")
    print("=" * 70)

    b1 = Budget(150.00)
    b2 = Budget(75.50)

    # 1. Budget + Budget (calls b1.__add__(b2))
    print(f"b1 + b2:          {b1 + b2}")

    # 2. Budget + float (calls b1.__add__(50.0))
    print(f"b1 + 50.0:        {b1 + 50.0}")

    # 3. float + Budget (float.__add__ returns NotImplemented -> calls b1.__radd__(50.0))
    print(f"50.0 + b1:        {50.0 + b1}")

    # 4. Invalid type: Budget + "invalid"
    try:
        _ = b1 + "not_a_number"
    except TypeError as e:
        print(f"Graceful TypeError on unsupported type: {e}")


# ==============================================================================
# SECTION 3, 4 & 5: AI PRODUCTION CLASS — Tensor1D
# ==============================================================================
# In Machine Learning and AI, mathematical abstractions like Tensors and Vectors
# represent embeddings, weights, and activations.
#
# Protocols implemented:
#   - Binary Arithmetic: __add__, __sub__, __mul__, __truediv__
#   - Reflected Arithmetic: __radd__, __rmul__ (e.g. 3.0 * tensor)
#   - In-Place Arithmetic: __iadd__, __imul__ (prevents unnecessary re-allocations)
#   - Matrix Multiplication: __matmul__ (@ operator for Dot Product / Projection)
#   - Unary Math: __neg__ (-v), __abs__ (Euclidean L2 norm ||v||)

class Tensor1D:
    """
    Production-grade 1-Dimensional Numerical Tensor / Embedding Vector.
    Implements the complete Python Arithmetic and Matrix Multiplication Protocols.
    """
    __slots__ = ("_data",)

    def __init__(self, elements: Sequence[Union[int, float]]):
        self._data = [float(x) for x in elements]

    @property
    def data(self) -> List[float]:
        return self._data

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        formatted = ", ".join(f"{x:.4f}" for x in self._data[:6])
        if len(self._data) > 6:
            formatted += f", ... ({len(self._data) - 6} more)"
        return f"Tensor1D([{formatted}], shape=({len(self._data)},))"

    # --------------------------------------------------------------------------
    # Unary Operators
    # --------------------------------------------------------------------------
    def __neg__(self) -> "Tensor1D":
        """Negates all elements: -t"""
        return Tensor1D([-x for x in self._data])

    def __pos__(self) -> "Tensor1D":
        """Unary positive: +t"""
        return Tensor1D([+x for x in self._data])

    def __abs__(self) -> float:
        """Euclidean L2 Norm: abs(t) -> sqrt(sum(x^2))"""
        return math.sqrt(sum(x * x for x in self._data))

    # --------------------------------------------------------------------------
    # Binary Addition (+) and Reflected (__radd__)
    # --------------------------------------------------------------------------
    def __add__(self, other: Any) -> "Tensor1D":
        if isinstance(other, Tensor1D):
            if len(self) != len(other):
                raise ValueError(f"Shape mismatch in Tensor addition: ({len(self)},) vs ({len(other)},)")
            return Tensor1D([a + b for a, b in zip(self._data, other._data)])
        elif isinstance(other, (int, float)):
            # Broadcast scalar addition across all dimensions
            return Tensor1D([a + other for a in self._data])
        return NotImplemented

    def __radd__(self, other: Any) -> "Tensor1D":
        # Addition is commutative: scalar + tensor == tensor + scalar
        return self.__add__(other)

    # --------------------------------------------------------------------------
    # Binary Subtraction (-) and Reflected (__rsub__)
    # --------------------------------------------------------------------------
    def __sub__(self, other: Any) -> "Tensor1D":
        if isinstance(other, Tensor1D):
            if len(self) != len(other):
                raise ValueError(f"Shape mismatch in Tensor subtraction: ({len(self)},) vs ({len(other)},)")
            return Tensor1D([a - b for a, b in zip(self._data, other._data)])
        elif isinstance(other, (int, float)):
            return Tensor1D([a - other for a in self._data])
        return NotImplemented

    def __rsub__(self, other: Any) -> "Tensor1D":
        # other - self (non-commutative)
        if isinstance(other, (int, float)):
            return Tensor1D([other - a for a in self._data])
        return NotImplemented

    # --------------------------------------------------------------------------
    # Binary Multiplication (*) — Element-wise and Scalar
    # --------------------------------------------------------------------------
    def __mul__(self, other: Any) -> "Tensor1D":
        """Element-wise Hadamard product or scalar scaling."""
        if isinstance(other, Tensor1D):
            if len(self) != len(other):
                raise ValueError(f"Shape mismatch in Hadamard product: ({len(self)},) vs ({len(other)},)")
            return Tensor1D([a * b for a, b in zip(self._data, other._data)])
        elif isinstance(other, (int, float)):
            return Tensor1D([a * other for a in self._data])
        return NotImplemented

    def __rmul__(self, other: Any) -> "Tensor1D":
        # Scalar * Tensor == Tensor * Scalar
        return self.__mul__(other)

    # --------------------------------------------------------------------------
    # Matrix Multiplication (@) — Dot Product (PEP 465)
    # --------------------------------------------------------------------------
    def __matmul__(self, other: Any) -> float:
        """
        Dot Product / Vector Inner Product using the @ operator:
          v1 @ v2 = sum(v1[i] * v2[i])
        """
        if isinstance(other, Tensor1D):
            if len(self) != len(other):
                raise ValueError(f"Shape mismatch in Dot Product: ({len(self)},) vs ({len(other)},)")
            return sum(a * b for a, b in zip(self._data, other._data))
        return NotImplemented

    # --------------------------------------------------------------------------
    # In-Place Operators (+=, *=) — In-Memory Mutation
    # --------------------------------------------------------------------------
    def __iadd__(self, other: Any) -> "Tensor1D":
        """In-place addition: self += other (mutates _data directly without new object)."""
        if isinstance(other, Tensor1D):
            if len(self) != len(other):
                raise ValueError(f"Shape mismatch in in-place addition: ({len(self)},) vs ({len(other)},)")
            for i in range(len(self._data)):
                self._data[i] += other._data[i]
            return self
        elif isinstance(other, (int, float)):
            for i in range(len(self._data)):
                self._data[i] += float(other)
            return self
        return NotImplemented

    def __imul__(self, other: Any) -> "Tensor1D":
        """In-place scaling: self *= other"""
        if isinstance(other, (int, float)):
            for i in range(len(self._data)):
                self._data[i] *= float(other)
            return self
        elif isinstance(other, Tensor1D):
            if len(self) != len(other):
                raise ValueError("Shape mismatch in in-place Hadamard product")
            for i in range(len(self._data)):
                self._data[i] *= other._data[i]
            return self
        return NotImplemented

    def cosine_similarity(self, other: "Tensor1D") -> float:
        """Computes Cosine Similarity between two embedding vectors: (A @ B) / (||A|| * ||B||)"""
        dot = self @ other
        norm_a = abs(self)
        norm_b = abs(other)
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot / (norm_a * norm_b)


def demonstrate_tensor_math():
    print("\n" + "=" * 70)
    print("SECTION 3: VECTOR MATH, BROADCASTING & SCALAR OPERATORS")
    print("=" * 70)

    v1 = Tensor1D([1.0, 2.0, 3.0])
    v2 = Tensor1D([4.0, 5.0, 6.0])

    print(f"v1: {v1}")
    print(f"v2: {v2}")

    # Vector + Vector
    v_sum = v1 + v2
    print(f"v1 + v2:           {v_sum}")

    # Vector - Vector
    v_diff = v2 - v1
    print(f"v2 - v1:           {v_diff}")

    # Scalar broadcasting: Vector + 10.0 and 10.0 + Vector
    print(f"v1 + 10.0:         {v1 + 10.0}")
    print(f"10.0 + v1 (radd):  {10.0 + v1}")

    # Scalar scaling: Vector * 2.5 and 2.5 * Vector
    print(f"v1 * 2.5:          {v1 * 2.5}")
    print(f"2.5 * v1 (rmul):  {2.5 * v1}")

    # Element-wise multiplication
    print(f"v1 * v2 (Hadamard): {v1 * v2}")

    # Unary negation & L2 Norm
    print(f"-v1 (Negation):    {-v1}")
    print(f"abs(v1) (L2 Norm): {abs(v1):.4f}")


def demonstrate_dot_product_and_in_place():
    print("\n" + "=" * 70)
    print("SECTION 4: DOT PRODUCT (@) & IN-PLACE MUTATION (+=)")
    print("=" * 70)

    # 1. Dot Product (@ / __matmul__)
    # Orthogonal vectors (perpendicular): dot product == 0.0
    x_axis = Tensor1D([1.0, 0.0, 0.0])
    y_axis = Tensor1D([0.0, 1.0, 0.0])
    print(f"x_axis @ y_axis (Orthogonal): {x_axis @ y_axis}")

    # AI Embedding similarity demo
    prompt_emb = Tensor1D([0.82, 0.14, 0.55, 0.02])
    doc1_emb = Tensor1D([0.80, 0.18, 0.52, 0.05])    # High relevance
    doc2_emb = Tensor1D([-0.75, 0.85, -0.10, 0.00])  # Irrelevant

    sim_1 = prompt_emb.cosine_similarity(doc1_emb)
    sim_2 = prompt_emb.cosine_similarity(doc2_emb)

    print(f"\nCosine Similarity (Prompt vs Doc1): {sim_1:.4f} (Highly Relevant)")
    print(f"Cosine Similarity (Prompt vs Doc2): {sim_2:.4f} (Unrelated)")

    # 2. In-place Mutation
    t = Tensor1D([10.0, 20.0, 30.0])
    orig_id = id(t)
    print(f"\nBefore in-place: {t} (id={orig_id})")
    
    t += Tensor1D([1.0, 2.0, 3.0])
    print(f"After t += [1,2,3]: {t} (id={id(t)})")
    print(f"Memory preserved (same object mutated): {id(t) == orig_id}")

    t *= 2.0
    print(f"After t *= 2.0:     {t} (id={id(t)})")


if __name__ == "__main__":
    demonstrate_not_implemented_and_radd()
    demonstrate_tensor_math()
    demonstrate_dot_product_and_in_place()

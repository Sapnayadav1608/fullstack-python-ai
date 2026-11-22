"""
================================================================================
DAY 16: PYTHON DATA MODEL & MAGIC METHODS — HANDS-ON WORKBOOK
================================================================================
Student: Sapna Yadav (@Sapnayadav1608)
Track: 30-Day Full Stack Python + AI Engineering Challenge

Instructions:
  - Complete the 6 challenge classes below.
  - Each task has clear docstrings, requirements, and # TODO comments.
  - Run this file directly to execute the comprehensive automated test suite:
      python day16/my_practice.py
================================================================================
"""

import functools
import math
from typing import Any, List, Union, Tuple, Iterator, Optional


# ==============================================================================
# TASK 1: OBJECT REPRESENTATION & TRUTHINESS PROTOCOL
# ==============================================================================
class Vector2D:
    """
    Task 1: Implement custom representation and truthiness for a 2D Vector.
    
    Requirements:
      1. __init__(self, x: float, y: float): Store self.x and self.y as floats.
      2. __repr__(self): Formal representation: "Vector2D(x=3.0, y=4.0)".
      3. __str__(self): Informal user string: "(3.0, 4.0)".
      4. __bool__(self): Return True ONLY if the vector is NOT at origin (i.e. x != 0 or y != 0).
         At origin (0.0, 0.0), bool(v) must evaluate to False.
    """
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __bool__(self) -> bool:
        return bool(self.x != 0.0 or self.y != 0.0)


# ==============================================================================
# TASK 2: ARITHMETIC & REFLECTED OPERATORS WITH NotImplemented
# ==============================================================================
class Money:
    """
    Task 2: Implement robust currency arithmetic with reflected operators.
    
    Requirements:
      1. __init__(self, amount: float, currency: str = "USD"):
         Store self.amount (float, rounded to 2 decimals) and self.currency (str, uppercase).
      2. __repr__(self): Return f"Money({self.amount:.2f}, {self.currency!r})".
      3. __add__(self, other):
         - If other is Money: check currencies match; if not, raise ValueError.
           Return new Money instance with summed amounts.
         - If other is int or float: return new Money instance with added scalar.
         - Otherwise: return NotImplemented!
      4. __radd__(self, other): Support scalar + Money (e.g. 50.0 + Money(100)).
      5. __mul__(self, other):
         - If other is int or float: return new Money instance with scaled amount.
         - Otherwise: return NotImplemented!
      6. __rmul__(self, other): Support scalar * Money (e.g. 2.5 * Money(100)).
    """
    def __init__(self, amount: float, currency: str = "USD"):
        self.amount = round(float(amount), 2)
        self.currency = currency.strip().upper()

    def __repr__(self) -> str:
        return f"Money({self.amount:.2f}, {self.currency!r})"

    def __add__(self, other: Any) -> "Money":
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"Cannot add different currencies: {self.currency} and {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + float(other), self.currency)
        return NotImplemented

    def __radd__(self, other: Any) -> "Money":
        return self.__add__(other)

    def __mul__(self, other: Any) -> "Money":
        if isinstance(other, (int, float)):
            return Money(self.amount * float(other), self.currency)
        return NotImplemented

    def __rmul__(self, other: Any) -> "Money":
        return self.__mul__(other)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Money):
            return (self.amount, self.currency) == (other.amount, other.currency)
        return False


# ==============================================================================
# TASK 3: MATRIX MULTIPLICATION PROTOCOL (@ / __matmul__)
# ==============================================================================
class NeuralLinearLayer:
    """
    Task 3: Implement matrix multiplication (@) for a 1-layer Neural Network.
    
    Requirements:
      1. __init__(self, weights: List[List[float]], bias: Optional[List[float]] = None):
         weights is a 2D matrix of shape (out_features, in_features).
         bias is optional list of length (out_features). If None, defaults to zeros.
      2. __matmul__(self, input_vector: List[float]) -> List[float]:
         Perform forward projection: y = weights @ input_vector + bias
         - Compute dot product of each row in weights with input_vector.
         - Add corresponding bias element.
         - Return output list of floats rounded to 4 decimals.
         - If input_vector length does not match weights columns (in_features), raise ValueError.
    """
    def __init__(self, weights: List[List[float]], bias: Optional[List[float]] = None):
        self.weights = weights
        self.out_features = len(weights)
        self.in_features = len(weights[0]) if weights else 0
        if bias is not None:
            if len(bias) != self.out_features:
                raise ValueError("Bias length must match output features")
            self.bias = [float(b) for b in bias]
        else:
            self.bias = [0.0] * self.out_features

    def __matmul__(self, input_vector: Any) -> List[float]:
        if not isinstance(input_vector, (list, tuple)):
            return NotImplemented
        if len(input_vector) != self.in_features:
            raise ValueError(f"Shape mismatch: Layer expects {self.in_features} features, got {len(input_vector)}")
        
        output = []
        for row_idx, row in enumerate(self.weights):
            dot_val = sum(w * x for w, x in zip(row, input_vector))
            total = dot_val + self.bias[row_idx]
            output.append(round(total, 4))
        return output


# ==============================================================================
# TASK 4: RICH COMPARISONS & @functools.total_ordering
# ==============================================================================
@functools.total_ordering
class ModelArtifact:
    """
    Task 4: Implement AI Model Artifact ranking using @functools.total_ordering.
    
    Requirements:
      1. __init__(self, name: str, params_billion: float, accuracy: float):
         Store self.name, self.params_billion, self.accuracy.
      2. __eq__(self, other):
         Two models are equal if (accuracy, params_billion) match.
      3. __lt__(self, other):
         Ordering rule:
           - Primary: Higher accuracy is BETTER (greater). So self < other if self.accuracy < other.accuracy.
           - Secondary (Tie-breaker): If accuracies are equal, FEWER parameters is BETTER (greater efficiency).
             So self < other if self.params_billion > other.params_billion!
    """
    def __init__(self, name: str, params_billion: float, accuracy: float):
        self.name = name
        self.params_billion = float(params_billion)
        self.accuracy = float(accuracy)

    def __repr__(self) -> str:
        return f"ModelArtifact({self.name!r}, {self.params_billion}B, {self.accuracy:.2%})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ModelArtifact):
            return NotImplemented
        return (self.accuracy, self.params_billion) == (other.accuracy, other.params_billion)

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, ModelArtifact):
            return NotImplemented
        if self.accuracy != other.accuracy:
            return self.accuracy < other.accuracy
        # Tie-breaker: smaller parameter count is better (greater)
        return self.params_billion > other.params_billion


# ==============================================================================
# TASK 5: THE SACRED HASHING CONTRACT (__eq__ & __hash__)
# ==============================================================================
class FeatureKey:
    """
    Task 5: Implement an immutable Feature Store key that participates in set/dict hashing.
    
    Requirements:
      1. __init__(self, feature_name: str, entity_type: str, version: int = 1):
         Store as private immutable attributes (_name, _entity_type, _version).
      2. Provide read-only @property accessors for name, entity_type, and version.
      3. __eq__(self, other):
         Equal if (name, entity_type, version) match.
      4. __hash__(self):
         Hash must be computed over the tuple: (self._name, self._entity_type, self._version).
         Guarantees: a == b => hash(a) == hash(b).
    """
    __slots__ = ("_name", "_entity_type", "_version")

    def __init__(self, feature_name: str, entity_type: str, version: int = 1):
        self._name = str(feature_name)
        self._entity_type = str(entity_type)
        self._version = int(version)

    @property
    def name(self) -> str:
        return self._name

    @property
    def entity_type(self) -> str:
        return self._entity_type

    @property
    def version(self) -> int:
        return self._version

    def __repr__(self) -> str:
        return f"FeatureKey('{self._name}', '{self._entity_type}', v={self._version})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FeatureKey):
            return NotImplemented
        return (self._name, self._entity_type, self._version) == (other._name, other._entity_type, other._version)

    def __hash__(self) -> int:
        return hash((self._name, self._entity_type, self._version))


# ==============================================================================
# TASK 6: SEQUENCE PROTOCOL & SLICING (__len__, __getitem__, __iter__)
# ==============================================================================
class TokenStream:
    """
    Task 6: Implement a Sequence Container with full integer and slice indexing.
    
    Requirements:
      1. __init__(self, tokens: List[str]): Store internal token list.
      2. __len__(self) -> int: Return total number of tokens.
      3. __getitem__(self, index: Union[int, slice]) -> Union[str, "TokenStream"]:
         - If index is int: return the single string token at that index.
         - If index is slice: return a NEW TokenStream containing the sliced tokens!
         - Otherwise: raise TypeError.
      4. __iter__(self) -> Iterator[str]: Yield tokens one by one.
      5. __repr__(self) -> str: Return f"TokenStream({self._tokens})".
    """
    def __init__(self, tokens: List[str]):
        self._tokens = [str(t) for t in tokens]

    def __len__(self) -> int:
        return len(self._tokens)

    def __getitem__(self, index: Union[int, slice]) -> Union[str, "TokenStream"]:
        if isinstance(index, slice):
            return TokenStream(self._tokens[index])
        elif isinstance(index, int):
            return self._tokens[index]
        raise TypeError(f"TokenStream indices must be integers or slices, not {type(index).__name__}")

    def __iter__(self) -> Iterator[str]:
        return iter(self._tokens)

    def __repr__(self) -> str:
        return f"TokenStream({self._tokens})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, TokenStream):
            return self._tokens == other._tokens
        return False


# ==============================================================================
# AUTOMATED TEST SUITE RUNNER
# ==============================================================================
def run_tests():
    print("=" * 75)
    print("🧪 RUNNING DAY 16 AUTOMATED PRACTICE TEST SUITE")
    print("=" * 75)

    passed = 0
    total = 6

    # Test 1: Vector2D
    try:
        v1 = Vector2D(3.0, 4.0)
        v_origin = Vector2D(0.0, 0.0)
        assert repr(v1) == "Vector2D(x=3.0, y=4.0)", f"Failed repr: {repr(v1)}"
        assert str(v1) == "(3.0, 4.0)", f"Failed str: {str(v1)}"
        assert bool(v1) is True, "v1 should be Truthy"
        assert bool(v_origin) is False, "v_origin should be Falsy"
        print("  ✅ Task 1 (Vector2D Representation & Truthiness): PASSED")
        passed += 1
    except Exception as e:
        print(f"  ❌ Task 1 FAILED: {e}")

    # Test 2: Money Arithmetic
    try:
        m1 = Money(100.50, "USD")
        m2 = Money(50.25, "USD")
        m_eur = Money(50.00, "EUR")

        assert (m1 + m2) == Money(150.75, "USD"), "Failed Money + Money"
        assert (m1 + 20) == Money(120.50, "USD"), "Failed Money + scalar"
        assert (20 + m1) == Money(120.50, "USD"), "Failed scalar + Money (radd)"
        assert (m1 * 2) == Money(201.00, "USD"), "Failed Money * scalar"
        assert (2 * m1) == Money(201.00, "USD"), "Failed scalar * Money (rmul)"

        # Currency mismatch error
        mismatch_caught = False
        try:
            _ = m1 + m_eur
        except ValueError:
            mismatch_caught = True
        assert mismatch_caught, "Expected ValueError on currency mismatch"

        print("  ✅ Task 2 (Money Arithmetic & Reflected Operators): PASSED")
        passed += 1
    except Exception as e:
        print(f"  ❌ Task 2 FAILED: {e}")

    # Test 3: NeuralLinearLayer MatMul
    try:
        # 2x3 weight matrix (2 output neurons, 3 input features)
        w = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]
        b = [0.5, -1.0]
        layer = NeuralLinearLayer(w, b)
        x = [1.0, 1.0, 1.0]
        # row 0: (1+2+3) + 0.5 = 6.5
        # row 1: (4+5+6) - 1.0 = 14.0
        y = layer @ x
        assert y == [6.5, 14.0], f"Expected [6.5, 14.0], got {y}"
        print("  ✅ Task 3 (NeuralLinearLayer Matrix Multiplication @): PASSED")
        passed += 1
    except Exception as e:
        print(f"  ❌ Task 3 FAILED: {e}")

    # Test 4: ModelArtifact Total Ordering
    try:
        m_a = ModelArtifact("Model-A", 7.0, 0.85)
        m_b = ModelArtifact("Model-B", 7.0, 0.90)  # Higher accuracy -> greater
        m_c = ModelArtifact("Model-C", 14.0, 0.85) # Same acc as A, but more params -> lesser efficiency

        assert m_b > m_a, "Model B should be greater than Model A"
        assert m_a > m_c, "Model A should be greater than Model C (tie-breaker on params)"
        assert m_c <= m_a, "Synthesized <= failed"
        assert m_a != m_b, "Models should not be equal"

        models = [m_a, m_b, m_c]
        models.sort(reverse=True)
        assert models == [m_b, m_a, m_c], f"Unexpected sort order: {models}"
        print("  ✅ Task 4 (ModelArtifact Total Ordering): PASSED")
        passed += 1
    except Exception as e:
        print(f"  ❌ Task 4 FAILED: {e}")

    # Test 5: FeatureKey Hashing Contract
    try:
        k1 = FeatureKey("user_embedding", "vector", 1)
        k2 = FeatureKey("user_embedding", "vector", 1)  # Duplicate
        k3 = FeatureKey("item_embedding", "vector", 1)

        assert k1 == k2, "k1 and k2 should be equal"
        assert hash(k1) == hash(k2), "Invariant violated: equal objects must have equal hashes!"
        
        # Test set deduplication
        feature_set = {k1, k2, k3}
        assert len(feature_set) == 2, f"Expected 2 unique keys in set, got {len(feature_set)}"

        # Test dict lookup
        store = {k1: "cached_weights"}
        assert store[k2] == "cached_weights", "Dict lookup by equal key failed"
        print("  ✅ Task 5 (FeatureKey Hashing Contract): PASSED")
        passed += 1
    except Exception as e:
        print(f"  ❌ Task 5 FAILED: {e}")

    # Test 6: TokenStream Sequence & Slicing
    try:
        raw = ["Hello", "world", "this", "is", "Python", "dunder", "methods"]
        stream = TokenStream(raw)

        assert len(stream) == 7, f"Expected length 7, got {len(stream)}"
        assert stream[0] == "Hello", "Single index access failed"
        assert stream[-1] == "methods", "Negative index access failed"

        # Slicing test
        sub_stream = stream[1:4]
        assert isinstance(sub_stream, TokenStream), "Slice must return a new TokenStream"
        assert sub_stream == TokenStream(["world", "this", "is"]), f"Slice contents mismatch: {sub_stream}"

        # Iteration test
        iterated = [t for t in stream]
        assert iterated == raw, "Iteration mismatch"
        print("  ✅ Task 6 (TokenStream Sequence Protocol & Slicing): PASSED")
        passed += 1
    except Exception as e:
        print(f"  ❌ Task 6 FAILED: {e}")

    print("=" * 75)
    print(f"🏁 RESULTS: {passed}/{total} Practice Tasks Passed Successfully!")
    print("=" * 75)


if __name__ == "__main__":
    run_tests()

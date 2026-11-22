"""
================================================================================
DAY 16: PYTHON DATA MODEL & MAGIC METHODS (PART 4)
Module 04: Custom Containers, Sequence Protocols & Callable Objects
================================================================================
Topics Covered:
  1. The Sequence & Container Protocol: __len__, __getitem__, __setitem__, __delitem__
  2. Slicing Mechanics in __getitem__: Handling slice objects (start, stop, step)
  3. Membership & Iteration: __contains__ vs Linear Fallback, __iter__, __reversed__
  4. The Callable Protocol: __call__ for Stateful Function Objects
  5. Dynamic Attribute Interception: __getattr__ vs __getattribute__
  6. Enterprise AI Pattern: PyTorchStyleDataset & CallablePromptPipeline
================================================================================
"""

from typing import Any, List, Union, Iterator, Dict, Optional


# ==============================================================================
# SECTION 1 & 2: SEQUENCE & CONTAINER PROTOCOLS WITH SLICING
# ==============================================================================
# When you write:
#   len(seq)        -> type(seq).__len__(seq)
#   seq[i]          -> type(seq).__getitem__(seq, i)
#   seq[1:4]        -> type(seq).__getitem__(seq, slice(1, 4, None))
#   seq[i] = val    -> type(seq).__setitem__(seq, i, val)
#   del seq[i]      -> type(seq).__delitem__(seq, i)
#   item in seq     -> type(seq).__contains__(seq, item)
#
# If __contains__ is omitted, Python falls back to linear scan using __iter__ or __getitem__!
# If __reversed__ is omitted, Python emulates reversed() using __len__ and __getitem__!

class EmbeddingBatch:
    """
    A custom container holding vector embeddings.
    Supports index access, slicing, item assignment, and membership checking.
    """
    def __init__(self, vectors: List[List[float]]):
        self._vectors = [list(v) for v in vectors]

    def __len__(self) -> int:
        return len(self._vectors)

    def __getitem__(self, index: Union[int, slice]) -> Union[List[float], "EmbeddingBatch"]:
        """
        Handles both single integer indices (batch[0]) and slices (batch[1:4]).
        """
        if isinstance(index, slice):
            # Return a new EmbeddingBatch containing the sliced subset
            return EmbeddingBatch(self._vectors[index])
        elif isinstance(index, int):
            return self._vectors[index]
        else:
            raise TypeError(f"EmbeddingBatch indices must be integers or slices, not {type(index).__name__}")

    def __setitem__(self, index: int, value: List[float]) -> None:
        if not isinstance(index, int):
            raise TypeError("Only integer index assignment is supported")
        if not isinstance(value, list):
            raise TypeError("Value must be a list of floats")
        self._vectors[index] = list(value)

    def __delitem__(self, index: int) -> None:
        del self._vectors[index]

    def __contains__(self, vector: Any) -> bool:
        """Fast membership testing (O(1) or optimized search)."""
        return vector in self._vectors

    def __iter__(self) -> Iterator[List[float]]:
        return iter(self._vectors)

    def __repr__(self) -> str:
        return f"EmbeddingBatch(count={len(self._vectors)}, dim={len(self._vectors[0]) if self._vectors else 0})"


def demonstrate_sequence_protocol():
    print("=" * 70)
    print("SECTION 1 & 2: SEQUENCE & CONTAINER PROTOCOLS WITH SLICING")
    print("=" * 70)

    raw_data = [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
        [0.7, 0.8, 0.9],
        [1.0, 1.1, 1.2],
        [1.3, 1.4, 1.5]
    ]
    batch = EmbeddingBatch(raw_data)
    print(f"Initial Container: {batch}")
    print(f"Container Length:  len(batch) = {len(batch)}")

    # 1. Single index access (__getitem__ with int)
    print(f"batch[0]:          {batch[0]}")
    print(f"batch[-1]:         {batch[-1]}")

    # 2. Slicing access (__getitem__ with slice)
    sub_batch = batch[1:4]
    print(f"batch[1:4] Slice:  {sub_batch}")
    print(f"Sliced Vectors:    {list(sub_batch)}")

    # 3. Item assignment (__setitem__)
    batch[0] = [9.9, 9.9, 9.9]
    print(f"After batch[0] = [9.9, 9.9, 9.9]: {batch[0]}")

    # 4. Membership testing (__contains__)
    target = [0.4, 0.5, 0.6]
    print(f"[0.4, 0.5, 0.6] in batch: {target in batch}")
    print(f"[0.0, 0.0, 0.0] in batch: {[0.0, 0.0, 0.0] in batch}")

    # 5. Iteration (__iter__)
    print("\nIterating over batch vectors:")
    for idx, vec in enumerate(batch):
        print(f"  [{idx}]: {vec}")


# ==============================================================================
# SECTION 3: THE CALLABLE PROTOCOL — __call__
# ==============================================================================
# An object is "callable" (callable(obj) == True) if its class defines __call__.
#
# Why this is revolutionary:
#   - Turns a class instance into a stateful function object!
#   - Powers PyTorch: When you write `output = model(images)`, PyTorch executes
#     `torch.nn.Module.__call__`, which manages forward hooks and calls `.forward()`.
#   - Powers LangChain: Runnable chains and prompt templates are callable objects.

class TemperatureScaledClassifier:
    """
    A callable ML classification post-processor that applies temperature scaling
    while maintaining state across invocations (call counts and history).
    """
    def __init__(self, temperature: float = 1.0):
        self.temperature = float(temperature)
        self.total_invocations = 0

    def __call__(self, logits: List[float]) -> List[float]:
        """
        Executes the forward pass when instance is called as a function:
          probs = softmax(logits / temperature)
        """
        import math
        self.total_invocations += 1

        # Scale logits
        scaled = [x / self.temperature for x in logits]
        # Softmax
        exp_vals = [math.exp(x) for x in scaled]
        sum_exp = sum(exp_vals)
        probabilities = [round(val / sum_exp, 4) for val in exp_vals]
        return probabilities

    def __repr__(self) -> str:
        return f"TemperatureScaledClassifier(T={self.temperature}, calls={self.total_invocations})"


def demonstrate_callable_protocol():
    print("\n" + "=" * 70)
    print("SECTION 3: THE CALLABLE PROTOCOL (__call__)")
    print("=" * 70)

    classifier = TemperatureScaledClassifier(temperature=0.5)
    print(f"Is instance callable? {callable(classifier)}")
    print(f"Initial State:        {classifier}")

    # Calling the object directly like a function!
    logits = [2.0, 1.0, 0.1]
    probs1 = classifier(logits)
    print(f"\nInference 1: classifier({logits}) -> {probs1}")

    probs2 = classifier([3.5, 0.2, -1.0])
    print(f"Inference 2: classifier([3.5, 0.2, -1.0]) -> {probs2}")

    print(f"\nUpdated Internal State: {classifier}")


# ==============================================================================
# SECTION 4: DYNAMIC ATTRIBUTE INTERCEPTION — __getattr__
# ==============================================================================
# Python Attribute Resolution:
#   1. Check instance __dict__.
#   2. Check class and MRO hierarchy.
#   3. If NOT found, Python calls __getattr__(self, name) as a fallback!
#   (Contrast with __getattribute__, which is called unconditionally for EVERY access).

class ConfigStore:
    """Dynamic config dictionary accessible via both dict syntax and dot notation."""
    def __init__(self, **kwargs):
        self._config = kwargs

    def __getattr__(self, name: str) -> Any:
        """Called ONLY when an attribute is not found in instance attributes."""
        if name in self._config:
            return self._config[name]
        raise AttributeError(f"ConfigStore has no key or attribute '{name}'")

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __repr__(self) -> str:
        return f"ConfigStore({self._config})"


def demonstrate_getattr():
    print("\n" + "=" * 70)
    print("SECTION 4: DYNAMIC ATTRIBUTE ACCESS VIA __getattr__")
    print("=" * 70)

    cfg = ConfigStore(learning_rate=0.001, batch_size=32, optimizer="AdamW")
    print(f"Config: {cfg}")

    # Accessed via dot notation thanks to __getattr__:
    print(f"cfg.learning_rate: {cfg.learning_rate}")
    print(f"cfg.batch_size:    {cfg.batch_size}")
    print(f"cfg['optimizer']:  {cfg['optimizer']}")

    try:
        _ = cfg.missing_parameter
    except AttributeError as e:
        print(f"Graceful AttributeError on missing key: {e}")


# ==============================================================================
# SECTION 5: ENTERPRISE AI PATTERN — PyTorchStyleDataset
# ==============================================================================
class PyTorchStyleDataset:
    """
    Production-grade Dataset emulation conforming to PyTorch Dataset protocols:
      - __len__: Returns dataset sample count.
      - __getitem__: Returns single sample (int) or mini-batch (slice).
      - __iter__: Supports streaming iteration in DataLoader loops.
    """
    def __init__(self, samples: List[Dict[str, Any]]):
        self._samples = samples

    def __len__(self) -> int:
        return len(self._samples)

    def __getitem__(self, index: Union[int, slice]) -> Any:
        if isinstance(index, slice):
            return PyTorchStyleDataset(self._samples[index])
        return self._samples[index]

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        return iter(self._samples)

    def __repr__(self) -> str:
        return f"PyTorchStyleDataset(num_samples={len(self._samples)})"


def demonstrate_pytorch_dataset_pattern():
    print("\n" + "=" * 70)
    print("SECTION 5: ENTERPRISE AI PATTERN — PyTorchStyleDataset")
    print("=" * 70)

    data = [
        {"input": "What is Python?", "target": "A programming language"},
        {"input": "What is MRO?", "target": "Method Resolution Order"},
        {"input": "What is ABC?", "target": "Abstract Base Class"},
        {"input": "What is LoRA?", "target": "Low-Rank Adaptation"},
        {"input": "What is RAG?", "target": "Retrieval Augmented Generation"},
    ]

    dataset = PyTorchStyleDataset(data)
    print(f"Dataset:            {dataset}")
    print(f"Length:             {len(dataset)} items")
    print(f"Sample 0:           {dataset[0]}")
    print(f"Sample -1:          {dataset[-1]}")

    # Batch Slicing:
    batch = dataset[1:4]
    print(f"\nBatch Slice [1:4]:  {batch}")
    for i, item in enumerate(batch):
        print(f"  Batch Item #{i}: {item['input']} -> {item['target']}")


if __name__ == "__main__":
    demonstrate_sequence_protocol()
    demonstrate_callable_protocol()
    demonstrate_getattr()
    demonstrate_pytorch_dataset_pattern()

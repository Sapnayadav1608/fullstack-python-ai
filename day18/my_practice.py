"""
===============================================================================
Day 18: Hands-On Practice Workbook & Automated Test Suite
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: File Systems, Encodings, Atomic Persistence & Streaming for AI
6 Rigorous Challenges with Automated Self-Testing Runner
===============================================================================
"""

from __future__ import annotations
import json
import os
import pickle
import pickletools
import shutil
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional


# ============================================================================
# CHALLENGE 1: PATHLIB FILE DISCOVERY
# ============================================================================
def find_model_artifacts(root_dir: Path, extension: str, recursive: bool = True) -> List[Path]:
    """
    Discovers all files ending with `extension` inside `root_dir`.
    If recursive=True, searches all nested subdirectories (rglob).
    Returns a sorted list of Path objects.
    """
    root = Path(root_dir)
    pattern = f"*{extension}" if extension.startswith(".") else f"*.{extension}"
    if recursive:
        matches = list(root.rglob(pattern))
    else:
        matches = list(root.glob(pattern))
    return sorted([p for p in matches if p.is_file()])


# ============================================================================
# CHALLENGE 2: CRASH-PROOF ATOMIC JSON DUMP
# ============================================================================
def atomic_json_dump(data: Dict[str, Any], filepath: Path) -> bool:
    """
    Writes dictionary as formatted JSON using the crash-proof atomic pattern:
      1. Write to a temporary file in the same parent directory.
      2. Call f.flush() and os.fsync(f.fileno()).
      3. Atomically rename using os.replace().
    Returns True upon success.
    """
    target = Path(filepath).resolve()
    temp_target = target.with_name(f".{target.name}.tmp_{time.time_ns()}")
    try:
        with open(temp_target, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp_target, target)
        return True
    except Exception:
        if temp_target.exists():
            temp_target.unlink()
        raise


# ============================================================================
# CHALLENGE 3: RESILIENT MULTILINGUAL TEXT DECODER
# ============================================================================
def clean_text_stream(raw_bytes: bytes) -> str:
    """
    Decodes raw bytes handling Windows UTF-8 BOM (\xef\xbb\xbf) automatically,
    falling back to utf-8 with error replacement to prevent UnicodeDecodeErrors.
    Strips leading/trailing whitespace.
    """
    if raw_bytes.startswith(b"\xef\xbb\xbf"):
        return raw_bytes.decode("utf-8-sig", errors="replace").strip()
    return raw_bytes.decode("utf-8", errors="replace").strip()


# ============================================================================
# CHALLENGE 4: LLM FINE-TUNING JSONL DATASET VALIDATOR
# ============================================================================
def validate_llm_jsonl_dataset(jsonl_filepath: Path) -> Dict[str, Any]:
    """
    Validates an LLM conversational fine-tuning dataset formatted as JSONL:
      - Each line must be a valid JSON object.
      - Must contain a 'messages' list with at least 1 message.
      - Each message must have 'role' in {'system', 'user', 'assistant'} and non-empty 'content'.
    Returns:
      {'total_records': int, 'valid_records': int, 'is_valid': bool}
    """
    total = 0
    valid = 0
    allowed_roles = {"system", "user", "assistant"}

    with open(jsonl_filepath, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if not line_str:
                continue
            total += 1
            try:
                record = json.loads(line_str)
                messages = record.get("messages")
                if not isinstance(messages, list) or len(messages) == 0:
                    continue

                msg_ok = True
                for msg in messages:
                    role = msg.get("role")
                    content = msg.get("content")
                    if role not in allowed_roles or not isinstance(content, str) or not content.strip():
                        msg_ok = False
                        break

                if msg_ok:
                    valid += 1
            except json.JSONDecodeError:
                continue

    return {
        "total_records": total,
        "valid_records": valid,
        "is_valid": (total > 0 and total == valid)
    }


# ============================================================================
# CHALLENGE 5: PICKLE SECURITY BYTECODE INSPECTOR
# ============================================================================
def inspect_pickle_security(payload: bytes) -> bool:
    """
    Inspects raw serialized pickle bytes for dangerous remote code execution
    opcodes (REDUCE, INST, OBJ) or unsafe module references ('os', 'nt', 'posix',
    'subprocess', 'builtins', 'eval', 'exec', 'system').
    Returns True if safe, False if malicious/dangerous.
    """
    dangerous_terms = {
        "os", "nt", "posix", "subprocess", "sys", "builtins", "__builtin__",
        "system", "popen", "spawn", "exec", "eval", "getattr"
    }
    try:
        for opcode, arg, pos in pickletools.genops(payload):
            if opcode.name in ("REDUCE", "INST", "OBJ"):
                return False
            if opcode.name in ("GLOBAL", "STACK_GLOBAL") and arg is not None:
                parts = arg.split()
                if any(p.lower() in dangerous_terms for p in parts):
                    return False
            if isinstance(arg, str):
                if any(term in arg.lower().split(".") for term in dangerous_terms) or arg in dangerous_terms:
                    return False
        return True
    except Exception:
        return False


# ============================================================================
# CHALLENGE 6: CHUNKED TOKEN STREAMER (O(1) MEMORY)
# ============================================================================
def chunked_token_streamer(filepath: Path, chunk_size_bytes: int = 1024) -> Generator[bytes, None, None]:
    """
    Streams a large binary file yielding exact slices of size `chunk_size_bytes`.
    Maintains O(1) memory overhead.
    """
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(chunk_size_bytes)
            if not chunk:
                break
            yield chunk


# ============================================================================
# AUTOMATED TEST RUNNER
# ============================================================================
def run_tests():
    print("=" * 70)
    print("RUNNING DAY 18 AUTOMATED TEST SUITE — FILE SYSTEMS & SERIALIZATION")
    print("=" * 70)

    temp_dir = Path(tempfile.mkdtemp(prefix="practice_test_"))
    try:
        # Test 1: Pathlib File Discovery
        sub1 = temp_dir / "checkpoints" / "run1"
        sub2 = temp_dir / "checkpoints" / "run2"
        sub1.mkdir(parents=True, exist_ok=True)
        sub2.mkdir(parents=True, exist_ok=True)
        (sub1 / "model.pt").write_bytes(b"123")
        (sub2 / "model.pt").write_bytes(b"456")
        (sub2 / "config.json").write_text("{}")

        found = find_model_artifacts(temp_dir, ".pt", recursive=True)
        assert len(found) == 2
        assert all(p.suffix == ".pt" for p in found)
        print("  [PASS] Challenge 1: find_model_artifacts discovers nested paths")

        # Test 2: Crash-Proof Atomic JSON Dump
        target_file = temp_dir / "state.json"
        assert atomic_json_dump({"status": "ready", "epoch": 5}, target_file) is True
        loaded = json.loads(target_file.read_text())
        assert loaded["epoch"] == 5
        print("  [PASS] Challenge 2: atomic_json_dump writes and verifies state")

        # Test 3: Resilient Multilingual Text Decoder
        bom_text = b"\xef\xbb\xbfHello AI \xf0\x9f\xa4\x96"  # BOM + Robot emoji
        assert clean_text_stream(bom_text) == "Hello AI 🤖"
        corrupt_text = b"Normal \xff\xfe Text"
        assert "Normal" in clean_text_stream(corrupt_text)
        print("  [PASS] Challenge 3: clean_text_stream strips BOM and handles errors")

        # Test 4: LLM JSONL Dataset Validator
        jsonl_valid = temp_dir / "train_valid.jsonl"
        jsonl_invalid = temp_dir / "train_invalid.jsonl"

        jsonl_valid.write_text(
            '{"messages": [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello"}]}\n'
            '{"messages": [{"role": "user", "content": "AI?"}, {"role": "assistant", "content": "Yes"}]}\n'
        )
        jsonl_invalid.write_text(
            '{"messages": [{"role": "user", "content": "Hi"}]}\n'
            '{"messages": [{"role": "hacker", "content": "bad role"}]}\n'
            'corrupt json line\n'
        )

        val_res = validate_llm_jsonl_dataset(jsonl_valid)
        assert val_res["is_valid"] is True and val_res["valid_records"] == 2

        inval_res = validate_llm_jsonl_dataset(jsonl_invalid)
        assert inval_res["is_valid"] is False and inval_res["valid_records"] == 1
        print("  [PASS] Challenge 4: validate_llm_jsonl_dataset validates LLM corpora")

        # Test 5: Pickle Security Bytecode Inspector
        safe_data = pickle.dumps({"weights": [0.1, 0.2, 0.3]})
        assert inspect_pickle_security(safe_data) is True

        class Malicious:
            def __reduce__(self):
                import os
                return (os.system, ("echo HACKED",))

        unsafe_data = pickle.dumps(Malicious())
        assert inspect_pickle_security(unsafe_data) is False
        print("  [PASS] Challenge 5: inspect_pickle_security catches RCE exploit payload")

        # Test 6: Chunked Token Streamer
        binary_file = temp_dir / "tokens.bin"
        binary_file.write_bytes(b"A" * 5000)

        chunks = list(chunked_token_streamer(binary_file, chunk_size_bytes=1000))
        assert len(chunks) == 5
        assert all(len(c) == 1000 for c in chunks)
        print("  [PASS] Challenge 6: chunked_token_streamer yields bounded chunks")

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    print("\n" + "=" * 70)
    print("ALL 6/6 CHALLENGES PASSED! FILE I/O & SERIALIZATION CERTIFIED!")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

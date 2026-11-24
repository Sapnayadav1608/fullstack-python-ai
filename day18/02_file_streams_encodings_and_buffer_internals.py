"""
===============================================================================
Day 18: Module 02 - File Streams, Encodings & CPython Buffer Internals
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Binary vs Text Streams, Unicode Encodings & Kernel Buffer Synchronization
Architecture: Crash-Proof Atomic File Writers for AI Inference Logs
===============================================================================

In mission-critical AI applications (saving model checkpoints, caching embeddings,
or appending audit logs), naive file writing frequently leads to:
  1. Silent data corruption on power/OS crash (because data sat in user-space buffer).
  2. Race conditions where concurrent processes read half-written JSON files.
  3. UnicodeDecodeErrors caused by Windows UTF-16 BOM or missing encoding flags.

This module explores the low-level mechanics of Python's I/O subsystems:
  1. File Open Modes: `r`, `w`, `a`, `x` (exclusive creation), `rb`, `wb`.
  2. The Unicode Architecture: UTF-8 vs UTF-16 vs ASCII, UTF-8-SIG BOM handling,
     and error recovery strategies (`replace`, `ignore`, `backslashreplace`).
  3. CPython I/O Buffering: Unbuffered vs Line-buffered vs Block-buffered (8KB).
  4. The Two-Stage Flush: `file.flush()` (CPython -> OS) vs `os.fsync()` (OS -> Physical Disk).
  5. Enterprise Resiliency Pattern: The Crash-Proof Atomic File Write Pattern.
"""

from __future__ import annotations
import io
import os
import shutil
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List


# ============================================================================
# SECTION 1: OPEN MODES & EXCLUSIVE CREATION ('x')
# ============================================================================
print("=" * 75)
print("SECTION 1: FILE OPEN MODES & RACE-CONDITION PROTECTION WITH 'x'")
print("=" * 75)

temp_dir = Path(tempfile.mkdtemp(prefix="stream_demo_"))
try:
    test_file = temp_dir / "model_lock.pid"

    # 'w': Truncates and overwrites
    with open(test_file, mode="w", encoding="utf-8") as f:
        f.write("PID=10492\n")

    # 'a': Appends to end of file without truncating
    with open(test_file, mode="a", encoding="utf-8") as f:
        f.write("STATUS=ACTIVE\n")

    # 'x': Exclusive creation! Fails atomically if file already exists
    # Critical for distributed locks and preventing accidental file overwrites
    try:
        with open(test_file, mode="x", encoding="utf-8") as f:
            f.write("ANOTHER_PROCESS")
    except FileExistsError as err:
        print(f"  [Race Protection with 'x'] Prevented overwrite: {err}")

    content = test_file.read_text(encoding="utf-8")
    print(f"  Resulting file content:\n{content.strip()}")

finally:
    shutil.rmtree(temp_dir, ignore_errors=True)


# ============================================================================
# SECTION 2: UNICODE ENCODINGS, BOM TRAPS & ERROR POLICIES
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: UNICODE ENCODINGS, BOM TRAPS & ERROR RECOVERY")
print("=" * 75)

# Text with multilingual AI prompts, math symbols, and emojis
sample_prompt = "User: Expliquez l'apprentissage profond (AI) 🧠 ∇L_w"
raw_utf8_bytes = sample_prompt.encode("utf-8")
print(f"String Length: {len(sample_prompt)} chars | UTF-8 Byte Size: {len(raw_utf8_bytes)} bytes")

# The Windows BOM (Byte Order Mark) Trap: \xef\xbb\xbf
# Windows Notepad or Excel often prepends BOM to UTF-8 files.
bom_bytes = b"\xef\xbb\xbf" + raw_utf8_bytes

# Naive decoding with 'utf-8' leaves the invisible zero-width BOM char (\ufeff)
naive_decoded = bom_bytes.decode("utf-8")
print(f"Naive 'utf-8' decode first char: {repr(naive_decoded[0])} (BOM Leak!)")

# Correct decoding using 'utf-8-sig' automatically strips the BOM cleanly!
clean_decoded = bom_bytes.decode("utf-8-sig")
print(f"Clean 'utf-8-sig' decode first char: {repr(clean_decoded[0])} (Clean string!)")
assert not clean_decoded.startswith("\ufeff")

# Error Handling Policies when reading corrupt bytes
corrupted_bytes = b"Valid ASCII \xff\xfe Corrupt Bytes \x80"

# 1. 'strict' (default) -> Raises UnicodeDecodeError
# 2. 'replace' -> Replaces corrupt bytes with U+FFFD ()
print(f"Decoded with 'replace': {corrupted_bytes.decode('utf-8', errors='replace')}")
# 3. 'ignore' -> Drops corrupt bytes entirely
print(f"Decoded with 'ignore':  {corrupted_bytes.decode('utf-8', errors='ignore')}")


# ============================================================================
# SECTION 3: CPYTHON BUFFERING & THE TWO-STAGE FLUSH (flush vs fsync)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 3: BUFFERING ARCHITECTURE & THE TWO-STAGE FLUSH")
print("=" * 75)

print(f"Default CPython I/O Block Buffer Size: {io.DEFAULT_BUFFER_SIZE} bytes (8 KB)")

# Anatomy of file writing:
# Python Application (f.write)
#      │
#      ▼ (Stage 1: User-Space CPython Buffer)
# file.flush()
#      │
#      ▼ (Stage 2: OS Kernel Page Cache)
# os.fsync(file.fileno())
#      │
#      ▼ (Stage 3: Physical Non-Volatile Storage NVMe / SSD)

temp_dir2 = Path(tempfile.mkdtemp(prefix="buffer_demo_"))
try:
    log_file = temp_dir2 / "server_telemetry.log"
    with open(log_file, "w", buffering=8192, encoding="utf-8") as f:
        f.write("Event: Model checkpoint started\n")
        # At this exact moment, data is in CPython's 8KB memory buffer!
        # The file on disk might literally report 0 bytes size!
        print(f"Bytes on disk before flush: {log_file.stat().st_size} bytes")

        # Step 1: Push from Python runtime to OS kernel cache
        f.flush()
        print(f"Bytes on disk after f.flush(): {log_file.stat().st_size} bytes")

        # Step 2: Force OS kernel to write dirty pages to physical drive
        os.fsync(f.fileno())
        print("os.fsync() complete: Data physically committed to hardware!")

finally:
    shutil.rmtree(temp_dir2, ignore_errors=True)


# ============================================================================
# SECTION 4: THE ATOMIC FILE WRITE PATTERN (Crash & Concurrency Proof)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 4: THE PRODUCTION CRASH-PROOF ATOMIC FILE WRITE PATTERN")
print("=" * 75)

def atomic_write(filepath: Path | str, content: str, encoding: str = "utf-8"):
    """
    Writes content to a file atomically:
      1. Write to temporary file in the EXACT same directory/filesystem.
      2. Call f.flush() and os.fsync() to guarantee hardware persistence.
      3. Use os.replace() to atomically rename temp file to target.

    Guarantees:
      - Readers NEVER see half-written or corrupt files.
      - If power fails mid-write, original file remains 100% intact!
    """
    target = Path(filepath).resolve()
    temp_target = target.with_name(f".{target.name}.tmp_{time.time_ns()}")

    try:
        with open(temp_target, "w", encoding=encoding) as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())

        # os.replace is an atomic rename on both POSIX and Windows (NTFS)
        os.replace(temp_target, target)
    except Exception:
        # Clean up temporary file if write failed
        if temp_target.exists():
            temp_target.unlink()
        raise


# Demonstration
temp_dir3 = Path(tempfile.mkdtemp(prefix="atomic_demo_"))
try:
    target_config = temp_dir3 / "active_model_config.json"
    atomic_write(target_config, '{"model": "gemini-1.5-pro", "version": "v1"}')
    print(f"Initial atomic write: {target_config.read_text()}")

    # Atomic update
    atomic_write(target_config, '{"model": "gemini-1.5-pro", "version": "v2"}')
    print(f"Updated atomic write: {target_config.read_text()}")
    assert '"version": "v2"' in target_config.read_text()
finally:
    shutil.rmtree(temp_dir3, ignore_errors=True)

print("\n" + "=" * 75)
print("Module 02 Complete: Streams, Encodings & Buffer Internals Mastered!")
print("=" * 75)

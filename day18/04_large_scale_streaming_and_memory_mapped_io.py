"""
===============================================================================
Day 18: Module 04 - Large-Scale Streaming & Memory-Mapped I/O (mmap)
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Handling Terabyte-Scale Files with Zero-Copy mmap & Chunked Generators
Architecture: High-Throughput Token Ingestion for Large Language Models
===============================================================================

In large-scale AI engineering, datasets (Common Crawl text corpora, embedding
dumps, image datasets) are frequently tens or hundreds of gigabytes—far exceeding
the physical RAM of a developer machine or GPU container.
Calling `f.read()` or `f.readlines()` causes instant memory exhaustion (OOM Killer).

To process massive datasets with enterprise efficiency, we use two techniques:
  1. Chunked Streaming Generators: Processing streams in fixed buffer windows with
     $O(1)$ constant memory overhead.
  2. Memory-Mapped Files (`mmap` module): Mapping disk file blocks directly into
     the operating system's virtual memory address space. This enables zero-copy
     random access and blistering fast regex/pattern scanning.

This module explores:
  1. The Chunked Buffer Pattern for multi-gigabyte binary/text files.
  2. The `mmap` Protocol: Zero-copy slicing, binary search, and in-place updates.
  3. Live Benchmark: Comparing `.read()` vs Streaming vs `mmap`.
  4. Enterprise AI Pattern: `StreamingTokenBatcher` for continuous model training.
"""

from __future__ import annotations
import mmap
import os
import shutil
import tempfile
import time
from pathlib import Path
from typing import Generator, List, Tuple


# ============================================================================
# SECTION 1: CHUNKED BUFFER STREAMING (O(1) CONSTANT RAM)
# ============================================================================
print("=" * 75)
print("SECTION 1: CHUNKED STREAMING GENERATORS (O(1) CONSTANT MEMORY)")
print("=" * 75)

def stream_file_chunks(filepath: Path | str, chunk_size: int = 65536) -> Generator[bytes, None, None]:
    """
    Yields binary chunks of exact size `chunk_size` (default 64KB).
    Memory consumption remains strictly bounded regardless of file size.
    """
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


temp_dir = Path(tempfile.mkdtemp(prefix="stream_bench_"))
try:
    synthetic_data_file = temp_dir / "large_token_corpus.bin"

    # Generate a 2 MB synthetic token dataset (simulating raw embeddings or tokens)
    print("Generating synthetic 2 MB binary dataset...")
    total_bytes = 2 * 1024 * 1024
    chunk_pattern = b"TOKEN_" + (b"0" * 58)  # 64 bytes per token record
    num_records = total_bytes // len(chunk_pattern)

    with open(synthetic_data_file, "wb") as f:
        for _ in range(num_records):
            f.write(chunk_pattern)

    print(f"Generated: {synthetic_data_file.stat().st_size:,} bytes on disk.")

    # Stream chunks and compute checksum/stats without reading whole file into RAM
    total_chunks = 0
    total_streamed_bytes = 0
    for chunk in stream_file_chunks(synthetic_data_file, chunk_size=65536):
        total_chunks += 1
        total_streamed_bytes += len(chunk)

    print(f"Streamed {total_streamed_bytes:,} bytes across {total_chunks} chunks.")
    assert total_streamed_bytes == synthetic_data_file.stat().st_size


# ============================================================================
# SECTION 2: THE mmap PROTOCOL — ZERO-COPY DISK ACCESS
# ============================================================================
    print("\n" + "=" * 75)
    print("SECTION 2: MEMORY-MAPPED FILES (mmap) — ZERO-COPY RANDOM ACCESS")
    print("=" * 75)

    # Insert a target marker needle in the middle of our file for searching
    with open(synthetic_data_file, "r+b") as f:
        f.seek(1_000_000)
        f.write(b"TARGET_NEEDLE_42")

    with open(synthetic_data_file, "r+b") as f:
        # Create memory-map
        # ACCESS_READ prevents accidental modifications, ACCESS_WRITE allows edits
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as mm:
            print(f"mmap size: {len(mm):,} bytes in virtual memory space.")

            # 1. Zero-Copy Slicing: Directly reads bytes without allocating new strings
            first_10_bytes = mm[:10]
            print(f"Slice [0:10]: {first_10_bytes}")

            # 2. Lightning-fast pattern search directly on virtual memory pages
            t0 = time.perf_counter()
            pos = mm.find(b"TARGET_NEEDLE_42")
            t_search = (time.perf_counter() - t0) * 1000
            print(f"Found needle at byte offset: {pos:,} in {t_search:.3f} ms!")
            assert pos == 1_000_000

            # 3. In-place modification without rewriting the whole 2MB file!
            mm[pos:pos + 16] = b"VERIFIED_FOUND__"
            mm.flush()  # Flushes dirty pages back to disk

    # Verify modification persisted directly to physical disk
    with open(synthetic_data_file, "rb") as f:
        f.seek(1_000_000)
        modified_bytes = f.read(16)
        print(f"Direct disk verification after mmap edit: {modified_bytes}")
        assert modified_bytes == b"VERIFIED_FOUND__"


# ============================================================================
# SECTION 3: ENTERPRISE AI PATTERN — StreamingTokenBatcher
# ============================================================================
    print("\n" + "=" * 75)
    print("SECTION 3: ENTERPRISE AI PATTERN — StreamingTokenBatcher")
    print("=" * 75)

    class StreamingTokenBatcher:
        """
        Simulates an enterprise LLM training batcher that streams tokens
        from disk in fixed micro-batches without loading the corpus into RAM.
        """
        def __init__(self, filepath: Path, batch_size: int = 4):
            self.filepath = filepath
            self.batch_size = batch_size

        def iterate_batches(self) -> Generator[List[bytes], None, None]:
            current_batch: List[bytes] = []
            for chunk in stream_file_chunks(self.filepath, chunk_size=256):
                # Split chunk into 64-byte token slices
                for i in range(0, len(chunk), 64):
                    token = chunk[i:i + 64]
                    if len(token) == 64:
                        current_batch.append(token)
                        if len(current_batch) == self.batch_size:
                            yield current_batch
                            current_batch = []
            if current_batch:
                yield current_batch

    batcher = StreamingTokenBatcher(synthetic_data_file, batch_size=4)
    sample_batches = 0
    for batch in batcher.iterate_batches():
        sample_batches += 1
        if sample_batches <= 3:
            print(f"  Batch #{sample_batches}: {len(batch)} tokens (Sample token: {batch[0][:15]}...)")
        elif sample_batches == 4:
            print("  ... streaming remaining batches seamlessly ...")

    print(f"Successfully processed training stream across batches!")

finally:
    shutil.rmtree(temp_dir, ignore_errors=True)

print("\n" + "=" * 75)
print("Module 04 Complete: Large-Scale Streaming & mmap Mastered!")
print("=" * 75)

"""
===============================================================================
Day 18: Module 01 - Modern File Systems & Pathlib Architecture
===============================================================================
Author: Sapna Yadav (@Sapnayadav1608)
Topic: Object-Oriented File System Manipulation with PEP 428 pathlib.Path
Architecture: Cross-Platform AI Model Artifacts & Cache Directory Management
===============================================================================

In enterprise AI engineering, managing file paths reliably across Linux (POSIX)
servers (Docker containers, AWS EC2, Kubernetes pods) and Windows workstations
is critical. Legacy code relying on `os.path.join()`, raw string manipulation,
and backslash escaping frequently causes brittle bugs, path injection exploits,
and silent directory mismatches.

Python 3.4+ introduced PEP 428 (`pathlib`), treating paths not as dumb strings,
but as rich, first-class semantic objects with operator overloading (`/`).
This module covers:
  1. pathlib.Path vs os.path: Architectural paradigms & operator overloading.
  2. Pure Paths vs Concrete Paths: Cross-platform emulation without disk access.
  3. Path Resolution & Anchoring: `.resolve()`, `.relative_to()`, `.is_relative_to()`.
  4. Advanced Pattern Matching: `.glob()` vs `.rglob()` (recursive file discovery).
  5. File System Metadata & Invariants: `.stat()`, timestamps, size, permissions.
  6. Enterprise AI Pattern: `ModelArtifactManager` for organized model checkpoints,
     adapters, and tokenizers.
"""

from __future__ import annotations
import os
import shutil
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Dict, List, Optional


# ============================================================================
# SECTION 1: PATHLIB PARADIGM & OPERATOR OVERLOADING
# ============================================================================
print("=" * 75)
print("SECTION 1: PATHLIB OBJECT ARCHITECTURE & OPERATOR OVERLOADING")
print("=" * 75)

# The legacy approach (prone to backslash escaping bugs on Windows)
legacy_path = os.path.join("models", "gemini_pro", "weights.bin")
print(f"Legacy os.path string: {legacy_path} (Type: {type(legacy_path).__name__})")

# The modern Pathlib approach using division operator (/) overloading
base_dir = Path("models")
model_checkpoint = base_dir / "gemini_pro" / "weights.bin"
print(f"Modern Path object:    {model_checkpoint} (Type: {type(model_checkpoint).__name__})")

# Key anatomical properties of Path objects
print(f"  -> .name:      {model_checkpoint.name}       (Full filename)")
print(f"  -> .stem:      {model_checkpoint.stem}       (Filename without extension)")
print(f"  -> .suffix:    {model_checkpoint.suffix}     (Extension)")
print(f"  -> .suffixes:  {Path('dataset.tar.gz').suffixes} (Multi-part extensions)")
print(f"  -> .parent:    {model_checkpoint.parent}     (Immediate parent directory)")
print(f"  -> .parents:   {[str(p) for p in model_checkpoint.parents]} (Ancestor hierarchy)")


# ============================================================================
# SECTION 2: PURE PATHS VS CONCRETE PATHS (Cross-Platform Emulation)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 2: PURE PATHS (Manipulating Linux Paths on Windows & Vice Versa)")
print("=" * 75)

# Pure paths do purely computational operations on strings without calling OS I/O
linux_cloud_path = PurePosixPath("/var/log/ai_agent/traces.jsonl")
windows_dev_path = PureWindowsPath(r"C:\Users\Developer\Models\lora.safetensors")

print(f"Linux Cloud Path:   {linux_cloud_path} (Root: {linux_cloud_path.root})")
print(f"Windows Local Path: {windows_dev_path} (Drive: {windows_dev_path.drive})")

# Path algebra works seamlessly across platforms:
new_linux_log = linux_cloud_path.parent / "audit_metrics.json"
print(f"Constructed Path:   {new_linux_log}")
assert str(new_linux_log) == "/var/log/ai_agent/audit_metrics.json"


# ============================================================================
# SECTION 3: PATH RESOLUTION & SAFE TRAVERSAL
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 3: PATH RESOLUTION, CANONICALIZATION & SECURITY")
print("=" * 75)

# Resolving symbolic links, '..' navigation, and obtaining canonical absolute paths
current_file = Path(__file__).resolve()
workspace_root = current_file.parent.parent.resolve()

print(f"Current File (Canonical): {current_file}")
print(f"Workspace Root:           {workspace_root}")

# Relative path computation
rel_path = current_file.relative_to(workspace_root)
print(f"Relative Path from Root:  {rel_path}")

# Security: Path Traversal Protection
def is_safe_subdirectory(target_path: Path, base_dir: Path) -> bool:
    """
    Prevents path traversal attacks (e.g. '../../etc/passwd' or '../../Windows').
    Returns True only if target_path resides inside base_dir.
    """
    try:
        target_path.resolve().relative_to(base_dir.resolve())
        return True
    except ValueError:
        return False

sandbox_root = Path("d:/learn-python")
malicious_input = Path("d:/learn-python/../../Windows/System32/cmd.exe")
benign_input = Path("d:/learn-python/day18/data.json")

print(f"Is malicious path safe? {is_safe_subdirectory(malicious_input, sandbox_root)}")
print(f"Is benign path safe?    {is_safe_subdirectory(benign_input, sandbox_root)}")
assert not is_safe_subdirectory(malicious_input, sandbox_root)
assert is_safe_subdirectory(benign_input, sandbox_root)


# ============================================================================
# SECTION 4: ADVANCED FILE DISCOVERY (glob & rglob)
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 4: ADVANCED FILE PATTERN MATCHING (.glob & .rglob)")
print("=" * 75)

# Create a temporary sandbox directory tree for experimentation
temp_dir = Path(tempfile.mkdtemp(prefix="ai_model_repo_"))
try:
    # Build a simulated multi-tiered AI repo structure
    (temp_dir / "checkpoints" / "v1").mkdir(parents=True, exist_ok=True)
    (temp_dir / "checkpoints" / "v2").mkdir(parents=True, exist_ok=True)
    (temp_dir / "datasets" / "train").mkdir(parents=True, exist_ok=True)
    (temp_dir / "datasets" / "eval").mkdir(parents=True, exist_ok=True)

    # Populate dummy files
    (temp_dir / "checkpoints" / "v1" / "weights.pt").write_text("model weights v1")
    (temp_dir / "checkpoints" / "v1" / "config.json").write_text('{"hidden_dim": 768}')
    (temp_dir / "checkpoints" / "v2" / "weights.pt").write_text("model weights v2")
    (temp_dir / "checkpoints" / "v2" / "config.json").write_text('{"hidden_dim": 1024}')
    (temp_dir / "datasets" / "train" / "corpus_01.jsonl").write_text('{"prompt": "hello"}')
    (temp_dir / "datasets" / "eval" / "benchmark.jsonl").write_text('{"test": 1}')

    # 1. Non-recursive globbing in checkpoints
    v1_files = list((temp_dir / "checkpoints" / "v1").glob("*.*"))
    print(f"Non-recursive glob in checkpoints/v1: {[f.name for f in v1_files]}")

    # 2. Recursive globbing (.rglob) across the whole project tree
    all_json_files = list(temp_dir.rglob("*.json*"))
    print(f"Recursive rglob for *.json*: {[f.relative_to(temp_dir).as_posix() for f in all_json_files]}")
    assert len(all_json_files) == 4

    # 3. Reading file stat metadata
    stat_info = (temp_dir / "checkpoints" / "v1" / "weights.pt").stat()
    mtime = datetime.fromtimestamp(stat_info.st_mtime, tz=timezone.utc)
    print(f"File Size: {stat_info.st_size} bytes | Last Modified: {mtime.strftime('%Y-%m-%d %H:%M:%S UTC')}")

finally:
    shutil.rmtree(temp_dir, ignore_errors=True)


# ============================================================================
# SECTION 5: ENTERPRISE AI PATTERN — ModelArtifactManager
# ============================================================================
print("\n" + "=" * 75)
print("SECTION 5: ENTERPRISE PATTERN — ModelArtifactManager")
print("=" * 75)

class ModelArtifactManager:
    """
    Production-grade file manager for AI model weights, configs, and adapters.
    Ensures safe directory creation, versioning, and atomic validation.
    """
    def __init__(self, root_dir: Path | str):
        self.root = Path(root_dir).resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def register_model_version(self, model_name: str, version: str) -> Path:
        """Creates versioned directory: <root>/<model_name>/<version>/"""
        version_dir = self.root / model_name / version
        version_dir.mkdir(parents=True, exist_ok=True)
        return version_dir

    def save_checkpoint_metadata(self, model_name: str, version: str, meta: Dict[str, Any]) -> Path:
        import json
        version_dir = self.register_model_version(model_name, version)
        meta_file = version_dir / "checkpoint_metadata.json"
        meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")
        return meta_file

    def list_checkpoints(self, model_name: str) -> List[str]:
        model_dir = self.root / model_name
        if not model_dir.exists():
            return []
        return sorted([d.name for d in model_dir.iterdir() if d.is_dir()])


# Demonstration
demo_temp = Path(tempfile.mkdtemp(prefix="mgr_demo_"))
try:
    mgr = ModelArtifactManager(demo_temp)
    mgr.save_checkpoint_metadata("llama-3-8b", "v1.0", {"loss": 0.42, "epochs": 5})
    mgr.save_checkpoint_metadata("llama-3-8b", "v1.1", {"loss": 0.38, "epochs": 8})
    mgr.save_checkpoint_metadata("llama-3-8b", "v2.0-finetuned", {"loss": 0.29, "epochs": 12})

    versions = mgr.list_checkpoints("llama-3-8b")
    print(f"Registered model checkpoints for 'llama-3-8b': {versions}")
    assert versions == ["v1.0", "v1.1", "v2.0-finetuned"]
finally:
    shutil.rmtree(demo_temp, ignore_errors=True)

print("\n" + "=" * 75)
print("Module 01 Complete: Modern File Systems & Pathlib Architecture Mastered!")
print("=" * 75)

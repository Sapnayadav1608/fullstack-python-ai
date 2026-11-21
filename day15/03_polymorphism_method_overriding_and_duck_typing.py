"""
Day 15: Advanced Object-Oriented Programming (OOP) Part 2
Module 03: Polymorphism, Method Overriding, Duck Typing & Protocols
=============================================================================
Full Stack Python + AI Engineering Track
30-Day Coding Challenge

Topics Covered:
1. Polymorphism: Uniform interfaces over diverse data types.
2. Method Overriding vs Method Overloading: Why Python has no native signature overloading.
3. Duck Typing Philosophy: "If it walks like a duck and quacks like a duck, it's a duck."
4. EAFP (Easier to Ask for Forgiveness than Permission) vs LBYL (Look Before You Leap).
5. Modern Static Duck Typing: `typing.Protocol` (PEP 544 Structural Subtyping).
6. Production Pattern: Unified Multimodal AI Document Ingestion Pipeline.
"""

from typing import Protocol, List, Dict, Any, runtime_checkable
import json


# ============================================================================
# 1. POLYMORPHISM VIA METHOD OVERRIDING
# ============================================================================
"""
WHAT IS POLYMORPHISM?
- Greek for "many shapes".
- In software design, polymorphism allows different classes to expose the same
  method signature, while executing completely different algorithms under the hood.
- Callers do not need to know the exact concrete class — they just call `obj.process()`.
"""

print("=" * 70)
print("1. CLASSICAL POLYMORPHISM & METHOD OVERRIDING")
print("=" * 70)

class NotificationService:
    def send(self, recipient: str, message: str) -> bool:
        raise NotImplementedError("Subclasses must implement send().")


class EmailNotification(NotificationService):
    def send(self, recipient: str, message: str) -> bool:
        print(f"  📧 [EMAIL SMTP] Sent to '{recipient}': {message}")
        return True


class SlackNotification(NotificationService):
    def send(self, recipient: str, message: str) -> bool:
        print(f"  💬 [SLACK WEBHOOK] Sent to channel '{recipient}': {message}")
        return True


class SMSNotification(NotificationService):
    def send(self, recipient: str, message: str) -> bool:
        print(f"  📱 [TWILIO SMS] Sent to '{recipient}': {message}")
        return True


def dispatch_alert(service: NotificationService, target: str, alert_msg: str) -> None:
    """Polymorphic dispatcher: operates on any service implementing .send()."""
    service.send(target, alert_msg)

services: List[NotificationService] = [
    EmailNotification(),
    SlackNotification(),
    SMSNotification()
]

for s in services:
    dispatch_alert(s, "dev-alerts", "High memory usage detected!")


# ============================================================================
# 2. DUCK TYPING: BEHAVIOR OVER INHERITANCE
# ============================================================================
"""
WHAT IS DUCK TYPING?
- "If it walks like a duck and quacks like a duck, it's a duck."
- Python does not require classes to inherit from a shared base class to be polymorphic!
- If an object has a `.read()` method, it can be treated as a file.
- If an object has `__len__()` and `__getitem__()`, it can be treated as a sequence.
"""

print("\n" + "=" * 70)
print("2. DUCK TYPING IN ACTION")
print("=" * 70)

class CloudStorageFile:
    """Does NOT inherit from io.IOBase, but quacks like a file!"""
    def __init__(self, contents: str) -> None:
        self.contents = contents

    def read(self) -> str:
        return self.contents


class InMemoryCacheStream:
    """Also completely unrelated class, but quacks like a file!"""
    def __init__(self, buffer: List[str]) -> None:
        self.buffer = buffer

    def read(self) -> str:
        return "\n".join(self.buffer)


def parse_and_count_words(file_like_object: Any) -> int:
    """Duck-typed function: only cares that object has a callable .read() method!"""
    # EAFP style: Try calling .read(), don't check isinstance()!
    text = file_like_object.read()
    return len(text.split())

cloud_file = CloudStorageFile("Python decorators and generators stream big data seamlessly.")
cache_stream = InMemoryCacheStream(["Line 1: AI Prompt", "Line 2: Vector Embedding"])

print(f"Cloud File Word Count:    {parse_and_count_words(cloud_file)}")
print(f"Cache Stream Word Count:  {parse_and_count_words(cache_stream)}")


# ============================================================================
# 3. MODERN STRUCTURAL SUBTYPING: `typing.Protocol` (PEP 544)
# ============================================================================
"""
Duck typing is great, but how do we get IDE autocompletion and static type checking
without forcing inheritance?
Enter `typing.Protocol` (Python 3.8+):
- Defines an interface statically.
- Any class that implements the methods automatically satisfies the Protocol,
  even if it has ZERO inheritance relationship!
"""

print("\n" + "=" * 70)
print("3. PROTOCOL (STRUCTURAL SUBTYPING) IN PYTHON")
print("=" * 70)

@runtime_checkable
class DocumentParser(Protocol):
    """Protocol defining the contract for document ingestion."""
    def extract_text(self) -> str:
        ...
    def get_metadata(self) -> Dict[str, Any]:
        ...


class PDFParser:
    """Satisfies DocumentParser implicitly without inheriting from it!"""
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def extract_text(self) -> str:
        return "Extracted 20 pages of machine learning architecture from PDF."

    def get_metadata(self) -> Dict[str, Any]:
        return {"format": "PDF", "file": self.filepath, "author": "Arxiv"}


class AudioTranscriptParser:
    """Also satisfies DocumentParser implicitly!"""
    def __init__(self, audio_id: str, duration_sec: int) -> None:
        self.audio_id = audio_id
        self.duration_sec = duration_sec

    def extract_text(self) -> str:
        return "Audio transcribed: 'Welcome back to Day 15 of our Python AI challenge.'"

    def get_metadata(self) -> Dict[str, Any]:
        return {"format": "WAV", "id": self.audio_id, "duration": f"{self.duration_sec}s"}


def ingest_ai_document(parser: DocumentParser) -> None:
    """Enforces protocol compliance at runtime and static type checking!"""
    print(f"  📄 Ingesting {parser.get_metadata()['format']} -> {parser.extract_text()[:40]}...")
    print(f"     Metadata: {parser.get_metadata()}")

pdf = PDFParser("ml_paper.pdf")
audio = AudioTranscriptParser("audio_rec_009", 40)

print(f"Does PDFParser implement DocumentParser? {isinstance(pdf, DocumentParser)}")  # True!
print(f"Does Audio implement DocumentParser?     {isinstance(audio, DocumentParser)}")  # True!

print("\nIngesting documents via unified pipeline:")
ingest_ai_document(pdf)
ingest_ai_document(audio)

print("\n" + "=" * 70)
print("DAY 15 MODULE 03: COMPLETED SUCCESSFULLY! [OK]")
print("=" * 70)

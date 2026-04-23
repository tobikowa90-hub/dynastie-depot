"""Pure helpers for the video ingest pipeline.

No subprocess calls, no network — only file reads for hashing.
Tested in 03_Tools/tests/test_video_ingest_lib.py.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

# ---------- Slug builder ----------

_SLUG_RE = re.compile(r"[^a-z0-9]+")

def build_slug(date_iso: str, channel: str, topic: str, collision_suffix: int | None = None) -> str:
    """Build a vault slug: <YYYY-MM-DD>-<channel>-<topic>[-N].

    Lowercases and kebab-cases channel and topic. Strips non-alphanumeric.
    """
    parts = [date_iso.strip(),
             _SLUG_RE.sub("-", channel.lower()).strip("-"),
             _SLUG_RE.sub("-", topic.lower()).strip("-")]
    slug = "-".join(p for p in parts if p)
    if collision_suffix is not None and collision_suffix > 1:
        slug = f"{slug}-{collision_suffix}"
    return slug


# ---------- Hashing ----------

def sha256_file(path: Path, chunk_size: int = 65536) -> str:
    """Return hex sha256 of file content. Streams to handle large files."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


# ---------- Quality gate ----------

@dataclass
class GateResult:
    passed: bool
    fails: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)
    manual_review: bool = False


def quality_gate(
    *,
    transcript_text: str,
    duration_min: float,
    segments: int,
    detected_lang: str,
    expected_lang: str,
    url_ok: bool,
) -> GateResult:
    """Run §6 quality gate. Returns GateResult."""
    fails: list[str] = []
    warns: list[str] = []

    # FAIL #1 — transcript not empty (>500 chars)
    if len(transcript_text) < 500:
        fails.append("transcript_empty")

    # FAIL #2 — duration missing (yt-dlp didn't extract or video corrupt)
    if duration_min <= 0:
        fails.append("duration_missing")

    # FAIL #6 — URL reachable
    if not url_ok:
        fails.append("url_unreachable")

    # WARN #2 — word density (only if duration is valid)
    if duration_min > 0:
        word_count = len(transcript_text.split())
        wpm = word_count / duration_min
        if wpm < 80:
            warns.append("word_density_low")
        elif wpm > 250:
            warns.append("word_density_high")

    # WARN #3 — segment count (only if duration is valid)
    if duration_min > 0 and segments > 0:
        spm = segments / duration_min
        if spm < 3 or spm > 30:
            warns.append("segment_count_abnormal")

    # WARN #4 — language match (skip if expected_lang not set)
    if expected_lang and detected_lang != expected_lang:
        warns.append("language_mismatch")

    return GateResult(
        passed=not fails,
        fails=fails,
        warns=warns,
        manual_review=bool(warns),
    )

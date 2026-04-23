"""Tests for video_ingest_lib pure functions."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from video_ingest_lib import (
    build_slug,
    sha256_file,
    quality_gate,
    GateResult,
)

FIXT = Path(__file__).parent / "fixtures"


# ---------- build_slug ----------

def test_build_slug_basic():
    assert build_slug("2024-05-04", "brk", "annual qa") == "2024-05-04-brk-annual-qa"

def test_build_slug_lowercases_and_kebabs():
    assert build_slug("2026-01-15", "Acquired", "NVIDIA Deep Dive") == "2026-01-15-acquired-nvidia-deep-dive"

def test_build_slug_strips_special_chars():
    assert build_slug("2026-04-22", "tmo", "Q1/FY26 Earnings — Call!") == "2026-04-22-tmo-q1-fy26-earnings-call"

def test_build_slug_collision_suffix():
    assert build_slug("2026-04-22", "tmo", "q1", collision_suffix=2) == "2026-04-22-tmo-q1-2"


# ---------- sha256_file ----------

def test_sha256_file_deterministic(tmp_path):
    f = tmp_path / "x.txt"
    f.write_bytes(b"hello world")
    h1 = sha256_file(f)
    h2 = sha256_file(f)
    assert h1 == h2
    # Known sha256 for "hello world"
    assert h1 == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"

def test_sha256_file_changes_with_content(tmp_path):
    f = tmp_path / "x.txt"
    f.write_bytes(b"hello")
    h1 = sha256_file(f)
    f.write_bytes(b"world")
    h2 = sha256_file(f)
    assert h1 != h2


# ---------- quality_gate ----------

def test_gate_fails_on_empty_transcript():
    result = quality_gate(transcript_text="", duration_min=10, segments=0,
                          detected_lang="en", expected_lang="en", url_ok=True)
    assert result.passed is False
    assert "transcript_empty" in result.fails

def test_gate_fails_on_short_transcript():
    result = quality_gate(transcript_text="short " * 10, duration_min=10, segments=2,
                          detected_lang="en", expected_lang="en", url_ok=True)
    assert result.passed is False
    assert "transcript_empty" in result.fails  # <500 chars treated as empty

def test_gate_fails_on_unreachable_url():
    result = quality_gate(transcript_text="x" * 600, duration_min=10, segments=20,
                          detected_lang="en", expected_lang="en", url_ok=False)
    assert result.passed is False
    assert "url_unreachable" in result.fails

def test_gate_warns_on_low_word_density():
    text = (FIXT / "sample_transcript_short.md").read_text(encoding="utf-8")
    # ~4 words over 10 min duration → density way below 80 wpm
    result = quality_gate(transcript_text=text * 100, duration_min=60, segments=20,
                          detected_lang="en", expected_lang="en", url_ok=True)
    # Pad transcript to >500 chars but stay below 80 wpm density
    assert "word_density_low" in result.warns

def test_gate_warns_on_lang_mismatch():
    text = (FIXT / "sample_transcript_normal.md").read_text(encoding="utf-8")
    result = quality_gate(transcript_text=text, duration_min=10, segments=50,
                          detected_lang="de", expected_lang="en", url_ok=True)
    assert result.passed is True  # warn, not fail
    assert "language_mismatch" in result.warns

def test_gate_passes_clean():
    text = (FIXT / "sample_transcript_normal.md").read_text(encoding="utf-8")
    result = quality_gate(transcript_text=text, duration_min=10, segments=50,
                          detected_lang="en", expected_lang="en", url_ok=True)
    assert result.passed is True
    assert result.warns == []
    assert result.fails == []
    assert result.manual_review is False

def test_gate_manual_review_set_when_warn():
    text = (FIXT / "sample_transcript_normal.md").read_text(encoding="utf-8")
    result = quality_gate(transcript_text=text, duration_min=10, segments=50,
                          detected_lang="de", expected_lang="en", url_ok=True)
    assert result.manual_review is True

def test_gate_warn_path_passes_with_manual_review():
    """WARN-but-not-FAIL: passed=True, manual_review=True simultaneously."""
    text = (FIXT / "sample_transcript_normal.md").read_text(encoding="utf-8")
    result = quality_gate(transcript_text=text, duration_min=10, segments=50,
                          detected_lang="de", expected_lang="en", url_ok=True)
    assert result.passed is True
    assert result.manual_review is True
    assert "language_mismatch" in result.warns
    assert result.fails == []

def test_gate_fails_on_zero_duration():
    """duration_min == 0 is explicit FAIL, not silent skip."""
    text = (FIXT / "sample_transcript_normal.md").read_text(encoding="utf-8")
    result = quality_gate(transcript_text=text, duration_min=0, segments=50,
                          detected_lang="en", expected_lang="en", url_ok=True)
    assert result.passed is False
    assert "duration_missing" in result.fails

def test_gate_warns_on_high_word_density():
    """Word density > 250 wpm should warn (likely whisper compression artifact)."""
    text = "word " * 5000  # 5000 words over 10 min = 500 wpm
    result = quality_gate(transcript_text=text, duration_min=10, segments=20,
                          detected_lang="en", expected_lang="en", url_ok=True)
    assert "word_density_high" in result.warns

def test_gate_warns_on_abnormal_segment_count():
    """Segments way outside [3, 30] per minute should warn."""
    text = "x" * 1000
    result = quality_gate(transcript_text=text, duration_min=10, segments=1,  # 0.1 spm
                          detected_lang="en", expected_lang="en", url_ok=True)
    assert "segment_count_abnormal" in result.warns

def test_gate_skips_lang_check_when_expected_lang_empty():
    """If expected_lang is empty/None, skip language match check (don't error)."""
    text = (FIXT / "sample_transcript_normal.md").read_text(encoding="utf-8")
    result = quality_gate(transcript_text=text, duration_min=10, segments=50,
                          detected_lang="de", expected_lang="", url_ok=True)
    assert "language_mismatch" not in result.warns

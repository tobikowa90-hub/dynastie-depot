"""Tests for _atomic_io (M5 Concurrency-Hazard-on-Append, stdlib-pure).

Scope: tear-safe single-writer. Multi-process correctness ist Tier-B-Future
(siehe Spec §8 Open Question 2 + Plan-Header G2-Round-1).
"""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import BaseModel

from _atomic_io import atomic_jsonl_append


class _Rec(BaseModel):
    id: int
    payload: str


class TestAtomicJsonlAppend:
    def test_appends_single_record(self, tmp_path: Path) -> None:
        target = tmp_path / "out.jsonl"
        atomic_jsonl_append(target, _Rec(id=1, payload="a"))
        lines = target.read_text(encoding="utf-8").splitlines()
        assert len(lines) == 1
        assert json.loads(lines[0]) == {"id": 1, "payload": "a"}

    def test_appends_multiple_records_in_order(self, tmp_path: Path) -> None:
        target = tmp_path / "out.jsonl"
        for i in range(5):
            atomic_jsonl_append(target, _Rec(id=i, payload=f"p{i}"))
        lines = target.read_text(encoding="utf-8").splitlines()
        assert len(lines) == 5
        assert [json.loads(line)["id"] for line in lines] == [0, 1, 2, 3, 4]

    def test_creates_parent_dir(self, tmp_path: Path) -> None:
        target = tmp_path / "deep" / "nested" / "out.jsonl"
        atomic_jsonl_append(target, _Rec(id=1, payload="x"))
        assert target.exists()

    def test_crash_mid_fsync_leaves_target_unchanged_and_preserves_tempfile(
        self, tmp_path: Path
    ) -> None:
        """v1.2 (Spec-v1.1 M5): Pre-replace-failures MÜSSEN Tempfile erhalten —
        nicht via `os.unlink` aufräumen — damit Tear-Recovery-Inspection möglich ist.
        Target-File muss unverändert bleiben."""
        target = tmp_path / "out.jsonl"
        target.write_text('{"id": 0, "payload": "orig"}\n', encoding="utf-8")
        with patch("_atomic_io.os.fsync", side_effect=OSError("simulated crash")):
            with pytest.raises(OSError, match="simulated crash"):
                atomic_jsonl_append(target, _Rec(id=99, payload="should-not-land"))
        # Target unchanged
        text = target.read_text(encoding="utf-8")
        assert text == '{"id": 0, "payload": "orig"}\n'
        # Tempfile bleibt — Spec-v1.1 §3 M5 "Pre-replace-Failures: Tempfile bleibt liegen"
        tempfiles = list(tmp_path.glob(f".{target.name}.*.tmp"))
        assert len(tempfiles) == 1, (
            f"Expected exactly 1 leftover tempfile, found {len(tempfiles)}"
        )

    def test_unicode_payload_preserved(self, tmp_path: Path) -> None:
        """Verify UTF-8 nicht-ASCII (Umlaute) durch model_dump_json() preserved."""
        target = tmp_path / "out.jsonl"
        atomic_jsonl_append(target, _Rec(id=1, payload="Ümlautß"))
        line = target.read_text(encoding="utf-8").splitlines()[0]
        # Pydantic v2 model_dump_json defaults to UTF-8 native (no ASCII escape)
        assert "Ümlautß" in line

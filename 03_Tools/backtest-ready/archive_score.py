"""Dynasty-Depot v3.7 Backtest-Ready: archive_score CLI.

Validates a ScoreRecord JSON (from file or stdin) and appends it as one line
to `05_Archiv/score_history.jsonl`. Append-only. Four validation layers:

1. JSON parsable
2. Pydantic ScoreRecord validation (arithmetic, DEFCON consistency,
   quality-trap, record_id format via schemas.py)
3. record_id uniqueness against existing JSONL
4. Forward-date-window: source='forward' score_datum must be within
   [today - 3 days, today]

Exit codes:
  0 — success (append or dry-run)
  1 — validation failure
  2 — IO failure

Spec: docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md
Plan: docs/superpowers/plans/2026-04-17-backtest-ready-infrastructure.md (Task 1.2)
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import argparse
import json
from datetime import date, timedelta
from typing import Any

from pydantic import ValidationError

from schemas import ScoreRecord  # noqa: E402


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# 03_Tools/backtest-ready/ → project root is two parents up
PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
DEFAULT_ARCHIVE_PATH: Path = PROJECT_ROOT / "05_Archiv" / "score_history.jsonl"

FORWARD_WINDOW_DAYS: int = 3


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------


def _configure_stdout_utf8() -> None:
    """Windows cp1252 console cannot render ✅; force UTF-8 best-effort."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None:
            continue
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except Exception:
            pass


def _read_json_from_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _read_json_from_stdin() -> Any:
    return json.loads(sys.stdin.read())


def _iter_existing_record_ids(archive_path: Path) -> list[str]:
    """Return all record_ids already present in archive_path (empty if file absent)."""
    if not archive_path.exists():
        return []
    ids: list[str] = []
    with archive_path.open("r", encoding="utf-8") as fh:
        for line_no, raw in enumerate(fh, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                obj = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    f"archive corrupt at line {line_no} of {archive_path}: {exc}"
                ) from exc
            rid = obj.get("record_id")
            if isinstance(rid, str):
                ids.append(rid)
    return ids


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def _check_forward_window(record: ScoreRecord, today: date) -> None:
    """For source=forward, score_datum must be within [today-3d, today]."""
    if record.source != "forward":
        return
    delta = today - record.score_datum
    if delta > timedelta(days=FORWARD_WINDOW_DAYS):
        raise ValueError(
            f"forward record score_datum={record.score_datum.isoformat()} is "
            f"{delta.days} days in the past (max {FORWARD_WINDOW_DAYS})"
        )
    if delta < timedelta(days=0):
        raise ValueError(
            f"forward record score_datum={record.score_datum.isoformat()} is in "
            f"the future (today={today.isoformat()})"
        )


def _check_uniqueness(record: ScoreRecord, archive_path: Path) -> None:
    existing = _iter_existing_record_ids(archive_path)
    if record.record_id in existing:
        raise ValueError(
            f"record_id '{record.record_id}' already exists in "
            f"{archive_path.name}; use --force to override (nicht implementiert)"
        )


# ---------------------------------------------------------------------------
# Append
# ---------------------------------------------------------------------------


def _append_record(record: ScoreRecord, archive_path: Path) -> int:
    """Append one JSONL line and return total record count after append."""
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    payload = record.model_dump(mode="json")
    line = json.dumps(payload, ensure_ascii=False)
    with archive_path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    # Count lines after
    total = 0
    with archive_path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            if raw.strip():
                total += 1
    return total


# ---------------------------------------------------------------------------
# Core pipeline
# ---------------------------------------------------------------------------


def run(
    raw_json: Any,
    *,
    dry_run: bool,
    archive_path: Path,
    today: date | None = None,
) -> tuple[int, str, str]:
    """Pipeline: validate → check forward-window → check uniqueness → (append).

    Returns (exit_code, stdout_msg, stderr_msg). Exactly one of the two msgs
    is non-empty. stderr_msg drives exit_code != 0.
    """
    today = today or date.today()

    # Step 2: Pydantic validation
    try:
        record = ScoreRecord.model_validate(raw_json)
    except ValidationError as exc:
        return 1, "", f"❌ SchemaError: {exc}"

    # Step 4: Forward-window
    try:
        _check_forward_window(record, today=today)
    except ValueError as exc:
        return 1, "", f"❌ ForwardWindowError: {exc}"

    # Step 3: Uniqueness
    try:
        _check_uniqueness(record, archive_path)
    except ValueError as exc:
        return 1, "", f"❌ DuplicateRecordError: {exc}"
    except RuntimeError as exc:
        return 2, "", f"❌ ArchiveCorruptError: {exc}"

    if dry_run:
        return (
            0,
            f"✅ VALID record_id={record.record_id} (dry-run, not appended)",
            "",
        )

    # Append
    try:
        total = _append_record(record, archive_path)
    except OSError as exc:
        return 2, "", f"❌ IOError: {exc}"

    rel = archive_path.relative_to(PROJECT_ROOT) if archive_path.is_relative_to(PROJECT_ROOT) else archive_path
    return (
        0,
        f"✅ APPENDED record_id={record.record_id} → {rel.as_posix()} (total records: {total})",
        "",
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="archive_score",
        description=(
            "Validate and append a Dynasty-Depot ScoreRecord JSON to "
            "05_Archiv/score_history.jsonl (append-only)."
        ),
    )
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument(
        "--file",
        type=Path,
        help="Path to JSON file containing one ScoreRecord object.",
    )
    src.add_argument(
        "--stdin",
        action="store_true",
        help="Read JSON ScoreRecord from stdin.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate only; do not append to the archive.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    _configure_stdout_utf8()
    parser = build_parser()
    args = parser.parse_args(argv)

    # Step 1: JSON parse
    try:
        if args.stdin:
            raw_json = _read_json_from_stdin()
        else:
            file_path: Path = args.file
            if not file_path.exists():
                print(f"❌ IOError: file not found: {file_path}", file=sys.stderr)
                return 2
            raw_json = _read_json_from_file(file_path)
    except json.JSONDecodeError as exc:
        print(f"❌ JSONParseError: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"❌ IOError: {exc}", file=sys.stderr)
        return 2

    exit_code, stdout_msg, stderr_msg = run(
        raw_json,
        dry_run=args.dry_run,
        archive_path=DEFAULT_ARCHIVE_PATH,
    )
    if stdout_msg:
        print(stdout_msg)
    if stderr_msg:
        print(stderr_msg, file=sys.stderr)
    return exit_code


# ---------------------------------------------------------------------------
# Smoke tests
# ---------------------------------------------------------------------------


def _build_valid_forward_record(score_datum: date) -> dict[str, Any]:
    """Build a minimal valid forward ScoreRecord (AVGO-like, v3.7-compliant).

    DEFCON-Thresholds per SKILL.md (fix 2026-04-18): >=80 -> D4 | 65-79 -> D3 | 50-64 -> D2.
    """
    ticker = "AVGO"
    rid = f"{score_datum.isoformat()}_{ticker}_vollanalyse"
    # Fundamentals: fwd_pe=1, p_fcf=1, bilanz=8, capex_ocf=7, roic=8, fcf_yield=6,
    # operating_margin=2, maluses=0 → gesamt=33
    # Moat=18, Tech=10, Insider=10, Sentiment=9 → 80 total, DEFCON 4.
    return {
        "schema_version": "1.0",
        "record_id": rid,
        "source": "forward",
        "ticker": ticker,
        "score_datum": score_datum.isoformat(),
        "analyse_typ": "vollanalyse",
        "defcon_version": "v3.7",
        "kurs": {
            "wert": 1847.32,
            "waehrung": "USD",
            "referenz": "close_of_score_datum",
            "quelle": "yahoo_eod",
        },
        "market_cap": {"wert": 865.4e9, "waehrung": "USD"},
        "scores": {
            "fundamentals": {
                "gesamt": 33,
                "fwd_pe": 1,
                "p_fcf": 1,
                "bilanz": 8,
                "capex_ocf": 7,
                "roic": 8,
                "fcf_yield": 6,
                "operating_margin": 2,
                "sbc_malus": 0,
                "accruals_malus": 0,
                "tariff_malus": 0,
            },
            "moat": {
                "gesamt": 18,
                "rating": "wide",
                "quellen": ["switching_costs", "intangibles"],
                "gm_trend_delta": 0,
                "pricing_power_bonus": 1,
            },
            "technicals": {
                "gesamt": 10,
                "ath_distanz": 4,
                "rel_staerke": 3,
                "trend_lage": 3,
                "dcf_relation_delta": 0,
            },
            "insider": {
                "gesamt": 10,
                "net_buy_6m": 4,
                "ownership": 3,
                "kein_20m_selling": 3,
            },
            "sentiment": {
                "gesamt": 9,
                "strong_buy_ratio": 4,
                "sell_ratio": 3,
                "pt_upside": 2,
                "eps_revision_delta": 0,
                "pt_dispersion_delta": 0,
            },
        },
        "score_gesamt": 80,
        "defcon_level": 4,
        "flags": {"aktiv_ids": [], "bei_analyse_referenziert": []},
        "metriken_roh": {
            "fwd_pe": 22.1,
            "p_fcf": 19.8,
            "operating_margin_ttm_pct": 32.1,
        },
        "quellen": {
            "fundamentals": "defeatbeta",
            "technicals": "shibui",
            "insider": "openinsider+sec_edgar",
            "moat": "gurufocus",
            "sentiment": "zacks+yahoo",
        },
        "notizen": "archive_score smoke-test record",
    }


def _smoke_tests() -> None:
    import tempfile

    today = date.today()

    # Test 1: dry-run with a valid forward record → exit 0, VALID message
    valid = _build_valid_forward_record(today)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_archive = Path(tmp) / "score_history.jsonl"
        exit_code, out, err = run(valid, dry_run=True, archive_path=tmp_archive, today=today)
        assert exit_code == 0, f"[1] expected 0, got {exit_code} (err={err})"
        assert "VALID" in out and "dry-run" in out, f"[1] unexpected stdout: {out!r}"
        assert not tmp_archive.exists() or tmp_archive.stat().st_size == 0, (
            f"[1] dry-run must not touch archive: {tmp_archive} size={tmp_archive.stat().st_size if tmp_archive.exists() else 0}"
        )
    print("  [1/5] dry-run valid forward record → VALID, no write")

    # Test 2: invalid JSON — handled at CLI-entry level, but run() is post-parse,
    # so we simulate by calling model_validate with a non-object.
    # Use a broken JSON string and verify _read_json_from_stdin equivalent.
    try:
        json.loads("{ not valid json }")
    except json.JSONDecodeError:
        pass
    else:  # pragma: no cover
        raise AssertionError("[2] expected JSONDecodeError on broken input")
    # And ensure run() rejects a non-dict cleanly (pydantic ValidationError)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_archive = Path(tmp) / "score_history.jsonl"
        exit_code, out, err = run(
            "not a dict", dry_run=True, archive_path=tmp_archive, today=today
        )
        assert exit_code == 1, f"[2] expected 1, got {exit_code}"
        assert "SchemaError" in err, f"[2] unexpected stderr: {err!r}"
    print("  [2/5] invalid JSON / non-dict payload → SchemaError exit 1")

    # Test 3: arithmetic schema violation (wrong score_gesamt)
    bad_arith = _build_valid_forward_record(today)
    bad_arith["score_gesamt"] = bad_arith["score_gesamt"] + 1  # off-by-one
    with tempfile.TemporaryDirectory() as tmp:
        tmp_archive = Path(tmp) / "score_history.jsonl"
        exit_code, out, err = run(
            bad_arith, dry_run=True, archive_path=tmp_archive, today=today
        )
        assert exit_code == 1, f"[3] expected 1, got {exit_code}"
        assert "SchemaError" in err and "arithmetic mismatch" in err, (
            f"[3] unexpected stderr: {err!r}"
        )
    print("  [3/5] arithmetic mismatch → SchemaError exit 1")

    # Test 4: forward-window violation (score_datum 10 days ago)
    old_record = _build_valid_forward_record(today - timedelta(days=10))
    with tempfile.TemporaryDirectory() as tmp:
        tmp_archive = Path(tmp) / "score_history.jsonl"
        exit_code, out, err = run(
            old_record, dry_run=True, archive_path=tmp_archive, today=today
        )
        assert exit_code == 1, f"[4] expected 1, got {exit_code}"
        assert "ForwardWindowError" in err, f"[4] unexpected stderr: {err!r}"
    print("  [4/5] forward-window violation (10 days old) → ForwardWindowError exit 1")

    # Test 5: real append + duplicate detection
    with tempfile.TemporaryDirectory() as tmp:
        tmp_archive = Path(tmp) / "score_history.jsonl"
        rec = _build_valid_forward_record(today)
        exit_code, out, err = run(rec, dry_run=False, archive_path=tmp_archive, today=today)
        assert exit_code == 0, f"[5a] expected 0, got {exit_code} (err={err})"
        assert "APPENDED" in out and "total records: 1" in out, (
            f"[5a] unexpected stdout: {out!r}"
        )
        assert tmp_archive.exists() and tmp_archive.stat().st_size > 0

        # verify JSONL shape: exactly one line, valid JSON, record_id matches
        with tmp_archive.open("r", encoding="utf-8") as fh:
            lines = [ln for ln in fh.read().splitlines() if ln.strip()]
        assert len(lines) == 1, f"[5a] expected 1 line, got {len(lines)}"
        parsed = json.loads(lines[0])
        assert parsed["record_id"] == rec["record_id"]

        # Re-append same record → duplicate
        exit_code, out, err = run(rec, dry_run=False, archive_path=tmp_archive, today=today)
        assert exit_code == 1, f"[5b] expected 1, got {exit_code}"
        assert "DuplicateRecordError" in err, f"[5b] unexpected stderr: {err!r}"
        # File must still have exactly 1 line
        with tmp_archive.open("r", encoding="utf-8") as fh:
            lines = [ln for ln in fh.read().splitlines() if ln.strip()]
        assert len(lines) == 1, f"[5b] duplicate attempt appended; now {len(lines)} lines"
    print("  [5/5] append + duplicate detection → 1 line persisted, duplicate rejected")

    print("✅ all archive_score smoke tests passed")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    _configure_stdout_utf8()
    if len(sys.argv) == 1:
        # No args → smoke tests
        _smoke_tests()
        sys.exit(0)
    sys.exit(main())

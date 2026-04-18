"""One-shot backfill CLI for FLAG events documented in CORE-MEMORY + config.yaml.

Reconstructs historical `source="backfill"` FlagEvent-records and appends them to
`05_Archiv/flag_events.jsonl`. Schema is imported from `schemas.py` (single source
of truth); this script is pure I/O + a hard-coded FLAG catalogue.

Design notes (per spec 2026-04-16 §6.4 + task-brief):
  - Only 2 of 4 known FLAGs are archivable:
      * MSFT capex_ocf  → wert=83.6, trigger 2026-01-15 (Monatsmitten-Proxy)
      * GOOGL capex_ocf → wert=None, trigger 2026-03-15 (Proxy)
  - APH is score-based → FLAG-Typ enum (capex_ocf | fcf_trend_neg |
    insider_selling_20m | tariff_exposure) deckt das nicht ab → skip + log.
  - AVGO insider-selling status=REVIEW_PENDING (Post-Vesting-Hypothese offen)
    → spec §9.2 "no guessing" → skip + log.
  - kurs_bei_event ist Pflicht im Schema, historischer Kurs aber nicht verfügbar
    → wert=0.0, waehrung="UNKNOWN", referenz="backfill_not_available",
      quelle="backfill".
  - Uniqueness gegen existierende flag_events.jsonl-Trigger (Idempotenz).
  - Fehler/Skips → `05_Archiv/_parser_errors.log` (append).
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).parent))
from schemas import FlagEvent  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

from pydantic import ValidationError  # noqa: E402


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT: Path = Path(__file__).parent.parent.parent
ARCHIVE_PATH: Path = ROOT / "05_Archiv" / "flag_events.jsonl"
ERROR_LOG_PATH: Path = ROOT / "05_Archiv" / "_parser_errors.log"


# ---------------------------------------------------------------------------
# Hard-coded backfill catalogue
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class BackfillCandidate:
    """Intermediate struct before FlagEvent validation.

    `wert` may be None (rohwert nicht rekonstruierbar) — der Pydantic-
    Direction-Validator überspringt in dem Fall (per schemas.py §FlagEvent).
    `skip_reason` != None → Candidate wird nicht archiviert (APH/AVGO).
    """

    ticker: str
    flag_typ: str
    wert: Optional[float]
    trigger_datum: str  # ISO
    metrik_definition: str
    notizen: str
    skip_reason: Optional[str] = None


# Alle 4 bekannten FLAGs (Plan Task 2.2). 2 archivierbar, 2 skipped.
CATALOGUE: list[BackfillCandidate] = [
    BackfillCandidate(
        ticker="MSFT",
        flag_typ="capex_ocf",
        wert=83.6,
        trigger_datum="2026-01-15",
        metrik_definition="Q2_FY26_GAAP_bereinigt_83.6pct",
        notizen=(
            "Backfill-Datum Proxy: Monatsmitte Januar 2026 "
            "(Q2 FY26 Earnings Call ca. 30.01.2026, exakter Trigger-Tag "
            "nicht rekonstruierbar). CORE-MEMORY §1: CapEx/OCF Q2 FY26 "
            "83.6% GAAP, bereinigt um Finance Leases ~63% (>60%-Schwelle)."
        ),
    ),
    BackfillCandidate(
        ticker="GOOGL",
        flag_typ="capex_ocf",
        wert=None,  # Rohwert nicht in CORE-MEMORY dokumentiert
        trigger_datum="2026-03-15",
        metrik_definition="fy26_guidance_capex_ratio_above_60pct",
        notizen=(
            "Rohwert nicht in CORE-MEMORY rekonstruierbar. Konservativ: "
            "wert=null gesetzt (Direction-Validator skipped). Trigger-"
            "Datum-Proxy: Monatsmitte März 2026. CORE-MEMORY §4 hat "
            "26.03.2026 als Score-Datum (Score 72, 🔴 FLAG kein Einstieg); "
            "CORE-MEMORY §3 nennt CapEx FY26 ~75% OCF."
        ),
    ),
    BackfillCandidate(
        ticker="APH",
        flag_typ="score_basiert",  # NICHT im schema-enum
        wert=None,
        trigger_datum="2026-03-15",
        metrik_definition="n/a",
        notizen="n/a",
        skip_reason=(
            "APH: score-based FLAG type not in schema enum (skipped, intentional)"
        ),
    ),
    BackfillCandidate(
        ticker="AVGO",
        flag_typ="insider_selling_20m",
        wert=123_000_000.0,
        trigger_datum="2026-04-02",
        metrik_definition="insider_selling_aggregate_usd",
        notizen="n/a",
        skip_reason=(
            "AVGO: insider_selling_20m status=REVIEW_PENDING "
            "(skipped per spec §9.2 no guessing)"
        ),
    ),
]


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------


def _load_existing_flag_ids(path: Path) -> set[str]:
    """Return set of `flag_id` for event_typ='trigger' already in archive."""
    if not path.exists():
        return set()
    out: set[str] = set()
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                if rec.get("event_typ") == "trigger":
                    fid = rec.get("flag_id")
                    if isinstance(fid, str):
                        out.add(fid)
    except (OSError, json.JSONDecodeError) as e:
        print(f"\u274c IOError/JSONError reading {path}: {e}", file=sys.stderr)
        sys.exit(2)
    return out


def _append_event(path: Path, event: FlagEvent) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(event.model_dump_json() + "\n")


def _append_error_log(path: Path, message: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().isoformat(timespec="seconds")
    with path.open("a", encoding="utf-8") as f:
        f.write(f"[{ts}] backfill_flags.py: {message}\n")


# ---------------------------------------------------------------------------
# Build FlagEvent
# ---------------------------------------------------------------------------


def _build_event(cand: BackfillCandidate) -> FlagEvent:
    """Validate + return FlagEvent. Raises ValidationError on failure."""
    flag_id = f"{cand.ticker}_{cand.flag_typ}_{cand.trigger_datum}"
    payload: dict[str, Any] = {
        "schema_version": "1.0",
        "flag_id": flag_id,
        "source": "backfill",
        "ticker": cand.ticker,
        "flag_typ": cand.flag_typ,
        "event_typ": "trigger",
        "event_datum": cand.trigger_datum,
        "metrik": {
            "name": "capex_ocf_pct",  # beide archivierbaren sind capex_ocf
            "wert": cand.wert,
            "schwelle": 60.0,
            "definition": cand.metrik_definition,
        },
        "kurs_bei_event": {
            "wert": 0.0,
            "waehrung": "UNKNOWN",
            "referenz": "backfill_not_available",
            "quelle": "backfill",
        },
        "related_score_record_id": None,
        "notizen": cand.notizen,
    }
    return FlagEvent.model_validate(payload)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------


@dataclass
class Summary:
    parsed: int = 0
    writable: int = 0
    skipped: int = 0
    failed: int = 0
    duplicates: int = 0


def run(
    *,
    archive_path: Path,
    error_log_path: Path,
    dry_run: bool,
    verbose: bool,
) -> Summary:
    existing = _load_existing_flag_ids(archive_path)
    if verbose:
        print(f"archive: {archive_path}")
        print(f"existing trigger flag_ids: {len(existing)}")

    summary = Summary(parsed=len(CATALOGUE))

    for cand in CATALOGUE:
        tag = f"{cand.ticker}_{cand.flag_typ}_{cand.trigger_datum}"

        if cand.skip_reason is not None:
            summary.skipped += 1
            _append_error_log(error_log_path, cand.skip_reason)
            if verbose:
                print(f"  SKIP {tag}: {cand.skip_reason}")
            continue

        if tag in existing:
            summary.duplicates += 1
            if verbose:
                print(f"  DUP  {tag}: already present (idempotent skip)")
            continue

        try:
            event = _build_event(cand)
        except (ValidationError, ValueError) as e:
            summary.failed += 1
            msg = f"{tag}: ValidationError — {e}"
            _append_error_log(error_log_path, msg)
            print(f"\u274c FAIL {tag}: {e}", file=sys.stderr)
            continue

        summary.writable += 1
        if dry_run:
            if verbose:
                print(f"  VALID {event.flag_id} (dry-run)")
            continue

        _append_event(archive_path, event)
        if verbose:
            print(f"  APPENDED {event.flag_id}")

    return summary


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="backfill_flags.py",
        description=(
            "One-shot: reconstruct historical FLAG events from CORE-MEMORY "
            "and append as source='backfill' records to flag_events.jsonl."
        ),
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate only; do not write to flag_events.jsonl.",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="Per-candidate log lines on stdout.",
    )
    return p


def main(argv: Optional[list[str]] = None) -> int:
    args = _build_parser().parse_args(argv)
    summary = run(
        archive_path=ARCHIVE_PATH,
        error_log_path=ERROR_LOG_PATH,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )

    mode = "DRY-RUN" if args.dry_run else "WRITE"
    print(
        f"[{mode}] parsed={summary.parsed} "
        f"writable={summary.writable} "
        f"skipped={summary.skipped} "
        f"duplicates={summary.duplicates} "
        f"failed={summary.failed}"
    )
    if not args.dry_run and summary.writable > 0:
        print(f"\u2705 appended {summary.writable} record(s) \u2192 {ARCHIVE_PATH}")
    if summary.skipped > 0 or summary.failed > 0:
        print(f"see {ERROR_LOG_PATH} for skip/error details")

    return 0 if summary.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

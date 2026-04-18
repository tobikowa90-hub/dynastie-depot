"""FLAG-Event-CLI for the Dynasty-Depot backtest-ready archive.

Three subcommands — trigger / resolve / list — over `05_Archiv/flag_events.jsonl`.
Schema lives in `schemas.py` (single source of truth); this CLI is pure I/O.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable, Optional

sys.path.insert(0, str(Path(__file__).parent))
from schemas import FlagEvent, FlagMetrik, Kurs, FLAG_RULES  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

from pydantic import ValidationError  # noqa: E402


# ---------------------------------------------------------------------------
# Paths + constants
# ---------------------------------------------------------------------------

ARCHIVE_PATH: Path = Path(__file__).parent.parent.parent / "05_Archiv" / "flag_events.jsonl"

# Map FLAG-Typ → metrik.name (Konvention Section 4.2 der Spec).
FLAG_METRIK_NAME: dict[str, str] = {
    "capex_ocf": "capex_ocf_pct",
    "fcf_trend_neg": "fcf_yoy_delta_pct",
    "insider_selling_20m": "insider_selling_20m_usd",
    "tariff_exposure": "tariff_exposure_pct",
}

# flag_id ← TICKER_FLAGTYP_YYYY-MM-DD (kombiniert für Parsing bei `resolve`).
FLAG_ID_PARSE_RE: re.Pattern[str] = re.compile(
    r"^(?P<ticker>[A-Z]{1,5}(?:\.[A-Z]{1,2})?)_(?P<flag_typ>[a-z_0-9]+)_(?P<datum>\d{4}-\d{2}-\d{2})$"
)


# ---------------------------------------------------------------------------
# Archive I/O
# ---------------------------------------------------------------------------


def _load_events(path: Path) -> list[dict[str, Any]]:
    """Read JSONL, return list of raw dicts. Missing file → []."""
    if not path.exists():
        return []
    out: list[dict[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                out.append(json.loads(line))
    except OSError as e:
        print(f"\u274c IOError: cannot read {path}: {e}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"\u274c JSONError: malformed line in {path}: {e}", file=sys.stderr)
        sys.exit(2)
    return out


def _append_event(path: Path, record: FlagEvent) -> None:
    """Append single FlagEvent as JSONL line."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(record.model_dump_json() + "\n")
    except OSError as e:
        print(f"\u274c IOError: cannot write {path}: {e}", file=sys.stderr)
        sys.exit(2)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_flag_id(flag_id: str) -> tuple[str, str, str]:
    """Return (ticker, flag_typ, datum) or exit with error."""
    m = FLAG_ID_PARSE_RE.match(flag_id)
    if not m:
        print(
            f"\u274c ValueError: flag_id '{flag_id}' has invalid format; "
            f"expected TICKER_FLAGTYP_YYYY-MM-DD",
            file=sys.stderr,
        )
        sys.exit(1)
    return m.group("ticker"), m.group("flag_typ"), m.group("datum")


def _find_event(
    events: Iterable[dict[str, Any]], flag_id: str, event_typ: str
) -> Optional[dict[str, Any]]:
    for rec in events:
        if rec.get("flag_id") == flag_id and rec.get("event_typ") == event_typ:
            return rec
    return None


def _build_flag_event(
    *,
    flag_id: str,
    ticker: str,
    flag_typ: str,
    event_typ: str,
    event_datum: str,
    metrik_wert: float,
    metrik_definition: str,
    kurs_wert: float,
    waehrung: str,
    kurs_quelle: str,
    source: str,
    related_score_record_id: Optional[str],
    notizen: Optional[str],
) -> FlagEvent:
    """Construct + validate FlagEvent; schwelle/name derived from FLAG_RULES."""
    if flag_typ not in FLAG_RULES:
        raise ValueError(
            f"unknown flag_typ '{flag_typ}'; expected one of {sorted(FLAG_RULES)}"
        )
    schwelle, _direction = FLAG_RULES[flag_typ]
    metrik_name = FLAG_METRIK_NAME[flag_typ]

    referenz = (
        "close_of_event_datum" if event_typ in ("trigger", "resolution") else "close_of_event_datum"
    )

    return FlagEvent.model_validate(
        {
            "schema_version": "1.0",
            "flag_id": flag_id,
            "source": source,
            "ticker": ticker,
            "flag_typ": flag_typ,
            "event_typ": event_typ,
            "event_datum": event_datum,
            "metrik": {
                "name": metrik_name,
                "wert": metrik_wert,
                "schwelle": schwelle,
                "definition": metrik_definition,
            },
            "kurs_bei_event": {
                "wert": kurs_wert,
                "waehrung": waehrung,
                "referenz": referenz,
                "quelle": kurs_quelle,
            },
            "related_score_record_id": related_score_record_id,
            "notizen": notizen,
        }
    )


# ---------------------------------------------------------------------------
# Subcommand: trigger
# ---------------------------------------------------------------------------


def cmd_trigger(args: argparse.Namespace, archive_path: Path) -> int:
    ticker = args.ticker
    flag_typ = args.flag_typ
    datum_str = args.datum if isinstance(args.datum, str) else args.datum.isoformat()
    flag_id = f"{ticker}_{flag_typ}_{datum_str}"

    # Uniqueness-Check gegen existierende Trigger.
    existing = _load_events(archive_path)
    if _find_event(existing, flag_id, "trigger") is not None:
        print(
            f"\u274c ValueError: flag_id '{flag_id}' already exists as trigger record",
            file=sys.stderr,
        )
        return 1

    try:
        event = _build_flag_event(
            flag_id=flag_id,
            ticker=ticker,
            flag_typ=flag_typ,
            event_typ="trigger",
            event_datum=datum_str,
            metrik_wert=args.metrik_wert,
            metrik_definition=args.metrik_definition,
            kurs_wert=args.kurs,
            waehrung=args.waehrung,
            kurs_quelle=args.kurs_quelle,
            source=args.source,
            related_score_record_id=args.related_score_record_id,
            notizen=args.notizen,
        )
    except (ValidationError, ValueError) as e:
        print(f"\u274c ValidationError: {e}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"\u2705 VALID flag_id={flag_id} (dry-run, not appended)")
        return 0

    _append_event(archive_path, event)
    print(f"\u2705 APPENDED flag_id={flag_id} event_typ=trigger \u2192 flag_events.jsonl")
    return 0


# ---------------------------------------------------------------------------
# Subcommand: resolve
# ---------------------------------------------------------------------------


def cmd_resolve(args: argparse.Namespace, archive_path: Path) -> int:
    flag_id = args.flag_id
    ticker, flag_typ, _trigger_datum = _parse_flag_id(flag_id)

    if flag_typ not in FLAG_RULES:
        print(
            f"\u274c ValueError: flag_id '{flag_id}' references unknown flag_typ '{flag_typ}'",
            file=sys.stderr,
        )
        return 1

    events = _load_events(archive_path)

    # Pflicht A: Trigger muss existieren.
    if _find_event(events, flag_id, "trigger") is None:
        print(
            f"\u274c ValueError: no trigger record found for flag_id '{flag_id}'",
            file=sys.stderr,
        )
        return 1

    # Pflicht B: Resolution darf nicht schon existieren.
    if _find_event(events, flag_id, "resolution") is not None:
        print(
            f"\u274c ValueError: flag_id '{flag_id}' is already resolved",
            file=sys.stderr,
        )
        return 1

    datum_str = args.datum if isinstance(args.datum, str) else args.datum.isoformat()
    try:
        event = _build_flag_event(
            flag_id=flag_id,
            ticker=ticker,
            flag_typ=flag_typ,
            event_typ="resolution",
            event_datum=datum_str,
            metrik_wert=args.metrik_wert,
            metrik_definition=args.metrik_definition,
            kurs_wert=args.kurs,
            waehrung=args.waehrung,
            kurs_quelle=args.kurs_quelle,
            source=args.source,
            related_score_record_id=args.related_score_record_id,
            notizen=args.notizen,
        )
    except (ValidationError, ValueError) as e:
        print(f"\u274c ValidationError: {e}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"\u2705 VALID flag_id={flag_id} (dry-run, not appended)")
        return 0

    _append_event(archive_path, event)
    print(f"\u2705 APPENDED flag_id={flag_id} event_typ=resolution \u2192 flag_events.jsonl")
    return 0


# ---------------------------------------------------------------------------
# Subcommand: list
# ---------------------------------------------------------------------------


def cmd_list(args: argparse.Namespace, archive_path: Path) -> int:
    events = _load_events(archive_path)

    filtered: list[dict[str, Any]] = []
    resolved_ids: set[str] = {
        rec["flag_id"] for rec in events if rec.get("event_typ") == "resolution"
    }

    for rec in events:
        if args.ticker and rec.get("ticker") != args.ticker:
            continue
        if args.flag_typ and rec.get("flag_typ") != args.flag_typ:
            continue
        if args.aktiv:
            # Nur Trigger ohne zugehörige Resolution.
            if rec.get("event_typ") != "trigger":
                continue
            if rec.get("flag_id") in resolved_ids:
                continue
        filtered.append(rec)

    if not filtered:
        print("no matching FLAG events")
        return 0

    # Tabelle: flag_id | event_typ | datum | ticker | metrik_wert | notizen
    headers = ["flag_id", "event_typ", "datum", "ticker", "metrik_wert", "notizen"]
    rows: list[list[str]] = [headers]
    for rec in filtered:
        metrik = rec.get("metrik") or {}
        rows.append(
            [
                str(rec.get("flag_id", "")),
                str(rec.get("event_typ", "")),
                str(rec.get("event_datum", "")),
                str(rec.get("ticker", "")),
                str(metrik.get("wert", "")),
                str(rec.get("notizen") or ""),
            ]
        )

    widths = [max(len(r[i]) for r in rows) for i in range(len(headers))]
    for i, row in enumerate(rows):
        line = " | ".join(cell.ljust(widths[j]) for j, cell in enumerate(row))
        print(line)
        if i == 0:
            print("-+-".join("-" * widths[j] for j in range(len(headers))))

    return 0


# ---------------------------------------------------------------------------
# argparse wiring
# ---------------------------------------------------------------------------


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="archive_flag.py",
        description="FLAG-Event-CLI for Dynasty-Depot backtest-ready archive.",
    )
    p.add_argument(
        "--smoke-test",
        action="store_true",
        help="Run internal smoke tests on a temp archive (no subcommand needed).",
    )

    sub = p.add_subparsers(dest="cmd")

    # trigger
    pt = sub.add_parser("trigger", help="Append a new FLAG trigger record.")
    pt.add_argument("--ticker", required=True)
    pt.add_argument(
        "--flag-typ",
        required=True,
        choices=sorted(FLAG_RULES.keys()),
        help="FLAG-Typ (determines schwelle + metrik.name).",
    )
    pt.add_argument("--datum", required=True, help="Event datum (YYYY-MM-DD).")
    pt.add_argument("--metrik-wert", required=True, type=float)
    pt.add_argument("--metrik-definition", required=True)
    pt.add_argument("--kurs", required=True, type=float)
    pt.add_argument("--waehrung", required=True)
    pt.add_argument("--kurs-quelle", required=True)
    pt.add_argument("--related-score-record-id", default=None)
    pt.add_argument("--notizen", default=None)
    pt.add_argument("--source", choices=["forward", "backfill"], default="forward")
    pt.add_argument("--dry-run", action="store_true")

    # resolve
    pr = sub.add_parser("resolve", help="Append a resolution record for an existing trigger.")
    pr.add_argument("--flag-id", required=True)
    pr.add_argument("--datum", required=True, help="Event datum (YYYY-MM-DD).")
    pr.add_argument("--metrik-wert", required=True, type=float)
    pr.add_argument("--metrik-definition", required=True)
    pr.add_argument("--kurs", required=True, type=float)
    pr.add_argument("--waehrung", required=True)
    pr.add_argument("--kurs-quelle", required=True)
    pr.add_argument("--related-score-record-id", default=None)
    pr.add_argument("--notizen", default=None)
    pr.add_argument("--source", choices=["forward", "backfill"], default="forward")
    pr.add_argument("--dry-run", action="store_true")

    # list
    pl = sub.add_parser("list", help="Query FLAG events (read-only).")
    pl.add_argument("--ticker", default=None)
    pl.add_argument("--flag-typ", choices=sorted(FLAG_RULES.keys()), default=None)
    pl.add_argument(
        "--aktiv",
        action="store_true",
        help="Nur Trigger ohne Resolution.",
    )

    return p


def main(argv: Optional[list[str]] = None, archive_path: Optional[Path] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    path = archive_path if archive_path is not None else ARCHIVE_PATH

    if args.smoke_test:
        return _run_smoke_tests()

    if args.cmd == "trigger":
        return cmd_trigger(args, path)
    if args.cmd == "resolve":
        return cmd_resolve(args, path)
    if args.cmd == "list":
        return cmd_list(args, path)

    parser.print_help()
    return 0


# ---------------------------------------------------------------------------
# Smoke tests — monkeypatch archive path to a temp file; real 05_Archiv bleibt unverändert.
# ---------------------------------------------------------------------------


def _run_smoke_tests() -> int:
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="archive_flag_smoke_"))
    tmp_archive = tmp / "flag_events.jsonl"

    def run(argv: list[str]) -> tuple[int, str, str]:
        """Run main() capturing stdout/stderr."""
        import io
        import contextlib

        out = io.StringIO()
        err = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                rc = main(argv, archive_path=tmp_archive)
            except SystemExit as e:
                rc = int(e.code) if e.code is not None else 0
        return rc, out.getvalue(), err.getvalue()

    # 1) Trigger GOOGL capex_ocf (valid) → VALID (dry-run first, then real)
    rc, out, err = run(
        [
            "trigger",
            "--ticker", "GOOGL",
            "--flag-typ", "capex_ocf",
            "--datum", "2025-10-28",
            "--metrik-wert", "78",
            "--metrik-definition", "annual_cash_flow_fy26_guidance",
            "--kurs", "142.30",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
            "--related-score-record-id", "2025-10-28_GOOGL_vollanalyse",
            "--notizen", "FY26 Guidance 74-79% OCF",
            "--dry-run",
        ]
    )
    assert rc == 0, f"[1a] expected rc=0, got {rc}; err={err}"
    assert "VALID" in out, f"[1a] expected VALID, got stdout={out!r}"

    rc, out, err = run(
        [
            "trigger",
            "--ticker", "GOOGL",
            "--flag-typ", "capex_ocf",
            "--datum", "2025-10-28",
            "--metrik-wert", "78",
            "--metrik-definition", "annual_cash_flow_fy26_guidance",
            "--kurs", "142.30",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
        ]
    )
    assert rc == 0, f"[1b] trigger append expected rc=0, got {rc}; err={err}"
    assert "APPENDED" in out, f"[1b] expected APPENDED, got {out!r}"
    print("  [1/7] trigger GOOGL capex_ocf appended")

    # 2) Resolve GOOGL (valid: wert 54 < schwelle 60 → rule held for '>')
    rc, out, err = run(
        [
            "resolve",
            "--flag-id", "GOOGL_capex_ocf_2025-10-28",
            "--datum", "2027-02-15",
            "--metrik-wert", "54",
            "--metrik-definition", "annual_cash_flow_fy27",
            "--kurs", "168.90",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
            "--dry-run",
        ]
    )
    assert rc == 0, f"[2] resolve dry-run expected rc=0, got {rc}; err={err}"
    assert "VALID" in out, f"[2] expected VALID, got {out!r}"
    print("  [2/7] resolve GOOGL dry-run valid")

    # Append actual resolution for later double-resolve test.
    rc, out, err = run(
        [
            "resolve",
            "--flag-id", "GOOGL_capex_ocf_2025-10-28",
            "--datum", "2027-02-15",
            "--metrik-wert", "54",
            "--metrik-definition", "annual_cash_flow_fy27",
            "--kurs", "168.90",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
        ]
    )
    assert rc == 0 and "APPENDED" in out, f"[2b] resolve append: rc={rc}, out={out!r}, err={err}"

    # 3) Resolve on non-existent flag_id → Error
    rc, out, err = run(
        [
            "resolve",
            "--flag-id", "MSFT_fcf_trend_neg_2025-01-01",
            "--datum", "2025-06-01",
            "--metrik-wert", "10",
            "--metrik-definition", "fy25_fcf",
            "--kurs", "400.00",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
        ]
    )
    assert rc == 1, f"[3] expected rc=1, got {rc}"
    assert "no trigger record found" in err, f"[3] expected 'no trigger record found' in err, got {err!r}"
    print("  [3/7] resolve on non-existent trigger rejected")

    # 4) Double-resolve → Error (already resolved above)
    rc, out, err = run(
        [
            "resolve",
            "--flag-id", "GOOGL_capex_ocf_2025-10-28",
            "--datum", "2027-03-01",
            "--metrik-wert", "50",
            "--metrik-definition", "annual_cash_flow_fy27_q4",
            "--kurs", "170.00",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
        ]
    )
    assert rc == 1, f"[4] expected rc=1, got {rc}; out={out!r}, err={err!r}"
    assert "already resolved" in err, f"[4] expected 'already resolved' in err, got {err!r}"
    print("  [4/7] double-resolve rejected")

    # 5) Trigger with wert < schwelle → Pydantic direction-check error
    rc, out, err = run(
        [
            "trigger",
            "--ticker", "AAPL",
            "--flag-typ", "capex_ocf",
            "--datum", "2026-01-15",
            "--metrik-wert", "45",  # < 60 → does NOT violate '>' rule
            "--metrik-definition", "fy26_guidance",
            "--kurs", "195.00",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
        ]
    )
    assert rc == 1, f"[5] expected rc=1, got {rc}; out={out!r}"
    assert "ValidationError" in err and "violate threshold" in err, (
        f"[5] expected direction-check error, got {err!r}"
    )
    print("  [5/7] trigger non-violation rejected by Pydantic")

    # 6) Duplicate trigger (same flag_id trigger again) → Error
    rc, out, err = run(
        [
            "trigger",
            "--ticker", "GOOGL",
            "--flag-typ", "capex_ocf",
            "--datum", "2025-10-28",
            "--metrik-wert", "78",
            "--metrik-definition", "duplicate",
            "--kurs", "142.30",
            "--waehrung", "USD",
            "--kurs-quelle", "yahoo_eod",
        ]
    )
    assert rc == 1, f"[6] expected rc=1, got {rc}"
    assert "already exists as trigger" in err, f"[6] expected duplicate-trigger error, got {err!r}"
    print("  [6/7] duplicate trigger rejected")

    # 7) list --aktiv → no matching (GOOGL trigger is resolved)
    rc, out, err = run(["list", "--aktiv"])
    assert rc == 0, f"[7] list expected rc=0, got {rc}"
    assert "no matching FLAG events" in out, f"[7] expected empty list msg, got {out!r}"
    print("  [7/7] list --aktiv correctly empty")

    # Cleanup
    try:
        tmp_archive.unlink(missing_ok=True)
        tmp.rmdir()
    except OSError:
        pass

    print("\u2705 all archive_flag smoke tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

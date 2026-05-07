"""TMO Record #28 Block-Coverage Migration.

Idempotenter Helper, der ``metriken_roh`` von Record-ID
``2026-04-23_TMO_vollanalyse`` um die fehlenden moat- und technicals-
Rohfelder ergänzt. Pattern analog ``migrate_defcon_drift.py``
(commit ca76114, 21.04.2026).

Hintergrund: Codex-Plan-Review (28.04.2026) zeigte, dass TMO #28
mit ``gm_trend_3j_pct_p_a=null`` + 4 Technicals-Rohfelder null
appendiert wurde (Task 0.1 PASS aktuell, weil Block-Coverage-Validator
noch nicht existiert). Provenance-Gate Plan v3.1 Task 2 fügt den
Validator hinzu — Task 2.7 Re-Validate-Sweep würde dann ohne diese
Migration mit ``empty_blocks=['moat','technicals']`` reißen.

Wert-Herkunft (deterministisch reproduzierbar):

- ``gm_trend_3j_pct_p_a = +0.5``
  yfinance v1.3.0 ``Ticker('TMO').income_stmt`` (annual):
  FY23 GM = 17.100B / 42.857B = 39.90 %
  FY25 GM = 18.239B / 44.557B = 40.93 %
  (FY25 − FY23) / 2 J = +0.515 pp/a → gerundet +0.5

- ``rel_strength_sp500_6m_pct = -16`` (Spec-Feld, primär)
  ``rel_staerke_sp500_6m_pct = -16`` (v3.5-Rename-Alias-Spiegel)
  yfinance ``history(period='1y', end='2026-04-23', auto_adjust=False)``:
  TMO 6M return (2025-10-22 → 2026-04-22) = -9.38 %
  SPY (^GSPC) 6M return                    = +6.55 %
  diff = -15.93 pp → gerundet -16

- ``kurs_vs_200ma_pct = -2.13``
  TMO 2026-04-22 Close = $513.98
  TMO 200MA at 2026-04-22 = $525.17
  (513.98 / 525.17 − 1) × 100 = -2.13 %

- ``ma200_slope = "rising"`` (Schema-Literal["rising","falling","flat"])
  200MA(2026-04-22) / 200MA(~21 Trading-Days vorher) − 1 = +1.83 %
  → eindeutig steigend, Schema-Mapping ``rising``.

Datenstand: TMO Q1 FY26 Vollanalyse-Score 2026-04-23 (Score-Datum) auf
Basis Pre-Briefing-Daten 2026-04-22 Close (yfinance ``end='2026-04-23'``
liefert deterministisch alle Bars bis einschließlich 2026-04-22 Close).

Idempotenz-Garantie: dry-run #1 und dry-run #2 produzieren byte-identische
Ausgaben. ``--apply`` #1 mutiert genau einen Record; ``--apply`` #2 ist
no-op (kein Diff, weil Felder bereits gesetzt). Empirisch belegt in
Step 0.5.4.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_PATH = REPO_ROOT / "05_Archiv" / "score_history.jsonl"
TARGET_RECORD_ID = "2026-04-23_TMO_vollanalyse"

BACKFILL_VALUES: dict[str, float | int | str] = {
    # FY23 GM 39.90% → FY25 GM 40.93%, (40.93−39.90)/2 = +0.515 pp/a
    # Quelle: yfinance income_stmt (Gross Profit / Total Revenue), siehe Module-Docstring
    "gm_trend_3j_pct_p_a": 0.5,

    # TMO 6M -9.38% vs SPY 6M +6.55% (anchor 2025-10-22 → 2026-04-22)
    # Quelle: yfinance history end='2026-04-23', auto_adjust=False
    "rel_strength_sp500_6m_pct": -16,
    "rel_staerke_sp500_6m_pct": -16,  # = rel_strength (v3.5-Rename-Alias-Spiegel)

    # Close $513.98 vs MA200 $525.17 am 2026-04-22
    "kurs_vs_200ma_pct": -2.13,

    # MA200 +1.83% über letzte ~21 Trading-Days → rising (Schema-Literal)
    "ma200_slope": "rising",
}


def _load_lines_with_endings() -> list[tuple[bytes, bytes]]:
    """Liest die Archiv-Datei zeilenweise als (json_bytes, line_ending_bytes).

    Preserviert original Line-Endings (CRLF / LF) pro Zeile, damit der Migration-
    Diff genau die mutierte Zeile betrifft und nicht unbeabsichtigt 27 weitere
    CRLF→LF-Konvertierungen produziert (Score-History ist überwiegend CRLF
    durch frühere Windows-Appends, Record #28 wurde 23.04. mit LF appendiert).
    """
    with ARCHIVE_PATH.open("rb") as fh:
        data = fh.read()
    # Split unter Erhalt der Endings
    out: list[tuple[bytes, bytes]] = []
    pos = 0
    while pos < len(data):
        nl = data.find(b"\n", pos)
        if nl == -1:
            # File endet ohne final newline (sollte nicht passieren, aber robust)
            out.append((data[pos:], b""))
            break
        line_end = nl + 1
        if nl > 0 and data[nl - 1:nl] == b"\r":
            json_part = data[pos:nl - 1]
            ending = b"\r\n"
        else:
            json_part = data[pos:nl]
            ending = b"\n"
        out.append((json_part, ending))
        pos = line_end
    return out


def _diff_for_record(record: dict) -> dict[str, tuple]:
    """Returns ``{field: (before, after)}`` mapping für Felder, die migriert werden."""
    if record.get("record_id") != TARGET_RECORD_ID:
        return {}
    metriken = record.get("metriken_roh", {})
    diffs: dict[str, tuple] = {}
    for field, new_value in BACKFILL_VALUES.items():
        old_value = metriken.get(field)
        if old_value is None and new_value is not None:
            diffs[field] = (old_value, new_value)
    return diffs


def _find_target(
    lines: list[tuple[bytes, bytes]],
) -> tuple[int, dict] | tuple[None, None]:
    """Finde Index + parsed dict des TARGET_RECORD_ID."""
    for idx, (json_bytes, _) in enumerate(lines):
        if not json_bytes.strip():
            continue
        record = json.loads(json_bytes.decode("utf-8"))
        if record.get("record_id") == TARGET_RECORD_ID:
            return idx, record
    return None, None


def _format_diff(diffs: dict[str, tuple]) -> str:
    if not diffs:
        return "(no-op — keine null-Felder gefunden, Migration bereits applied?)"
    lines = []
    for field, (before, after) in diffs.items():
        lines.append(f"  {field}: {before!r} -> {after!r}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Persist changes (default = dry-run).")
    args = parser.parse_args()

    # Guard: BACKFILL_VALUES darf keine unaufgelösten Ellipsis-Sentinels haben
    # (Codex-Round-3-LOW-Patch — verhindert versehentlichen Lauf mit Template-Stubs).
    unresolved = [k for k, v in BACKFILL_VALUES.items() if v is Ellipsis]
    if unresolved:
        print(
            f"ERROR: BACKFILL_VALUES hat unaufgeloeste Ellipsis-Sentinels in "
            f"{unresolved}. Step 0.5.3 (BACKFILL_VALUES mit echten Werten "
            f"fuellen) muss vor dry-run/apply erfolgen.",
            file=sys.stderr,
        )
        return 2

    lines = _load_lines_with_endings()
    target_idx, target = _find_target(lines)
    if target is None:
        print(f"ERROR: Record-ID '{TARGET_RECORD_ID}' nicht gefunden.", file=sys.stderr)
        return 2

    diffs = _diff_for_record(target)
    if not diffs:
        print(f"no-op: {TARGET_RECORD_ID} hat bereits alle Backfill-Felder gesetzt.")
        return 0

    print(f"Target: {TARGET_RECORD_ID} (line {target_idx + 1})")
    print(f"Diffs ({len(diffs)} fields):")
    print(_format_diff(diffs))

    if not args.apply:
        print("\n[DRY-RUN] Keine Persistierung. Fuehre mit --apply aus.")
        return 0

    # Apply: mutiere genau die Target-Zeile, alle anderen Zeilen byte-identisch
    for field, (_, new_value) in diffs.items():
        target.setdefault("metriken_roh", {})[field] = new_value
    new_json_bytes = json.dumps(target, ensure_ascii=False).encode("utf-8")
    original_ending = lines[target_idx][1]
    lines[target_idx] = (new_json_bytes, original_ending)

    # Atomic-rewrite, Line-Endings preserviert (rest der Datei byte-identisch)
    tmp_path = ARCHIVE_PATH.with_suffix(".jsonl.tmp")
    with tmp_path.open("wb") as fh:
        for json_bytes, ending in lines:
            fh.write(json_bytes)
            fh.write(ending)
    tmp_path.replace(ARCHIVE_PATH)

    print("\n[APPLIED] 1 record migrated, score_history.jsonl rewritten "
          "(original line-endings preserved).")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    sys.exit(main())

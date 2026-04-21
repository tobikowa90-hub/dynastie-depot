"""One-shot migration: snap defcon_level to current schema thresholds.

Auslöser 2026-04-21: Pre-Check vor Provenance-Gate-Plan deckte 12/27
Records in score_history.jsonl auf, die unter aktuellem Schema
(_check_defcon_level seit 18.04. mit SKILL-aligned Thresholds 80/65/50)
inkonsistent sind. Vorher (vor 18.04.) galten 70/60/50.

Idempotent: Re-Run = no-op. Atomare Datei-Operation via .tmp + os.replace.

Usage:
    python migrate_defcon_drift.py --dry-run    # zeige Diff, schreibe nicht
    python migrate_defcon_drift.py              # write changes
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
ARCHIVE = PROJECT_ROOT / "05_Archiv" / "score_history.jsonl"


def compute_defcon(score_gesamt: int) -> int:
    """SKILL-aligned thresholds (gültig seit 18.04.2026, fix in schemas.py:340)."""
    if score_gesamt >= 80:
        return 4
    if score_gesamt >= 65:
        return 3
    if score_gesamt >= 50:
        return 2
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not ARCHIVE.exists():
        print(f"ERROR: archive not found: {ARCHIVE}", file=sys.stderr)
        return 2

    drifted: list[tuple[int, str, int, int, int]] = []  # (line_no, record_id, score, old_defcon, new_defcon)
    out_lines: list[str] = []

    with ARCHIVE.open("r", encoding="utf-8") as fh:
        for line_no, raw in enumerate(fh, start=1):
            stripped = raw.rstrip("\n")
            if not stripped.strip():
                out_lines.append(stripped)
                continue
            obj = json.loads(stripped)
            score = obj["score_gesamt"]
            old_defcon = obj["defcon_level"]
            new_defcon = compute_defcon(score)
            if new_defcon != old_defcon:
                drifted.append((line_no, obj["record_id"], score, old_defcon, new_defcon))
                obj["defcon_level"] = new_defcon
                out_lines.append(json.dumps(obj, ensure_ascii=False))
            else:
                out_lines.append(stripped)

    print(f"Total records:    {len(out_lines)}")
    print(f"Drifted records:  {len(drifted)}")
    print()
    if drifted:
        print(f"{'Line':>5}  {'record_id':<42}  Score  Old→New")
        print("-" * 72)
        for line_no, rid, score, old, new in drifted:
            print(f"{line_no:>5}  {rid:<42}  {score:>5}  D{old}→D{new}")
        print()

    if args.dry_run:
        print("DRY-RUN — no changes written.")
        return 0

    if not drifted:
        print("Nothing to do.")
        return 0

    tmp = ARCHIVE.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8") as fh:
        fh.write("\n".join(out_lines) + "\n")
    os.replace(tmp, ARCHIVE)
    print(f"WROTE {len(drifted)} corrections atomically to {ARCHIVE.name}")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    sys.exit(main())

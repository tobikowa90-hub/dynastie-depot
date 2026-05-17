"""xlsx-smoke-test pre-commit-Hook (Spec §3.1).

Reproduziert das §18.7-Verhalten (`03_Tools/xlsx-smoke-test.md`) fail-close als
git-Gate. Dieser Hook ist **Executor, nicht SSoT** — die Soll-Werte
(Sheet-Namen, Conditional-Format-Counts, Voll-vs-Minimal-Scope) leben in
`03_Tools/xlsx-smoke-test.md`. Implementiert den Excel-Desktop-Fallback
Punkt A (Open) + B (Error-Scan) + E (CF-Count); F/C/D = manuell/UI-only,
nicht git-gate-fähig.

Read-only: lädt nur via openpyxl, schreibt nie (Memory
feedback_onedrive_edit_collision — Edit-Collision bei offenem Editor).

Aufruf: pre-commit übergibt die staged Pfade als argv (`language: system`).
Fail-close: EXIT 1 bei erstem Fail, Pfad+Profil+Grund auf stderr.
"""

from __future__ import annotations

import contextlib
import sys
from pathlib import Path

with contextlib.suppress(Exception):
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

import openpyxl
from openpyxl.utils.exceptions import InvalidFileException

# Error-Strings (xlsx-smoke-test.md Punkt B). Substring-Scan statt exact-match
# der md-Fallback-B: fängt sowohl reine '#REF!'-Werte als auch in Formeln
# eingebettete '=A1+#REF!' (data_only=False) → robustere Intent-Erfüllung.
# Bewusste Abweichung von der md-exact-match, zur Codex-Disposition (Spec §6).
_ERROR_TOKENS: tuple[str, ...] = ("#REF!", "#NAME?", "#VALUE!", "#N/A")

# Profil-Soll-Werte. SSoT = 03_Tools/xlsx-smoke-test.md (Scope-Tabelle).
# `cf_rule_count` ist gegen die Live-xlsx beim ersten pre-commit-Smoke zu
# verifizieren/justieren (Spec Akzeptanz-Kriterium 1) — Annahme explizit (§0.1).
_PROFILES: dict[str, dict] = {
    "Rebalancing_Tool": {
        "scope": "voll",
        "sheets": ("Portfolio & Rebalancing",),
        "cf_rule_count": 6,  # md: "218 Formeln + 6 Conditional Formats"
    },
    "Satelliten_Monitor": {
        "scope": "voll",
        "sheets": ("Satelliten Monitor",),
        "cf_rule_count": 5,  # md: "12 Formeln + 5 Conditional Formats + Σ-Check"
    },
    "Watchlist_Ersatzbank_Monitor": {
        "scope": "minimal",  # md Minimal-Check-Annex: nur A1 + Existenz
        "sheets": (),
        "cf_rule_count": 0,
    },
}


def _fail(path: Path, profil: str, grund: str) -> int:
    print(
        f"❌ xlsx-smoke-test: FAIL [{path.name} | profil={profil}] {grund}",
        file=sys.stderr,
    )
    return 1


def _resolve_profil(path: Path) -> tuple[str, dict] | None:
    for key, prof in _PROFILES.items():
        if path.name.startswith(key):
            return key, prof
    return None


def _count_cf_rules(wb: openpyxl.Workbook) -> int:
    total = 0
    for ws in wb.worksheets:
        total += sum(1 for _ in ws.conditional_formatting)
    return total


def validate_file(path: Path) -> int:
    resolved = _resolve_profil(path)
    if resolved is None:
        return _fail(
            path,
            "UNKNOWN",
            "kein bekanntes Profil (Spec-Scope = Rebalancing_Tool / "
            "Satelliten_Monitor / Watchlist_Ersatzbank_Monitor) — fail-close",
        )
    profil, prof = resolved

    # Punkt A: Open-Repair (Exception/Load-Fail = strukturelle Korruption).
    try:
        wb = openpyxl.load_workbook(path, data_only=False)
    except (InvalidFileException, KeyError, OSError, ValueError) as e:
        return _fail(path, profil, f"openpyxl load failed (Punkt A): {e}")

    try:
        first_ws = wb.worksheets[0]
        if first_ws["A1"].value in (None, ""):
            return _fail(path, profil, "A1 leer — Sheet-Existenz-Check (Punkt A)")

        for sheet in prof["sheets"]:
            if sheet not in wb.sheetnames:
                return _fail(path, profil, f"erwartetes Sheet '{sheet}' fehlt")

        if prof["scope"] == "minimal":
            return 0  # Watchlist: nur A1 + Existenz (0 Formeln/CF)

        # Punkt B: Error-Token-Scan über alle Zellen aller Sheets.
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for cell in row:
                    val = cell.value
                    if isinstance(val, str) and any(t in val for t in _ERROR_TOKENS):
                        return _fail(
                            path,
                            profil,
                            f"Formel-/Wert-Fehler in {ws.title}!{cell.coordinate}: "
                            f"{val!r} (Punkt B)",
                        )

        # Punkt E: Conditional-Format-Regel-Count.
        cf_count = _count_cf_rules(wb)
        if cf_count != prof["cf_rule_count"]:
            return _fail(
                path,
                profil,
                f"Conditional-Format-Count {cf_count} != erwartet "
                f"{prof['cf_rule_count']} — CF von openpyxl-Write zerstört? "
                f"(Punkt E; Soll-SSoT = xlsx-smoke-test.md)",
            )
        return 0
    finally:
        wb.close()


def main(argv: list[str] | None = None) -> int:
    paths = list(sys.argv[1:]) if argv is None else argv
    for p in paths:
        path = Path(p)
        if not path.is_file():
            continue
        rc = validate_file(path)
        if rc != 0:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())

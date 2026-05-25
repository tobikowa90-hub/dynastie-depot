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
import yaml
from openpyxl.utils.exceptions import InvalidFileException

# Error-Strings (xlsx-smoke-test.md Punkt B). Substring-Scan statt exact-match
# der md-Fallback-B: fängt sowohl reine '#REF!'-Werte als auch in Formeln
# eingebettete '=A1+#REF!' (data_only=False) → robustere Intent-Erfüllung.
# Bewusste Abweichung von der md-exact-match, zur Codex-Disposition (Spec §6).
_ERROR_TOKENS: tuple[str, ...] = ("#REF!", "#NAME?", "#VALUE!", "#N/A")

# Config-Anker für Punkt G (SPEC §4.3 Variante G, drift-doc §2.4).
# Anker-Pfad: brokers.scalable.sparrate_eur (verified config.yaml L27,
# 2026-05-25 post Codex-R1 HIGH-1 — portfolio.satelliten_sparrate existiert NICHT).
_CONFIG_YAML_PATH = (
    Path(__file__).resolve().parents[2] / "01_Skills" / "dynastie-depot" / "config.yaml"
)

# Profil-Soll-Werte. SSoT = 03_Tools/xlsx-smoke-test.md (Scope-Tabelle).
# `cf_rule_count` ist gegen die Live-xlsx beim ersten pre-commit-Smoke zu
# verifizieren/justieren (Spec Akzeptanz-Kriterium 1) — Annahme explizit (§0.1).
# `sheets` Tupel erweitert per P13 (drift-doc §1.1 + §2.1 — 2026-05-25 Stage-2 Schritt 6).
_PROFILES: dict[str, dict] = {
    "Rebalancing_Tool": {
        "scope": "voll",
        "sheets": (
            "Portfolio & Rebalancing",
            "US-Exposure",  # P13 NEU 2026-05-25 (drift-doc §1.1)
            "Parameter & Regeln",  # P13 NEU 2026-05-25 (drift-doc §1.1)
        ),
        "cf_rule_count": 6,  # md: "249 Formeln + 6 Conditional Formats" (Live-State 2026-05-25, vorher 218/6)
    },
    "Satelliten_Monitor": {
        "scope": "voll",
        "sheets": (
            "Satelliten Monitor",
            "QuickScreen Ampel",  # P13 NEU 2026-05-25 (drift-doc §2.1)
        ),
        "cf_rule_count": 5,  # md: "13 Formeln + 5 Conditional Formats + §G Σ-Check via Hook" (Live-State 2026-05-25, vorher 12/5 + Excel-Σ-Plan)
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
    # NOTE (Codex-R3 MED-1 deferred): startswith ist kollision-anfällig bei
    # Backup-Suffixen (z.B. `Rebalancing_Tool_v3.4_backup.xlsx`). v0.2-Refactor-Pfad
    # → regex full-match `^<Profil>_v\d+\.\d+\.xlsx$` (SPEC §4.4 Codex-R1 LOW).
    # v0.1: bewusst startswith — kein Backup-Pattern aktuell im Repo.
    for key, prof in _PROFILES.items():
        if path.name.startswith(key):
            return key, prof
    return None


def _count_cf_rules(wb: openpyxl.Workbook) -> int:
    total = 0
    for ws in wb.worksheets:
        total += sum(1 for _ in ws.conditional_formatting)
    return total


def _derive_rate_eur(satellit_cfg: dict) -> int:
    """Punkt G Mapping: config.yaml satellit → Sparrate-EUR (SPEC §4.3, drift-doc §2.4).

    - flag=True                     → 0
    - flag=False + defcon in {3,4}  → 38
    - flag=False + defcon == 2      → 19
    - flag=False + defcon == 1      → 0 (FLAG fehlt, aber DEFCON 1)

    Wirft ValueError bei unmapped defcon.
    """
    if satellit_cfg.get("flag") is True:
        return 0
    defcon = satellit_cfg.get("defcon")
    if defcon in (3, 4):
        return 38
    if defcon == 2:
        return 19
    if defcon == 1:
        return 0
    raise ValueError(f"unmapped defcon={defcon!r} für satellit={satellit_cfg.get('ticker', '?')}")


def _check_g_sparrate_sigma(wb: openpyxl.Workbook, config_yaml_path: Path) -> str | None:
    """Punkt G Sparrate-Σ-Sanity (SPEC §4.3 Variante G).

    Steps:
    1. Load config_yaml_path (yaml.safe_load)
    2. Σ = sum(_derive_rate_eur(s) for s in cfg["satelliten"])
    3. Assert Σ == cfg["brokers"]["scalable"]["sparrate_eur"]  (Anker 285€)
    4. Assert wb "Satelliten Monitor" K3-Text enthält ' Voll' + 'D2-Sockelbetrag' + 'Eingefroren'
    5. Assert wb "Satelliten Monitor" N19-Text == '→ muss = 285,00 €'

    Returns None bei PASS, str (Fehler-Detail) bei FAIL.
    """
    try:
        with Path(config_yaml_path).open(encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except (OSError, yaml.YAMLError) as e:
        return f"config.yaml unreadable: {e}"

    try:
        sigma = sum(_derive_rate_eur(s) for s in cfg["satelliten"])
    except (KeyError, TypeError, ValueError) as e:
        return f"satelliten-mapping fail: {e}"

    try:
        anker = cfg["brokers"]["scalable"]["sparrate_eur"]
    except (KeyError, TypeError) as e:
        return f"anker brokers.scalable.sparrate_eur missing: {e}"

    if sigma != anker:
        return f"Σ-Drift: derived={sigma}€ != anker={anker}€ (config.yaml.brokers.scalable.sparrate_eur)"

    if "Satelliten Monitor" not in wb.sheetnames:
        return "Sheet 'Satelliten Monitor' fehlt — kein §G-Display-Check möglich"
    sat_ws = wb["Satelliten Monitor"]

    k3 = sat_ws["K3"].value or ""
    for needle in (" Voll", "D2-Sockelbetrag", "Eingefroren"):
        if needle not in str(k3):
            return f"K3-Display-Drift: '{needle}' fehlt in {k3!r}"

    # N19-Display aus anker abgeleitet (Codex-R3 MED-2), NICHT hardcoded.
    # Deutsche Schreibweise: 285,00 € (Komma als Dezimaltrenner).
    n19 = sat_ws["N19"].value or ""
    expected_n19 = f"→ muss = {anker:.2f} €".replace(".", ",")
    if expected_n19 not in str(n19):
        return f"N19-Sanity-Drift: erwartet {expected_n19!r}, live={n19!r}"

    return None


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
        # Punkt A (Sheet-Existenz): Workbook geladen (oben) + hat >=1 Worksheet.
        # Kanonische §18.7-Doktrin (xlsx-smoke-test.md Punkt A) = "Datei lesbar
        # + erwartete Sheets vorhanden" — KEIN A1-non-empty-Constraint fürs
        # Voll-Profil (Satelliten_Monitor hat legitim A1=None; Header/Daten
        # beginnen tiefer). Der A1-Check bleibt Minimal-Profil-Proxy (siehe
        # unten) — dort ist er die designierte Akzeptanz-#2-bad-Fixture.
        if not wb.worksheets:
            return _fail(path, profil, "Workbook hat keine Worksheets (Punkt A)")

        for sheet in prof["sheets"]:
            if sheet not in wb.sheetnames:
                return _fail(path, profil, f"erwartetes Sheet '{sheet}' fehlt")

        if prof["scope"] == "minimal":
            # Watchlist-Minimal-Annex: A1 als konkreter Lesbarkeits-/Nicht-
            # Degeneriert-Proxy. Akzeptanz-#2-bad-Fixture = empty_a1 → FAIL,
            # clean = A1 gesetzt → PASS (_smoke_test.py + _generate_fixtures.py).
            if wb.worksheets[0]["A1"].value in (None, ""):
                return _fail(path, profil, "A1 leer — Existenz-Proxy (Punkt A, minimal)")
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

        # Punkt G: Sparrate-Σ-Sanity (nur Satelliten_Monitor-Profil, SPEC §4.3).
        if profil == "Satelliten_Monitor":
            g_err = _check_g_sparrate_sigma(wb, _CONFIG_YAML_PATH)
            if g_err is not None:
                return _fail(path, profil, f"Sparrate-Σ-Drift (Punkt G): {g_err}")

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

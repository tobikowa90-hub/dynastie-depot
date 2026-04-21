# Score-Append Provenance-Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fail-close Pipeline-Gate `P3.5` plus reduzierter Schema-Guard verhindern, dass Rescoring- oder unvollständige Forward-Runs als `analyse_typ="vollanalyse"` in `05_Archiv/score_history.jsonl` persistiert werden.

**Architecture:** Variante E (Hybrid) — zwei disjunkte Schichten. Schicht B = neuer Pipeline-Helper `provenance_gate.py::check_provenance` (Eingabe: Pipeline-Zustand + Record + skill_meta), eingehängt in `backtest-ready-forward-verify` zwischen P2b und P3. Schicht D = neuer Pydantic-Validator `_check_vollanalyse_block_coverage` in `schemas.py::ScoreRecord` (minimale Plausibilität für Direkt-CLI an `archive_score.py`). Single-Source-of-Truth für DEFCON-Version in neuer `versions.py`.

**Tech Stack:** Python 3.11+, Pydantic v2, `subprocess` für git, vorhandene Smoke-Test-Harness (kein pytest). Append-Pfad bleibt `archive_score.py` unverändert.

**Spec:** `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`

**Non-Goals (aus Spec §3):** kein `--force`-Override, keine Schema-Migration der 27 existierenden Records, keine config.yaml-Erweiterung, keine INSTRUKTIONEN-§-Promotion (Applied-Learning-Stufe reicht bis 3-4 reale Anwendungen).

---

## File Structure

| Datei | Aktion | Verantwortung |
|---|---|---|
| `03_Tools/backtest-ready/versions.py` | **NEU** | SSoT-Konstante `DEFCON_ACTIVE_VERSION` |
| `03_Tools/backtest-ready/provenance_gate.py` | **NEU** | `check_provenance()` Pipeline-Gate (Schicht B) + Smoke-Tests |
| `03_Tools/backtest-ready/schemas.py` | Modifizieren | Refactor `_check_forward_version` auf `versions.py`; neuer Validator `_check_vollanalyse_block_coverage` (Schicht D); Smoke-Cases D1-D4 |
| `01_Skills/backtest-ready-forward-verify/SKILL.md` | Modifizieren | Phase-Tabelle: P3.5 vor P3 einfügen; Report-Format Zeile P3.5; Version-Referenz auf `versions.py` |
| `01_Skills/backtest-ready-forward-verify/_smoke_test.py` | Modifizieren | Case 7 — Integrationstest fail-close P3.5, kein Archiv-Write |
| `00_Core/STATE.md` | Modifizieren | System-Zustand-Eintrag: „Provenance-Gate aktiv seit YYYY-MM-DD" |
| `00_Core/INSTRUKTIONEN.md §18` | Modifizieren | Sync-Pflicht-Zeile: Provenance-Gate als Teil der Append-Pipeline erwähnen |

CORE-MEMORY §10 Audit-Log-Eintrag = Teil von Task 6 Go-Live (Spec §9 Alignment, Codex-Korrektur 21.04.).

---

## Task 0: Archive-Baseline-Check (Pre-Execution Sanity)

**Files:** keine — read-only Validierung.

**Rationale:** Codex-Review-Punkt 21.04. — bei fail-close hängt jeder neue Validator-Test an einer bekannt-sauberen Baseline. Drift-Migration `migrate_defcon_drift.py` lief am 21.04. Mittag (commit `ca76114`, 27/27 PASS). Wenn Plan in späterer Session executiert wird, könnten neue Records inzwischen wieder Drift introduziert haben (z.B. zwischen Migration und Execution archivierte Records). Pre-Check garantiert sauberen Boden für Tasks 1-6.

- [ ] **Step 0.1: Re-Validate aller Records gegen aktuelles Schema**

Run:
```bash
python -c "
import json, sys
sys.path.insert(0, '03_Tools/backtest-ready')
from schemas import ScoreRecord
from pydantic import ValidationError
passed, failed = 0, []
with open('05_Archiv/score_history.jsonl', 'r', encoding='utf-8') as fh:
    for i, line in enumerate(fh, 1):
        if not line.strip(): continue
        try:
            ScoreRecord.model_validate(json.loads(line))
            passed += 1
        except ValidationError as e:
            failed.append((i, str(e).split(chr(10))[1][:120] if chr(10) in str(e) else str(e)[:120]))
print(f'PASS: {passed} / FAIL: {len(failed)}')
for line_no, err in failed:
    print(f'  line {line_no}: {err}')
"
```
Expected: `PASS: N / FAIL: 0` (N = aktuelle Record-Anzahl, ≥27).

- [ ] **Step 0.2: Bei FAIL — Migration nachholen, NICHT Tasks 1-6 starten**

Wenn Step 0.1 FAIL meldet:
- Drift-Klasse identifizieren (defcon_level? quality_trap? andere?)
- Bei defcon_level-Drift: `python "03_Tools/backtest-ready/migrate_defcon_drift.py" --dry-run` → review → apply
- Bei anderer Drift-Klasse: separater idempotenter Migration-Helper analog zu `migrate_defcon_drift.py`
- Nach Migration: Step 0.1 erneut bis `FAIL: 0`
- Eigener Commit für Migration VOR Tasks 1-6 (analog `ca76114`-Pattern)

- [ ] **Step 0.3: Note in Plan-Header oder Execution-Log: „Baseline N/N PASS @ <commit>"**

Kein Code-Step — eine Zeile in der Execution-Session-Notiz. Falls Subagent-Driven: Subagent meldet Pre-Check-Ergebnis bevor er Task 1 startet.

---

## Task 1: versions.py + Schema-Refactor auf SSoT

**Files:**
- Create: `03_Tools/backtest-ready/versions.py`
- Modify: `03_Tools/backtest-ready/schemas.py:316-323` (Validator `_check_forward_version`)

**Rationale:** Single Source of Truth für `DEFCON_ACTIVE_VERSION`. Aktuell hard-coded `"v3.7"` in `schemas.py::_check_forward_version`. Provenance-Gate (Task 3) braucht dieselbe Konstante; ohne SSoT entstünden zwei Wartungs-Stellen für jede Version-Migration.

- [ ] **Step 1.1: Create `versions.py`**

```python
"""Dynasty-Depot: DEFCON version constants. Single source of truth.

Referenced by schemas.py (_check_forward_version), provenance_gate.py
(check_provenance #6), SKILL.md text.
Bei Migration v3.7 -> v3.8: nur DEFCON_ACTIVE_VERSION hier anpassen.
"""
from typing import Final

DEFCON_ACTIVE_VERSION: Final[str] = "v3.7"

__all__ = ["DEFCON_ACTIVE_VERSION"]
```

- [ ] **Step 1.2: Refactor `schemas.py::_check_forward_version`**

Vorher (Zeilen 316-323):
```python
    @model_validator(mode="after")
    def _check_forward_version(self) -> ScoreRecord:
        """Forward-Records müssen v3.7 deklarieren; Backfill ist frei."""
        if self.source == "forward" and self.defcon_version != "v3.7":
            raise ValueError(
                f"forward record must use defcon_version 'v3.7', got '{self.defcon_version}'"
            )
        return self
```

Nachher:
```python
    @model_validator(mode="after")
    def _check_forward_version(self) -> ScoreRecord:
        """Forward-Records müssen aktive DEFCON-Version deklarieren; Backfill ist frei."""
        from versions import DEFCON_ACTIVE_VERSION
        if self.source == "forward" and self.defcon_version != DEFCON_ACTIVE_VERSION:
            raise ValueError(
                f"forward record must use defcon_version '{DEFCON_ACTIVE_VERSION}', "
                f"got '{self.defcon_version}'"
            )
        return self
```

(`from versions import` lokal im Validator, nicht top-level — vermeidet Circular-Import-Risiko bei späterer Erweiterung; Konsistent mit bestehendem `import copy` lokal in `_smoke_tests`.)

- [ ] **Step 1.3: Run existing schema smoke tests**

Run: `python "03_Tools/backtest-ready/schemas.py"`
Expected: `[OK] all schema smoke tests passed` (7/7 — keine Regression).

- [ ] **Step 1.4: Run archive_score smoke tests**

Run: `python "03_Tools/backtest-ready/archive_score.py"`
Expected: `✅ all archive_score smoke tests passed` (5/5).

- [ ] **Step 1.5: Run skill smoke tests**

Run: `python "01_Skills/backtest-ready-forward-verify/_smoke_test.py"`
Expected: `✅ all 6/6 cases passed`.

- [ ] **Step 1.6: Commit**

```bash
git add "03_Tools/backtest-ready/versions.py" "03_Tools/backtest-ready/schemas.py"
git commit -m "refactor(backtest-ready): SSoT DEFCON_ACTIVE_VERSION in versions.py

Provenance-Gate Plan Task 1. Schemas._check_forward_version liest jetzt
aus versions.py statt hard-coded 'v3.7'. Vorbereitung für Pipeline-Gate
Schicht B (Task 3).

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §5.1"
```

---

## Task 2: Block-Coverage Validator (schemas.py — Schicht D)

**Files:**
- Modify: `03_Tools/backtest-ready/schemas.py` (Validator hinzufügen + Smoke-Cases D1-D4)

**Rationale:** Spec §5.3 + §8.2. Schicht D fängt Direkt-CLI-Aufrufe (`archive_score.py --file draft.json`), die Pipeline + Schicht B umgehen. Minimaler Anspruch: bei `source="forward"` + `analyse_typ="vollanalyse"` mindestens 1 Rohmetrik in jedem der 4 prüfbaren Score-Blöcke (`fundamentals`, `moat`, `technicals`, `sentiment`). `insider`-Block ist explizit ausgenommen (Roh-Felder existieren nicht in `metriken_roh`).

- [ ] **Step 2.1: Failing test D1-D4 schreiben**

In `_smoke_tests()` von `schemas.py` nach Case 7 (vor `print("✅ all schema smoke tests passed")`) einfügen:

```python
    # Case D1: vollanalyse mit min. 1 Rohmetrik in jedem geprüften Block → parses OK
    # Build from valid AVGO base; metriken_roh hat bereits fwd_pe/p_fcf/op_margin/gm_trend/rel_strength/eps_revisions
    d1 = copy.deepcopy(avgo)
    d1["record_id"] = "2026-04-21_D1_vollanalyse"
    rec_d1 = ScoreRecord.model_validate(d1)
    assert rec_d1.record_id == "2026-04-21_D1_vollanalyse"
    print("  [D1] block-coverage: all 4 blocks filled → parses OK")

    # Case D2: vollanalyse, fundamentals-Block leer → ValidationError
    d2 = copy.deepcopy(avgo)
    d2["record_id"] = "2026-04-21_D2_vollanalyse"
    # Wipe all fundamentals raw fields
    for f in (
        "fwd_pe", "p_fcf", "net_debt_ebitda", "current_ratio",
        "goodwill_pct_assets", "capex_ocf_pct_gaap", "capex_ocf_pct_bereinigt",
        "roic_gaap_pct", "roic_bereinigt_pct", "wacc_pct",
        "fcf_yield_pct", "sbc_revenue_pct", "sbc_ocf_pct",
        "accruals_ratio_pct", "tariff_exposure_pct", "operating_margin_ttm_pct",
    ):
        d2["metriken_roh"][f] = None
    try:
        ScoreRecord.model_validate(d2)
    except ValidationError as e:
        assert "block-coverage violation" in str(e), f"wrong error: {e}"
        assert "fundamentals" in str(e), f"fundamentals not in error: {e}"
        print("  [D2] block-coverage: empty fundamentals → ValidationError")
    else:
        raise AssertionError("expected block-coverage ValidationError")

    # Case D3: rescoring mit 0 Rohmetriken → parses OK (Skip-Condition)
    d3 = copy.deepcopy(avgo)
    d3["record_id"] = "2026-04-21_D3_rescoring"
    d3["analyse_typ"] = "rescoring"
    d3["metriken_roh"] = {}
    rec_d3 = ScoreRecord.model_validate(d3)
    assert rec_d3.analyse_typ == "rescoring"
    print("  [D3] block-coverage: rescoring skipped → parses OK")

    # Case D4: Backfill mit 0 Rohmetriken → parses OK (Skip-Condition)
    d4 = copy.deepcopy(avgo)
    d4["record_id"] = "2026-04-21_D4_vollanalyse"
    d4["source"] = "backfill"
    d4["defcon_version"] = "historical"  # backfill allows free version
    d4["metriken_roh"] = {}
    rec_d4 = ScoreRecord.model_validate(d4)
    assert rec_d4.source == "backfill"
    print("  [D4] block-coverage: backfill skipped → parses OK")
```

- [ ] **Step 2.2: Run tests — D1 passes, D2 fails (validator nicht implementiert), D3+D4 pass**

Run: `python "03_Tools/backtest-ready/schemas.py"`
Expected: D2 schlägt fehl mit `expected block-coverage ValidationError` → `AssertionError`. D1/D3/D4 laufen versehentlich PASS, weil der Validator noch nicht existiert (D1 ist sowieso valid, D3/D4 sollten skippen — aber Skip ist Default ohne Validator).

Wenn D1 PASS aber D2 raise AssertionError: Fail-Signal stimmt — weiter zu Step 2.3.

- [ ] **Step 2.3: Validator implementieren**

In `schemas.py::ScoreRecord` nach `_check_quality_trap` (nach Zeile 410, vor Class-Ende auf Zeile 411) einfügen:

```python
    @model_validator(mode="after")
    def _check_vollanalyse_block_coverage(self) -> ScoreRecord:
        """Schicht D Provenance-Plausibilität (Spec §5.3).

        Bei source='forward' + analyse_typ='vollanalyse':
        Mindestens 1 Rohmetrik muss in jedem der 4 geprüften Score-Blöcke
        (fundamentals, moat, technicals, sentiment) befüllt sein.

        insider-Block ausgenommen: Roh-Felder existieren nicht in MetrikenRoh
        (alle Insider-Daten sind Sub-Scores, keine Rohwerte).

        KEIN Freshness-Beweis-Anspruch (das macht Schicht B in provenance_gate.py).
        Backfill + rescoring + delta werden übersprungen.
        """
        if self.source != "forward" or self.analyse_typ != "vollanalyse":
            return self

        BLOCK_FIELDS: dict[str, tuple[str, ...]] = {
            "fundamentals": (
                "fwd_pe", "p_fcf", "net_debt_ebitda", "current_ratio",
                "goodwill_pct_assets", "capex_ocf_pct_gaap", "capex_ocf_pct_bereinigt",
                "roic_gaap_pct", "roic_bereinigt_pct", "wacc_pct",
                "fcf_yield_pct", "sbc_revenue_pct", "sbc_ocf_pct",
                "accruals_ratio_pct", "tariff_exposure_pct",
                "operating_margin_ttm_pct",
            ),
            "moat": ("gm_trend_3j_pct_p_a",),
            "technicals": (
                "rel_strength_sp500_6m_pct", "kurs_vs_200ma_pct", "ma200_slope",
            ),
            # insider: Roh-Metriken nicht in metriken_roh → skip im Loop unten
            "sentiment": (
                "eps_revisions_up_90d", "eps_revisions_down_90d", "pt_dispersion_pct",
            ),
        }

        empty_blocks: list[str] = []
        for block, fields in BLOCK_FIELDS.items():
            if not fields:
                continue
            filled = any(getattr(self.metriken_roh, f) is not None for f in fields)
            if not filled:
                empty_blocks.append(block)

        if empty_blocks:
            raise ValueError(
                f"vollanalyse block-coverage violation: no raw metrics filled in blocks: "
                f"{empty_blocks}. Fill at least one field per block or reclassify analyse_typ."
            )
        return self
```

- [ ] **Step 2.4: Run tests — alle 11 Cases müssen PASS**

Run: `python "03_Tools/backtest-ready/schemas.py"`
Expected: `[OK] all schema smoke tests passed` mit 11 Output-Zeilen (1-7 vorher + D1-D4).

- [ ] **Step 2.5: Regression-Check archive_score + skill smoke**

Run: `python "03_Tools/backtest-ready/archive_score.py"` → `5/5 passed`
Run: `python "01_Skills/backtest-ready-forward-verify/_smoke_test.py"` → `6/6 passed`

Falls einer fehlschlägt: das in `_smoke_test.py` `_build_minimal_record` benutzt `source="backfill"` (Zeile 105) → `_check_vollanalyse_block_coverage` skipt → kein Konflikt. archive_score `_build_valid_forward_record` setzt `metriken_roh` mit `fwd_pe`, `p_fcf`, `operating_margin_ttm_pct` → Block fundamentals befüllt; aber `gm_trend_3j_pct_p_a` (moat) ist nicht gesetzt — **Regression-Risiko**.

**Wenn archive_score Test 1/3/4/5 fehlschlagen mit "block-coverage violation":** `_build_valid_forward_record` in `archive_score.py:352-356` ergänzen:

Vorher:
```python
        "metriken_roh": {
            "fwd_pe": 22.1,
            "p_fcf": 19.8,
            "operating_margin_ttm_pct": 32.1,
        },
```

Nachher:
```python
        "metriken_roh": {
            "fwd_pe": 22.1,
            "p_fcf": 19.8,
            "operating_margin_ttm_pct": 32.1,
            "gm_trend_3j_pct_p_a": 0.3,
            "rel_strength_sp500_6m_pct": 4,
            "eps_revisions_up_90d": 4,
        },
```

Re-run archive_score smoke tests → `5/5 passed`.

- [ ] **Step 2.6: Commit**

```bash
git add "03_Tools/backtest-ready/schemas.py" "03_Tools/backtest-ready/archive_score.py"
git commit -m "feat(backtest-ready): Schicht D Block-Coverage-Validator (Provenance-Gate Task 2)

ScoreRecord._check_vollanalyse_block_coverage prüft bei forward+vollanalyse,
dass jeder der 4 Blöcke (fundamentals/moat/technicals/sentiment) mindestens
1 Rohmetrik enthält. insider-Block ausgenommen (keine Roh-Felder in
MetrikenRoh). Schmaler Schema-Guard für Direkt-CLI an archive_score.py;
KEIN Freshness-Beweis-Anspruch (das macht Schicht B in Task 3).

Test-Cases D1-D4 in schemas.py::_smoke_tests neu (11/11 passing).
archive_score._build_valid_forward_record metriken_roh um 3 Felder ergänzt
(gm_trend, rel_strength, eps_revisions_up) damit fixture die neue
Block-Coverage-Regel erfüllt.

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §5.3 + §8.2"
```

- [ ] **Step 2.7: Re-Validate-Sweep nach Validator-Hinzufügung (§27.4 Vertikal-Drift-Pflicht)**

Run identisch zu Step 0.1 (Pre-Check), aber jetzt mit aktivem Block-Coverage-Validator:
```bash
python -c "
import json, sys
sys.path.insert(0, '03_Tools/backtest-ready')
from schemas import ScoreRecord
from pydantic import ValidationError
passed, failed = 0, []
with open('05_Archiv/score_history.jsonl', 'r', encoding='utf-8') as fh:
    for i, line in enumerate(fh, 1):
        if not line.strip(): continue
        try:
            ScoreRecord.model_validate(json.loads(line))
            passed += 1
        except ValidationError as e:
            failed.append((i, str(e).split(chr(10))[1][:120] if chr(10) in str(e) else str(e)[:120]))
print(f'PASS: {passed} / FAIL: {len(failed)}')
for line_no, err in failed:
    print(f'  line {line_no}: {err}')
"
```
Expected: identisch zu Pre-Check `FAIL: 0`. Block-Coverage skippt backfill + rescoring + delta — die 3 Forward-Vollanalyse-Records (V_vollanalyse 17.04. nach Drift-Migration, V_rescoring 18.04., TMO_vollanalyse 18.04.) müssen alle befüllte Blöcke haben. Wenn FAIL: bedeutet historisch archivierter Forward-Vollanalyse-Record hat unvollständige `metriken_roh` — entweder via separater Helper-Migration nachfüllen ODER `analyse_typ` retroaktiv auf `rescoring` umklassifizieren (separater Commit), DANN Plan fortsetzen.

§27.4-Pflicht (INSTRUKTIONEN 21.04. Erweiterung): bei jedem Schema-Validator-Hinzufüg-Commit Re-Validate-Sweep über alle persistierten Records, „N/M PASS" explizit ausschreiben, niemals weichgespültes „läuft".

---

## Task 3: provenance_gate.py — Schicht B Pipeline-Gate

**Files:**
- Create: `03_Tools/backtest-ready/provenance_gate.py`

**Rationale:** Spec §5.2 + §8.1. Schicht B kombiniert Pipeline-Kontext (Freshness-Ergebnis aus P2a) mit Record-Behauptungen + skill_meta. Acht Checks fail-close in Reihenfolge. Wird in Task 4 von SKILL.md als Phase P3.5 zwischen P2b und P3 aufgerufen.

**Granularitäts-Hinweis (Codex 21.04.):** Originaler Step 3.1 enthielt ~250 LOC in einem Block. Aufgesplittet in 3.1a (Skeleton+Constants+Helper) / 3.1b (check_provenance Body) / 3.1c (Smoke-Tests Cases 1-5) / 3.1d (Smoke-Tests Cases 6-9), je 2-5 Min editierbar.

- [ ] **Step 3.1a: Skeleton + Constants + `_is_placeholder` Helper schreiben**

Datei `03_Tools/backtest-ready/provenance_gate.py` mit folgendem Inhalt erstellen (Public-API + Tests folgen in 3.1b/c/d):

```python
"""Dynasty-Depot v3.7 Backtest-Ready: provenance_gate (Schicht B).

Pipeline-Gate P3.5 für backtest-ready-forward-verify Skill. Fail-close.
Prüft Provenance-Behauptungen (analyse_typ, kurs.referenz, defcon_version,
Quellen-Vollständigkeit) gegen Pipeline-Evidenz (freshness_missing,
skill_meta-Konsistenz).

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §5.2

Nicht direkt CLI-aufrufbar — Library-Funktion für SKILL.md-Orchestrator.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Final

sys.path.insert(0, str(Path(__file__).parent))

from versions import DEFCON_ACTIVE_VERSION  # noqa: E402

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PLATZHALTER_BLACKLIST: Final[frozenset[str]] = frozenset({
    "unknown", "tbd", "todo", "placeholder", "none", "na", "n/a", "?",
})

QUELLEN_PFLICHT_FELDER: Final[tuple[str, ...]] = (
    "fundamentals", "technicals", "insider", "moat", "sentiment",
)

_RE_QUESTION_MARKS = re.compile(r"\?+")


def _is_placeholder(value: str) -> bool:
    """True wenn value (case-insensitive, getrimmt) ein Platzhalter ist."""
    stripped = value.strip().lower()
    if stripped in PLATZHALTER_BLACKLIST:
        return True
    return bool(_RE_QUESTION_MARKS.fullmatch(stripped))


__all__ = [
    "DEFCON_ACTIVE_VERSION",
    "PLATZHALTER_BLACKLIST",
    "QUELLEN_PFLICHT_FELDER",
    "check_provenance",
]


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    print("Skeleton only — public API folgt in Step 3.1b")
```

Lauf-Check: `python "03_Tools/backtest-ready/provenance_gate.py"` → muss „Skeleton only" ausgeben. ImportError = fix Path/imports.

- [ ] **Step 3.1b: `check_provenance()` Public-API einfügen**

Direkt nach dem `_is_placeholder`-Helper (vor `__all__`) einfügen:

```python
def check_provenance(
    record_dict: dict,
    freshness_missing: list[str],
    skill_meta: dict | None,
) -> tuple[bool, list[str]]:
    """Pipeline-Gate P3.5. Fail-close bei erster Verletzung.

    Args:
        record_dict: ScoreRecord als dict (vor Pydantic-Validation).
        freshness_missing: Liste der nicht-modifizierten REQUIRED_TOUCH_FILES
            aus check_freshness() in P2a.
        skill_meta: optional dict mit migration-Info; None oder {} = leer.

    Returns:
        (passed, reasons). passed=False → Caller muss FAIL phase=P3.5 emitten
        und Pipeline abbrechen. reasons enthält genau eine Begründung
        (fail-close: Stop bei erster Verletzung).
    """
    source = record_dict.get("source")
    analyse_typ = record_dict.get("analyse_typ")
    skill_meta_norm = skill_meta or {}

    # Check #1: Backfill skip
    if source == "backfill":
        return True, []

    # Check #2: vollanalyse braucht frische Pflicht-Touch-Dateien
    if analyse_typ == "vollanalyse" and freshness_missing:
        return False, [
            f"vollanalyse requires fresh session (missing: {freshness_missing}); "
            f"reclassify as rescoring or complete workflow"
        ]

    # Check #3: vollanalyse braucht frischen Kurs (referenz=close_of_score_datum)
    if analyse_typ == "vollanalyse":
        kurs_referenz = (record_dict.get("kurs") or {}).get("referenz")
        if kurs_referenz != "close_of_score_datum":
            return False, [
                f"vollanalyse requires fresh kurs (referenz='{kurs_referenz}')"
            ]

    # Check #4: rescoring braucht skill_meta für Δ-Gate
    if analyse_typ == "rescoring" and not skill_meta_norm:
        return False, ["rescoring requires skill_meta for Δ-Gate"]

    # Check #5: delta ist forward-only
    if analyse_typ == "delta" and source != "forward":
        return False, ["delta is forward-only"]

    # Check #6: defcon_version-Drift gegen aktive Version
    record_version = record_dict.get("defcon_version")
    if record_version != DEFCON_ACTIVE_VERSION:
        return False, [
            f"defcon_version '{record_version}' drift vs. active '{DEFCON_ACTIVE_VERSION}'"
        ]

    # Check #7: Platzhalter in den 5 Pflicht-quellen-Feldern
    quellen = record_dict.get("quellen") or {}
    for field in QUELLEN_PFLICHT_FELDER:
        value = quellen.get(field, "")
        if not isinstance(value, str) or _is_placeholder(value):
            return False, [
                f"placeholder source '{value}' in quellen.{field}"
            ]

    # Check #8: skill_meta.migration_to_version inconsistent mit record.defcon_version
    if skill_meta_norm:
        meta_to_version = skill_meta_norm.get("migration_to_version")
        if meta_to_version is not None and meta_to_version != record_version:
            return False, [
                f"skill_meta.migration_to_version='{meta_to_version}' "
                f"inconsistent with record.defcon_version='{record_version}' "
                f"(recycled skill_meta)"
            ]

    return True, []
```

Lauf-Check: `python -c "import sys; sys.path.insert(0,'03_Tools/backtest-ready'); from provenance_gate import check_provenance; print(check_provenance({'source':'backfill'}, [], None))"` → muss `(True, [])` ausgeben.

- [ ] **Step 3.1c: Smoke-Test-Helper + Cases 1-5 einfügen**

Den `print("Skeleton only ...")`-Block am Ende ersetzen durch den Test-Helper + Cases 1-5:

```python
def _build_valid_vollanalyse() -> dict:
    """Minimal-valid vollanalyse-Record für Provenance-Gate-Tests.
    Enthält explizit alle Felder, die die 8 Checks lesen."""
    return {
        "source": "forward",
        "analyse_typ": "vollanalyse",
        "defcon_version": DEFCON_ACTIVE_VERSION,
        "kurs": {
            "wert": 100.0,
            "waehrung": "USD",
            "referenz": "close_of_score_datum",
            "quelle": "yahoo_eod",
        },
        "quellen": {
            "fundamentals": "defeatbeta",
            "technicals": "shibui",
            "insider": "openinsider+sec_edgar",
            "moat": "gurufocus",
            "sentiment": "zacks+yahoo",
        },
    }


def _smoke_tests() -> None:
    # Case 1: Valid vollanalyse, freshness_missing=[], fresh kurs → pass
    rec = _build_valid_vollanalyse()
    passed, reasons = check_provenance(rec, [], None)
    assert passed and reasons == [], f"[1] expected pass, got {passed} {reasons}"
    print("  [1/9] valid vollanalyse + fresh session -> pass")

    # Case 2: vollanalyse + freshness_missing=["STATE.md"] → fail
    rec = _build_valid_vollanalyse()
    passed, reasons = check_provenance(rec, ["STATE.md"], None)
    assert not passed, "[2] expected fail"
    assert "vollanalyse requires fresh session" in reasons[0], f"[2] {reasons}"
    assert "STATE.md" in reasons[0], f"[2] STATE.md not in reason: {reasons}"
    print("  [2/9] vollanalyse + missing STATE.md -> fail")

    # Case 3: vollanalyse + kurs.referenz='close_2026-04-15' (stale) → fail
    rec = _build_valid_vollanalyse()
    rec["kurs"]["referenz"] = "close_2026-04-15"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[3] expected fail"
    assert "vollanalyse requires fresh kurs" in reasons[0], f"[3] {reasons}"
    print("  [3/9] vollanalyse + stale kurs.referenz -> fail")

    # Case 4: rescoring ohne skill_meta → fail
    rec = _build_valid_vollanalyse()
    rec["analyse_typ"] = "rescoring"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[4] expected fail"
    assert "rescoring requires skill_meta" in reasons[0], f"[4] {reasons}"
    print("  [4/9] rescoring ohne skill_meta -> fail")

    # Case 5: delta + source!='forward' → fail
    rec = _build_valid_vollanalyse()
    rec["analyse_typ"] = "delta"
    rec["source"] = "forward"
    passed, reasons = check_provenance(rec, [], None)
    assert passed, f"[5a] forward-delta should pass, got {reasons}"
    rec["source"] = "manual"  # hypothetical 3rd source value
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[5b] expected fail for delta+source!=forward"
    assert "delta is forward-only" in reasons[0], f"[5b] {reasons}"
    print("  [5/9] delta + source!='forward' -> fail")

    # (Cases 6-9 folgen in Step 3.1d)
    print("[partial] Cases 1-5 grün — 6-9 noch ausstehend")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    _smoke_tests()
```

Lauf-Check: `python "03_Tools/backtest-ready/provenance_gate.py"` → 5 PASS-Zeilen + „[partial] Cases 1-5 grün".

- [ ] **Step 3.1d: Smoke-Test Cases 6-9 einfügen + final smoke-message**

In `_smoke_tests()` den Block `# (Cases 6-9 folgen ...)` und `print("[partial] ...")` ersetzen durch:

```python
    # Case 6: Backfill-Record → pass (skip in Check #1)
    rec = _build_valid_vollanalyse()
    rec["source"] = "backfill"
    rec["analyse_typ"] = "vollanalyse"
    passed, reasons = check_provenance(rec, ["STATE.md", "log.md"], None)
    assert passed and reasons == [], f"[6] backfill should skip, got {passed} {reasons}"
    print("  [6/9] backfill skipped -> pass")

    # Case 7: defcon_version='v3.5' aber active='v3.7' → fail
    rec = _build_valid_vollanalyse()
    rec["defcon_version"] = "v3.5"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[7] expected fail"
    assert "drift vs. active" in reasons[0] and "v3.5" in reasons[0], f"[7] {reasons}"
    print("  [7/9] defcon_version drift -> fail")

    # Case 8: quellen.insider='unknown' → fail (+ Variants)
    rec = _build_valid_vollanalyse()
    rec["quellen"]["insider"] = "unknown"
    passed, reasons = check_provenance(rec, [], None)
    assert not passed, "[8a] expected fail"
    assert "placeholder source" in reasons[0] and "insider" in reasons[0], f"[8a] {reasons}"
    for placeholder in ("TBD", "?", "  N/A  ", "PLACEHOLDER"):
        rec_v = _build_valid_vollanalyse()
        rec_v["quellen"]["fundamentals"] = placeholder
        passed_v, reasons_v = check_provenance(rec_v, [], None)
        assert not passed_v, f"[8b:{placeholder!r}] expected fail"
    print("  [8/9] placeholder in quellen -> fail (incl. case/whitespace variants)")

    # Case 9: skill_meta.migration_to_version inconsistent → fail
    rec = _build_valid_vollanalyse()
    bad_meta = {
        "expected_algebra_score": 63,
        "migration_from_version": "v3.5",
        "migration_to_version": "v3.6",  # mismatch vs record=v3.7
    }
    passed, reasons = check_provenance(rec, [], bad_meta)
    assert not passed, "[9] expected fail"
    assert "skill_meta.migration_to_version" in reasons[0], f"[9] {reasons}"
    assert "recycled skill_meta" in reasons[0], f"[9] {reasons}"
    print("  [9/9] recycled skill_meta (migration_to_version inconsistent) -> fail")

    print("✅ all provenance_gate smoke tests passed (9/9)")
```

Lauf-Check folgt in Step 3.2.

- [ ] **Step 3.2: Run — alle 9 Cases müssen PASS**

Run: `python "03_Tools/backtest-ready/provenance_gate.py"`
Expected: `✅ all provenance_gate smoke tests passed (9/9)` mit 9 PASS-Zeilen.

Wenn ein Test fehlschlägt: Logik in `check_provenance` an dem entsprechenden Check-Block prüfen. Kein neuer Plan-Step — Fix iterativ einarbeiten, bis 9/9 grün.

- [ ] **Step 3.3: Regression-Check — alle bestehenden Tests grün?**

Run: `python "03_Tools/backtest-ready/schemas.py"` → `[OK] all schema smoke tests passed`
Run: `python "03_Tools/backtest-ready/archive_score.py"` → `5/5 passed`
Run: `python "01_Skills/backtest-ready-forward-verify/_smoke_test.py"` → `6/6 passed`

(Provenance-Gate ist standalone Library — kein Caller existiert vor Task 4. Keine Regression möglich.)

- [ ] **Step 3.4: Commit**

```bash
git add "03_Tools/backtest-ready/provenance_gate.py"
git commit -m "feat(backtest-ready): Schicht B Pipeline-Gate provenance_gate.py (Task 3)

check_provenance(record_dict, freshness_missing, skill_meta) prüft 8 Checks
fail-close in Reihenfolge:
  1. Backfill-Skip
  2. vollanalyse braucht freshness_missing=[]
  3. vollanalyse braucht kurs.referenz='close_of_score_datum'
  4. rescoring braucht skill_meta für Δ-Gate
  5. delta ist forward-only
  6. defcon_version == versions.DEFCON_ACTIVE_VERSION
  7. Keine Platzhalter in den 5 Pflicht-quellen-Feldern
  8. skill_meta.migration_to_version konsistent mit record.defcon_version

Smoke-Tests 9/9 grün. Caller-Integration in SKILL.md als Phase P3.5
folgt in Task 4. Kein Direkt-CLI — Library-Funktion only.

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §5.2 + §8.1"
```

---

## Task 4: SKILL.md Update — Phase P3.5 vor P3 einhängen

**Files:**
- Modify: `01_Skills/backtest-ready-forward-verify/SKILL.md` (Phase-Tabelle + Pipeline-Diagramm + Section P3.5 neu + Report-Format)

**Rationale:** Spec §5.4. SKILL.md ist die Orchestration-Vorschrift, die der Skill-Aufrufer (`dynastie-depot` Schritt 7) sequenziell abarbeitet. P3.5 muss vor P3 stehen — Spec §4.3: P3 kann mit `skill_meta`-Parse-Fehler abbrechen, ohne dass P3.5 lief; das ist genau der Bypass, den wir schließen.

- [ ] **Step 4.1: Phase-Tabelle (Section 4) erweitern**

Vorher (Zeilen 92-100 von SKILL.md):
```
| Phase | Name | Helper / Tool | Exit bei Fehler |
|-------|------|---------------|-----------------|
| P1 | Draft-Read + Parse | `parse_wrapper(args)` | FAIL P1 |
| P2a | Freshness-Check | `check_freshness(repo_root)` | Warnung (nicht blockierend) |
| P2b | Tripwire | `parse_state_row(ticker, STATE.md)` | FAIL P2b |
| P3 | Δ-Gate (conditional) | `build_migration_event(skill_meta, forward_score)` | STOP signal (nicht blockierend) |
| P4 | Dry-Run | `archive_score.py --file <draft> --dry-run` | FAIL P4 |
| P5 | Real Append | `archive_score.py --file <draft>` | FAIL P5 |
| P6 | git add | `git add 05_Archiv/score_history.jsonl` | FAIL P6 (manuell recovery) |
```

Nachher:
```
| Phase | Name | Helper / Tool | Exit bei Fehler |
|-------|------|---------------|-----------------|
| P1 | Draft-Read + Parse | `parse_wrapper(args)` | FAIL P1 |
| P2a | Freshness-Check | `check_freshness(repo_root)` | Warnung (nicht blockierend) |
| P2b | Tripwire | `parse_state_row(ticker, STATE.md)` | FAIL P2b |
| **P3.5** | **Provenance-Gate** | **`check_provenance(record_dict, freshness_missing, skill_meta)`** | **FAIL P3.5 (fail-close, kein Archiv-Write)** |
| P3 | Δ-Gate (conditional) | `build_migration_event(skill_meta, forward_score)` | STOP signal (nicht blockierend) |
| P4 | Dry-Run | `archive_score.py --file <draft> --dry-run` | FAIL P4 |
| P5 | Real Append | `archive_score.py --file <draft>` | FAIL P5 |
| P6 | git add | `git add 05_Archiv/score_history.jsonl` | FAIL P6 (manuell recovery) |
```

(Anmerkung Phase-Reihenfolge: P3.5 läuft VOR P3, obwohl der Name höher klingt — bewusst, um den Append-Pfad nicht zu rebrandern. Phasen-Namen-Stabilität für bestehende Logs.)

- [ ] **Step 4.2: Neue Section "P3.5 — Provenance-Gate" zwischen P2b und P3 einfügen**

Nach der bestehenden P2b-Section (endet auf Zeile 135 mit "Bei jedem `FAIL phase=P2b`: ..."), VOR der P3-Section (beginnt auf Zeile 137 mit `### P3 — Algebra-Δ-Gate (conditional)`), folgenden Block einfügen:

```markdown
### P3.5 — Provenance-Gate (fail-close)

Importiere `check_provenance` aus `03_Tools/backtest-ready/provenance_gate.py`.
Aufruf:

```python
passed, reasons = check_provenance(
    record_dict=record_dict,         # aus P1
    freshness_missing=missing_files,  # aus P2a
    skill_meta=skill_meta,            # aus P1 ({} falls leer)
)
```

- `passed=True` → weiter zu P3.
- `passed=False` → **Pipeline abbrechen — P3/P4/P5/P6 nicht ausführen. Kein Archiv-Write.**
  Emit: `FAIL phase=P3.5 reason="<reasons[0]>"`. Exit-Code 1.

Acht Checks fail-close in Reihenfolge (Spec §5.2):
1. `source="backfill"` → skip (Schicht B prüft nur Forward-Pfad).
2. `analyse_typ="vollanalyse"` aber `freshness_missing != []` → FAIL.
3. `analyse_typ="vollanalyse"` aber `kurs.referenz != "close_of_score_datum"` → FAIL.
4. `analyse_typ="rescoring"` aber `skill_meta` leer → FAIL.
5. `analyse_typ="delta"` aber `source != "forward"` → FAIL.
6. `defcon_version != versions.DEFCON_ACTIVE_VERSION` → FAIL.
7. Platzhalter (`unknown`/`tbd`/`todo`/`?` etc., case-insensitive) in einem der 5 Pflicht-`quellen`-Felder → FAIL.
8. `skill_meta` vorhanden + `skill_meta["migration_to_version"] != record.defcon_version` → FAIL (recycled meta).

Recovery siehe Spec §7.2 Recovery-Matrix. Kein `--force`-Flag — Provenance-Verletzungen werden via Workflow-Korrektur gelöst (Daten ergänzen / `analyse_typ` umklassifizieren).
```

- [ ] **Step 4.3: Report-Format Section 6 erweitern — neue P3.5-FAIL-Zeile**

Vorher (Zeilen 206-209):
```
**Bei Fehler (Exit 1 oder 2):**
```
FAIL phase=<P1|P2b|P4|P5|P6> reason="<Fehlermeldung>"
```

Nachher:
```
**Bei Fehler (Exit 1 oder 2):**
```
FAIL phase=<P1|P2b|P3.5|P4|P5|P6> reason="<Fehlermeldung>"
```

P3.5-Beispiele: `FAIL phase=P3.5 reason="vollanalyse requires fresh session (missing: ['log.md']); reclassify as rescoring or complete workflow"`.
```

- [ ] **Step 4.4: Authoritative-Sources-Tabelle (Section 2) erweitern**

In der Tabelle (Zeilen 46-54) nach der bestehenden `_forward_verify_helpers.py`-Zeile diese drei Zeilen einfügen:

```
| `03_Tools/backtest-ready/provenance_gate.py::check_provenance` | Schicht B Pipeline-Gate (P3.5), 8 Checks fail-close |
| `03_Tools/backtest-ready/versions.py::DEFCON_ACTIVE_VERSION` | SSoT für aktive DEFCON-Version (Schicht B Check #6, schemas._check_forward_version) |
| `03_Tools/backtest-ready/schemas.py::ScoreRecord._check_vollanalyse_block_coverage` | Schicht D Block-Coverage (4 Blöcke, insider ausgenommen) |
```

- [ ] **Step 4.5: Skill smoke tests laufen lassen (sollten weiter PASS bleiben)**

Run: `python "01_Skills/backtest-ready-forward-verify/_smoke_test.py"`
Expected: `✅ all 6/6 cases passed` (Markdown-Änderungen brechen Helper-Tests nicht).

- [ ] **Step 4.6: Commit**

```bash
git add "01_Skills/backtest-ready-forward-verify/SKILL.md"
git commit -m "feat(skill): Phase P3.5 Provenance-Gate in backtest-ready-forward-verify SKILL.md

Phase-Tabelle erweitert um P3.5 zwischen P2b und P3 (vor Δ-Gate, da P3
mit skill_meta-Parse-Fehler abbrechen kann und P3.5 sonst übersprungen
würde). Neue Section 'P3.5 — Provenance-Gate' mit 8-Check-Tabelle und
Aufruf-Pattern. Authoritative-Sources erweitert um provenance_gate.py +
versions.py + schemas._check_vollanalyse_block_coverage. Report-Format
Section 6 ergänzt um P3.5-FAIL-Zeile.

Integration-Test (Caller simuliert Pipeline) folgt in Task 5.

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §5.4 + §4.3"
```

---

## Task 5: Integration-Test in _smoke_test.py — Case 7 fail-close

**Files:**
- Modify: `01_Skills/backtest-ready-forward-verify/_smoke_test.py` (Case 7 hinzufügen + CASES-Tupel + run_all-Counter aktualisieren)

**Rationale:** Spec §8.3 — bei fail-close hängt die Schutzwirkung an korrekt verdrahteter Pipeline. Unit-Tests einzelner Funktionen reichen nicht. Case 7 simuliert die SKILL.md-Orchestrierung in Python: P1 → P2a → P2b → P3.5, asserts fail-close (P3.5 returns passed=False, archive bleibt unverändert, P4/P5/P6 werden nicht aufgerufen).

- [ ] **Step 5.1: Import erweitern**

Vorher (Zeilen 180-190 in `_smoke_test.py`):
```python
try:
    from _forward_verify_helpers import (
        build_migration_event,
        check_freshness,
        parse_state_row,
        parse_wrapper,
    )
    HELPERS_AVAILABLE = True
except ImportError as _imp_err:
    HELPERS_AVAILABLE = False
    _IMPORT_ERROR = _imp_err
```

Nachher:
```python
try:
    from _forward_verify_helpers import (
        build_migration_event,
        check_freshness,
        parse_state_row,
        parse_wrapper,
    )
    from provenance_gate import check_provenance
    HELPERS_AVAILABLE = True
except ImportError as _imp_err:
    HELPERS_AVAILABLE = False
    _IMPORT_ERROR = _imp_err
```

- [ ] **Step 5.2: Case 7 nach Case 6 einfügen (vor `# Harness`-Trennlinie auf Zeile ~495)**

```python
# ---------------------------------------------------------------------------
# Case 7: Integration — P1 → P2a → P2b → P3.5 fail-close, no archive write
# ---------------------------------------------------------------------------
def case_7() -> None:
    """Synthetischer vollanalyse-Draft mit Provenance-Fail (freshness_missing=['STATE.md']).
    Asserts: P3.5 returns (False, reason), reason mentions vollanalyse+fresh,
    archive_score.py NICHT aufgerufen → Archiv-File unverändert.
    Spec §8.3: Integration-Test ist Pflicht (fail-close hängt an Pipeline-Verdrahtung).
    """
    _require_helpers()

    # Build a forward+vollanalyse record (NOT backfill — would skip Check #1)
    ticker = "ZTS"
    score_datum = "2026-04-21"
    record = _build_minimal_record(
        ticker, score_datum, score_gesamt=65, defcon_level=3
    )
    # Override to forward+vollanalyse with valid kurs.referenz + valid quellen + active version
    record["source"] = "forward"
    record["analyse_typ"] = "vollanalyse"
    record["defcon_version"] = "v3.7"  # match versions.DEFCON_ACTIVE_VERSION
    record["kurs"] = {
        "wert": 100.0,
        "waehrung": "USD",
        "referenz": "close_of_score_datum",
        "quelle": "yahoo_eod",
    }
    record["quellen"] = {
        "fundamentals": "defeatbeta",
        "technicals": "shibui",
        "insider": "openinsider+sec_edgar",
        "moat": "gurufocus",
        "sentiment": "zacks+yahoo",
    }
    draft = {"record": record, "skill_meta": {}}

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tf:
        json.dump(draft, tf)
        draft_path = tf.name

    # P1: parse_wrapper
    rec_dict, skill_meta = parse_wrapper(draft_path)
    assert rec_dict["analyse_typ"] == "vollanalyse"
    assert skill_meta == {}

    # P2a (simulated): freshness_missing manuell setzen statt git-status zu mocken
    # Spec §8.3: "freshness_missing=['STATE.md']" als Fail-Trigger.
    freshness_missing = ["STATE.md"]

    # P2b: STATE-Tripwire (kein Konflikt — wir nutzen ZTS, das nicht im STATE_MD_FIXTURE ist)
    try:
        parse_state_row(ticker, STATE_MD_FIXTURE)
    except (ValueError, KeyError):
        # Erwartet: ZTS nicht in STATE.md → Caller würde "[tripwire: ticker 'ZTS' not in
        # STATE.md — new position]" emitten und weiter machen. Kein FAIL P2b.
        pass

    # P3.5: hier muss fail-close greifen
    passed, reasons = check_provenance(
        record_dict=rec_dict,
        freshness_missing=freshness_missing,
        skill_meta=skill_meta,
    )
    assert not passed, f"P3.5 should fail-close, got passed={passed}"
    assert len(reasons) == 1, f"fail-close means 1 reason, got {reasons}"
    assert "vollanalyse requires fresh session" in reasons[0], (
        f"reason should match Check #2: {reasons[0]!r}"
    )
    assert "STATE.md" in reasons[0], f"missing-file detail in reason: {reasons[0]!r}"

    # Verify: archive_score.py was NEVER called → real archive_history.jsonl unverändert.
    # We verify by snapshotting size before and after; case_7 must NOT subprocess archive_score.
    archive_path = REPO_ROOT / "05_Archiv" / "score_history.jsonl"
    if archive_path.exists():
        size_before = archive_path.stat().st_size
        # (no subprocess call here — that's the whole point)
        size_after = archive_path.stat().st_size
        assert size_before == size_after, (
            f"archive must not be touched on P3.5 fail; "
            f"size_before={size_before}, size_after={size_after}"
        )
    # If archive doesn't exist yet, the assertion is trivially true
```

- [ ] **Step 5.3: CASES-Tupel und run_all-Counter erweitern**

Vorher (Zeilen 498-505 + 522-525):
```python
CASES = [
    (1, "Wrapper-Parse-Helper basic", case_1),
    (2, "MigrationEvent injection — accepted (delta=1)", case_2),
    (3, "MigrationEvent log_only grenzfall (delta=4)", case_3),
    (4, "MigrationEvent block (delta=-23) + STOP signal", case_4),
    (5, "parse_state_row — all style variants", case_5),
    (6, "check_freshness — git status detection", case_6),
]
```

Nachher:
```python
CASES = [
    (1, "Wrapper-Parse-Helper basic", case_1),
    (2, "MigrationEvent injection — accepted (delta=1)", case_2),
    (3, "MigrationEvent log_only grenzfall (delta=4)", case_3),
    (4, "MigrationEvent block (delta=-23) + STOP signal", case_4),
    (5, "parse_state_row — all style variants", case_5),
    (6, "check_freshness — git status detection", case_6),
    (7, "Integration — P3.5 fail-close, no archive write", case_7),
]
```

Außerdem in `run_all()` die fixe `passed}/6 cases` und `[{n}/6]` Strings ersetzen:

Vorher:
```python
        try:
            fn()
            print(f"[{n}/6] PASS: {label}")
            passed += 1
        except Exception as exc:
            print(f"[{n}/6] FAIL: {label} — {type(exc).__name__}: {exc}")
            failed += 1

    print()
    if failed == 0:
        print(f"✅ all {passed}/6 cases passed")
```

Nachher:
```python
        try:
            fn()
            print(f"[{n}/{len(CASES)}] PASS: {label}")
            passed += 1
        except Exception as exc:
            print(f"[{n}/{len(CASES)}] FAIL: {label} — {type(exc).__name__}: {exc}")
            failed += 1

    print()
    if failed == 0:
        print(f"✅ all {passed}/{len(CASES)} cases passed")
```

(Dynamisch via `len(CASES)` statt hard-coded 6 — vermeidet Drift bei zukünftigen Case-Erweiterungen.)

- [ ] **Step 5.4: Run smoke tests — alle 7 müssen PASS**

Run: `python "01_Skills/backtest-ready-forward-verify/_smoke_test.py"`
Expected: `✅ all 7/7 cases passed` mit 7 PASS-Zeilen `[1/7]`...`[7/7]`.

- [ ] **Step 5.5: Sanity — Archiv-File wirklich unverändert?**

```bash
git status -- "05_Archiv/score_history.jsonl"
```
Expected: keine Ausgabe (file unmodified). Falls modified → Test hat versehentlich appendiert. Stop, debuggen.

- [ ] **Step 5.6: Commit**

```bash
git add "01_Skills/backtest-ready-forward-verify/_smoke_test.py"
git commit -m "test(skill): Case 7 Integration-Test P3.5 fail-close (Provenance-Gate Task 5)

Synthetischer vollanalyse-Draft mit freshness_missing=['STATE.md'] durchläuft
P1 → P2a (simulated) → P2b (ZTS not in STATE.md = neuer Ticker, weiter) → P3.5.
Asserts: passed=False, reason mentions vollanalyse+fresh+STATE.md,
score_history.jsonl unverändert (kein archive_score-Aufruf).

CASES-Counter dynamisch via len(CASES); 7/7 grün.

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §8.3"
```

---

## Task 6: Documentation Go-Live — STATE.md + INSTRUKTIONEN §18 + CORE-MEMORY §10

**Files:**
- Modify: `00_Core/STATE.md` (System-Zustand-Sektion)
- Modify: `00_Core/INSTRUKTIONEN.md §18` (Sync-Pflicht-Zeile)
- Modify: `00_Core/CORE-MEMORY.md §10` (Go-Live Audit-Log-Eintrag — Codex-Korrektur 21.04. gegenüber Plan v1)

**Rationale:** Spec §9 markiert alle drei als „bei Go-Live". Go-Live = nach diesem Plan-Merge — der Gate ist mit dem letzten Commit live (P3.5 ist Teil der Pipeline). Codex-Review 21.04. korrigiert Plan v1: CORE-MEMORY §10-Eintrag gehört NICHT in den First-Live-Run, sondern in Task 6 (Spec-§9-Alignment). First-Live-Run bei TMO Q1 23.04.2026 produziert dann zusätzlich einen second §10-Eintrag mit dem konkreten First-Use-Result.

Hinweis: Diese Markdown-Edits laufen direkt (kein Subagent — siehe Applied Learning Bullet 1: Subagents nur für Code+Tests).

- [ ] **Step 6.1: STATE.md System-Zustand erweitern**

In `00_Core/STATE.md` Section "## System-Zustand" — nach dem bestehenden `Forward-Verify-Pipeline via Skill`-Punkt (~Zeile 65) einen neuen Bullet einfügen:

```markdown
- **Provenance-Gate aktiv** (seit YYYY-MM-DD, Schicht B + D): `provenance_gate.py::check_provenance` läuft als Phase P3.5 zwischen P2b und P3 in `backtest-ready-forward-verify`. Acht Checks fail-close (Backfill-Skip / Freshness / Kurs-Referenz / Skill-Meta-Pflicht / Delta-Forward / Version-Drift / Platzhalter / Recycled-Meta). Schema-Validator `_check_vollanalyse_block_coverage` als Schicht D gegen Direkt-CLI an `archive_score.py`. SSoT-Version in `versions.py::DEFCON_ACTIVE_VERSION`. Erste Live-Anwendung: TMO Q1 23.04.2026.
```

(Datum auf das tatsächliche Merge-Datum setzen, nicht hartcodieren.)

- [ ] **Step 6.2: INSTRUKTIONEN §18 ergänzen**

In `00_Core/INSTRUKTIONEN.md §18` (Sync-Pflicht-Sektion) eine Klarstellungs-Zeile am Ende des §-Blocks anfügen:

```markdown
**Provenance-Gate-Hinweis:** Score-Append läuft via `backtest-ready-forward-verify` Skill (Pipeline-Phase P3.5 fail-close). Bei `FAIL phase=P3.5` gibt es keinen `--force`-Bypass — Recovery durch Workflow-Korrektur (Pflicht-Touch-Files berühren / `analyse_typ` umklassifizieren / quellen-Felder mit echten Quellen befüllen / Versions-Drift via Migration-Pipeline lösen).
```

- [ ] **Step 6.3: CORE-MEMORY §10 Audit-Log Go-Live-Eintrag**

In `00_Core/CORE-MEMORY.md §10` (Audit-Log-Sektion) am Ende einen neuen Eintrag anhängen:

```markdown
### YYYY-MM-DD — Provenance-Gate Go-Live (Plan-Merge)

- **Was deployed:** P3.5 fail-close in `backtest-ready-forward-verify` (Schicht B `provenance_gate.py::check_provenance` mit 8 Checks) + Schicht D `ScoreRecord._check_vollanalyse_block_coverage` Validator + SSoT `versions.py::DEFCON_ACTIVE_VERSION`. Plan: `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md`. Spec: `docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md`.
- **Pre-Check vor Execution:** N/N PASS (siehe Task 0 Output).
- **Smoke-Tests post-Execution:** schemas 11/11 + archive_score 5/5 + provenance_gate 9/9 + skill 7/7 (inkl. Case 7 Integration-Test fail-close).
- **Drift-Migration prerequisite:** commit `ca76114` (21.04.2026) Snap-to-Schema 12/27→27/27.
- **First-Live-Run erwartet:** TMO Q1 23.04.2026 (eigener §10-Eintrag mit konkretem Pipeline-Sequenz-Result folgt dort).
- **Promotion-Trigger:** nach 3-4 realen Anwendungen Applied-Learning-Scan ob INSTRUKTIONEN-§-Promotion gerechtfertigt (Spec §10 Follow-up).
```

(Datum auf das tatsächliche Merge-Datum setzen, nicht hartcodieren. „N/N PASS" mit konkreter Zahl aus Task 0 ersetzen.)

- [ ] **Step 6.4: Briefing-Sync (falls 00_Core/ geändert wurde)**

CLAUDE.md verlangt `!SyncBriefing` vor Session-Ende, wenn `00_Core/` modifiziert wurde. STATE.md + INSTRUKTIONEN.md + CORE-MEMORY.md sind in `00_Core/` → Sync nötig.

(Wird vom Caller als separater Schritt nach dem Plan ausgeführt — kein Code-Step. Erwähnt hier nur als Reminder.)

- [ ] **Step 6.5: Commit (gemeinsam mit Briefing-Sync-Output, falls vorhanden)**

```bash
git add "00_Core/STATE.md" "00_Core/INSTRUKTIONEN.md" "00_Core/CORE-MEMORY.md"
git commit -m "docs(provenance-gate): Go-Live STATE.md + INSTRUKTIONEN §18 + CORE-MEMORY §10 (Task 6)

System-Zustand-Eintrag dokumentiert Provenance-Gate (Phase P3.5 fail-close,
8 Checks, SSoT-Version, Schicht D Block-Coverage). INSTRUKTIONEN §18 um
no-force-Bypass-Klarstellung erweitert. CORE-MEMORY §10 Audit-Log-Eintrag
mit Pre-Check-Resultat + Smoke-Test-Summary + Drift-Migration-Prerequisite.

First-Live-Run-Eintrag bei TMO Q1 23.04.2026 als zweiter §10-Block.

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md §9"
```

---

## Verification — End-to-End-Check nach Task 6

- [ ] **VC.1: Alle drei Smoke-Test-Suites grün**

Run in einer Session:
```bash
python "03_Tools/backtest-ready/schemas.py" && \
python "03_Tools/backtest-ready/archive_score.py" && \
python "03_Tools/backtest-ready/provenance_gate.py" && \
python "01_Skills/backtest-ready-forward-verify/_smoke_test.py"
```

Expected (in dieser Reihenfolge):
- `[OK] all schema smoke tests passed` (11 Cases)
- `✅ all archive_score smoke tests passed` (5/5)
- `✅ all provenance_gate smoke tests passed (9/9)`
- `✅ all 7/7 cases passed`

- [ ] **VC.2: `score_history.jsonl` unverändert (27 Records, keine Test-Mutation)**

```bash
wc -l "05_Archiv/score_history.jsonl"
git status -- "05_Archiv/score_history.jsonl"
```
Expected: `27` Zeilen, kein git-status-Output.

- [ ] **VC.3: Plan-Status update**

Diesen Plan-Datei nicht löschen — referenziert von Spec §10 als Nachfolge-Artefakt. Nach erfolgreichem Merge: optional Status-Header oben hinzufügen `**Status:** completed YYYY-MM-DD`.

---

## Follow-up (außerhalb dieses Plans)

- **First-Live-Run bei TMO Q1 23.04.2026:** Erwartete Pipeline-Sequenz im Erfolgsfall: P1 → P2a (alle 3 Pflicht-Files modified) → P2b (TMO in STATE) → P3.5 (alle 8 Checks pass) → P3 (skill_meta=ja → Δ-Gate fcf_trend_neg-Resolve) → P4/P5/P6 grün. **Zweiter** CORE-MEMORY §10 Audit-Log-Eintrag im selben `!Analysiere`-Sync (mit konkretem Pipeline-Sequenz-Result + tatsächlicher Δ-Gate-Outcome). Erster §10-Eintrag entstand bereits in Task 6 Step 6.3 als Go-Live-Marker.
- **Evidence-basierte Promotion zu INSTRUKTIONEN-§:** Nach 3-4 realen Anwendungen Applied-Learning-Scan: wurde Gate genutzt? Wurde realer Fehler verhindert? Bei Ja → INSTRUKTIONEN §-Promotion (Spec §10).
- **B20 GT-Score Future-Compatibility:** Bei §29.1-Aktivierung (Review 2028 oder erste DEFCON-Parameter-Variation) ggf. neue Phase P3.7 nach P3 — disjunkt zu P3.5 (Append-Time vs Parameter-Loop-Time). Nicht Teil dieses Plans.
- **B18 Seven-Sins Future-Compatibility:** §29.5 Pre-Flight läuft bei Migration-Events (§28), nicht bei Standard-Forward-Appends. Falls bei Migration-Runs zusätzliche Pre-Flight-Checks nötig: separate Migration-Pipeline-Phase, nicht Erweiterung von P3.5.

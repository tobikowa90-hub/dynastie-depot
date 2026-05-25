# SPEC — xlsx-smoke-test-runner v0.1 (α+ Adaption)

**Status**: GO-Ready post Codex-Sparring R1+R2 — 0 HIGH offen, alle R1+R2-Findings adressiert. Bereit für Stage-1-Implementation (Schritt 0-4 in §6).
**Stand**: 2026-05-25 ~20:00
**Substrate**: `drift-live-vs-doc.md` v1.4 (16 Patches, 8 HIGH/5 MED/3 LOW)
**Scope-Mode**: α+ — Verify-Wrapper + `safe_insert.py` Helper, Pipeline ~2.5h (revised 3.75h), KEIN „Core Slim Refactor 2.0"
**Detail-Mode**: Option 2 — Function-Signatures + Docstring-Verträge, KEIN Body (Execution = separate Session per `feedback_brainstorming_terminal_override_dynastie`)

## Changelog (R1+R2-Patches + Coverage-Gap-Expansion)

**Coverage-Gap-Expansion 2026-05-25T20:05** (post grep-Verify Schritt 0+1): P15 Multi-File-Sync von 3 auf 4 Files erweitert — SYSTEM.md L42 (v2.4-Lifecycle-Eintrag mit Live-State-Aussage „218/6 + 12/5") war initial als „historischer Snapshot" mis-skopt. User-Direktive: Live-State-Aussagen sind Live unabhängig von Lifecycle-Umrahmung. Neuer Memory: [[feedback_historical_snapshot_not_a_scope_excuse]].

**R2 Diff-Re-Review (post R1-Patches)** — Verdikt: HOLD mit 0 HIGH + 3 MED + 1 LOW; alle adressiert. R3 NICHT pflicht (HIGH-Threshold per `feedback_codex_sparring_heuristic` nicht erreicht).

| R2-Finding | Severity | Adressiert in | Mechanismus |
|------------|----------|---------------|-------------|
| MED-1 sha256-Determinismus unvollständig | MED | §5.2 normativer Rewrite | ZIP-Subset-Hashing (`fixture_content_sha256`) statt Core-Properties-Null; Akzeptanz-#5 angepasst |
| MED-2 Changelog ↔ §4.3/§9 Widerspruch | MED | §4.3 + §9 | „Offene Frage" als CLOSED markiert; §9-HIGH-Risiko-Eintrag als RESOLVED markiert |
| MED-3 §4.1 alter Import-Pfad | MED | §4.1 `safe_save`-Docstring | Verweis auf `_load_hook_module()` statt dotted-Import |
| LOW Schritt-0-Aufwand | LOW | §6 Schritt 0 | 5min → 10min (inkl. grep-Verify) |
| INFO Commit-Strategie | — | §6 Schritt 0 | „gemeinsamer Commit mit Schritt 1" als Default, getrennt nur mit explizitem Type-Scope |

## Changelog (R1-Patches)

| Finding | Severity | Adressiert in | Mechanismus |
|---------|----------|---------------|-------------|
| HIGH-1: §G Anker-Pfad-Drift | HIGH | §4.3 + §10 + §6 Sync-Pflicht | Pfad-Korrektur auf `brokers.scalable.sparrate_eur` (verified L27); drift-doc §2.4 + §P8 Multi-File-Sync-Pflicht ergänzt |
| HIGH-2: verify_wrapper Import-Pfad | HIGH | §4.2 SSoT-Delegation-Block + Code-Snippet `_load_hook_module` | importlib.util.spec_from_file_location-Pattern (Standard-Library) |
| MED-1: Fixture-Summe-Arithmetik | MEDIUM | §5 Total-Zeile | „12 Profile + 3 Helper = 15" |
| MED-2: open-repair/shared-string Fixtures | MEDIUM | §5.3 (neu) | Explizit out-of-scope mit Re-Activation-Trigger |
| MED-3: sha256-Determinismus | MEDIUM | §5.2 (neu) | Core-Properties-Fix-Snippet + ZIP-Subset-Alternative |
| MED-4: Schritt-7-Zeitschätzung | MEDIUM | §6 Schritt 7a/7b/7c-Split | 30min → 20+15+15min |
| LOW: §4.1 Cross-Sheet-Refs | LOW | §4.1 Docstring | Out-of-Scope-Klausel |
| LOW: §2.3 vs §7 Redundanz | LOW | §2.3 Kurz-Liste | Verweis auf §7 normativ |
| LOW: §4.4 startswith-Fragilität | LOW | §4.4 Profile-Matching-Block | v0.2-Refactor-Pfad dokumentiert |
| LOW: §9 §G-Latenz-Risiko | LOW | §9 Risiko-Tabelle | Latenz-Schätzung + Mitigation |

---

## §0 Lineage + Methodologie

Diese Spec ist Output von 3 Gate-0-Vorarbeiten (durable, in Repo):

| Gate | Artefakt | verified via |
|------|----------|--------------|
| 0a (Skill-Scope-Statement) | `drift-live-vs-doc.md` §0a | Codex-R2-F5 adressiert |
| 0b (Drift-Doc) | `drift-live-vs-doc.md` 16 Patches | empirie-getestet 2026-05-25T17:31 + T18:30 |
| 0c (Coverage-Matrix) | **§2 dieser Spec** | Pflicht per `feedback_skill_name_is_scope_contract` |

**Annotations-Regel**: Jede normative Behauptung in dieser Spec trägt `verified via:`-Annotation (Mindeststandard v0.1: `sheet!cell + timestamp` ODER `Pfad:Zeile + grep-cmd`). Volles 4-Felder-Schema (sheet!cell + Read-Expr + Erwartet + Timestamp) verschoben auf v0.2 (Codex-R2-F4-deferred).

---

## §1 Skill-Identity (literal aus drift-doc §0a)

**Name**: `xlsx-smoke-test-runner`
**Version**: v0.1
**Capability-Vertrag** (NICHT aspirational, normativ literal):

**In-Scope (Skill automatisiert)**:
- **§A** Open-Repair (Workbook-Load + Sheet-Existenz aller Profile-Sheets)
- **§B** Error-Token-Scan (`#REF!`/`#NAME?`/`#VALUE!`/`#N/A` in allen Sheets)
- **§E** CF-Rule-Count-Drift-Check pro Profil
- **§G** Sparrate-Σ-Sanity (config.yaml-Mapping → Σ-Check gegen Anker 285€ + xlsx-Display-Konsistenz K3/B3/B26/N19)
- Pflicht-Cell-Existenz-Checks (Adressen aus `xlsx-smoke-test.md` §C/§D)

**Out-of-Scope (manuell bzw. UI-only)**:
- **§C/§D** Pflicht-Cell-Inhalt-Semantik (gehört zu §18-Sync)
- **§F** Read-only-Close (interaktiv)
- Cell-Number-Format, CF-Rules-Identität, Defined Names, Pivots, Workbook-Protection, Print-Settings

**SKILL.md `description`-Field** (Pflicht-Übernahme): muss diese In/Out-Listen literal nennen — keine Erweiterung ohne SPEC-Update + Coverage-Matrix-Re-Run.

---

## §2 Coverage-Matrix (Gate-0 — NORMATIV)

Pflicht-Tabelle per `feedback_skill_name_is_scope_contract`: **alle in-scope Targets × alle Capabilities × Hook-Coverage × Test-Fixture**. Lücken werden HIGH-Findings im Codex-Sparring.

### 2.1 Profile × Capability

| Profil | §A Open | §A Sheets | §B Error-Tokens | §E CF-Count | §G Sparrate-Σ | §C/§D Pflicht-Cell-Existenz |
|--------|---------|-----------|-----------------|-------------|---------------|-----------------------------|
| `Rebalancing_Tool_v3.4.xlsx` | ✓ Pflicht | 3 Sheets (Portfolio & Rebalancing, US-Exposure, Parameter & Regeln) | ✓ alle Sheets | 6 CF (5+0+1) | n/a (Rebal hat P22-Formel-Σ, kein Hook-G) | R2/A2 datum-stempel + N10-N21 DEFCON + O10-O21 FLAG + P5-P21 Sparrate-Formeln + R22-Aggregate + US-Exposure-Sentinel R4/R20/R21E/R25B |
| `Satelliten_Monitor_v2.0.xlsx` | ✓ Pflicht | 2 Sheets (Satelliten Monitor, QuickScreen Ampel) | ✓ alle Sheets | 5 CF | ✓ Pflicht (config.yaml → Σ=285 + K3/B3/B26/N19 Display-Konsistenz) | O2 Stand-String + B3 Sparrate-Header + H3 Eingefroren-Liste + K3 Ergebnis-Zeile + L7-L18 Score/DEFCON + M7-M18 Δ + N7-N18 Status + B24 Legende + B25 Eingefroren-Liste + B26 Volle-Rate-Liste + N19 Sanity-Echo |
| `Watchlist_Ersatzbank_Monitor_v1.1.xlsx` | ✓ Pflicht (Minimal) | 1 Sheet (Watchlist_Ersatzbank) | n/a (0 Formeln) | 0 CF | n/a | A1-non-empty (Existenz-Proxy) + R3 Ersatzbank-Count-Konsistenz (optional P11) |

**verified via**: `wb.sheetnames` + `len(ws.conditional_formatting._cf_rules)` 2026-05-25T17:31 (drift-doc §1.1 + §2.1 + §3.2)

### 2.2 Coverage-Status pro Capability

| Capability | Hook (`xlsx_smoke_test.py`) | Verify-Wrapper (neu) | safe_insert.py (neu) | Test-Fixtures (neu) |
|------------|-----------------------------|----------------------|----------------------|----------------------|
| §A Open + Sheets | ✓ existing (post-P13) | post-Write Re-Open | n/a | clean + corrupted_file |
| §B Error-Tokens | ✓ existing | post-Write Re-Scan | n/a | clean + error_token_in_cell |
| §E CF-Count | ✓ existing | post-Write Re-Count | preserve-on-insert | clean + cf_count_mismatch |
| §G Sparrate-Σ | NEU (Punkt G ext) | post-Write Display-Konsistenz | n/a (config.yaml read-only) | clean + g_mapping_drift + g_display_drift |
| Pflicht-Cell-Existenz | nicht-implementiert (out-of-hook, manuell §C/§D) | n/a | n/a | n/a |

**Implikation**: Hook bekommt §G-Erweiterung (P8). Verify-Wrapper ist neuer Layer um openpyxl-Writes (post-Write Re-Validation via Hook-Funktionen). `safe_insert.py` ist insert+merge-Trap-Schutz (AMZN-Bug-Klasse, `feedback_openpyxl_insert_merge_trap`), nicht Sparrate-Σ-related.

### 2.3 Coverage-Lücken (Kurz-Liste — normativ siehe §7)

Per Codex-R1 LOW: §2.3 ist NICHT Doppel-Pflege gegen §7, sondern Kurz-Hinweis. §7 ist normative Out-of-Scope-Liste.

- Cross-Sheet-Refs systematisch (LOW, v0.2)
- 4-Felder-Annotation-Schema (LOW, v0.2)
- §C/§D Cell-Semantik-Validation (by-design manuell)
- Cell-Number-Format / CF-Rules-Identität / Defined Names / Pivots / Protection / Print (by-design)

**→ Volldetail, Re-Activation-Trigger, Promotion-Schwelle: §7 dieser Spec.**

---

## §3 Architecture — 3-Layer-Modell

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: Pre-commit Hook (existing + P13/P8-Erweiterung)    │
│   03_Tools/precommit/xlsx_smoke_test.py                     │
│   Gates: §A + §B + §E + §G (neu)                            │
│   Trigger: git pre-commit, fail-close auf stderr            │
├─────────────────────────────────────────────────────────────┤
│ Layer 2: Verify-Wrapper (neu, Skill-Body)                   │
│   01_Skills/xlsx-smoke-test-runner/verify_wrapper.py        │
│   Funktion: Post-Write-Re-Validation um openpyxl-Saves      │
│   Use-Case: §18-Sync-Edits an Rebal/Sat/Watch xlsx          │
│   Library-Mode (kein CLI) — Skill konsumiert via import     │
├─────────────────────────────────────────────────────────────┤
│ Layer 3: safe_insert.py (neu, Skill-Helper)                 │
│   01_Skills/xlsx-smoke-test-runner/safe_insert.py           │
│   Schutz: openpyxl insert+merge Trap (AMZN-Bug-Klasse)      │
│   Pattern: unmerge VOR insert → insert → re-merge aus capt. │
└─────────────────────────────────────────────────────────────┘
```

**Composability**: Verify-Wrapper ruft Hook-Funktionen (`validate_file`, `_count_cf_rules`) via import auf. `safe_insert.py` ist standalone (kein Hook-Import). SSoT für Profile-Soll-Werte bleibt `_PROFILES`-Dict im Hook (post-P13 mit erweiterten Sheets-Listen).

---

## §4 Component-Specs (Signatures + Docstring-Verträge)

### 4.1 `safe_insert.py` — openpyxl Insert+Merge-Trap-Schutz

**Datei**: `01_Skills/xlsx-smoke-test-runner/safe_insert.py`
**Zweck**: AMZN-Bug-Klasse (`feedback_openpyxl_insert_merge_trap`) — merged Range über insert-Zeile schluckt non-anchor-Writes silent.
**Substrate-Audit**: 0 existing Code (drift-doc §Substrate-Status, Grep 2026-05-25T18:15). Neubau.

```python
from __future__ import annotations
from pathlib import Path
from typing import Literal
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


def safe_insert_rows(
    ws: Worksheet,
    idx: int,
    amount: int = 1,
) -> None:
    """Sicheres `ws.insert_rows(idx, amount)` mit Merge-Preservation.

    Per `feedback_openpyxl_insert_merge_trap`:
    1. Capture aller `ws.merged_cells.ranges` die `idx` überlappen
    2. Unmerge dieser Ranges VOR `insert_rows`
    3. `ws.insert_rows(idx, amount)` ausführen
    4. Re-merge der gecaptureten Ranges, verschoben um `amount` Zeilen

    Vertrag:
    - Schreibt NICHT die Datei (Caller muss `wb.save()` aufrufen + Verify-Wrapper laufen lassen)
    - Wirft `ValueError` bei `amount < 1` (inkl. `amount=0` → ValueError)
    - Wirft `IndexError` bei `idx < 1`
    - Wirft `RuntimeError` falls Merge-Restoration silent fail (Re-Read-Assert)

    **Explizit out-of-scope v0.1** (Codex-R1 LOW): Cross-Sheet-Formel-Refs
    werden NICHT automatisch verschoben (openpyxl handhabt nur lokale Refs
    in `ws.insert_rows`-Output). Caller-Verantwortung. Promotion-Trigger:
    Real-Incident wo cross-sheet-Ref nach safe_insert broken zeigt.

    verified via: contract-only, Implementation in Execution-Session.
    """
    ...


def safe_insert_cols(
    ws: Worksheet,
    idx: int,
    amount: int = 1,
) -> None:
    """Spalten-Analog zu `safe_insert_rows`.

    Identische Merge-Preservation-Logik, aber für `ws.insert_cols`.

    verified via: contract-only.
    """
    ...


def safe_save(
    wb: openpyxl.Workbook,
    path: Path,
    profile: Literal["Rebalancing_Tool", "Satelliten_Monitor", "Watchlist_Ersatzbank_Monitor"],
) -> None:
    """Save + Post-Save-Verify via Hook-Funktionen.

    Ruft `wb.save(path)` und delegiert an Hook-Validation via
    `verify_wrapper.verify_after_write(path)` (intern via
    `_load_hook_module().validate_file(...)` — KEIN dotted-Import möglich,
    siehe §4.2 SSoT-Delegation post R1-HIGH-2-Fix).

    Vertrag:
    - Fail-close: wirft `RuntimeError` mit Hook-stderr-Text bei rc != 0
    - Idempotent: kein Side-Effect ausser dem Save selbst
    - Atomisch im Sinne von „save → verify → raise-or-return", kein Rollback bei verify-fail
      (Caller-Verantwortung: VCS-revert oder manueller Fix)

    verified via: contract-only.
    """
    ...
```

**Akzeptanz-Kriterien**:
1. `safe_insert_rows` auf Sheet mit merged Range über `idx` → Range bleibt intakt nach Re-Read (Test: `g_safe_insert_preserves_merges_fixture.xlsx`)
2. `safe_insert_rows(ws, 0)` → `IndexError` (Test: `g_safe_insert_invalid_idx_fixture.xlsx`)
3. `safe_save` mit corrupted post-save xlsx → `RuntimeError` (Test: `g_safe_save_post_corruption_fixture.xlsx`)

### 4.2 `verify_wrapper.py` — Post-Write Re-Validation

**Datei**: `01_Skills/xlsx-smoke-test-runner/verify_wrapper.py`
**Zweck**: Programmatisches Re-Run der Hook-Validation nach openpyxl-Write (§18-Sync-Pfad).
**SSoT-Delegation**: Lädt Hook-Funktionen via `importlib.util.spec_from_file_location` aus absolutem Datei-Pfad `03_Tools/precommit/xlsx_smoke_test.py`. **KEIN regulärer Package-Import möglich** — Verzeichnis startet mit Ziffer + kein `__init__.py` vorhanden (Codex-R1 HIGH-2, verified via Glob `03_Tools/**/__init__.py` 2026-05-25 = nur tests/para18_sync/system_audit haben welche, precommit/ NICHT). Refactor zu shared-module-Package (`tools/precommit_smoke.py` + `__init__.py`) ist v0.2-Pfad — out-of-scope α+ v0.1.

```python
from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
import importlib.util
import sys


def _load_hook_module():
    """Lädt 03_Tools/precommit/xlsx_smoke_test.py via importlib.

    Required weil:
    - `03_Tools/` startet mit Ziffer (kein gültiger Package-Name)
    - `03_Tools/precommit/` hat KEIN __init__.py
    - Standard-Import (`from 03_Tools.precommit...`) wirft SyntaxError

    Pattern aus Standard-Library (importlib.util Doku-Snippet),
    nicht eigene Erfindung. Wirft FileNotFoundError bei fehlendem Hook.

    verified via: Glob `03_Tools/**/__init__.py` 2026-05-25 = 0 Treffer in precommit/.
    """
    hook_path = Path(__file__).resolve().parents[2] / "03_Tools" / "precommit" / "xlsx_smoke_test.py"
    spec = importlib.util.spec_from_file_location("xlsx_smoke_test_hook", hook_path)
    if spec is None or spec.loader is None:
        raise FileNotFoundError(f"Hook-Modul nicht ladbar: {hook_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["xlsx_smoke_test_hook"] = module
    spec.loader.exec_module(module)
    return module


@dataclass(frozen=True)
class VerifyResult:
    """Ergebnis-Container für post-Write-Verifikation.

    Felder:
    - `ok`: bool — True wenn alle Gates §A/§B/§E/§G PASS
    - `profile`: str — auf gelöstes Profil-Key (`Rebalancing_Tool` / ...)
    - `failed_gate`: str | None — z.B. "B" oder "E" oder "G"; None bei ok
    - `detail`: str — Hook-stderr-Text bei fail; leerer String bei ok
    """
    ok: bool
    profile: str
    failed_gate: str | None
    detail: str


def verify_after_write(
    path: Path,
    *,
    run_g: bool = True,
) -> VerifyResult:
    """Run Hook-Validation nach openpyxl-Save.

    Vertrag:
    - Liest `path` read-only via Hook-Funktionen (nie Edit/Write)
    - `run_g`: True = inkludiert §G Sparrate-Σ-Sanity (nur für Satelliten_Monitor)
    - Returns `VerifyResult(ok=False, ...)` bei Hook-rc != 0, NIE Exception (Caller-friendly)
    - Exception nur bei IO-Fehler (FileNotFoundError, PermissionError) — fail-loud

    Use-Case (typisch):
        path = Path("03_Tools/Satelliten_Monitor_v2.0.xlsx")
        wb = openpyxl.load_workbook(path)
        # ... edits ...
        wb.save(path)
        result = verify_after_write(path)
        if not result.ok:
            raise RuntimeError(f"§18-Sync verify FAIL: {result.detail}")

    verified via: contract-only, Hook-Funktion bereits in xlsx_smoke_test.py:79 existent.
    """
    ...


def verify_batch(
    paths: list[Path],
    *,
    run_g: bool = True,
) -> list[VerifyResult]:
    """Batch-Verify mehrerer xlsx (z.B. alle 3 xlsx in einem §18-Sync-Commit).

    Vertrag:
    - Verarbeitet ALLE paths auch bei zwischenzeitlichem Fail (kein early exit)
    - Liefert Result pro path in Eingabe-Reihenfolge
    - Keine Parallelisierung in v0.1 (sequenziell, openpyxl-load ist nicht thread-safe per Spec)

    verified via: contract-only.
    """
    ...
```

**Akzeptanz-Kriterien**:
1. `verify_after_write` auf clean xlsx → `VerifyResult(ok=True, ...)`
2. `verify_after_write` auf xlsx mit injected `#REF!` → `VerifyResult(ok=False, failed_gate="B", ...)`
3. `verify_batch([rebal, sat, watch])` mit Sat-CF-mismatch → 3 Results, Sat hat `ok=False`

### 4.3 Hook-Punkt-G Extension (P8 Variante G)

**Datei (Edit)**: `03_Tools/precommit/xlsx_smoke_test.py`
**Zweck**: Sparrate-Σ-Sanity-Check über config.yaml-Mapping + xlsx-Display-Konsistenz.
**Empirie-Basis**: drift-doc §2.4 — Σ = 7×38 + 1×19 + 4×0 = 285€ ✓

```python
# In xlsx_smoke_test.py einzufügen, NACH _count_cf_rules, VOR validate_file:

def _derive_rate_eur(satellit_cfg: dict) -> int:
    """Mapping config.yaml satellit → Sparrate-EUR.

    Regel (drift-doc §2.4 P8):
    - flag=True                  → 0
    - flag=False + defcon ∈ {3,4} → 38
    - flag=False + defcon == 2   → 19
    - flag=False + defcon == 1   → 0

    Wirft `ValueError` bei unmapped defcon-Wert (defensive).

    verified via: drift-doc §2.4 Empirie-Tabelle 2026-05-25T18:30.
    """
    ...


def _check_g_sparrate_sigma(
    wb: openpyxl.Workbook,
    config_yaml_path: Path,
) -> str | None:
    """§G Sparrate-Σ-Sanity-Check für Satelliten_Monitor.

    Schritte:
    1. Load `config_yaml_path` (yaml.safe_load)
    2. Σ = sum(_derive_rate_eur(s) for s in cfg["satelliten"])
    3. Assert Σ == cfg["brokers"]["scalable"]["sparrate_eur"] (Anker 285.00 €)
       NORMATIVER PFAD post-R1-Fix: `brokers.scalable.sparrate_eur` (L27).
       `portfolio.satelliten_sparrate` existiert NICHT — drift-doc §2.4 + §P8 sind
       parallel zu patchen (Codex-R1 HIGH-1, verified via grep 0-Treffer 2026-05-25).
    4. Assert xlsx K3-Text enthält literal `' Voll'` + `' Eingefroren'` + `'D2-Sockelbetrag'`
    5. Assert xlsx N19-Text == `'→ muss = 285,00 €'`

    Returns:
        None bei PASS
        str (Fehler-Detail) bei FAIL — wird von validate_file an _fail() weitergegeben

    verified via: drift-doc §2.4 + config.yaml L9+L27 2026-05-25T17:31.
    """
    ...


# In validate_file(), nach Punkt E, vor `return 0`, NUR für Satelliten_Monitor-Profil:
#
#     if profil == "Satelliten_Monitor":
#         g_err = _check_g_sparrate_sigma(wb, _CONFIG_YAML_PATH)
#         if g_err is not None:
#             return _fail(path, profil, f"Sparrate-Σ-Drift (Punkt G): {g_err}")
```

**Akzeptanz-Kriterien**:
1. `_derive_rate_eur({"flag": True, "defcon": 3})` → `0`
2. `_derive_rate_eur({"flag": False, "defcon": 3})` → `38`
3. `_derive_rate_eur({"flag": False, "defcon": 2})` → `19`
4. `_derive_rate_eur({"flag": False, "defcon": 5})` → `ValueError`
5. `_check_g_sparrate_sigma` gegen Live-config.yaml + Live-Sat-xlsx → `None` (PASS)
6. Fixture mit gedrehter `flag`-Setting (z.B. APH flag=False) → Σ≠285 → FAIL-String

**Offene Frage (R1 GESCHLOSSEN)**: ~~Anker-Source ist `portfolio.satelliten_sparrate` ODER `brokers.scalable.sparrate_eur`?~~ **Resolved post Codex-R1 HIGH-1**: Anker = `brokers.scalable.sparrate_eur: 285.00` (config.yaml L27). `portfolio.satelliten_sparrate` existiert nicht (grep 0-Treffer 2026-05-25T19:34). drift-doc §2.4 + §P8 müssen separat gepatched werden (siehe §6 Schritt 0).

### 4.4 Hook-Profile-Erweiterung (P13)

**Datei (Edit)**: `03_Tools/precommit/xlsx_smoke_test.py:38-54`
**Zweck**: Sheet-Vollständigkeit über das primäre Sheet hinaus prüfen.

```python
_PROFILES: dict[str, dict] = {
    "Rebalancing_Tool": {
        "scope": "voll",
        "sheets": (
            "Portfolio & Rebalancing",
            "US-Exposure",         # NEU per P13
            "Parameter & Regeln",  # NEU per P13
        ),
        "cf_rule_count": 6,  # md: "249 Formeln + 6 Conditional Formats" (P15 sync)
    },
    "Satelliten_Monitor": {
        "scope": "voll",
        "sheets": (
            "Satelliten Monitor",
            "QuickScreen Ampel",   # NEU per P13
        ),
        "cf_rule_count": 5,  # md: "13 Formeln + 5 Conditional Formats + §G Σ-Check" (P15 sync)
    },
    "Watchlist_Ersatzbank_Monitor": {
        "scope": "minimal",
        "sheets": (),
        "cf_rule_count": 0,
    },
}
```

**Source-Kommentar-Update** (P15 Multi-File-Sync): Z42 `# md: "218..."` → `# md: "249..."`; Z47 `# md: "12..."` → `# md: "13..."`.
**Non-Goal (Codex-R2-F3)**: Q-Spalten-Datum-Drift wird im Hook explizit NICHT geprüft (gehört zu manuellen §C/§D-Checks).

**Profile-Matching Fragilität (Codex-R1 LOW)**: `_resolve_profil` macht aktuell `path.name.startswith(key)` (`xlsx_smoke_test.py:65-67`). Mit den 3 fixen Filename-Prefixen aktuell ohne Kollision, aber bei zukünftigen Renames (z.B. `Rebalancing_Tool_v3.5` + `Rebalancing_Tool_v3.5_archive`) wäre Match ambig. **v0.2-Refactor-Pfad**: regex mit Versions-Capture (`^(Rebalancing_Tool|Satelliten_Monitor|Watchlist_Ersatzbank_Monitor)_v\d+\.\d+\.xlsx$`). Out-of-Scope α+ v0.1.

---

## §5 Test-Fixture-Strategie

**Pattern-SSoT**: `03_Tools/precommit/_fixtures/_generate_fixtures.py` (etabliert per Memory `feedback_cr_convergence_and_project_compat`).

**Regeln**:
- Deterministisch (kein Timestamp, kein Random)
- Byte-exakt reproduzierbar
- Pro Test: 1 valid + 1 invalid Fixture
- **Beschreibende Namen** (KEIN `bad_*`/`good_*` per Memory) — Schema: `<profil>_<gate>_<scenario>_fixture.xlsx`
- Schema-Drift wirft laut (`assert` / `ValueError` statt silent-pass)
- Generator in `01_Skills/xlsx-smoke-test-runner/_fixtures/_generate_fixtures.py`

### 5.1 Fixture-Liste (Pflicht-Set v0.1)

| Datei | Profil | Gate | Scenario | Erwartung |
|-------|--------|------|----------|-----------|
| `rebal_a_open_clean_fixture.xlsx` | Rebal | §A | minimale 3-Sheet-Struktur, 0 Formeln | PASS |
| `rebal_a_open_missing_us_exposure_fixture.xlsx` | Rebal | §A | nur 2 Sheets (kein US-Exposure) | FAIL §A |
| `rebal_b_error_token_in_p5_fixture.xlsx` | Rebal | §B | P5 = `'#REF!'` | FAIL §B |
| `rebal_e_cf_count_mismatch_fixture.xlsx` | Rebal | §E | 5 CF statt 6 | FAIL §E |
| `sat_a_open_clean_fixture.xlsx` | Sat | §A | 2-Sheet-Struktur + 13 Formeln + 5 CF | PASS |
| `sat_a_open_missing_quickscreen_fixture.xlsx` | Sat | §A | nur „Satelliten Monitor"-Sheet | FAIL §A |
| `sat_b_error_token_in_l7_fixture.xlsx` | Sat | §B | L7 = `'#NAME?'` | FAIL §B |
| `sat_e_cf_count_mismatch_fixture.xlsx` | Sat | §E | 4 CF statt 5 | FAIL §E |
| `sat_g_sparrate_mapping_drift_fixture.xlsx` + companion `_config.yaml` | Sat | §G | config flag=False für APH → Σ=323 ≠ 285 | FAIL §G |
| `sat_g_display_drift_fixture.xlsx` | Sat | §G | N19 = `'→ muss = 999,00 €'` | FAIL §G |
| `watch_a_open_clean_fixture.xlsx` | Watch | §A | 1-Sheet, A1 = `'Watchlist'` | PASS |
| `watch_a_open_empty_a1_fixture.xlsx` | Watch | §A | A1 = None | FAIL §A |
| `g_safe_insert_preserves_merges_fixture.xlsx` | n/a | safe_insert | merged Range A1:C3, insert at idx=2 | merges intakt nach Re-Read |
| `g_safe_insert_invalid_idx_fixture.xlsx` | n/a | safe_insert | call safe_insert_rows(ws, 0) | IndexError |
| `g_safe_save_post_corruption_fixture.xlsx` | n/a | safe_save | save dann CF-corrupt | RuntimeError |

**Total**: 15 Fixtures = **12 Profile-Fixtures** (Rebal 4 + Sat 6 + Watch 2) + **3 Skill-Helper-Fixtures** (safe_insert/safe_save). Arithmetik korrigiert post Codex-R1 MED-1 (vorher fälschlich „13+3").
**Generator-Aufwand**: ~150 LOC Python (per `_generate_fixtures.py`-Pattern).

### 5.2 Determinismus-Constraint (Akzeptanz-Kriterium #5)

openpyxl schreibt per default in `docProps/core.xml` die aktuellen Timestamps (`created`/`modified`/`lastModifiedBy`). Das bricht sha256-byte-Diff zwischen zwei Generator-Läufen (Codex-R1 MED-3).

**Pflicht-Mitigation (NORMATIV post R2-MED-1)**: **ZIP-Subset-Hashing** ist verbindlich, weil openpyxl `subject`/`description`/`category`/`revision`/`keywords`/`identifier`/`language`/`contentStatus`/`version` zusätzlich zu created/modified mit Session-Daten befüllen kann (Codex-R2-MED-1). Eine vollständige Core-Properties-Nullung wäre brittle gegen openpyxl-Version-Drift.

```python
import hashlib, zipfile
from pathlib import Path

_EXCLUDED_ZIP_MEMBERS = frozenset({
    "docProps/core.xml",   # Timestamps + creator/lastModifiedBy
    "docProps/app.xml",    # App-Name + Application-Version
})

def fixture_content_sha256(path: Path) -> str:
    """sha256 über ZIP-Subset (ohne docProps-Volatil-Members).

    Output deterministisch für 2 Generator-Läufe gleicher Input-Daten.
    verified via: openpyxl-Version-Test n=3 auf gleichem Workbook,
    erwartet identischer Hash; Test in Execution-Session.
    """
    h = hashlib.sha256()
    with zipfile.ZipFile(path, "r") as zf:
        for name in sorted(zf.namelist()):
            if name in _EXCLUDED_ZIP_MEMBERS:
                continue
            h.update(name.encode("utf-8"))
            h.update(zf.read(name))
    return h.hexdigest()
```

Akzeptanz-Kriterium #5 (§8) wird auf diese Funktion umgestellt — NICHT auf naive `sha256sum file.xlsx`.

verified via: openpyxl `Workbook.properties` API + Codex-R1 MED-3-Finding.

### 5.3 Out-of-Scope-Fixture-Klassen v0.1 (Codex-R1 MED-2)

Explizit nicht abgedeckt, Promotion via Real-Incident:

| Fixture-Klasse | Begründung | Re-Activation-Trigger |
|----------------|------------|----------------------|
| `open_with_repair_prompt` | Excel-Repair-Dialog ist UI-only, openpyxl-Load ignoriert ihn; Hook fail-close greift bereits bei strukturellem Korruption-Subset | Wenn ein User-Edit Excel-Repair-Prompt erzeugt OHNE openpyxl-Load-Exception |
| `shared_string_corruption` | calcChain/sharedStrings re-save-drop ist als benigne bekannt (Memory `feedback_openpyxl_insert_merge_trap`); kein semantischer Daten-Verlust | Wenn ein Sat/Rebal-Sync nach openpyxl-Save User-Sichtbar falsche Strings zeigt |

---

## §6 Implementations-Sequenz (P-Patches Order)

Per drift-doc Sequenzierungs-Regel (post-Substrate-Audit):

| Schritt | Patches | Commit-Typ | Aufwand | Pflicht-Sync |
|---------|---------|------------|---------|--------------|
| 0 | **drift-doc §2.4 + §P8 Pfad-Korrektur** (post R1-HIGH-1) | **gemeinsamer Commit mit Schritt 1** (Drift-Vermeidung, atomarer Patch-State; getrennt NUR bei explizitem `docs(drift)` vs `chore(xlsx-smoke)` Type-Scope-Wunsch) | ~10min (inkl. grep-Verify dass alle `portfolio.satelliten_sparrate`-Occurrences in drift-doc gefunden sind — Aufwand-Korrektur post R2-LOW) | `drift-live-vs-doc.md` Z162-188 + P8-Zeile (Z280) |
| 1 | **P1 + P13 + P15 Multi-File-Sync (4 Files)** | EIN Commit (Vier-Wege-Drift-Vermeidung post Coverage-Gap-Expansion 2026-05-25T20:05) | ~25min | `xlsx-smoke-test.md` L17/L18 + `INSTRUKTIONEN.md §18.7 Z475` + `SYSTEM.md L42 v2.4-Lifecycle-Block` + `xlsx_smoke_test.py Z42/Z47` |
| 2 | P13 Hook-`_PROFILES["sheets"]`-Erweiterung | gleicher Commit wie Schritt 1 | (inkl.) | `xlsx_smoke_test.py:38-54` |
| 3 | P16 PIPELINE-Reference-Klärung | separater Doc-Commit | ~10min | `xlsx-smoke-test.md` §Annex + ggf. `PIPELINE.md` neues Item |
| 4 | Spec write (diese Datei) + Coverage-Matrix-Gate-Check | Spec-Commit | ~45min | `SPEC.md` |
| 5 | `safe_insert.py` Implementation | Code-Commit | ~30min | Skill-Body |
| 6 | Hook-Punkt-G Extension (`_derive_rate_eur` + `_check_g_sparrate_sigma`) | Code-Commit | ~25min | `xlsx_smoke_test.py` |
| 7a | Basis-Fixtures (9 = Rebal/Sat/Watch × §A/§B/§E) | Asset-Commit | ~20min | `_fixtures/` |
| 7b | §G-Fixtures (2 + companion config.yaml) | Asset-Commit | ~15min | `_fixtures/` |
| 7c | safe_insert/safe_save-Fixtures (3) | Asset-Commit | ~15min | `_fixtures/` |
| 8 | Test-Run + Pflicht-Smoke-Test (§18.7) | Verification | ~10min | n/a |
| 9 | Restliche Patches (P2-P12, P14) | Doc-Commits in beliebiger Reihenfolge | ~40min | `xlsx-smoke-test.md` |

**Gesamt**: ~225min ≈ 3.75h post Codex-R1 MED-4-Split (vorher ~210min/3.5h, jetzt detaillierter; Stage-Cut-Logik unverändert).
**Risiko-Mitigation**: Schritte 1+2+3 (Patch-Phase) und 4 (Spec) sind in dieser Session machbar; 5-8 (Implementation) gehören in separate Execution-Session per `feedback_brainstorming_terminal_override_dynastie`.

**Stage-Cut für diese Session**: Schritte 1-4 (Patch-Phase + Spec-Fertigstellung post Codex-R1).
**Stage-Cut für Execution-Session**: Schritte 5-9.

---

## §7 Out-of-Scope (literal aus drift-doc §5)

Folgende Dimensionen sind in v0.1 explizit out-of-scope (verhindert Mis-Interpretation als „vollständige Abdeckung"):

| Dimension | Re-Activation-Trigger |
|-----------|----------------------|
| Cell-Number-Format | A2-datetime falsch in Excel rendert oder Sparrate als String statt Zahl |
| CF-Rules-Identität (nicht nur Count) | CF-Count match aber Färbung falsch (silent CF-Rule-Mutation) |
| Defined Names | Formeln migrieren zu Named-Ranges-Refs |
| Pivot-Tables | Ein Sheet bekommt Pivot-Source |
| Workbook-Protection | Versehentliche Protection-Aktivierung blockiert Smoke-Test |
| Print-Settings | Print-Area falsch → Sparplan-Druck unvollständig |
| Cross-Sheet-Refs systematisch (C4-deferred) | v0.2-Iteration |
| 4-Felder-Annotation-Schema (C5-deferred) | v0.2-Iteration |

**Promotion-Schwelle**: Dimension wird v0.2+ aufgenommen wenn (a) Real-Incident, ODER (b) systematischer User-Edit-Pattern-Drift, ODER (c) Skill-Coverage-Erweiterungs-Bedarf.

**Non-Goal explizit (Codex-R2-F3)**: Q-Spalten-Datum-Drift im Rebal wird NICHT vom Hook geprüft — gehört zu manuellen §C/§D-Checks (P9/P14). Keine falsche Sicherheit erzeugen.

---

## §8 Akzeptanz-Kriterien (Skill-Level)

| # | Kriterium | Verification-Methode |
|---|-----------|---------------------|
| 1 | Alle 3 xlsx-Files passen Hook §A/§B/§E post-P13-Patch | `precommit run xlsx-smoke-test` auf clean repo state |
| 2 | Satelliten_Monitor passt Hook §G post-Punkt-G-Extension | `_check_g_sparrate_sigma` returns None auf Live-config.yaml + Live-Sat |
| 3 | `verify_after_write` korrekt fail-close auf injected `#REF!` | Test-Fixture `sat_b_error_token_in_l7_fixture.xlsx` |
| 4 | `safe_insert_rows` preserved merges nach insert | Test-Fixture `g_safe_insert_preserves_merges_fixture.xlsx` + Re-Read-Assert |
| 5 | 15 Fixtures alle erzeugbar deterministic via Generator | `python _generate_fixtures.py` 2× → `fixture_content_sha256(path)` identisch (§5.2 ZIP-Subset-Hash, NICHT naive sha256sum) |
| 6 | SKILL.md `description` matched drift-doc §0a literal | manueller Diff (Coverage-Matrix-Gate) |
| 7 | Multi-File-Sync P1+P13+P15 in EINEM Commit | `git log --name-only -1` zeigt alle 3 Files |
| 8 | Hook unverändert read-only (kein Schreibpfad) | `grep -E 'wb\\.save|open.*[\"w\"]'` in xlsx_smoke_test.py = 0 Treffer |

---

## §9 Risiken + Mitigationen

| Risiko | Severity | Mitigation |
|--------|----------|-----------|
| ~~§G Anker-Pfad-Drift~~ (R1 HIGH-1 RESOLVED, Pfad = `brokers.scalable.sparrate_eur` L27) | ~~HIGH~~ → CLOSED | Resolved 2026-05-25T19:40 via grep-empirie; drift-doc §2.4 Pfad-Korrektur ist §6 Schritt 0 |
| `safe_insert` Re-Merge nach insert produziert silent off-by-one | MEDIUM | Re-Read-Assert in `safe_save` + Test-Fixture `g_safe_insert_preserves_merges_fixture.xlsx` |
| 3.5h-Aufwand >2.5h-Pipeline-Annahme | MEDIUM | Stage-Cut nach §6 — Patch-Phase + Spec in dieser Session, Implementation separate Session |
| Hook-§G triggert false-positive bei legitimen Config-Updates | MEDIUM | `_check_g_sparrate_sigma` nur für Sat-Profil, nicht universell |
| Test-Fixture-Generator hat Pattern-Drift gegen `_generate_fixtures.py` | LOW | Generator-Code Review im Codex-R1 + Re-Run-Determinismus-Test |
| §G-Hook-Latenz auf pre-commit | LOW | yaml.safe_load + 13-Satelliten-Iteration + Sat-Sheet-Text-Scan (K3/B3/B26/N19) ≈ <50ms-Schätzung (HYPOTHESE, verified via Execution-Session-Bench n=30). Bei >100ms: §G-Cache (yaml-mtime-keyed). |

---

## §10 Verification-Annotations-Manifest

| Behauptung | verified via |
|------------|--------------|
| §1 Skill-Scope literal aus §0a | `drift-live-vs-doc.md:11-27` 2026-05-25T17:31 |
| §2.1 Profile × Capability | drift-doc §1.1 + §2.1 + §3.2 (Sheet-Liste + CF-Count + Pflicht-Cells) |
| §3 Architecture 3-Layer | `xlsx_smoke_test.py:38-54` + drift-doc §Substrate-Status |
| §4.1 `safe_insert` 0 existing Substrate | `Grep safe_insert\|insert_rows...` 2026-05-25T18:15 (drift-doc §Substrate-Status) |
| §4.3 Hook-§G Mapping | drift-doc §2.4 Empirie-Tabelle 2026-05-25T18:30 |
| §4.3 Σ=285 Anker | config.yaml L27 `brokers.scalable.sparrate_eur: 285.00` 2026-05-25T17:33 — NORMATIVE-PFAD post R1 HIGH-1-Fix |
| §4.3 `portfolio.satelliten_sparrate` existiert NICHT | grep `satelliten_sparrate` in config.yaml = 0 Treffer 2026-05-25T19:34 (Codex-R1 HIGH-1) — drift-doc §2.4 hat Pfad-Drift, parallel zu fixen |
| §4.2 `__init__.py` fehlt in `03_Tools/precommit/` | Glob `03_Tools/**/__init__.py` 2026-05-25T19:34 = nur tests/, para18_sync/, system_audit/, system_audit/checks/ (Codex-R1 HIGH-2) |
| §4.3 `satelliten:` Block | config.yaml L116-... (12 Satelliten mit `flag`+`defcon` Feldern) 2026-05-25T19:43 — bestätigt Mapping-Logik §4.3 |
| §4.4 Hook-Profile P13 | drift-doc §4 Hook-Reconciliation + `xlsx_smoke_test.py:38-54` |
| §5 Fixture-Pattern | Memory `feedback_cr_convergence_and_project_compat` + drift-doc §Spec-Phase-Test-Fixture-Constraint |
| §6 Multi-File-Sync P15 | drift-doc P15 + `Grep §18\\.7` in INSTRUKTIONEN.md Z475 2026-05-25T18:15 |
| §7 Out-of-Scope-Liste | drift-doc §5 1:1 |

---

## §11 Memory-Links (Pre-Existing)

- [[feedback_skill_name_is_scope_contract]] — Coverage-Matrix Gate-0 Pflicht
- [[feedback_brainstorming_terminal_override_dynastie]] — Execution = separate Session
- [[feedback_openpyxl_insert_merge_trap]] — AMZN-Bug-Klasse, safe_insert-Substrate
- [[feedback_review_via_codex_not_advisor]] — R1-Sparring statt advisor()
- [[feedback_codex_sparring_heuristic]] — Single-Pass Default, R2 conditional auf HIGH≥2
- [[feedback_xlsx_tools_in_sync_set]] — §18-Sync-Pflicht für Rebal/Sat
- [[feedback_watchlist_xlsx_in_sync_set]] — §18-Sync-Pflicht für Watchlist + §18.7 fail-close
- [[feedback_empirie_statt_annahmen]] — Methodologie: jede Behauptung verified via
- [[feedback_cr_convergence_and_project_compat]] — Fixture-Namens-Disziplin (KEIN bad_*/good_*)
- [[feedback_redefer_over_prespec_dynastie]] — v0.1 vor v0.2-Erweiterung min 2 Real-Runs

---

## §12 Next-Step Sequence

1. **Diese Session**: SPEC.md geschrieben (Status: Draft) → **Codex-Sparring R1**
2. R1-Findings einarbeiten → SPEC.md v0.1.1
3. Multi-File-Sync-Commit (P1+P13+P15) in dieser Session ODER nächster
4. **Session-Cut nach Spec-Finalisierung** — Execution (§4 Implementation) = separate Session

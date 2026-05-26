---
name: xlsx-smoke-test-runner
description: |-
  Post-Write Integritäts-Verifikation für die drei live xlsx-Tools des Dynastie-Depots
  (`03_Tools/Rebalancing_Tool_v3.4.xlsx`, `03_Tools/Satelliten_Monitor_v2.0.xlsx`,
  `03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx`). Library-Mode (kein CLI) —
  importiere `verify_wrapper` + `safe_insert` aus Python.

  **Pflicht-Anwendung — diesen Skill IMMER verwenden, wenn:**
  - eine xlsx-Datei in `03_Tools/` mit `openpyxl` mutiert wurde (Score/FLAG/Sparraten-
    Sync, Watchlist-Update, Rebalancing-Stand-Update, CapEx/FCF-Modell-Edits) und
    der nächste Schritt `git add <xlsx>` wäre — Smoke ZWINGEND vor `git add`,
    fail-close, kein `--force`-Bypass (CLAUDE.md §18.7, INSTRUKTIONEN.md §18.7);
  - openpyxl-Code `ws.insert_rows`/`ws.insert_cols` auf eine Datei mit Merged-Ranges
    aufruft — dann `safe_insert_rows`/`safe_insert_cols` statt nativ (AMZN-
    Merge-Trap-Klasse `feedback_openpyxl_insert_merge_trap`);
  - der User Phrasen wie „smoke-test xlsx", „post-write verify", „re-validate
    xlsx", „xlsx persistiert?", „xlsx-Sync committen" benutzt.

  **Abgrenzung:** Dieser Skill ersetzt keine Score-/Analyse-Workflows (z.B.
  `dynastie-depot`); er ist ausschließlich Post-openpyxl-Verify/Insert-Safety-
  Layer. Bei „Score-Update committen" bleibt `dynastie-depot`/Pipeline-Owner;
  xlsx-smoke-test-runner wird darin als Library-Call eingehängt, nicht als
  konkurrierender Workflow.

  **In-Scope (Skill automatisiert):**
  - §A Open-Repair (Workbook-Load + Sheet-Existenz aller Profile-Sheets)
  - §B Error-Token-Scan (`#REF!`/`#NAME?`/`#VALUE!`/`#N/A` in allen Sheets)
  - §E CF-Rule-Count-Drift-Check pro Profil
  - §G Sparrate-Σ-Sanity (config.yaml-Mapping → Σ-Check gegen Anker 285€ +
    xlsx-Display-Konsistenz K3/B3/B26/N19, nur Satelliten_Monitor)

  **Out-of-Scope (manuell bzw. UI-only — empirisch verifiziert via
  `03_Tools/precommit/xlsx_smoke_test.py` Kommentar L7-8 + SPEC Coverage-Matrix
  §2.2):**
  - §C/§D Pflicht-Cell-Existenz UND -Semantik (Skill prüft beides NICHT;
    Cell-Adressen-Cross-Check passiert manuell per `03_Tools/xlsx-smoke-test.md`)
  - §F Read-only-Close (interaktiv)
  - Cell-Number-Format, CF-Rules-Identität, Defined Names, Pivots,
    Workbook-Protection, Print-Settings

  Erweiterungen über diese Liste hinaus erfordern SPEC-Update + Coverage-Matrix-
  Re-Run; nicht aspirational benutzen.
version: 0.1.0
---

# xlsx-smoke-test-runner v0.1

Tooling-Wrapper um `03_Tools/precommit/xlsx_smoke_test.py` (Pre-Commit-Hook,
Layer 1). Bietet zwei Library-Layer für Inline-Use in §18-Sync-Scripts.

## Wann verwenden

Genau dann, wenn ein Skill/Tool eines der drei produktiven xlsx-Files mit
`openpyxl` schreibt und der Working-Tree-Diff danach committed werden soll.
Der Pre-Commit-Hook fängt Verstöße zwar zusätzlich auf Commit-Zeit ab, der
inline-Aufruf hier liefert aber sofortiges Fail-Signal vor dem Pre-Commit-Lauf
und gibt strukturiertes `VerifyResult` zurück (Profile, fehlgeschlagenes Gate,
Detail) statt nur rc≠0.

## Library-API

### `verify_wrapper` — Post-Write Re-Validation (SPEC §4.2)

```python
from pathlib import Path
import sys
sys.path.insert(0, "01_Skills/xlsx-smoke-test-runner")
from verify_wrapper import verify_after_write, verify_batch, VerifyResult

# Einzeln
r = verify_after_write(Path("03_Tools/Rebalancing_Tool_v3.4.xlsx"))
if not r.ok:
    raise SystemExit(f"FAIL profile={r.profile} gate={r.failed_gate}: {r.detail}")

# Batch (kein early-exit; ALLE Pfade laufen)
results = verify_batch([
    Path("03_Tools/Rebalancing_Tool_v3.4.xlsx"),
    Path("03_Tools/Satelliten_Monitor_v2.0.xlsx"),
    Path("03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx"),
])
```

Vertrag:
- read-only auf das xlsx (Hook delegiert `openpyxl.load_workbook`)
- caller-friendly: Hook-Crash → `VerifyResult(ok=False, failed_gate="UNKNOWN", detail="hook crashed: ...")`, KEINE Exception
- fail-loud nur bei `FileNotFoundError`/`PermissionError` (re-raise)
- Profil-Auto-Resolution per Dateiname (`_PROFILES`-Dict im Hook, SSoT)

### `safe_insert` — openpyxl Insert+Merge-Trap-Schutz (SPEC §4.1)

```python
import sys
from pathlib import Path
sys.path.insert(0, "01_Skills/xlsx-smoke-test-runner")
from safe_insert import safe_insert_rows, safe_insert_cols, safe_save
import openpyxl

wb = openpyxl.load_workbook("03_Tools/Rebalancing_Tool_v3.4.xlsx")
ws = wb["Portfolio & Rebalancing"]
safe_insert_rows(ws, idx=20, amount=1)   # merged Ranges werden preserved
safe_save(wb, Path("03_Tools/Rebalancing_Tool_v3.4.xlsx"), profile="Rebalancing_Tool")
```

Adressiert die `feedback_openpyxl_insert_merge_trap`-Klasse: merged Range
über insert-Zeile schluckt non-anchor-Writes silent. Pattern: unmerge VOR
insert → insert → re-merge aus capture.

`safe_save` ruft post-Write automatisch `verify_after_write` und wirft
`RuntimeError` falls Verify fail-close.

## Pointer (Progressive Disclosure)

| Bedarf | Datei |
|--------|-------|
| Fachlicher Vertrag (Punkt A–G, Profile-Tabelle, Toleranz-Ausnahmen) | `03_Tools/xlsx-smoke-test.md` |
| Function-Signatures + Docstring-Verträge | `verify_wrapper.py` + `safe_insert.py` (Docstrings) |
| Hook-Implementierung (Layer 1) | `03_Tools/precommit/xlsx_smoke_test.py` |
| Test-Fixtures (15 Profile, deterministisch) | `_fixtures/_generate_fixtures.py` |
| Pytest-Suite (54/54 green 2026-05-26) | `tests/` |
| Design-Snapshot (Pre-Release v0.1, lokal/gitignored) | `docs/superpowers/specs/2026-05-25-xlsx-smoke-test-runner-v0.1-design.md` |

## Out-of-Scope (Erinnerung)

§C/§D Pflicht-Cell-Existenz UND -Semantik (Skill prüft beides NICHT —
empirisch verifiziert via `03_Tools/precommit/xlsx_smoke_test.py` L7-8 +
SPEC Coverage-Matrix §2.2), Cell-Number-Format, CF-Rules-Identität, Defined
Names, Pivots, Workbook-Protection, Print-Settings, Read-only-Close (§F),
Cross-Sheet-Formel-Refs nach `safe_insert`. Diese Items sind explizit manuell
bzw. by-design ausgeklammert — siehe Design-Snapshot (`docs/superpowers/specs/
2026-05-25-xlsx-smoke-test-runner-v0.1-design.md` §7, lokal) für Re-Activation-
Trigger.

## Repo-Floor

Python ≥3.14 (`requires-python = ">=3.14"`), ruff `target-version = "py314"`.
Verify-Wrapper nutzt PEP-758 unparenthesized except — bewusst gewählt,
ruff-format würde Klammer-Form aktiv rückgängig machen.

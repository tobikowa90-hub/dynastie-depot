# Session-Handover xlsx-smoke-test-runner Skill (α+ Adaption)

**Stand**: 2026-05-25 ~18:30 (kurz vor Session-Cut wegen Kontext-Voll)

## Resume-Prompt für nächste Session

```
Resume xlsx-smoke-test-runner Skill α+ Spec-Phase.
Drift-Doc Gate-0 fertig + Codex R1+R2 GO-mit-Conditions adressiert.
Pflicht-Lesen vor Spec-Phase-Start: 01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md
Plus _SESSION-HANDOVER.md (diese Datei).
Direkt zu Task #3 (Spec α+ Scope) — Skill-Scope-Statement aus drift-doc §0a literal in SKILL.md description übernehmen.
```

## Was erledigt ist (durable)

| ID | Stand | Pfad |
|----|-------|------|
| context-mode v1.0.124→v1.0.151 | ✅ aktiv (Node 22 via fnm + ctx-upgrade + /reload-plugins) | Memory `reference_context_mode_surrogate_crash_and_fix.md` |
| Drift-Analyse Gate-0 alle 3 xlsx + Hook + config.yaml | ✅ v1.4 16 Patches (8 HIGH + 5 MED + 3 LOW) | `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` |
| Codex R1 GO-mit-Conditions | ✅ 4 von 6 adressiert (C1/C2/C3/C6), 2 deferred (C4/C5) | drift-doc §1.5 + §4 + §5 + Sequenz-Regel |
| Codex R2 Diff-Re-Review | ✅ 5 Findings, alle adressiert (F1/F3/F4/F5 trivial, F2 via Variante-G) | drift-doc P8 + P13 + §5 + §0a |
| P8-Entscheidung empirisch validiert | ✅ Variante G (config.yaml SSoT + Hook-Logik), Σ=285€ MATCH | drift-doc §2.4 + P8-Zeile |
| Substrate-Audit (4 Schritte) | ✅ INSTRUKTIONEN/PIPELINE/safe_insert-Substrate/_fixtures | drift-doc P15 + P16 |
| Primary-Session-Rekonstruktion | ✅ Option α+ + Adaption verified | drift-doc Header |

## Tasks-State

- **#3 pending** — Spec α+ schreiben (Verify-Wrapper + safe_insert.py Helper)
- **#7 pending** — PIPELINE-Items C4 (Cross-Sheet-Refs systematisch) + C5 (4-Felder-Schema) für v0.2

## Kritische Befunde der Session (vor Spec wichtig)

1. **Variante G Mapping-Empirie**:
   - Mapping aus config.yaml: `flag=True→0€`, `flag=False+defcon∈{3,4}→38€`, `flag=False+defcon=2→19€`
   - Live-Test (12 Satelliten): 7×38 + 1×19 + 4×0 = 285€ ✅
   - Variante F (SEARCH auf N-Spalte-Freitext) failed: Σ=95€ weil 5 Tickers `'● Halten | ...'` haben statt `'● Volle Rate 38'`
   - **Lesson**: config.yaml > Freitext-Parsing in Excel

2. **3 Doku-Files haben identischen Formel-Count-Drift** (P15 Multi-File-Sync):
   - `xlsx-smoke-test.md` Scope-Tabelle
   - `00_Core/INSTRUKTIONEN.md §18.7 Z475`
   - `03_Tools/precommit/xlsx_smoke_test.py` Z42/Z47-Kommentare
   - Alle 3 zitieren „218 Formeln + 6 CF; 12 Formeln + 5 CF" → Live ist 249 / 13
   - **Sync-Pflicht**: müssen in EINEM Commit gepatched werden

3. **safe_insert.py hat 0 existing Substrate** im Repo (Grep verifiziert) → Neubau in Spec, kein Duplicate-Risiko

4. **PIPELINE.md hat KEIN „Watchlist-Tool-Update"-Item** trotz Doku-Referenz → P11/P16 Re-Phrase nötig

5. **`_generate_fixtures.py` Pattern muss Skill adopten**: deterministisch + beschreibende Namen (nicht `bad_*`/`good_*`) + 1 valid + 1 invalid pro Test

## Spec-Phase Vorbereitung (Task #3 Start-Punkt)

**α+ Scope** (User-confirmed):
- **Verify-Wrapper**: Post-Write-Verifikation um xlsx-Schreiboperationen
- **`safe_insert.py` Helper**: AMZN-Bug-Klasse-Prävention (openpyxl insert+merge trap)
- Pipeline-Aufwand ~2.5h

**α+ Adaption** (User-Pflicht):
- Dry-runs gegen Live-State so weit/tief wie möglich
- Jede Spec-Annahme bekommt `verified via:`-Annotation (Mindeststandard v0.1: `sheet!cell + timestamp`)
- KEIN „Core Slim Refactor 2.0"

**SKILL.md FIRST-DELIVERABLE**: Capability-Scope-Statement aus drift-doc §0a literal in `description` übernehmen (NICHT aspirational).

**Implementations-Sequenz** (per Sequenzierungs-Regel):
1. P1+P13+P15 Multi-File-Sync (in EINEM Commit)
2. P13 Hook-Profile-Erweiterung
3. P16 PIPELINE-Reference-Klärung
4. Spec schreiben (mit Coverage-Matrix-Check gegen drift-doc §0a)
5. safe_insert.py Implementation
6. Hook-Erweiterung um „Punkt G Sparrate-Σ-Sanity"
7. Voll-Scope-Fixtures generieren (Rebal + Sat, beschreibende Namen)
8. Test-Run + Smoke-Test

## Memory-State (was diese Session geschrieben hat)

- `reference_context_mode_surrogate_crash_and_fix.md` ergänzt im MEMORY.md Index

## Cross-Reference Pfade

- Drift-Doc: `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` (16 Patches, 6 Sections)
- Soll-Doku: `03_Tools/xlsx-smoke-test.md` (zu patchen P1-P12)
- Anker-Top-Level: `00_Core/INSTRUKTIONEN.md §18.7` (zu patchen P15)
- Hook: `03_Tools/precommit/xlsx_smoke_test.py` (zu patchen P13)
- Test-Fixture-Pattern: `03_Tools/precommit/_fixtures/_generate_fixtures.py`
- config.yaml: `01_Skills/dynastie-depot/config.yaml` (SSoT für Variante G Mapping)
- Live-xlsx: `03_Tools/Rebalancing_Tool_v3.4.xlsx`, `03_Tools/Satelliten_Monitor_v2.0.xlsx`, `03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx`

# Session-Handover xlsx-smoke-test-runner Skill (α+ Adaption)

**Stand**: 2026-05-25 ~20:45 (Session-Cut nach Klasse-D §D-Block-Rewrite COMPLETE + Push `ecf3b12`)

## Resume-Prompt für nächste Session

```
Resume xlsx-smoke-test-runner Stage-2 Execution (SPEC §6 Schritte 5-8).
SPEC v0.1 GO-Ready + Klasse-D §D-Block-Rewrite committed+pushed (ecf3b12). Substrate vollständig.
Pflicht-Lesen: SPEC.md §6 Schritte 5-8 + drift-live-vs-doc.md §2.4 (Variante G Mapping-Regel).
Direkt zu Stage-2 in fixer Reihenfolge:
  Schritt 5 — safe_insert.py Implementation (AMZN-Bug-Klasse, openpyxl insert+merge trap, ~30min, ~80 LOC)
  Schritt 6 — Hook-§G Extension in 03_Tools/precommit/xlsx_smoke_test.py (_derive_rate_eur + _check_g_sparrate_sigma, ~25min, ~30 LOC)
  Schritt 7 — 15 Test-Fixtures Generator (7a/7b/7c-Split, deterministisch, beschreibende Namen — KEIN bad_*/good_*-Pattern, ~50min)
  Schritt 8 — Test-Run + §18.7 xlsx-Smoke-Test gegen alle 3 Live-Files (~10min)
TDD-Disziplin pro Sub-Task (Test vor Implementation). Codex-Single-Pass Diff-Review nach Schritt 5+6 vor Commit. Substrate ist gereviewt, kein eigener Spec-Pass nötig.
```

## Session-Output 2026-05-25 (durable in Repo, Commits d10b63d + 369b476 + ecf3b12)

| Artefakt | Stand | Notiz |
|----------|-------|-------|
| `01_Skills/xlsx-smoke-test-runner/SPEC.md` | 635 LOC, GO-Ready | Post 2× Codex-Sparring (R1: 2 HIGH + 4 MED + 4 LOW; R2: 0 HIGH + 3 MED + 1 LOW), alle Findings adressiert |
| `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` | 16 Patches + R1+R2 + Coverage-Expansion + RESOLVED-Marker | Substrate für Klasse D (jetzt vollständig konsumiert) |
| `01_Skills/xlsx-smoke-test-runner/_SESSION-HANDOVER.md` | (diese Datei, post-Stage-2-Cut-Update) | Resume-Pointer für Stage-2 Execution |
| Multi-File-Sync 4 Files | INSTRUKTIONEN §18.7 + SYSTEM L42 + xlsx-smoke-test.md L17/L18 + Hook Z42/Z47 | Formel-Counts 218→249, 12→13 + Anker-Pfad-Korrektur |
| `03_Tools/xlsx-smoke-test.md` Klasse-D §D-Block-Rewrite | **NEU 2026-05-25 20:45** committed `ecf3b12` (+37/-8) | P6+P7+P8+P9+P10+P14+P16 + §E-Beispiel-Fix; 20/20 empirisch verifiziert |
| `01_Skills/dynastie-depot/config.yaml` L70-78 | post-AMZN Sparraten-Kommentar | 3× → 4× eingefroren, Math 285€ identisch |
| log.md | system-zustand-Eintrag | Spec-Phase + Multi-File-Sync dokumentiert |
| Memory `feedback_historical_snapshot_not_a_scope_excuse.md` | NEU | Lifecycle-Snapshot ≠ Scope-Reduktions-Argument |

## Was als nächstes erledigt werden muss (priorisiert)

### ✅ 1. Klasse D — xlsx-smoke-test.md §D-Block-Rewrite (DONE 2026-05-25, commit `ecf3b12`)

Alle Klasse-D-Patches angewendet und empirisch verifiziert (20/20 PASS via `openpyxl.load_workbook` gegen 3 Live-xlsx):

| Patch | Section | Live-Verification |
|-------|---------|-------------------|
| P6 | §D B24↔B25 Swap | ✅ B24 enthält `[~]/[V]/[TC]`-Legende, B25 enthält EINGEFROREN-Liste |
| P7 | §D B26 Pflicht-Zelle | ✅ Volle Rate 38€ + D2-Sockel 19€ + Eingefroren + Nenner-Aufteilung |
| P8 | §D Σ-Check zu Hook-§G | ✅ N19=`'→ muss = 285,00 €'` literal, kein `=`-Prefix |
| P9 | §D2 QuickScreen-Ampel-Sheet | ✅ B5:I5 8 Headers + B6:B17 12 Ticker (Set-Eq Hauptsheet) + B19 'LEGENDE' + B20:B23 |
| P10 | ●-Status-Marker | ✅ K3 + Konvention-Note + alle Sat-Pflicht-Cells |
| P14 | §C US-Exposure-Sentinel-Set | ✅ R4+R20 Mirror (no #REF!), E21 SUM, B25→Parameter!B11 |
| P16 | §Annex Watchlist Re-Phrase | ✅ file-pattern-Trigger, kein PIPELINE-Backing |
| §E | Stichprobe-Beispiel-Fix (collateral) | ✅ B25-Referenz entfernt |

**Output**: commit `ecf3b12` (+37/-8, 1 File), gepusht zu origin/main.

### 2. Stage-2 Execution (NEUE SESSION, per `feedback_brainstorming_terminal_override_dynastie`)

**SPEC §6 Schritte 5-8** in fixer Sequenz:

| Schritt | Task | LOC | Zeit |
|---------|------|-----|------|
| 5 | `safe_insert.py` Implementation — AMZN-Bug-Klasse-Prevention (openpyxl insert+merge trap), unmerge VOR insert → re-merge aus Original-Capture | ~80 LOC | ~30 min |
| 6 | Hook-§G Extension in `03_Tools/precommit/xlsx_smoke_test.py` — `_derive_rate_eur(flag, defcon)` + `_check_g_sparrate_sigma()`; Mapping aus config.yaml, Cross-Check Σ == `brokers.scalable.sparrate_eur` (285€) | ~30 LOC | ~25 min |
| 7 | 15 Test-Fixtures Generator (`_generate_fixtures.py`-Pattern adopten) — 7a Rebal-Fixtures, 7b Sat-Fixtures, 7c Watchlist-Fixtures. Beschreibende Namen (NICHT `bad_*`/`good_*` per Memory `feedback_cr_convergence_and_project_compat`). 1 valid + 1 invalid pro Test-Klasse. | Generator + 15 xlsx | ~50 min |
| 8 | Test-Run + §18.7 xlsx-Smoke-Test gegen alle 3 Live-Files | — | ~10 min |

**Disziplin**:
- TDD pro Sub-Task (Test vor Implementation)
- Codex-Single-Pass Diff-Review nach Schritt 5 (safe_insert) und Schritt 6 (Hook-§G) vor Commit
- Substrate ist gereviewt — kein eigener Spec-Pass nötig
- Cross-Check Skill-vs-Standalone (per Memory `feedback_cross_check_skill_vs_standalone`) bei Hook-§G

**§18-Sync-Awareness**: Hook-Extension berührt `03_Tools/precommit/xlsx_smoke_test.py` — NICHT im §18-Trigger-Pattern (kein PORTFOLIO/SYSTEM/CORE-MEMORY/log/xlsx-Touch). Standard Doku-Commit ohne `paragraph-18-sync`.

## Cross-Reference (für Resume)

- SPEC: `01_Skills/xlsx-smoke-test-runner/SPEC.md` (§6 Schritte 0-9 Sequenz)
- Drift-Doc: `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` (§2.2 + §2.4 Soll-Werte)
- Soll-Doku (Patch-Target Klasse D): `03_Tools/xlsx-smoke-test.md` L77-85
- Hook: `03_Tools/precommit/xlsx_smoke_test.py` (jetzt Z42/Z47 sync)
- config.yaml: `01_Skills/dynastie-depot/config.yaml` (L27 Anker, L70-78 Sparraten-Kommentar)
- Codex-Threads: R1 `task-mplhql8t-klqd0v` resumable, R2 `aee23b12f73d5f502`
- Memory: `feedback_historical_snapshot_not_a_scope_excuse` + `feedback_skill_name_is_scope_contract` + `feedback_codex_sparring_heuristic`

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

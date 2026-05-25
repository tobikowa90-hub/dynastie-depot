# Session-Handover xlsx-smoke-test-runner Skill (α+ Adaption)

**Stand**: 2026-05-25 ~20:30 (Session-Cut nach SPEC-COMPLETE + Multi-File-Sync-Commit `d10b63d`)

## Resume-Prompt für nächste Session

```
Resume xlsx-smoke-test-runner Klasse-D §D-Block-Rewrite (SPEC §6 Schritt 9).
SPEC v0.1 GO-Ready + Multi-File-Sync committed (d10b63d). Substrate stabil.
Pflicht-Lesen: SPEC.md + drift-live-vs-doc.md §2.2 + §2.4 (Soll-Werte).
Direkt zu xlsx-smoke-test.md §D-Block-Rewrite: P6 (B24↔B25 Swap) + P7 (B26 neue Pflicht-Cell) + P8 (Σ-Check-Paradigma zu Hook via Variante G) + P10 (●-Status-Marker-Vereinheitlichung).
Inline-Übernahme aus drift-doc (Substrate ist Codex-R1+R2 gereviewt) — kein eigener Codex-Pass nötig sofern strikt §2.2 + §2.4 Werte verwendet.
```

## Session-Output 2026-05-25 (durable in Repo, Commit d10b63d)

| Artefakt | Stand | Notiz |
|----------|-------|-------|
| `01_Skills/xlsx-smoke-test-runner/SPEC.md` | 635 LOC, GO-Ready | Post 2× Codex-Sparring (R1: 2 HIGH + 4 MED + 4 LOW; R2: 0 HIGH + 3 MED + 1 LOW), alle Findings adressiert |
| `01_Skills/xlsx-smoke-test-runner/drift-live-vs-doc.md` | 16 Patches + R1+R2 + Coverage-Expansion + RESOLVED-Marker | Substrate für Klasse D |
| `01_Skills/xlsx-smoke-test-runner/_SESSION-HANDOVER.md` | (diese Datei, post-Cut-Update) | Resume-Pointer für D |
| Multi-File-Sync 4 Files | INSTRUKTIONEN §18.7 + SYSTEM L42 + xlsx-smoke-test.md L17/L18 + Hook Z42/Z47 | Formel-Counts 218→249, 12→13 + Anker-Pfad-Korrektur |
| `01_Skills/dynastie-depot/config.yaml` L70-78 | post-AMZN Sparraten-Kommentar | 3× → 4× eingefroren, Math 285€ identisch |
| log.md | system-zustand-Eintrag | Spec-Phase + Multi-File-Sync dokumentiert |
| Memory `feedback_historical_snapshot_not_a_scope_excuse.md` | NEU | Lifecycle-Snapshot ≠ Scope-Reduktions-Argument |

## Was als nächstes erledigt werden muss (priorisiert)

### 1. Klasse D — xlsx-smoke-test.md §D-Block-Rewrite (kleiner Doku-Patch, ~15-30min)

**File**: `03_Tools/xlsx-smoke-test.md` Zeilen 77-85 (§D Satelliten Pflicht-Zellen + PASS-Criteria + CF-Stichprobe)

**Pflicht-Patches** (Soll-Werte literal aus `drift-live-vs-doc.md` §2.2 + §2.4):
- **P6**: Tabellen-Row L77 = `B24 | Footer Eingefroren-Liste` → ist falsch; B24 ist **Legende** `[~]/[V]/[TC]`. SWAP mit L78.
- **P6**: Tabellen-Row L78 = `B25 | Footer Volle-Rate-Liste | Mit Σ-Check-Formel` → ist falsch; B25 ist **Eingefroren-Liste**.
- **P7**: NEU `B26 | Footer Volle-Rate-Liste + Nenner-Aufteilung` als Pflicht-Cell (User-Erweiterung 2026-05-25).
- **P8**: PASS-Criteria L80 `Σ-Check-Formel im Footer B25 resolvet ohne Fehler` → Variante G: Σ-Check ist Text-Sanity in N19 (`'→ muss = 285,00 €'`), KEINE Excel-Formel; PASS-Kriterium an Hook-§G delegiert (post Skill-Execution-Stage).
- **P9**: QuickScreen-Ampel-Sheet als §D2 oder Sub-Section ergänzen (R5 Headers + R6-R17 Ticker-Konsistenz gegen Satelliten R7-R18 + R19+ Legende).
- **P10**: ●-Status-Marker-Vereinheitlichung dokumentieren (vs alte Doku 🟢/🟡/🟠/🔴).
- **P14**: US-Exposure-Sentinel-Set in §C aufnehmen (R4+R20 Mirror + R21 E Σ + R25 B Cross-Ref auf Parameter!B11).
- **P16**: §Annex-Reference auf nicht-existentes PIPELINE-Item — entweder konkrete Item-ID nachziehen ODER „Logik" → „Formeln (`=...`)" Re-Phrase ohne PIPELINE-Backing.

**Empfohlener Modus**: Inline-Patch direkt, kein Codex-Sparring (Substrate ist gereviewt). Falls Unsicherheit → Single-Pass R1 auf den Diff.

### 2. Stage-2 Execution (separate Session pflicht per `feedback_brainstorming_terminal_override_dynastie`)

SPEC §6 Schritte 5-9:
- `safe_insert.py` Implementation (Body, ~30min)
- Hook-Punkt-G Extension (`_derive_rate_eur` + `_check_g_sparrate_sigma`, ~25min)
- 15 Fixtures Generator + Generierung (~50min via 7a/7b/7c-Split)
- Test-Run + §18.7-Smoke-Test (~10min)

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

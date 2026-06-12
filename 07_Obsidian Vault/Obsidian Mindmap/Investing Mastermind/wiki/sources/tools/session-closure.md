---
title: "session-closure (Skill)"
type: source
medium: tool
aliases:
  - "session-closure"
  - "Session-Closure"
  - "!SessionClose"
tags: [skill, workflow, session-management, governance, safety-boundary]
created: 2026-05-21
updated: 2026-05-22
sources: [session-closure]
related: [dynastie-depot-skill, paragraph-18-sync]
---

# session-closure (Skill v0.2.0)

## Rolle

Autonome Session-Closure-Sequenz — orchestriert standardisierten Abschluss einer Dynastie-Depot-Session inkl. §18-Sync-Check, Commit-Staging, Pre-Commit-Diff-Inspection und atomarem Commit. **Hard-Stop vor push** — User-Entscheidung zum Push bleibt manuell.

## Aktivierung

**Strict-Trigger:** `!SessionClose` (literal, kein Fuzzy-Match — gemäß Routing-Table-Konvention)

Kein anderer Aufruf-Pfad. Generische Phrasen wie "Session abschließen", "Sync machen", "commit" sind KEIN Aktivierungsgrund.

## Sicherheits-Boundary

**fail-close** — bei Validierungsfehler, fehlgeschlagenem Pre-Commit-Hook oder unklarer Sync-Set-Zuordnung bricht der Skill ab statt zu raten. Kein `--force`/`--no-verify`-Bypass.

## SSoT / Boundary-Verträge

- **Normativ:** [[INSTRUKTIONEN-md|`00_Core/INSTRUKTIONEN.md` §25.5]] Session-Closure-Workflow
- **§18-Sync-Set-Determinant:** §18.1 (Event-Klassifikation) + §18.2 (Multi-Event-Union)
- **Pre-Commit-Substrate:** `.pre-commit-config.yaml` (crlf-guard, ruff, validate-score-history, validate-flag-events, xlsx-smoke-test)

## Pfad zur Quelldatei

`C:\Users\tobia\OneDrive\Desktop\Claude Stuff\01_Skills\session-closure\`

6 Files (799 Z. Stand v0.2.0):

- `SKILL.md` — Hauptlogik + Strict-Trigger-Definition
- `references/` — Sub-Konventionen + Sync-Set-Tabellen
- Spec-Review-Trail in `docs/superpowers/specs/` (gitignored, lokal)

## Deployment-Status

- **v0.2.0 deployed 2026-05-21** (commit `42eca7c`)
- **Spec-Review:** Gemini-Single-Pass H1-H4 appliziert (Codex auth-blockiert vor Errata-Fix 21.05. ~23:30; Codex ab Build-Sessions wieder regulär — siehe Memory `feedback_review_via_codex_not_advisor`)
- **Anker im SSoT 22.05.:** [[INSTRUKTIONEN-md|`00_Core/INSTRUKTIONEN.md` §25.5]] verankert

## Sync-Set bei Aktivierung (typisch)

Variiert je Event-Klasse (§18.1). Score-Event-Sync-Set:

- `PORTFOLIO.md` + `Faktortabelle.md` + `CORE-MEMORY.md` (§12 + §13) + Vault `log.md`
- `score_history.jsonl` (via [[backtest-ready-forward-verify]] Schritt 7)
- `flag_events.jsonl` (via `03_Tools/backtest-ready/archive_flag.py`)
- `01_Skills/dynastie-depot/config.yaml`
- `03_Tools/Rebalancing_Tool` + `Satelliten_Monitor` (+ §18.7-Smoke pflicht)

System-Event-Sync-Set: PIPELINE.md + STATE.md + SYSTEM.md + Vault log.md + ggf. CORE-MEMORY §13.

## Skill-Backlog-Kontext (PIPELINE #73)

Identifiziert als Top-Skill-Kandidat #1 (vor `xlsx-smoke-test-runner` und `paragraph-18-sync`). Reinfall-Belege motivierten Skill-Bau:

- §18-Sync-Anchor-Promotion-Gaps
- Pre-Commit-Diff-Inspection-Lücken
- xlsx-Tools-Out-of-Sync-Vorfälle (mehrere Reinfälle in Spec-/Build-Plan-Pässen)

## Verwandte Skills & Pages

- [[dynastie-depot-skill]] — primärer Vollanalyse-Workflow (ruft session-closure NICHT programmatisch — User-getriggert)
- [[backtest-ready-forward-verify]] — Persistenz-Pipeline-Satellit (von dynastie-depot programmatisch aufgerufen)
- [[paragraph-18-sync]] (Spec v0.3 Build-ready, PIPELINE #73a) — Schwester-Skill für §18-Sync-Orchestrierung (Build deferred zu separater Session)
- [[INSTRUKTIONEN-md|§25.5]] — normative Session-Closure-Definition

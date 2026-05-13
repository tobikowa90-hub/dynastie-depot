# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort **`00_Core/STATE.md` (Hub) und `00_Core/PORTFOLIO.md`** — ohne Rückfrage. Hub gibt Navigation + Critical-Alert; PORTFOLIO ist der Live-State für 90% der Sessions (Scores, DEFCON, FLAGs, Sparraten, Trigger, Watches).

Danach: kompakte Zusammenfassung (max. 10 Zeilen). **`dynastie-depot`-Skill NICHT auto-laden** — nur lazy via Routing-Table-Trigger (`!Analysiere`/`!QuickCheck`/`!Rebalancing`/`!Briefing`/`!CAPEX-FCF-ANALYSIS`) oder expliziter User-Aufforderung. Begründung: Default-Session = Pipeline/Strategie/Wiki/Tools-Engineering ohne Skill-Bedarf; eager-load kostete ~10-15k Tokens pro non-Analysis-Session. Spec-Lücke 09.05.2026 geschlossen via TOKEN-RULES.md "Skills lazy-load"-Bullet + SKILL.md-Frontmatter-Verengung. Bei Unsicherheit lieber Routing-Table-Match prüfen statt eager laden.

## Verhalten

- `00_Core/CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Code-Verhalten (Karpathy-Regeln):** Bei Code-/File-Edit-Operationen gelten Think-Before-Coding, Simplicity-First, Surgical-Changes, Goal-Driven-Execution, **Pre-Refactor-Caller-Scan** (`Grep` auf Symbol vor Edit bei externen Aufrufern) und **Approach-Reset-Schwelle** (nach 2 identischen Failed-Attempts: Stop → Codex-Sparring / Plan-Wechsel / User-Konsultation). Detail: `INSTRUKTIONEN.md §0`. Nicht verbindlich für Markdown-Sync und Wiki-Operationen.
- **Sync-Pflicht (§18 v2.4):** Trigger-basiertes Event-Mapping. Score/FLAG/Sparraten-Change → log.md + CORE-MEMORY.md + Faktortabelle + **PORTFOLIO.md** + score_history.jsonl + **`01_Skills/dynastie-depot/config.yaml`** + **`03_Tools/Rebalancing_Tool_v3.4.xlsx`** + **`03_Tools/Satelliten_Monitor_v2.0.xlsx`** (+ ggf. flag_events.jsonl), alles in einem git-Commit (xlsx-Tools können separater Tool-Commit sein, aber gleiche Session pflicht). Pipeline-Item → PIPELINE.md + log.md. System-Zustand-Change → SYSTEM.md + log.md. Multi-Event-Aktionen = Union der Sets. **score_history.jsonl-Write** via Skill `backtest-ready-forward-verify` (v1.0.1, seit dynastie-depot v3.7.3 Schritt 7). **flag_events.jsonl** CLI-direkt via `03_Tools/backtest-ready/archive_flag.py`. **config.yaml** manuell sync auch ohne FLAG-Change (Lücke 25.04. nach 7-Tage-Drift TMO 23.04. gefixt — siehe §18 v2.0→v2.1). **xlsx-Tools** via `openpyxl` manuell sync — User-Direktive 28.04. spätabends (v2.2→v2.3): xlsx ist operative Zero-Token-Lookup-Quelle für Sparpläne + Depot-Übersicht. **xlsx-Smoke-Test §18.7 (v2.4 seit 11.05.2026):** nach jedem `openpyxl`-Write Pflicht-Smoke-Test gemäß `03_Tools/xlsx-smoke-test.md` (6-Punkte-Manual-Check + Excel-Fallback) vor `git add` der xlsx-Files; fail-close, kein `--force`-Bypass.
- **Earnings-Call-Wait-Discipline (§19.1, NEU 28.04. spätabends post V Q2 Reinfall):** Klasse-B-Vollanalyse läuft strikt **Tag +1 morgens nach Earnings Call**, nicht Tag 0. Tag 0 = `_extern/earnings-recap`-Skill für Press-Release-Recap + manueller FLAG-Quick-Check (FLAG-Trigger/Resolve via `archive_flag.py` sofort, Score unverändert) + Pre-Call-Snapshot in CORE-MEMORY §12.<ticker>. Score-Move + 8-File-Sync ausschließlich am Tag +1 mit Transcript-Read via defeatbeta-MCP. Outlier-Bypass: Tag-0-FLAG-Event ja, Score-Move nein. Detail INSTRUKTIONEN §19.1 + Memory `feedback_earnings_call_wait_discipline.md`.
- **Briefing-Sync:** Vor Session-Ende `!SyncBriefing` falls 00_Core/ geändert wurde (§25). SessionEnd-Hook warnt automatisch.
- **Remote-Control (User-Trigger):** Wenn User `remote-Control` eingibt (oder sinngemäße Phrase „remote weiter"/„mobile weiter"), Remote-Routine mit State-Snapshot via `ccr` spawnen (Memory remote-trigger-api.md). Sonst kein automatischer Prompt — User-gesteuert, Zero-Overhead. Spawn-Mechanismus + Kontext-Scope final am Konsolidierungstag 24.04. festlegen.

## Kontinuierliches Lernen

| Tier | Speicherort | Wer schreibt | Wann gelesen | Pflege |
|------|------------|--------------|-------------|--------|
| 1. Auto-Memory | ~/.claude/.../memory/*.md | Claude automatisch | Session-Start | Auto-Dream konsolidiert |
| 2. Applied Learning | `00_Core/APPLIED-LEARNING.md` | Manuell bei Review | On-Demand (per Routing-Table) | Monatlich + Kurator-Regel |
| 3. Formelle Regeln | `00_Core/INSTRUKTIONEN.md` §§ | Bei bewiesenem Bedarf | Per Routing-Table | Bei Systemänderungen |

Bullets, Pflege-Regeln, Promotion-Logik, Historie: siehe `00_Core/APPLIED-LEARNING.md`.

## Projektstruktur

- `00_Core/` — Kontext, Instruktionen, Gedächtnis (STATE, CORE-MEMORY, INSTRUKTIONEN, RETROSPECTIVE-GATE, APPLIED-LEARNING, TOKEN-RULES, KONTEXT, Faktortabelle, SESSION-HANDOVER)
- `01_Skills/` — dynastie-depot · backtest-ready-forward-verify · insider-intelligence · non-us-fundamentals · quick-screener · sec-edgar-skill · `_extern/` (read-only)
- `02_Analysen/` — DEFCON-Analysen als Excel
- `03_Tools/` — Rebalancing · Satelliten-Monitor · Watchlist · Briefing-Hook · system_audit
- `04_Templates/` — Pointer + spezifische Templates (z.B. `04_Templates/CAPEX-FCF-ANALYSE.md` zeigt auf `01_Skills/dynastie-depot/capex-fcf-template.md` v4.0)
- `05_Archiv/` — Historische Dateien
- `06_Skills-Pakete/` — Installierbare ZIP-Skills
- `07_Obsidian Vault/` — Wiki (71 Notes, Schema + Workflows via WIKI-SCHEMA.md)

## Routing-Table

> STATE.md + PORTFOLIO.md immer. **Match-Regel (Hybrid):** exakte Trigger strikt; bare Ticker → `!QuickCheck`; Mehrfach-Match = Union der Lies-Spalten. Bei Trigger-Miss: konservativ mehr laden.

| Trigger | Lies zusätzlich | Skippe | Skill-Call |
|---------|-----------------|--------|------------|
| `Session starten` (default) | (Resume-Fall: SESSION-HANDOVER.md) | PIPELINE, SYSTEM, CORE-MEMORY, INSTRUKTIONEN, KONTEXT, Faktortabelle, Wissenschaftliche-Fundierung-DEFCON | — |
| `!Analysiere <Ticker>` | INSTRUKTIONEN.md, Faktortabelle.md, …/synthesis/Wissenschaftliche-Fundierung-DEFCON.md | KONTEXT, CORE-MEMORY (außer §5 bei Scoring-Edge-Case) | `dynastie-depot` + `backtest-ready-forward-verify` (Schritt 7, programmatisch) |
| `!QuickCheck <Ticker>` | Faktortabelle.md | INSTRUKTIONEN, KONTEXT, CORE-MEMORY, Wiss-Fundierung | `quick-screener` |
| `!Rebalancing` | INSTRUKTIONEN.md, KONTEXT.md | CORE-MEMORY, Faktortabelle, Wiss-Fundierung | — |
| `!SyncBriefing` | INSTRUKTIONEN.md (§25) + SYSTEM.md §Briefing-Status (nur wenn Briefing-Version/Deploy-Status seit letztem Sync geändert) | alle anderen | — |
| Wiki-Ops (`ingest`/`lint`/`query`, „Vault"/„Obsidian"/„Faktortabelle-Edit"/„Score-Update"/„Insider scan"/„entity"/„Satellit Seite") | `07_Obsidian Vault/.../WIKI-SCHEMA.md` | INSTRUKTIONEN, KONTEXT, CORE-MEMORY (außer Wiki-Bezug) | je nach WIKI-SCHEMA-Workflow (`insider-intelligence`, `non-us-fundamentals`, …) |
| `remote-Control` / „mobile weiter" | Auto-Memory remote-trigger-api.md | alles andere (Snapshot reicht) | — (User-getriggerter `ccr`-Spawn) |
| Konsolidierungstag / System-Audit / Backlog-Review | SESSION-HANDOVER.md, STATE.md (Hub für Critical-Alerts + Last-Audit-Block) + PIPELINE.md + SYSTEM.md | KONTEXT, Faktortabelle (außer ticker-spezifisch) | `SystemAudit` (slash) bei Audit-Lauf |
| Strategie-/Allokations-Frage | KONTEXT.md | Faktortabelle, Wiss-Fundierung | — |
| Code-Edit-Session ohne anderen Trigger (z.B. „fix bug in X.py", „refactor Y") | INSTRUKTIONEN.md (§0 zuerst lesen) | alle anderen Pflicht-Lese-Files | — |

**Edge-Cases der Match-Regel:**
- **Trigger + Wiki-Begriff** (z.B. „!Analysiere TMO und update Vault-Faktortabelle"): Union beider „Lies zusätzlich"-Spalten; Skip-Spalten verlieren Wirkung wenn anderer Trigger die Datei explizit anfordert; Skill-Calls beider Trigger ausführen.
- **Tippfehler / fast-exakte Trigger / Case-Drift / Sprach-Varianten** (z.B. `!Analysier`, `!Quickcheck`, `!analysiere`, `!Analyze TMO`): Kein Fuzzy-Match. Trigger sind strikt deutsch und PascalCase (`!Analysiere`, `!QuickCheck`, `!Rebalancing`, `!SyncBriefing`). Default-Verhalten + Rückfrage stellen („Meintest du `!Analysiere TMO`?"). Keine Selbstinterpretation.
- **Bare Symbol mit Wort-Ambiguität** (z.B. „V"): Soft-Match nur bei Symbolen aus den 11 aktuellen Satelliten-Tickern (siehe PORTFOLIO.md Portfolio-Tabelle). Bei Zweifel Rückfrage.

## Wiki-Modus

**Aktivierung:** Bei Wiki-Operationen (`ingest`, `lint`, `query`, oder Begriffen wie "Wiki", "Vault", "Obsidian", "Seite anlegen", "Faktortabelle", "Score aktualisieren", "Insider scan", "entity", "Satellit Seite"):
→ `07_Obsidian Vault/WIKI-SCHEMA.md` lesen und den dortigen Workflows folgen.

Wiki-Modus und Dynasty-Depot-Modus schließen sich **nicht** aus.

## Pointer (Ausgelagertes)

| Datei | Zweck |
|-------|-------|
| `00_Core/APPLIED-LEARNING.md` | Tier-2-Arbeitsprinzipien + Pflege-Regeln + Historie |
| `00_Core/TOKEN-RULES.md` | Token-Effizienz-Regeln (Accessibility, kein Enforcement) |
| `00_Core/INSTRUKTIONEN.md` | Tier-3-Regeln (Scoring-Skalen, Workflows, §§) |
| `00_Core/PORTFOLIO.md` | Live-Portfolio (Satelliten + Watches + 30-Tage-Trigger) — default-load bei Session-Start |
| `00_Core/PIPELINE.md` | Pipeline-SSoT (alle offenen Plan-Items + Long-Term-Gates) |
| `00_Core/SYSTEM.md` | System-Zustand (DEFCON-Version, MCP, Briefing, Backtest, R5, §30, Backlog) |
| `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md` | Chronik vor 15.04.2026 (Projekt-Aufbau, Tool-Setups, erste Analysen) |

---

## Plugin-Layer (2026-05-13)

Ruflo Sunset. Aktive Plugins als passive Substrate: **context-mode** (Tool-Output-Sandbox + FTS5) · **claude-mem** (Cross-Session-Memory + Chroma). AIDefence-Block im Morning-Briefing v3.2.0 unangetastet (FAIL-OPEN). Detail → SYSTEM.md §Plugin-Layer.

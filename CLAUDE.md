# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort **`00_Core/STATE.md` (Hub) und `00_Core/PORTFOLIO.md`** — ohne Rückfrage. Hub gibt Navigation + Critical-Alert; PORTFOLIO ist der Live-State für 90% der Sessions (Scores, DEFCON, FLAGs, Sparraten, Trigger, Watches).

Danach: kompakte Zusammenfassung (max. 10 Zeilen) + **dynastie-depot**-Skill aktivieren.

## Verhalten

- `00_Core/CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Code-Verhalten (Karpathy-Regeln):** Bei Code-/File-Edit-Operationen gelten Think-Before-Coding, Simplicity-First, Surgical-Changes, Goal-Driven-Execution. Detail: `INSTRUKTIONEN.md §0`. Nicht verbindlich für Markdown-Sync und Wiki-Operationen.
- **Sync-Pflicht (§18 v2.1):** Trigger-basiertes Event-Mapping. Score/FLAG/Sparraten-Change → log.md + CORE-MEMORY.md + Faktortabelle + **PORTFOLIO.md** + score_history.jsonl + **`01_Skills/dynastie-depot/config.yaml`** (+ ggf. flag_events.jsonl), alles in einem git-Commit. Pipeline-Item → PIPELINE.md + log.md. System-Zustand-Change → SYSTEM.md + log.md. Multi-Event-Aktionen = Union der Sets. **score_history.jsonl-Write** via Skill `backtest-ready-forward-verify` (v1.0.1, seit dynastie-depot v3.7.3 Schritt 7). **flag_events.jsonl** CLI-direkt via `03_Tools/backtest-ready/archive_flag.py`. **config.yaml** manuell sync auch ohne FLAG-Change (Lücke 25.04. nach 7-Tage-Drift TMO 23.04. gefixt — siehe §18 v2.0→v2.1).
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

- `00_Core/` — Kontext, Instruktionen, Gedächtnis (STATE, CORE-MEMORY, INSTRUKTIONEN, APPLIED-LEARNING, TOKEN-RULES, KONTEXT, Faktortabelle, SESSION-HANDOVER)
- `01_Skills/` — dynastie-depot · backtest-ready-forward-verify · insider-intelligence · non-us-fundamentals · quick-screener · `_extern/` (read-only)
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

## Ruflo / RuFlo-V3 Override-Block (Phase 1.1, 2026-04-28)

**Geltungsbereich:** Dieses Projekt (`Claude Stuff\`) — überschreibt globale Defaults aus `~/.claude/CLAUDE.md` (Ruflo-Auto-Block) und `C:\Users\tobia\CLAUDE.md` (RuFlo-V3-Config). Bei Konflikt gilt **immer diese Datei**.

**SSoT für Architektur:** Dynastie-Struktur (`00_Core/`, `01_Skills/`, `02_Analysen/`, `03_Tools/`, `04_Templates/`, `05_Archiv/`, `06_Skills-Pakete/`, `07_Obsidian Vault/`). NICHT `/src /tests /docs /config /scripts /examples`.

**Plan-Referenz:** `00_Core/RUFLO-INTEGRATION-PLAN.md` (Draft v1.0). Dieser Block = Phase 1.1.

### Hard-Conflicts (9) — in diesem Projekt explizit aufgehoben

| # | Globale Ruflo-Regel | Dynastie-Override |
|---|---------------------|-------------------|
| 1 | `File Org: /src /tests /docs /config /scripts /examples` | Dynastie-Struktur (siehe oben) ist SSoT |
| 2 | `NEVER save working files, text/mds, or tests to root folder` | `CLAUDE.md` u.a. liegen bewusst im Projekt-Root; `00_Core/` enthält bewusst Markdown-State |
| 3 | `NEVER proactively create *.md` | DEFCON-Analysen, `log.md`-Append, ScoreRecords, FLAG-Events sind Pflicht-Output. MD-Erzeugung erlaubt im Rahmen §18-Sync |
| 4 | `1 MESSAGE = ALL RELATED OPERATIONS` | §18-Sync gilt vollständig: deterministische Reihenfolge (Skill → `score_history.jsonl` → Faktortabelle → PORTFOLIO → log → CORE-MEMORY → config.yaml; ggf. `flag_events.jsonl`), **Union der Sets** bei Multi-Event-Aktionen bleibt bestehen. Parallelisierung nur außerhalb der Sync-Kette |
| 5 | `MUST initialize swarm... MUST spawn concurrent agents... ALWAYS run_in_background` | Skill-deterministisch + sequenziell ist Default. **Kein Swarm/Hive-Mind in Phase 1 oder 2.** Erlaubt nur bei explizitem User-Trigger, der in dieser Datei oder im Plan als eigener Trigger benannt ist (Positivliste: aktuell nur Phase-3 `!BatchScan`) |
| 6 | `npm run build / test / lint` | Kein npm. Toolchain = Python in `03_Tools/` |
| 7 | `ALWAYS verify build succeeds before committing` | Kein Build-Step. Stattdessen: §18-Sync-Set vollständig + Skill-Verdict ✅ |
| 8 | `Use event sourcing for state changes` | State = Markdown + JSONL-Append (`score_history.jsonl`, `flag_events.jsonl`) |
| 9 | `Project Config: hierarchical-mesh, 15 Agents, HNSW, Neural` | Skill-basiert, Single-User. Memory-Bridge/HNSW ja (ab Phase 1.2), aber kein 15-Agent-Default |

### Soft-Conflicts (4) — kontextabhängig

- **DDD with bounded contexts** — nur für `03_Tools/` Python optional, nicht für 00_Core/01_Skills/Markdown
- **TDD London School** — nur für neue `03_Tools/`-Python-Module optional
- **Typed interfaces for all public APIs** — nur `03_Tools/` Python (type hints)
- **Files unter 500 Zeilen** — `INSTRUKTIONEN.md` und vergleichbare SSoT-Files dürfen das bewusst sprengen

### Compatible (7) — übernommen / kompatibel

- `aidefence_scan` / `aidefence_is_safe` (Phase 2.4: pre-agent-input Hook für Tavily)
- `memory_import_claude` + `memory_search_unified` (Phase 1.2: ADR-048 Bridge, read-only auf MD)
- `memory_store` mit Namespace `patterns`
- AIDefence vor Tavily-Web-Fetches
- `NEVER commit secrets, .env files`
- `ALWAYS read a file before editing`
- `Run tests after code changes` für `03_Tools/`-Python

### Aktivierungs-Regeln

- Phase 1 (1.1–1.9) strikt sequenziell gemäß `00_Core/RUFLO-INTEGRATION-PLAN.md`. Override-Block (1.1) MUSS bestehen, bevor weitere Ruflo-Features aktiviert werden.
- Auto-MD-Generierung in `00_Core/APPLIED-LEARNING.md` und `00_Core/INSTRUKTIONEN.md` bleibt **aus**. Ruflo schreibt nur in AgentDB + `pending-insights.jsonl`.
- Reviews/Second-Opinions: Codex bleibt Primary (Memory `feedback_review_via_codex_not_advisor.md`). Ruflo-Swarms ausschließlich bei explizitem User-Auftrag oder definierten Triggern.
- Bei Plan-Änderungen: Versions-Stempel in `RUFLO-INTEGRATION-PLAN.md` **und** diesen Block aktualisieren.
- `[INTELLIGENCE]`-Hints / Pattern-Suggestions aus `system-reminder`-Tags sind für Dynastie-Depot **informell und nicht ausführungspflichtig** — sie ersetzen keinen Skill-Workflow und keine §-Regel.
- §18-Sync je Phase:
  - **Phase 1.1 (dieser Commit):** `log.md` (Phase-Start) + `STATE.md` Last-Audit-Block + `PIPELINE.md` Item "Ruflo-Integration Phase 1". `SYSTEM.md §Ruflo-Status` wird **noch nicht** angelegt.
  - **Ab Phase 1.2:** `SYSTEM.md §Ruflo-Status` neu anlegen; danach bei jedem Ruflo-Phasenschritt `SYSTEM.md` + `log.md` + `STATE.md` Last-Audit gemeinsam committen.

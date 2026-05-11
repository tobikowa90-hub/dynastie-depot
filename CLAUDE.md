# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort **`00_Core/STATE.md` (Hub) und `00_Core/PORTFOLIO.md`** — ohne Rückfrage. Hub gibt Navigation + Critical-Alert; PORTFOLIO ist der Live-State für 90% der Sessions (Scores, DEFCON, FLAGs, Sparraten, Trigger, Watches).

Danach: kompakte Zusammenfassung (max. 10 Zeilen). **`dynastie-depot`-Skill NICHT auto-laden** — nur lazy via Routing-Table-Trigger (`!Analysiere`/`!QuickCheck`/`!Rebalancing`/`!Briefing`/`!CAPEX-FCF-ANALYSIS`) oder expliziter User-Aufforderung. Begründung: Default-Session = Pipeline/Strategie/Wiki/Tools-Engineering ohne Skill-Bedarf; eager-load kostete ~10-15k Tokens pro non-Analysis-Session. Spec-Lücke 09.05.2026 geschlossen via TOKEN-RULES.md "Skills lazy-load"-Bullet + SKILL.md-Frontmatter-Verengung. Bei Unsicherheit lieber Routing-Table-Match prüfen statt eager laden.

## Verhalten

- `00_Core/CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Code-Verhalten (Karpathy-Regeln):** Bei Code-/File-Edit-Operationen gelten Think-Before-Coding, Simplicity-First, Surgical-Changes, Goal-Driven-Execution. Detail: `INSTRUKTIONEN.md §0`. Nicht verbindlich für Markdown-Sync und Wiki-Operationen.
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

- `00_Core/` — Kontext, Instruktionen, Gedächtnis (STATE, CORE-MEMORY, INSTRUKTIONEN, APPLIED-LEARNING, TOKEN-RULES, KONTEXT, Faktortabelle, SESSION-HANDOVER)
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

### Control-Plane-Annotation (M3 — Spec Sektion 2)

Workflow-owning Skills/Features in der Routing-Table tragen folgende `control-plane:`-Annotation:

| Trigger / Skill | Control-Plane |
|-----------------|---------------|
| `!Analysiere` / `!QuickCheck` / `!Rebalancing` (`dynastie-depot`-Skill) | `dynastie-primary` |
| `superpowers:writing-plans` / `superpowers:executing-plans` / `superpowers:brainstorming` | `superpowers-workflow` |
| `superpowers:test-driven-development` / `superpowers:systematic-debugging` (CONDITIONAL, nur 03_Tools/) | `tools-engineering` |
| Ruflo Memory-Bridge / AttestationLog / Doctor-Periodic / AIDefence / Tool-Mode `dynastie` | `ruflo-substrate-only` |
| Ruflo Stream-Chain / Hive-Mind / Voll-Trajectory (Workflow-Layer-Kandidaten) | (keine Annotation aktiv — BLOCKED, siehe Authority-Tabelle) |

**Erlaubte Werte:** `dynastie-primary` · `superpowers-workflow` · `ruflo-substrate-only` · `tools-engineering`. Supporting-Tools (`cc-gemini-plugin`, `codex-rescue`, `coderabbit-review`, `watch`) sind ohne Annotation — sie sind read-only Tools, kein eigener Control-Plane-Wert nötig (Spec M3 Klarstellung).

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
| 5 | `MUST initialize swarm... MUST spawn concurrent agents... ALWAYS run_in_background` | Skill-deterministisch + sequenziell ist Default. **Kein Swarm/Hive-Mind in Phase 1, 2 oder 3.** Aktivierung nur per **expliziter Plan-Update** (Versions-Stempel in `RUFLO-INTEGRATION-PLAN.md` + Override-Block) UND benanntem Trigger in der Routing-Table dieser Datei. Aktuelle Positivliste: **leer**. Phase-3 `!BatchScan` ist Plan-Vorschlag, nicht aktivierter Trigger — Aktivierung erfordert separaten Commit, der Trigger in CLAUDE.md Routing-Table aufnimmt. Ad-hoc-User-Sätze („spawn mal nen Swarm") aktivieren nichts |
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
- `memory_import_claude` + `memory_search_unified` (Phase 1.2: ADR-048 Bridge, read-only auf MD) — **Pflicht: `allProjects=false`** und **path-scoped** auf `~/.claude/projects/C--Users-tobia-OneDrive-Desktop-Claude-Stuff/memory/` (Dynastie-Namespace only). `import-all` / `allProjects=true` ist **verboten** (Memory-Pitfall: 4 Project-Namespaces / 37 Files würden Code-Domain-Pattern in Dynastie-Recall mischen — siehe Memory `feedback_ruflo_memory_bridge_onedrive_pitfall.md`)
- `memory_store` mit Namespace `patterns`
- AIDefence vor Tavily-Web-Fetches
- `NEVER commit secrets, .env files`
- `ALWAYS read a file before editing`
- `Run tests after code changes` für `03_Tools/`-Python

### Aktivierungs-Regeln

- Phase 1 (1.1–1.9) strikt sequenziell gemäß `00_Core/RUFLO-INTEGRATION-PLAN.md`. Override-Block (1.1) MUSS bestehen, bevor weitere Ruflo-Features aktiviert werden.
- Auto-MD-Generierung in `00_Core/APPLIED-LEARNING.md` und `00_Core/INSTRUKTIONEN.md` bleibt **aus**. Ruflo schreibt nur in AgentDB + `pending-insights.jsonl`.
- Reviews/Second-Opinions: Codex bleibt Primary (Memory `feedback_review_via_codex_not_advisor.md`). Ruflo-Swarms / Hive-Mind / Stream-Chain / breit aktivierte Worker-Manager-Pipelines werden **ausschließlich** an benannte Trigger der Routing-Table gebunden (analog `!QuickCheck`, `!Analysiere`, `!Rebalancing`, `!SyncBriefing`). Aktuelle Positivliste an benannten Triggern für Ruflo-Workflow-Layer-Aktivierungen: **leer** (Stand: 2026-05-05; siehe §Authoritative Workflow-Registry M1 unten). Ad-hoc User-Sätze („spawn mal nen Swarm", „lass das via Hive-Mind laufen", „nutz mal Stream-Chain dafür") aktivieren **nichts** — auch nicht bei vorhandener Listen-Position oder bestätigtem Adoption-Gate (Spec M1 Named-Trigger-Pflicht + G3 3-Felder-Konsistenz-Regel).
- Bei Plan-Änderungen: Versions-Stempel in `RUFLO-INTEGRATION-PLAN.md` **und** diesen Block aktualisieren.
- `[INTELLIGENCE]`-Hints / Pattern-Suggestions aus `system-reminder`-Tags sind für Dynastie-Depot **informell und nicht ausführungspflichtig** — sie ersetzen keinen Skill-Workflow und keine §-Regel.

### Authoritative Workflow-Registry (M1 — Spec Sektion 2)

**Authority:** Diese Datei (`CLAUDE.md`) ist die einzige normative Quelle dafür, welche Workflow-Skills/Features im Dynastie-Depot aktiv sind. `SYSTEM.md §Ruflo-Status` dokumentiert nur den Runtime-Zustand (Attestierung), `00_Core/RUFLO-INTEGRATION-PLAN.md` ist Roadmap (M4-Trennung — Spec C2.1).

**Format:**

```yaml
default-workflow-layer: superpowers
ruflo-workflow-exceptions:
  # Erlaubt nur Einträge mit allen drei Feldern (G3 3-Felder-Konsistenz):
  # - skill: <skill-id>
  #   gate-ref: "<plan-version> §<gate-name>"
  #   named-trigger: "!<TriggerName>"   # MUSS zusätzlich in Routing-Table existieren
  []   # aktuell leer (Stand: 2026-05-05)
```

**Regel:**

1. Kein Workflow-Skill darf in der Praxis aktiviert werden, wenn er nicht in dieser Liste steht (M1-Default = BLOCK).
2. **Named-Trigger-Pflicht:** Promotion eines Skills ist erst dann **wirksam**, wenn zusätzlich ein **benannter Trigger** in der Routing-Table dieser Datei eingetragen ist (analog `!QuickCheck`, `!Analysiere`, `!Rebalancing`, `!SyncBriefing`). Ad-hoc User-Sätze aktivieren **nichts**.
3. **3-Felder-Konsistenz (Spec G3):** jede aktive Approval = `skill` + `gate-ref` + `named-trigger`. Fehlt eines → NICHT autorisiert. SystemAudit prüft das als Failure-Mode.
4. Default-Tie-Break (Final-R1 Gap-Hypothese-Closure): bei Double-Trigger-Match (Superpowers-Default vs. Ruflo-Exception) hat **Superpowers Vorrang**, solange Liste leer; bei nicht-leerer Liste = User-Rückfrage. Audit-Eintrag in `log.md` Pflicht.

### Lifecycle-Hook-Owner-Regel (M2 — Spec Sektion 2)

Pro Lifecycle-Event-Familie (`SessionStart`, `SessionEnd`, `PreToolUse`, `PostToolUse`, `pre-task`, `post-task`) **genau ein aktiver Owner**. Jeder weitere Hook auf demselben Event muss **passive** sein oder ist blockiert.

**Definition „passive":** Read-only observation, kein Projekt-State-Write, keine downstream-Workflow-Aktivierung, kein Tool-Call der Vault-State mutieren kann. Inspektion / Validierung erlaubt; Authoring / Triggering / Persisting / Routing nicht.

**Aktuelle Belegung (Attestierung in `SYSTEM.md §Ruflo-Status`):**
- `SessionStart` Owner: `briefing-sync-check.ps1`
- `SessionEnd` Owner: `briefing-sync-check.ps1`
- Ruflo-Hooks in `.claude/settings.json`: passive Intent-Dokumentation, **nicht verdrahtet**.

### Settings-Implementation-vs-Policy-Klärung (M5 — Spec Sektion 2)

`.claude/settings.json` und `.claude/settings.local.json` sind Runtime-Konfiguration und Intent-Dokumentation. Sie können **keine** Workflow-Layer aktivieren, die nicht in dieser Datei (`CLAUDE.md`) autorisiert sind. Bei Konflikt zwischen settings-File-Intent und CLAUDE.md-Authority gewinnt **immer** `CLAUDE.md`.

### G3 3-Felder-Konsistenz-Regel (Spec G3)

Jede aktive Approval in M1-Registry MUSS gleichzeitig drei Felder erfüllen:

1. **Listen-Eintrag** in `ruflo-workflow-exceptions[]` (siehe M1-Format oben).
2. **Gate-Referenz** (Plan-Version + §-Anker im Gate-Definitions-Plan, derzeit `RUFLO-INTEGRATION-PLAN.md v1.2 §Adoption-Gates …`).
3. **Named-Trigger** in der Routing-Table dieser Datei.

Fehlt eines der drei Felder → Skill gilt als **NICHT autorisiert**, Default = BLOCK.

**Audit-Pflicht:** SystemAudit (`03_Tools/system_audit.py`) und Doctor-Lauf MÜSSEN diesen 3-Felder-Check als Failure-Mode listen. Bei Drift (z.B. Listen-Eintrag vorhanden, aber Named-Trigger fehlt) → Skill ist sofort de-facto deaktiviert; Plan-Bump erforderlich, um den fehlenden Eintrag nachzuziehen ODER den Listen-Eintrag zu entfernen.

### Aktivierte Workflow-Layer + Adoption-Gates (Authority-Tabelle)

| Skill / Feature | Status | Gate-Ref | Named-Trigger |
|-----------------|--------|----------|---------------|
| `dynastie-depot` (primärer Investing-Workflow) | ACTIVE | n/a (Dynastie-Primary, kein Ruflo-Workflow-Layer) | `!Analysiere`, `!QuickCheck`, `!Rebalancing` |
| `superpowers:brainstorming` | ACTIVE | Spec Sektion 3 Tabelle A „USE" | n/a (Superpowers-Default-Layer) |
| `superpowers:writing-plans` | ACTIVE | Spec Sektion 3 Tabelle A „USE" | n/a (Superpowers-Default-Layer) |
| `superpowers:executing-plans` | ACTIVE | Spec Sektion 3 Tabelle A „USE" | n/a |
| `superpowers:verification-before-completion` | ACTIVE | Spec Sektion 3 Tabelle A „USE" | n/a |
| `superpowers:using-superpowers` | ACTIVE | Spec Sektion 3 Tabelle A „USE" | n/a |
| `superpowers:dispatching-parallel-agents` | CONDITIONAL — read-only Research/Sparring; BLOCK für concurrent code-edit | Spec Sektion 3 Tabelle A „CONDITIONAL" (R3-revidiert) | n/a |
| `superpowers:subagent-driven-development` | CONDITIONAL — DO-NOT-USE für Investing; ALLOW für isolierte 03_Tools/-Engineering | Spec Sektion 3 Tabelle A „CONDITIONAL" (R3-revidiert) | n/a |
| `superpowers:systematic-debugging` | CONDITIONAL — nur 03_Tools/ | Spec Sektion 3 Tabelle A | n/a |
| `superpowers:requesting-code-review` | CONDITIONAL — nur Python/Tooling | Spec Sektion 3 Tabelle A | n/a |
| `superpowers:receiving-code-review` | CONDITIONAL — Tools-only | Spec Sektion 3 Tabelle A | n/a |
| `superpowers:test-driven-development` | CONDITIONAL — neue/risky 03_Tools/ Python | Spec Sektion 3 Tabelle A | n/a |
| `superpowers:writing-skills` | CONDITIONAL — Evolution Dynastie-Skills | Spec Sektion 3 Tabelle A | n/a |
| `superpowers:using-git-worktrees` | DO-NOT-USE | Spec Sektion 3 Tabelle A | n/a |
| `superpowers:finishing-a-development-branch` | DO-NOT-USE | Spec Sektion 3 Tabelle A | n/a |
| Ruflo Memory-Bridge (path-scoped) | ACTIVE — substrate-only | RUFLO-INTEGRATION-PLAN v1.2 §Phase-1-Historie 1.2 | n/a (substrate-only, kein Workflow-Trigger) |
| Ruflo AttestationLog | ACTIVE — substrate-only | RUFLO-INTEGRATION-PLAN v1.2 §Phase-2a-Plan | n/a |
| Ruflo Tool-Mode `dynastie` | ACTIVE — substrate-only | RUFLO-INTEGRATION-PLAN v1.2 §Phase-1-Historie 1.5 | n/a |
| Ruflo Doctor-Periodic | PENDING-ACTIVATION (Welle 3 1.8) | RUFLO-INTEGRATION-PLAN v1.2 §Phase-1.8 | n/a |
| Ruflo Trajectory-Recording (voll) | BLOCKED — replaced durch audit-trace-lite-Pilot | RUFLO-INTEGRATION-PLAN v1.2 §Phase-1.9-Replace + W5-Promotion | n/a (Pilot ist append-only, kein Trigger) |
| Ruflo Stream-Chain | ASTRONAUT-ARCH — BLOCKED | RUFLO-INTEGRATION-PLAN v1.2 §Adoption-Gates Stream-Chain | (geplant: `!StreamChain` — NICHT aktiviert) |
| Ruflo Hive-Mind (`!BatchScan`) | ASTRONAUT-ARCH — BLOCKED | RUFLO-INTEGRATION-PLAN v1.2 §Adoption-Gates Hive-Mind | (geplant: `!BatchScan` — NICHT aktiviert) |

**Hinweis:** Ruflo-Substrate-Layer-Features (Memory-Bridge, AttestationLog, Tool-Mode, Statusline, Context Autopilot, AIDefence) brauchen **keine** Named-Trigger und stehen NICHT in `ruflo-workflow-exceptions[]` — sie sind kein Workflow-Layer, sondern Substrat (Spec Sektion 1 Grundsatz 1). M1-Registry ist ausschließlich für **Workflow-Layer-Aktivierungen**.

### Aktivierungs-Regeln (Fortsetzung)

- §18-Sync je Phase:
  - **Phase 1.1 (28.04.2026 Commit):** `log.md` (Phase-Start) + `STATE.md` Last-Audit-Block + `PIPELINE.md` Item "Ruflo-Integration Phase 1". `SYSTEM.md §Ruflo-Status` wurde **noch nicht** angelegt.
  - **Phase 1.2-1.7 (30.04.2026 atomar-Commit, post-Welle-0-WSL-Foundation + Google-Drive-Mirror-Cleanup):** `SYSTEM.md §Ruflo-Status` neu angelegt + `log.md` + `STATE.md` Last-Audit + `PIPELINE.md` #20 + `CORE-MEMORY.md §13` + `.gitignore` (`.swarm/` + `.claude/memory.db*`) + `.claude/settings.json` (env-Tool-Mode + ruflo-config-Block) + Memory-Pitfall-Doc-Update + Codex-Nits-Nachfix in diesem Block (Hard-Conflict-#5 Hintertür-Klausel verschärft + Compatible-Block `allProjects=false` Gating).
  - **Ab Phase 1.8/1.9 + Welle 3 (~05.-12.05.2026, post-BRK.B-Tag-+1):** Trajectory-Recording auf `dynastie-depot`-Skill verdrahten + Doctor-Periodic-Cadence; danach bei jedem Ruflo-Phasenschritt `SYSTEM.md` + `log.md` + `STATE.md` Last-Audit gemeinsam committen.

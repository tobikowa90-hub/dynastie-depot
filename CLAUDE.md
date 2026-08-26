# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort **`00_Core/STATE.md` (Hub) und `00_Core/PORTFOLIO.md`** — ohne Rückfrage. Hub gibt Navigation + Critical-Alert; PORTFOLIO ist der Live-State für 90% der Sessions (Scores, DEFCON, FLAGs, Sparraten, Trigger, Watches).

Danach: kompakte Zusammenfassung (max. 10 Zeilen). **`dynastie-depot`-Skill NICHT auto-laden** — nur lazy via Routing-Table-Trigger (`!Analysiere`/`!QuickCheck`/`!Rebalancing`/`!Briefing`/`!CAPEX-FCF-ANALYSIS`) oder expliziter User-Aufforderung. Begründung + Spec-Historie: `00_Core/TOKEN-RULES.md` „Skills lazy-load"-Bullet (SSoT). Bei Unsicherheit Routing-Table-Match prüfen statt eager laden.

## Session-Optimierung

- **Gotcha-Regel**: Optimiere basierend auf Verlauf jeder Session jegliche genutzten Skills und Workflows.
- **Sektions-Pflicht**: Am Ende jeder Aufgabe oder Konversation zwingend Sektion `### Mögliche Stolpersteine (Gotchas)` anfügen.
- **Inhalt**: Expliziter Verweis auf in dieser Session gemachte Fehler, versteckte Bugs, Edge Cases, Performance-Risiken oder typische Denkfehler. Ziel: Fehlervermeidung in Folge-Sessions.
- **Tier-2-Bridge**: Identifizierst du in den Gotchas eine fundamentale Erkenntnis, schlage mir am Session-Ende den exakten Markdown-Code für den Übertrag in `00_Core/APPLIED-LEARNING.md` (Tier 2) aktiv vor.


## Verhalten

**Oberste Leitlinien**:

Wenn du mir Informationen mitteilst, sei äußerst prägnant und verzichte zugunsten der Prägnanz auf grammatikalische Korrektheit.

Bevor du mit einem Workflow beginnst, gib an, wie dieser überprüft werden soll. Wenn du fertig bist, führe diese Überprüfung durch und berichte über    die Ergebnisse. Bevor du irgendwelche Änderungen an der Codebase vornimmst, frag mich zuerst und erkläre mir den Wirkungsradius.

- `00_Core/CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Code-Verhalten (Karpathy-Regeln):** Bei Code-/File-Edit-Operationen gelten Think-Before-Coding, Simplicity-First, Surgical-Changes, Goal-Driven-Execution, **Pre-Refactor-Caller-Scan** (`Grep` auf Symbol vor Edit bei externen Aufrufern) und **Approach-Reset-Schwelle** (nach 2 identischen Failed-Attempts: Stop → Codex-Sparring / Plan-Wechsel / User-Konsultation). **Vor jedem Code-/File-Edit zwingend `00_Core/CODE_GUIDELINES.md` laden + befolgen** (Volltext §0, ausgelagert 2026-06-09; INSTRUKTIONEN.md §0 = Stub). Nicht verbindlich für Markdown-Sync und Wiki-Operationen.
- **Pre-Investigation-Recall-Check:** Vor einer mehrschrittigen Re-Investigation (≥3 Tool-Calls Diagnose) eines Symptoms/Fehlers/Anomalie zuerst **EIN** gezielter `mem-search`/`get_observations`-Pass („schon mal gelöst/entschieden?"). Treffer = **advisory Prior** → billig gegen Live-State verifizieren (Memory-Guard-Rail/§17.1), nie als Ground-Truth übernehmen. Session-typ-übergreifend. Detail/Auslöser → Memory `feedback_pre_investigation_recall_check.md`.
- **Sync-Pflicht (§18 — Voll-Spec + Versions-Historie → INSTRUKTIONEN §18):** Trigger-basiertes Event-Mapping. Score/FLAG/Sparraten-Change → log.md + CORE-MEMORY.md + Faktortabelle + **PORTFOLIO.md** + score_history.jsonl + **`01_Skills/dynastie-depot/config.yaml`** + **`03_Tools/Rebalancing_Tool`** + **`03_Tools/Satelliten_Monitor`** (xlsx; Versionen gepinnt in `SYSTEM.md` §Active xlsx-Filenames) (+ ggf. flag_events.jsonl), alles in einem git-Commit (xlsx-Tools können separater Tool-Commit sein, aber gleiche Session pflicht). Pipeline-Item → PIPELINE.md + log.md. System-Zustand-Change → SYSTEM.md + log.md. Multi-Event-Aktionen = Union der Sets. **score_history.jsonl-Write** via Skill `backtest-ready-forward-verify` (Schritt 7). **flag_events.jsonl** CLI-direkt via `03_Tools/backtest-ready/archive_flag.py`. **config.yaml** manuell sync auch ohne FLAG-Change. **xlsx-Tools** via `openpyxl` manuell sync (operative Zero-Token-Lookup-Quelle für Sparpläne + Depot-Übersicht). **xlsx-Smoke-Test §18.7:** nach jedem `openpyxl`-Write Pflicht-Smoke-Test gemäß `03_Tools/xlsx-smoke-test.md` vor `git add` der xlsx-Files; fail-close, kein `--force`-Bypass.
- **Token-Effizienz (Claude-Disziplin — Operator-Detail in `00_Core/TOKEN-RULES.md`):** **Snapshot-First** PORTFOLIO + Faktortabelle vor API/MCP-Call (Routing-Table macht das default-implizit; explizit-pflicht bei Cross-Source-Drift-Check, spart 3-5 Tool-Calls). **DEFCON-1-Stopp** Score <50 → Analyse-Schritte stoppen, Insider-Modul läuft durch (siehe `dynastie-depot` §170/§172). **/compact-Cue** vorschlagen bei ~60% Kontext-Voll oder >5min Pause (Operator triggert; Preserve: Score/Tabelle/Urteil/FLAGs/**aktuelle Gotchas**). Skills-lazy-load + §18-Sync sind bereits eigene Verhalten-Bullets.
- **Earnings-Call-Wait-Discipline (§19.1):** Klasse-B-Vollanalyse läuft strikt **Tag +1 morgens nach Earnings Call**, nicht Tag 0. Tag 0 = `_extern/earnings-recap`-Skill für Press-Release-Recap + manueller FLAG-Quick-Check (FLAG-Trigger/Resolve via `archive_flag.py` sofort, Score unverändert) + Pre-Call-Snapshot in CORE-MEMORY §12.<ticker>. Score-Move + 8-File-Sync ausschließlich am Tag +1 mit Transcript-Read via defeatbeta-MCP. Outlier-Bypass: Tag-0-FLAG-Event ja, Score-Move nein. Detail INSTRUKTIONEN §19.1 + Memory `feedback_earnings_call_wait_discipline.md`.


## Kontinuierliches Lernen

| Tier | Speicherort | Wer schreibt | Wann gelesen | Pflege |
|------|------------|--------------|-------------|--------|
| 1. Auto-Memory | `~/.claude/projects/C--Users-tobia-Code/memory/*.md` | Claude automatisch | Session-Start (MEMORY.md auto-loaded) | Auto-Dream konsolidiert |
| 2. Applied Learning | `00_Core/APPLIED-LEARNING.md` | Manuell / Claude-Vorschlag | On-Demand (per Routing-Table) | Monatlich + Kurator-Regel |
| 3. Formelle Regeln | `00_Core/INSTRUKTIONEN.md` §§ | Bei bewiesenem Bedarf | Per Routing-Table | Bei Systemänderungen |

**Tier-1 Pfad-SSoT (NORMATIV ab 2026-05-26):** Code-Path `~/.claude/projects/C--Users-tobia-Code/memory/` ist der **einzige** Speicherort und die **einzige Quelle** für Auto-Memory-Files. Index = `MEMORY.md` (auto-loaded). **Anti-Fork-Direktive:** Neue Memories IMMER hier ablegen — keine Parallel-Pfade (z.B. `C--Users-tobia-OneDrive-Desktop-Claude-Stuff/memory/` ist DEPRECATED + konsolidiert 2026-05-26), keine Duplikate, keine Pfad-Schatten-Welten. Bei Fork-Verdacht oder unsichtbaren Memories: `reference_memory_fork_onedrive_vs_code_path` konsultieren.

**S-Tier-Memories (workflow-blocking, immer-relevant — Volle Liste in MEMORY.md):**
- `feedback_pre_investigation_recall_check` — vor jeder ≥3-Tool-Diagnose 1× mem-search/PIPELINE-Live-Grep-Pass
- `feedback_empirie_statt_annahmen` — Real-Verhalten via Grep/Test-Run/Code-Read VOR Edit verifizieren (Karpathy-Sibling)
- `feedback_xlsx_tools_in_sync_set` — §18.1 Pflicht-Sync: Rebalancing + Satelliten-Monitor + Watchlist xlsx bei Score/FLAG/Sparraten-Change
- `feedback_earnings_call_wait_discipline` — §19.1: Klasse-B-Vollanalyse Tag +1 morgens (nicht Tag 0)
- `feedback_review_via_codex_not_advisor` — Reviews/Second-Opinions via Codex (`codex:codex-rescue` / `codex:rescue`), nie `advisor()`
- `feedback_correctness_over_runtime` — Datenkorrektheit/Recall > Runtime-Optimierung (Briefing + Scoring + FLAG + alle Pipelines)
- `reference_no_cloud_sync_onedrive_inactive` — Pfad heißt nur „OneDrive", KEIN aktiver Cloud-Sync; Worktree-Drift nicht auf Cloud schieben
**Memory-Guard-Rail** siehe Routing-Table-Klausel + `INSTRUKTIONEN.md §17.1`.

Bullets, Pflege-Regeln, Promotion-Logik, Historie: siehe `00_Core/APPLIED-LEARNING.md`.

## Projektstruktur

- `00_Core/` — Kontext, Instruktionen, Gedächtnis (STATE, CORE-MEMORY, INSTRUKTIONEN, CODE_GUIDELINES [§0-Volltext, Code-Edit-Lazy-Load], RETROSPECTIVE-GATE, APPLIED-LEARNING, TOKEN-RULES, KONTEXT, Faktortabelle, SESSION-HANDOVER)
- `01_Skills/` — dynastie-depot · backtest-ready-forward-verify · insider-intelligence · non-us-fundamentals · quick-screener · sec-edgar-skill · session-closure · paragraph-18-sync · core-slim-refactor · xlsx-smoke-test-runner · `_extern/` (read-only)
- `02_Analysen/` — DEFCON-Analysen als Excel sowie Earnings Reports der Satelliten
- `03_Tools/` — Rebalancing_Tool · Satelliten_Monitor · Watchlist_Ersatzbank_Monitor · Briefing-Hook · system_audit
- `04_Templates/` — Pointer + spezifische Templates
- `05_Archiv/` — Historische Dateien
- `06_Skills-Pakete/` — Installierbare ZIP-Skills
- `07_Obsidian Vault/` — Wiki (Schema + Workflows via WIKI-SCHEMA.md)

## Routing-Table

> STATE.md + PORTFOLIO.md immer. **Match-Regel (Hybrid):** exakte Trigger strikt; bare Ticker → `!QuickCheck`; Mehrfach-Match = Union der Lies-Spalten. Bei Trigger-Miss: konservativ mehr laden.

| Trigger | Lies zusätzlich | Skippe | Skill-Call |
|---------|-----------------|--------|------------|
| `Session starten` (default) | (Resume-Fall: SESSION-HANDOVER.md) | PIPELINE, SYSTEM, CORE-MEMORY, INSTRUKTIONEN, KONTEXT, Faktortabelle, Wissenschaftliche-Fundierung-DEFCON | — |
| `!Analysiere <Ticker>` | INSTRUKTIONEN.md, Faktortabelle.md, …/synthesis/Wissenschaftliche-Fundierung-DEFCON.md | KONTEXT, CORE-MEMORY (außer §5 bei Scoring-Edge-Case) | `dynastie-depot` + `backtest-ready-forward-verify` (Schritt 7, programmatisch) |
| `!QuickCheck <Ticker>` | Faktortabelle.md | INSTRUKTIONEN, KONTEXT, CORE-MEMORY, Wiss-Fundierung | `quick-screener` |
| `!Rebalancing` | INSTRUKTIONEN.md, KONTEXT.md | CORE-MEMORY, Faktortabelle, Wiss-Fundierung | — |
| `!SyncBriefing` | INSTRUKTIONEN.md (§25) + SYSTEM.md §Briefing-Status (nur wenn Briefing-Version/Deploy-Status seit letztem Sync geändert) | alle anderen | — |
| `!SessionClose` | INSTRUKTIONEN.md §25.5 | alle anderen | `session-closure` |
| `!ParaSync18 <event-type>` | INSTRUKTIONEN.md §18, `01_Skills/paragraph-18-sync/references/event_typ_mapping.yaml` | KONTEXT, CORE-MEMORY (außer system-zustand `--version-bump`), Wiss-Fundierung | `paragraph-18-sync` |
| **§18-File-Touch (auto, file-pattern-driven; NEU 2026-05-23 spätabends)** — Working-Tree-Diff enthält EINEN von: `00_Core/{PIPELINE,PORTFOLIO,CORE-MEMORY,Faktortabelle,SYSTEM}.md` · `07_Obsidian Vault/.../log.md` · `05_Archiv/{score_history,flag_events}.jsonl` · `01_Skills/dynastie-depot/config.yaml` · `01_Skills/*/SKILL.md` (Version-Edit) · `03_Tools/{Rebalancing,Satelliten_Monitor,Watchlist_Ersatzbank_Monitor}_v*.xlsx` | INSTRUKTIONEN.md §18 | KONTEXT, Wiss-Fundierung | `paragraph-18-sync` (event-type aus File-Pattern inferred — score-flag-sparraten/pipeline-item/system-zustand/critical-alert; `--dry-run` für Edit-Vorschau, ohne `--dry-run` vor `git commit`; Multi-Event via `--also`) |
| Wiki-Ops (`ingest`/`lint`/`query`, „Vault"/„Obsidian"/„Faktortabelle-Edit"/„Score-Update"/„Insider scan"/„entity"/„Satellit Seite") | `07_Obsidian Vault/.../WIKI-SCHEMA.md` | INSTRUKTIONEN, KONTEXT, CORE-MEMORY (außer Wiki-Bezug) | je nach WIKI-SCHEMA-Workflow (`insider-intelligence`, `non-us-fundamentals`, …) · **Referenz-Lookup** über stabilen Text (Wiss-Fundierung/Vault-**Synthesis**/Earnings) → `ctx_search` explorativ; Live-State NIE indexiert, Scoring-Pfad bleibt autoritativer Vollread (`TOKEN-RULES.md §Referenz-Korpus-Index` · ADR-0001) |
| `remote-Control` / „mobile weiter" | Auto-Memory `reference_remote_trigger_api.md` | alles andere (Snapshot reicht) | — (User-getriggerter `ccr`-Spawn) |
| Konsolidierungstag / System-Audit / Backlog-Review | SESSION-HANDOVER.md, STATE.md (Hub für Critical-Alerts + Last-Audit-Block) + PIPELINE.md + SYSTEM.md | KONTEXT, Faktortabelle (außer ticker-spezifisch) | `SystemAudit` (slash) bei Audit-Lauf |
| Strategie-/Allokations-Frage | KONTEXT.md | Faktortabelle, Wiss-Fundierung | — |
| Code-Edit-Session ohne anderen Trigger (z.B. „fix bug in X.py", „refactor Y") | **`00_Core/CODE_GUIDELINES.md`** (Code-Verhaltens-Regeln §0 — Volltext; INSTRUKTIONEN.md nur bei Bedarf, §0 dort = Stub) | INSTRUKTIONEN.md (außer Bedarf), alle anderen Pflicht-Lese-Files | — |

**Memory-Guard-Rail (normativ; Voll-Spec → INSTRUKTIONEN.md §17.1):** Routing nur aus Routing-Table, expliziter User-Nachricht und absoluten Live-Dateien (`PORTFOLIO.md`, `STATE.md`, `INSTRUKTIONEN.md`) bestimmen. Memory (`autoMemory`, `claude-mem`, folder-memory, context-mode-search) erst nach Match konsultieren; strikt advisory, nie Override gegen Live-Dateien.

**Edge-Cases der Match-Regel:**
- **Trigger + Wiki-Begriff** (z.B. „!Analysiere TMO und update Vault-Faktortabelle"): Union beider „Lies zusätzlich"-Spalten; Skip-Spalten verlieren Wirkung wenn anderer Trigger die Datei explizit anfordert; Skill-Calls beider Trigger ausführen.
- **Tippfehler / fast-exakte Trigger / Case-Drift / Sprach-Varianten** (z.B. `!Analysier`, `!Quickcheck`, `!analysiere`, `!Analyze TMO`): Kein Fuzzy-Match. Trigger mit `!` sind strikt deutsch und PascalCase (z.B. `!Analysiere`, `!SessionClose`). Default-Verhalten + Rückfrage stellen („Meintest du `!Analysiere TMO`?"). Keine Selbstinterpretation.
- **Bare Symbol mit Wort-Ambiguität** (z.B. „V"): Soft-Match nur bei Symbolen aus den 11 aktuellen Satelliten-Tickern (siehe PORTFOLIO.md Portfolio-Tabelle). Bei Zweifel Rückfrage.

## Wiki-Modus

**Aktivierung:** Bei Wiki-Operationen (`ingest`, `lint`, `query`, oder Begriffen wie "Wiki", "Vault", "Obsidian", "Seite anlegen", "Faktortabelle", "Score aktualisieren", "Insider scan", "entity", "Satellit Seite"):
→ `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/WIKI-SCHEMA.md` lesen und den dortigen Workflows folgen.

Wiki-Modus und Dynasty-Depot-Modus schließen sich **nicht** aus.

## Pointer (Ausgelagertes)

| Datei | Zweck |
|-------|-------|
| `00_Core/APPLIED-LEARNING.md` | Tier-2-Arbeitsprinzipien + Pflege-Regeln + Historie |
| `00_Core/TOKEN-RULES.md` | Token-Effizienz-Regeln (Accessibility, kein Enforcement) |
| `00_Core/INSTRUKTIONEN.md` | Tier-3-Regeln (Scoring-Skalen, Workflows, §§; §17.1 Memory-Guard-Rail: Routing-Inputs/Advisory-only/`mem-conflict`) |
| `00_Core/PORTFOLIO.md` | Live-Portfolio (Satelliten + Watches + 30-Tage-Trigger) — default-load bei Session-Start |
| `00_Core/PIPELINE.md` | Pipeline-SSoT (alle offenen Plan-Items + Long-Term-Gates) |
| `00_Core/SYSTEM.md` | System-Zustand (DEFCON-Version, MCP, Briefing, Backtest, R5, §30, Backlog) |
| `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md` | Chronik vor 15.04.2026 (Projekt-Aufbau, Tool-Setups, erste Analysen) |

---

## Engineering-Skills — Pocock-Subset (2026-06-05)

`grill-with-docs` + `improve-codebase-architecture` aktiv; **lazy-create-Design** — kein eager-Seed von `CONTEXT.md` / `docs/adr/` (Skill scaffoldet beim ersten Real-Trigger selbst, SKILL.md L52). `prototype` aktiv als **Empirie-Sandbox-Layer** vor Spec/Plan bei High-Fi-Fragen (Pocock-Pattern `grill → prototype → grill again`; Detail Memory `feedback_pocock_low_fi_high_fi_grilling.md`) — nicht Code-Bau-Ersatz, sondern Pre-Spec-Empirie für Fragen die parametrisches Grilling nicht beantworten kann (Coverage-Matrix, Real-Datenstand, Edge-Case-Topologie). Issue-/Triage-/PRD-Skills (`triage`/`to-issues`/`qa`/`to-prd`) **SKIP** — `00_Core/PIPELINE.md` ist Work-SSoT, würde §18-Sync brechen. `/setup-matt-pocock-skills` nicht ausgeführt (Walk-Through 2026-06-05).

---

## Plugin-Layer (2026-05-13, Hybrid 2026-05-16)

Passive Substrate: context-mode + obsidian-skills + **claude-mem v13.2.0 enabled = rein additiver read-only Augmentation-Layer, nie SSoT**; natives autoMemory kanonisch + Live-State-Priorität unberührt (HYBRID, empirisch verifiziert). Memory-Guard-Rail → §Routing-Table + INSTRUKTIONEN.md §17.1. Voll-Detail (Bun-Invariante, Begründung, Backups) → **SYSTEM.md §Plugin-Layer**.

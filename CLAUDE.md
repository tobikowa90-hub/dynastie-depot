# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort **nur `00_Core/STATE.md`** — ohne Rückfrage. Diese Datei ist Single-Entry-Point und genügt für 90% der Sessions (Scores, DEFCON, FLAGs, Sparraten, Trigger, Watches).

Danach: kompakte Zusammenfassung (max. 10 Zeilen) + **dynastie-depot**-Skill aktivieren.

## Verhalten

- `CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Sync-Pflicht:** Nach jeder Analyse: log.md + CORE-MEMORY.md + Faktortabelle + **STATE.md** + **score_history.jsonl** (+ ggf. **flag_events.jsonl**) aktualisieren, alles in einem git-Commit (STATE.md bei jeder Score/FLAG/Sparraten-Änderung). **score_history.jsonl-Write** via Skill `backtest-ready-forward-verify` (v3.7.2, seit 19.04.2026 — dynastie-depot Schritt 7). **flag_events.jsonl** weiterhin CLI-direkt via `03_Tools/backtest-ready/archive_flag.py`.
- **Briefing-Sync:** Vor Session-Ende `!SyncBriefing` falls 00_Core/ geändert wurde (§25). SessionEnd-Hook warnt automatisch.
- **Remote-Control (User-Trigger):** Wenn User `remote-Control` eingibt (oder sinngemäße Phrase „remote weiter"/„mobile weiter"), Remote-Routine mit State-Snapshot via `ccr` spawnen (Memory `remote-trigger-api.md`). Sonst kein automatischer Prompt — User-gesteuert, Zero-Overhead. Spawn-Mechanismus + Kontext-Scope final am Konsolidierungstag 24.04. festlegen.

## Kontinuierliches Lernen

| Tier | Speicherort | Wer schreibt | Wann gelesen | Pflege |
|------|------------|--------------|-------------|--------|
| 1. Auto-Memory | `~/.claude/.../memory/*.md` | Claude automatisch | Session-Start | Auto-Dream konsolidiert |
| 2. Applied Learning | `00_Core/APPLIED-LEARNING.md` | Manuell bei Review | On-Demand (per Routing-Table) | Monatlich + Kurator-Regel |
| 3. Formelle Regeln | `00_Core/INSTRUKTIONEN.md` §§ | Bei bewiesenem Bedarf | Per Routing-Table | Bei Systemänderungen |

Bullets, Pflege-Regeln, Promotion-Logik, Historie: siehe `00_Core/APPLIED-LEARNING.md`.

## Projektstruktur

- `00_Core/` — Kontext, Instruktionen, Gedächtnis (STATE, CORE-MEMORY, INSTRUKTIONEN, APPLIED-LEARNING, TOKEN-RULES, KONTEXT, Faktortabelle, SESSION-HANDOVER)
- `01_Skills/` — dynastie-depot · backtest-ready-forward-verify · insider-intelligence · non-us-fundamentals · quick-screener · `_extern/` (read-only)
- `02_Analysen/` — DEFCON-Analysen als Excel
- `03_Tools/` — Rebalancing · Satelliten-Monitor · Watchlist · Briefing-Hook · system_audit
- `04_Templates/` — SSoT aller Templates
- `05_Archiv/` — Historische Dateien
- `06_Skills-Pakete/` — Installierbare ZIP-Skills
- `07_Obsidian Vault/` — Wiki (71 Notes, Schema + Workflows via `WIKI-SCHEMA.md`)

## Routing-Table

> STATE.md immer. **Match-Regel (Hybrid):** exakte Trigger strikt; bare Ticker → `!QuickCheck`; Mehrfach-Match = Union der Lies-Spalten. Bei Trigger-Miss: konservativ mehr laden.

| Trigger | Lies zusätzlich | Skippe | Skill-Call |
|---------|-----------------|--------|------------|
| `Session starten` (default) | (Resume-Fall: SESSION-HANDOVER.md) | CORE-MEMORY, INSTRUKTIONEN, KONTEXT, Faktortabelle, Wissenschaftliche-Fundierung-DEFCON | — |
| `!Analysiere <Ticker>` | INSTRUKTIONEN.md, Faktortabelle.md, `…/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` | KONTEXT, CORE-MEMORY (außer §5 bei Scoring-Edge-Case) | `dynastie-depot` + `backtest-ready-forward-verify` (Schritt 7, programmatisch) |
| `!QuickCheck <Ticker>` | Faktortabelle.md | INSTRUKTIONEN, KONTEXT, CORE-MEMORY, Wiss-Fundierung | `quick-screener` |
| `!Rebalancing` | INSTRUKTIONEN.md, KONTEXT.md | CORE-MEMORY, Faktortabelle, Wiss-Fundierung | — |
| `!SyncBriefing` | INSTRUKTIONEN.md (§25) | alle anderen | — |
| Wiki-Ops (`ingest`/`lint`/`query`, „Vault"/„Obsidian"/„Faktortabelle-Edit"/„Score-Update"/„Insider scan"/„entity"/„Satellit Seite") | `07_Obsidian Vault/.../WIKI-SCHEMA.md` | INSTRUKTIONEN, KONTEXT, CORE-MEMORY (außer Wiki-Bezug) | je nach WIKI-SCHEMA-Workflow (`insider-intelligence`, `non-us-fundamentals`, …) |
| `remote-Control` / „mobile weiter" | Auto-Memory `remote-trigger-api.md` | alles andere (Snapshot reicht) | — (User-getriggerter `ccr`-Spawn) |
| Konsolidierungstag / System-Audit / Backlog-Review | SESSION-HANDOVER.md, STATE.md §Pipeline + §System | KONTEXT, Faktortabelle (außer ticker-spezifisch) | `SystemAudit` (slash) bei Audit-Lauf |
| Strategie-/Allokations-Frage | KONTEXT.md | Faktortabelle, Wiss-Fundierung | — |

**Edge-Cases der Match-Regel:**
- **Trigger + Wiki-Begriff** (z.B. „!Analysiere TMO und update Vault-Faktortabelle"): Union beider „Lies zusätzlich"-Spalten; Skip-Spalten verlieren Wirkung wenn anderer Trigger die Datei explizit anfordert; Skill-Calls beider Trigger ausführen.
- **Tippfehler / fast-exakte Trigger / Case-Drift / Sprach-Varianten** (z.B. `!Analysier`, `!Quickcheck`, `!analysiere`, `!Analyze TMO`): Kein Fuzzy-Match. Trigger sind strikt deutsch und PascalCase (`!Analysiere`, `!QuickCheck`, `!Rebalancing`, `!SyncBriefing`). Default-Verhalten + Rückfrage stellen („Meintest du `!Analysiere TMO`?"). Keine Selbstinterpretation.
- **Bare Symbol mit Wort-Ambiguität** (z.B. „V"): Soft-Match nur bei Symbolen aus den 11 aktuellen Satelliten-Tickern (siehe STATE.md Portfolio-Tabelle). Bei Zweifel Rückfrage.

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
| `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md` | Chronik vor 15.04.2026 (Projekt-Aufbau, Tool-Setups, erste Analysen) |

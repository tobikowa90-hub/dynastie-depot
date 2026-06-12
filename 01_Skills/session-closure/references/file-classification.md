# File-Classification Matrix

Klassifikation jedes Modified-/Untracked-Files in eine von vier Kategorien.
Triff Entscheidung **per File**, nicht per Ordner — manche Ordner mischen.

## Kategorie 1: scoring-relevant

Files mit Sync-Pflicht. Coupling-Trigger entscheidet, welches Sync-Set greift —
**nicht alle scoring-relevant-Files sind Score-Event-getriggert.**

### 1a — Score-Event-coupled (Trigger: `score_history.jsonl`-Mutation)

§18.1 v2.4 Pflicht-Set bei Score/FLAG/Sparraten-Change. Alle 8 müssen zusammen synchen:

| Pfad | Kommentar |
|------|-----------|
| `05_Archiv/score_history.jsonl` | Append-only Score-Records (via backtest-ready-forward-verify) — Trigger-File |
| `00_Core/PORTFOLIO.md` | Live-State (Score/DEFCON/Rate/FLAG je Satellit) |
| `00_Core/Faktortabelle.md` | Per-Ticker Faktor-Werte |
| `00_Core/CORE-MEMORY.md` | §5/§12 Score-/Earnings-Lifecycle |
| `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` | Narrative Lifecycle-Log |
| `01_Skills/dynastie-depot/config.yaml` | Per-Ticker Score/FLAG/Rate-SSoT für Skill |
| `03_Tools/Rebalancing_Tool` | xlsx-Tool (Sparpläne) — §18.1 Pflicht ab v2.4 |
| `03_Tools/Satelliten_Monitor` | xlsx-Tool (Depot-Übersicht) — §18.1 Pflicht ab v2.4 |

### 1b — FLAG-Event-coupled (Trigger: `flag_events.jsonl`-Mutation)

| Pfad | Kommentar |
|------|-----------|
| `05_Archiv/flag_events.jsonl` | Append-only FLAG-Trigger/Resolve (via `archive_flag.py`) — Trigger-File |
| `00_Core/PORTFOLIO.md` | FLAG-Spalte konsistent |
| `00_Core/CORE-MEMORY.md` | §12.<ticker> FLAG-Event-Bullet |

(FLAG ohne Score-Move löst NICHT das volle 8-File-Score-Set aus.)

### 1c — KONTEXT-coupled (Trigger: `00_Core/KONTEXT.md §6` Drop/Add/Reassign)

| Pfad | Kommentar |
|------|-----------|
| `00_Core/KONTEXT.md` | §6 Watchlist/Ersatzbank-State — Trigger-File |
| `03_Tools/Watchlist_Ersatzbank_Monitor` | xlsx-Spiegel — Memory `feedback_watchlist_xlsx_in_sync_set.md` |

**Wichtig:** Watchlist-xlsx ist **nicht** Score-Event-coupled. Wenn nur Watchlist + KONTEXT mutiert sind, **darf** Skill nicht das 8-File-Score-Set verlangen. Coupling-Check muss nach Trigger-File-Typ unterscheiden.

### 1d — Live-State-Edit ohne Event-Trigger

| Pfad | Kommentar |
|------|-----------|
| `00_Core/PORTFOLIO.md` (alleinige Edit ohne `score_history.jsonl`) | Watch-Hinzufügen, Sparplan-Notiz-Update etc. → kein Sync-Set-Pflicht, nur dieser File. |

**Sonderfall:** `PORTFOLIO.md` allein ist erlaubt. Coupling-Check (siehe `sync-coupling.md`)
entscheidet konkret anhand des Trigger-Files.

## Kategorie 2: doc-only

Files, die reine Dokumentation/Recherche-Materialien sind. Keine §18-Pflicht.

| Pfad-Pattern | Beispiel |
|-------------|----------|
| `02_Analysen/Earnings Reports/**/*` | Press-Release PDFs, Transkripte, Recap-Notes |
| `02_Analysen/Watchlist/**/*` | Watchlist-Recherche |
| `07_Obsidian Vault/**/*.md` außer `log.md` | Vault-Notes, Faktortabelle-Wiki-Spiegel (siehe Hinweis) |
| `Onboarding-Source-Docs/**/*` | Externe Quellen, Briefing-Materialien |
| `02_Analysen/Videos/**/*` | INGEST-VIDEO-Output (per `03_Tools/video_ingest.py`) |
| `*.pdf`, `*.txt`, `*.json` (research-data) | Quellmaterial |

**Hinweis Vault:** Faktortabelle-Wiki-Seiten im Vault sind doc-only (Spiegel),
aber `00_Core/Faktortabelle.md` ist scoring-relevant (SSoT). Vault `log.md` ist
scoring-relevant trotz Vault-Pfad.

## Kategorie 3: code

Files mit Logik/Schema/Executable. Brauchen pre-commit-Hook-Pass (mypy/black/etc.).

| Pfad-Pattern | Beispiel |
|-------------|----------|
| `03_Tools/**/*.py` | Backtest-Ready-Scripts, Skill-Helpers |
| `03_Tools/**/*.yaml`, `*.toml` (außer Tool-Outputs) | Config, pyproject |
| `01_Skills/**/SKILL.md` | Skill-Bodys (nicht config.yaml — die ist scoring-relevant) |
| `01_Skills/**/references/*.md` | Skill-References |
| `01_Skills/**/scripts/*.py` | Skill-Scripts |
| `06_Skills-Pakete/**/*.zip` | Installierbare Skill-Bundles |

## Kategorie 4: meta

Spec/Governance-Files. Pre-commit muss crlf-guard passen, sonst kein hartes Validator-Set.

| Pfad | Kommentar |
|------|-----------|
| `00_Core/INSTRUKTIONEN.md` | Tier-3-Regeln |
| `00_Core/CLAUDE.md` (Root: `CLAUDE.md`) | Session-Init + Routing |
| `00_Core/PIPELINE.md` | Pipeline-SSoT |
| `00_Core/SYSTEM.md` | System-Zustand |
| `00_Core/STATE.md` | Hub |
| `00_Core/KONTEXT.md` | Allokations-Logik |
| `00_Core/TOKEN-RULES.md` | Token-Effizienz-Regeln |
| `00_Core/APPLIED-LEARNING.md` | Tier-2 |
| `00_Core/SESSION-HANDOVER.md` | Resume-Doc |
| `00_Core/RETROSPECTIVE-GATE.md` | §29 Spec |
| `04_Templates/**` | Templates |
| `05_Archiv/CORE-MEMORY-Meilensteine-*.md` | Chronik (historisch) |

**Briefing-Trigger:** Mutation von `00_Core/**` außer `PORTFOLIO.md`/`Faktortabelle.md`/
`CORE-MEMORY.md` löst `!SyncBriefing`-Reminder aus (§25), blockiert aber nicht.

## Entscheidungs-Heuristik bei Ambiguität

1. Wenn der File in §18-Sync-Set-Liste → **scoring-relevant**.
2. Wenn `02_Analysen/**` ohne Code-Extension → **doc-only**.
3. Wenn `03_Tools/**` mit `.py`/`.yaml`/`.toml` → **code**. Wenn `.xlsx` → **scoring-relevant**.
4. Wenn `00_Core/**` und nicht in Sync-Set → **meta**.
5. Bei Zweifel: User fragen. Falsch-Klassifikation kann §18-Coupling falsch auslösen.

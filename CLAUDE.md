# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort **nur `00_Core/STATE.md`** — ohne Rückfrage. Diese Datei ist Single-Entry-Point und genügt für 90% der Sessions (Scores, DEFCON, FLAGs, Sparraten, Trigger, Watches).

**On-Demand-Lektüre** (nur wenn Kontext explizit gebraucht wird):
- `CORE-MEMORY.md` — Scoring-Lektionen (§5), Positions-Entscheidungen (§3), Audit-Log (§10), aktuelle Meilensteine ab 15.04. (§1)
- `INSTRUKTIONEN.md` — Scoring-Skalen, Sparplan-Formel, Workflows (bei `!Analysiere`, `!Rebalancing`)
- `KONTEXT.md` — Strategie, Allokation, Slot-Zuteilung (bei Strategie-Fragen)
- `Faktortabelle.md` — Detail-Metriken pro Ticker (bei Deep-Dive)
- `SESSION-HANDOVER.md` — Last-Session-Kontext (bei Fortsetzung)
- `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md` — Chronik vor 15.04. (Projekt-Aufbau, Tool-Setups, erste Analysen)

Danach: kompakte Zusammenfassung (max. 10 Zeilen) + **dynastie-depot**-Skill aktivieren.

## Verhalten

- `CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Sync-Pflicht:** Nach jeder Analyse: log.md + CORE-MEMORY.md + Faktortabelle + **STATE.md** + **score_history.jsonl** (+ ggf. **flag_events.jsonl**) aktualisieren, alles in einem git-Commit (STATE.md bei jeder Score/FLAG/Sparraten-Änderung, JSONL-Archive via `03_Tools/backtest-ready/archive_*.py`)
- **Briefing-Sync:** Vor Session-Ende `!SyncBriefing` falls 00_Core/ geändert wurde (§25). SessionEnd-Hook warnt automatisch.

## Projektstruktur

```
00_Core/            → Kontext, Instruktionen, Gedächtnis (IMMER zuerst lesen)
01_Skills/          → Skill-Quelldateien (Arbeitsversion)
  ├── dynastie-depot/       → Haupt-Skill (DEFCON-System)
  ├── insider-intelligence/ → Form-4-Scanner (8 US-Satelliten)
  ├── non-us-fundamentals/  → yfinance IFRS-Modul (ASML/RMS/SU)
  ├── quick-screener/       → Stufe-0-Vorfilter
  └── _extern/              → Fremd-Skills (read-only Referenz)
02_Analysen/        → DEFCON-Analysen als Excel
03_Tools/           → Rebalancing-Tool, Satelliten-Monitor, Watchlist, Briefing-Hook
04_Templates/       → Single-Source-of-Truth für alle Templates
05_Archiv/          → Historische Dateien
06_Skills-Pakete/   → Installierbare ZIP-Skills (Deployables)
07_Obsidian Vault/  → Investing Mastermind Wiki (71 Notes — Stand 15.04.2026)
  └── Obsidian Mindmap/Investing Mastermind/
      ├── WIKI-SCHEMA.md  → Schema + Workflows (bei Wiki-Ops lesen)
      ├── index.md        → Content-Katalog
      ├── wiki/           → Entitäten, Konzepte, Quellen, Synthesen
      └── raw/            → Quelldokumente (nie editieren)
```

## Wiki-Modus

**Aktivierung:** Bei Wiki-Operationen (`ingest`, `lint`, `query`, oder Begriffen wie "Wiki", "Vault", "Obsidian", "Seite anlegen", "Faktortabelle", "Score aktualisieren", "Insider scan", "entity", "Satellit Seite"):
→ `07_Obsidian Vault/WIKI-SCHEMA.md` lesen und den dortigen Workflows folgen.

Wiki-Modus und Dynasty-Depot-Modus schließen sich **nicht** aus.

## Token-Effizienz (operativ)

- **Snapshot-First:** STATE.md + Faktortabelle vor API — spart 3-5 Tool-Calls
- **Sync-Pflicht (alle sechs):** log.md + CORE-MEMORY.md + Faktortabelle + STATE.md + score_history.jsonl + flag_events.jsonl
- **Pause-Regel:** >5 Min → /compact (Preserve: Score/Tabelle/Urteil/FLAGs) oder /clear
- **DEFCON 1 Stopp:** Score <50 → Analyse stoppen (Insider-Modul läuft durch)
- **MCP:** Tool Search lädt lazy. Manuell deaktivieren nur bei Vault-Only-Sessions.
- **Modell:** Sonnet 4.6 default; `/model opus` für !Analysiere, Multi-Step-Refactors, strategische Entscheidungen.

## Kontinuierliches Lernen (3-Tier-System)

**Automatisch aktiv** (`autoMemoryEnabled + autoDreamEnabled`):

| Tier | Speicherort | Wer schreibt | Wann gelesen | Pflege |
|------|------------|--------------|-------------|--------|
| 1. Auto-Memory | `~/.claude/.../memory/*.md` | Claude automatisch | Session-Start | Auto-Dream konsolidiert |
| 2. Applied Learning | CLAUDE.md (diese Sektion) | Manuell bei Review | Session-Start | Monatlich: Obsoletes raus |
| 3. Formelle Regeln | INSTRUKTIONEN.md §§ | Bei bewiesenem Bedarf | Session-Start | Bei Systemänderungen |

**Promotion-Logik:** Auto-Memory → Applied Learning (wenn kritisch + wiederholbar) → INSTRUKTIONEN (wenn systemisch).

### Applied Learning (kuratiert, max. 20 Bullets)

> <15 Wörter pro Bullet. Nur operativ relevante Fakten.
>
> **Kurator-Regel bei Überlauf (20/20):** Hybrid-Strategie in dieser Reihenfolge anwenden: (1) Tool-References evakuieren → Auto-Memory oder INSTRUKTIONEN; (2) stabile API-/Regel-Bullets **promoten** → neue INSTRUKTIONEN-§; (3) thematisch verwandte Bullets **konsolidieren**. Ziel: 15/20 nach Revision. Archivierung ist kein Weg (toter Code).

- RemoteTrigger update ersetzt ccr-Objekt komplett — immer alle 3 Felder mitsenden
- JSON-Nesting: parent_tool_use_id/session_id/type/uuid auf data-Level, nie in message
- Yahoo Finance 403 von Cloud-IPs — curl aus Remote-Triggern funktioniert nicht
- Berkshire (BRK.B) fehlt komplett in Shibui — immer externen Provider nutzen
- Shibui code='SU' ist Suncor, nicht Schneider — nie SU in Shibui-Queries
- D3 = volle Rate (1.0), nicht 50% — systemweit seit v3.4 korrigiert
- SessionEnd-Hook + Windows-Toast für Briefing-Sync → 03_Tools/briefing-sync-check.ps1
- Subagents nur für Code+Tests — Markdown/YAML-Edits direkt editieren (3×Subagent-Overhead unnötig)
- Paper-Ingest ≠ System-Update: Wissenschaft validiert Regeln, erzwingt keine neuen — Redundanz-Check vor jeder Scoring-Erweiterung
- Double-Counting-Falle: Aggregat-Scores (z.B. F-Score) prüfen ob Sub-Signale schon dekomponiert im System sind
- Bonus-Cap-Check: Bei neuen Boni erst Punkteverteilung Top-Namen prüfen — sonst wirken Boni nur in Mitte
- Informationsverlust-Aversion > Ästhetik: bei Delete-vs-Keep Default = erhalten + Zeitstand-Banner
- Advisor-Empfehlung nicht ohne neue Evidenz überstimmen — Ästhetik-Argumente zählen nicht als Evidenz
- Vor "fertig"-Meldung Multi-Source-Drift-Grep (INSTRUKTIONEN/CORE-MEMORY §4/Vault-Synthesen/Tools) — config.yaml-Fix allein reicht nie
- Parallel-Agents für !Analysiere REJECTED 17.04.: ~270k Token + Screener-Exception-Fehler — Genauigkeit > Wall-Time
- Projection-Layer (STATE.md) ≠ Wahrheitsquelle — nur aus State+Narrative synchron halten, nie selbst fortschreiben (verhindert Drift)
- Backfill-Tolerant-Pattern für Cross-Validators: bei fehlenden Rohwerten moat.rating="narrow" → Quality-Trap-Validator deaktiviert, keine Schätzungen nötig

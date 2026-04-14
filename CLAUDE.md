# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort diese vier Dateien — ohne Rückfrage:

1. `00_Core/CORE-MEMORY.md` — institutionelles Gedächtnis, aktuelle Positionen, offene Trigger
2. `00_Core/KONTEXT.md` — Strategie, Allokation, Philosophie, Depot-Struktur
3. `00_Core/INSTRUKTIONEN.md` — Workflows, DEFCON-Regeln, Skill-Befehle
4. `00_Core/Faktortabelle.md` — aktueller Score-State aller Satelliten

Danach: kompakte Zusammenfassung (max. 10 Zeilen) + **dynastie-depot**-Skill aktivieren.
Fallback: Scheduled Task `dynastie-session-init` manuell starten.

## Verhalten

- `CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Sync-Pflicht:** Nach jeder Analyse: log.md + CORE-MEMORY.md + Faktortabelle aktualisieren

## Projektstruktur

```
00_Core/            → Kontext, Instruktionen, Gedächtnis (IMMER zuerst lesen)
01_Skills/          → Skill-Quelldateien (Arbeitsversion)
  ├── dynastie-depot/   → Haupt-Skill (DEFCON-System)
  ├── quick-screener/   → Stufe-0-Screener
  └── _extern/          → Installierte Fremd-Skills (read-only Referenz)
02_Analysen/        → DEFCON-Analysen als Excel
03_Tools/           → Rebalancing-Tool, Satelliten-Monitor, Watchlist
04_Templates/       → Single-Source-of-Truth für alle Templates
05_Archiv/          → Historische Dateien
06_Skills-Pakete/   → Installierbare ZIP-Skills (Deployables)
07_Obsidian Vault/  → Investing Mastermind Wiki (71 Notes)
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

## Token-Effizienz Kurzreferenz

- **Snapshot-First:** Faktortabelle vor API-Abfragen lesen — spart 3-5 Tool-Calls
- **MCP nach Bereich:** Analyse: Shibui+defeatbeta+WebSearch | Vault: filesystem | Code: Tool Search auto
- **/compact 60%:** Preserve Score/Tabelle/Urteil/FLAGs. Discard: rohe API-Outputs.
- **5-Min-Regel:** Vor Pause >5 Min: /compact oder /clear
- **DEFCON 1 Stopp:** Score <50 → Analyse stoppen (Insider-Modul läuft IMMER durch)
- **Sync-Pflicht:** log.md + CORE-MEMORY.md + Faktortabelle — immer alle drei
- **Morning Briefing:** Scheduled 10:00, ~15k Tokens/Tag. Manuell: `!Briefing`

## MCP-Session-Check

Bei Session-Start ausgeben:
```
Aktive MCP-Server: [/mcp ausführen und auflisten]
Analyse-Session benötigt: Shibui + defeatbeta + WebSearch
Vault-Session benötigt: filesystem
Nicht benötigt → /mcp disable [name]
Claude Code: Tool Search aktiv, automatisch.
```

## Applied Learning

> Max. 15 Wörter pro Bullet. Wird durch Nutzung befüllt.

*(leer — wird durch Session-Erfahrungen ergänzt)*

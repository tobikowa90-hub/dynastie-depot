# SESSION-INITIALISIERUNG — Dynasty-Depot Projekt

**PFLICHT bei `Session starten`:** Lies sofort diese vier Dateien — ohne Rückfrage:

1. `00_Core/CORE-MEMORY.md` — institutionelles Gedächtnis, aktuelle Positionen, offene Trigger
2. `00_Core/KONTEXT.md` — Strategie, Allokation, Philosophie, Depot-Struktur
3. `00_Core/INSTRUKTIONEN.md` — Workflows, DEFCON-Regeln, Skill-Befehle
4. `00_Core/Faktortabelle.md` — aktueller Score-State aller Satelliten

Danach: kompakte Zusammenfassung (max. 10 Zeilen) + **dynastie-depot**-Skill aktivieren.

## Verhalten

- `CORE-MEMORY.md` **live** fortschreiben — sofort bei relevanten Ereignissen
- Stil: direkt, faktenbasiert, kein Filler — siehe INSTRUKTIONEN.md
- **Sync-Pflicht:** Nach jeder Analyse: log.md + CORE-MEMORY.md + Faktortabelle aktualisieren
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

## Token-Effizienz Kurzreferenz

- **Snapshot-First:** Faktortabelle vor API-Abfragen lesen — spart 3-5 Tool-Calls
- **MCP nach Bereich:** Analyse: Shibui+defeatbeta+WebSearch | Vault: filesystem | Code: Tool Search auto
- **/compact 60%:** Preserve Score/Tabelle/Urteil/FLAGs. Discard: rohe API-Outputs.
- **5-Min-Regel:** Vor Pause >5 Min: /compact oder /clear
- **DEFCON 1 Stopp:** Score <50 → Analyse stoppen (Insider-Modul läuft IMMER durch)
- **Sync-Pflicht:** log.md + CORE-MEMORY.md + Faktortabelle — immer alle drei
- **Morning Briefing:** Remote Trigger v2.1, täglich 10:00 MESZ. Manuell: `!Briefing`

## MCP-Session-Check

Bei Session-Start ausgeben:
```
Aktive MCP-Server: [/mcp ausführen und auflisten]
Analyse-Session benötigt: Shibui + defeatbeta + WebSearch
Vault-Session benötigt: filesystem
Nicht benötigt → /mcp disable [name]
Claude Code: Tool Search aktiv, automatisch.
```

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

- RemoteTrigger update ersetzt ccr-Objekt komplett — immer alle 3 Felder mitsenden
- JSON-Nesting: parent_tool_use_id/session_id/type/uuid auf data-Level, nie in message
- Yahoo Finance 403 von Cloud-IPs — curl aus Remote-Triggern funktioniert nicht
- Berkshire (BRK.B) fehlt komplett in Shibui — immer externen Provider nutzen
- Shibui code='SU' ist Suncor, nicht Schneider — nie SU in Shibui-Queries
- D3 = volle Rate (1.0), nicht 50% — systemweit seit v3.4 korrigiert
- SessionEnd-Hook + Windows-Toast für Briefing-Sync → 03_Tools/briefing-sync-check.ps1
- Subagents nur für Code+Tests — Markdown/YAML-Edits direkt editieren (3×Subagent-Overhead unnötig)
- Skill-ZIP: Hauptdatei muss `SKILL.md` heißen (nicht SKILL-dynasty-depot.md). Desktop App liest aus AppData-Pfad, nicht ~/.claude/
- Paper-Ingest ≠ System-Update: Wissenschaft validiert Regeln, erzwingt keine neuen — Redundanz-Check vor jeder Scoring-Erweiterung
- Double-Counting-Falle: Aggregat-Scores (z.B. F-Score) prüfen ob Sub-Signale schon dekomponiert im System sind
- Bonus-Cap-Check: Bei neuen Boni erst Punkteverteilung Top-Namen prüfen — sonst wirken Boni nur in Mitte

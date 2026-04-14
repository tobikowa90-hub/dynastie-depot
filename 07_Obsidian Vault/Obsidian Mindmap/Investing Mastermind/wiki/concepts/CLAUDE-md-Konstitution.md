---
title: "CLAUDE.md Konstitution"
type: concept
tags: [system, claude, konfiguration, session-management]
related: "[[Context-Hygiene]], [[Token-Mechanik]], [[Context-Hygiene-Code]]"
defcon_block: "System-Konfiguration"
operative_regel: "CLAUDE.md ist die einzige Wahrheitsquelle für Session-Verhalten — jede strukturelle Änderung sofort dort dokumentieren."
---

# CLAUDE.md Konstitution

## Definition
CLAUDE.md ist die primäre Konfigurationsdatei für das Verhalten von Claude-Sessions im Dynasty-Depot-Projekt. Sie definiert Session-Initialisierung, Wiki-Modus-Trigger, Token-Effizienz-Regeln und MCP-Session-Check. Als "Konstitution" hat sie Vorrang vor allen anderen Anweisungen in der Session — außer expliziten User-Befehlen.

## Struktur (Pflicht-Sektionen)

| Sektion | Inhalt | Priorität |
|---------|--------|-----------|
| SESSION-INITIALISIERUNG | 4 Pflicht-Lektüren + Zusammenfassung | Kritisch |
| Wiki-Modus | Trigger-Wörter + 4-Schritt-Workflow | Hoch |
| Token-Effizienz Kurzreferenz | 6 Bullets, operativ | Hoch |
| MCP-Session-Check | Ausgabe bei Session-Start | Mittel |
| Applied Learning | Lessons-Learned-Sammlung | Niedrig |

## 4 Pflicht-Lektüren (Session-Init)

```
1. 00_Core/CORE-MEMORY.md
2. 00_Core/KONTEXT.md
3. 00_Core/INSTRUKTIONEN.md
4. 00_Core/Faktortabelle.md  ← NEU seit 2026-04-14
```

## Wiki-Modus-Trigger (vollständig)

Auslösende Begriffe: `ingest`, `lint`, `query`, `Wiki`, `Vault`, `Obsidian`, `Seite anlegen`, `Faktortabelle`, `Score aktualisieren`, `Insider scan`, `entity`, `Satellit Seite`

## Änderungsprotokoll

| Datum | Änderung |
|-------|---------|
| 2026-04-14 | Faktortabelle als 4. Pflicht-Lektüre hinzugefügt |
| 2026-04-14 | Token-Effizienz Kurzreferenz + MCP-Session-Check + Applied Learning hinzugefügt |
| 2026-04-14 | Wiki-Modus-Trigger um 5 Begriffe erweitert |

## Backlinks
- [[Context-Hygiene]] — Context-Regeln operationalisiert in CLAUDE.md
- [[Token-Mechanik]] — Token-Kurzreferenz-Quelle
- [[Context-Hygiene-Code]] — Claude Code-Spezifika

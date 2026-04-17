---
title: "CLAUDE.md Konstitution"
type: concept
tags: [system, claude, konfiguration, session-management]
related: "[[Context-Hygiene]], [[Token-Mechanik]], [[Context-Hygiene-Code]], [[Session-Start-Protokoll]], [[Faktortabelle-Architektur]], [[INSTRUKTIONEN-SKILL-Trennung]]"
defcon_block: "System-Konfiguration"
operative_regel: "CLAUDE.md ist die einzige Wahrheitsquelle für Session-Verhalten — jede strukturelle Änderung sofort dort dokumentieren. Seit 17.04.2026: Session-Init liest nur STATE.md, andere 00_Core-Dateien on-demand."
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

## Session-Init: STATE.md-First (Stand 17.04.2026)

Seit **17.04.2026** liest Claude beim Session-Start **nur `00_Core/STATE.md`** — Einzelheiten siehe [[Session-Start-Protokoll]]. Die 4-Datei-Architektur wurde abgelöst, weil sie ~1.200 Zeilen Auto-Read pro Session erzwang, von denen 99% nicht gebraucht wurden.

**Frühere 4 Pflicht-Lektüren** (jetzt on-demand):

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
| 2026-04-17 | STATE.md-First Session-Init (ersetzt 4-Datei-Auto-Read); CORE-MEMORY §1-Archivierung |
| 2026-04-17 | Post-STATE Konsolidierung: Token-Block verdichtet, MCP-Session-Check zu 1 Bullet, Applied Learning 12→11 (SKILL-Rename obsolet), Modell-Toggle-Bullet ergänzt — siehe [[INSTRUKTIONEN-SKILL-Trennung]] |

## Backlinks
- [[Context-Hygiene]] — Context-Regeln operationalisiert in CLAUDE.md
- [[Token-Mechanik]] — Token-Kurzreferenz-Quelle
- [[Context-Hygiene-Code]] — Claude Code-Spezifika

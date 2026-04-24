---
title: "CLAUDE.md Konstitution"
type: concept
tags: [system, claude, konfiguration, session-management]
related: "[[Context-Hygiene]], [[Token-Mechanik]], [[Context-Hygiene-Code]], [[Session-Start-Protokoll]], [[Faktortabelle-Architektur]], [[INSTRUKTIONEN-SKILL-Trennung]]"
defcon_block: "System-Konfiguration"
operative_regel: "CLAUDE.md ist die einzige Wahrheitsquelle für Session-Verhalten — jede strukturelle Änderung sofort dort dokumentieren. Seit 17.04.2026: Session-Init liest nur STATE.md, andere 00_Core-Dateien on-demand. Seit 24.04.2026 (Tier-1-Refactor): 71-Zeilen-Hub mit Routing-Table + Pointer; Applied-Learning und Token-Rules ausgelagert nach `00_Core/APPLIED-LEARNING.md` + `00_Core/TOKEN-RULES.md`."
---

# CLAUDE.md Konstitution

## Definition
CLAUDE.md ist die primäre Konfigurationsdatei für das Verhalten von Claude-Sessions im Dynasty-Depot-Projekt. Sie definiert Session-Initialisierung, Wiki-Modus-Trigger, Token-Effizienz-Regeln und MCP-Session-Check. Als "Konstitution" hat sie Vorrang vor allen anderen Anweisungen in der Session — außer expliziten User-Befehlen.

## Struktur (Top-Level-Sektionen, Tier-1-Refactor 24.04.2026)

| # | Sektion | Inhalt | Priorität |
|---|---------|--------|-----------|
| 1 | SESSION-INITIALISIERUNG | Pflicht-Read STATE.md + Skill-Aktivierung | Kritisch |
| 2 | Verhalten | Sync-Pflicht, CORE-MEMORY live, Briefing-Sync §25, Remote-Control | Hoch |
| 3 | Kontinuierliches Lernen | 3-Tier-Tabelle (Auto-Memory / Applied-Learning / Instruktionen) | Hoch |
| 4 | Projektstruktur | Ordner-Map `00_Core/` bis `07_Obsidian Vault/` | Mittel |
| 5 | Routing-Table | 9 Trigger × (Lies / Skippe / Skill-Call) + Hybrid-Match + Edge-Cases | Kritisch |
| 6 | Wiki-Modus | Trigger-Begriffe + Pointer zu `WIKI-SCHEMA.md` | Hoch |
| 7 | Pointer (Ausgelagertes) | Fuß-Tabelle → APPLIED-LEARNING / TOKEN-RULES / INSTRUKTIONEN / Meilensteine-Archiv | Mittel |

## Session-Init: STATE.md-First (Stand 17.04.2026)

Seit **17.04.2026** liest Claude beim Session-Start **nur `00_Core/STATE.md`** — Einzelheiten siehe [[Session-Start-Protokoll]]. Die 4-Datei-Architektur wurde abgelöst, weil sie ~1.200 Zeilen Auto-Read pro Session erzwang, von denen 99% nicht gebraucht wurden.

**Frühere 4 Pflicht-Lektüren** (jetzt on-demand):

```
1. 00_Core/CORE-MEMORY.md
2. 00_Core/KONTEXT.md
3. 00_Core/INSTRUKTIONEN.md
4. 00_Core/Faktortabelle.md  ← NEU seit 2026-04-14
```

## Routing-Table + Auslagerung (Tier-1-Refactor, Stand 24.04.2026)

Der **Tier-1-Refactor 24.04.2026** (Spec `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md`, Plan `docs/superpowers/plans/2026-04-24-claude-md-routing-refactor.md`) hat CLAUDE.md von 97 auf **71 Zeilen** verdichtet und drei strukturelle Änderungen gebracht:

1. **Routing-Table ersetzt On-Demand-Lektüre-Liste.** Statt in Prose zu beschreiben, was „bei Rebalancing zusätzlich gelesen wird", definiert eine 9-Trigger-Tabelle pro Trigger die Spalten „Lies zusätzlich", „Skippe" und „Skill-Call". **Hybrid-Match-Regel:** exakte Trigger strikt; bare Ticker → `!QuickCheck`; Mehrfach-Match = Union der Lies-Spalten; bei Trigger-Miss konservativ mehr laden.
2. **Zwei neue SSoT-Dateien** (Auslagerung):
   - `00_Core/APPLIED-LEARNING.md` (Tier-2-SSoT, 14/20 Bullets + Pflege-Regeln + Historie v1.0–v2.5)
   - `00_Core/TOKEN-RULES.md` (**Accessibility-Modell, kein Enforcement** — Regeln liegen vor, via Pointer nachlesbar)
3. **Neue Fuß-Sektion `## Pointer (Ausgelagertes)`** — 4 Zeilen: APPLIED-LEARNING, TOKEN-RULES, INSTRUKTIONEN, Meilensteine-Archiv.

**Deferred (nicht in Tier 1):** Tier-2 STATE-Split Variante-B-Hub (`STATE.md` → ~10-Z-Hub + `PORTFOLIO.md`/`PIPELINE.md`/`SYSTEM.md`). Tier-2b CORE-MEMORY-Subkategorisierung. Eigene Brainstorm-Session — siehe STATE.md Pipeline-Deferred #12 „00_Core Perfect-Organization".

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
| 2026-04-24 | **Tier-1-Refactor:** 97→71 Zeilen · Routing-Table (9 Trigger + Hybrid-Match + 3 Edge-Cases) ersetzt On-Demand-Lektüre · neue SSoT `APPLIED-LEARNING.md` + `TOKEN-RULES.md` (Accessibility-Modell) · neue `## Pointer (Ausgelagertes)`-Sektion · 7 Top-Level-Sektionen. Spec/Plan: `2026-04-24-claude-md-routing-refactor-*`. Tier-2 STATE-Split deferred. |

## Backlinks
- [[Context-Hygiene]] — Context-Regeln operationalisiert in CLAUDE.md
- [[Token-Mechanik]] — Token-Kurzreferenz-Quelle
- [[Context-Hygiene-Code]] — Claude Code-Spezifika

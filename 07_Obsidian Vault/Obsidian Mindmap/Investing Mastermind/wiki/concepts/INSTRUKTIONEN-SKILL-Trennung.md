---
tags: [concept, architektur, token-effizienz, dedup, workflow]
stand: 2026-04-17
typ: konzept
---

# INSTRUKTIONEN ↔ SKILL Trennung (Post-Dedup 17.04.2026)

> Arbeitsteilung nach der INSTRUKTIONEN-SKILL-Deduplication vom 17.04.2026. Ergebnis des Token-Strategie-Refactors nach STATE.md-Einführung.

## Grundsatz

Zwei Dokumente — zwei Rollen, kein Duplikat.

| Dokument | Rolle | Typische Inhalte |
|----------|-------|------------------|
| `00_Core/INSTRUKTIONEN.md` | **User-Workflow-Doku** — das WIE aus Nutzersicht | Befehls-Übersicht, Pipeline, Quick-Screener, !Rebalancing, !QuickCheck, CapEx-FCF, config-Pflege, Kalibrierungsanker, Skill-Hierarchie, Update-Klassen, Sparplan-Formel (aktueller Stand), Morning Briefing, Briefing-Sync |
| `01_Skills/dynastie-depot/SKILL.md` | **Scoring-Technik (Single Source of Truth)** — das WIE aus Engine-Sicht | DEFCON-Matrix, Detailskalen, Quality-Trap-Interaktion, Fundamentals-Cap, FLAG-Regeln, API-Routing, Pre-Processing, Quarterly Sanity Check, Verhaltensregeln, Value Legends |

## Entscheidungsregel bei neuen Inhalten

- **Beschreibt Inhalt eine Scoring-Mechanik, eine FLAG-Regel, eine API-Semantik?** → nur SKILL.md
- **Beschreibt Inhalt einen User-Workflow, einen Befehl, eine Meta-Regel (Sync, Briefing, Skill-Hierarchie)?** → nur INSTRUKTIONEN.md
- **Beides?** → Kernlogik in SKILL, Kurz-Trigger + Cross-Ref in INSTRUKTIONEN

## Cross-Referenzen

INSTRUKTIONEN verlinkt auf SKILL.md Sektionen per relativem Pfad: `[SKILL.md §X](../01_Skills/dynastie-depot/SKILL.md)`. 10 Cross-Refs aktiv nach Dedup.

## Motivation

1. **Token-Effizienz:** Kein doppeltes Laden bei !Analysiere (SKILL wird geladen) + Session-Start (INSTRUKTIONEN on-demand).
2. **Wartbarkeit:** Eine Änderung an Quality-Trap-Regel = eine Datei, nicht zwei.
3. **Drift-Vermeidung:** Historische Fehler (z.B. D3-Rate 50% in INSTRUKTIONEN, 100% in SKILL) nicht wiederholbar.

## Ergebnis

- INSTRUKTIONEN.md: 587 → 452 Zeilen (-23%)
- Keine Dubletten bei Scoring-Skalen, FLAG-Regeln, Sentiment v3.7, Quality-Trap, Tariff, API Sanity Check, Verhaltensregeln
- SKILL.md Cashless-Exercise-Ausnahme ergänzt (Nuance aus §6 preserved)

## Verlinkungen

- [[CLAUDE-md-Konstitution]] — Meta-Regelwerk
- [[Session-Start-Protokoll]] — STATE.md als Single-Entry-Point
- [[Faktortabelle-Architektur]] — Snapshot-First-Prinzip
- [[Context-Hygiene]] — Token-Regeln
- [[dynastie-depot-skill]] — SKILL v3.7 Monolith-Definition

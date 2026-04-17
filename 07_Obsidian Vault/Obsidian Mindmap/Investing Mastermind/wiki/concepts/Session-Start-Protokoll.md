---
title: "Session-Start-Protokoll — STATE.md als Single-Entry-Point"
type: concept
tags: [token-effizienz, session-management, snapshot-first, claude-md]
related: "[[CLAUDE-md-Konstitution]], [[Faktortabelle-Architektur]], [[Context-Hygiene]], [[Token-Mechanik]], [[Update-Klassen-DEFCON]]"
defcon_block: "System-Konfiguration"
operative_regel: "Session-Start liest nur STATE.md (≈40 Zeilen). Andere 00_Core-Dateien on-demand. Spart ~80% Auto-Read-Token gegenüber 4-Datei-Auto-Load."
---

# Session-Start-Protokoll — STATE.md als Single-Entry-Point

## Definition

Seit **17.04.2026** liest Claude beim Session-Start **ausschließlich `00_Core/STATE.md`** — einen ~40-Zeiler, der Scores, DEFCON-Stufen, FLAGs, Sparraten, nächste Trigger und aktive Watches enthält. Die bis dahin üblichen 4 Pflicht-Lektüren (CORE-MEMORY + KONTEXT + INSTRUKTIONEN + Faktortabelle, zusammen ~1.200 Zeilen) sind **on-demand** geworden.

## Motivation

Der alte 4-Datei-Auto-Read beim Session-Start verbrannte bei jeder Eröffnung massiv Token für historische Meilensteine, die in 99% der Sessions nicht gebraucht wurden. Konkret:

| Datei | Zeilen | Relevanz pro Session |
|-------|--------|----------------------|
| CORE-MEMORY.md (alt) | ~362 | 70% historische Chronik (Section 1), 30% operativ |
| INSTRUKTIONEN.md | ~588 | nur bei `!Analysiere`/`!Rebalancing` nötig |
| KONTEXT.md | ~148 | nur bei Strategie-Fragen nötig |
| Faktortabelle.md | ~114 | nur bei Deep-Dive nötig |
| **Summe Auto-Load** | **~1.212** | **Realbedarf: ~40 Zeilen Snapshot** |

→ Token-Overload ohne Nutzen. Applied Learning 17.04.2026: **Snapshot-First konsequent umsetzen**.

## Architektur

```
Session-Start
     ↓
00_Core/STATE.md (IMMER — ~40 Zeilen Snapshot)
     ↓
On-Demand (nur bei expliziter Anfrage):
  ├─ CORE-MEMORY.md §§2–10 (Lektionen, Positions-Entscheidungen, Audit-Log)
  ├─ CORE-MEMORY.md §1 (nur Einträge ab 15.04.2026)
  ├─ INSTRUKTIONEN.md (Scoring-Skalen, Workflows)
  ├─ KONTEXT.md (Strategie, Allokation)
  ├─ Faktortabelle.md (Detail-Metriken)
  ├─ SESSION-HANDOVER.md (Last-Session-Kontext)
  └─ 05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md (Chronik <15.04.)
```

## STATE.md — Inhalt (Pflicht-Sektionen)

| Block | Inhalt |
|-------|--------|
| Portfolio-State | 11 Satelliten: Score, DEFCON, Rate, FLAG, nächster Trigger |
| Sparraten-Nenner | aktueller Divisor + Einzelraten + Summencheck |
| Aktive Watches | Grenzfälle (z.B. ASML Fwd P/E FY27 30,30), FLAG-Review-Pfade |
| Nächste kritische Trigger | 30-Tage-Horizont, Klassifikation |
| System-Zustand | Scoring-Version, Live-Verify-Fortschritt, Allokation, MCP |
| Navigation | Pointer-Tabelle: "Wenn du brauchst… lies…" |

## Sync-Pflicht (erweitert)

Die **Sync-Pflicht** umfasst jetzt **4 Dateien** (statt 3):

1. `log.md` — technisches Protokoll (Vault)
2. `CORE-MEMORY.md` — strategisches Gedächtnis
3. `Faktortabelle.md` — Score-Snapshot
4. **`STATE.md`** — Live-Snapshot (bei jeder Score/FLAG/Sparraten-Änderung)

→ Bei DEFCON-Analyse oder FLAG-Trigger **alle vier** aktualisieren. Siehe [[Faktortabelle-Architektur]] für die darunterliegende Snapshot-First-Logik.

## Beziehung zu anderen Konzepten

- **[[Faktortabelle-Architektur]]** — gleiche Token-Einsparungs-Logik auf Ticker-Metrik-Ebene; STATE.md ist die aggregierte Ebene darüber
- **[[CLAUDE-md-Konstitution]]** — Session-Initialisierung-Section wurde von "4 Pflicht-Lektüren" auf "nur STATE.md" umgestellt (17.04.2026)
- **[[Context-Hygiene]]** — Hauptprinzip: nur laden, was in der Session gebraucht wird
- **[[Update-Klassen-DEFCON]]** — STATE.md ist Klasse-A/B-Primary-Sink (quartals-/earnings-getriggerte Updates landen hier zuerst)
- **[[Token-Mechanik]]** — Snapshot-First als operative Umsetzung der Token-Effizienz

## Verhalten bei Migration (17.04.2026)

- CORE-MEMORY.md Section 1: alle Meilensteine vor 15.04.2026 → `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md`. Mapping-Tabelle dokumentiert, wo jede Lektion permanent lebt (Sections 2–10, INSTRUKTIONEN, Vault).
- **Kein Kontext-Verlust:** Archiv + Permanent-Referenzen + Verweis-Block in CORE-MEMORY §1.
- CLAUDE.md Session-Init-Regel umformuliert.
- Neue Sync-Pflicht in CLAUDE.md "Verhalten"-Block.

## Trade-off

**Gewinn:** ~80% weniger Auto-Read-Token pro Session-Start. Session-Briefing in <10 Zeilen möglich.

**Kosten:** Bei komplexen Analysen muss Claude explizit eine Zusatzquelle laden (z.B. "§5 Fundamentals-Skala"). Der `dynastie-depot`-Skill enthält die operativen Skalen aber bereits im SKILL-Text — in der Praxis fast verlustfrei.

---
*🦅 Session-Start-Protokoll | Vault-Konzept | Stand: 17.04.2026*

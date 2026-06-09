---
title: "Session-Start-Protokoll — Hub + PORTFOLIO Default-Load"
type: concept
tags: [token-effizienz, session-management, snapshot-first, claude-md]
sources: []
related:
  - "[[CLAUDE-md-Konstitution]]"
  - "[[Faktortabelle-Architektur]]"
  - "[[Context-Hygiene]]"
  - "[[Token-Mechanik]]"
  - "[[Update-Klassen-DEFCON]]"
defcon_block: "System-Konfiguration"
operative_regel: "Session-Start liest STATE.md (Hub, ~40 Z) + PORTFOLIO.md (Live-State). Andere 00_Core-Dateien on-demand via Routing-Table. Spart ~80% Auto-Read-Token gegenüber 4-Datei-Auto-Load."
---

# Session-Start-Protokoll — Hub + PORTFOLIO Default-Load

## Definition

Seit **17.04.2026** ist der Session-Start auf einen Snapshot-First-Pfad umgestellt — initial las Claude nur `00_Core/STATE.md` als Single-Entry-Point. Mit dem **Tier-2-00_Core-Refactor 25.04.2026** wurde der Live-Zustand in [[PORTFOLIO]] ausgelagert; STATE.md bleibt als **Hub** (~40 Z, Verweise + Critical-Alerts + Last-Audit). Aktueller Pflicht-Pfad: **STATE.md (Hub) + PORTFOLIO.md (default-load, Live-State)**. Die früher üblichen 4 Pflicht-Lektüren (CORE-MEMORY + KONTEXT + INSTRUKTIONEN + Faktortabelle, ~1.200 Zeilen) sind **on-demand** via [[CLAUDE-md-Konstitution|CLAUDE.md `## Routing-Table`]].

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
00_Core/STATE.md (IMMER — Hub: Verweise + Critical-Alerts + Last-Audit, ~40 Z)
00_Core/PORTFOLIO.md (default-load — Live-State: Scores, FLAGs, Sparraten, Watches, 30-Tage-Trigger)
     ↓
On-Demand via CLAUDE.md `## Routing-Table` (trigger-spezifisch):
  ├─ PIPELINE.md (Offene Pläne, Long-Term-Gates)
  ├─ SYSTEM.md (DEFCON-Version, MCP, Briefing, Backtest, R5, Backlog)
  ├─ CORE-MEMORY.md §§2–13 (§5 Lektionen / §12 Per-Ticker-Chronik / §13 System-Lifecycle)
  ├─ INSTRUKTIONEN.md (Scoring-Skalen, Workflows, §18 v2.1 Sync-Pflicht)
  ├─ KONTEXT.md (Strategie, Allokation)
  ├─ Faktortabelle.md (Detail-Metriken)
  ├─ SESSION-HANDOVER.md (Resume-Fall)
  └─ 05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md (Chronik <15.04.)
```

## STATE.md (Hub) — Inhalt

| Block | Inhalt |
|-------|--------|
| Verweise | Pointer auf PORTFOLIO / PIPELINE / SYSTEM / CORE-MEMORY / SESSION-HANDOVER |
| ⚠️ Critical-Alerts | ≤ 10 Tage, handgepflegt (Earnings, FLAG-Reviews, D2-Entscheidungen) |
| Navigation | "Wenn du brauchst… lies…"-Tabelle |
| Last Audit | `system_audit.py`-Timestamp + Result + Run-Variante |

## PORTFOLIO.md — Live-State (default-load)

| Block | Inhalt |
|-------|--------|
| Portfolio-Tabelle | 13 Satelliten: Score, DEFCON, Rate, FLAG, nächster Trigger |
| Sparraten-Nenner | aktueller Divisor + Einzelraten + Summencheck |
| Aktive Watches | Grenzfälle (z.B. ASML Fwd P/E FY27 30,30), FLAG-Review-Pfade |
| 30-Tage-Trigger | klassifizierte Earnings-/Watch-Termine |
| Allokation | 60/35/5 Ziel + US-Hard-Cap-Check |

## Sync-Pflicht (§18 v2.1, Trigger-basiertes Mapping)

Statt pauschaler 6er-Liste definiert §18 v2.1 **Pflicht-Listen pro Event-Typ**. Score/FLAG/Sparraten-Change-Set:

1. `log.md` — technisches Protokoll (Vault)
2. `CORE-MEMORY.md` — Lektionen / Per-Ticker-Chronik (§12) / Lifecycle (§13)
3. `Faktortabelle.md` — Score-Snapshot
4. **`PORTFOLIO.md`** — Live-Snapshot (Tier-2-Migration vom STATE.md aus April-2026)
5. `score_history.jsonl` — append-only via Skill `backtest-ready-forward-verify`
6. `01_Skills/dynastie-depot/config.yaml` — Score/DEFCON/FLAG-Persistenz
7. _conditional:_ `flag_events.jsonl` (bei FLAG-Trigger/Resolve)

Multi-Event-Aktionen (Score-Change + Pipeline-Item gleichzeitig) = **Union** der File-Sets. Pipeline-Item-Changes → PIPELINE.md + log.md. System-Zustand-Changes → SYSTEM.md + log.md. Details: [INSTRUKTIONEN §18 v2.1](../../../../00_Core/INSTRUKTIONEN.md). Snapshot-First-Logik: [[Faktortabelle-Architektur]].

## Beziehung zu anderen Konzepten

- **[[Faktortabelle-Architektur]]** — gleiche Token-Einsparungs-Logik auf Ticker-Metrik-Ebene; PORTFOLIO.md ist die aggregierte Live-State-Ebene darüber
- **[[CLAUDE-md-Konstitution]]** — Session-Initialisierung-Section auf "Hub + PORTFOLIO default-load" umgestellt (17.04. STATE-First → 25.04. Tier-2-Hub-Split)
- **[[Context-Hygiene]]** — Hauptprinzip: nur laden, was in der Session gebraucht wird
- **[[Update-Klassen-DEFCON]]** — PORTFOLIO.md ist Klasse-A/B-Primary-Sink (quartals-/earnings-getriggerte Updates landen hier zuerst)
- **[[Token-Mechanik]]** — Snapshot-First als operative Umsetzung der Token-Effizienz

## Migrations-Historie

**17.04.2026 — STATE-First Session-Init:**
- CORE-MEMORY.md Section 1 (alt): Meilensteine vor 15.04.2026 → `05_Archiv/CORE-MEMORY-Meilensteine-bis-14.04.2026.md`
- CLAUDE.md Session-Init-Regel umformuliert: 4-Datei-Auto-Read → STATE.md-First
- Neue Sync-Pflicht in CLAUDE.md "Verhalten"-Block

**25.04.2026 — Tier-2-00_Core-Refactor (Hub-Split):**
- STATE.md (159 Z → 40 Z Hub) — Live-Inhalte ausgelagert in 3 Satelliten:
  - `PORTFOLIO.md` (Live-State, default-load)
  - `PIPELINE.md` (Offene Pläne, Long-Term-Gates)
  - `SYSTEM.md` (DEFCON-Version, MCP, Briefing, Backtest, R5, Backlog)
- CORE-MEMORY.md §1 → §12 (Per-Ticker-Chronik) + §13 (System-Lifecycle-History) — Topic-Auflösung statt Chronologie
- INSTRUKTIONEN §18 v2.1 — Trigger-basiertes Sync-Mapping + Multi-Event-Union-Regel + `config.yaml` im Score-Event-Set
- Skill-Bumps: dynastie-depot v3.7.3, backtest-ready-forward-verify v1.0.1
- **Kein Kontext-Verlust:** Archiv + Permanent-Referenzen + Tier-2-Plan in `docs/superpowers/plans/2026-04-24-00core-perfect-organization.md`

## Trade-off

**Gewinn:** ~80% weniger Auto-Read-Token pro Session-Start. Session-Briefing in <10 Zeilen möglich. Hub+PORTFOLIO-Split macht Critical-Alerts und Live-State semantisch trennbar.

**Kosten:** Bei komplexen Analysen muss Claude explizit eine Zusatzquelle laden (z.B. "§5 Fundamentals-Skala"). Der `dynastie-depot`-Skill enthält die operativen Skalen aber bereits im SKILL-Text — in der Praxis fast verlustfrei.

---
*🦅 Session-Start-Protokoll | Vault-Konzept | Stand: 25.04.2026 (Tier-2-Hub-Split)*

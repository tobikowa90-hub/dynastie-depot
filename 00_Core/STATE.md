# 🎯 STATE.md — Dynasty-Depot Hub

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — Offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Infrastruktur / Briefing / Backtest-Ready
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13)
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Banner-Chronik

## ⚠️ Critical-Alerts (≤ 10 Tage — handgepflegt)
- **29.04.** MSFT Q3 FY26 — FLAG-Review (CapEx/OCF bereinigt <60% = Auflösung)
- **29.04.** APH Q1 FY26 — DONE Tag-0-Recap (Earnings-Calendar-Drift detektiert, Trigger stand auf 23.07. Q2)
- **30.04.** APH Q1 FY26 Vollanalyse Tag +1 (§19.1) — Sub-Score-Refresh, Methodology-Watch China-Tax/CommScope-Leverage

## Navigation (on-demand)
| Wenn du brauchst… | Lies… |
|---|---|
| Scores / FLAGs / Watches / Sparraten / 30-Tage-Trigger | **PORTFOLIO.md** (default-load) |
| Offene Pläne, Gates, Primary-Track | PIPELINE.md |
| System-Versionen, Briefing-Status, Infra | SYSTEM.md |
| Lektionen / Per-Ticker-Chronik / Lifecycle | CORE-MEMORY.md (§5 / §12 / §13) |
| Workflows / Sparraten-Formel / Sync-Pflicht | INSTRUKTIONEN.md |
| Strategie / Allokation | KONTEXT.md (on-demand) |
| Score-Detail pro Ticker | Faktortabelle.md |

**Sync-Pflicht (§18 v2.3):** bei Score/FLAG/Sparraten-Change → PORTFOLIO.md + CORE-MEMORY + Faktortabelle + log.md + score_history.jsonl + `01_Skills/dynastie-depot/config.yaml` + `03_Tools/Rebalancing_Tool_v3.4.xlsx` + `03_Tools/Satelliten_Monitor_v2.0.xlsx` (+ flag_events.jsonl). Details in INSTRUKTIONEN §18 (inkl. Multi-Event-Union-Regel + xlsx-Tools-Pflicht seit v2.3 28.04. spätabends).

<!-- system-audit:last-audit:start -->
---

## 🔍 Last Audit

**Timestamp (UTC):** 2026-04-29T12:58:56Z
**Result:** 11/14 PASS (1 FAIL, 2 WARN)
**Run:** `python 03_Tools/system_audit.py -v`
**Full-Report:** stdout (kein Archiv-File)

<!-- system-audit:last-audit:end -->

*🦅 STATE.md Hub v2.0 | Dynasty-Depot | Navigation + Critical-Alert + Last-Audit | Stand: 27.04.2026*

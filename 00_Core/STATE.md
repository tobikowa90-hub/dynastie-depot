# 🎯 STATE.md — Dynasty-Depot Hub

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — Offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Infrastruktur / Briefing / Backtest-Ready
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13)
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Banner-Chronik

## ⚠️ Critical-Alerts (≤ 10 Tage — handgepflegt)
- **30.04.** PIPELINE #28 Quality-Trap-Methodology-Review **DONE** — Skill-Paket v3.7.5→v3.7.6 mit B6 Drawdown-Modulator (Option 2 chirurgisch). Codex-R1→R4 96% Confidence (4 HIGH + 4 MEDIUM closed inkl. B1 Nenner-Sign-Gate). Mechanik: `max 1`-Caps deaktiviert per-Subscore wenn Drawdown ≥-20% vs 52W-High UND Multiple unter 5J-Median (np.median 20 Stichtage, mind. 12 belastbar, strikt positive Nenner). Hard-Caps unverändert. Forward-only (keine MSFT-Q3-Backfill); Non-US-Freeze (ASML/SU INAKTIV); Screener-Exceptions (BRK.B/COST/RMS/TMO) ausgenommen.
- **30.04.** MSFT Q3 FY26 Tag-+1 Vollanalyse — **DONE** (Score 59→**50** Δ-9, D2/FLAG aktiv unverändert; Bull-Case Trigger A ✅ / B ❌ FAIL CY26 $190B vs Konsens $154,6B Surprise +23% / C ✅✅; Codex-R1+R2-Doppel-Review V-Q2-Mittelweg via Insider-Skip-Carryover; 4 PIPELINE-Items #25-28 aktiv; Sparrate 0€ unverändert; Methodology-Watch defeatbeta-WACC 13,64% vs FRED-Baseline 9,7% Q4-Verify)
- **30.04.** APH Q1 FY26 Tag-+1 Vollanalyse — DONE (Score 63→61, D2/FLAG aktiv unverändert, Codex-Review-Pass). Methodology-Watch Q2: China-Tax-ETR 27% strukturell + CommScope-Net-Lev 1,6x → <1,5x bis Q4 + ROIC-GW-Bereinigung Full-Year-Confirm
- **14.05.** MSFT Insider-Block-Re-Score post-14d-Skip-Window via insider_intel.py (PIPELINE #26)

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

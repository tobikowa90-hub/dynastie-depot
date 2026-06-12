# 🎯 STATE.md — Dynasty-Depot Hub

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — Offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Infrastruktur / Briefing / Backtest-Ready
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker-Chronik (§12) + System-Lifecycle (§13)
- [SESSION-HANDOVER.md](SESSION-HANDOVER.md) — Session-Banner-Chronik

## ⚠️ Critical-Alerts (≤ 10 Tage — handgepflegt)

> **Konvention (11.05.2026 Slim-Refactor):** 1-3-Zeilen-Pointer. Detail → `git log` + `CORE-MEMORY.md §13` + PIPELINE-Item-Body.

- **12.06. 🟢 exUSA-Re-Add — EXUS (Xtrackers MSCI World ex USA, IE0006WW1TQ4) @82€ reaktiviert** (User-Lock). US-Klumpenrisiko-Hedge, 8% Gesamtdepot, US-Faktor 0. Intern finanziert aus IWDA −51/AVGC −21/JEDI −10 → ETF-Block **616€ unverändert**, Slots 19→**20** (20 Positionen). Phase-B-Plan unberührt (EXUS+EIMI→Scalable, IWDA-Verkauf 2027). Rebalancing_Tool_v4.0 = SSoT. Detail → PORTFOLIO + config.yaml + git log.
- **06.–08.06. 🔴 Umstrukturierung-2027 Phase A — Major Depot-Umbau** (User-Lock 05.06.). Split 65/30/5→**60/35/5**, Equal-Weight→**3-Tier Conviction** (Basis 40/32/18€ × DEFCON-Modulation × FLAG), Roster 12→**13** (VEEV+COST raus; NOW/KYCCF/ZETA rein als DEFCON-3-Platzhalter, **Scoring pending O3**), ETF exUSA→JEDI+WQTM, ~**1031€**/Mt (ETF 616 + Satelliten-SOLL 364 + Gold 51). Markdown-Sync + Hook-§G-False-PASS-Fix + AVGC-Broker-Fix `1e3c817`. Detail → 00_Core/UMSTRUKTURIERUNG-2027.md + PORTFOLIO + git log.
- **04.06. ✅ AVGO Q2 FY26 Vollanalyse DONE** (Score 53→56, D2, FLAG bleibt — Insider-Selling 90d). Detail → CORE-MEMORY §12.1 + git log.

**Forward-Triggers (`earnings_calendar.py`-Sync 09.06. — yfinance+Override):**
- **Nächstes Event = ASML Q2 15.07.** (bmo, confirmed). 30-Tage-Fenster (→09.07.) sonst leer; einziges Pre-Cluster-Event.
- **Juli-Cluster 22.–30.07.:** 22.07. NOW Q2 (yf/UW; TipRanks 29.07 — IR-confirm pending) + TMO Q2 (bmo, yf+Nasdaq) · 28.07. V Q3 FY26 (amc) · 29.07. MSFT Q4 FY26 (amc) + APH Q2 (13:00 ET) + RMS H1 + KYCCF Q1 (yf, JP-verifizieren) · 30.07. SU H1 + AMZN Q2 (amc, CapEx/OCF-FLAG-Re-Eval)
- **Aug + Gates:** 01.08. BRK.B Q2 (Sa, 10-Q) · 04.08. ZETA Q2 · **03.09.** AVGO Q3 FY26 Re-Eval (Insider-FLAG 90d-rolling)
- **O3-Scoring-Nachzug pending:** NOW (US `!Analysiere`, ~22.07.) · KYCCF (JP `non-us-fundamentals`, ~29.07. yf — JP-Q1-Termin verifizieren) · ZETA (US, war QuickScreener-Rot, ~04.08.) → echte Scores ersetzen die DEFCON-3-Platzhalter
- **06.07.** FinnHub-Shadow-Run Reklassifizierungs-Gate (PIPELINE #75, scoring-neutral)

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

**Sync-Pflicht (§18 v2.4):** bei Score/FLAG/Sparraten-Change → PORTFOLIO.md + CORE-MEMORY + Faktortabelle + log.md + score_history.jsonl + `01_Skills/dynastie-depot/config.yaml` + `03_Tools/Rebalancing_Tool_v3.4.xlsx` + `03_Tools/Satelliten_Monitor_v2.0.xlsx` (+ flag_events.jsonl). Nach xlsx-Write **verpflichtender §18.7 Smoke-Test** (`03_Tools/xlsx-smoke-test.md`, fail-close vor `git add`). Details in INSTRUKTIONEN §18 (inkl. Multi-Event-Union-Regel + xlsx-Tools-Pflicht seit v2.3 28.04. spätabends + Smoke-Test seit v2.4 11.05.2026).

<!-- system-audit:last-audit:start -->
---

## 🔍 Last Audit

**Timestamp (UTC):** 2026-05-24T23:38:46Z
**Result:** 10/15 PASS (2 FAIL, 3 WARN)
**Run:** `python 03_Tools/system_audit.py --core`
**Full-Report:** stdout (kein Archiv-File)

<!-- system-audit:last-audit:end -->

*🦅 STATE.md Hub v2.5 | Dynasty-Depot | **Stand:** 2026-06-12 (exUSA-Re-Add: EXUS @82€ reaktiviert als US-Hedge, Slots 19→20, ETF-Block 616€ unverändert. Vorher: 2026-06-09 Earnings-Kalender-Sync via `earnings_calendar.py` [yfinance+Override] — Forward-Triggers auf Tool-Kanon: ASML 15.07. → NOW/TMO 22.07. → V 28.07. → MSFT/APH/RMS/KYCCF 29.07. → SU/AMZN 30.07. → BRK.B 01.08. → ZETA 04.08. → AVGO 03.09. Tool-Regex-Bug gefixt [7-Spalten-3-Tier-Tabelle]. Date-only, kein Score-Event. Vorher: 2026-06-08 Umstrukturierung-2027 Phase A Markdown-Sync)*

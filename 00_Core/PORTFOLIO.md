# PORTFOLIO.md — Depot-Live-State

**Stand:** 11.05.2026 (Live-State stabil seit 04.05. BRK.B; letzter Score-Move 04.05.; Doctor-Mo-Anker 7P/7W/0F). Score-/FLAG-/Sparraten-Chronik aller Moves seit 17.04. → CORE-MEMORY §12.X + git log (kanonische Detail-Quelle).

## Verweise
- [INSTRUKTIONEN.md §22](INSTRUKTIONEN.md#22-sparplan-formel-aktuell-18042026-v37) — Sparplan-Formel (Nenner-Berechnung)
- [INSTRUKTIONEN.md §18](INSTRUKTIONEN.md#18-sync-pflicht-logmd--core-memorymd--faktortabellemd--statemd--score_historyjsonl--flag_eventsjsonl) — Sync-Pflicht bei Score-/FLAG-/Sparraten-Change
- [PIPELINE.md](PIPELINE.md) — Nächste-Trigger-Liste synchron mit Hub-Critical-Alert
- [CORE-MEMORY.md §12](CORE-MEMORY.md#12-per-ticker-chronik) — Per-Ticker-Analyse-Historie
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail pro Ticker

---

## Portfolio-State (12 Satelliten)

| Ticker | Score | DEFCON | Rate | FLAG | Nächster Trigger |
|--------|-------|--------|------|------|------------------|
| AVGO | **53** | **🟠 2** | **0€** | 🔴 Insider-Selling 90d $106M+ (27.04.) | **03.06.2026** (amc) Q2 FY26 Earnings — FLAG-Resolve-Gate ($20M-Schwelle vs. $106M-Diskr.); Score 84→53 am 30.04. (§12.1); Drift erkannt via `earnings_calendar.py` 25.05. |
| BRK.B | **71** | 🟡 3 | **38,00€** | ✅ Insurance Exception | Q2 FY26 ~02./03.08. — KHC-OTTI / GEICO-Decel / Form-13F Apple-Trim ~14.05. / Buyback-Cashflow-Reconciliation (PIPELINE #36-#41) |
| VEEV | 74 | 🟡 3 | **38,00€** | ✅ | **03.06.2026** (amc) Q1 FY27 Earnings (Date-Recheck 25.05. Finnhub+Yahoo+IR konvergent; vorherige 27.05.-Annahme war Stale-yfinance-Pull 30.04.) |
| SU | 69 | 🟡 3 | **38,00€** | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | **38,00€** | ✅ Screener-Exception | **28.05.2026** Q3 FY26 Earnings (yfinance-Pull 30.04. — Membership-Yield-Watch); Q1 FY27 ~Dez |
| RMS | 68 | 🟡 3 | **38,00€** | ✅ Screener-Exception | H1 Juli/Aug |
| ASML | 68 | 🟡 3 | **38,00€** | ✅ | Q2 2026 (Q1 17.04. Vollanalyse ✅) |
| TMO | 67 | 🟡 3 | **38,00€** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR 23.04.) | Q2 FY26 ~Ende Juli — Organic-Akzeleration + Clario-Integration-Check |
| **V** | **64** | **🟠 2** | **19,00€** | ✅ Clean (D2 nach Rescoring-Revert 28.04. spätabends) | **Q3 FY26 ~Ende Juli — Cross-Border-Velocity + ROIC-Methodology-Verify** |
| APH | **61** | 🟠 2 | **0€** | 🔴 Score-basiert (Score 61 < 65 D3-Threshold) | Q2 FY26 ~23.07. — China-Tax + CommScope-Net-Lev Methodology-Watch (Score 63→61 am 30.04., Detail §12.7) |
| MSFT | **50** | 🟠 2 | **0€** | 🔴 CapEx/OCF aktiv (Trigger A ✅ 57,7% / B ❌ / C ✅✅ — UND nicht vollumfänglich) | Q4 FY26 ~Juli — CapEx-Plateau-Recheck + WACC-Methodology-Verify; Insider-Block-Re-Score 14.05. (PIPELINE #25-#27) |
| **AMZN** | **42** | **🔴 1** | **0€** | 🔴 CapEx/OCF aktiv (TTM netto 99,2% / gross 101,7% ≫60% — Neuaufnahme 12. Satellit 15.05.) | **Q2 FY26 ~Ende Juli — CapEx/OCF-FLAG-Re-Eval + Vollanalyse** |

**Sparraten-Nenner:** 7×1,0 + 1×0,5 + 4×0 = **7,5** → 38,00€ volle / 19,00€ D2 / 0€ FLAG. **Summe 285€** ✓ (7×38 + 1×19 + 4×0). FLAG-Override-Raten Score-unabhängig — Score-Moves bei AVGO/MSFT/APH/AMZN wirken nicht auf Nenner solange FLAG aktiv. **AMZN-Neuaufnahme (12. Satellit, User-Direktive 18.05.) ist nenner-neutral:** FLAG=Gewicht 0,0 → Nenner unverändert 7,5, alle 11 bestehenden Einzelraten unverändert (38€/19€/0€).

> **Chronik aller Score-/FLAG-/Sparraten-Moves seit 17.04.2026** → CORE-MEMORY §12.X (Per-Ticker) + git log + `score_history.jsonl`. PORTFOLIO.md hält nur den Live-State; Vorgeschichte-Quotes 17.04.→04.05. entfernt (Cleanup 11.05.) — kein Info-Loss, da §12 + jsonl SSoT sind.

---

## Aktive Watches

- **V D2-Watch (REAKTIVIERT 28.04.2026 spätabends nach Codex-Review-Revert):** Beat-Cascade allein lieferte methodisch nicht den D3-Pfad — ROIC-Sub-Score-Move 1→7 via SKILL absolute alternative scale war regelwidrig (WACC vorhanden 10,48% ≠ "fehlende WACC-Schätzung"). Score 68→64, D3→D2, Sparrate 35,63€→19,00€. **Q3 FY26 ~Ende Juli** entscheidet via:
  - **Cross-Border-Velocity:** Q2 +12% cc deceleriert von Pre-Q-Niveau >15%; <10% cc Q3 = Travel-Schwäche-Signal
  - **defeatbeta-ROIC-Methodology-Verify (PIPELINE #21):** 18.04. defeatbeta-Wert 9,89% empirisch inkonsistent mit Standard-NOPAT/IC-Formeln; Q3 Roh-Output-Dump + primary-source-Calc-Abgleich
  - **Litigation-MDL persistent (Risk-Map):** 6M FY26 $2,05B accrued litigation paid (Settlement-Tranche), weitere möglich
  - 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA (Tech-Carryover bestätigt)
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- **MSFT FLAG-Status (UPDATED 30.04.2026):** Trigger A ✅ 57,7% / B ❌ FAIL CY26 $190B +23% Surprise / C ✅✅ Azure +39% cc — UND nicht vollumfänglich → FLAG bleibt aktiv. Re-Eval Q4 FY26 ~Juli + Insider-Block-Re-Score post-14.05. (Skip-Window läuft).
- **TMO Q2 Re-Check** (Q1 23.04. resolved): Organic-Akzeleration H2 3-4%-Guide + Clario-Integration-Execution — Q2 Ende Juli.
- **AVGO Re-Eval Q2 FY26 03.06.2026 (amc) [FLAG-Resolve-Gate primär]** → Folge-Re-Eval Q3 FY26 ~Sept (FLAG aktiv seit 27.04. $106,4M Diskr. 90d >> $20M-Resolve-Schwelle; Vollanalyse 30.04. Score 84→53 D4→D2; Detail §12.1).
- **AMZN Neuaufnahme 12. Satellit (15.05.2026, User-Direktive 18.05.):** Score 42/D1, 🔴 CapEx/OCF-FLAG TTM 99,2% netto (≫60%, schärfer als GOOGL 74-79%). FCF TTM nur $1,2B (-95% YoY, FCF-Yield 0,04%). Sparrate **0€ regelkonform** (User-Entscheidung: kein Owner-Override, FLAG heilig). Slot-Erweiterung 11→12 nenner-neutral. **Resolve-Gate:** CapEx/OCF <60% — frühestens wenn Monetarisierung der KI-CapEx OCF überholt (Jassy: "early years FCF challenged", 6-24 Mt. Lag). Re-Eval Q2 FY26 ~Ende Juli. Detail §12.<amzn> + score_history.jsonl + flag_events.jsonl.

---

## Nächste kritische Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| 28.04. (overdue) | SNPS/SPGI | B | Watchlist-Review Q1 Earnings — Nachholbedarf (PIPELINE #62) |
| Mai | ZTS/PEGA/CPRT | B | Q-Earnings + Slot-16 |
| 28.05. | COST | B | Q3 FY26 Earnings (Membership-Yield-Watch) |
| 03.06. (amc) | AVGO | B | Q2 FY26 Earnings + FLAG-Resolve-Gate ($20M-Schwelle vs. $106M-Diskr. 27.04.; Drift erkannt 25.05. via `earnings_calendar.py`) |
| 03.06. (amc) | VEEV | B | Q1 FY27 Earnings (Date-Korrektur 25.05., war 27.05. = Stale) |
| ~Ende Juli | AMZN | B/C | Q2 FY26 Earnings — CapEx/OCF-FLAG-Re-Eval (Resolve-Gate <60%) + Vollanalyse (Score 42/D1, FLAG seit 15.05.) |


---

*🦅 PORTFOLIO.md v1.2 | Dynasty-Depot | Live-State — default-load bei Session-Start | Stand: 2026-05-23 (Live-State stabil seit AMZN-Neuaufnahme 18.05.; 00_Core Slim-Refactor 23.05. — stale Earnings-Window-Note entfernt. Detail-Chronik → CORE-MEMORY §12 + git log + score_history.jsonl)*

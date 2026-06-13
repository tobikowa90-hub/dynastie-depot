# PORTFOLIO.md — Depot-Live-State

**Stand:** 09.06.2026 (Earnings-Kalender-Sync via `03_Tools/earnings_calendar.py` [yfinance+Override, SSoT]: alle „Nächster Trigger"-Termine auf Tool-Kanon — ASML 15.07. → NOW/TMO 22.07. → V 28.07. → MSFT/APH/RMS/KYCCF 29.07. → SU/AMZN 30.07. → BRK.B 01.08. → ZETA 04.08. → AVGO 03.09. NOW yf-soft [TipRanks 29.07]. Date-only, kein Score-Event. Umstrukturierung-2027 Phase A: Roster 12→13, Equal-Weight→3-Tier, Split 60/35/5; letzter Score-Move AVGO 04.06. Q2 FY26 53→56 FLAG-bleibt). Score-/FLAG-/Sparraten-Chronik aller Moves seit 17.04. → CORE-MEMORY §12.X + git log (kanonische Detail-Quelle).

**Allokation:** 60/35/5 (ETF 616€ / Satelliten SOLL 364€ [Funded 210€] / Gold 51€), Gesamt ~1031€/Mt. US-Cap 63% / Ist ~53% (Tool). **20 Positionen** (6 ETF + 13 Aktien + Gold). ETF-Broker: ING (IWDA 206 + EIMI 123 + EXUS 82) · Scalable (AVGC 82 + JEDI 72 + WQTM 51). **exUSA-Re-Add 2026-06-12 (User-Lock):** EXUS (Xtrackers MSCI World ex USA) @82€ als US-Klumpenrisiko-Hedge (8% Gesamtdepot, US-Faktor 0), intern finanziert aus IWDA −51/AVGC −21/JEDI −10 — ETF-Block bleibt 616€. Raten = Rebalancing_Tool_v4.0 (SSoT).

## Verweise
- [INSTRUKTIONEN.md §22](INSTRUKTIONEN.md#22-sparplan-formel-aktuell-18042026-v37) — Sparplan-Formel (Nenner-Berechnung)
- [INSTRUKTIONEN.md §18](INSTRUKTIONEN.md#18-sync-pflicht-logmd--core-memorymd--faktortabellemd--statemd--score_historyjsonl--flag_eventsjsonl) — Sync-Pflicht bei Score-/FLAG-/Sparraten-Change
- [PIPELINE.md](PIPELINE.md) — Nächste-Trigger-Liste synchron mit Hub-Critical-Alert
- [CORE-MEMORY.md §12](CORE-MEMORY.md#12-per-ticker-chronik) — Per-Ticker-Analyse-Historie
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail pro Ticker

---

## Portfolio-State (13 Satelliten — 3-Tier Conviction)

> Rate = Tier-Basis (T1 40 / T2 32 / T3 18€) × DEFCON-Modulation (D3/D4 ×1,0 · D2 ×0,5 · D1 0) × FLAG (🔴 → 0€, heilig). `—` Score = O3-Scoring noch nachzuholen (DEFCON-3-Platzhalter, Owner-Conviction-Add §6.4).

| Tier | Ticker | Score | DEFCON | Rate | FLAG | Nächster Trigger |
|------|--------|-------|--------|------|------|------------------|
| **T1** | NOW | **— (O3)** | 🟡 3\* | **40€** | ✅ Platzhalter | **Q2 22.07.** (yf/UW; TipRanks: 29.07 — IR-confirm pending) — O3-Vollanalyse pending (US `!Analysiere`) — Owner-Add ohne Score (§6.4, analog AMZN) |
| **T1** | AVGO | **56** | 🟠 2 | **0€** | 🔴 Insider-Selling 90d $106M+ (27.04.) | **Q3 FY26 03.09.** (amc) Re-Eval + FLAG-Resolve-Gate; Q2 04.06. 53→56 (§12.1; Beat-Raise, FLAG bleibt: Samueli $281M=10b5-1 ausgeschl., C-Suite $106M diskr.) |
| **T1** | MSFT | **50** | 🟠 2 | **0€** | 🔴 CapEx/OCF (A ✅ 57,7% / B ❌ / C ✅✅ — UND nicht vollumfänglich) | **Q4 FY26 29.07.** (amc) — CapEx-Plateau + WACC-Methodology-Verify; Insider-Block-Re-Score (PIPELINE #25-#27) |
| **T1** | AMZN | **42** | 🔴 1 | **0€** | 🔴 CapEx/OCF (TTM netto 99,2% ≫60%) | **Q2 FY26 30.07.** (amc) — CapEx/OCF-FLAG-Re-Eval + Vollanalyse |
| **T2** | ASML | **68** | 🟡 3 | **32€** | ✅ | **Q2 2026 15.07.** (bmo, confirmed; Q1 17.04. Vollanalyse ✅) — nächstes Event im Roster |
| **T2** | KYCCF | **67** | 🟡 3 | **32€** | ✅ Clean | **Q1 FY27 29.07.** (yf — JP-Termin verifizieren) — O3 DONE 13.06. (JGAAP FY26 Primärquelle; Wide-Moat QT beide Zweige hart 0, Festungs-Bilanz EQ-Ratio 94,6%, §12.14) |
| **T2** | V | **64** | 🟠 2 | **16€** | ✅ Clean (D2-Sockelbetrag = 50% von 32) | **Q3 FY26 28.07.** (amc) — Cross-Border-Velocity + ROIC-Methodology-Verify |
| **T3** | BRK.B | **71** | 🟡 3 | **18€** | ✅ Insurance Exception | **Q2 FY26 01.08.** (Sa, 10-Q — BRK released samstags) — KHC-OTTI / GEICO-Decel / Form-13F Apple-Trim / Buyback-Reconciliation (#36-#41) |
| **T3** | SU | **69** | 🟡 3 | **18€** | ✅ | **H1 30.07.** (confirmed) |
| **T3** | RMS | **68** | 🟡 3 | **18€** | ✅ Screener-Exception | **H1 29.07.** (8:00 CEST, confirmed) |
| **T3** | TMO | **67** | 🟡 3 | **18€** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR 23.04.) | **Q2 FY26 22.07.** (bmo, yf+Nasdaq) — Organic-Akzeleration + Clario-Integration |
| **T3** | APH | **61** | 🟠 2 | **0€** | 🔴 Score-basiert (61 < 65 D3-Threshold) | **Q2 FY26 29.07.** (13:00 ET) — China-Tax + CommScope-Net-Lev (Score 63→61 am 30.04., §12.7) |
| **T3** | ZETA | **— (O3)** | 🟡 3\* | **18€** | ✅ Platzhalter | **Q2 04.08.** — O3-Vollanalyse pending (US, war QuickScreener-Rot, bewusste Spekulation) — Owner-Add ohne Score (§6.4) |

\* DEFCON-3-Platzhalter (NOW/ZETA): Owner-Conviction-Add ohne DEFCON-Score → volle Tier-Rate bis O3-Vollanalyse echten Score liefert. (KYCCF O3 DONE 13.06. → Score 67/D3.)

**Sparraten-Modell (3-Tier × DEFCON-Modulation × FLAG):** **SOLL-Σ = 4×40 + 3×32 + 6×18 = 364€** (== `config.yaml` brokers.scalable.sparrate_eur). **Funded-Σ = 210€** = NOW 40 + [ASML 32 + KYCCF 32 + V 16] + [RMS/BRK.B/TMO/SU/ZETA je 18 = 90]. Differenz **154€** (138€ FLAG-eingefroren AMZN/MSFT/AVGO/APH + 16€ V-D2-Sockel) → Rebalancing-Tool lenkt value-based auf untergewichtete Positionen (voller Monatsbeitrag deployed, nur Verteilung verschiebt sich). FLAG ist score-unabhängig (heilig) — Score-Moves bei geflaggten Titeln wirken nicht auf die Rate solange FLAG aktiv.

> **Chronik aller Score-/FLAG-/Sparraten-Moves seit 17.04.2026** → CORE-MEMORY §12.X (Per-Ticker) + git log + `score_history.jsonl`. PORTFOLIO.md hält nur den Live-State; Vorgeschichte-Quotes 17.04.→04.05. entfernt (Cleanup 11.05.) — kein Info-Loss, da §12 + jsonl SSoT sind.

---

## Aktive Watches

- **V D2-Watch (REAKTIVIERT 28.04.2026 spätabends nach Codex-Review-Revert):** Beat-Cascade allein lieferte methodisch nicht den D3-Pfad — ROIC-Sub-Score-Move 1→7 via SKILL absolute alternative scale war regelwidrig (WACC vorhanden 10,48% ≠ "fehlende WACC-Schätzung"). Score 68→64, D3→D2, Sparrate 35,63€→19,00€. **Q3 FY26 28.07.** (amc) entscheidet via:
  - **Cross-Border-Velocity:** Q2 +12% cc deceleriert von Pre-Q-Niveau >15%; <10% cc Q3 = Travel-Schwäche-Signal
  - **defeatbeta-ROIC-Methodology-Verify (PIPELINE #21):** 18.04. defeatbeta-Wert 9,89% empirisch inkonsistent mit Standard-NOPAT/IC-Formeln; Q3 Roh-Output-Dump + primary-source-Calc-Abgleich
  - **Litigation-MDL persistent (Risk-Map):** 6M FY26 $2,05B accrued litigation paid (Settlement-Tranche), weitere möglich
  - 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA (Tech-Carryover bestätigt)
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- **MSFT FLAG-Status (UPDATED 30.04.2026):** Trigger A ✅ 57,7% / B ❌ FAIL CY26 $190B +23% Surprise / C ✅✅ Azure +39% cc — UND nicht vollumfänglich → FLAG bleibt aktiv. Re-Eval Q4 FY26 29.07. + Insider-Block-Re-Score post-14.05. (Skip-Window läuft).
- **TMO Q2 Re-Check** (Q1 23.04. resolved): Organic-Akzeleration H2 3-4%-Guide + Clario-Integration-Execution — Q2 22.07. (bmo).
- **AVGO Re-Eval Q3 FY26 03.09.2026 (amc) [FLAG-Resolve-Gate primär]** (FLAG aktiv seit 27.04. $106,4M Diskr. 90d >> $20M-Resolve-Schwelle — Q2-Earnings 03.06. Beat-and-Raise [Rev $22,2B +48%, AI-Semi $10,8B +143%, EPS $2,44 Beat] aber FLAG bleibt: Samueli $281M=10b5-1 korrekt ausgeschl., C-Suite $106M non-plan; Q2 Vollanalyse 04.06. Score 53→56 D2 [sell-the-news −12,6% da FY27-AI nicht angehoben]; Detail §12.1).
- **AMZN (Tier 1, Neuaufnahme 15.05.2026, User-Direktive 18.05.):** Score 42/D1, 🔴 CapEx/OCF-FLAG TTM 99,2% netto (≫60%, schärfer als GOOGL 74-79%). FCF TTM nur $1,2B (-95% YoY, FCF-Yield 0,04%). Sparrate **0€ regelkonform** (User-Entscheidung: kein Owner-Override, FLAG heilig). Slot-Erweiterung 11→12 nenner-neutral. **Resolve-Gate:** CapEx/OCF <60% — frühestens wenn Monetarisierung der KI-CapEx OCF überholt (Jassy: "early years FCF challenged", 6-24 Mt. Lag). Re-Eval Q2 FY26 30.07. (amc). Detail §12.<amzn> + score_history.jsonl + flag_events.jsonl.

---

## Nächste kritische Trigger (30 Tage)

> Quelle: `03_Tools/earnings_calendar.py --check` (yfinance + Override-YAML, Stand 09.06.). Mid-Juli Re-Run lockt yf-Soft-Termine.

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| **15.07.** (bmo) | ASML | B | Q2 2026 — nächstes Roster-Event (30-Tage-Fenster →09.07. sonst leer) |
| **22.07.** | NOW / TMO | A/B | NOW Q2 (yf/UW; TipRanks 29.07 — IR-confirm pending, O3) · TMO Q2 (bmo, yf+Nasdaq) |
| **28.07.** (amc) | V | B | Q3 FY26 — Cross-Border-Velocity + ROIC-Methodology-Verify |
| **29.07.** | MSFT / APH / RMS / KYCCF | A/B | MSFT Q4 FY26 (amc, CapEx+WACC) · APH Q2 (13:00 ET, Score 61<65 FLAG) · RMS H1 (8:00 CEST) · KYCCF Q1 (yf, JP-Termin verifizieren; Score 67/D3) |
| **30.07.** (amc) | SU / AMZN | B/C | SU H1 · AMZN Q2 FY26 — CapEx/OCF-FLAG-Re-Eval (Resolve-Gate <60%) + Vollanalyse (Score 42/D1) |
| **01.08.** (Sa, 10-Q) | BRK.B | B | Q2 FY26 — KHC-OTTI / GEICO-Decel / Form-13F Apple-Trim (#36-#41) |
| **04.08.** | ZETA | A | Q2 2026 — O3-Scoring-Nachzug |
| **03.09.** (amc) | AVGO | B | Q3 FY26 + FLAG-Resolve-Gate (Q2 04.06. Score 53→56, FLAG bleibt) |


---

*🦅 PORTFOLIO.md v1.5 | Dynasty-Depot | Live-State — default-load bei Session-Start | Stand: 2026-06-13 (KYCCF O3-Vollanalyse: Score 67/🟡 D3, kein FLAG, Tier-2-Rate 32€ unverändert [Platzhalter war voll gefunded → Funded-Σ 210€ stabil]; Primärquelle JGAAP FY26; ersetzt DEFCON-3-Platzhalter; O3-Backlog jetzt NOW/ZETA. Vorher: 2026-06-12 exUSA-Re-Add: EXUS @82€ reaktiviert als US-Hedge, Slots 19→20, intern aus IWDA/AVGC/JEDI finanziert, ETF-Block 616€ unverändert; Rebalancing_Tool_v4.0 SSoT. Vorher: 2026-06-09 Earnings-Kalender-Sync via `earnings_calendar.py` [yfinance+Override SSoT]; Tool-Regex-Bug für 7-Spalten-3-Tier-Tabelle gefixt; date-only, kein Score-Event. Vorher: 2026-06-08 Umstrukturierung-2027 Phase A 13-Roster + 3-Tier + 60/35/5. Detail-Chronik → CORE-MEMORY §12 + git log + score_history.jsonl)*

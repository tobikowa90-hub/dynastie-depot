# DEFCON Faktortabelle

**Stand:** 2026-09-04 (**AVGO Q3 FY26 Vollanalyse: 56 -> 59, DEFCON 2, FLAG-Resolve-Gate verfehlt** [$33,69M > $20M]; score_datum 2026-09-03. Vorher: 2026-06-13 KYCCF O3-Vollanalyse 67/D3 — JGAAP-Primärquelle, ersetzt Platzhalter; O3-Backlog jetzt NOW/ZETA. Vorher: Umstrukturierung-2027 Phase A Roster 12→13, VEEV+COST raus, NOW/KYCCF/ZETA rein. Detail-Move-Chronik → CORE-MEMORY §12 + git log + score_history.jsonl)
**Primärquelle:** config.yaml (hat immer Vorrang)
**Scoring-Version:** DEFCON v3.7 (Quality-Trap-Interaktion + OpM + Analyst-Bias-Kalibrierung + Fundamentals-Cap 50)
**DEFCON-Thresholds (SKILL.md-aligned seit 18.04.):** ≥80 → D4 | 65-79 → D3 | 50-64 → D2 | <50 → D1

> ⚠️ VALIDIERUNGSHINWEIS
> Konflikt Faktortabelle ↔ config.yaml: config.yaml gewinnt immer.
> score_datum > 90 Tage → 🟡 veraltet markieren.
> Bei Datenzweifel → Shibui direkt abfragen.
> **Seit 25.04.2026 (00_Core Hub-Split):** Session-Start liest `00_Core/STATE.md` (Hub) + `00_Core/PORTFOLIO.md` (Live-State); Faktortabelle ist on-demand Deep-Dive-Quelle. Sync-Pflicht §18 v2 = Trigger-basiertes Event-Mapping (Score-Event-Set inkl. PORTFOLIO.md statt STATE.md).

## Verweise
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (Primärquelle, synchron mit dieser Tabelle)
- [INSTRUKTIONEN.md §4](INSTRUKTIONEN.md#4-stufe-2--defcon-scoring-100-punkte-matrix) — DEFCON-Scoring-Regeln
- [CORE-MEMORY.md §4](CORE-MEMORY.md#4-score-register) — Score-Register
- [CORE-MEMORY.md §5](CORE-MEMORY.md#5-scoring-lektionen-gelernte-regeln) — Scoring-Lektionen
- [CORE-MEMORY.md §12](CORE-MEMORY.md#12-per-ticker-chronik) — Per-Ticker-Historie

---

## Haupttabelle

| Position | FCF-Marge 5J | ROIC TTM | Gross Margin | Debt/EBITDA | Moat | Score | DEFCON | FLAG | Score-Datum | Nächstes Update |
|----------|-------------|----------|--------------|-------------|------|-------|--------|------|-------------|-----------------|
<!-- DATA:ASML -->
| ASML | 33,8% | 26,48% | 52,8% | 0,21x | Wide | 68 | 🟡 3 | ✅ Clean | 2026-04-17 | Q2 2026 Earnings — FY27 Fwd P/E Watch (30,30 → D4-Kandidat <30) |
<!-- DATA:AVGO -->
| AVGO | 44,2% (TTM FCF 39,4B / Rev 89,1B) | **6,72% GAAP-Q / 52,8% §410-Goodwill-bereinigt (M&A-Compounder VMware/CA/Symantec/Brocade, GW 51,98% Assets — von 57,2% gefallen, Assets 171→188B) vs WACC defeatbeta 15,96% (carryover, Tool-Bug `bc10_year` weiterhin offen)** | 75,5% TTM | **0,68x** (von 1,41x — $5,6B Tilgung in Q3) | Wide | **59** | **🟠 2** | 🔴 Insider-Selling 90d **$33,69M** (FLAG aktiv seit 27.04.2026 — Sparrate 0€, Resolve-Gate ≤$20M **am 04.09. verfehlt**; $29,19M davon allein Brazeal/CLO in 3 Tranchen ohne 10b5-1) | **2026-09-03** | **Q4 FY26 09.12.** (amc, im Q3-Call bestätigt) — FLAG-Resolve-Gate #2; Fwd P/E 20,65 hat den QT-Korridor 22–30 nach unten verlassen |
<!-- DATA:V -->
| V | ~54% 5J | **9,89% defeatbeta vs WACC 10,48% [carryover 18.04.; Q3-Verify-Watch PIPELINE #21]** | 80,4% | 0,31x | Wide | **64** | **🟠 2** | ✅ Clean (D2 nach Rescoring-Revert 28.04. spätabends) | **2026-04-28** | **Q3 FY26 ~Ende Juli** — Cross-Border-Velocity + ROIC-Methodology-Verify |
<!-- DATA:MSFT -->
| MSFT | ~58% (9M FY26 bereinigt 57,7%) | **7,68% defeatbeta vs WACC 13,64% [Methodology-Watch FRED-Baseline-Verify Q4 PIPELINE]** | ~69% | ~0,5x (Net-Cash) | Wide | **50** | 🟠 2 | 🔴 CapEx/OCF aktiv (Trigger A erfüllt 9M-bereinigt 57,7%, B FAIL CY26 $190B Surprise, C ✅✅ Azure +39%cc — UND nicht vollumfänglich) | **2026-04-30** | **Q4 FY26 ~Juli** — CapEx-Plateau-Recheck + WACC-Methodology-Verify (Insider-Re-Score 14.05. DONE, Δ=0) |
<!-- DATA:TMO -->
| TMO | ~15% 5J | 8,04% GAAP / 17,18% bereinigt (GW-Ausnahme) vs WACC 10,44% | 40,9% | 2.57x (Pre-Clario) | Wide | **67** | **🟡 3** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR — Q1 FCF $825M +121% YoY, WC-Unwind bestätigt) | **2026-04-23** | **Q2 FY26 ~Ende Juli** — Organic-Akzeleration + Clario-Integration-Check |
<!-- DATA:RMS -->
| RMS | ~28% 5J FCF | 24.2% TTM | ~71% | Netto-Cash +€9,89B | Wide | 68 | 🟡 3 | ✅ Clean | 2026-04-17 | H1 2026 Report Juli/Aug 2026 |
<!-- DATA:SU -->
| SU | ~10% 5J | 10.48% TTM | ~42% | 2.51x | Narrow/Wide | 69 | 🟡 3 | ✅ Clean | 2026-04-17 | H1 2026 Earnings Juli/Aug 2026 |
<!-- DATA:BRK.B -->
| BRK.B | N/A (Float-Modell) | 5.6–7.8% GAAP (Insurance-Cycle, Float-Spread > Standard-ROIC) | N/A (Holdings) | Netto-Cash $380B effektiv (T-Bill-Settlement-bereinigt; nominal $397,4B − $17,2B Payable, 10-Q p.2-3 Primary; Forbes/Bill-Stone Secondary-Confirm) | Wide | **71** (Codex-R1-REJECT-Korrektur 75→71 Δ-4) | 🟡 3 | ✅ Clean (Insurance Exception) | **2026-05-04** | **Q2 FY26 ~02./03.08.** — KHC-OTTI-Resolve + GEICO-UW-Decel-Trend + Form-13F Apple-Trim-Magnitude + Buyback-Cashflow-Reconciliation |
<!-- DATA:APH -->
| APH | 19,0% FY25 | 28% bereinigt §410 (CommScope-GW) vs WACC 14,30% | 36,9% FY25 | 1,6x Q1 FY26 (post-CommScope) | Wide | **61** | 🟠 2 | 🔴 FLAG (Score-basiert <65 D3) | **2026-04-30** | **Q2 FY26 ~23.07.** — China-Tax-ETR-27%-Verify + CommScope-Net-Lev-Verlauf + ROIC-GW-Bereinigung-Full-Year-Check |
<!-- DATA:AMZN -->
| AMZN | ~1% 5J (FCF TTM $1,2B, CapEx-Boom) | 5,4% 6Q-Ø GAAP vs WACC 15,57% (defeatbeta; §410 N/A GW 2,6%) | 50,3% FY25 (3J +1,65pp/J) | NetDebt/EBITDA ~0,4x | Wide | **42** | **🔴 1** | 🔴 CapEx/OCF TTM 99,2% netto (FLAG aktiv 2026-05-15 — Sparrate 0€, Resolve-Gate <60%) | **2026-05-15** | **Q2 FY26 ~Ende Juli — CapEx/OCF-FLAG-Re-Eval + Vollanalyse** |
<!-- DATA:NOW -->
| NOW | — | — | — | — | — | **— (O3)** | 🟡 3\* | ✅ Platzhalter (Owner-Add §6.4) | — | O3-Vollanalyse (US `!Analysiere`) — Score nachzuholen |
<!-- DATA:KYCCF -->
| KYCCF | 34,4% (FY26) | 19,9% GuruFocus / op-ROIC >100% (Cash-verwässert) vs WACC 5,54% | 83,0% | Netto-Cash (EQ-Ratio 94,6%) | Wide | **67** | 🟡 3 | ✅ Clean | 2026-06-13 | Q1 FY27 ~29.07. (JP-Termin verifizieren) — JGAAP-Quelle |
<!-- DATA:ZETA -->
| ZETA | — | — | — | — | — | **— (O3)** | 🟡 3\* | ✅ Platzhalter (Owner-Add §6.4) | — | O3-Vollanalyse (US, war QuickScreener-Rot) — Score nachzuholen |
<!-- END_TABLE -->

**Aktive FLAGs:** MSFT (CapEx/OCF >60%, T1) | **AVGO** (Insider-Selling 90d — aktiviert 27.04.2026 mit $106,4M; Stand 04.09. **$33,69M**, weiterhin ueber der $20M-Schwelle, T1) | APH (Score-basiert <65, DEFCON 2, T3) | **AMZN (CapEx/OCF TTM 99,2% netto — aktiviert 2026-05-15, T1)** — alle 4 FLAG → Rate 0€ (heilig)
**Struktureller Disclosure (kein FLAG):** ~~TMO (fcf_trend_neg)~~ **Resolved 23.04.2026** (Q1 FY26 FCF $825M +121% YoY, WC-Unwind-These bestätigt)
**Unter Review:** — (AVGO 27.04.2026 zu aktivem FLAG promotet)
**Analysierte Positionen:** 11/13 ✅ (Umstrukturierung 2026-06-07: VEEV+COST raus, NOW/KYCCF/ZETA rein als DEFCON-3-Platzhalter ohne Score → O3-Scoring-Nachzug. Bestehende Scores: ASML/RMS/SU 17.04. + V 18.04. + TMO 23.04. + MSFT/APH 30.04. + BRK.B 04.05. + AMZN 15.05. + AVGO 04.06. + KYCCF 13.06. + AVGO Q3 03.09.)
**Offene Scores:** 2/13 (NOW · ZETA — O3-Vollanalyse pending; KYCCF O3 DONE 13.06. → 67/D3)
**Tariff-Check:** APH abgeschlossen 15.04.2026 — China Revenue 14.7% (kein Revenue-FLAG), Supply-Chain CN/MY Risk-Map-Notiz aktiv
**Sparraten-Modell (3-Tier, Umstrukturierung 2026-06-07):** Rate = Tier-Basis (T1 40 / T2 32 / T3 18€) × DEFCON-Modulation (D3/D4 ×1,0 · D2 ×0,5 · D1 0) × FLAG (🔴 → 0€). **SOLL-Σ = 4×40 + 3×32 + 6×18 = 364€**; **Funded-Σ = 210€** (FLAG-frozen AMZN/MSFT/AVGO/APH + V-D2-Sockel 16€ + NOW/KYCCF/ZETA-Platzhalter voll). SSoT = config.yaml `satelliten_tier_raten` + PORTFOLIO.md.

> ℹ️ **v3.7 (17.04.2026):** Fix 1 als Interaktionsterm (nicht Moat-Malus) gegen Double-Counting. Algebra-Projektion v3.5→v3.7: ASML 68→66 (bleibt D3, **Post-Q1 17.04. Vollanalyse: 68**), AVGO 85→84, MSFT 60→59, TMO 62→63, RMS 69→68, SU 71→69, APH 61→63, COST 69→69, V 86→86, BRK.B 75→75, VEEV 74→74.
>
> **Live-Verify-Status (Schritt-2-Restarbeit):** 5/11 verifiziert — **V (18.04. Forward 72→63 nach Advisor-Review), TMO (18.04. Forward 63→64, fcf_trend_neg struktureller Disclosure), ASML (±2, 17.04.), RMS (±2, 17.04.)**. V-Befund: Algebra-Projektion 86 war empirisch nicht haltbar (-23 pts). TMO-Befund: Algebra-Projektion empirisch haltbar (±1), FLAG-Entscheidung strukturell gerechtfertigt. Rest-Tickers (AVGO, MSFT, SU, BRK.B, APH) bei regulärem Earnings-Trigger. *(Hist. April-Snapshot; VEEV+COST seit 06/2026 exited — siehe Live-Tabelle oben.)* **Watch:** ASML Fwd P/E FY27 30,30 Grenzfall — bei <30 Score +6-8 möglich (D3→D4-Pfad, QT-P/E-Zweig deaktiviert).
>
> **18.04.2026 Updates:** (1) V-Forward-Vollanalyse + Rescoring → Score 63/D2, Sparrate 17,81€. (2) DEFCON-Threshold-Schema-SKILL-Drift gefixt (schemas.py: ≥80→D4, 65-79→D3, 50-64→D2) — betrifft Label 5 Tickern (BRK.B/VEEV/SU/COST/RMS: D4→D3) + APH (D3→D2), Sparraten unberührt bei D3/D4-Übergang. Nenner 8.5→8.0, volle Rate 33,53€→35,63€. (3) **TMO-Forward-Vollanalyse** → Score 63→64 (marginal +1), D2 unverändert, Sparrate 17,81€. fcf_trend_neg schema-getriggert (FY25 FCF 6293M / FY24 7267M = -13,4% YoY) aber **nicht aktiviert** per Advisor-Review: WC-Delta FY25 -1766M > FCF-Delta -974M = WC-Noise-Erklärung; 4J-Trajektorie FY22-25 $6,9→6,9→7,3→6,3B zeigt Plateau, kein Mehrjahres-Abwärtstrend; OpInc +5,1% YoY. Q1 23.04. = natürlicher Resolve-Gate. Befund: Schema-Validator ≠ SKILL-Regel-Semantik (CORE-MEMORY §11 Befund #4).

---

## Update-Kalender

| Datum | Position | Klasse | Trigger |
|-------|----------|--------|---------|
| pending (O3) | NOW / ZETA | A | Scoring-Nachzug — DEFCON-3-Platzhalter → echter Score (NOW US · ZETA US). KYCCF O3 DONE 13.06. → 67/D3 |
| overdue | SNPS / SPGI | B | Q1 Earnings Watchlist-Review — Nachholbedarf (PIPELINE #62) |
| Juni 2026 | — | — | Bausparvertrag 9.500€ + Steuererstattung ~2.000€ → Slot-Entscheidung |
| ~23.07. | APH | B | Q2 FY26 — China-Tax + CommScope-Net-Lev |
| ~Ende Juli | AMZN | B/C | Q2 FY26 — CapEx/OCF-FLAG-Re-Eval (Resolve-Gate <60%) + Vollanalyse |
| ~Ende Juli | V / TMO | B | V Q3 (Cross-Border-Velocity + ROIC-Verify) · TMO Q2 (Organic + Clario) |
| ~02./03.08. | BRK.B | B | Q2 FY26 — KHC-OTTI / GEICO / Form-13F (#36-#41) |
| Q2 2026 | GOOGL | C | FLAG-Review nach Earnings |
| **09.12.** (amc) | AVGO | B | Q4 FY26 — FLAG-Resolve-Gate #2 (Stand 04.09. $33,69M; Juni/Juli-Tranchen fallen ab ~08.10. aus dem 90d-Fenster) + Fwd-P/E-QT-Korridor-Watch |

---

## Ersatzbank

→ SSoT: [KONTEXT.md §6 Ersatzbank & Watchlist](KONTEXT.md#6-ersatzbank--watchlist). Faktortabelle-Ersatzbank am 2026-05-23 zu Pointer-only umgestellt (Drift-Surface-Cleanup; KONTEXT §6 ist Refresh-getrieben SSoT, hier hatten wir stale-Snapshot von pre-April). **SU-Ersatz-Brainstorm offen** (DE/Legrand/Siemens) → PIPELINE #77.

---

## Vault-Verknüpfungen

[[ASML]] · [[AVGO]] · [[MSFT]] · [[RMS]] · [[SU]] · [[BRK.B]] · [[V]] · [[TMO]] · [[APH]] · [[AMZN]] · [[NOW]] · [[KYCCF]] · [[ZETA]]

Konzept-Referenz: [[Faktortabelle-Architektur]] · [[Update-Klassen-DEFCON]] · [[Context-Hygiene]]

---

*🦅 Faktortabelle.md | Dynasty-Depot | DEFCON v3.7 | Stand: 2026-06-13 (KYCCF O3 67/D3 JGAAP-Primärquelle; O3-Backlog NOW/ZETA. Vorher 2026-06-08: 13-Roster, VEEV+COST DATA-Rows raus, NOW/KYCCF/ZETA Platzhalter-Rows rein, Sparraten-Nenner→3-Tier-Modell)*

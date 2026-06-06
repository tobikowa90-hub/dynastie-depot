# DEFCON Faktortabelle

**Stand:** 2026-05-23 (Live-State; letzter Score-Move BRK.B 75→71 am 04.05.; AMZN-Neuaufnahme 12. Satellit 18.05. Score 42/D1. Detail-Move-Chronik → CORE-MEMORY §12 + git log + score_history.jsonl)
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
| AVGO | ~30% | **5,54% GAAP / 51,1% §410-Goodwill-bereinigt (M&A-Compounder VMware/CA/Symantec/Brocade GW 57,2% Assets) vs WACC defeatbeta 15,96% (carryover, Tool-Bug `bc10_year`)** | ~67% | ~1,1x | Wide | **56** | **🟠 2** | 🔴 Insider-Selling 90d $106,4M (FLAG aktiv 27.04.2026 — Sparrate 0€, Resolve-Gate ≤$20M; Q2 04.06. Beat-Raise aber FLAG bleibt) | **2026-06-04** | **Q3 FY26 ~02.09. — !Analysiere Re-Eval; FLAG-Resolve-Check** |
<!-- DATA:V -->
| V | ~54% 5J | **9,89% defeatbeta vs WACC 10,48% [carryover 18.04.; Q3-Verify-Watch PIPELINE #21]** | 80,4% | 0,31x | Wide | **64** | **🟠 2** | ✅ Clean (D2 nach Rescoring-Revert 28.04. spätabends) | **2026-04-28** | **Q3 FY26 ~Ende Juli** — Cross-Border-Velocity + ROIC-Methodology-Verify |
<!-- DATA:MSFT -->
| MSFT | ~58% (9M FY26 bereinigt 57,7%) | **7,68% defeatbeta vs WACC 13,64% [Methodology-Watch FRED-Baseline-Verify Q4 PIPELINE]** | ~69% | ~0,5x (Net-Cash) | Wide | **50** | 🟠 2 | 🔴 CapEx/OCF aktiv (Trigger A erfüllt 9M-bereinigt 57,7%, B FAIL CY26 $190B Surprise, C ✅✅ Azure +39%cc — UND nicht vollumfänglich) | **2026-04-30** | **Q4 FY26 ~Juli** — CapEx-Plateau-Recheck + WACC-Methodology-Verify (Insider-Re-Score 14.05. DONE, Δ=0) |
<!-- DATA:TMO -->
| TMO | ~15% 5J | 8,04% GAAP / 17,18% bereinigt (GW-Ausnahme) vs WACC 10,44% | 40,9% | 2.57x (Pre-Clario) | Wide | **67** | **🟡 3** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR — Q1 FCF $825M +121% YoY, WC-Unwind bestätigt) | **2026-04-23** | **Q2 FY26 ~Ende Juli** — Organic-Akzeleration + Clario-Integration-Check |
<!-- DATA:RMS -->
| RMS | ~28% 5J FCF | 24.2% TTM | ~71% | Netto-Cash +€9,89B | Wide | 68 | 🟡 3 | ✅ Clean | 2026-04-17 | H1 2026 Report Juli/Aug 2026 |
<!-- DATA:VEEV -->
| VEEV | — | — | — | — | Wide | 74 | 🟡 3 | ✅ Clean | 2026-04-17 | Nächste Earnings |
<!-- DATA:SU -->
| SU | ~10% 5J | 10.48% TTM | ~42% | 2.51x | Narrow/Wide | 69 | 🟡 3 | ✅ Clean | 2026-04-17 | H1 2026 Earnings Juli/Aug 2026 |
<!-- DATA:BRK.B -->
| BRK.B | N/A (Float-Modell) | 5.6–7.8% GAAP (Insurance-Cycle, Float-Spread > Standard-ROIC) | N/A (Holdings) | Netto-Cash $380B effektiv (T-Bill-Settlement-bereinigt; nominal $397,4B − $17,2B Payable, 10-Q p.2-3 Primary; Forbes/Bill-Stone Secondary-Confirm) | Wide | **71** (Codex-R1-REJECT-Korrektur 75→71 Δ-4) | 🟡 3 | ✅ Clean (Insurance Exception) | **2026-05-04** | **Q2 FY26 ~02./03.08.** — KHC-OTTI-Resolve + GEICO-UW-Decel-Trend + Form-13F Apple-Trim-Magnitude + Buyback-Cashflow-Reconciliation |
<!-- DATA:APH -->
| APH | 19,0% FY25 | 28% bereinigt §410 (CommScope-GW) vs WACC 14,30% | 36,9% FY25 | 1,6x Q1 FY26 (post-CommScope) | Wide | **61** | 🟠 2 | 🔴 FLAG (Score-basiert <65 D3) | **2026-04-30** | **Q2 FY26 ~23.07.** — China-Tax-ETR-27%-Verify + CommScope-Net-Lev-Verlauf + ROIC-GW-Bereinigung-Full-Year-Check |
<!-- DATA:COST -->
| COST | ~3% 5J | 5.6% GAAP (MY 15.2%) | ~12.7% | <1x | Wide | 69 | 🟡 3 | ✅ Clean (Screener-Exception) | 2026-04-17 | Q1 FY27 Earnings ~Dez 2026 |
<!-- DATA:AMZN -->
| AMZN | ~1% 5J (FCF TTM $1,2B, CapEx-Boom) | 5,4% 6Q-Ø GAAP vs WACC 15,57% (defeatbeta; §410 N/A GW 2,6%) | 50,3% FY25 (3J +1,65pp/J) | NetDebt/EBITDA ~0,4x | Wide | **42** | **🔴 1** | 🔴 CapEx/OCF TTM 99,2% netto (FLAG aktiv 2026-05-15 — Sparrate 0€, Resolve-Gate <60%) | **2026-05-15** | **Q2 FY26 ~Ende Juli — CapEx/OCF-FLAG-Re-Eval + Vollanalyse** |
<!-- END_TABLE -->

**Aktive FLAGs:** MSFT (CapEx/OCF >60%) | **AVGO (Insider-Selling 90d $106M+ — aktiviert 27.04.2026)** | APH (Score-basiert, DEFCON 2 seit Threshold-Alignment) | **AMZN (CapEx/OCF TTM 99,2% netto — aktiviert 2026-05-15, Neuaufnahme 12. Satellit)**
**Struktureller Disclosure (kein FLAG):** ~~TMO (fcf_trend_neg)~~ **Resolved 23.04.2026** (Q1 FY26 FCF $825M +121% YoY, WC-Unwind-These bestätigt)
**Unter Review:** — (AVGO 27.04.2026 zu aktivem FLAG promotet)
**Analysierte Positionen:** 12/12 ✅ (AMZN Neuaufnahme 15.05.2026 Forward-Vollanalyse — 12. Satellit; V 18.04. + TMO 18.04./23.04. + AVGO/MSFT/APH 30.04. + BRK.B 04.05. Forward-Vollanalyse, Rest Algebra-Projektion)
**Offene Scores:** 0/12
**Tariff-Check:** APH abgeschlossen 15.04.2026 — China Revenue 14.7% (kein Revenue-FLAG), Supply-Chain CN/MY Risk-Map-Notiz aktiv
**Sparraten-Nenner:** 7×1,0 + 1×0,5 + 3×0 = **7,5** → volle Rate **38,00€** / D2-Rate **19,00€** (V allein) / FLAG (APH, MSFT, AVGO) **0€**

> ℹ️ **v3.7 (17.04.2026):** Fix 1 als Interaktionsterm (nicht Moat-Malus) gegen Double-Counting. Algebra-Projektion v3.5→v3.7: ASML 68→66 (bleibt D3, **Post-Q1 17.04. Vollanalyse: 68**), AVGO 85→84, MSFT 60→59, TMO 62→63, RMS 69→68, SU 71→69, APH 61→63, COST 69→69, V 86→86, BRK.B 75→75, VEEV 74→74.
>
> **Live-Verify-Status (Schritt-2-Restarbeit):** 5/11 verifiziert — **V (18.04. Forward 72→63 nach Advisor-Review), TMO (18.04. Forward 63→64, fcf_trend_neg struktureller Disclosure), ASML (±2, 17.04.), RMS (±2, 17.04.)**. V-Befund: Algebra-Projektion 86 war empirisch nicht haltbar (-23 pts). TMO-Befund: Algebra-Projektion empirisch haltbar (±1), FLAG-Entscheidung strukturell gerechtfertigt. Rest-Tickers (AVGO, MSFT, VEEV, SU, BRK.B, APH, COST) bei regulärem Earnings-Trigger. **Watch:** ASML Fwd P/E FY27 30,30 Grenzfall — bei <30 Score +6-8 möglich (D3→D4-Pfad, QT-P/E-Zweig deaktiviert).
>
> **18.04.2026 Updates:** (1) V-Forward-Vollanalyse + Rescoring → Score 63/D2, Sparrate 17,81€. (2) DEFCON-Threshold-Schema-SKILL-Drift gefixt (schemas.py: ≥80→D4, 65-79→D3, 50-64→D2) — betrifft Label 5 Tickern (BRK.B/VEEV/SU/COST/RMS: D4→D3) + APH (D3→D2), Sparraten unberührt bei D3/D4-Übergang. Nenner 8.5→8.0, volle Rate 33,53€→35,63€. (3) **TMO-Forward-Vollanalyse** → Score 63→64 (marginal +1), D2 unverändert, Sparrate 17,81€. fcf_trend_neg schema-getriggert (FY25 FCF 6293M / FY24 7267M = -13,4% YoY) aber **nicht aktiviert** per Advisor-Review: WC-Delta FY25 -1766M > FCF-Delta -974M = WC-Noise-Erklärung; 4J-Trajektorie FY22-25 $6,9→6,9→7,3→6,3B zeigt Plateau, kein Mehrjahres-Abwärtstrend; OpInc +5,1% YoY. Q1 23.04. = natürlicher Resolve-Gate. Befund: Schema-Validator ≠ SKILL-Regel-Semantik (CORE-MEMORY §11 Befund #4).

---

## Update-Kalender

| Datum | Position | Klasse | Trigger |
|-------|----------|--------|---------|
| 2026-04-28 (overdue) | SNPS | B | Q1 Earnings — Watchlist-Review (PIPELINE #62) |
| 2026-04-28 (overdue) | SPGI | B | Q1 Earnings — Watchlist-Review (PIPELINE #62) |
| 2026-05-27 | VEEV | B | Q1 FY27 Earnings |
| 2026-05-28 | COST | B | Q3 FY26 Earnings (Membership-Yield-Watch) |
| Mai 2026 | CPRT/ZTS/PEGA | B | Earnings → Watchlist-Review |
| Juni 2026 | — | — | Bausparvertrag 9.500€ + Steuererstattung ~2.000€ → Slot-Entscheidung |
| Q2 2026 | GOOGL | C | FLAG-Review nach Earnings |
| ~Ende Juli | AMZN | B/C | Q2 FY26 — CapEx/OCF-FLAG-Re-Eval (Resolve-Gate <60%) + Vollanalyse |
| Q3 FY26 | AVGO | C | !Analysiere — FLAG-Re-Eval + DEFCON-Refresh + Methodology-Watches |

---

## Ersatzbank

→ SSoT: [KONTEXT.md §6 Ersatzbank & Watchlist](KONTEXT.md#6-ersatzbank--watchlist). Faktortabelle-Ersatzbank am 2026-05-23 zu Pointer-only umgestellt (Drift-Surface-Cleanup; KONTEXT §6 ist Refresh-getrieben SSoT, hier hatten wir stale-Snapshot von pre-April). **SU-Ersatz-Brainstorm offen** (DE/Legrand/Siemens) → PIPELINE #77.

---

## Vault-Verknüpfungen

[[ASML]] · [[AVGO]] · [[MSFT]] · [[RMS]] · [[VEEV]] · [[SU]] · [[BRK.B]] · [[V]] · [[TMO]] · [[APH]] · [[COST]]

Konzept-Referenz: [[Faktortabelle-Architektur]] · [[Update-Klassen-DEFCON]] · [[Context-Hygiene]]

---

*🦅 Faktortabelle.md | Dynasty-Depot | DEFCON v3.7 | Stand: 2026-05-23 (00_Core Slim-Refactor — historische Score-Move-Comments + dead-Row-Backfill-Anchors gestrippt, Offene-Scores-Stub entfernt, Ersatzbank zu Pointer auf KONTEXT §6; alle Live-DATA-Anker erhalten)*

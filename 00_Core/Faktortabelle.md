# DEFCON Faktortabelle

**Stand:** 04.05.2026 (BRK.B Q1 FY26 Tag-+1 Vollanalyse + Codex-R1-REJECT-Korrektur — Score **75→71 (Δ-4)** post-R1-Sparring; D3/Sparrate 38€/FLAG ✅ Clean Insurance-Exception unverändert, keine Kaskade; korrigierte Sub-Karte F=35/M=19/T=1/I=10/S=6 — T-Block 200MA-Skala SKILL Z.603 strict 0/3, Sentiment +2 Annual-Meeting-Color V-Q2-Methodology-Drift entfernt, F-Block Forbes=Secondary kein +1-Lift; 15/15 Codex-HIGH-Antis pre-empted; 6 Q2-Methodology-Watches PIPELINE #36-#41)
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
| AVGO | ~30% | **3,98% GAAP / 45,7% §410-Goodwill-bereinigt (M&A-Compounder VMware/CA/Symantec/Brocade GW 57,2% Assets) vs WACC defeatbeta 15,96%** | ~65% | 1,41x | Wide | **53** | **🟠 2** | 🔴 Insider-Selling 90d $106,4M (FLAG aktiv 27.04.2026 — Sparrate 0€, Resolve-Gate ≤$20M) | **2026-04-30** | **Q3 FY26 — !Analysiere Re-Eval; FLAG-Resolve-Check** |
<!-- DEFCON-Label-Drift-Fix 18.04.: BRK.B/VEEV/SU/COST/RMS D4→D3, APH D3→D2 (Schema-Thresholds auf SKILL.md aligned). Sparraten unverändert bei D3/D4-Übergängen. -->
<!-- V-Score-Update 18.04.: 86 (Backfill) → 63 (Forward-Vollanalyse + Rescoring nach Advisor-Review). D4→D2, Sparrate 33,53€→17,81€. -->
<!-- Nenner 8.5→8.0, volle Rate 33,53€→35,63€. -->
<!-- DATA:V_OLD_BACKFILL -->
<!-- | V | ~54% 5J | ~9.9% Q TTM | ~80% | 0.31x | Wide | 86 | 🟢 4 | ✅ Clean | 2026-04-17 | Q2 FY26 Earnings ~22.04. | -->
<!-- DATA:V -->
<!-- V-Score-Update 28.04. mittags: 63 → 68 (Q2 FY26 Forward-Vollanalyse, Beat-Cascade). D2→D3, Sparrate 19,00€→35,63€. -->
<!-- V-Rescoring-Revert 28.04. spätabends nach Codex-HIGH-1+HIGH-2-Review: 68 → 64, D3→D2, Sparrate 35,63€→19,00€. HIGH-1: ROIC 1→7 via SKILL absolute alt-scale war regelwidrig (WACC vorhanden 10,48%); HIGH-2: kurs.referenz close_of_score_datum verletzt (27.04.-Proxy statt 28.04.-Close $309,30). ROIC-Carryover (1/8) + WACC-Carryover (10,48%) + Sentiment-Δ +1 (EPS-Rev post-beat) bleibt legitim. Nenner 8,0→7,5, volle Rate 35,63€→38,00€. defeatbeta-ROIC-Methodology-Watch in PIPELINE #21 für Q3 FY26 ~Ende Juli. -->
| V | ~54% 5J | **9,89% defeatbeta vs WACC 10,48% [carryover 18.04.; Q3-Verify-Watch PIPELINE #21]** | 80,4% | 0,31x | Wide | **64** | **🟠 2** | ✅ Clean (D2 nach Rescoring-Revert 28.04. spätabends) | **2026-04-28** | **Q3 FY26 ~Ende Juli** — Cross-Border-Velocity + ROIC-Methodology-Verify |
<!-- DATA:MSFT -->
<!-- MSFT-Score-Update 30.04.: 59 → 50 (Q3 FY26 Tag-+1 Vollanalyse, V-Q2-Mittelweg-Pfad). D2 unverändert, FLAG aktiv unverändert (Bull-Case Trigger A ✅ / B ❌ FAIL CY26 $190B vs Konsens $154,6B / C ✅✅ — UND nicht erfüllt). Sparrate 0€ unverändert (keine Kaskade). Codex-R1+R2-Doppel-Review (R1 strict 48 D1, R2 V-Q2-Mittelweg 50 D2 via Insider-Skip-Window-Carryover Backfill 6/10). Quality-Trap aktiv: Wide × Fwd P/E 22,44 → max 1; Wide × P/FCF 39,7x >35 → hart 0. ROIC 7,68% < WACC defeatbeta 13,64% (Methodology-Watch FRED-Baseline-Verify Q4). 4 PIPELINE-Items aktiv. -->
| MSFT | ~58% (9M FY26 bereinigt 57,7%) | **7,68% defeatbeta vs WACC 13,64% [Methodology-Watch FRED-Baseline-Verify Q4 PIPELINE]** | ~69% | ~0,5x (Net-Cash) | Wide | **50** | 🟠 2 | 🔴 CapEx/OCF aktiv (Trigger A erfüllt 9M-bereinigt 57,7%, B FAIL CY26 $190B Surprise, C ✅✅ Azure +39%cc — UND nicht vollumfänglich) | **2026-04-30** | **Q4 FY26 ~Juli** — CapEx-Plateau-Recheck + WACC-Methodology-Verify + Insider-Block-Re-Score post-14.05. |
<!-- TMO-Score-Update 18.04.: 63 (Backfill) → 64 (Forward-Vollanalyse). fcf_trend_neg schema-getriggert (FCF FY25 -13,4% YoY), NICHT aktiviert (WC-Noise-Erklärung, 4J-Plateau). Q1 23.04. = Resolve-Gate. -->
<!-- TMO-Score-Update 23.04.: 64 → 67 (Q1 FY26 Forward-Vollanalyse). Beat + Guidance-Raise. FCF $825M +121% YoY, OCF +65%, ΔWC -313M besser → fcf_trend_neg Resolve-Gate CLEAR, Schema-Watch deaktiviert. D2→D3, Sparrate 17,81€→33,53€. Nenner 8,0→8,5, volle Rate 35,63€→33,53€. -->
<!-- DATA:TMO_OLD_BACKFILL -->
<!-- | TMO | ~15% | 2.6% | ~42% | 2.57x | Wide | 63 | 🟠 2 | — | 2026-04-17 | 2026-04-23 Q1 Earnings | -->
<!-- DATA:TMO_PRE_Q1 -->
<!-- | TMO | ~15% 5J | 8,04% GAAP / 17,18% bereinigt | 40,9% | 2.57x | Wide | 64 | 🟠 2 | ✅ (fcf_trend_neg schema-trigger, nicht aktiviert) | 2026-04-18 | 23.04. Q1 FY26 Earnings | -->
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
<!-- END_TABLE -->

**Aktive FLAGs:** MSFT (CapEx/OCF >60%) | **AVGO (Insider-Selling 90d $106M+ — aktiviert 27.04.2026)** | APH (Score-basiert, DEFCON 2 seit Threshold-Alignment)
**Struktureller Disclosure (kein FLAG):** ~~TMO (fcf_trend_neg)~~ **Resolved 23.04.2026** (Q1 FY26 FCF $825M +121% YoY, WC-Unwind-These bestätigt)
**Unter Review:** — (AVGO 27.04.2026 zu aktivem FLAG promotet)
**Analysierte Positionen:** 11/11 ✅ ALLE SATELLITEN auf v3.7 rekalibriert (V 18.04. + TMO 18.04./23.04. Forward-Vollanalyse, Rest Algebra-Projektion)
**Offene Scores:** 0/11
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
| ~~2026-04-28~~ | ~~V~~ | — | **DONE (mittags)** Q2 FY26 Beat-Cascade — D2→D3 (Score 63→68). **REVERTED (spätabends)** nach Codex-HIGH-1+HIGH-2: Score 68→64, D3→D2, Sparrate 35,63€→19,00€. ROIC-Methodology-Verify Q3 FY26 in PIPELINE #21. |
| 2026-04-23 | TMO | B | Q1 2026 Earnings — FCF >$7.3B nötig für FCF-Yield >4% |
| 2026-04-28 | SNPS | B | Q1 Earnings — Watchlist (Score 76, Ersatz ASML) |
| 2026-04-28 | SPGI | B | Q1 Earnings — Watchlist (Score 74) |
| ~~2026-04-29~~ | ~~MSFT~~ | — | **DONE Tag-0** 10-Q-Read 29.04. (CapEx/OCF 9M-bereinigt 57,7% Trigger A ✅) + **Tag-+1 Vollanalyse 30.04.**: Score 59→**50** (Δ-9), D2 unverändert, FLAG aktiv unverändert. Bull-Case nicht vollumfänglich (Trigger B FAIL CY26 $190B vs Konsens $154,6B Surprise +23%). Codex-R1+R2-Doppel-Review (V-Q2-Mittelweg via Insider-Carryover). Sparrate 0€ unverändert. 4 PIPELINE-Items aktiv. |
| Mai 2026 | CPRT/ZTS/PEGA | B | Earnings → Watchlist-Review |
| Juni 2026 | — | — | Bausparvertrag 9.500€ + Steuererstattung ~2.000€ → Slot-Entscheidung |
| Q2 2026 | GOOGL | C | FLAG-Review nach Earnings |
| ~~2026-04-30~~ | ~~AVGO~~ | — | **DONE** Forward-Vollanalyse Score 84→53 (Δ-31), D4→D2, FLAG aktiv unverändert. Codex R1+R2-Pass 74% Confidence. Quality-Trap voll aktiv + §410-Goodwill-bereinigt ROIC 45,7%. Sparrate 0€ unverändert (keine Kaskade). 5 PIPELINE-Methodology-Watches #30-34. |
| Q3 FY26 | AVGO | C | !Analysiere — FLAG-Re-Eval (insider_selling_20m) + voller DEFCON-Refresh + Methodology-Watches-Resolve |

---

## Offene Scores

> Status aller 11 Satelliten siehe Haupttabelle oben + [PORTFOLIO.md](PORTFOLIO.md) (Live-SSoT). Diese Sektion war historisch redundant (100% Subset der Haupttabelle, Drift-Surface) und wurde am 02.05.2026 entfernt (PIPELINE #29 Kat. A).

---

## Ersatzbank

| Satellit | Ersatz | Score | Status |
|----------|--------|-------|--------|
| ASML | SNPS | 76 (D3) | v3.5 Ankerwert |
| AVGO | NVDA / MRVL | — | Kein Score |
| MSFT | GOOGL → ZTS/VEEV | 72 (D3, FLAG!) | GOOGL selbst FLAG — Alternativ: ZTS oder VEEV |
| RMS | RACE | — | Kein Score |
| VEEV | ZTS / SAP | — | Kein Score |
| SU | DE | — | Kein Score |
| BRK.B | MKL / FFH.TO | 82 (D4) | MKL bereit — bester Ersatz im Portfolio |
| TMO | ZTS | — | Vorbereitung aktiv bei D3 |
| APH | — | — | Kein Ersatz definiert |
| COST | — | — | Strukturell einzigartig — kein direkter Ersatz |

---

## Vault-Verknüpfungen

[[ASML]] · [[AVGO]] · [[MSFT]] · [[RMS]] · [[VEEV]] · [[SU]] · [[BRK.B]] · [[V]] · [[TMO]] · [[APH]] · [[COST]]

Konzept-Referenz: [[Faktortabelle-Architektur]] · [[Update-Klassen-DEFCON]] · [[Context-Hygiene]]

---

*🦅 Faktortabelle.md | Dynasty-Depot | DEFCON v3.7 | Stand: 30.04.2026 (AVGO Forward-Vollanalyse Score 84→53 D4→D2 FLAG aktiv unverändert; MSFT 59→50; APH 63→61) | Nächste Vollaktualisierung: 17.07.2026*

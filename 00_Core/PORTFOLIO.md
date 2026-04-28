# PORTFOLIO.md — Depot-Live-State

**Stand:** 28.04.2026 spätabends (V Rescoring-Revert nach Codex-HIGH-1+HIGH-2 — D3→D2, Nenner 8,0→7,5)

## Verweise
- [INSTRUKTIONEN.md §22](INSTRUKTIONEN.md#22-sparplan-formel-aktuell-18042026-v37) — Sparplan-Formel (Nenner-Berechnung)
- [INSTRUKTIONEN.md §18](INSTRUKTIONEN.md#18-sync-pflicht-logmd--core-memorymd--faktortabellemd--statemd--score_historyjsonl--flag_eventsjsonl) — Sync-Pflicht bei Score-/FLAG-/Sparraten-Change
- [PIPELINE.md](PIPELINE.md) — Nächste-Trigger-Liste synchron mit Hub-Critical-Alert
- [CORE-MEMORY.md §12](CORE-MEMORY.md#12-per-ticker-chronik) — Per-Ticker-Analyse-Historie
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail pro Ticker

---

## Portfolio-State (11 Satelliten)

| Ticker | Score | DEFCON | Rate | FLAG | Nächster Trigger |
|--------|-------|--------|------|------|------------------|
| AVGO | 84 | 🟢 4 | **0€** | 🔴 Insider-Selling 90d $106M+ (27.04.) | Q3 FY26 — !Analysiere Re-Eval |
| BRK.B | 75 | 🟡 3 | **38,00€** | ✅ Insurance Exception | Q-Earnings Mai |
| VEEV | 74 | 🟡 3 | **38,00€** | ✅ | Earnings-Trigger |
| SU | 69 | 🟡 3 | **38,00€** | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | **38,00€** | ✅ Screener-Exception | Q1 FY27 ~Dez |
| RMS | 68 | 🟡 3 | **38,00€** | ✅ Screener-Exception | H1 Juli/Aug |
| ASML | 68 | 🟡 3 | **38,00€** | ✅ | Q2 2026 (Q1 17.04. Vollanalyse ✅) |
| TMO | 67 | 🟡 3 | **38,00€** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR 23.04.) | Q2 FY26 ~Ende Juli — Organic-Akzeleration + Clario-Integration-Check |
| **V** | **64** | **🟠 2** | **19,00€** | ✅ Clean (D2 nach Rescoring-Revert 28.04. spätabends) | **Q3 FY26 ~Ende Juli — Cross-Border-Velocity + ROIC-Methodology-Verify** |
| APH | 63 | 🟠 2 | **0€** | 🔴 Score-basiert | 23.07. Q2 |
| MSFT | 59 | 🟠 2 | **0€** | 🔴 CapEx/OCF 83.6% | **29.04. Q3 FY26 — FLAG-Review** |

**Sparraten-Nenner:** 7×1,0 + 1×0,5 + 3×0 = **7,5** → 38,00€ volle / 19,00€ D2 / 0€ FLAG. **Summe 285€** ✓ (7×38,00 + 1×19,00 + 3×0 = 266,00 + 19,00 = 285,00)

> **28.04.2026 Änderung (spätabends, NEU):** V Rescoring-Revert nach Codex-HIGH-1+HIGH-2-Review der 28.04.-Vollanalyse. Score **68→64**, **D3→D2**, Sparrate **35,63€→19,00€**. **HIGH-1 (CHALLENGE):** ROIC 1→7 via SKILL absolute alternative scale war regelwidrig — SKILL erlaubt das nur "bei fehlender WACC-Schätzung", `wacc_pct=8.0` war gesetzt (carryover 18.04. wacc_pct=10.48). ROIC<WACC → Standard-Skala 0-1 Pkt. **HIGH-2 (CHALLENGE):** `kurs.referenz="close_of_score_datum"` semantisch verletzt — Kurs war 27.04.-close-Carryover-Proxy ($309,42), nicht 28.04.-close ($309,30). Provenance-Gate bestand formal (String-Equality), Intent verletzt. **Korrektur:** ROIC-Carryover (1/8) + WACC-Carryover (10,48%) + Kurs-Refresh ($309,30 yahoo_close_28.04.) + Sentiment-Δ +1 (EPS-Rev post-beat) bleibt legitim als einziger fresh-Block. Insider/Tech/Moat unverändert vom 18.04.-Carryover. **Kaskade:** Nenner 8,0→7,5 (V Gewicht 1,0→0,5), volle Rate 35,63€→38,00€ (7 andere D3/D4 +2,37€), D2-Rate 0€→19,00€ (V wieder allein in D2), FLAG-Rate (AVGO/APH/MSFT) bleibt 0€. **D2-Watch reaktiviert:** Beat allein lieferte methodisch nicht den D3-Pfad; Q3 FY26 ~Ende Juli mit ROIC-Methodology-Verify (PIPELINE #21) entscheidet. Original-Record `2026-04-28_V_vollanalyse` bleibt historisch in jsonl (append-only); operative Werte überschreiben durch Korrektur-Record `2026-04-28_V_rescoring`.
>
> **28.04.2026 Änderung (mittags, frühere Position):** V Q2 FY26 Forward-Vollanalyse — Beat-Cascade triggerte D2→D3 Re-Rating (Score 63→68). Beat-Headline: Net Rev $11,23B (+17%, höchstes Wachstum seit 2022) vs Konsens $10,75B (+4,5%); Non-GAAP EPS $3,31 (+20%) vs $3,099 (+6,8%); Cross-Border +12% cc; Other Revenue +41% (VAS-Hyperscaling); $20B neue Buyback-Authorization. **First-Live-Run Provenance-Gate** Pipeline (P3.5 8 Checks fail-close + Schicht D Block-Coverage) erfolgreich. **Spätabends durch Codex-Review-Korrektur überschrieben (siehe oben).**
>
> **27.04.2026 Änderung:** AVGO Insider-FLAG aktiviert (insider_selling_20m). OpenInsider-Cross-Check: 9 Transaktionen 90d, alle „S - Sale" ohne 10b5-1-Suffix; kein Cashless-Pattern. Skript-Lesart $106M (5× Schwelle), OpenInsider-Lesart $280M+ (14× inkl. Samueli $250M Dir 25.03.). Watchlist-These „Post-Vesting" widerlegt. Score 84/D4 unverändert — FLAG überschreibt. Sparrate 33,53€→0€. Kaskade: Nenner 8,5→7,5, volle Rate 33,53€→38,00€ (7 D3/D4 +4,47€), V D2-Rate 16,76€→19,00€. **23.04.2026 Änderung:** TMO Q1 FY26 Forward-Vollanalyse (67, D3) — Beat + Guidance-Raise, `fcf_trend_neg` Resolve-Gate CLEAR. D2→D3, Sparrate 17,81€→33,53€. Kaskade: Nenner 8,0→8,5, volle Rate 35,63€→33,53€ (7 andere D3/D4-Satelliten −2,10€), V D2-Rate 17,81€→16,76€. **18.04.2026 Änderung:** V-Forward-Vollanalyse (63, D2) ersetzt 17.04.-Backfill-Projektion (86, D4) — siehe CORE-MEMORY §11. Gleichzeitig Schema-SKILL-Threshold-Drift gefixt: 5 Tickers (BRK.B/VEEV/SU/COST/RMS) D4→D3 (Label-Fix, Sparrate unverändert), APH D3→D2 (FLAG überschreibt Sparrate weiterhin). Nenner schrumpft von 8.5 auf 8.0, volle Rate steigt 33,53€ → 35,63€.

---

## Aktive Watches

- **V D2-Watch (REAKTIVIERT 28.04.2026 spätabends nach Codex-Review-Revert):** Beat-Cascade allein lieferte methodisch nicht den D3-Pfad — ROIC-Sub-Score-Move 1→7 via SKILL absolute alternative scale war regelwidrig (WACC vorhanden 10,48% ≠ "fehlende WACC-Schätzung"). Score 68→64, D3→D2, Sparrate 35,63€→19,00€. **Q3 FY26 ~Ende Juli** entscheidet via:
  - **Cross-Border-Velocity:** Q2 +12% cc deceleriert von Pre-Q-Niveau >15%; <10% cc Q3 = Travel-Schwäche-Signal
  - **defeatbeta-ROIC-Methodology-Verify (PIPELINE #21):** 18.04. defeatbeta-Wert 9,89% empirisch inkonsistent mit Standard-NOPAT/IC-Formeln; Q3 Roh-Output-Dump + primary-source-Calc-Abgleich
  - **Litigation-MDL persistent (Risk-Map):** 6M FY26 $2,05B accrued litigation paid (Settlement-Tranche), weitere möglich
  - 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA (Tech-Carryover bestätigt)
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- ~~**AVGO Insider $123M (90d)**~~ **→ FLAG aktiviert 27.04.2026.** OpenInsider-Cross-Check zeigte 9 Transaktionen alle als „S - Sale" ohne 10b5-1-Suffix; kein Cashless-Pattern (M+S gleicher Tag). Watchlist-These „Post-Vesting" widerlegt. Skript-Diskretionär $106M (5× Schwelle), OpenInsider-Lesart $280M+ inkl. Samueli (Dir, $250M am 25.03. ohne 10b5-1-Marker). Sparrate 33,53€→0€, Kaskade Nenner 8,5→7,5. Re-Eval bei Q3 FY26 via !Analysiere AVGO.
- ~~**TMO D2-Kritik + FLAG-Resolve-Gate (NEU 18.04.)**~~ **Resolved 23.04.2026:** Q1 FY26 Beat + Guidance-Raise, FCF $825M +121% YoY, WC-Unwind-These bestätigt (ΔWC -1.112M vs -1.425M = +$313M besser), Management FY26-FCF-Guide $6,9-7,4B. `fcf_trend_neg` Resolve-Gate CLEAR, Schema-Watch deaktiviert. Score 64→67, D2→D3, Sparrate 17,81€→33,53€. Neue Watch: **Organic-Akzeleration Q1 +1% → H2 3-4%-Guide** + **Clario-Integration-Execution** (Q2 Ende Juli Re-Check). ZTS-Ersatz-Vorbereitung pausiert.
- **MSFT FLAG-Auflösungs-Pfad:** Q3 29.04. — bereinigtes CapEx/OCF <60% (Finance Lease $19.5B raus) = Auflösung. Darüber = Veto-Verschärfung.

---

## Nächste kritische Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| ~~27.04.~~ | ~~AVGO~~ | — | **DONE** Insider-FLAG aktiviert (insider_selling_20m, $106M+ diskretionär 90d). Re-Eval bei Q3 FY26 via !Analysiere. |
| ~~28.04.~~ | ~~V~~ | — | **DONE (mittags)** Q2 FY26 Beat-Cascade — D2→D3 Re-Rating (Score 63→68). **REVERTED (spätabends)** nach Codex-HIGH-1+HIGH-2-Review: Score 68→64, D3→D2, Sparrate 35,63€→19,00€. ROIC-Methodology-Verify Q3 FY26 in PIPELINE #21. |
| 28.04. | SNPS/SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — FLAG-Review** |
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |

---

*🦅 PORTFOLIO.md v1.0 | Dynasty-Depot | Live-State — default-load bei Session-Start | Stand: 28.04.2026 spätabends (V Rescoring-Revert D3→D2 nach Codex-HIGH-1+HIGH-2, Nenner 8,0→7,5)*

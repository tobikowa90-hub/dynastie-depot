# PORTFOLIO.md — Depot-Live-State

**Stand:** 28.04.2026 (V Q2 FY26 Forward-Vollanalyse — D2→D3 Re-Rating, Nenner 7,5→8,0)

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
| BRK.B | 75 | 🟡 3 | **35,63€** | ✅ Insurance Exception | Q-Earnings Mai |
| VEEV | 74 | 🟡 3 | **35,63€** | ✅ | Earnings-Trigger |
| SU | 69 | 🟡 3 | **35,63€** | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | **35,63€** | ✅ Screener-Exception | Q1 FY27 ~Dez |
| **V** | **68** | **🟡 3** | **35,63€** | ✅ Clean (D2-Watch RESOLVED 28.04.) | **Q3 FY26 ~Ende Juli — Cross-Border-Velocity-Check** |
| RMS | 68 | 🟡 3 | **35,63€** | ✅ Screener-Exception | H1 Juli/Aug |
| ASML | 68 | 🟡 3 | **35,63€** | ✅ | Q2 2026 (Q1 17.04. Vollanalyse ✅) |
| TMO | 67 | 🟡 3 | **35,63€** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR 23.04.) | Q2 FY26 ~Ende Juli — Organic-Akzeleration + Clario-Integration-Check |
| APH | 63 | 🟠 2 | **0€** | 🔴 Score-basiert | 23.07. Q2 |
| MSFT | 59 | 🟠 2 | **0€** | 🔴 CapEx/OCF 83.6% | **29.04. Q3 FY26 — FLAG-Review** |

**Sparraten-Nenner:** 8×1,0 + 0×0,5 + 3×0 = **8,0** → 35,63€ volle / 0€ D2 (entfällt) / 0€ FLAG. **Summe 285€** ✓ (8×35,63 + 3×0 = 285,04 ≈ 285,00)

> **28.04.2026 Änderung (NEU):** V Q2 FY26 Forward-Vollanalyse — Beat-Cascade triggert D2→D3 Re-Rating. Score 63→68 (Δ=+5: ROIC-Methodology-Correction 1→7 via SKILL absolute alternative scale post-Q2 NOPAT/IC ~48% [18.04. defeatbeta-derived 9,89% empirisch inkonsistent — `defeatbeta-ROIC-Methodology-Watch` für Q3-Verify offen]; Sentiment +1 EPS-Rev post-beat; Moat -1 konservativer ohne Transcript-Pricing-Power-Bonus; Tech -1 ATH-Distanz Mid-Band; Insider +1 carryover-rounding). Beat-Headline: Net Rev $11,23B (+17%, höchstes Wachstum seit 2022) vs Konsens $10,75B (+4,5%); Non-GAAP EPS $3,31 (+20%) vs $3,099 (+6,8%); Cross-Border +12% cc; Other Revenue +41% (VAS-Hyperscaling); $20B neue Buyback-Authorization. Sparrate 19,00€→35,63€. **Kaskade:** Nenner 7,5→8,0 (V Gewicht 0,5→1,0), volle Rate 38,00€→35,63€ (7 andere D3/D4 -2,37€), D2-Rate entfällt (war nur V), FLAG-Rate (AVGO/APH/MSFT) bleibt 0€. **First-Live-Run Provenance-Gate** Pipeline (P3.5 8 Checks fail-close + Schicht D Block-Coverage) erfolgreich.
>
> **27.04.2026 Änderung:** AVGO Insider-FLAG aktiviert (insider_selling_20m). OpenInsider-Cross-Check: 9 Transaktionen 90d, alle „S - Sale" ohne 10b5-1-Suffix; kein Cashless-Pattern. Skript-Lesart $106M (5× Schwelle), OpenInsider-Lesart $280M+ (14× inkl. Samueli $250M Dir 25.03.). Watchlist-These „Post-Vesting" widerlegt. Score 84/D4 unverändert — FLAG überschreibt. Sparrate 33,53€→0€. Kaskade: Nenner 8,5→7,5, volle Rate 33,53€→38,00€ (7 D3/D4 +4,47€), V D2-Rate 16,76€→19,00€. **23.04.2026 Änderung:** TMO Q1 FY26 Forward-Vollanalyse (67, D3) — Beat + Guidance-Raise, `fcf_trend_neg` Resolve-Gate CLEAR. D2→D3, Sparrate 17,81€→33,53€. Kaskade: Nenner 8,0→8,5, volle Rate 35,63€→33,53€ (7 andere D3/D4-Satelliten −2,10€), V D2-Rate 17,81€→16,76€. **18.04.2026 Änderung:** V-Forward-Vollanalyse (63, D2) ersetzt 17.04.-Backfill-Projektion (86, D4) — siehe CORE-MEMORY §11. Gleichzeitig Schema-SKILL-Threshold-Drift gefixt: 5 Tickers (BRK.B/VEEV/SU/COST/RMS) D4→D3 (Label-Fix, Sparrate unverändert), APH D3→D2 (FLAG überschreibt Sparrate weiterhin). Nenner schrumpft von 8.5 auf 8.0, volle Rate steigt 33,53€ → 35,63€.

---

## Aktive Watches

- ~~**V D2-Kritik (NEU 18.04.):** 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA, Crowd-Sell-Ratio 0%~~ **RESOLVED 28.04.2026** durch Q2 FY26 Beat-Cascade: Net Rev +17% (höchstes Wachstum seit 2022), Non-GAAP EPS +20%, Cross-Border +12% cc, Other Revenue +41% VAS-Hyperscaling, $20B neue Buyback-Auth. Score 63→68, D2→D3, Sparrate 19,00€→35,63€. **Neue Watch:** Cross-Border-Velocity Q3 FY26 ~Ende Juli (Q2 +12% cc deceleriert von Pre-Q-Niveau >15%; <10% cc Q3 = Travel-Schwäche-Signal). Litigation-MDL persistent (Risk-Map): 6M FY26 $2,05B accrued litigation paid (Settlement-Tranche), weitere möglich. **defeatbeta-ROIC-Methodology-Watch:** 18.04. Wert 9,89% empirisch inkonsistent mit Standard-Formeln; Q3-Verify offen.
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- ~~**AVGO Insider $123M (90d)**~~ **→ FLAG aktiviert 27.04.2026.** OpenInsider-Cross-Check zeigte 9 Transaktionen alle als „S - Sale" ohne 10b5-1-Suffix; kein Cashless-Pattern (M+S gleicher Tag). Watchlist-These „Post-Vesting" widerlegt. Skript-Diskretionär $106M (5× Schwelle), OpenInsider-Lesart $280M+ inkl. Samueli (Dir, $250M am 25.03. ohne 10b5-1-Marker). Sparrate 33,53€→0€, Kaskade Nenner 8,5→7,5. Re-Eval bei Q3 FY26 via !Analysiere AVGO.
- ~~**TMO D2-Kritik + FLAG-Resolve-Gate (NEU 18.04.)**~~ **Resolved 23.04.2026:** Q1 FY26 Beat + Guidance-Raise, FCF $825M +121% YoY, WC-Unwind-These bestätigt (ΔWC -1.112M vs -1.425M = +$313M besser), Management FY26-FCF-Guide $6,9-7,4B. `fcf_trend_neg` Resolve-Gate CLEAR, Schema-Watch deaktiviert. Score 64→67, D2→D3, Sparrate 17,81€→33,53€. Neue Watch: **Organic-Akzeleration Q1 +1% → H2 3-4%-Guide** + **Clario-Integration-Execution** (Q2 Ende Juli Re-Check). ZTS-Ersatz-Vorbereitung pausiert.
- **MSFT FLAG-Auflösungs-Pfad:** Q3 29.04. — bereinigtes CapEx/OCF <60% (Finance Lease $19.5B raus) = Auflösung. Darüber = Veto-Verschärfung.

---

## Nächste kritische Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| ~~27.04.~~ | ~~AVGO~~ | — | **DONE** Insider-FLAG aktiviert (insider_selling_20m, $106M+ diskretionär 90d). Re-Eval bei Q3 FY26 via !Analysiere. |
| ~~28.04.~~ | ~~V~~ | — | **DONE** Q2 FY26 Beat-Cascade — D2→D3 Re-Rating (Score 63→68, Sparrate 19,00€→35,63€). Neue Watch: Cross-Border-Velocity Q3 FY26 ~Ende Juli. |
| 28.04. | SNPS/SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — FLAG-Review** |
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |

---

*🦅 PORTFOLIO.md v1.0 | Dynasty-Depot | Live-State — default-load bei Session-Start | Stand: 28.04.2026 (V Q2 FY26 Beat-Cascade D2→D3, Nenner 7,5→8,0)*

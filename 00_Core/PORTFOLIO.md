# PORTFOLIO.md — Depot-Live-State

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
| AVGO | 84 | 🟢 4 | **0€** | 🔴 **Insider-Selling 90d $106M+ (NEU 27.04.)** | Q3 FY26 — !Analysiere Re-Eval |
| BRK.B | 75 | 🟡 3 | **38,00€** | ✅ Insurance Exception | Q-Earnings Mai |
| VEEV | 74 | 🟡 3 | **38,00€** | ✅ | Earnings-Trigger |
| SU | 69 | 🟡 3 | **38,00€** | ✅ | H1 Juli/Aug |
| COST | 69 | 🟡 3 | **38,00€** | ✅ Screener-Exception | Q1 FY27 ~Dez |
| RMS | 68 | 🟡 3 | **38,00€** | ✅ Screener-Exception | H1 Juli/Aug |
| ASML | 68 | 🟡 3 | **38,00€** | ✅ | Q2 2026 (Q1 17.04. Vollanalyse ✅) |
| **TMO** | **67** | **🟡 3** | **38,00€** | ✅ Clean (fcf_trend_neg Resolve-Gate CLEAR 23.04.) | **Q2 FY26 ~Ende Juli — Organic-Akzeleration + Clario-Integration-Check** |
| V | 63 | 🟠 2 | **19,00€** | ✅ | **28.04. Q2 FY26 — D2-Entscheidung** |
| APH | 63 | 🟠 2 | **0€** | 🔴 Score-basiert | 23.07. Q2 |
| MSFT | 59 | 🟠 2 | **0€** | 🔴 CapEx/OCF 83.6% | **29.04. Q3 FY26 — FLAG-Review** |

**Sparraten-Nenner:** 7×1,0 + 1×0,5 + 3×0 = **7,5** → 38,00€ volle / 19,00€ D2 / 0€ FLAG. **Summe 285€** ✓ (7×38,00 + 19,00 + 3×0 = 266,00 + 19,00 = 285,00)

> **27.04.2026 Änderung (NEU):** AVGO Insider-FLAG aktiviert (insider_selling_20m). OpenInsider-Cross-Check: 9 Transaktionen 90d, alle „S - Sale" ohne 10b5-1-Suffix; kein Cashless-Pattern. Skript-Lesart $106M (5× Schwelle), OpenInsider-Lesart $280M+ (14× inkl. Samueli $250M Dir 25.03.). Watchlist-These „Post-Vesting" widerlegt. Score 84/D4 unverändert — FLAG überschreibt. Sparrate 33,53€→0€. Kaskade: Nenner 8,5→7,5, volle Rate 33,53€→38,00€ (7 D3/D4 +4,47€), V D2-Rate 16,76€→19,00€. **23.04.2026 Änderung:** TMO Q1 FY26 Forward-Vollanalyse (67, D3) — Beat + Guidance-Raise, `fcf_trend_neg` Resolve-Gate CLEAR. D2→D3, Sparrate 17,81€→33,53€. Kaskade: Nenner 8,0→8,5, volle Rate 35,63€→33,53€ (7 andere D3/D4-Satelliten −2,10€), V D2-Rate 17,81€→16,76€. **18.04.2026 Änderung:** V-Forward-Vollanalyse (63, D2) ersetzt 17.04.-Backfill-Projektion (86, D4) — siehe CORE-MEMORY §11. Gleichzeitig Schema-SKILL-Threshold-Drift gefixt: 5 Tickers (BRK.B/VEEV/SU/COST/RMS) D4→D3 (Label-Fix, Sparrate unverändert), APH D3→D2 (FLAG überschreibt Sparrate weiterhin). Nenner schrumpft von 8.5 auf 8.0, volle Rate steigt 33,53€ → 35,63€.

---

## Aktive Watches

- **V D2-Kritik (NEU 18.04.):** 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA, Crowd-Sell-Ratio 0%. Q2 FY26 am 28.04. entscheidet: Beat + Guidance-Bestätigung → Technicals-Reversal möglich (zurück Richtung D3). Miss → weiterer Downshift Richtung D1.
- **ASML Fwd P/E FY27 = 30,30** — Grenzfall. Bei <30 deaktiviert Fix-1-Fwd-Zweig → Score +1 bis +2 möglich (D3→D4-Kandidat).
- ~~**AVGO Insider $123M (90d)**~~ **→ FLAG aktiviert 27.04.2026.** OpenInsider-Cross-Check zeigte 9 Transaktionen alle als „S - Sale" ohne 10b5-1-Suffix; kein Cashless-Pattern (M+S gleicher Tag). Watchlist-These „Post-Vesting" widerlegt. Skript-Diskretionär $106M (5× Schwelle), OpenInsider-Lesart $280M+ inkl. Samueli (Dir, $250M am 25.03. ohne 10b5-1-Marker). Sparrate 33,53€→0€, Kaskade Nenner 8,5→7,5. Re-Eval bei Q3 FY26 via !Analysiere AVGO.
- ~~**TMO D2-Kritik + FLAG-Resolve-Gate (NEU 18.04.)**~~ **Resolved 23.04.2026:** Q1 FY26 Beat + Guidance-Raise, FCF $825M +121% YoY, WC-Unwind-These bestätigt (ΔWC -1.112M vs -1.425M = +$313M besser), Management FY26-FCF-Guide $6,9-7,4B. `fcf_trend_neg` Resolve-Gate CLEAR, Schema-Watch deaktiviert. Score 64→67, D2→D3, Sparrate 17,81€→33,53€. Neue Watch: **Organic-Akzeleration Q1 +1% → H2 3-4%-Guide** + **Clario-Integration-Execution** (Q2 Ende Juli Re-Check). ZTS-Ersatz-Vorbereitung pausiert.
- **MSFT FLAG-Auflösungs-Pfad:** Q3 29.04. — bereinigtes CapEx/OCF <60% (Finance Lease $19.5B raus) = Auflösung. Darüber = Veto-Verschärfung.

---

## Nächste kritische Trigger (30 Tage)

| Datum | Ticker | Klasse | Aktion |
|-------|--------|--------|--------|
| ~~27.04.~~ | ~~AVGO~~ | — | **DONE** Insider-FLAG aktiviert (insider_selling_20m, $106M+ diskretionär 90d). Re-Eval bei Q3 FY26 via !Analysiere. |
| **28.04.** | **V** | **B** | **Q2 FY26 — D2-Entscheidung (Technicals-Reversal?)** |
| 28.04. | SNPS/SPGI | B | Watchlist-Review |
| **29.04.** | **MSFT** | **C** | **Q3 FY26 — FLAG-Review** |
| Mai | BRK.B/ZTS/PEGA | B | Q-Earnings + Slot-16 |

---

*🦅 PORTFOLIO.md v1.0 | Dynasty-Depot | Live-State — default-load bei Session-Start | Stand: 27.04.2026 (AVGO Insider-FLAG)*

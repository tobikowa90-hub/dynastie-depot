# DEFCON Faktortabelle

**Stand:** 17.04.2026 (v3.7 System-Gap-Release) | **Nächste Vollaktualisierung:** 17.07.2026
**Primärquelle:** config.yaml (hat immer Vorrang)
**Scoring-Version:** DEFCON v3.7 (Quality-Trap-Interaktion + OpM + Analyst-Bias-Kalibrierung + Fundamentals-Cap 50)

> ⚠️ VALIDIERUNGSHINWEIS
> Konflikt Faktortabelle ↔ config.yaml: config.yaml gewinnt immer.
> score_datum > 90 Tage → 🟡 veraltet markieren.
> Bei Datenzweifel → Shibui direkt abfragen.
> **Seit 17.04.2026:** Session-Start-Entry-Point ist `00_Core/STATE.md` — Faktortabelle ist on-demand Deep-Dive-Quelle. Sync-Pflicht unverändert (immer mit aktualisieren).

---

## Haupttabelle

| Position | FCF-Marge 5J | ROIC TTM | Gross Margin | Debt/EBITDA | Moat | Score | DEFCON | FLAG | Score-Datum | Nächstes Update |
|----------|-------------|----------|--------------|-------------|------|-------|--------|------|-------------|-----------------|
<!-- DATA:ASML -->
| ASML | — | — | ~52% | <1x | Wide | 66 | 🟡 3 | — | 2026-04-17 | Q1 Earnings 15.04. |
<!-- DATA:AVGO -->
| AVGO | ~30% | >20% | ~65% | ~2.5x | Wide | 84 | 🟢 4 | ⚠️ Insider $123M (vermutl. Post-Vesting — OpenInsider prüfen!) | 2026-04-17 | Q3 FY26 Earnings |
<!-- DATA:MSFT -->
| MSFT | ~25% | 7.5% | ~69% | ~1x | Wide | 59 | 🟠 2 | 🔴 CapEx/OCF >60% | 2026-04-17 | 2026-04-29 Q3 FY26 |
<!-- DATA:TMO -->
| TMO | ~15% | 2.6% | ~42% | 2.57x | Wide | 63 | 🟠 2 | — | 2026-04-17 | 2026-04-23 Q1 Earnings |
<!-- DATA:RMS -->
| RMS | ~28% 5J FCF | 24.2% TTM | ~71% | Netto-Cash +€9,89B | Wide | 68 | 🟢 4 | ✅ Clean | 2026-04-17 | H1 2026 Report Juli/Aug 2026 |
<!-- DATA:VEEV -->
| VEEV | — | — | — | — | Wide | 74 | 🟢 4 | ✅ Clean | 2026-04-17 | Nächste Earnings |
<!-- DATA:SU -->
| SU | ~10% 5J | 10.48% TTM | ~42% | 2.51x | Narrow/Wide | 69 | 🟢 4 | ✅ Clean | 2026-04-17 | H1 2026 Earnings Juli/Aug 2026 |
<!-- DATA:BRK.B -->
| BRK.B | N/A (Float-Modell) | 5.6–7.8% GAAP | N/A (Holdings) | Netto-Cash | Wide | 75 | 🟢 4 | ✅ Clean (Insurance Exception) | 2026-04-17 | Q-Earnings Mai 2026 |
<!-- DATA:V -->
| V | ~54% 5J | ~9.9% Q TTM | ~80% | 0.31x | Wide | 86 | 🟢 4 | ✅ Clean | 2026-04-17 | Q2 FY26 Earnings ~22.04. |
<!-- DATA:APH -->
| APH | — | — | ~32% | — | Narrow/Wide | 63 | 🟡 3 | 🔴 FLAG (Score-basiert) | 2026-04-17 | Q2 2025 Earnings 23.07. |
<!-- DATA:COST -->
| COST | ~3% 5J | 5.6% GAAP (MY 15.2%) | ~12.7% | <1x | Wide | 69 | 🟢 4 | ✅ Clean (Screener-Exception) | 2026-04-17 | Q1 FY27 Earnings ~Dez 2026 |
<!-- END_TABLE -->

**Aktive FLAGs:** MSFT (CapEx/OCF >60%) | AVGO (Insider $123M unter Review) | APH (Score-basiert, DEFCON 3)
**Unter Review:** AVGO (Insider $123M — wahrscheinlich Post-Vesting, manueller OpenInsider-Check vor FLAG-Aktivierung)
**Analysierte Positionen:** 11/11 ✅ ALLE SATELLITEN auf v3.7 rekalibriert
**Offene Scores:** 0/11
**Tariff-Check:** APH abgeschlossen 15.04.2026 — China Revenue 14.7% (kein Revenue-FLAG), Supply-Chain CN/MY Risk-Map-Notiz aktiv
**Stand:** 17.04.2026 — v3.7 System-Gap-Release (Quality-Trap-Interaktion + OpM + Analyst-Bias + Fundamentals-Cap 50)

> ℹ️ **v3.7 (17.04.2026):** Fix 1 als Interaktionsterm (nicht Moat-Malus) gegen Double-Counting. Einzige DEFCON-Klassifikations-Shifts: keine. ASML 68→66 (bleibt D3), AVGO 85→84, MSFT 60→59, TMO 62→63, RMS 69→68, SU 71→69, APH 61→63, COST 69→69, V 86→86, BRK.B 75→75, VEEV 74→74.
>
> **Live-Verify-Status (Schritt-2-Restarbeit):** 3/11 verifiziert am 17.04. — **TMO (±1), ASML (±2), RMS (±2)** alle innerhalb Toleranz bestätigt. Fix-1 empirisch validiert: differenziert (TMO nur P/FCF) vs. maximal (ASML/RMS beide Zweige). Rest-Tickers (AVGO, MSFT, VEEV, SU, BRK.B, V, APH, COST) bei regulärem Earnings-Trigger. **Watch:** ASML Fwd P/E FY27 30,30 Grenzfall — bei <30 Score +1-2 möglich (D4-Upside).

---

## Update-Kalender

| Datum | Position | Klasse | Trigger |
|-------|----------|--------|---------|
| ~2026-04-22 | V | B | Q2 FY26 Earnings — QuickCheck, Sparplan bestätigen |
| 2026-04-23 | TMO | B | Q1 2026 Earnings — FCF >$7.3B nötig für FCF-Yield >4% |
| 2026-04-28 | SNPS | B | Q1 Earnings — Watchlist (Score 79, Ersatz ASML) |
| 2026-04-28 | SPGI | B | Q1 Earnings — Watchlist (Score 77) |
| 2026-04-29 | MSFT | C | Q3 FY26 Earnings — FLAG-Review: CapEx/OCF <60% = FLAG-Auflösung |
| Mai 2026 | CPRT/ZTS/PEGA | B | Earnings → Watchlist-Review |
| Juni 2026 | — | — | Bausparvertrag 9.500€ + Steuererstattung ~2.000€ → Slot-Entscheidung |
| Q2 2026 | GOOGL | C | FLAG-Review nach Earnings |
| Q3 FY26 | AVGO | C | Insider-FLAG-Review — erneuter OpenInsider-Check |

---

## Offene Scores (0 von 11 — ALLE VOLLSTÄNDIG)

> ✅ **Alle 11 Satelliten haben formelle DEFCON v3.4 Vollanalysen** (Stand: 15.04.2026).
> Nächste Vollaktualisierung: bei Earnings-Trigger, Score-Verfall >180 Tage, oder Klasse-C-Event.

| Position | Score | DEFCON | Analyse-Datum | Nächster Trigger |
|----------|-------|--------|--------------|-----------------|
| ASML | 66 | 🟡 3 | 17.04.2026 | Q1 2026 Earnings 15.04. |
| AVGO | 84 | 🟢 4 | 17.04.2026 | Q3 FY26 Earnings |
| MSFT | 59 | 🟠 2 | 17.04.2026 | Q3 FY26 Earnings 29.04. (FLAG-Review) |
| TMO | 63 | 🟠 2 | 17.04.2026 | Q1 2026 Earnings 23.04. |
| RMS | 68 | 🟢 4 | 17.04.2026 | H1 2026 Report Juli/Aug 2026 |
| VEEV | 74 | 🟢 4 | 17.04.2026 | Nächste Earnings |
| SU | 69 | 🟢 4 | 17.04.2026 | H1 2026 Earnings Juli/Aug 2026 |
| BRK.B | 75 | 🟢 4 | 17.04.2026 | Q-Earnings Mai 2026 |
| V | 86 | 🟢 4 | 17.04.2026 | Q2 FY26 Earnings ~22.04. |
| APH | 63 | 🟡 3 | 17.04.2026 | Q2 2025 Earnings 23.07. (FLAG aktiv) |
| COST | 69 | 🟢 4 | 17.04.2026 | Q1 FY27 Earnings ~Dez 2026 |

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

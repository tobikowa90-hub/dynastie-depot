---
title: "Fact, Fiction, and Factor Investing"
date: 2023
type: source
subtype: academic-paper
tags: [factor-investing, value, momentum, quality, defensive, benchmark, external-validation]
url: https://www.pm-research.com/content/iijpormgmt/49/2
journal: "The Journal of Portfolio Management, Quantitative Special Issue 49(2), January 2023"
authors: "Michele Aghassi, Cliff Asness, Charles Fattouche, Tobias J. Moskowitz — AQR Capital"
status: processed
defcon_relevanz: "Externer Kalibrierungsanker: DEFCON = impliziter Long-Only-Multi-Faktor-Selektor (Value/Quality/Momentum/Defensive). Retrospective-Gate §29.2 — aggregierte Portfolio-SR muss im Band der AQR/Ilmanen-Benchmark liegen. NICHT pro Ticker anwendbar (AQR-Value-Spread ist Long-Short-Faktor-Instrument)."
related: "[[Factor-Investing-Framework]], [[QMJ-Faktor]], [[Buffett-Faktorlogik]], [[Backtest-Methodik-Roadmap]], [[Wissenschaftliche-Fundierung-DEFCON]], [[DEFCON-System]]"
---

# Aghassi, Asness, Fattouche, Moskowitz — Fact, Fiction, and Factor Investing (2023)

## Abstract (eigene Worte)
AQRs peer-reviewte Antwort auf alle gängigen Kritiken an systematischem Faktor-Investing. Strukturiert in 10 Facts & Fictions: Data-Mining-Vorwurf entkräftet, Faktor-Risiken dokumentiert, Diversifikations-Missverständnisse aufgelöst, Faktor-Timing als extrem schwierig belegt, Crowding-Vorwurf empirisch widerlegt. Öffentlich replizierbare Daten (Ilmanen et al. 2021 Century-Dataset, AQR-Library HMLDEVIL/UMD/QMJ/BAB, Kenneth French Library). Kern-Fokus: **Value, Momentum, Carry, Defensive/Quality** als peer-reviewed valide Faktoren. Size explizit verworfen.

## Kern-Zahlen & Thresholds

| Metrik | Wert | Quelle/Kontext |
|---|---|---|
| Multi-Faktor-Portfolio US-Stocks SR | 1,1 (t=10,8) | Ilmanen 2021, 1926–2020 |
| Multi-Faktor all-asset SR | 1,5 (t>14) | Ilmanen 2021 |
| OOS-Decay (McLean & Pontiff) | ~25% SR-Decay Post-Publication | + 32% durch Arbitrage |
| **Harvey/Liu/Zhu Hurdle** | **t-Stat ≥ 3** | Für Multiple-Testing-Correction |
| Trials bis False-Positive (t=3) | 393 unabhängig | Anstieg von 121 bei t=2 |
| Trials bis False-Positive (t=5) | 408.234 | |
| Trials bis False-Positive (t=8) | ~0,5 Billionen | |
| Value-Timing Korrelation zu Static-Value | r = 0,7 | Asness et al. 2017 |
| Drawdown-Tiefe bei SR 0,5 in 25J | **>30% mit ≥5% WS** | Normal, nicht Anomalie |

## 10 Facts & Fictions (Struktur)

| # | Thema | Kern-Aussage |
|---|---|---|
| 1 | Fiction: Data-Mined | Factors haben Economic Story + starkes OOS |
| 2 | Fact: Factors Are Risky | Drawdowns sind intrinsisch, nicht Fehler |
| 3 | Fiction: Diversification Fails | Verwechslung Diversifikation vs Hedge |
| 4 | Fact: Works Across Markets | Nicht Makro-sensitiv (außer Defensive: Inflation/Vol) |
| 5 | Fiction: New Economy Kills | Value überlebt auch Tech-Booms |
| 6 | Fact: Not Crowded | Value-Spreads widerlegen Crowding-Narrative |
| 7 | Fiction: Everyone Should | Per Definition unmöglich — jemand muss Gegenseite sein |
| 8 | Fact: Discipline > Timing | Factor-Timing ~ Static Exposure (r=0,7) |
| 9 | Fiction: Know Drawdown/Recovery | Timing von Vol/Cut/Add ist kaum möglich |
| 10 | Fact: Hard but Worth It | Sticking-with-it ist der Edge |

## DEFCON-Implikation — Faktor-Mapping

| DEFCON-Block | AQR-Faktor-Analog | Anmerkung |
|---|---|---|
| `fundamentals` (Fwd P/E, P/FCF) | **Value** (HML / HMLDEVIL) | Direkte Entsprechung |
| `moat` + Quality-Teile von `fundamentals` (FCF-Yield, Op-Margin, ROIC) | **Quality** (QMJ) / **Defensive** (BAB) | Asness/Frazzini/Pedersen 2019 Def. von QMJ |
| `technicals` (rel. Stärke, ATH-Distanz, Trend) | **Momentum** (UMD) | Jegadeesh/Titman 1993 Tradition |
| `sentiment` (eps_revision_delta) | Ergänzend fundamentaler Momentum | Chan et al. 1996 |
| `insider` | **nicht** im AQR-Kanon | Unser Edge für Concentrated Long-Only |
| Size | — | Von Autoren explizit verworfen (S. 11, Fn 21) |

**→ DEFCON ist faktor-wissenschaftlich fundiert**, keine arbitraere Matrix. 5 Blöcke sind aligned mit peer-reviewed-validen Faktoren + Insider als Spezifikum.

## Öffentliche Daten-Anker für spätere Benchmarks

- **Ilmanen et al. 2021:** Century-Dataset, 1920–2022, alle 4 Faktoren × 5 Asset-Klassen
- **Kenneth French Library:** klassische Fama-French-Factors
- **AQR Data Library:** HMLDEVIL, UMD, QMJ, BAB — direkte Zeitserien
- **Alquist et al. 2020:** Low-Risk Fact/Fiction (Vorgänger-Paper)

## Anwendungs-Grenzen für unser System

**Was funktioniert:**
- Aggregierte Satelliten-Portfolio-SR gegen Multi-Faktor-Benchmark bei Review 2028
- Einzel-Faktor-Exposure pro Ticker grob einschätzen (DEFCON-Mapping oben)
- Harvey/Liu/Zhu t-Stat ≥ 3 als Hurdle für neue DEFCON-Sub-Scores

**Was NICHT funktioniert:**
- AQR Value-Spread pro Ticker anwenden (ist Long-Short-Cross-Section-Instrument, nicht Single-Stock)
- Faktor-Timing aktiv betreiben (Paper zeigt: unmöglich reliable)
- Crowding-Signale als aktionable FLAGs (Paper zeigt: Crowding-Narrative meist falsch)

## Operationalisierung

- **§29.2** (Retrospective-Gate): aggr. Portfolio-SR im Band der AQR/Ilmanen-Multifaktor-Verteilung
- **§29.4** (neue Scoring-Parameter): t-Stat ≥ 3 Pflicht (Harvey/Liu/Zhu via dieses Paper)
- **!Analysiere-Checkliste:** Fwd P/E gegen eigene 5J-Range im Kommentartext (AQR-Value-Stretch-Intuition, kein Score-Impact)

## Backlinks
- [[Factor-Investing-Framework]] — operative Konzeptseite
- [[QMJ-Faktor]] — bestehendes Konzept; Ergänzung durch dieses Paper
- [[Buffett-Faktorlogik]] — cheap+safe+quality; AQR's Formalisierung
- [[Backtest-Methodik-Roadmap]] — Option A/B/C Benchmark-Anker
- [[PBO-Backtest-Overfitting]] — komplementäre Methoden-Ebene
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B16

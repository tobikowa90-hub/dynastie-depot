# 🔬 RETROSPECTIVE-GATE.md — §29 Retrospective-Analyse-Gate (4-Dimensionen-Framework)

**Version:** 1.0 (Pointer-Extraction 09.05.2026 aus INSTRUKTIONEN.md, PIPELINE #16 Variante A)

> Detail-Spec für `00_Core/INSTRUKTIONEN.md §29` (dort als Stub + Pointer geführt). Cross-Reference-Anker §28→§29 / §18→§29.5 / §27→§29.4 / §30→§29.3 / §4→§29-Layer (B25 → §29.7) bleiben funktional.

---

## 29. Retrospective-Analyse-Gate

> **`[FUTURE-ACTIVATION: 2028-04-01]` für §29.1-4 + §29.6 + §29.7. §29.5 Seven-Sins-Gate aktiv bereits jetzt bei Migration-Events.**

Systemischer Gate für jede retrospektive Analyse der `score_history.jsonl` (Strategy-Selection, Parameter-Tuning, Portfolio-Return-Validation). Aktivierung: Review 2028-04-01 ODER erste DEFCON-Parameter-Variation. §28 (Migration-Workflow) ist **komplementär**, nicht konkurrierend: §28 schützt Versions-Sprünge, §29 schützt Retrospective-Auswertungen.

**4-Dimensionen-Gate-Framework** (jede Dimension unabhängig validierbar — erweitert 26.04.2026 um §29.7 M&P-Discount-Layer aus B25 McLean-Pontiff):

### 29.1 Methoden-Gate — Overfitting (Bailey et al. 2015)

**Regel:** Vor jedem Strategy-Selection/Parameter-Tuning gegen `score_history.jsonl` PBO < 0,05 berechnen via CSCV.

**Implementierung:** `03_Tools/backtest-ready/pbo_cscv.py` bei Aktivierung. S=16 Default (12.780 Logits), N≥10 Trials, T≥2×Modellwahl-Fenster. CRAN R-Package `pbo` als Referenz-Implementierung.

**Komplementär:** walk-forward + k-fold + randomized backtests nach Palomar Ch 8.4 als Cross-Check (keine Ersetzung).

**In-the-Loop-Alternative (Sheppert 2026, B20):** GT-Score Composite-Objective (Performance × Significance × Consistency × Downside-Risk) als **Objective-Function während** Strategy-Selection — komplementär, nicht ersetzend zu PBO. PBO ist Post-hoc-Filter (Kandidat → Test), GT-Score ist In-the-Loop-Objective (Kandidat-Generierung optimiert bereits gegen Anti-Overfitting-Aggregat). Bei DEFCON-Parameter-Tuning ab 2028: beide Layer lauffähig — GT-Score als Tie-Break innerhalb PBO-Kandidatenmenge.

Quelle: [[Bailey-2015-PBO]] / [[PBO-Backtest-Overfitting]] / [[Sheppert-2026-GT-Score]] / [[Composite-Anti-Overfitting-Objective]]

### 29.2 External-Benchmark-Gate (Aghassi et al. 2023)

**Regel:** Aggregierte Satelliten-Portfolio-SR muss im Band der AQR/Ilmanen-Multifaktor-Benchmark liegen (Ilmanen et al. 2021 Century-Dataset). Bei signifikanter Abweichung: Ursache identifizieren (DEFCON-Mapping-Fehler, Selektions-Bias, echter Out-of-Band-Effekt).

**DEFCON-Faktor-Mapping** (Referenz für Benchmark-Auswahl):
- Fundamentals (Fwd P/E, P/FCF) → Value (HMLDEVIL)
- Moat + Quality-Fundamentals → Quality (QMJ) / Defensive (BAB)
- Technicals → Momentum (UMD)
- Insider → non-AQR-Edge, keine Benchmark

**Nicht anwendbar pro Ticker** — AQR-Value-Spread ist Long-Short-Cross-Section-Instrument, nicht Single-Stock.

Quelle: [[Aghassi-2023-Fact-Fiction]] / [[Factor-Investing-Framework]]

### 29.3 Temporal-Konsistenz (Flint & Vermaak 2021)

**Regel:** Score-Cadence muss mit der Faktor-Half-Life des dominanten DEFCON-Block konsistent sein.

| Faktor-Analog | Optimale Cadence | Unsere Cadence | Status |
|---|---|---|---|
| Value | 3-4M | Earnings-Trigger ~3M | ✅ aligned |
| Quality | 4-5M | Earnings-Trigger + jährliche Vollanalyse | ✅ konservativ |
| Momentum | 3M | Earnings-Trigger + Monitor | ✅ aligned |
| Investment | **1M** | Earnings-Trigger (zu träge bei aktiven FLAGs) | ⚠️ Watch |
| Insider | Real-time | OpenInsider | ✅ aligned |

**Investment-Watch:** MSFT-CapEx-FLAG + TMO-fcf_trend_neg sind Investment-Klasse. Bei Review 2028 prüfen, ob Monthly-Fundamentals-Refresh aktiviert werden muss.

Quelle: [[Flint-Vermaak-2021-Decay]] / [[Factor-Information-Decay]]

### 29.4 Neue-Parameter-Gate — Harvey/Liu/Zhu-Hurdle

**Regel:** Jede neue DEFCON-Sub-Komponente (neuer FLAG, Sub-Score, Metrik) muss **t-Stat ≥ 3** erreichen (nicht 2,0). Begründung: 121 unabh. Trials genügen für t=2-False-Positive, 393 für t=3. Academic Finance hat 400+ publizierte Faktoren — die meisten wären bei t≥3 verworfen.

**Aktivierungs-Trigger:** SOFORT (nicht 2028) — prospektiv auf alle zukünftigen DEFCON-Erweiterungen anwendbar. Ergänzt §28.1 Step 1 (Paper/Evidence-Check) um formale Signifikanz-Schwelle.

Quelle: [[Aghassi-2023-Fact-Fiction]] (zitiert Harvey/Liu/Zhu 2016)

### 29.5 Seven-Sins-Pre-Flight-Gate (Palomar 2025 Ch 8.2)

**Regel:** Vor jeder retrospektiven Analyse UND vor jedem Migration-Event (§28) folgende 7-Punkt-Checkliste:

- [ ] **Sin #1 Survivorship Bias:** Reject-Set aus Quick-Screener-Historie rekonstruieren (sonst explizit dokumentieren)
- [ ] **Sin #2 Look-Ahead Bias:** Nur `source=forward` Records, oder Backfill explizit deklariert
- [ ] **Sin #3 Storytelling Bias:** Rationale ex-ante in CORE-MEMORY §5, nicht post-hoc
- [ ] **Sin #4 Overfitting:** → §29.1 PBO<0,05
- [ ] **Sin #5 Turnover & Transaction Cost:** Sparplan-Gebühren + Spread modelliert
- [ ] **Sin #6 Outliers:** COVID 2020, Liberation Day 2026, GFC 2008 explizit behandelt
- [ ] **Sin #7 Asymmetric Pattern & Shorting:** **n.a.** (Dynasty-Depot ist strikt Long-Only)

**Aktivierungs-Trigger:** SOFORT bei Migration-Events. Bei retrospektiven Analysen ab 2028.

Quelle: [[Palomar-2025-Portfolio-Optimization]] / [[Seven-Sins-Backtesting]]

**Regime-Audit-Addendum (B19 FINSABER-Extension, 2026-04-20):**

Ergänzung zu Sin #4 (Overfitting) + Sin #6 (Outliers) bei Migration- und Retrospective-Events. FINSABER zeigt, dass LLM-Backtest-Vorteile unter realistischer Evaluation (20-Jahres-Fenster, 100+ Symbole, Bias-Mitigation) verschwinden und dass Bull/Bear-Subsample-SR-Divergenzen systematisch sind.

- [ ] **Bull/Bear-Subsample-SR-Trennung:** Score-Performance in Bull-Phasen (SPY > 200MA) und Bear-Phasen (SPY < 200MA) getrennt ausweisen. Divergenzen >2σ SR dokumentieren.
- [ ] **Symbol-Breite-Deklaration:** Backtest-Universum explizit benennen. Bei Universen <100 Symbole ("Dynasty-Satelliten-Cluster n=11") keine Skalierungs-Ansprüche formulieren.
- [ ] **Zeitfenster-Deklaration:** Backtest-Zeiträume <5 Jahre als "Proof-of-Concept" einordnen, nicht als strategische Evidenz.

**Aktivierungs-Trigger:** SOFORT bei Migration-Events (identisch mit §29.5-Kern). Skill-Self-Audit-Dimension in §33 adressiert.

Quelle: [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] / [[LLM-Investing-Bias-Audit]] / [[Regime-Aware-LLM-Failure-Modes]]

### 29.6 Portfolio-Return-Metrik-Layer (Palomar 2025 Ch 6)

**Regel:** Bei Aktivierung `risk-metrics-calculation`-Skill (bestehend) gegen `05_Archiv/portfolio_returns.jsonl` (Phase 3, in Aufbau): Sortino/CVaR/Calmar/Max-DD/IR nach Palomar-Ch-6-Formel-Konventionen berechnen.

**Voraussetzung:** portfolio_returns.jsonl-Persistenz ab Q2 2026 aktiv (Phase 3 dieses Plans).

**Aktivierungs-Trigger:** Review 2028-04-01 ODER ≥24 Monate sauberer Return-Serie.

**Interim-Gate:** 2027-10-19 Dry-Run für Data-Quality-Check.

**Composite-Objective-Alignment (B20 GT-Score, 2026-04-20):** Die Downside-Risk-Komponente des GT-Score-Composite-Objectives (Performance × Significance × Consistency × Downside-Risk) ist konzeptuell deckungsgleich mit Palomar Sortino/CVaR/Max-DD — downside-deviation-basierte Risk-Metriken. Bei §29.1/§29.6-Co-Aktivierung (ab 2028-04-01): GT-Score operationalisiert die vier Dimensionen als **In-the-Loop-Objective** während Strategy-Selection; Palomar liefert die mathematische Berechnungs-Konvention für die Einzel-Metrik-Ebene. Gemeinsamer Zweck: Score-Serie gegen Downside-Asymmetrien absichern, nicht nur Mean-Return optimieren.

Quelle: [[Palomar-2025-Portfolio-Optimization]] / [[Palomar-Methods-Reference]] / [[Sheppert-2026-GT-Score]] / [[Composite-Anti-Overfitting-Objective]]

### 29.7 M&P-Discount-Gate — Post-Publication-Decay (McLean & Pontiff 2016, B25)

**Regel:** In-sample-Performance-Claims aus akademischen oder externen Quellen werden vor Adoption mit dem **M&P-Discount-Faktor 0,42** multipliziert (= 1 − 0,58, Post-Publication-Decay-Median). Das Ergebnis ist die neue Plausibility-Erwartung für Forward-Performance.

```
realistische_forward_erwartung = in_sample_claim × 0,42
```

**Anwendungs-Bereich:** Externe Faktor-/Strategy-Claims (Paper, Vendor-Pitches, Backtest-Whitepapers) BEVOR sie in DEFCON-Erweiterungen, §28-Migrations oder §29-Validation-Vergleichen verankert werden. NICHT auf eigenes `score_history.jsonl` anwendbar — Score-Archiv ist seit 17.04.2026 post-publication-Sample (forward-only) und benötigt keinen zusätzlichen Discount.

**Wissenschaftliche Basis:** McLean & Pontiff (2016, JF 71(1)) testen 97 Cross-Sectional-Predictoren aus 80 Studien:
- Out-of-Sample-Decay −26% (statistical bias upper bound)
- Post-Publication-Decay −58% (publication-effect lower bound = 32pp Differenz)
- Decay stärker bei höheren in-sample-Returns/t-Stats (Mispricing + Investor-Learning-Hypothese)
- Korrelation zwischen Predictor-Portfolios STEIGT post-publication → Crowded-Trade-Risiko in Stress-Events

**Komplementarität zu anderen §29-Layern:**

| §29-Layer | M&P-Beitrag |
|---|---|
| §29.1 PBO/CSCV (Bailey) | Reicht nicht — testet nur in-sample-Overfitting; M&P-Discount adressiert zusätzlichen Post-Publication-Decay |
| §29.2 External Bench (Aghassi) | Reicht nicht — externe Daten reduzieren in-sample-Bias, nicht Publication-Decay |
| §29.3 Decay/Half-Life (Flint-Vermaak) | Direkter Match — beide messen verwandte Phänomene; §29.7 ist makro-publikationsbezogen, §29.3 mikro-faktoren-bezogen |
| §29.4 t-Hurdle ≥3 (Harvey/Liu/Zhu) | Notwendig, nicht hinreichend — M&P zeigt: HÖHERE t-Stats decayen STÄRKER |
| §29.5 Seven-Sins (Palomar) | Sin #6 Look-Ahead-Bias verwandt; Publication-Decay ist eigener Layer |

**Operative Konsequenzen:**

1. **Briefing-Sprache:** Keine in-sample-Performance-Claims im Briefing ohne Diskontierungsformel `claim × 0,42`. Jede zitierte Faktor-Outperformance aus Paper/Vendor → realistische Erwartung explizit ausweisen.
2. **§28.1-Erweiterung:** Migration-Workflow Step 1 (Paper/Evidence-Check) prüft NEU, ob Paper-Claim post-publication validiert wurde. Wenn nicht: M&P-Discount auf in-sample-Werte anwenden vor §29.4 t-Hurdle-Vergleich.
3. **Crowding-Watch:** Post-Publication-Increase in Predictor-Korrelationen (Lee/Shleifer/Thaler-Pattern) → DEFCON-Wide-Moat-Strategien können in Stress-Events korrelierter abstürzen als in-sample-Sharpe suggeriert. Faktor 5b FRED-Regime-Filter (geplant) adressiert das partiell.
4. **Score-Archiv-Markierung:** Bei retrospektiven Analysen der `score_history.jsonl` ab 2028 explizit ausweisen, dass Sample-Periode post-publication ist (kein zusätzlicher Discount nötig).

**Aktivierungs-Trigger:** Review 2028-04-01 ODER erste DEFCON-Parameter-Variation (parallel zu §29.1-4 + §29.6).

**Strukturelle DEFCON-Bestätigung (kein Aktion-Item):** M&P zeigen, dass Fundamentals-/Accounting-Predictoren STRUKTURELL robuster gegen Post-Publication-Decay sind als Price-/Trading-only-Predictoren (höhere Arbitragekosten, langsamere Korrektur). Das bestätigt die DEFCON-Block-Gewichtung 50/20/10/10/10 (Fundamentals + Moat dominieren) als wissenschaftlich tragfähige Architektur-Entscheidung.

Quelle: [[McLean-Pontiff-2016]] / [[Post-Publication-Decay]] (Concept-Page, Phase B2)

### 29.8 Aktivierungs-Reihenfolge bei Review 2028

1. §29.5 Sünden-Pre-Flight (Sin #1-#6) — wenn nicht alle grün: Stopp
2. §29.1 Methoden-Gate (PBO/CSCV, walk-forward Cross-Check)
3. §29.2 External-Benchmark (AQR/Ilmanen-Band)
4. §29.3 Temporal-Konsistenz (Cadence vs. Half-Life)
5. §29.6 Portfolio-Return-Metriken
6. **§29.7 M&P-Discount auf alle externen In-Sample-Claims (jede zitierte Paper-Outperformance × 0,42 vor Vergleich)**
7. Dann Options A–D aus [[Backtest-Methodik-Roadmap]] anwendbar

### 29.9 Rückverweise

Andere §§ die auf §29-Gates verweisen:
- §18 Sync-Pflicht → §29.5 Sin #2 (Look-Ahead)
- §27 Scoring-Hygiene → §29.4 t-Hurdle
- §28 Migration-Workflow → §29.1 PBO + §29.5 Seven-Sins + **§29.7 M&P-Discount auf externe In-Sample-Claims**
- §30 Live-Monitoring → §29.3 Half-Life (ab Phase 4)
- **§4 Befunde-Router → `meta-gate`-Befunde (B15, B16, B17, B18, B19, B20, B25) verweisen alle auf §29-Layer (B25 → §29.7)**

---

*🦅 RETROSPECTIVE-GATE.md v1.0 | Dynasty-Depot | §29-Detail-Spec — verbatim-Extraktion aus INSTRUKTIONEN.md (PIPELINE #16 Variante A) | Stand: 09.05.2026 spätabends Konsolidierungstag-Wave-3*

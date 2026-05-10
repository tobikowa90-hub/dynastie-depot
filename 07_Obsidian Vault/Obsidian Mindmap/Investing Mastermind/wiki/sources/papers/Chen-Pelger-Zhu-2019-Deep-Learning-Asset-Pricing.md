---
title: "Deep Learning in Asset Pricing"
date: 2019
type: source
subtype: academic-paper
medium: paper
tags: [defcon, deep-learning, sdf-approximation, source-only, deferred-stub, future-arch, phase-d-3]
url: https://pubsonline.informs.org/doi/10.1287/mnsc.2023.4695
venue: "PDF-Draft June 2019 (First March 2019); später Management Science Vol. 70 Nr. 2, 2024 (online 2023)"
authors: "Luyang Chen (Stanford ICME), Markus Pelger (Stanford MS&E), Jason Zhu (Stanford MS&E)"
status: deferred-stub
triage_class: source-only-deferred-D3
raw_path: "raw/papers/Chen, Pelger, Zhu (2023).pdf"
defcon_relevanz: "Phase-D-3 SOURCE-ONLY-deferred-Stub (Vault-Inventur 2026-05-10). Trigger: 2028-Review-Gate ODER nächste Backtest-Validation-Wave (R5/R6). Future-Reference als Benchmark-Modell für Long-Short-Portfolio-Optimierung; Linearitäts-Befund („SDF approximately linear on most chars in isolation, non-linearities matter for interactions") implizit-validiert die multiplikative DEFCON-Block-Aggregation."
sources: []
related:
  - "[[Wolff-Echterling-2023]]"
  - "[[Hou-Xue-Zhang-2015-q-Factor]]"
  - "[[Gu-Kelly-Xiu-2020]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
  - "[[DEFCON-System]]"
  - "[[luyang-chen]]"
  - "[[markus-pelger]]"
  - "[[jason-zhu]]"
created: 2026-05-10
updated: 2026-05-10
aliases:
  - "Chen Pelger Zhu 2019"
  - "Chen Pelger Zhu 2023"
  - "CPZ 2019"
  - "CPZ 2023"
  - "Deep Learning in Asset Pricing"
---

# Chen, Pelger & Zhu (2019/2023) — Deep Learning in Asset Pricing

> 🟡 **DEFERRED-STUB (Phase-D-3 source-only-deferred):** Voll-PDF in `raw/papers/Chen, Pelger, Zhu (2023).pdf` vorhanden, Volltext-Read aufgeschoben bis 2028-Review-Gate. Diese Stub-Page dokumentiert das DL-SDF-Framework als Future-Reference; Magnituden (OoS-Sharpe 2,6 / R² >90%) sind aus Abstract zitiert, nicht voll-verifiziert. Black-Box-Charakter + Compute-Anforderungen machen Adoption für Single-User-DEFCON nicht realistisch — die Page existiert primär als methodisches Benchmark + Linearitäts-Argument.

## Abstract (eigene Worte, sekundär-zitiert)

Chen, Pelger und Zhu konstruieren eine Stochastic-Discount-Factor-Approximation für US-Aktien via drei kombinierte Deep-Neural-Networks: (1) **Feedforward-DNN** für statisches Char-Mapping, (2) **LSTM** für zeitdynamische Sequence-Modellierung, (3) **GAN-Adversarial-Network** zur No-Arbitrage-Constraint-Enforcement im Training. Das resultierende SDF erreicht **Out-of-Sample-Sharpe 2,6** (vs. 1,7 linear-Modell, 1,5 naïve-DL ohne No-Arbitrage, 0,8 Fama-French-5) und **Cross-sectional-R² >90%** auf 46 Anomalien-Decile-Sortierungen.

## Drei Kern-Befunde (für DEFCON-Future-Reference relevant)

1. **No-Arbitrage-Constraint im Training ist nicht-trivial.** Naïve-DL-Modelle ohne Adversarial-No-Arbitrage-Term liefern OoS-Sharpe nur 1,5 vs. 2,6 mit GAN — das ist die zentrale methodische Innovation. Reine Char-Prediction ohne Pricing-Constraint produziert Overfitting auf historische Returns ohne Cross-Section-Konsistenz.

2. **SDF ist quasi-linear in einzelnen Chars, non-linear in Interaktionen.** Aus den Modell-Sensitivitäten: marginale Effekte einzelner Charakteristiken sind weitgehend monoton/linear; die Erklärungs-Kraft kommt aus 2-er- und 3-er-Interaktionen. Das ist Existenzargument für multiplikativ-aggregierende Score-Systeme (DEFCON-Block-Multiplikation, B6 Quality-Trap-Mechanik).

3. **OoS-Sharpe 2,6 ist Long-Short-Portfolio-Spread.** Long-Only-Konversion liefert deutlich kleineren Sharpe (analog DHS-Caveat). Für Long-Only-Stock-Picking ist die Black-Box-Natur des SDF ein zusätzliches Adoption-Hindernis (Code-Audit + Replikations-Disziplin).

## DEFCON-Future-Reference-Funktion

### Wann das Paper relevant wird

- 2028-Review-Gate Backtest-Methodik-Roadmap
- DEFCON-ML-Migration (eigene Migration-Session, nicht Phase-D)
- Bei Backtest-Skepsis-Cycle: CPZ-OoS-Sharpe als Plausibilitäts-Anker (was ist der theoretisch erreichbare DEFCON-Performance-Plafond?)

### Was das Paper NICHT begründet

- Adoption als Sub-Score-Element — Compute-/Black-Box-Constraints prohibitiv
- Direktes Performance-Versprechen für DEFCON — Long-Short-vs-Long-Only-Mapping nicht-trivial
- Linearitäts-Argument als alleinige Block-Konstruktions-Begründung — DEFCON-multiplikative-Aggregation hat eigene Begründungs-Linien (Quality-Trap, B7 ROIC-vs-WACC-Top-Prädiktor)

## Beziehung zu anderen DEFCON-Layern

| Bezug | Anknüpfung |
|---|---|
| **B7 Wolff/Echterling 2023** | ML-Top-Prädiktor-Identifikation (ROIC-vs-WACC) — CPZ liefert das DL-Framework, Wolff/Echterling die spezifische Variable-Importance-Hierarchie |
| **B19 FINSABER (Li/Kim/Cucuringu/Ma 2026)** | beide ML-getriebene Asset-Pricing-Papers; CPZ ist SDF-Approximation, FINSABER ist Bull/Bear-Asymmetrie-Audit; orthogonal aber methodisch verwandt |
| **Hou-Xue-Zhang 2015 q-Factor** | linearer Standard-Vergleichsbenchmark für CPZ; CPZ-Sharpe 2,6 vs. q-Factor-Sharpe ~1 |
| **Gu/Kelly/Xiu 2020** | erste systematische DL-Asset-Pricing-Studie ohne No-Arbitrage; CPZ erweitert um GAN-Term |
| **Multiplikative DEFCON-Block-Aggregation** | CPZ-Befund „Linearität in einzelnen Chars, Non-Linearität in Interaktionen" ist Existenzargument; aber nicht alleiniger Beweis |

## Limitationen

- **Black-Box / Replikations-Hürde:** Code-Veröffentlichung partiell, Reproduzierbarkeit schwierig.
- **Compute-prohibitiv:** Einzeluser-DEFCON kann das Modell nicht selbst trainieren oder updaten.
- **Sample-Periode:** US-CRSP, Decile-sortierte Anomalien; Non-US-Übertragbarkeit nicht im Original.
- **GAN-Stabilität:** GAN-Training ist notorisch sensitiv auf Hyperparameter — Replikations-Robustness ist offene Frage.
- **Long-Short-Konstruktion:** SDF ist Long-Short, DEFCON ist Long-Only.

## Backlinks

- [[Wolff-Echterling-2023]] — ML-Top-Prädiktor-Linie B7
- [[Hou-Xue-Zhang-2015-q-Factor]] — linearer Standard-Vergleichsbenchmark
- [[Gu-Kelly-Xiu-2020]] — erste systematische DL-Asset-Pricing-Studie
- [[Wissenschaftliche-Fundierung-DEFCON]] — Phase-D-3-source-only-deferred-Eintrag
- [[DEFCON-System]] — multiplikative-Aggregation-Existenzargument
- [[luyang-chen]], [[markus-pelger]], [[jason-zhu]] — Author-Entities

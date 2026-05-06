---
title: "...and the Cross-Section of Expected Returns"
date: 2016
type: source
subtype: academic-paper
tags: [factor-discovery, t-statistic-hurdle, multiple-testing, false-discovery, asset-pricing, source-only]
url: https://www.nber.org/papers/w20592
venue: "Review of Financial Studies 29(1), 2016, 5-68. NBER Working Paper 20592 (Oct 2014)"
authors: "Campbell R. Harvey (Duke Fuqua, NBER), Yan Liu (Texas A&M), Heqing Zhu (University of Oklahoma)"
status: processed
defcon_relevanz: "SOURCE-ONLY (anchors B16 §29.4-Hurdle). Strukturelle Begründung für die **t≥3-Hurdle** im DEFCON-Backtest-Validation-Framework (B16). Kern: Bei 313 publizierten Cross-Section-Faktor-Studien und multiple-testing-adjustierten Schwellen muss ein neuer Faktor **t≥3.0** erreichen, um echte Signifikanz zu beanspruchen — der traditionelle t≥2-Cutoff ist nach 50 Jahren Faktor-Mining nicht mehr zulässig. **Komplementär zu McLean/Pontiff (B25):** während HLZ multiple-testing-Bias adressiert (in-sample-Inflation), zeigt M&P den zusätzlichen Post-Publication-Decay (32% lower-bound). DEFCON-Konsequenz: §29.4 t≥3-Hurdle ist SOFORT aktiv (nicht erst 2028) — bei jedem zukünftigen Score-Element-Add muss t-Stat aus underlying-Forschung ≥3 sein."
sources: []
related:
  - "[[Factor-Investing-Framework]]"
  - "[[McLean-Pontiff-2016]]"
  - "[[Bailey-2015-PBO]]"
  - "[[Aghassi-2023-Fact-Fiction]]"
  - "[[Backtest-Methodik-Roadmap]]"
  - "[[DEFCON-System]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/harvey, liu & zhu.pdf"
aliases:
  - "Harvey Liu Zhu 2016"
  - "and the Cross-Section of Expected Returns"
  - "t-stat 3 Hurdle Paper"
---

# Harvey, Liu & Zhu (2016) — t≥3 Hurdle for Factor Discovery

## Abstract (eigene Worte)

Harvey, Liu und Zhu katalogisieren **316 publizierte Faktoren aus 313 Studien** in Top-Finance-Journals (1967-2014) und entwickeln ein Multiple-Testing-Framework, das den traditionellen t≥2.0-Cutoff für statistische Signifikanz neu kalibriert. Bei kumulierter Faktor-Mining-Aktivität über 50 Jahre + Publication-Bias (failed Faktoren werden nicht publiziert) muss ein neuer Faktor **t≥3.0** erreichen — und für besonders Mining-anfällige Sub-Bereiche (Behavioral-Faktoren, charakteristik-basiert) sogar **t≥3.5+**.

Methodisch:
- Frequentist-Multiple-Testing-Frameworks (Bonferroni, Holm, BHY) angepasst für Korrelation zwischen Faktoren + missing data (failed Studies)
- Faktor-Klassifikation in Common (113) vs. Individual (203) und Sub-Kategorien Financial/Macro/Microstructure/Behavioral/Accounting/Other
- Forward-Projection bis 2032: Hurdle wird weiter steigen wenn Faktor-Produktionsrate konstant bleibt

**Berühmtester Slogan:** "Most claimed research findings in financial economics are likely false." — direkte Anspielung auf Ioannidis (2005) "Why Most Published Research Findings Are False" aus Medical Literature.

## Direct-Operative DEFCON-Konsequenz (ankert B16)

§29.4 t-Hurdle ist **SOFORT aktiv** (nicht erst 2028-Backtest-Gate):

| Score-Element-Hinzufügung | t-Stat-Anforderung | Quelle |
|---|---|---|
| Theory-derived Faktor (z.B. CAPM-Beta) | t ≥ 2.5 | HLZ Limitation-Section |
| Empirical-derived Faktor | **t ≥ 3.0** | HLZ Hauptbefund |
| Behavioral-Faktor | t ≥ 3.5 | HLZ Sub-Kategorie-Adjustment |
| LLM-/ML-derived Faktor | **NICHT in DEFCON** ohne FINSABER-Audit (B19) + GT-Score-Validation (B20) | HLZ × FINSABER-Synthese |

→ Praktisch: Wenn jemand "X prädiziert Returns mit t=2.3" als Argument für DEFCON-Erweiterung bringt — ABLEHNEN mit HLZ-Verweis. Der traditionelle Cutoff war Bias-induziert.

## Komplementarität zu B25 (McLean/Pontiff)

```
HLZ:     False-Discovery-Bias    →  t≥3 Hurdle (in-sample-Inflation-Korrektur)
M&P:     Post-Publication-Decay  →  32% Lower-Bound (out-of-sample-Decay)
─────────────────────────────────────────────────────────────────
Total:   Plausibilitäts-Discount = (1/HLZ-Bias-Faktor) × 0.42 (M&P-Discount)
```

→ Ein Faktor mit publizierter t=2.5-Evidenz und 1% in-sample-Return ist nach beiden Korrekturen wahrscheinlich **<0.4% real-life-Edge** — zu wenig für DEFCON-Score-Element. Das ist die strukturelle Gate-Logik für künftige Erweiterungen.

## Limitations (HLZ-Selbstkritik, in DEFCON relevant)

- **Theory vs. Empirics-Diskriminierung:** HLZ behandeln alle Faktoren gleich; in der Praxis sollte theoretisch fundierte Empirik niedrigeren Hurdle haben. DEFCON's ROIC-WACC ist theoretisch hard ankert (Modigliani-Miller, Gordon-Modell) — das rechtfertigt t<3 wenn nötig.
- **Conditional vs. Unconditional Tests:** HLZ testen unconditional. Faktoren, die nur in Bull/Bear-Regimen wirken, werden marginal beurteilt. FINSABER (B19) adressiert das mit Bull/Bear-Subsample-Audit.
- **Sample bis 2014:** Post-2014 LLM/ML-Faktoren sind nicht inkludiert. Die FinDPO/FINSABER-Generation (B19, B24) braucht eigene HLZ-artige Meta-Studie.

## Backlinks

- [[Factor-Investing-Framework]] — Concept-Page (B16 hier ankert)
- [[McLean-Pontiff-2016]] — komplementärer Befund (B25)
- [[Bailey-2015-PBO]] — komplementäre PBO/CSCV-Methodik (B15)
- [[Aghassi-2023-Fact-Fiction]] — AQR-Praxis-Anwendung (anchors B16 ebenfalls)
- [[Backtest-Methodik-Roadmap]] — 2028-Review-Strategie
- [[DEFCON-System]] — §29-Backtest-Validation-Framework
- [[Wissenschaftliche-Fundierung-DEFCON]] — Source-only-Quelle (anchors B16 §29.4)
- [[Campbell R. Harvey]], [[yan-liu|Yan Liu]], [[heqing-zhu|Heqing Zhu]] — Author-Entities

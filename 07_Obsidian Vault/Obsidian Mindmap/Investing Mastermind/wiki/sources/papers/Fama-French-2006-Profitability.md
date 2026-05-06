---
title: "Profitability, Investment, and Average Returns"
date: 2006
type: source
subtype: academic-paper
tags: [fundamentals, profitability, investment, valuation-equation, cross-section, fama-french, source-only]
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=787467
venue: "Journal of Financial Economics 82(3), 2006, 491-518. First Draft Sep 2001, this draft Jun 2005"
authors: "Eugene F. Fama (University of Chicago Booth), Kenneth R. French (Dartmouth Tuck)"
status: processed
defcon_relevanz: "SOURCE-ONLY. Theorie-historisch wichtig: erste vollständige Empirik der Valuation-Equation-Decomposition (Mt/Bt = Σ E(Yt+τ − dBt+τ) / (1+r)^τ / Bt) für Cross-Section-Returns. Drei Vorhersagen werden bestätigt: (i) höheres B/M bei kontrolliertem Earnings/Investment → höhere Returns; (ii) höhere Profitability bei kontrolliertem B/M/Investment → höhere Returns; (iii) höheres Investment bei kontrolliertem B/M/Profitability → niedrigere Returns. Direkter Vorgänger zum FF-5-Faktor-Modell ([[Fama-French-2015-Five-Factor]]). Auch: Sloan-1996-Accruals-Effekt schrumpft auf <1% p.a. wenn man für B/M+Profit+Investment kontrolliert — wichtige Limitation der Accruals-Anomalie. **Sibling-Note:** Das geplante Paper #14 ('F/F 2004/2005 Draft Profitability, Growth, and Average Returns') ist die Working-Paper-Vorgängerversion dieses publizierten Papers — gleiche Autoren, gleiche These, frühere Iteration. Wird hier in der Source-Page mitgeführt, keine separate Page nötig (User-Decision 26.04.2026)."
sources: []
related:
  - "[[FCF-Primacy]]"
  - "[[5J-Fundamental-Fenster]]"
  - "[[Novy-Marx-2013]]"
  - "[[Fama-French-2015-Five-Factor]]"
  - "[[Hou-Xue-Zhang-2015-q-Factor]]"
  - "[[Sloan-1996]]"
  - "[[Accruals-Anomalie-Sloan]]"
  - "[[DEFCON-System]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/Profitability, Investment, and Average Returns.pdf"
aliases:
  - "Fama French 2006"
  - "FF 2006 Profitability"
  - "Profitability Investment Average Returns"
---

# Fama & French (2006) — Profitability, Investment, and Average Returns

## Abstract (eigene Worte)

Fama und French testen die Valuation-Equation-Predictions für expected Returns:

```
Mt/Bt = Σ E(Yt+τ − dBt+τ) / (1+r)^τ / Bt
```

Drei zugrundeliegende Predictions, alle empirisch bestätigt (1962-2003 NYSE/AMEX/NASDAQ):

1. **B/M-Effekt** (controlling for Earnings + Investment): höheres B/M → höhere expected Returns
2. **Profitability-Effekt** (controlling for B/M + Investment): höhere expected Earnings → höhere expected Returns
3. **Investment-Effekt** (controlling for B/M + Profitability): höheres Asset-Growth → niedrigere expected Returns

Methodisch wichtig: Alle drei Effekte sind **conditional** — sie zeigen sich nur bei Kontrolle der jeweils anderen zwei. Ein einfacher univariater B/M-Sort ohne Profit-/Invest-Kontrolle verfehlt die Theorie.

**Wichtige zusätzliche Befunde:**

- **Sloan-Accruals-Effekt** schrumpft auf <1% p.a. wenn B/M + Profit + Investment kontrolliert werden. Das ist eine zentrale Limitation der Accruals-Anomalie ([[Sloan-1996]] B14): viel der scheinbaren Accruals-Premium ist tatsächlich Investment-Effekt-Proxy. **DEFCON-Konsequenz:** Accruals-Ratio-Watch (B14-Erbe) bleibt valid, aber sollte nicht in Isolation interpretiert werden — Investment-Quality (CapEx-FLAG) ist bereits operativ und absorbiert Teil des Signals.
- **Composite Firm-Strength-Measures** (z.B. Piotroski F-Score) prädizieren Returns — F-Score ist mit FF-2006-Logik kompatibel: aggregiert Profitability + Investment-Discipline + Bilanz.

## Sibling-Note: F/F 2004/2005 Draft "Profitability, Growth, and Average Returns"

Im Brainstorm-Selektions-Matrix war ein separates Paper #14 ("F/F 2004 Draft") aufgeführt. Nach Inhaltsprüfung: **#14 ist die Working-Paper-Vorgängerversion dieses publizierten Papers** — gleiche Autoren, gleiche Valuation-Equation-Decomposition, frühere Iteration mit "Growth" statt "Investment" im Titel und qualitativ ähnlichen Befunden:

- Bei kontrolliertem B/M: höhere Profitability + moderates Wachstum → höhere expected Returns
- Hohes Asset-Growth → niedrigere Returns

Da die FJE-2006-Publikation die finale, peer-reviewed Version ist und keine substanziell anderen Befunde liefert, wird #14 hier mitgeführt statt als separate Page angelegt (User-Decision 26.04.2026: "ist einfach nur ein Auszug aus #12"). Falls künftig differential-historische Analyse nötig: #14 ist im NBER-Archiv unter "Profitability, Growth, and Average Returns" auffindbar.

## DEFCON-Konsequenzen

| FF-2006 Befund | DEFCON-Status |
|---|---|
| B/M-Effekt | DEFCON nutzt **Forward**-Bewertung (Fwd-P/E, P/FCF), nicht klassisches B/M; kontextuell konsistent |
| Profitability-Effekt | ROIC + OpM bereits Score-Element |
| Investment-Effekt (negative Korrelation zu Returns) | CapEx-FLAG (DIE heilige Regel) operationalisiert das aggressiv (Threshold-basiert, nicht Faktor-basiert) |
| Conditional-Nature | DEFCON-Block-Gewichtung respektiert Multi-Faktor-Komplementarität (50/20/10/10/10) |
| Accruals-Schrumpfung mit Kontrollen | Watch-Item: Accruals-Ratio nicht in Isolation interpretieren — bei TMO-Q1-FY26-Analyse (23.04.2026) war WC-Unwind klare Story, nicht Accruals-Anomaly-pur |

## Backlinks

- [[FCF-Primacy]] — Fwd-FCF-Yield-Logik (Mt-Decomposition-konform)
- [[5J-Fundamental-Fenster]] — expected-Earnings-Trendperspektive
- [[Novy-Marx-2013]] — Profitability-Pillar-Detail
- [[Fama-French-2015-Five-Factor]] — finaler 5-Faktor-Modell-Erbe
- [[Hou-Xue-Zhang-2015-q-Factor]] — paralleles q-Factor-Modell, konvergent
- [[Sloan-1996]] — Accruals-Quelle, hier kritisch eingeordnet
- [[Accruals-Anomalie-Sloan]] — Concept-Page (Watch-Verweis)
- [[DEFCON-System]] — Fundamentals-Block + CapEx-FLAG validated
- [[Wissenschaftliche-Fundierung-DEFCON]] — Source-only-Quelle
- [[Eugene F. Fama]], [[Kenneth R. French]] — Author-Entities

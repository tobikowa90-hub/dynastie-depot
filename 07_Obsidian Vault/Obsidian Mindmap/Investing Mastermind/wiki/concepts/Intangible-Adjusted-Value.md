---
title: "Intangible-Adjusted Value"
type: concept
tags: [defcon, intangible-capital, total-q, goodwill-bereinigung, fundamentals-block, b29, active-scoring-validation]
created: 2026-05-09
updated: 2026-05-10
sources: [Peters-Taylor-2017-Intangible-Capital]
related: [Wissenschaftliche-Fundierung-DEFCON, Quality-Trap, QMJ-Faktor, FCF-Primacy, Buffett-Faktorlogik, Wolff-Echterling-2023, Buffetts-Alpha, DEFCON-System, AVGO, MSFT, V, BRKB]
wissenschaftlicher_anker: "B29 (Peters & Taylor 2017, JFE 123(2)) — Total q als investment-q-Korrektur über physisches PLUS intangibles Kapital; Hayashi-Bedingung wird unter Total q nicht abgelehnt, unter klassischem Tobin's q schon. Theoretische Fundierung der seit AVGO-30.04.2026 operativen §410-Goodwill-Bereinigung (NOPAT / (Invested Capital − Goodwill)) als Mainstream-Asset-Pricing-Anker statt rein-Präzedenz-Argument."
konfidenzstufe: peer-reviewed
defcon_block: "Fundamentals-Block (50 Pt., siehe SKILL.md §410 IC-bereinigte ROIC + Tie-Break IC-GW vs Regel-4)"
operative_regel: "Bei Goodwill > 40% Assets dominiert §410 IC-Bereinigung über Regel-4 Cash-ROIC-Add-Back; bei moderaten Goodwill-Anteilen (30-40%) bleibt Regel-4 Default. §410 ist KEIN ad-hoc-Heuristikum, sondern theoretisch fundiert via Total-q-Logik (Goodwill als externalisiertes Intangibles-Capital bei M&A-Compoundern)."
aliases:
  - "Total-q"
  - "Total q"
  - "Intangible-Adjusted Book"
  - "IC-bereinigt"
  - "Goodwill-Bereinigung-Theorie"
---

# Intangible-Adjusted Value

> Peters & Taylor (2017) zeigen: Investment-q-Anomalien klassischer Tobin's-q-Modelle sind ein Mess-Artefakt, nicht ein Markt-Versagen. Bei korrekter Capital-Messung (physisch + intangibles) erfüllt das Investment-q-Modell die Hayashi-Bedingung — Capital-Effizienz prädiziert Investitionsverhalten. Goodwill bei M&A-Compoundern ist Approximation für externalisiertes Intangibles-Capital; rohe GAAP-ROIC mit Bilanz-Goodwill verschleiert die ökonomische Capital-Effizienz strukturell.

## Operative Definition

**Intangible-Adjusted Value** bezeichnet den Bewertungs-Frame, der Intangible Capital (R&D-Capital + Organisation-Capital + extern erworbene Goodwill-Approximationen) als gleichberechtigte Komponente des Total-Capital-Stocks neben physischem PP&E behandelt. Klassisches Tobin's q ignoriert diese Komponente; Total q (Peters/Taylor 2017) berücksichtigt sie.

Im DEFCON-Kontext wird diese Theorie operativ über **§410 IC-Bereinigung** umgesetzt — eine vereinfachte Version, die Goodwill aus Invested Capital herausrechnet und damit die Bilanz-Verzerrung bei M&A-Compoundern adressiert, ohne ein vollständiges Total-q-Capital-Modell zu rekonstruieren.

| Variante | Formel | Verwendung |
|---|---|---|
| **Klassisches ROIC (GAAP)** | NOPAT / Invested Capital | Default für Non-M&A-Heavy-Firmen, Goodwill < 30% Assets |
| **Regel-4 Cash-ROIC** | (NOPAT + 0,65 × D&A) / Invested Capital | Moderate Goodwill-Anteile 30-40% Assets |
| **§410 IC-bereinigt** | NOPAT / (Invested Capital − Goodwill) | M&A-Compounder mit Goodwill > 40% Assets |
| **Total q (full Peters/Taylor)** | Total-Market-Value / (PP&E + R&D-Capital-PIM + OrgCap-PIM) | NICHT in DEFCON v3.7 — Reconstruction-Aufwand prohibitiv für 4-Min-Score-Routine |

## Theoretische Brücke Goodwill ↔ Intangibles

Peters/Taylor diskutieren Goodwill nur peripher (S. 13 + Robustness Table 9 „Exclude Goodwill" — Hauptbefunde unverändert). **Crouzet/Eberly/Eisfeldt/Papanikolaou (2022)** ([[Crouzet-Eberly-Eisfeldt-Papanikolaou-2022-Economics-Intangible-Capital]], JEP 36(3) Summer 2022, S. 29-52) formalisieren über die zwei distinguishing properties Non-Rivalry in Use + Limited Excludability: bei Acquisition-Heavy-Sektoren ist Bilanz-Goodwill eine Lower-Bound-Approximation für extern erworbenes Intangibles-Capital. Die Logik:

1. Eine Firma erwirbt eine andere für $X über Bilanz-Buchwert hinaus.
2. Dieser Excess-Payment ($X − Bilanz-Buchwert-Target) reflektiert die ökonomische Bewertung der nicht-bilanzierten Intangibles des Targets (Brand, Customer-Relationships, Tech-Stack, Talent-Base).
3. GAAP zwingt zur Klassifikation als Goodwill (statt Identifizierbares-Intangibles) für den Großteil des Excess.
4. Operativ ist dieser Goodwill der ökonomisch produktive Capital-Stock — er repräsentiert echtes, gewinnbringendes Intangibles-Capital, das nur bilanzrechtlich nicht weiter dekomponiert werden konnte.

→ **§410-Logik:** Wer ROIC mit Goodwill im Nenner berechnet, doppelzählt: das Goodwill ist bereits im Zähler (NOPAT) abgebildet (die Earnings entstehen aus dem Intangibles-Capital, das den Goodwill rechtfertigt), und das gleiche Capital steht zusätzlich nochmal im Nenner. Korrekt ist entweder Total q (Capital im Nenner = ökonomisches Capital inkl. aller Intangibles) ODER Goodwill aus Invested Capital herausrechnen — letzteres ist die DEFCON-Operationalisierung.

## DEFCON-Anwendungsfälle (Präzedenz-Anker)

| Ticker | Datum | Goodwill-% Assets | §410-Ergebnis | Codex-Status |
|---|---|---|---|---|
| **AVGO** | 30.04.2026 (Forward-Vollanalyse) | 57,2% (M&A-Compounder VMware $61B + CA $19B + Symantec $10B + Brocade $5,5B) | NOPAT $22,2B / IC-GW $48,6B = **45,7% bereinigt** vs GAAP **3,98%** | Codex-R1-APPROVE mit Confidence-Caveat 7/8 statt 8/8 wegen StockAnalysis-Methodology-Drift |
| **MSFT** | 30.04.2026 (Q3-Vollanalyse) | ~26-28% (Activision $69B + LinkedIn $26B + GitHub $7,5B) | ROIC 6Q-Ø 7,68% < WACC 13,64% — bereinigt nicht in 7-8/8-Bereich, daher §410 angewendet aber kein Score-Block-Move | Methodology-Watch PIPELINE #25 (defeatbeta-WACC-Verify Q4) |
| **V** | 18.04.2026 (Q1-Vollanalyse) | ~15-18% (Visa Europe Acquisition + Plaid-Failed-Bid-Goodwill-Carry) | defeatbeta liefert ROIC 9,89% (suspekt — Standard-NOPAT/IC liefert >25%); Methodology-Watch in PIPELINE #21 | Q3 FY26 Methodology-Verify deferred |

## Beziehung zu anderen DEFCON-Layern

- **Quality-Trap (B6, Morningstar Wide-Moat)** — deckelt Wide-Moat × teure Bewertung-Subscores. Verbindung zu B29: bei intangibles-dominierten Wide-Moat-Namen ist die teure Bewertung partiell Total-q-perspektivisch korrigierbar. KEINE Quality-Trap-Bypass-Funktion — Quality-Trap arbeitet auf Fwd-P/E + P/FCF (cash-basiert, Intangibles-neutral), nicht auf P/B (bilanz-basiert, Intangibles-verzerrt).
- **B5 Buffetts-Alpha cheap+safe+quality** — Total-q ist die theoretische Brücke zwischen „cheap" und „quality" für intangibles-dominierte Firmen. Buffett-Faktorlogik (Quality dominant) profitiert von B29-Anker.
- **B8 Wolff/Echterling 2023 ROIC-vs-WACC** — wird durch Total-q-Hayashi-Bedingung theoretisch unterfüttert: Capital-Effizienz prädiziert Returns iff Capital-Messung korrekt. §410 ist die Operationalisierung, B8 die empirische Validation.
- **B13 Novy-Marx GP/TA** — `design-rejected` (§27.1 Double-Counting). B29 legitimiert Nicht-Reaktivierung: GP/TA hat dasselbe Capital-Mess-Problem wie ROIC ohne IC-Bereinigung; reaktivierungs-relevante Variante wäre GP/Total-Capital, was außerhalb DEFCON-v3.7-Scope liegt.

## Was diese Page NICHT umfasst

- **Vollständiges Total-q-Capital-Reconstruction** (Peters/Taylor PIM-Methode mit Branch-spezifischen R&D/OC-Depreciation-Rates) — Reconstruction-Aufwand prohibitiv für 4-Min-Score-Routine; §410 ist die pragmatische Approximation.
- **Intangible-Adjusted Book/Value als eigener Faktor-Score** — wäre §28.1-Migration-Workflow mit §29.4 t-Hurdle + §29.7 M&P-Discount. Deferred. Trigger: gehäuftes Auftreten von Bilanz-vs-Total-q-Diskrepanzen über mehrere Q-Vollanalysen, die §410 nicht ausreichend abdeckt.
- **Organisation-Capital als eigenständige Sub-Score-Achse** (Eisfeldt/Papanikolaou 2013, +4,6% p.a.) — `design-context`-Phase D-2 deferred. Trigger: V Q3 FY26 ROIC-Methodology-Verify (PIPELINE #21).
- **NBER „Intangible Value"-Strategy (Eisfeldt/Kim/Papanikolaou 2020)** — siehe [[Eisfeldt-Kim-Papanikolaou-2020-Intangible-Value]], Phase-D-2 active-deferred-D2 (per User-Direktive 2026-05-10 von D-3 SOURCE-ONLY hochgestuft, Cluster mit EP-2013 für Q3-2026-V-Trigger).

## Limitationen

- **PIM-Sensitivität:** Peters/Taylor verwenden Branch-spezifische R&D-Depreciation 10-30%; ±5pp ändert Total-q-Werte um ~5-15%. §410-Goodwill-Approach ist robuster (Goodwill ist hard-bilanziert), aber gröber.
- **Non-US-Übertragbarkeit:** IFRS R&D-Capitalization-Regeln (development phase aktivierbar, research phase nicht) unterscheiden sich von US-GAAP (Expense-Mehrheit). §410 ist neutral gegenüber dieser Unterschiedslage, weil es nur Goodwill (IFRS+GAAP einheitlich) entfernt; Total-q wäre Non-US-anpassungsbedürftig.
- **Acquisition-Vintage-Bias:** Goodwill aus 1990er-Akquisitionen reflektiert ökonomische Realität von 1990, nicht 2026. M&A-Compounder mit alten Goodwill-Stücken (BRK.B, IBM) haben strukturell höhere Goodwill-Reductions-Risiken — §410 ist robust gegen aktuelle FV-Tests, aber nicht prädiktiv gegen zukünftige Impairment-Risiken (siehe BRK.B KHC-OTTI-Watch PIPELINE #36 als Sonderfall).
- **Fortlaufende Methodik-Diskussion:** Das Total-q-Konzept war 2017 state-of-the-art; die in Peters/Taylor referenzierte alternative δ_SG&A=20%-Spezifikation (Falato/Kadyrzhanova/Sim 2013, FEDS Working Paper 2013-67) und die offene Frage zur Heterogenität von SG&A-Komponenten (Marketing-Flow vs. echte Capital-Investitionen) sind dokumentierte methodische Caveats. §410 ist robust gegen diese Methodik-Diskussion, weil es nur die Bilanz-Goodwill-Position adressiert, nicht die PIM-Konstruktion selbst.

## Operative Anwendung in DEFCON

1. **SKILL.md §410-Block trägt B29-Anker explizit** (eingeführt 2026-05-09 Phase D-1). Wissenschaftliche Begründung neben AVGO-30.04.-Kalibrierungs-Präzedenz.
2. **Tie-Break-Regel §410 vs Regel-4** (PIPELINE #30 Closure 09.05.) bleibt unverändert; B29 liefert die theoretische Begründung für die 40%-Goodwill-Asset-Schwelle.
3. **Confidence-Caveat bei Methodology-Drift** (StockAnalysis Hard-Ausschluss aus sources.md §7) bleibt unverändert; B29 verstärkt die Caveat-Logik — IC-Bereinigung ist algebraisch-theoretisch korrekt, aber Multi-Source-Konsistenz schützt vor Mess-Artefakten in der Goodwill-Klassifikation selbst.
4. **Anti-Pattern bestätigt:** P/B + EV/Book + Bilanz-multiple-basierte Bewertungen werden in DEFCON nicht verwendet — wäre genau die Tobin's-q-Verzerrung, die Peters/Taylor identifizieren.

## Backlinks

- [[Peters-Taylor-2017-Intangible-Capital]] — Primärquelle (B29, source-page)
- [[Wissenschaftliche-Fundierung-DEFCON]] — §Status-Matrix B29 `active-scoring-validation`
- [[Quality-Trap]] — DEFCON-Mechanik B6 (Wide-Moat × teure Bewertung)
- [[QMJ-Faktor]] — Buffetts-Alpha B5 Quality-Komponente
- [[FCF-Primacy]] — DEFCON-Block-Gewichtung 50/20/10/10/10
- [[Buffett-Faktorlogik]] — cheap+safe+quality theoretische Brücke
- [[Wolff-Echterling-2023]] — B8 ROIC-vs-WACC, theoretischer Unterbau via B29
- [[Buffetts-Alpha]] — B5 cheap+safe+quality (Float-Leverage nicht replizierbar; QMJ als operativer Pfad)
- [[DEFCON-System]] — Fundamentals-Block 50 Pt., §410-Verbindung
- [[AVGO]], [[MSFT]], [[V]], [[BRKB]] — Präzedenz-Anker §410-Anwendung (M&A-Compounder)

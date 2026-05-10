---
title: "Intangible Value"
date: 2020
type: source
subtype: academic-paper
medium: paper
tags: [defcon, intangible-value, hml-int, deferred-stub, fundamentals-block, design-context, phase-d-2]
url: https://www.nber.org/papers/w28056
venue: "NBER Working Paper No. 28056, November 2020"
authors: "Andrea L. Eisfeldt (UCLA Anderson), Edward Kim (UCLA PhD-Cand.), Dimitris Papanikolaou (Northwestern Kellogg)"
status: deferred-stub
triage_class: active-deferred-D2
raw_path: "raw/papers/Intangible Value.pdf"
defcon_relevanz: "Phase-D-2 deferred-Stub, von D-3 SOURCE-ONLY auf D-2 active-deferred hochgestuft (User-Direktive 2026-05-10). Trigger: V Q3 FY26 ~Juli 2026 (PIPELINE #21 ROIC-Methodology-Verify) — gemeinsam mit EP-2013 als Cluster-Aktivierung. Wissenschaftliche Härtung der DEFCON-P/B-De-Prio (Faktortabelle): EKP-2020 zeigt, dass ein Intangibles-augmented HML_INT-Faktor (Book-Equity erweitert um kumulierten intangible-Asset-Stock auf SG&A-Basis) Standard-Test-Assets besser preist als HML_FF, post-2007 besonders ausgeprägt."
sources: []
related:
  - "[[Eisfeldt-Papanikolaou-2013-Organization-Capital]]"
  - "[[Peters-Taylor-2017-Intangible-Capital]]"
  - "[[Crouzet-Eberly-Eisfeldt-Papanikolaou-2022-Economics-Intangible-Capital]]"
  - "[[Intangible-Adjusted-Value]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
  - "[[DEFCON-System]]"
  - "[[andrea-l-eisfeldt]]"
  - "[[edward-kim]]"
  - "[[dimitris-papanikolaou]]"
created: 2026-05-10
updated: 2026-05-10
aliases:
  - "Eisfeldt Kim Papanikolaou 2020"
  - "EKP 2020"
  - "Intangible Value"
  - "HML_INT"
---

# Eisfeldt, Kim & Papanikolaou (2020) — Intangible Value

> 🟡 **DEFERRED-STUB (Phase-D-2 active-deferred, hochgestuft von D-3):** Voll-PDF in `raw/papers/Intangible Value.pdf` vorhanden, Volltext-Read aufgeschoben bis V Q3 FY26 ~Juli 2026 (PIPELINE #21). Diese Stub-Page dokumentiert das HML_INT-Konstruktions-Skelett + DEFCON-Anknüpfungs-Plan; spezifische Magnituden (2,4% IRR-Alpha, Sharpe 0,40) sind aus Abstract zitiert, nicht aus Voll-Tabellen-Verifikation. **Hinweis:** Frühe Gemini-Triage attribuierte Authors fälschlich „Kuchler et al."; korrekt sind Eisfeldt/Kim/Papanikolaou.

## Abstract (eigene Worte, sekundär-zitiert)

Eisfeldt, Kim und Papanikolaou konstruieren einen **Intangibles-augmented Value-Faktor HML_INT**, indem sie zur klassischen Book-Equity-Komponente von HML_FF die kumulierte intangible-Asset-Stock-Größe (auf SG&A-Basis via PIM, analog EP-2013) addieren. Sortiert wird auf Intangibles-Adjusted-Book-to-Market statt klassisches Book-to-Market. Das Resultat ist ein Faktor, der **81% mit HML_FF korreliert** ist, aber **Standard-Test-Assets besser preist** und insbesondere **post-2007 robuste Performance** zeigt, während HML_FF in dieser Sub-Periode nicht-signifikant ist. Eine Long-HML_INT-/Short-HML_FF-Strategie liefert **2,4% IRR-Alpha + Sharpe 0,40**.

## Drei Kern-Befunde (für DEFCON-Aktivierung relevant)

1. **HML_INT preist Standard-Test-Assets besser als HML_FF.** Mainstream-Anomalien (Profitability, Investment, Operating-Cashflow) lassen sich durch HML_INT besser absorbieren — das ist starke Evidenz, dass Intangibles-Underrepresentation in Bilanz-Book-Equity ein systematisches Problem ist.

2. **Post-2007-Robustness.** HML_FF wird in der Sub-Periode 2007-2020 nicht-signifikant (Value-Premium-Decay-Debatte); HML_INT bleibt robust. Das ist die strukturell wichtigste Evidenz: Wenn klassisches Value durch Intangibles-Verzerrung zerlegt wird, sollte Intangibles-Adjusted-Value robust bleiben — genau das beobachten EKP.

3. **Long-HML_INT-/Short-HML_FF-Spread quantifiziert die Verzerrung.** 2,4% IRR-Alpha p.a. ist die monetäre Größenordnung der Bilanz-Capital-Fehlmessung im Value-Premium.

## DEFCON-Aktivierungs-Plan (deferred bis V Q3 FY26)

### Trigger-Bedingung

V Q3 FY26 ~Juli 2026 ROIC-Methodology-Verify (PIPELINE #21). Gemeinsame Aktivierung mit EP-2013 als Cluster (User-Direktive 2026-05-10).

### Bei Aktivierung zu klären

- DEFCON nutzt P/B explizit NICHT als Bewertungs-Multiple (siehe Faktortabelle.md, B29-Anti-Pattern). EKP-2020 würde diese De-Priorisierung wissenschaftlich härten — Intangibles-bereinigtes P/B wäre informativ, aber rohes P/B ist genau die EKP-2020-identifizierte Verzerrung.
- §28.1-Migration falls HML_INT als Sub-Score eingeführt werden soll: §29.4 t-Hurdle + §29.7 M&P-Discount-Faktor 0,42 anwenden auf 2,4%-Spread.
- Long-Only-Konversion: HML_INT ist Long-Short konstruiert — Long-Side-Beitrag zu schätzen vor Adoption (analog DHS-Long-Only-Caveat).
- Post-2007-Robustness ist starkes Argument, aber Sample-Endpunkt 2020 (NBER-WP); 2020-2026-OoS-Verify wäre zusätzlicher Pre-Adoption-Schritt.

### Anti-Pattern (NICHT bei Aktivierung)

- HML_INT-Argument als „rohes P/B-Multiple wieder rein" missverstehen — das wäre genau die Verzerrung, die EKP identifizieren.
- Adoption ohne Long-Only-Konversionsverlust-Quantifizierung.

## Beziehung zu anderen DEFCON-Layern

| Bezug | Layer | Anknüpfung |
|---|---|---|
| **B29 Peters/Taylor 2017** | Total-q-Framework | EKP-2020 ist die Faktor-Anwendung des Peters/Taylor-Total-q-Insights — gleicher Capital-Mess-Problem-Fix |
| **EP-2013** | OrgCap-Faktor | Author-Cluster-Folge-Paper; OC ist Komponente des Intangibles-Stocks in HML_INT-Konstruktion |
| **CEEP-2022** | JEP-Synthese | Konzeptionelle Synthese desselben Cluster-Frameworks (Non-Rivalry + Limited-Excludability) |
| **Quality-Trap (B6)** | Wide-Moat × teure Bewertung | EKP-2020 erklärt, warum P/B-basierte Bewertungs-Trap in Tech-Wide-Moats besonders falsch ist — DEFCON nutzt P/B nicht aus genau diesem Grund |
| **Faktortabelle.md** | DEFCON-Bewertungs-Multiple-Liste | EKP-2020 würde rohes P/B-De-Prio zementieren als wissenschaftlich gehärtetes Anti-Pattern |

## Limitationen (Abstract-Level)

- **Sample-Endpunkt 2020:** Post-Pandemic-Datapunkte fehlen; Robustness 2020-2026 nicht im Original validiert.
- **HML_INT 81%-Korrelation mit HML_FF:** Die meiste Variation ist gemeinsam — das macht den 19%-Residual-Driver-Spread interpretativ heikel.
- **PIM-Sensitivität:** Wie EP-2013 + Peters/Taylor — alle Intangibles-Stock-PIMs hängen an der δ-Spezifikation.

## Backlinks

- [[Eisfeldt-Papanikolaou-2013-Organization-Capital]] — Author-Cluster-Vorgänger
- [[Peters-Taylor-2017-Intangible-Capital]] — Total-q-Framework-Anker
- [[Crouzet-Eberly-Eisfeldt-Papanikolaou-2022-Economics-Intangible-Capital]] — JEP-Synthese desselben Cluster
- [[Intangible-Adjusted-Value]] — Concept-Anker (B29-Verbindung)
- [[Wissenschaftliche-Fundierung-DEFCON]] — Phase-D-2-deferred-Eintrag
- [[DEFCON-System]] — potenzieller Fundamentals-Block-Hardening-Pfad
- [[andrea-l-eisfeldt]], [[edward-kim]], [[dimitris-papanikolaou]] — Author-Entities

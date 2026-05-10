---
title: "Organization Capital and the Cross-Section of Expected Returns"
date: 2013
type: source
subtype: academic-paper
medium: paper
tags: [defcon, organization-capital, sga-capitalization, deferred-stub, fundamentals-block, design-context, phase-d-2]
url: https://onlinelibrary.wiley.com/doi/10.1111/jofi.12034
venue: "Journal of Finance Vol. 68 Nr. 4, 2013, S. 1365-1406 (SSRN 1359320)"
authors: "Andrea L. Eisfeldt (UCLA Anderson), Dimitris Papanikolaou (Northwestern Kellogg)"
status: deferred-stub
triage_class: active-deferred-D2
raw_path: "raw/papers/Organization Capital and the Cross-Section of.pdf"
defcon_relevanz: "Phase-D-2 deferred-Stub (Vault-Inventur 2026-05-10 Phase-D-1-Confidence-Upgrade-Pass). Trigger: V Q3 FY26 ~Juli 2026 (PIPELINE #21 ROIC-Methodology-Verify) — gemeinsam mit IV-2020-Cluster (User-Hochstufung von D-3 SOURCE-ONLY auf D-2 active-deferred). Falls dort SaaS/Service-Heavy-OrgCap-Lücke material wird, eigenständige §28.1-Migration-Session mit §29.4 t-Hurdle + §29.7 M&P-Discount."
sources: []
related:
  - "[[Peters-Taylor-2017-Intangible-Capital]]"
  - "[[Eisfeldt-Kim-Papanikolaou-2020-Intangible-Value]]"
  - "[[Crouzet-Eberly-Eisfeldt-Papanikolaou-2022-Economics-Intangible-Capital]]"
  - "[[Intangible-Adjusted-Value]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
  - "[[DEFCON-System]]"
  - "[[andrea-l-eisfeldt]]"
  - "[[dimitris-papanikolaou]]"
created: 2026-05-10
updated: 2026-05-10
aliases:
  - "Eisfeldt Papanikolaou 2013"
  - "EP 2013"
  - "Organization Capital and the Cross-Section of Expected Returns"
  - "Organization Capital JoF 2013"
---

# Eisfeldt & Papanikolaou (2013) — Organization Capital and the Cross-Section of Expected Returns

> 🟡 **DEFERRED-STUB (Phase-D-2 active-deferred):** Voll-PDF in `raw/papers/Organization Capital and the Cross-Section of.pdf` vorhanden, Volltext-Read aufgeschoben bis zum natürlichen Trigger V Q3 FY26 ~Juli 2026 (PIPELINE #21). Diese Stub-Page dokumentiert Befund-Skelett + DEFCON-Anknüpfungs-Plan für künftige Aktivierung; spezifische Magnituden sind aus Abstract + Intro zitiert, nicht aus Tabellen-Voll-Verifikation. Bei Aktivierung Phase-D-2: Voll-Read durchführen + Status auf `active-scoring-validation` oder `design-context` upgraden + ScoreRecord-Cross-Reference durch §28.1-Migration validieren.

## Abstract (eigene Worte, sekundär-zitiert)

Eisfeldt und Papanikolaou definieren **Organisation-Capital (OC)** als das produktionsrelevante Capital, das in Schlüsselpersonal, Routinen und Prozessen einer Firma akkumuliert ist — distinct von physischem PP&E und R&D-Capital. OC wird via Perpetual-Inventory-Method aus historischen SG&A-Investitionen aufgebaut (~30% δ analog Hulten/Hao 2008). Empirisches Hauptergebnis: Firmen mit High-OC-to-Capital-Ratio (O/K) outperformen Low-O/K-Firmen um **~4,6 Prozentpunkte p.a.** Das OMK-Long-Short-Portfolio liefert Sharpe-Ratios in der Größenordnung des Markt-Sharpe und bleibt unkorreliert mit FF-3- und Carhart-4-Faktoren.

## Drei Kern-Befunde (für DEFCON-Aktivierung relevant)

1. **OC ist quantitativ messbar via SG&A-PIM.** Die OC-zu-Total-Capital-Ratio (O/K) ist eine cross-sectional aussagekräftige Variable. Tech/Healthcare/Service-Heavy-Sektoren haben strukturell höhere O/K-Werte; Manufacturing/Consumer-Heavy niedriger.

2. **High-O/K-Firmen verdienen positive Risikoprämien.** Long-Short-Portfolio-Spread ~4,6% p.a., over-and-above FF-Carhart-Faktoren — das spricht für eine eigenständige Risiko-/Mispricing-Quelle.

3. **OC-Dynamik korreliert mit Frontier-Productivity-Shocks.** Theoretisches Modell: OC ist embodied in Schlüsselpersonal, das mobil ist; technologische Frontier-Schocks erhöhen die OC-Mobilität-Risiken → systematische Risikoprämie.

## DEFCON-Aktivierungs-Plan (deferred bis V Q3 FY26)

### Trigger-Bedingung

V Q3 FY26 ~Juli 2026 ROIC-Methodology-Verify (PIPELINE #21): Falls defeatbeta-ROIC-Wert weiterhin von Standard-NOPAT/IC-Berechnungen abweicht UND der Verdacht entsteht, dass eine OC-bereinigte Capital-Basis die Diskrepanz erklärt → Phase-D-2-Aktivierung.

### Bei Aktivierung zu klären

- Migrations-Pfad als eigenständiger Sub-Score (Long-Only-konvertiert) vs. als Confidence-Modifier auf existierende ROIC-Variante
- §29.4 t-Hurdle (≥ 3,0 t-Stat post-M&P-Discount-Faktor 0,42) — bei +4,6% p.a. mit ~30 Jahre US-Compustat sollten t-Stats den Hurdle passieren, aber Re-Verifikation Pflicht
- §29.7 M&P-Discount sicher anwenden auf Magnitude
- Long-Only-Konversionsverlust quantifizieren (Long-Side allein typischerweise nur ~50-60% des Faktor-Returns — analog DHS-Caveat)
- Sample-Periode-Decay: Original-Sample 1970-2008 — kein Post-GFC-Datenpunkt im Original-Paper; Replikations-Empirie 2008-2024 prüfen

### Anti-Pattern (NICHT bei Aktivierung)

- Naive O/K-Ratio als zusätzliches Score-Element ohne §28.1-Migration → §27.1 Double-Counting mit existierender ROIC + FCF-Yield
- O/K als Quality-Modifier ohne Long-Only-Validierung → analog DHS-Long-Short-Trap

## Beziehung zu anderen DEFCON-Layern

| Bezug | Layer | Anknüpfung |
|---|---|---|
| **B29 Peters/Taylor 2017** | Total-q-Framework (`active-scoring-validation`) | OC ist die größere Komponente von Intangibles in Peters/Taylor (76% vs Knowledge-Cap 24%); EP-2013 ist die methodische Vorlage für die SG&A-PIM-Konstruktion |
| **B25 McLean/Pontiff 2016** | Post-Publication-Decay-Konvention | Discount-Faktor 0,42 anzuwenden bei Magnituden-Zitaten |
| **B26 Lakonishok/Lee 2001** | Insider-Buy>Sell | Indirekt: Insider sind Schlüsselpersonal, das OC trägt — Insider-Aktivität kann OC-Mobilität-Signal sein (Sekundär-Hypothese) |
| **Quality-Trap (B6)** | Wide-Moat × teure Bewertung | OC-bereinigte Capital-Basis könnte „teure" P/B-Multiples partiell als Mess-Artefakt erklären (analog Total-q-Logik) |

## Limitationen (Abstract-Level)

- **SG&A-Brittleness:** Wie bei Peters/Taylor diskutiert, enthält SG&A Non-Capital-Komponenten (Marketing-Flow, normale Verwaltung); 30%-Capitalization-Rate behandelt diese Heterogenität nicht.
- **Sample-Periode 1970-2008:** kein Post-GFC-Datenpunkt; Decay-Risiken nicht im Original validiert.
- **Risk-vs-Mispricing:** Eisfeldt/Papanikolaou präsentieren beide Interpretationen; die Theorie-Debatte (rational risk premium vs. behavioral mispricing) ist für DEFCON-Operationalisierung sekundär.

## Backlinks

- [[Peters-Taylor-2017-Intangible-Capital]] — methodische Vorlage SG&A-PIM
- [[Eisfeldt-Kim-Papanikolaou-2020-Intangible-Value]] — Folge-Paper im selben Author-Cluster
- [[Crouzet-Eberly-Eisfeldt-Papanikolaou-2022-Economics-Intangible-Capital]] — JEP-Synthese desselben Cluster-Frameworks
- [[Intangible-Adjusted-Value]] — Concept-Anker (B29-Verbindung)
- [[Wissenschaftliche-Fundierung-DEFCON]] — Status-Matrix Phase-D-2-deferred-Eintrag
- [[DEFCON-System]] — potenzieller Fundamentals-Block-Erweiterungs-Pfad
- [[andrea-l-eisfeldt]], [[dimitris-papanikolaou]] — Author-Entities

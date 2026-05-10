---
title: "Which Alpha?"
date: 2015
type: source
subtype: academic-paper
medium: paper
tags: [defcon, asset-pricing-modellvergleich, meta-gate, deferred-stub, retrospective-gate, phase-d-2]
url: https://www.nber.org/papers/w21698
venue: "NBER Working Paper No. 21698, November 2015 (später Review of Financial Studies Vol. 30 Nr. 4, 2017, S. 1316-1338)"
authors: "Francisco Barillas (Emory Goizueta), Jay Shanken (Emory Goizueta + NBER)"
status: deferred-stub
triage_class: meta-gate-deferred-D2
raw_path: "raw/papers/Barillas & Shanken (2015).pdf"
defcon_relevanz: "Phase-D-2 deferred-Stub (Vault-Inventur 2026-05-10). Trigger: 2028-Review-Gate ODER nächste DEFCON-Block-Re-Gewichtung (z.B. wenn ein neuer Block vorgeschlagen wird — DHS-B30-Frage zur formalen FIN-Sub-Score-Migration wäre erster Live-Test). **Meta-Gate**-Funktion: methodisch schärfere Alternative zum AAFM-t-Stat-Anker (§29.4) bei Modellvergleich mit getradeten Faktoren — Test-Asset-Alpha-Wettbewerbe sind nach Barillas/Shanken redundant. Komplementär zu §29.4 t-Hurdle, ergänzt um die Frage „Welcher Block spannt welche andere Block-Strategien?"."
sources: []
related:
  - "[[Daniel-Hirshleifer-Sun-2020-Behavioural-Factors]]"
  - "[[Wolff-Echterling-2023]]"
  - "[[Hou-Xue-Zhang-2015-q-Factor]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
  - "[[RETROSPECTIVE-GATE]]"
  - "[[DEFCON-System]]"
  - "[[francisco-barillas]]"
  - "[[jay-shanken]]"
created: 2026-05-10
updated: 2026-05-10
aliases:
  - "Barillas Shanken 2015"
  - "BS 2015"
  - "Which Alpha"
  - "Which Alpha NBER"
  - "Barillas-Shanken-2017"
---

# Barillas & Shanken (2015) — Which Alpha?

> 🟡 **DEFERRED-STUB (Phase-D-2 meta-gate-deferred):** Voll-PDF in `raw/papers/Barillas & Shanken (2015).pdf` vorhanden, Volltext-Read aufgeschoben bis 2028-Review-Gate ODER bei nächster DEFCON-Block-Re-Gewichtung. Diese Stub-Page dokumentiert das methodische Argument als künftigen Meta-Gate-Anker; Magnituden + Beweis-Skizze sind aus Abstract + Standard-Sekundärliteratur zitiert, nicht aus Voll-Tabellen-Verifikation. Bei Aktivierung: §29.4-Block der INSTRUKTIONEN.md erweitern um Barillas/Shanken-Modellvergleichs-Logik.

## Abstract (eigene Worte, sekundär-zitiert)

Barillas und Shanken stellen die Frage, wie Asset-Pricing-Modelle korrekt verglichen werden, wenn beide Modelle ausschließlich aus **getradeten Faktoren** bestehen (im Gegensatz zu nicht-getradeten makroökonomischen Faktoren). Ihr Hauptbefund: Bei Modellvergleichen unter dieser Bedingung ist der **Test-Asset-Alpha-Wettbewerb irrelevant** — egal welche Test-Assets man wählt (FF-25 Size/BM-Portfolios, Industry-Portfolios, Anomalie-Decile-Portfolios), die Modellvergleichs-Antwort bleibt identisch. Was zählt, ist nur die Frage: „Wie gut preist Modell A die in Modell B excluded Faktoren?" und vice versa. Konsequenz: Die in der Literatur übliche Praxis, Modelle nach ihrer Test-Asset-Alpha-Spanning-Performance zu ranken, ist methodisch redundant.

## Kern-Argument

1. **Spanning-Test ist Dual-Form des Test-Asset-Tests bei traded factors.** Wenn Faktor F_A in Modell B's Spanning-Test ein signifikantes Alpha aufweist, ist F_A informationstragend gegenüber Modell B; Test-Assets sind redundant.

2. **Test-Asset-Wahl ist konventionell, nicht methodisch.** Verschiedene Test-Assets liefern dieselbe Modellrangfolge → die Wahl ist Stilfrage, nicht Wissenschaftsfrage.

3. **Bayesian-Aggregation (Folge-Paper 2018 JoF):** Im 2017 RFS-Folgepaper erweitern Barillas/Shanken die Logik auf Bayesian-Posterior-Probabilities über Modell-Klassen — relevant für Multi-Modell-Ensemble-Designs (außerhalb DEFCON-v3.7-Scope, aber Future-Reference).

## DEFCON-Meta-Gate-Funktion (deferred)

### Aktivierungs-Trigger

- **2028-Review-Gate** (planmäßig)
- **Block-Re-Gewichtung-Vorschlag** (z.B. neuer Sub-Score-Block-Vorschlag wie FIN aus DHS-B30, OrgCap aus EP-2013, Intangible-Value aus EKP-2020)
- Jeder Vorschlag, der existierende Block-Gewichtungen 50/20/10/10/10 verändert

### Bei Aktivierung zu klären

- Aktuelle DEFCON-Block-Konstruktion ist NICHT formell Faktor-Modell — sie ist Long-Only-Score-Aggregation. Barillas/Shanken-Logik gilt strict bei traded-factor-Modellvergleichen; Übertragung auf DEFCON erfordert Modell-Mapping.
- Das Mapping: Wenn ein neuer Block N als „erweitert DEFCON's Spanning-Performance gegenüber Anomalien-Cluster X" begründet wird, dann ist die methodisch saubere Frage: Spannt N den Cluster, den die existierenden Blöcke nicht spannen? — also Anti-Inkrementalismus-Argument vs. naive Hinzufügung.
- Komplementär zu §29.4 (t-Hurdle ≥ 3,0): Barillas/Shanken adressiert Block-Span-Frage, §29.4 adressiert Magnitude-Robustness; beide nötig, nicht ersetzend.

### Anti-Pattern (NICHT bei Aktivierung)

- Test-Assets ad-hoc auswählen, um gewünschten Block-Vorschlag durchzubringen — genau die Praxis, die Barillas/Shanken als methodisch redundant identifizieren.
- Naive Anwendung auf Long-Only-Score-System ohne Modell-Mapping — würde Theorie-Anwendungs-Drift produzieren.

## Beziehung zu anderen DEFCON-Layern

| Bezug | Anknüpfung |
|---|---|
| **§29.4 t-Hurdle (AAFM)** | komplementär: Barillas/Shanken adressiert Span-Frage, §29.4 Magnitude-Robustness |
| **B30 Daniel/Hirshleifer/Sun 2020** | DHS-Paper nutzt 34-Anomalien-Spanning-Test; bei FIN-Sub-Score-Migration ist Barillas/Shanken-Logik der formal-saubere Pfad zur Frage „Erweitert FIN DEFCON?" |
| **B7 Wolff/Echterling 2023** | ROIC-vs-WACC ist im B7-Paper als Top-Prädiktor identifiziert — Barillas/Shanken-Logik würde fragen: Spannt ROIC-vs-WACC die anderen DEFCON-Sub-Scores oder umgekehrt? |
| **B13 Novy-Marx 2013** | GP/TA `design-rejected` (§27.1 Double-Counting) — Barillas/Shanken hätte die Spanning-Frage formal beantworten können vor dem Reject |
| **RETROSPECTIVE-GATE §29** | Barillas/Shanken-Logik gehört in §29.4-Erweiterung bei Aktivierung |

## Limitationen

- **Gilt nur für getradete Faktoren** — DEFCON-Sub-Scores sind nicht 1:1 mit getradeten Faktoren mappbar; Theorie-Anwendung erfordert sorgfältige Übersetzung.
- **2015-WP-Version vs. 2017-RFS-Version:** Bayesian-Aggregation ist nur in der 2017-RFS-Variante voll entwickelt; vorliegende WP-PDF deckt das Argument vermutlich noch knapper ab.
- **Frequentistisch-Theorie-Cluster:** Barillas/Shanken sind in der Likelihood-Ratio-Test-Tradition; konkurrierende Bayesian-Frameworks (Harvey/Liu/Zhu 2016) liefern alternative Modellvergleichs-Logiken.

## Backlinks

- [[Daniel-Hirshleifer-Sun-2020-Behavioural-Factors]] — DHS-Modell ist erster Live-Test-Kandidat für Barillas/Shanken-Logik
- [[Wolff-Echterling-2023]] — ROIC-vs-WACC-Top-Prädiktor-Befund, Spanning-Frage offen
- [[Hou-Xue-Zhang-2015-q-Factor]] — q-Factor-Konkurrent zu FF-5, Barillas/Shanken-Vergleichs-Anwendung
- [[Wissenschaftliche-Fundierung-DEFCON]] — Phase-D-2 meta-gate-deferred-Eintrag
- [[RETROSPECTIVE-GATE]] — §29-Erweiterungs-Anker bei Aktivierung
- [[DEFCON-System]] — Block-Re-Gewichtungs-Trigger-Bedingung
- [[francisco-barillas]], [[jay-shanken]] — Author-Entities

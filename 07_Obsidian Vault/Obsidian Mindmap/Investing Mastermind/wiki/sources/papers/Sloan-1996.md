---
title: "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?"
date: 1996
type: source
subtype: academic-paper
tags: [defcon, accruals, earnings-quality, sloan, fundamentals, cash-flow]
url: https://www.jstor.org/stable/248290
authors: "Richard G. Sloan (University of Pennsylvania, The Accounting Review 71(3))"
status: processed
defcon_relevanz: "Fundamentals — Grundlagenpaper für Accrual Ratio. Low-Accrual-Firmen outperformen High-Accrual um +10,4% p.a. Validiert bestehende Accrual-Schwellen (<5% / >10%) wissenschaftlich (Befund B14)."
related: "[[Accruals-Anomalie-Sloan]], [[F-Score-Quality-Signal]], [[FCF-Primacy]], [[DEFCON-System]], [[Wissenschaftliche-Fundierung-DEFCON]], [[Gross-Profitability-Premium]]"
---

# Sloan: Accruals Anomaly (1996)

## Abstract (eigene Worte)
Richard Sloan zeigt, dass Aktienmärkte Cash-Earnings und Accrual-Earnings nicht korrekt gewichten: Investoren behandeln beide Komponenten des Net Income gleich, obwohl Accruals **deutlich weniger persistent** sind als Cash Flows. Folge: Firmen mit hohen Accruals sind systematisch überbewertet (künftige Earnings enttäuschen), Firmen mit niedrigen Accruals sind unterbewertet. Ein Long-Short-Portfolio (kaufe Low-Accrual, shorte High-Accrual) erzielt **+10,4% jährliche Überrendite**. Dies ist das **Gründungspaper der Accrual-Anomalie** und die empirische Basis für alle Earnings-Quality-Metriken, einschließlich unserer aktuellen Accrual Ratio.

## Kern-Formel

```
Accruals = Net Income − Operating Cash Flow
Accrual Ratio = Accruals / Total Assets (5-Jahres-Durchschnitt oder TTM)
```

**Interpretation:**
- **Positive Accruals:** Net Income > OCF → Gewinn wird durch nicht-cash-wirksame Buchungen (Forderungen, Lagerbestand, Abschreibungen) aufgebläht
- **Negative Accruals:** OCF > Net Income → Cash-Earnings stärker als ausgewiesener Gewinn → konservative Rechnungslegung

## Key Findings (DEFCON-gemappt)

- **Top-Dezil Accruals unterperformt Bottom-Dezil um +10,4% p.a.** — robust über 30+ Jahre
- **Anomalie persistiert** trotz Bekanntheit seit 1996 — Investoren korrigieren systematisch zu langsam
- **Quality > Quantity:** Ein niedriger aber „echter" Gewinn (OCF-getrieben) schlägt hohe aber „künstliche" Gewinne (Accrual-getrieben)
- **Validierung unserer Schwellen:**
  - Sloan-High-Accrual-Dezil: Accrual Ratio typisch > 10% → matches unser >10% = -2 Pt. Malus
  - Sloan-Low-Accrual-Dezil: Accrual Ratio typisch < 5% → matches unser <5% = kein Abzug

## Verbindung zu Piotroski

Sloan (1996) und [[Piotroski-2000]] sind komplementär:
- **Sloan:** definiert Accrual-Anomalie als Renditefaktor (statistisch)
- **Piotroski:** operationalisiert Anti-Accrual als F-Score-Kriterium #4 („OCF > NI")

Piotroski-Kriterium #4 ist im Kern ein **binärisierter Sloan-Test**. Unsere Accrual Ratio ist die **kontinuierliche Version** davon.

## DEFCON-Implikation

| Block | Aktuelle Behandlung | Nach B14 (Status quo validiert) |
|-------|--------------------|----------------------------------|
| Fundamentals (50 Pt.) | Accrual Ratio Malus: <5% kein / 5–10% -1 / >10% -2 | Unverändert — wissenschaftlich korrekt kalibriert |
| Bonus (optional, v3.6) | Nicht vergeben | Erweiterung: <3% = +2 Bonus (vgl. Piotroski #4 positiv) |

> **Operative Schlussfolgerung:** Sloan liefert kein neues Scoring-Regel, sondern **wissenschaftliche Rückendeckung für unsere bestehende Accrual Ratio**. Der neue Wert liegt in Audit-Stärke und Begründungstiefe — nicht in neuer Logik.

## Kalibrierung (live)

| Ticker | Accrual Ratio TTM | Sloan-Dezil | DEFCON-Effekt |
|--------|-------------------|-------------|----------------|
| AVGO | ~2% | Bottom (good) | kein Abzug |
| V | ~1% | Bottom (good) | kein Abzug |
| COST | ~3% | Bottom (good) | kein Abzug |
| MSFT | ~6% | Middle | -1 Pt. |
| TMO | ~9% | Upper-middle | -1 Pt. |
| APH | ~8% | Middle | -1 Pt. |

(Werte aus Erinnerung; bei v3.6-Implementierung formell neu berechnen)

## Backlinks
- [[Accruals-Anomalie-Sloan]] — operative Konzeptseite
- [[Piotroski-2000]] — komplementäre Quality-Operationalisierung (F-Score #4)
- [[FCF-Primacy]] — OCF > Net Income als Cash-Primacy
- [[Gross-Profitability-Premium]] — parallele Fundamentals-Anomalie
- [[DEFCON-System]] — Accrual Ratio bleibt als Malus, wissenschaftlich fundiert
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B14

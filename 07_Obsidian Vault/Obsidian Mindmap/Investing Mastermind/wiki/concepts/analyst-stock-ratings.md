---
title: "Analyst Stock Ratings"
type: concept
tags: [aktienanalyse, analyst, wall-street, rating, investment-banking]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [llm-stock-rating, forward-returns-evaluation, financial-fundamentals-analysis, sp-500, ai-in-investment-analysis]
aliases:
  - "Analyst Stock Ratings"

---

# Analyst Stock Ratings

Empfehlungen von professionellen Wertpapieranalysten (meist bei Investmentbanken und Brokerhäusern), die Investoren bei Kauf-, Halte- und Verkaufsentscheidungen unterstützen sollen. Sie sind eine der ältesten und meistgenutzten Informationsquellen im Finanzmarkt — und gleichzeitig eine, die systematische Schwächen aufweist.

## Standard-Rating-Skala (5-stufig)

| Rating | Synonyme | Bedeutung |
|---|---|---|
| Strong Buy | Buy | Deutliche Outperformance erwartet |
| Moderate Buy | Outperform, Overweight | Leichte Outperformance erwartet |
| Hold | Neutral, Market Perform | Marktperformance erwartet |
| Moderate Sell | Underperform, Underweight | Leichte Underperformance erwartet |
| Strong Sell | Sell | Deutliche Underperformance erwartet |

*Terminologie variiert zwischen Institutionen — manche nutzen 1–5 Skalen, andere proprietäre Systeme.*

## Typischer Analyst-Prozess

1. **Fundamentalanalyse:** Bilanz, GuV, Cashflow, Kennzahlen
2. **Technische Analyse:** Kursmuster, Handelsvolumen
3. **Qualitative Faktoren:** Management-Qualität, Wettbewerbsposition, Markttrends
4. **Earnings Calls & Management-Gespräche:** Direkte Einschätzungen
5. **Modellierung:** DCF-Bewertung, Peer-Vergleich
6. **Veröffentlichung:** nach Quartalsergebnissen, bei signifikanten Ereignissen

## Bewiesene Schwächen (aus Forschung)

### 1. Massiver Positivitäts-Bias
Aus [[LLMs for Equity Stock Ratings]]:
- **43% Strong Buy**, 34% Moderate Buy, 16% Hold, 4% Moderate Sell, 1% Strong Sell
- Weniger als 5% aller Ratings sind Verkaufsempfehlungen
- Grund: kommerzielle Abhängigkeiten (Investmentbanking-Gebühren, Unternehmensbeziehungen)

### 2. Interessenkonflikte
- Analysten bei Investmentbanken haben incentives, positive Ratings zu vergeben
- Unternehmen mit Investment-Banking-Mandaten erhalten tendenziell bessere Ratings
- Regulierung (seit 2003) hat verbessert aber nicht eliminiert

### 3. Datenverzögerung
- Ratings werden meist reaktiv (nach Quartalsberichten) aktualisiert
- Verpasst Marktbewegungen zwischen Veröffentlichungen
- Durchschnittlich 75.9% der Ratings werden "maintained" (unverändert beibehalten)

### 4. Überlegenheit durch LLMs (mittelfristig)
LLM-Modelle schlagen Analysten-Ratings bei 3-, 6- und 12-Monats-Horizonten (MAE: Analyst 1.570 vs. Fundamentals+Sentiment 1.417)

## Stärken von Analysten

- **Langfristig (>12 Monate):** Analysten performen besser als LLMs
- **Qualitative Einschätzungen:** Management-Qualität, Wettbewerbsdynamik, regulatorische Risiken
- **Earnings-Call-Nuancen:** Tonalität, Körpersprache, Ausweichen bei kritischen Fragen
- **Branchen-Expertise:** Deep Domain Knowledge in spezifischen Sektoren
- **Netzwerkeffekte:** Direktzugang zu Unternehmensführung

## Nutzung von Analysten-Ratings in der Praxis

### Was nützlich ist
- **Konsensus-Rating** (Durchschnitt vieler Analysten): weniger biased als Einzelmeinungen
- **Rating-Änderungen:** Upgrades/Downgrades signalisieren Informationswert
- **Target-Price-Konsensus:** Als Bewertungsanker, nicht als absolute Wahrheit

### Was kritisch zu betrachten ist
- Einzelne Buy-Empfehlungen von der anbietenden Bank
- Ratings kurz vor großen Deals (IPO, M&A)
- Rating-Cluster: wenn alle gleichzeitig upgraden, ist der Markt oft schon gelaufen

### Datenquellen
- Bloomberg Terminal
- FactSet
- TipRanks (Analyst-Performance-Tracking)
- Seeking Alpha

## Marktreaktionen auf Ratings

Forschung zeigt:
- Signifikante Kursreaktionen auf Rating-Revisionen (besonders Downgrades)
- US-Markt zeigt die größten Reaktionen unter G7-Ländern
- Abnormale Returns für Strategien basierend auf Analyst-Empfehlungen (polnischer Markt: statistisch signifikant)

## Relevanz für eigene Strategie

> Analysten-Ratings sind **ein Signal unter vielen** — nicht das führende. Sinnvolle Nutzung:
> - Konsensus-Änderungen tracken (nicht absolute Werte)
> - Für Long-Term (>12M) Horizonte stärker gewichten
> - Immer auf Positivitäts-Bias adjustieren
> - LLM-eigene Analyse als unabhängigen Check verwenden

## Verbundene Seiten

- [[LLMs for Equity Stock Ratings]] · [[LLM-Based Stock Rating]] · [[Forward Returns Evaluation]]
- [[Financial Fundamentals Analysis]] · [[S&P 500]] · [[AI in Investment Analysis]]

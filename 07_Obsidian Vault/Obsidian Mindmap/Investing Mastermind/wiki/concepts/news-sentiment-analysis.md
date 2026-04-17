---
title: "News Sentiment Analysis"
type: concept
tags: [sentiment, news, nlp, aktienanalyse, ki-methodik]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings, Jadhav-Mirza-2025]
related: [llm-stock-rating, financial-fundamentals-analysis, chain-of-thought-prompting, ai-in-investment-analysis, Wissenschaftliche-Fundierung-DEFCON]
---

# News Sentiment Analysis

Die automatisierte Bewertung der Stimmung (positiv/negativ/neutral) von Finanznachrichten, Unternehmensberichten und Marktkommentaren — entweder als Textklassifikation oder als numerischer Score. Im LLM-Kontext dient sie als komprimierter Marktinformations-Input für Prognosemodelle.

## Grundkonzept

Finanznachrichten enthalten Informationen, die kurzfristig die Aktienkurse bewegen. Sentiment-Analyse extrahiert das Signal (positiv/negativ) und gibt es dem Modell in strukturierter Form.

## Zwei Ansätze im Vergleich

### Ansatz 1: Volltext-Zusammenfassungen (News Summary)
- GPT-4 fasst alle Nachrichten eines Monats für Unternehmen und Sektor zusammen
- Detaillierte, kontextreiche Information
- Hoher Token-Verbrauch im LLM-Kontext

### Ansatz 2: Sentiment-Score (numerisch)
- GPT-4 bewertet die Zusammenfassungen auf einer Skala −5 bis +5
- **Firmen-Score:** Sentiment der unternehmensspecifischen News
- **Sektor-Score:** Sentiment der Branchenentwicklung
- Kompakter: zwei Zahlen statt langer Texte

## Ergebnis aus [[LLMs for Equity Stock Ratings]]

**Kein signifikanter Unterschied** zwischen Volltext und Score-Methode bei mittleren und langen Horizonten. Für die Praxis: **Sentiment-Scores sind gleichwertig und deutlich effizienter.**

| Methode | Return MAE | Token-Verbrauch |
|---|---|---|
| News Summary | 1.491 | Hoch |
| Sentiment Score | 1.496 | Niedrig |
| Vanilla (ohne News) | 1.447 | Niedrig |

**Wichtige Erkenntnis:** Beide News-Methoden schneiden *schlechter* als Vanilla (ohne News) ab bei mittleren Horizonten. News erhöhen kurzfristig die Genauigkeit (1 Monat), schaden aber ab 3 Monate durch **Positivity Bias**.

## Positivity Bias — das Kernproblem

News-Sentiment korreliert stark mit LLM-Ratings (Spearman ~0.44 bei 1-Monats-Horizont für Firmennews). Das Modell übernimmt die positive/negative Stimmung der News direkt in seine Prognosen, statt sie kritisch einzuordnen.

**Folge:** Mehr positive News → mehr Buy-Ratings → weniger akkurate mittelfristige Prognosen, weil gute aktuelle News nicht zwingend gute zukünftige Performance bedeutet.

## Praktische Empfehlungen

1. **Kurzfrist-Analyse (1 Monat):** News-Zusammenfassungen sinnvoll, geben aktuellen Kontext
2. **Mittelfrist-Analyse (3–12 Monate):** News weglassen oder nur Sentiment-Score verwenden
3. **Immer:** Sektor-Sentiment getrennt von Firmen-Sentiment betrachten
4. **Bias-Kontrolle:** LLM explizit anweisen, Sentiment-Scores als *einen Faktor unter vielen* zu gewichten

## Datenquellen für Sentiment

- News-APIs: Benzinga, Seeking Alpha, Reuters, Bloomberg
- Social Media (Reddit/WallStreetBets) — höheres Rauschen
- Earnings-Call-Transkripte (Managementton) — qualitativ wertvoll
- Analyst-Reports-Tonalität

## Named Entity Recognition (NER) für News-Filterung

Bevor Sentiment berechnet wird, müssen irrelevante Artikel gefiltert werden. NER identifiziert, ob ein Artikel wirklich über das gesuchte Unternehmen berichtet (inkl. Aliases, Tochtergesellschaften).

## Verbundene Seiten

- [[LLMs for Equity Stock Ratings]] · [[LLM-Based Stock Rating]] · [[Financial Fundamentals Analysis]]
- [[Chain-of-Thought Prompting]] · [[AI in Investment Analysis]]
- [[Jadhav-Mirza-2025]] — 84-Paper Meta-Survey bestätigt Positivity-Bias (B11)
- [[Wissenschaftliche-Fundierung-DEFCON]] — B11: Sentiment-Cap 10 Pt. wissenschaftlich begründet

---
title: "LLM-Based Stock Rating"
type: concept
tags: [llm, stock-rating, aktienanalyse, ki-prognose, financial-ai]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [financial-fundamentals-analysis, chain-of-thought-prompting, news-sentiment-analysis, forward-returns-evaluation, analyst-stock-ratings, gpt-4, ai-in-investment-analysis, defcon-system, analyse-pipeline, dynastie-depot-skill]
aliases:
  - "LLM-Based Stock Rating"

---

# LLM-Based Stock Rating

Die Verwendung von Large Language Models (LLMs) zur automatisierten Generierung von Aktien-Ratings (Buy/Hold/Sell und Abstufungen) auf Basis multimodaler Finanzdaten — ohne Fine-Tuning, allein durch gezieltes Prompting.

## Grundidee

Ein LLM übernimmt die Rolle eines Financial Analysts und verarbeitet dieselben Daten, die ein menschlicher Analyst berücksichtigen würde:
- Fundamentaldaten aus Unternehmensberichten
- Technische Indikatoren & Kursentwicklung
- Nachrichten & Marktstimmung

Der entscheidende Unterschied: Ein LLM kann hunderte Unternehmen **gleichzeitig, konsistent und kostengünstig** bewerten.

## Rating-Skala (Standard 5-stufig)

| Wert | Bezeichnung | Bedeutung |
|---|---|---|
| +2 | Strong Buy | Deutliche Outperformance erwartet |
| +1 | Moderate Buy / Outperform | Leichte Outperformance erwartet |
| 0 | Hold | Markt-Performance erwartet |
| −1 | Moderate Sell / Underperform | Leichte Underperformance erwartet |
| −2 | Strong Sell | Deutliche Underperformance erwartet |

## Bewiesene Vorteile gegenüber menschlichen Analysten

Aus [[LLMs for Equity Stock Ratings]] (J.P. Morgan, 2024):
1. **Geringerer MAE** bei 3-, 6- und 12-Monats-Prognosen (Vanilla: 1.447 vs. Analyst: 1.570)
2. **Kein Positivitäts-Bias:** Analysten vergeben 43% Strong Buy, LLMs verteilen gleichmäßiger
3. **Konsistenz:** Gleiche Methodik für alle Unternehmen, keine persönlichen Interessenkonflikte
4. **Skalierbarkeit:** Gesamtes S&P-500-Universum monatlich in einem Durchgang

## Beste Datenkombination (Stand 2024)

**Fundamentals + Sentiment-Score** (MAE 1.417) > Nur Fundamentals (1.421) > Vanilla (1.447) > News/Sentiment (1.491/1.496) > Analysten (1.570)

## Grenzen

- Kurzfristig (< 12 Monate) besser als Analysten, langfristig (> 12 Monate) schlechter
- Keine Verarbeitung von Earnings Calls, Managementgesprächen, qualitativen Einschätzungen
- Kontext-Limits der Modelle begrenzen Datenmenge pro Abfrage
- News-Daten induzieren Positivitäts-Bias → sparsam einsetzen

## Technische Umsetzung (Best Practices aus Forschung)

1. System-Prompt: Analyst-Persona + explizite Rating-Skala mit Definitionen
2. [[Chain-of-Thought Prompting]]: erst begründen, dann raten
3. Few-Shot Beispiel im Kontext
4. HTML-Format für tabellarische Daten (Fundamentals)
5. CoVE (Chain of Verification) für Datumsprüfung
6. [[News Sentiment Analysis|Sentiment-Scores]] statt Volltext-News (gleiche Performance, weniger Token)

## Offene Forschungsfragen

- Performance mit neueren Modellen (GPT-4o, Claude 3.5+, Gemini Ultra)
- Integration von Earnings-Call-Transkripten
- Anwendung auf Small/Mid-Caps und internationale Märkte
- Kombination mit klassischen Quant-Modellen

## Umsetzung im Dynastie-Depot

Die JPM-Forschungsergebnisse zu LLM-Stock-Rating sind direkt in das [[DEFCON-System]] eingeflossen:

| Forschungsergebnis | DEFCON-Umsetzung |
|---|---|
| Fundamentals = stärkste Modalität (MAE 1.421) | Fundamentals-Block = 50 von 100 Punkten |
| Kein Positivitäts-Bias bei LLMs | Analyst-Konsensus nur 10 Pt. (Sentiment-Block) |
| CoT erhöht Qualität & Interpretierbarkeit | !Analysiere folgt Begründung-vor-Score-Prinzip |
| Quintil-Bewertung nach Forward Returns | DEFCON-Schwellen (≥80/65/50/<50) analog zu Quintilen |

Operative Integration über die [[Analyse-Pipeline]]: LLM-gestützte Tiefen­analyse in Stufe 2 (!Analysiere), Stufe 0 als schneller Vorfilter.

## Verbundene Seiten

- [[LLMs for Equity Stock Ratings]] (Quelle) · [[Analyst Stock Ratings]] (Vergleich)
- [[Financial Fundamentals Analysis]] · [[Chain-of-Thought Prompting]] · [[News Sentiment Analysis]]
- [[Forward Returns Evaluation]] · [[GPT-4]] · [[AI in Investment Analysis]]
- [[DEFCON-System]] · [[Analyse-Pipeline]] · [[dynastie-depot-skill]]

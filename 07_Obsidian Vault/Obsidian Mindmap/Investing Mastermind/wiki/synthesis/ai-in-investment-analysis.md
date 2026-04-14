---
title: "AI in Investment Analysis"
type: synthesis
tags: [ki, investment, aktienanalyse, depot-strategie, synthese, trading, llm]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [llm-stock-rating, financial-fundamentals-analysis, analyst-stock-ratings, chain-of-thought-prompting, news-sentiment-analysis, forward-returns-evaluation, gpt-4, sp-500, jp-morgan-ai-research, defcon-system, analyse-pipeline, dynastie-depot-skill]
---

# AI in Investment Analysis

> **Diese Seite ist die zentrale Synthese** für alles rund um den Einsatz von Künstlicher Intelligenz in der Aktienanalyse, Depot-Verwaltung, Trading-Strategien und Finanzplanung. Sie wächst mit jedem neuen ingested Source und jeder neuen Erkenntnis.

---

## Leitthese

KI — insbesondere Large Language Models — ist heute in der Lage, mehrere klassische Aufgaben der professionellen Finanzanalyse zu übernehmen, zu ergänzen und in Teilen zu übertreffen. Die Kombination aus **strukturierten Finanzdaten, gezieltem Prompting und kontinuierlichem Lernen** ermöglicht eine neue Art der personalisierten, datengetriebenen Depot-Strategie.

---

## Bewiesene KI-Fähigkeiten (Stand 2024–2025)

### Was KI heute kann

| Aufgabe | Qualität | Quellen |
|---|---|---|
| Aktien-Ratings (3–6 Monate) | Besser als Wall-Street-Analysten | [[LLMs for Equity Stock Ratings]] |
| Sentiment-Analyse von News | Zuverlässig, effizient | [[LLMs for Equity Stock Ratings]] |
| Fundamentaldaten-Analyse | Sehr stark, stärkste Modalität | [[LLMs for Equity Stock Ratings]] |
| News-Zusammenfassung | Gut, effektiv für Kurzfrist | [[LLMs for Equity Stock Ratings]] |
| Chain-of-Thought Reasoning | Transparent, nachvollziehbar | [[LLMs for Equity Stock Ratings]] |

### Wo menschliche Analysten noch besser sind
- **Langfristige Prognosen (>12 Monate)**
- Qualitative Unternehmensbeurteilung (Management, Kultur)
- Regulatorische & politische Risikobewertung
- Earnings-Call-Nuancen (Tonalität, implizite Signale)

---

## Aktuelle Erkenntnisse (nach Quellen)

### Quelle 1: [[LLMs for Equity Stock Ratings]] (J.P. Morgan, 2024)

**Kernbotschaft:** GPT-4 schlägt ohne Fine-Tuning professionelle Analysten bei 3–12-Monats-Ratings.

**Schlüsselergebnisse:**
1. Vanilla-LLM (13 Kennzahlen) > Analyst-Baseline (MAE 1.447 vs. 1.570)
2. Fundamentals = stärkste Daten-Modalität (MAE 1.421)
3. Fundamentals + Sentiment = beste Gesamtperformance (MAE 1.417)
4. News hilfreich nur kurzfristig (1 Monat), sonst schädlich durch Positivity Bias
5. Analysten haben 43% Strong Buy → struktureller Positivitäts-Bias
6. LLMs stärker bei 1–6 Monaten, Analysten bei 12–18 Monaten

---

## Handlungs-Framework für eigene Depot-Strategie

### Daten-Pyramide (Priorität bei eigener Analyse)

```
       ┌─────────────┐
       │  Fundamentals │  ← Höchste Priorität: Bilanz, GuV, FCF
       │   (10-Q/10-K) │
       └──────┬────────┘
              │
       ┌──────┴──────────┐
       │ Technische      │  ← Mittlere Priorität: Preis, Volatilität,
       │  Indikatoren    │    Relative Performance
       └──────┬──────────┘
              │
       ┌──────┴──────────┐
       │ Sentiment-      │  ← Ergänzend: Nur Score, nicht Volltext-News
       │  Scores         │    Kurzfrist-Signal, nicht Long-Term-Basis
       └─────────────────┘
```

### Zeithorizont-Matrix

| Horizont | Beste Methode | Vertrauen |
|---|---|---|
| 1 Monat | News Summary + Technisch | Mittel (viel Rauschen) |
| 3–6 Monate | Fundamentals + Sentiment | Hoch |
| 12 Monate | Fundamentals | Gut |
| >12 Monate | Fundamentals + Analysten-Konsensus | Kombiniert |

### Checkliste vor jeder Investment-Entscheidung

- [ ] Fundamentaldaten der letzten 4 Quartale gelesen (Bilanz, GuV, FCF)?
- [ ] Sektor-Relative Performance bewertet?
- [ ] Analyst-Konsensus verglichen (mit Positivitäts-Bias adjustiert)?
- [ ] Sentiment-Score als Zusatz-Signal geprüft?
- [ ] LLM-Analyse mit Chain-of-Thought durchgeführt?
- [ ] Zeithorizont definiert und passende Methode angewendet?

---

## Offene Fragen & Forschungsrichtungen

### Ungeklärt / Zu erforschen
1. **Performance neuerer Modelle:** Claude 3.5+, GPT-4o, Gemini Ultra auf dieser Aufgabe
2. **Earnings Call Integration:** Wie stark verbessern Transkripte die Prognosegenauigkeit?
3. **Portfolio-Konstruktion:** Wie baut man ein diversifiziertes Portfolio auf Basis von LLM-Ratings?
4. **Rebalancing-Frequenz:** Monatlich (wie in der Studie) vs. quartalsweise vs. ereignisbasiert
5. **Internationale Märkte:** DAX, MSCI World — gelten dieselben Erkenntnisse?
6. **Small/Mid-Caps:** Weniger Analyst-Coverage → LLM-Vorteil noch größer?
7. **Alternative Daten:** Satellitendaten, Kreditkartentransaktionen, Social Media

### Widersprüche & Limitierungen im Wissensstand
- *Noch keine Widersprüche zwischen Quellen — Wiki wächst*

---

## Wichtige Konzepte (Quick-Links)

**Methodik:** [[LLM-Based Stock Rating]] · [[Chain-of-Thought Prompting]] · [[Forward Returns Evaluation]]  
**Daten:** [[Financial Fundamentals Analysis]] · [[News Sentiment Analysis]]  
**Vergleich:** [[Analyst Stock Ratings]]  
**Tools/Modelle:** [[GPT-4]]  
**Universum:** [[S&P 500]]

---

## Verbindung zum Dynastie-Depot System

Die Erkenntnisse aus der JP-Morgan-Forschung fließen direkt ins **[[DEFCON-System]]** ein:

| Forschungsergebnis | DEFCON-Implementierung |
|--------------------|----------------------|
| Fundamentals = stärkste Modalität | Fundamentals-Block = 50 von 100 Punkten |
| News-Sentiment nur kurzfristig | Sentiment-Block = 10 Punkte (Ergänzung, nicht Kern) |
| 43% Strong-Buy-Bias bei Analysten | Analyst-Konsensus mit Bias-Korrektur gewertet |
| Chain-of-Thought erhöht Qualität | !Analysiere = strukturierter CoT-Workflow |
| Quintil-basierte Bewertung | DEFCON-Schwellen (4/3/2/1) analog zu Quintilen |

**Operative Umsetzung:**
- [[Analyse-Pipeline]] — Wie KI-Analyse in den Workflow integriert ist
- [[defeatbeta]] · [[Shibui-SQL]] — Datenquellen für die Fundamentals-Analyse
- [[quick-screener]] — Schnell-Filter vor der KI-gestützten Tiefenanalyse

---

## Originaldokumente (raw/)

- [[AI in Investment Analysis LLMs for Equity Stock Ratings]] — J.P. Morgan, ICAIF 2024
- [[Stock picking with machine learning]] — [[Dominik Wolff]], [[Fabian Echterling]] (Wiley, 2024): ML-basierte wöchentliche Aktienauswahl im S&P 500; regularisierte Logistic Regression ~ komplexere ML-Modelle
- [[Large Language Models in equity markets applications, techniques, and insights]] — [[Aakanksha Jadhav]], [[Vishal Mirza]] (PMC, 2025): Survey über 84 Studien zu LLMs in Equity Markets

---

## Nächste Schritte & Quellen-Wünsche

> Quellen, die diese Synthese vertiefen würden:
> - Paper zu Earnings-Call-Transkript-Analyse mit LLMs
> - Studien zu Portfolio-Konstruktion auf Basis von Faktor-Signalen
> - Research zu Rebalancing-Strategien (Frequenz, Trigger)
> - Vergleich verschiedener LLM-Architekturen für Finanzaufgaben
> - Paper zu KI-gestütztem Risikomanagement & Position Sizing

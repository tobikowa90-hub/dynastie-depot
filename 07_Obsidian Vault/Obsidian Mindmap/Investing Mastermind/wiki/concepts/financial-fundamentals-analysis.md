---
title: "Financial Fundamentals Analysis"
type: concept
tags: [fundamentalanalyse, bilanz, sec-filings, aktienanalyse, kennzahlen]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [llm-stock-rating, analyst-stock-ratings, forward-returns-evaluation, sp-500, ai-in-investment-analysis]
---

# Financial Fundamentals Analysis

Die Analyse von Unternehmensdaten aus offiziellen Finanzberichten — Bilanz, Gewinn- und Verlustrechnung, Cashflow-Statement — um den inneren Wert und die finanzielle Gesundheit eines Unternehmens zu beurteilen. Fundamentaldaten sind die stärkste nachgewiesene Daten-Modalität für LLM-basierte Aktienprognosen.

## Die drei Kernberichte

### Bilanz (Balance Sheet)
Zeigt Vermögen, Schulden und Eigenkapital zu einem Stichtag.
- **Assets:** Umlauf- und Anlagevermögen
- **Liabilities:** kurz- und langfristige Verbindlichkeiten
- **Equity:** Eigenkapital der Aktionäre

Wichtige Kennzahlen: Verschuldungsgrad (Debt/Equity), Current Ratio, Book Value per Share

### Gewinn- & Verlustrechnung (Income Statement)
Zeigt Erlöse, Kosten und Gewinn über einen Zeitraum.
- Revenue (Umsatz)
- Gross Profit / Operating Income / Net Income
- EPS (Earnings per Share)
- Margins (Gross Margin, Operating Margin, Net Margin)

### Cashflow-Statement
Zeigt tatsächliche Geldflüsse — wichtiger als Buchgewinn.
- Operating Cash Flow (OCF) — Kerngeschäft
- Investing Cash Flow — Investitionen (CapEx)
- Financing Cash Flow — Schulden, Dividenden, Aktienrückkäufe
- Free Cash Flow (FCF) = OCF − CapEx

## Datenquellen für US-Aktien

### SEC EDGAR (primär)
- **10-Q:** Quartalsbericht (ungeprüft)
- **10-K:** Jahresbericht (geprüft)
- **8-K:** Ad-hoc-Meldungen bei wesentlichen Ereignissen
- Zugang: via `finagg` API, `sec-edgar-api`, direkt über SEC API

### Weitere Quellen
- Yahoo Finance (eingeschränkte API)
- Macrotrends.net (historisch)
- Simplywall.st (visualisiert)
- Morningstar, Bloomberg (professionell)

## Einsatz im LLM-Kontext

Aus [[LLMs for Equity Stock Ratings]] (J.P. Morgan):
- Letzte 4 Quartalsberichte (12 Monate) werden im Kontext bereitgestellt
- **Format:** HTML-Tabellen (übertrifft JSON/CSV für LLM-Verständnis)
- Detaillierte Metriken-Definitionen im System-Prompt
- LLM wird explizit aufgefordert, Fundamentaldaten in seiner Analyse zu verwenden

**Ergebnis:** Fundamentals sind die mit Abstand stärkste Daten-Modalität. MAE sinkt von 1.447 (Vanilla) auf 1.421 (Fundamentals) — konsistente Verbesserung über alle Zeithorizonte.

## Wichtige Fundamentalkennzahlen für Aktienanalyse

| Kategorie | Kennzahl | Bedeutung |
|---|---|---|
| Bewertung | P/E Ratio | Kurs/Gewinn-Verhältnis |
| Bewertung | P/B Ratio | Kurs/Buchwert-Verhältnis |
| Bewertung | EV/EBITDA | Enterprise Value / operativer Gewinn |
| Profitabilität | ROE | Return on Equity |
| Profitabilität | ROA | Return on Assets |
| Profitabilität | Net Margin | Nettogewinnmarge |
| Liquidität | Current Ratio | Kurzfristige Zahlungsfähigkeit |
| Verschuldung | Debt/Equity | Fremdkapitalquote |
| Wachstum | Revenue Growth YoY | Umsatzwachstum |
| Cashflow | FCF Yield | Free Cashflow / Marktkapitalisierung |

## Relevanz für eigene Depot-Strategie

> Fundamentaldaten sind der **wichtigste Input** für jede KI-gestützte Aktienanalyse. Vor jeder Investment-Entscheidung sollten Bilanz, GuV und Cashflow der letzten 4 Quartale analysiert werden — entweder manuell oder als strukturierter LLM-Input.

## Verbundene Seiten

- [[LLMs for Equity Stock Ratings]] · [[LLM-Based Stock Rating]] · [[Analyst Stock Ratings]]
- [[S&P 500]] · [[Forward Returns Evaluation]] · [[AI in Investment Analysis]]

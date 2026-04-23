---
title: "LLMs for Equity Stock Ratings"
type: source
tags: [llm, equity-analysis, stock-rating, jp-morgan, gpt-4, fundamentals, sentiment-analysis, chain-of-thought, financial-ai, sp-500]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [llm-stock-rating, financial-fundamentals-analysis, chain-of-thought-prompting, news-sentiment-analysis, forward-returns-evaluation, analyst-stock-ratings, jp-morgan-ai-research, gpt-4, sp-500, ai-in-investment-analysis]
aliases:
  - "LLMs for Equity Stock Ratings"

---

# LLMs for Equity Stock Ratings

**Originaltitel:** AI in Investment Analysis: LLMs for Equity Stock Ratings  
**Autoren:** Kassiani Papasotiriou, Srijan Sood, Shayleen Reynolds ([[J.P. Morgan AI Research]]) · Tucker Balch (Emory University)  
**Konferenz:** ICAIF '24, 14.–17. November 2024, Brooklyn, NY, USA  
**arXiv:** 2411.00856  
**Modell:** [[GPT-4]]-32k (v0613), Training-Cutoff September 2021  
**Datenzeitraum:** Januar 2022 – Juni 2024 · Universum: [[S&P 500]] (500 Aktien)

---

## Kernthese

LLMs können ohne Fine-Tuning allein durch gezieltes Prompting Stock-Ratings generieren, die traditionelle Wall-Street-Analysten in ihrer Genauigkeit übertreffen — gemessen an tatsächlichen Forward Returns. Das Paper ist eine der ersten reproduzierbaren Studien, die LLMs direkt für die Aktien-Rating-Aufgabe einsetzt und verschiedene Daten-Modalitäten systematisch vergleicht.

---

## Methodik

### Modell & Setup
- **Modell:** [[GPT-4]]-32k (v0613), gehostet auf Azure
- **Kontextfenster:** 32.000 Token
- **Training-Cutoff:** September 2021 — bewusst gewählt, um Information Leakage zu verhindern
- **Kein Fine-Tuning** — rein Prompting-basiert, kostengünstig und reproduzierbar

### Prompt-Design
- **System-Prompt:** LLM übernimmt Rolle eines Financial Analysts; Rating-Skala und Definitionen werden explizit vorgegeben inkl. Synonyme für unterschiedliche Terminologien
- **User-Prompt:** [[Chain-of-Thought Prompting]] — LLM begründet zuerst, nennt Preis-Targets, dann gibt es das Rating aus
- **Few-Shot Learning:** Ein vollständiges Beispiel (Input + Output) im Kontext
- **Chain of Verification (CoVE):** Datumsprüfung als Halluzinations-Check
- **Datenformat:** HTML-Tabellen für Fundamentaldaten (übertrifft JSON/CSV laut Literatur)

### Rating-Skala
5 Stufen (ordinal): Strong Sell (−2) · Moderate Sell (−1) · Hold (0) · Moderate Buy (+1) · Strong Buy (+2)

### Problemformulierung
- Rating `rating_c(t,p)` für Unternehmen `c`, veröffentlicht am Datum `t`, mit Zeithorizont `p` Monate
- Ground Truth: Quintil des tatsächlichen Forward Returns im Vergleich zu allen anderen S&P-500-Unternehmen
- Rating gilt als korrekt, wenn Quintil des Returns = Rating-Stufe

### Evaluierungsmetrik
- **MAE (Mean Absolute Error)** — berücksichtigt Magnitude der Fehler, nicht nur ob richtig/falsch
- Zwei Varianten: market-relative und sector-relative Forward Returns
- **Composite Score:** Durchschnitt über 3-, 6- und 12-Monats-Horizonte (1 Monat zu kurzfristig, 18 Monate außerhalb normalem Analysten-Horizont)

### Zeithorizonte
1, 3, 6, 12 und 18 Monate

---

## Daten-Modalitäten (5 Experimente)

| Methode | Dateneingabe | Return MAE | Sector MAE |
|---|---|---|---|
| Analyst (Baseline) | Echte Wall-Street-Ratings | 1.570 ± 0.637 | 1.591 ± 0.648 |
| Vanilla | Technische Indikatoren (13 Werte) | 1.447 ± 0.745 | 1.459 ± 0.749 |
| News (Summary) | + Monats-News-Zusammenfassung | 1.491 ± 0.738 | 1.513 ± 0.744 |
| News (Sentiment) | + Sentiment-Score (−5 bis +5) | 1.496 ± 0.752 | 1.512 ± 0.755 |
| Fundamentals | + SEC-Filings (10-Q/10-K) | 1.421 ± 0.732 | 1.439 ± 0.739 |
| **Fundamentals + Sentiment** | + SEC + Sentiment-Score | **1.417 ± 0.747** | **1.441 ± 0.752** |

*Niedrigerer MAE = bessere Prognose. Alle LLM-Methoden schlagen die Analyst-Baseline.*

---

## Datensätze im Detail

### Analyst-Ratings
- 45.000 Ratings von 126 Firmen (Jan 2022 – Jun 2024)
- Rating-Typen: 75.9% Maintained, 7.25% Reiterate, 6.27% Downgrade, 5.68% Upgrade, 4.89% Initiate
- Top-5-Firmen: Morgan Stanley (9.99%), Barclays (6.52%), Wells Fargo (5.91%), Citigroup (4.67%), RBC Capital (4.52%) = 31.61% aller Ratings

### Financial News Summaries
- Quellen: mehrere News-Provider, S&P-500-Universum
- Filterung: Named Entity Recognition (NER) mit Unternehmensname + Aliases
- Ø pro Ticker/Monat: 39.63 Artikel · 187K Zeichen · 40K Token · 74.7 URLs
- Zusammenfassung: GPT-4-32k fasst monatlich Firmen- und Sektor-News zusammen

### News Sentiment
- GPT-4-32k bewertet jede Zusammenfassung: Skala −5 (extrem negativ) bis +5 (extrem positiv)
- Zwei Scores: Firmen-Sentiment + Sektor-Sentiment

### Historical Returns (Technische Indikatoren)
- Aktueller Preis, 52-Wochen-Range (Min/Max), 90-Tage-Volatilität
- Performance-Metriken: 1-, 3-, 12-Monats-Returns (absolut, markt-relativ, sektor-relativ)
- Gesamt: 13 Zahlenwerte pro Unternehmen

### Financial Fundamentals
- Quelle: SEC-Filings (10-Q + 10-K) via `finagg` API / SEC EDGAR API
- Zeitraum: Jan 2022 – Mrz 2024 · jeweils die letzten 4 Quartalsberichte
- Inhalte: Bilanz (Balance Sheet), Gewinn- & Verlustrechnung (Income Statement), Cashflow-Statement
- Format im Prompt: HTML-Tabellen

---

## Kernergebnisse

### 1. LLM schlägt Analysten (Vanilla vs. Analyst)
Das Vanilla-Modell (nur 13 Kennzahlen) erreicht MAE 1.447 vs. 1.570 bei echten Analysten — eine Verbesserung von ~8%. Allerdings hat Vanilla eine höhere Standardabweichung (0.745 vs. 0.637), was auf weniger Konsistenz hindeutet.

**Einschränkung:** Analysten-Ratings fehlt das exakte Target-Date, daher wurde mit mehreren Zeithorizonten verglichen — kein perfekter 1:1-Vergleich.

### 2. Fundamentaldaten = stärkste Daten-Modalität
[[Financial Fundamentals Analysis]] (Bilanz, GuV, Cashflow) verbessert die Prognosegenauigkeit am stärksten und konsistentsten über alle Zeithorizonte (3, 6, 12 Monate). Fundamentals + Sentiment erreicht den besten Composite-MAE (1.417).

### 3. News: kurzfristig hilfreich, mittelfristig schädlich
[[News Sentiment Analysis]] verbessert 1-Monats-Prognosen (beste Kurzzeit-Performance aller Methoden), verschlechtert aber mittelfristige Prognosen gegenüber Vanilla. Ursache: **Positivity Bias** — News-Daten veranlassen das LLM zu übermäßig positiven Ratings.

Evidenz: Spearman-Korrelation zwischen News-Sentiment und LLM-Rating: ~0.44 (Firmennews, 1-Monats-Horizont) — News dominiert Urteil des Modells stärker als Fundamentaldaten.

### 4. Sentiment-Score ≈ News-Summary (bei deutlich weniger Token-Kosten)
Kein signifikanter Unterschied in der Performance zwischen vollständigen News-Texten und reinen Sentiment-Scores (−5 bis +5). Für die Praxis: **Sentiment-Scores sind effizienter und gleichwertig.**

### 5. Analysten besser bei langen Horizonten (12–18 Monate)
Analysten-MAE sinkt mit längerem Horizont. LLM-Fehler steigen mit Horizont. Kreuzungspunkt ca. bei 12–18 Monaten. LLM-Stärke: 1–6 Monate.

### 6. Analyst-Bias: 43% Strong Buy
Echte Analysten vergeben 43% Strong Buy und <5% Sell-Ratings — struktureller Positivitäts-Bias (kommerzielle Interessenkonflikte). LLMs verteilen Ratings deutlich gleichmäßiger.

### 7. News-Sentiment korreliert stark mit LLM-Output
Heatmap-Analyse zeigt: LLM-Ratings korrelieren stark mit eigenen Sentiment-Einschätzungen aus dem Vormonat — News-Stimmung "infiziert" Ratings systematisch.

---

## Limitierungen

- Forward-Return-Evaluierung sensitiv gegenüber Markt-Extremereignissen
- Keine Earnings-Call-Reports, Managementgespräche, qualitative Einschätzungen
- Exaktes Target-Date der Analysten-Ratings unbekannt → eingeschränkte Vergleichbarkeit
- GPT-4-32k (v0613) — neuere Modelle könnten deutlich besser abschneiden
- Nur S&P 500 — keine Small/Mid-Caps, keine internationalen Märkte
- Zeitraum (2022–2024) enthält spezifische Marktbedingungen (Zinswende, Inflation)

---

## Zukunft (laut Paper)

- Längere Zeithorizonte
- Diversere Datensätze
- Neuere LLM-Modelle
- Detailliertere Investment-Reports

---

## Relevanz für eigene Depot-Strategie

> Dieses Paper ist methodische Grundlage für KI-gestützte Depot-Analyse.
>
> **Praktische Ableitungen:**
> - Fundamentaldaten (Bilanz, GuV, Cashflow) sind der wertvollste Input für LLM-Ratings → Priorität bei eigener Analyse
> - Sentiment-Scores statt Volltext-News einsetzen für effiziente und rauscharme Analyse
> - LLM-Ratings für 1–6 Monate als Entscheidungshilfe nutzen, für längere Horizonte Analysten-Research hinzuziehen
> - Analyst-Ratings kritisch betrachten: strukturell zu positiv (43% Strong Buy)
> - Bei News-Integration: Positivitäts-Bias aktiv gegensteuern

---

## Verbundene Seiten

- [[LLM-Based Stock Rating]] · [[Financial Fundamentals Analysis]] · [[Chain-of-Thought Prompting]]
- [[News Sentiment Analysis]] · [[Forward Returns Evaluation]] · [[Analyst Stock Ratings]]
- [[J.P. Morgan AI Research]] · [[GPT-4]] · [[S&P 500]]
- [[AI in Investment Analysis]] (Synthesis)

## Originaldokument

- [[AI in Investment Analysis LLMs for Equity Stock Ratings]] — Volltext (raw/)

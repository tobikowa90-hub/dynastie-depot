---
title: "Forward Returns Evaluation"
type: concept
tags: [evaluierung, rendite, backtesting, prognose-güte, quantitativ]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [llm-stock-rating, analyst-stock-ratings, sp-500, financial-fundamentals-analysis, ai-in-investment-analysis]
aliases:
  - "Forward Returns Evaluation"

---

# Forward Returns Evaluation

Eine Methode zur Bewertung der Qualität von Aktien-Ratings, bei der die prognostizierte Einschätzung (Buy/Hold/Sell) mit der tatsächlichen zukünftigen Rendite (Forward Return) verglichen wird. Kernfrage: Hat das Rating die relative Performance des Unternehmens korrekt eingeschätzt?

## Grundidee

Statt zu messen, ob ein Analyst "Recht hatte" (binär), wird bewertet, **wie nah die Einschätzung an der tatsächlichen relativen Performance** lag. Dies ist robuster als einfache Accuracy-Messungen.

## Technische Umsetzung

### Schritt 1: Forward Returns berechnen
Für jedes Unternehmen `c` und Zeithorizont `p`:
```
R_c(t, p) = (P_c(t+p) - P_c(t)) / P_c(t)
```
Zusätzlich: markt-relative und sektor-relative Returns.

### Schritt 2: Quintil-Einteilung
Alle Unternehmen im Universum (z.B. S&P 500) werden nach ihrer Forward-Rendite in **5 gleichgroße Gruppen** (Quintile) aufgeteilt:
- Quintil 5 (bester 20%): Strong Buy
- Quintil 4: Moderate Buy
- Quintil 3: Hold
- Quintil 2: Moderate Sell
- Quintil 1 (schlechtester 20%): Strong Sell

### Schritt 3: Vergleich Rating vs. Ground Truth
Ein Rating gilt als korrekt, wenn das Quintil des tatsächlichen Returns mit der Rating-Stufe übereinstimmt.

### Schritt 4: MAE berechnen
MAE = Mean Absolute Error zwischen prognositiziertem Rating und Ground-Truth-Quintil.
- Fehler von 0: perfekte Prognose
- Fehler von 4: maximal falsch (Strong Buy bei tatsächlichem Strong Sell)
- Typische Werte in Studien: 1.4–1.6

## Warum MAE statt Accuracy?

- **Accuracy** behandelt alle Fehler gleich — ein Rating um 1 Stufe daneben ist "falsch" wie 4 Stufen daneben
- **MAE** gewichtet größere Fehler stärker — realistischer für Investmententscheidungen
- Bei balancierter Klassen-Verteilung (Quintile = je 20%) ist MAE direkt vergleichbar

## Composite Score

In [[LLMs for Equity Stock Ratings]] wird der MAE über **3-, 6- und 12-Monats-Horizonte gemittelt** als Composite Score für Methodenvergleich:
- 1 Monat: zu kurzfristig, zu viel Rauschen
- 18 Monate: außerhalb normaler Analysten-Planungshorizonte
- 3/6/12 Monate: der praktisch relevante Bereich

## Markt-relativ vs. Sektor-relativ

Zwei Varianten werden parallel berechnet:
- **Markt-relative** Returns: Vergleich mit allen anderen S&P-500-Aktien
- **Sektor-relative** Returns: Vergleich nur innerhalb desselben Sektors

Sektor-relative Bewertung ist relevanter für **Sektor-Rotation-Strategien** und Portfolios, die Sektor-Exponierungen kontrollieren.

## Relevanz für eigene Strategie

> Forward Returns Evaluation ist der Standard zur Bewertung von Prognose-Systemen. Wenn du KI-generierte Ratings testest, solltest du:
> 1. Immer **relative** (nicht absolute) Returns verwenden
> 2. Mehrere Zeithorizonte gleichzeitig testen
> 3. MAE als primäre Metrik nutzen
> 4. Sektor-relative Analyse für gezielte Sektor-Strategien einsetzen

## Verbundene Seiten

- [[LLMs for Equity Stock Ratings]] · [[LLM-Based Stock Rating]] · [[Analyst Stock Ratings]]
- [[S&P 500]] · [[AI in Investment Analysis]]

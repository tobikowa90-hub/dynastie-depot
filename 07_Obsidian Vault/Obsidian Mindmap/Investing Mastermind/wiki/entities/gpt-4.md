---
title: "GPT-4"
type: entity
tags: [llm, openai, sprachmodell, ki-modell]
created: 2026-04-10
updated: 2026-04-10
sources: [llms-for-equity-stock-ratings]
related: [llm-stock-rating, chain-of-thought-prompting, ai-in-investment-analysis, jp-morgan-ai-research]
---

# GPT-4

Großes Sprachmodell (LLM) von OpenAI. In der Finanzforschung weit verbreitet für Textanalyse, Sentiment-Scoring, Zusammenfassungen und strukturierte Prognosen.

## Relevante Variante: GPT-4-32k (v0613)
- **Kontextfenster:** 32.000 Token
- **Training-Cutoff:** September 2021
- **Hosting:** Azure (in J.P. Morgan Studie)
- **Warum diese Version gewählt:** Training-Cutoff vor dem Datenzeitraum der Studie (Jan 2022 – Jun 2024) → kein Information Leakage möglich

## Einsatz in Finanzforschung
- Stock-Rating-Prognosen (J.P. Morgan, [[LLMs for Equity Stock Ratings]])
- News-Zusammenfassungen auf Firmen- und Sektor-Ebene
- Sentiment-Scoring (Skala −5 bis +5)
- Chain-of-Thought Reasoning für Investmententscheidungen

## Stärken im Finanzkontext
- Verarbeitung langer, strukturierter Dokumente (SEC-Filings)
- Zero-Shot / Few-Shot Lernfähigkeit
- Interpretierbarkeit durch Chain-of-Thought
- Kein Fine-Tuning notwendig

## Limitierungen
- Kontextfenster begrenzt (32K Token) — schränkt Datenmenge ein
- Training-Cutoff kann veraltet sein
- Neigt bei News-Daten zu Positivitäts-Bias

## Verbundene Seiten
- [[LLMs for Equity Stock Ratings]] · [[Chain-of-Thought Prompting]] · [[LLM-Based Stock Rating]] · [[J.P. Morgan AI Research]]

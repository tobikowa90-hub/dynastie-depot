---
title: "RAG-Uncertainty-Quantification (Bayesian-RAG-Pattern)"
type: concept
tags: [rag, uncertainty-quantification, monte-carlo-dropout, epistemic-uncertainty, retrieval, hallucination-mitigation]
created: 2026-04-20
updated: 2026-04-20
sources: [Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]
related: [Knowledge-Graph-Finance-Architecture, Agentic-Reflection-Pattern, Knowledge-Graph-Architektur-Roadmap]
wissenschaftlicher_anker: "Ngartera, Nadarajah, Koina (2026, Frontiers AI) — Bayesian RAG Framework"
konfidenzstufe: methoden-referenz
---

# RAG-Uncertainty-Quantification (Bayesian-RAG-Pattern)

> **Monte-Carlo-Dropout auf Query- und Document-Embeddings liefert epistemische Unsicherheits-Schätzung pro Retrieval-Treffer. Scoring-Funktion $S_i = \mu_i - \lambda \cdot \sigma_i$ balanciert Relevanz gegen Unsicherheit. Deployment-Pflicht für High-Stakes-Finance-QA.**

## Kern-Idee

Klassische Dense-Retrieval nutzt deterministische Embeddings: pro Query/Document genau **ein** Vektor, cosine-similarity ranking. Folge: Top-1-Treffer wird gleich behandelt, egal ob sehr zuverlässig oder nur knapp über Threshold.

**Bayesian RAG fügt Unsicherheits-Dimension hinzu:**

1. Aktiviere Dropout während Inference (nicht nur Training)
2. Führe $n$ Forward-Passes pro Query durch → $n$ stochastische Embeddings
3. Berechne $\mu_i$ (Mittelwert, = Relevanz) und $\sigma_i$ (Standardabweichung, = Unsicherheit)
4. Score: $S_i = \mu_i - \lambda \cdot \sigma_i$

$\lambda$ = risk-aversion parameter (hoch = konservativ, penalize unsichere Treffer stärker).

## Epistemic vs. Aleatoric

Bayesian RAG fokussiert **epistemische Unsicherheit** (Modell-Unsicherheit aus limitierten Trainingsdaten), nicht aleatoric uncertainty (irreduzibles Datenrauschen).

| Typ | Ursache | Reduzierbar? | Relevanz für Finance-QA |
|---|---|---|---|
| Epistemic | Modell hat wenig Trainingsdaten zu diesem Topic | Ja (mehr Training) | **Hoch** (Finance-Spezifika sind oft unter-repräsentiert) |
| Aleatoric | Inherente Ambiguität im Input (z.B. doppeldeutiger Text) | Nein | Mittel (kontext-dependent) |

Für High-Stakes-Finance zählt primär epistemische Unsicherheit — "weiß das Modell genug über diese Entity/Metric, um vertrauenswürdig zu antworten?"

## Empirische Effekte (FNQA auf AAPL + MSFT 2023 10-K)

| Metrik | vs. BM25 | vs. DPR (Dense) | vs. ColBERT |
|---|---|---|---|
| Precision@3 | +20,6% | +10,1% | +5,6% |
| NDCG@10 | +25,4% | +13,8% | +8,8% |
| Uncertainty Calibration (ECE↓) | -26,8% | -21,1% | -18,2% |
| Faithfulness (Hallucination ↓) | +6,1% | +4,2% | +2,8% |

**15ms Latency, 20,8 queries/sec** — produktionsreif für interaktive Systeme.

## Architektonischer Vorteil: In-Scoring statt Post-hoc

Frühere Uncertainty-Methoden (Soudani et al. 2025) rekalibrieren Scores **nach** dem Ranking. Bayesian RAG integriert Uncertainty **ins Core-Scoring** — das downstream-LLM sieht bereits uncertainty-gewichtete Context-Chunks, muss keine eigene Confidence ableiten.

Parallele zu Composite-Anti-Overfitting-Objective (GT-Score): auch dort ist "in-the-loop" > "post-hoc".

## Abgrenzung zu verwandten Methoden

| Methode | Uncertainty-Quelle | Produktions-Readiness |
|---|---|---|
| **Bayesian RAG (MC-Dropout)** | Dropout-Ensemble auf Embeddings | Self-hosted Models only |
| Deep Ensembles (Lakshminarayanan et al.) | Mehrere unabhängig trainierte Modelle | Teuer (N× Compute) |
| Bayesian Neural Networks | Full posterior über Weights | Zu teuer für Production |
| Temperature-Scaling (post-hoc) | Kalibrierung des Output-Softmax | Nur für Klassifikation, nicht Retrieval |
| Conformal Prediction | Distribution-free Intervals | Retrieval-Adaption unklar |

Bayesian RAG ist **praktikabel** (MC-Dropout hat konstante Training-Cost, linear Inference-Cost in n).

## Anwendung auf Dynasty-Depot (heute: null operativ, konzeptuell wertvoll)

**DEFCON nutzt keine RAG.** Aber das Korrektheits-Prinzip (memory `feedback_correctness_over_runtime.md`) ist strukturell aligned:

| Morning-Briefing v3.0.3 Element | Bayesian-RAG-Äquivalent |
|---|---|
| `n.v. [Yahoo 403 known]` deterministisch | Uncertainty explizit → signal-bereinigt |
| Soft-Alert-Schema <180s/180-400s/>400s | abgestufte Confidence |
| Tavily-Triangulation 3-Quellen | statistische Ensemble-Proxy für echte MC-Dropout |
| "nicht verschleiern, markieren" | Bayesian-Output-Prinzip |

**Konkrete Limitation:** Production-Einsatz braucht selbst-gehostete Embedding-Modelle. Tavily/OpenAI/Cohere APIs erlauben kein Dropout-Tuning. Kein heute-wirksamer Pfad für Dynasty-Depot.

## Relevanz für zukünftige Skill-Erweiterungen

| Skill | Bayesian-RAG-Potenzial | Voraussetzungen |
|---|---|---|
| `insider-intelligence` (Form-4 XML) | nein | Strukturierte Daten, kein Retrieval |
| Morning-Briefing (Tavily) | theoretisch ja, produktiv nein | Self-hosted Embeddings |
| Hypothetisches 10-K-QA-Modul | ja | KG + Bayesian Retrieval |

Die Konzeptseite [[Knowledge-Graph-Architektur-Roadmap]] v0.1 adressiert diese Entscheidungen formal.

## Dos & Don'ts

**Do:**
- MC-Dropout als erste Wahl für Uncertainty (cheap im Training, linear in Inference)
- ECE-Kalibrierung als Post-Training-Check
- $\lambda$-Tuning auf Validation-Set, nicht Production-Traffic

**Don't:**
- Bayesian RAG bei Third-Party-Embeddings versprechen (nicht tunable)
- Uncertainty-Score als absolute Wahrscheinlichkeit interpretieren (Relativ-Maß)
- Einzelne MC-Samples nutzen (n muss ≥ 10-20 für stabile σ-Schätzung)

## Backlinks

- [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]] — primäre Source
- [[Knowledge-Graph-Finance-Architecture]] — komplementäres Konzept (KG + uncertainty-aware Retrieval)
- [[Agentic-Reflection-Pattern]] — Gegenstück für Extraction (statt Retrieval)
- [[Knowledge-Graph-Architektur-Roadmap]] — Architektur-Entscheidungsvorlage

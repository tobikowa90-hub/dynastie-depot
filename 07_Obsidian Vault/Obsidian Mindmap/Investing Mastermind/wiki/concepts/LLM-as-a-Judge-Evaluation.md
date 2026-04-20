---
title: "LLM-as-a-Judge-Evaluation"
type: concept
tags: [evaluation, llm-judge, ground-truth-agnostic, inter-rater-agreement, comparative-eval, chain-of-thought]
created: 2026-04-20
updated: 2026-04-20
sources: [Arun-et-al-2025-FinReflectKG]
related: [Agentic-Reflection-Pattern, Knowledge-Graph-Finance-Architecture, LLM-Investing-Bias-Audit, Composite-Anti-Overfitting-Objective]
wissenschaftlicher_anker: "Arun et al. (2025) — FinReflectKG Section 5.4; Lopez-Lira & Tang (2023); Vamvourellis & Mehta (2025)"
konfidenzstufe: methoden-referenz
---

# LLM-as-a-Judge-Evaluation

> **Ground-truth-agnostic Evaluation-Methodik: LLM vergleicht konkurrierende Outputs und votiert auf 4 Dimensionen (Precision, Faithfulness, Comprehensiveness, Relevance). 3-Vote-Consensus. Nutzt post-hoc-Rationalisierung statt Chain-of-Thought.**

## Kern-Idee

Klassische Evaluation braucht Ground-Truth-Referenzen (annotierte Datensätze, menschliche Labels). Für Knowledge-Graph-Extraction aus 10-K-Filings existiert keine solche Baseline — Ground-Truth-Generation wäre mehrjährige Expert-Arbeit.

**Alternative:** Setze einen LLM-Richter ein, der **konkurrierende Outputs relativ** bewertet, ohne Absolut-Baseline zu benötigen.

## FinReflectKG-Protokoll

1. Produziere drei Extraction-Outputs (Single-Pass, Multi-Pass, Reflection) für denselben Dokumenten-Chunk $c$
2. LLM-Judge erhält alle drei + den Source-Chunk
3. Judge vergibt Präferenzen auf vier Dimensionen:

| Dimension | Definition |
|---|---|
| **Precision** | Klarheit, Spezifität, Uniqueness der Triples |
| **Faithfulness** | Faktische Akkuratesse + Grounding im Source-Text |
| **Comprehensiveness** | Abdeckung der kern-informativen Inhalte |
| **Relevance** | Kontextuelle Alignment mit Themen des Chunks |

4. **3-Vote-Consensus** — 3 unabhängige Judge-Runs; bei Non-Consensus: 4. decisive vote
5. Aggregat-Agreement als Zuverlässigkeits-Metrik:

| Dimension | Agreement |
|---|---|
| Precision | 82,1% |
| Faithfulness | 81,3% |
| Comprehensiveness | 86,7% |
| Relevance | 83,7% |

Sub-85%-Agreement deutet auf höhere kontextuelle Unsicherheit hin (Tafel 8).

## Kritische Designentscheidung: Kein Chain-of-Thought beim Judge

FinReflectKG verwendet **direkte Judgment ohne explizites Reasoning davor**. Das widerspricht der Intuition — aber ist empirisch begründet:

- **Chen et al. 2024** ("Do not think that much for 2+3") — CoT unterperformt bei schnellen, intuitiven Aufgaben; Overthinking produziert Noise
- **Sui et al. 2025** (Survey Efficient Reasoning) — CoT hat spezifische Anwendungs-Sweet-Spots
- **Vamvourellis & Mehta 2025** (spezifisch Finance-Sentiment) — Reasoning vor Commitment verschlechtert Performance

**Implementation:** Judge committed first (gibt Vote ab), dann erklärt post-hoc. Das Human-Interpretierbarkeit-Argument (Post-hoc-Rationalization) kommt aus Kognitions-Forschung.

Parameter: Qwen3-32B, Temperatur 0,1, kein Reasoning-Prompt.

## Vorteile

1. **Keine Ground-Truth-Datensatz-Arbeit nötig** — instant anwendbar auf neuen Domains
2. **Cross-Model-Validation möglich** — verschiedene Judge-LLMs für Bias-Check
3. **Skalierbar** — parallelisierbar über Chunks
4. **Interpretierbare Output** — Judge gibt strukturiertes Vote + Post-hoc-Reasoning

## Limitationen & Risiken

1. **Bias des Judge-LLMs** — Qwen3-32B hat Eigen-Präferenzen; Cross-Family-Validation (GPT, Claude, Gemini) empfohlen
2. **Relativ, nicht absolut** — Aussagen sind "A > B" oder "A = B", nicht "A hat Qualität 87/100"
3. **Inter-Rater-Agreement <90%** deutet auf inhärente Unsicherheit hin — Cross-Check mit Human-Experts bleibt Gold-Standard
4. **Judge-LLM muss mächtig genug sein** — kleinere Judges (z.B. <10B) produzieren inkonsistente Votes

## Verwandte Muster

- **[[Composite-Anti-Overfitting-Objective]]** (GT-Score) — eigenständige Scoring-Methodik; kombiniert mit LLM-Judge als Evaluation
- **[[Agentic-Reflection-Pattern]]** — Gegenstück: LLM kritisiert eigenen Output; LLM-Judge bewertet konkurrierende Outputs

## Anwendung auf Dynasty-Depot

**Heute: null.** DEFCON-Scoring ist regelbasiert, nicht LLM-Output, keine "konkurrierenden Varianten" zu bewerten.

**Hypothetisch:** Bei zukünftigem A/B-Test verschiedener Scoring-Versionen (v3.7 vs. v3.8-Hypothese) könnte ein LLM-Judge-Ansatz helfen, qualitative Aspekte zu evaluieren — aber das ist **kein Ersatz** für empirische Backtesting-Validation (siehe [[Backtest-Methodik-Roadmap]]). LLM-Judges sind Ergänzung, nicht Kern.

## Dos & Don'ts

**Do:**
- 3-Vote-Consensus nutzen (nicht Single-Run)
- Cross-Model-Validation für Judge-Bias-Diagnose
- Agreement-Score als Uncertainty-Signal interpretieren
- Post-hoc-Rationalisierung statt Reasoning-vor-Commitment

**Don't:**
- Judge-Votes als absolute Qualitäts-Scores interpretieren
- Schwache Judge-LLMs nutzen (<10B Parameter produzieren Noise)
- Judge-Output als Ersatz für Human-Expert-Review behandeln (Komplementär, nicht Substitut)

## Backlinks

- [[Arun-et-al-2025-FinReflectKG]] — Quelle (Section 5.4)
- [[Agentic-Reflection-Pattern]] — Extraction-Seite (LLM-Judge bewertet deren Output)
- [[Knowledge-Graph-Finance-Architecture]] — Evaluations-Methode für KG-Quality
- [[LLM-Investing-Bias-Audit]] — Querbezug: LLM-Judges haben auch Bias-Risiko
- [[Composite-Anti-Overfitting-Objective]] — komplementäre Methoden-Alternative (GT-Score)

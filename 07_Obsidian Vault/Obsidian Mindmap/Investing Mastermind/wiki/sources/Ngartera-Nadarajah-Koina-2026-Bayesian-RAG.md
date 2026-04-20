---
title: "Bayesian RAG: Uncertainty-Aware Retrieval for Reliable Financial Question Answering"
date: 2026-01-27
type: source
subtype: academic-paper
tags: [rag, uncertainty-quantification, bayesian, monte-carlo-dropout, financial-qa, 10-k, epistemic-uncertainty, hallucination-reduction]
url: https://doi.org/10.3389/frai.2025.1668172
venue: "Frontiers in Artificial Intelligence (Frontiers) Vol. 8, 1668172 — Published 27 January 2026, Open Access (CC BY); Editor: Joerg Osterrieder (U Twente)"
authors: "Lebede Ngartera (TeraSystemsAI, Philadelphia PA), Saralees Nadarajah (Department of Mathematics, University of Manchester), Rodoumta Koina (University of N'Djamena, Chad; Present: ENSTP N'Djamena)"
status: processed
defcon_relevanz: "Keine DEFCON-Scoring-Änderung. Methoden-Anker für Morning-Briefing-Infrastruktur (Tavily-RAG-Pipeline): Bayesian RAG fügt einen 'epistemic uncertainty'-Score zu jeder Retrieval-Antwort hinzu (Monte Carlo Dropout auf Embeddings), der potenziell als Confidence-Signal für Tavily-Tavily-Quellen nutzbar wäre. ABER: produktionsbereit heute nicht — erfordert Model-Weights-Zugriff (Dropout-Inference), nicht verfügbar bei Third-Party-APIs wie Tavily. Relevanz eher konzeptuell: Validiert, dass Morning-Briefing v3.0.3 'Soft-Alert-Schema' + 'n.v.-deterministisch'-Markierungen der richtigen Design-Richtung folgen (Uncertainty explizit, nicht verschleiert)."
related: "[[RAG-Uncertainty-Quantification]], [[Knowledge-Graph-Finance-Architecture]], [[Knowledge-Graph-Architektur-Roadmap]]"
---

# Ngartera, Nadarajah, Koina — Bayesian RAG (Frontiers AI, Jan 2026)

## Abstract (eigene Worte)

Die Autoren lösen ein **Deployment-Problem** für RAG-Systeme in regulierten Finance-Kontexten: Deterministische Embeddings können **Unsicherheit nicht quantifizieren** → RAG-Systeme liefern überzeugende, aber falsche Antworten (Hallucinations) auf 10-K-Fragen. **Bayesian RAG** integriert **epistemische Unsicherheit** direkt in den Retrieval-Score via **Monte Carlo Dropout** auf Query- und Document-Embeddings. Scoring-Funktion $S_i = \mu_i - \lambda \cdot \sigma_i$ balanciert semantische Relevanz gegen Unsicherheit. Evaluation auf Apple + Microsoft 2023 10-K: **93,1% Accuracy** (Bayesian RAG + GPT Framework, Tab. Final-Results), +20,6% Precision@3, +22,7% MRR, +25,4% NDCG@10 vs. BM25 (Abstract); +26,8% bessere Uncertainty-Calibration gemäß Abstract (ECE 0,37 → 0,30 vs. BM25) bzw. -52% ECE gemäß Figure 2 (0,142 → 0,068 vs. Standard RAG) — **beide Zahlen stehen im Paper, verschiedene Baselines**; 27,8% weniger Hallucinations (Faithfulness-Metrik vs. best baseline). 15ms Latency, 20,8 Queries/Sekunde — produktionsreif.

## Kern-Innovation: Uncertainty-Aware Scoring

Klassisches Dense-RAG: cosine-similarity → Top-K → kontextualisiere LLM. **Fehlt:** Confidence-Maß für einzelne Retrieval-Treffer.

**Bayesian RAG**: 
1. Gleiche Query $n$ mal durch Dropout-aktiviertes Embedding-Modell → $n$ stochastische Embeddings pro Query und Document
2. Berechne Mean $\mu_i$ (Relevanz) + Standardabweichung $\sigma_i$ (Unsicherheit)
3. Score: $S_i = \mu_i - \lambda \cdot \sigma_i$ — penalize unsichere Treffer
4. $\lambda$ = risikoadjustierter Tuning-Parameter (hoch = konservativ)

**Definition Abgrenzung:** Das Paper fokussiert explizit **epistemic uncertainty** (Modell-Unsicherheit aus limitierten Trainingsdaten), NICHT aleatoric uncertainty (irreduzibles Datenrauschen). Das ist die entscheidungsrelevante Dimension für High-Stakes-Finance.

## Quantitative Befunde (Apple + MSFT 2023 10-K)

Das Paper gibt **mehrere Vergleichsebenen** — je nach Baseline unterschiedliche Prozentzahlen. Klar trennen:

**Ebene 1: Bayesian RAG vs. BM25 (Abstract, Tab. 1 Haupt-Benchmark)**

| Metrik | BM25-Baseline | **Bayesian RAG** | Δ |
|---|---|---|---|
| Precision@3 | baseline | +20,6% | +20,6% |
| Recall@5 | baseline | +15,2% | +15,2% |
| MRR | baseline | +22,7% | +22,7% |
| NDCG@10 | baseline | +25,4% | +25,4% |
| Uncertainty Calibration (ECE↓) | 0,37 | **0,30** | **-26,8%** |

**Ebene 2: Bayesian RAG vs. Standard RAG (Figure 2 Six-Panel)**

| Metrik | Standard RAG | **Bayesian RAG** | Δ |
|---|---|---|---|
| ECE | 0,142 | **0,068** | **-52%** |
| Precision@1 | baseline | +33% | +33% |
| Latency | 8ms | 15ms | +87,5% (akzeptierter Trade-off) |

**Ebene 3: Bayesian RAG + GPT Framework (End-to-End)**

| Metrik | Standard RAG + GPT | **Bayesian RAG + GPT** | Δ |
|---|---|---|---|
| Accuracy | ~85-88% | **93,1%** | +5-8pp |
| ECE | 0,052 | **0,034** | -34,6% |
| AUC | baseline | 0,961 | — |

**Konkrete Zahlen-Extraction** (Section 5 Case Study): Bayesian RAG extrahiert korrekt "$211.915B Microsoft Revenue 2023" und "$383.285B Apple Revenue 2023" aus 10-K-Tabellen — BM25 und Dense-Retrieval scheitern oder produzieren Halluzinationen.

**Wichtig für DEFCON-Kontext:** Die 26,8%-ECE-Reduktion (Abstract) und die 52%-ECE-Reduktion (Figure 2) sind **keine Widersprüche** — sie messen unterschiedliche Vergleiche (vs. BM25 vs. Standard-RAG). Beim Zitieren immer Baseline angeben.

## Beitrag zu DEFCON / Dynasty-Depot

**Direkte Anwendung: null.** DEFCON ist nicht RAG-basiert.

**Indirekte Relevanz — Morning-Briefing-Architektur:**

| Morning-Briefing v3.0.3 Design | Bayesian-RAG-Prinzip | Status |
|---|---|---|
| `n.v. [Yahoo 403 known]` deterministische Gap-Markierung | Uncertainty explizit machen statt verschleiern | **bereits verankert** (v3.0.3, Lever 1) |
| Soft-Alert-Schema <180s/180-400s/>400s | Abstufte Confidence statt Binär-Verdikt | **bereits verankert** (v3.0.3, Spec §6(E)) |
| Tavily-RAG-Pipeline mit fixed Top-K | Deterministische Embeddings, kein Uncertainty-Signal | Limitation, nicht adressierbar ohne Model-Weights-Zugriff |
| 3-Quellen-Triangulation vor Material-Filter | Statistische Redundanz statt Bayesian MC-Dropout | proxy-adäquat für Third-Party-APIs |

**Konsequenz:** Keine Skill-Code-Änderung. Aber: Bayesian RAG ist **wissenschaftliche Fundierung für das Korrektheits-Prinzip** aus memory `feedback_correctness_over_runtime.md` — das Morning-Briefing adressiert Uncertainty über **Soft-Alerts + n.v.-Markierungen**, nicht über Auto-Rollback oder aggressive Caching. Das steht jetzt wissenschaftlich belegt.

## Regulatorische Einordnung (Section 5.1)

Die Autoren heben hervor, dass interpretierbare Confidence-Scores mit **EU AI Act**, **SEC transparency requirements** und **NIST AI Risk Management Framework** alignen. Für Retail-Investor-Tools wie Dynasty-Depot ist das noch nicht regulatorisch bindend, aber zeigt die Richtung: Uncertainty-Disclosure wird in regulierten Finance-Anwendungen Standard.

## Limitationen (implizit aus Paper + Eigenanalyse)

1. **Nur 2 Ticker evaluiert** (AAPL + MSFT) — Generalisierung auf andere Sektoren offen
2. **Monte Carlo Dropout braucht Training-Time-Dropout** — in Third-Party-Embedding-APIs (OpenAI, Cohere, Tavily) nicht konfigurierbar. Produktions-Einsatz nur mit selbst-gehosteten Modellen (Sentence-BERT, BGE, etc.)
3. **15ms Latency bei $n$ MC-Samples** — skaliert linear mit $n$; Papier nennt Anzahl nicht explizit
4. **Trade-off Relevanz vs. Unsicherheit ($\lambda$-Tuning)** — keine allgemeine Kalibrierungs-Heuristik angegeben

## Abgrenzung — Was Bayesian RAG NICHT liefert

- **Keine Trading-Strategie** — Retrieval-Komponente, nicht Decision-Layer
- **Keine Backtest-Methodik** — orthogonal zu FINSABER/GT-Score/Bailey
- **Kein Knowledge-Graph** — klassisches Dense-Retrieval mit Dropout-Ensemble, keine Entity-Extraction (vgl. [[Arun-et-al-2025-FinReflectKG]])
- **Keine Fundamentals-Scoring-Änderung** — orthogonal zu DEFCON-Blöcken

## Abgrenzung zu anderen RAG-Unsicherheitsmethoden

Frühere Ansätze (Soudani et al. 2025) behandeln Uncertainty als **post-hoc recalibration** — nachgelagerte Kalibrierung der Ranking-Scores. Bayesian RAG integriert Uncertainty **im Core-Scoring** → principled relevance-confidence trade-off beim Retrieval, nicht nachgelagert. Architektonischer Vorteil mit praktischer Konsequenz: Downstream-LLM sieht bereits uncertainty-gewichtete Kontexte, muss keine eigene Confidence ableiten.

## Backlinks

- [[RAG-Uncertainty-Quantification]] — Konzeptseite (Core-Idee)
- [[Knowledge-Graph-Finance-Architecture]] — Konzeptseite (komplementär: KG + uncertainty-aware Retrieval)
- [[Knowledge-Graph-Architektur-Roadmap]] — neue Synthesis v0.1 (RAG-vs-KG-Trade-off)
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B23
- [[Lebede Ngartera]], [[Saralees Nadarajah]], [[Rodoumta Koina]] — Author-Entities

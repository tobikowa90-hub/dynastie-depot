---
title: "FinReflectKG: Agentic Construction and Evaluation of Financial Knowledge Graphs"
date: 2025
type: source
subtype: academic-paper
tags: [knowledge-graph, sec-10k, llm-extraction, agentic-reflection, financial-ai, information-extraction, llm-as-a-judge]
url: https://arxiv.org/abs/2508.17906
github: https://anonymous.4open.science/r/KG-Financial-Datasets-SP-100-529B/README.md
venue: "arXiv preprint 2508.17906v2 (2025); Author affiliation: Domyn (New York / Gurgaon India)"
authors: "Abhinav Arun, Fabrizio Dimino, Tejas Prakash Agarwal, Bhaskarjit Sarmah, Stefano Pasquali (alle Domyn)"
status: processed
defcon_relevanz: "Keine DEFCON-Scoring-Änderung. Architektur-Anker für Entscheidung `insider-intelligence` Skill: KG-Mehrwert vs. XML-Direkt-Parsing. Form-4-Insider-Filings sind strukturiertes XML (direkt parsebar) — aber 10-K-Kontext (MD&A, Risk Factors) ist narrativ und KG-extrahiert wertvoller. Codex Round 2: aus 🔴-Cluster auf 🟡 verschoben, weil Form-4 bereits XML = kein zwingender KG-Use-Case. Mögliche Nutzung: Cross-Entity-Queries (z.B. 'welche Satelliten haben Insider-Transactions bei Zuliefern?')."
related: "[[Labre-2025-FinReflectKG-Companion]], [[Knowledge-Graph-Finance-Architecture]], [[Agentic-Reflection-Pattern]], [[LLM-as-a-Judge-Evaluation]], [[Knowledge-Graph-Architektur-Roadmap]], [[insider-intelligence]]"
---

# Arun, Dimino, Agarwal, Sarmah, Pasquali — FinReflectKG (arXiv 2508.17906, 2025)

## Abstract (eigene Worte)

Die Domyn-Autoren lösen zwei lange offene Probleme im Finance-KG-Bereich: **Datenlücke** (keine offenen großskaligen KG-Benchmarks aus SEC-Filings) und **Qualitäts-Validierung** (fehlende ground-truth-agnostische Evaluations-Methodik). Sie veröffentlichen einen offenen KG-Datensatz aus **allen S&P-100 2024 10-K-Filings** und eine vollständige Konstruktions-Pipeline (Docling-Parsing → Tabellen-aware Chunking → schema-guided Triple-Extraction → Reflection-Feedback-Loop). Drei Extraktions-Modi (Single-Pass, Multi-Pass, Reflection-agentic) werden mit Qwen2.5-72B-Instruct empirisch verglichen. **Reflection-Modus** gewinnt in 3 von 4 LLM-as-a-Judge-Dimensionen (Precision 39,1%, Comprehensiveness 48,1%, Relevance 37,3%) und erreicht **64,8% CheckRules-Compliance bei allen 4 Regeln gleichzeitig**, während Single-Pass nur 42,3% erzielt. Trade-off: zusätzliche Inferenz-Rounds; nicht für Realtime-News-Feeds geeignet.

## Vier Hauptbeiträge (Section 1)

1. **Open-Source Finance-KG-Datensatz** — S&P-100, 2024-Jahres-10-K, 5-tupel-Triples (Head Entity, Head Type, Relationship, Tail Entity, Tail Type)
2. **3-Modi-Extraction-Pipeline** — Single-Pass / Multi-Pass / Reflection-agentic; letztere kombiniert Extraction-LLM + Critic-LLM + Correction-LLM in iterativem Feedback-Loop
3. **Holistische Evaluation** — CheckRules (Subject Reference, Length, Schema-Compliance) + Coverage-Ratios (ECR, TCR, RCR) + Shannon/Rényi-Entropy + LLM-as-a-Judge (3-Vote-Consensus)
4. **Schema-Canonicalisation-Vorbereitung** — schema-guided Extraction mit SME-approved Entity-Types (ORG, PERSON, COMP, PRODUCT, SEGMENT, FIN_METRIC, RISK_FACTOR, EVENT, REGULATORY_REQUIREMENT, ESG_TOPIC) und Relations (Has_Stake_In, Operates_In, Produces, Impacts, Discloses, Complies_With, Supplies, Partners_With, …)

## Reflection-Agentic-Workflow (Section 4.3.3)

Ein dreistufiger iterativer Loop pro Chunk `c`:

| Schritt | Rolle | Aktion |
|---|---|---|
| 1 | Extraction-LLM | Generiert initiale Triples $T_c^{(1)}$ gemäß Schema $S$ |
| 2 | Feedback-LLM (Critic) | Markiert Issues (abstrakte Referenzen, Schema-Verletzungen, Business-Relevanz) als strukturiertes JSON $F_c^{(t)}$ |
| 3 | Correction-LLM | Aktualisiert oder verwirft problematische Triples → $T_c^{(t)}$ |

Stopp-Kriterium: $F_c^{(t^*)} = \emptyset$ (keine Issues mehr) oder $t^* = n_{max}$. Die Schleife adressiert die drei häufigsten Extraction-Fehler: (a) "We"/"the company" statt Ticker, (b) Non-Schema-Entity-Types wie "RISK_TYPE" statt "RISK_FACTOR", (c) redundante Relationship-Varianten wie "supplies"↔"is supplier of".

## Quantitative Ergebnisse

### CheckRules-Compliance (Table 3-4)

| Regel (↑) | Single Pass | Multi Pass | Reflection |
|---|---|---|---|
| Subject Reference | 99,9% | 100,0% | 100,0% |
| Entity Length ≤5 Wörter | 68,2% | 79,5% | 78,0% |
| Entity Schema Compliance | 95,9% | 96,6% | **98,1%** |
| Relationship Schema Compliance | 64,6% | 62,0% | **84,2%** |
| **Alle 4 Regeln gleichzeitig** | 42,3% | 47,3% | **64,8%** |

### LLM-as-a-Judge (Table 7, 3-Vote-Consensus, Qwen3-32B)

| Metrik (↑) | Single Pass | Multi Pass | Reflection |
|---|---|---|---|
| Precision | 22,3% | 38,6% | **39,1%** |
| Faithfulness | **40,1%** | 24,4% | 35,5% |
| Comprehensiveness | 36,3% | 15,6% | **48,1%** |
| Relevance | 34,6% | 28,1% | **37,3%** |

### Coverage-Ratios (Table 5)

Reflection erzeugt **15,8 Triples/Chunk** (vs. 13,3 / 12,4), ECR 0,53 (vs. 0,30/0,31), RCR 0,38 (vs. 0,21/0,22) — reichere semantische Abdeckung.

## DEFCON-Relevanz — Architektur-Frage statt Scoring-Change

**Dieses Paper ändert nicht DEFCON.** Es öffnet eine **Architektur-Frage** für die Insider-Intelligence-Skill-Evolution:

| Dimension | Form-4 (aktuell) | 10-K-KG (hypothetisch) |
|---|---|---|
| Datenformat | XML (strukturiert, direkt parsebar) | Narrativ (KG-Extraction nötig) |
| Extraktions-Aufwand | Python-Parser, ~Min pro Satellit | LLM-Pipeline, ~Stunden pro Satellit + Evaluation |
| Cross-Entity-Queries | begrenzt (Insider → Ticker) | reichhaltig (Produkte, Zulieferer, Risk-Factors, ESG) |
| Insider-Scan-Nutzen | direkt | indirekt (Kontext-Anreicherung) |

**Codex Round 2 Verdikt:** KG-Konstruktion für Form-4 ist **Over-Engineering** — XML direkt zu parsen ist korrekt. KG-Mehrwert liegt in 10-K-Analyse (MD&A, Risk Factors, Management-Discussion) oder Cross-Filing-Queries (Supplier-Relationen, ESG-Themen, Segment-Performance). Diese Frage ist keine Scoring-, sondern **Skill-Architektur-Frage**.

→ **Konsequenz:** Keine §-Änderung in INSTRUKTIONEN. Neue Synthesis-Seite [[Knowledge-Graph-Architektur-Roadmap]] v0.1 mit Entscheidungsvorlage (KG vs. XML-Direkt-Parsing vs. Hybrid).

## Limitationen (Section 6 Discussion)

1. **Cross-Document Co-Reference** nur partiell — Reflection-Loop arbeitet auf isolierten Filings
2. **LLM-as-a-Judge ist Surrogat** — Qwen3-32B-Bias propagiert in Evaluation; Cross-Family-Validation empfohlen
3. **Faithfulness sinkt bei Reflection (35,5% vs. 40,1% Single-Pass)** — mehr Triples → höhere Chance auf hallucination; Trade-off Comprehensiveness vs. Accuracy
4. **Schema-normalisierte Entropy zeigt Underutilization** — aktuelles Schema captures nicht alle Nuancen; Schema-Free-Variante (EDC-Paradigma) als Future Work

## Zukunftsarbeiten der Autoren

- **Schema-Free KG + EDC-Paradigma** — Schemata per LLM entdecken statt vordefinieren
- **Temporal Knowledge Graphs** — zeitvarianter KG für Event-Reihen und Causal-Reasoning (Anknüpfung an FinDKG, Li/Passino 2024)
- **Enhanced LLM-as-a-Judge** — Reasoning-Modelle (o1-Familie) als Judges evaluieren
- **Table-Aware Serialization** — dedicated Modul für Markdown-Tabellen; kleinere LLMs extrahieren zu konservativ aus strukturierten Tabellen

## Abgrenzung — Was FinReflectKG NICHT liefert

- **Keine Trading-Strategie** — reine Infrastruktur-Arbeit (Daten + Evaluations-Framework)
- **Kein Backtest** — orthogonal zu FINSABER/GT-Score/Bailey-Validation
- **Keine Insider-Transaktions-Analyse** — 10-K-Inhalt, nicht Form-4
- **Keine Produktions-Deployment-Blaupause** — Qwen2.5-72B + 3-Stage-LLM-Loop hat hohe Inferenz-Kosten

## Backlinks

- [[Labre-2025-FinReflectKG-Companion]] — Praktiker-Lens (towardsai Blog zum selben Paper)
- [[Knowledge-Graph-Finance-Architecture]] — Konzeptseite (KG-Struktur für Finance)
- [[Agentic-Reflection-Pattern]] — Konzeptseite (Critic-Corrector-Loop)
- [[LLM-as-a-Judge-Evaluation]] — Konzeptseite (Ground-truth-agnostic Evaluation)
- [[Knowledge-Graph-Architektur-Roadmap]] — neue Synthesis v0.1 (Entscheidungsvorlage)
- [[insider-intelligence]] — Skill, für den diese Architektur-Frage relevant ist
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B21
- [[Abhinav Arun]], [[Fabrizio Dimino]], [[Tejas Prakash Agarwal]], [[Bhaskarjit Sarmah]], [[Stefano Pasquali]] — Author-Entities

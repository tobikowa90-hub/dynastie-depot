---
title: "Knowledge-Graph-Finance-Architecture"
type: concept
tags: [knowledge-graph, finance-ai, sec-filings, schema, entity-extraction, relationship-modeling]
created: 2026-04-20
updated: 2026-04-20
sources: [Arun-et-al-2025-FinReflectKG, Labre-2025-FinReflectKG-Companion]
related: [Agentic-Reflection-Pattern, LLM-as-a-Judge-Evaluation, RAG-Uncertainty-Quantification, Knowledge-Graph-Architektur-Roadmap, insider-intelligence]
wissenschaftlicher_anker: "Arun, Dimino, Agarwal, Sarmah, Pasquali (2025) — FinReflectKG; Labre (2025) — Companion-Commentary"
konfidenzstufe: methoden-referenz
---

# Knowledge-Graph-Finance-Architecture

> **Konzept-Framework für strukturierte Knowledge-Graphs aus Finance-Dokumenten (SEC-Filings, News, Earnings-Calls). 5-tupel-Triples + schema-guided Extraction + hybride Evaluation. Nicht zu verwechseln mit General-Domain-KGs oder reinem Dense-Retrieval.**

## Kern-Idee

Finance-KGs unterscheiden sich von General-KGs (z.B. Wikidata) durch:

1. **Regulierte Dokumenten-Basis** — SEC-Filings, nicht beliebiger Text
2. **Business-aligned Schema** — SME-approved Entity/Relation-Typen (ORG, FIN_METRIC, RISK_FACTOR, ESG_TOPIC vs. Freitext-Relations)
3. **Closed Information Extraction** — Schema constraint ist bewusste Designentscheidung, reduziert Noise
4. **Tabellen-Sensitivität** — Quantitative Disclosures in Tabellen sind oft wichtiger als Narrativ-Text
5. **Audit-Trail-Pflicht** — Triple-Provenienz zurück zur Quelle (regulatorisch, EU AI Act / SEC transparency)

## Schema-Design-Primitive (aus FinReflectKG)

### Entity-Types (Auswahl)

| Type | Definition | Beispiel |
|---|---|---|
| ORG | Filing-Company (Issuer) | AAPL, MSFT |
| COMP | Externe Unternehmen (Competitors, Suppliers, Customers) | TSMC in Apple-10-K |
| PERSON | Key-Individuals (CEO, CFO, Board) | Tim Cook, Satya Nadella |
| SEGMENT | Interne Divisions | Cloud-Segment, North America Retail |
| FIN_METRIC | Numerische Metriken | Revenue, EBITDA, CapEx |
| RISK_FACTOR | Dokumentierte Risiken | Supply-Chain-Risk, Regulatory-Risk |
| EVENT | Material-Events | Pandemien, M&A |
| REGULATORY_REQUIREMENT | Regulationen | Basel III, GDPR |
| ESG_TOPIC | ESG-Themen | Carbon Emissions, DEI |

### Relationship-Types (Auswahl)

`Has_Stake_In` / `Operates_In` / `Produces` / `Impacts` / `Impacted_By` / `Discloses` / `Complies_With` / `Supplies` / `Partners_With`

## 5-Tuple-Form

$$(\text{Head Entity, Head Type, Relationship, Tail Entity, Tail Type})$$

Beispiel: `(NVDA, ORG, Impacted_By, supply chain disruptions, RISK_FACTOR)`

Das Entity-**Type**-Feld ist zusätzlich zur Entity-Identifikation — verhindert falsche Relation-Disambiguation und ermöglicht schema-basiertes Reasoning downstream.

## Architektonische Trade-offs

### Closed-Schema vs. Schema-Free

| Closed-Schema (FinReflectKG aktuell) | Schema-Free (EDC-Paradigma, Zhang & Soh 2024) |
|---|---|
| ✅ Interpretierbar, audit-fähig | ✅ Flexibel, captures unerwartete Nuancen |
| ✅ Niedriger Noise | ❌ Höhere semantische Fragmentierung |
| ❌ Underutilization (Schema-normalisierte Entropy 0,63/0,89 bei Reflection) | ✅ Bessere Coverage |
| ✅ Business-Relevanz erzwungen | ❌ SME-Validierung schwieriger |

FinReflectKG's Future Work: Hybrid-Pipeline mit EDC-Integration für private Datenquellen, bei denen Schema nicht a priori definierbar ist.

### Tabellen-aware-Chunking vs. Naive-Sliding-Window

Tabellen in 10-K-Filings encodieren oft die **wichtigsten quantitativen Disclosures** (Segment-Revenue, Finanzmetriken, Risk-Breakdowns). Naive-Chunking fragmentiert Tabellen → Spalten-Row-Assoziationen gehen verloren → Extraction-Qualität fällt massiv.

**Architektonischer Fix (Docling + Table-Aware-Chunking):** Tabellen als **atomic Markdown-Chunks** behandeln, max. Chunk-Size 2048 Tokens. Verhindert Tabellen-Split, erhält Kontext.

## Abgrenzung zu FinDKG (Li & Passino 2024)

| FinDKG (2024) | FinReflectKG (2025) |
|---|---|
| Basis: News-Feeds | Basis: SEC 10-K (authoritative) |
| Dynamisch, temporal-variant | Statisch pro Filing-Jahr (temporal-Extension future work) |
| Fine-tuned LLM-Pipeline | Schema-guided Prompt-Engineering (Qwen2.5-72B) |
| Event-Quadruples | 5-Tuples mit expliziten Entity-Types |

Komplementär: News → Event-zentriert, Filings → Entity/Relation-zentriert.

## Anwendung auf Dynasty-Depot

**Heute: keine operative Nutzung.** DEFCON extrahiert Fundamentals aus strukturierten APIs (defeatbeta, Shibui, Yahoo), nicht aus 10-K-KG.

**Entscheidungsvorlage:** [[Knowledge-Graph-Architektur-Roadmap]] v0.1 dokumentiert, unter welchen Bedingungen eine KG-Integration wertvoll würde:

| Use-Case | KG-Mehrwert | XML-Direkt-Parsing reicht |
|---|---|---|
| Form-4 Insider-Transactions | ❌ Overkill (XML strukturiert) | ✅ |
| 10-K MD&A / Risk Factors | ✅ (Narrativ, Entity-Extraction nötig) | ❌ |
| Cross-Entity-Queries (Supplier-Cluster) | ✅ (Multi-Hop) | ❌ |
| Einzel-Metrik-Lookup (Revenue, FCF) | ❌ (API reicht) | ✅ |

## Dos & Don'ts

**Do:**
- Schema an Business-Use-Case anpassen (SME + LLM kollaborativ)
- Tabellen atomic halten
- Evaluation: CheckRules + Coverage + LLM-as-a-Judge kombinieren

**Don't:**
- KG für strukturierte XML-Daten (Form-4) bauen — Over-Engineering
- Single-Pass-Extraction als Produktionsstandard ohne Reflection-Loop akzeptieren (42% All-Rules-Compliance)
- Entropy-Reduktion ignorieren (siehe Labre 2025 Diversity-Monitor)

## Backlinks

- [[Arun-et-al-2025-FinReflectKG]] — primäre Source
- [[Labre-2025-FinReflectKG-Companion]] — Praktiker-Lens
- [[Agentic-Reflection-Pattern]] — Extraction-Methode
- [[LLM-as-a-Judge-Evaluation]] — Evaluations-Methode
- [[RAG-Uncertainty-Quantification]] — komplementäres Konzept (Retrieval statt Extraction)
- [[Knowledge-Graph-Architektur-Roadmap]] — Entscheidungsvorlage
- [[insider-intelligence]] — Skill, für den diese Architektur-Frage relevant ist

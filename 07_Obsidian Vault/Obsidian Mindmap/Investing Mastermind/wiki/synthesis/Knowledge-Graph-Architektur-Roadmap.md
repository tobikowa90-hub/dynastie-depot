---
title: "Knowledge-Graph-Architektur-Roadmap"
type: synthesis
tags: [knowledge-graph, architektur, entscheidungsvorlage, insider-intelligence, 10-k, form-4, rag, roadmap]
created: 2026-04-20
updated: 2026-04-20
version: v0.1
status: draft-frozen
re_review_trigger: "Konkreter Cross-Entity-/10-K-Narrativ-Bedarf ODER Score-Archiv-Interim-Gate 2026-10-17 (whichever first)"
sources: [Arun-et-al-2025-FinReflectKG, Labre-2025-FinReflectKG-Companion, Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]
related: [Knowledge-Graph-Finance-Architecture, Agentic-Reflection-Pattern, RAG-Uncertainty-Quantification, LLM-as-a-Judge-Evaluation, insider-intelligence, dynastie-depot-skill, Backtest-Methodik-Roadmap]
wissenschaftlicher_anker: "FinReflectKG (Arun et al. 2025) + Labre-Companion (2025) + Bayesian RAG (Ngartera et al. 2026) — drei komplementäre Papers zur Finance-KG/RAG-Architektur"
konfidenzstufe: synthese-entscheidungsvorlage
---

> **Status (2026-04-20 Nacht):** `draft-frozen` — inhaltliche Schlussfolgerungen gelten faktisch (Szenario 1 Form-4 XML bleibt, Szenario 3 Bayesian-RAG-Briefing-Rewrite verworfen, Szenario 2 10-K-KG bleibt `future-arch`), aber keine formale v1.0-Ratifikation ohne Usage-Evidence. Codex-Verdikt Option D (siehe CORE-MEMORY §1 Meilenstein 2026-04-20 Nacht). Re-Review-Trigger: konkreter Cross-Entity-/10-K-Narrativ-Bedarf ODER Score-Archiv-Interim-Gate **2026-10-17** (whichever first). Q1-Q3 bleiben explizit offen, nicht release-blockierend.

# Knowledge-Graph-Architektur-Roadmap

> **Entscheidungsvorlage: Wann bringt eine Knowledge-Graph-Komponente Mehrwert für Dynasty-Depot, wann reicht direktes Parsen / strukturiertes API-Fetching? Und wann wäre Bayesian RAG eine Alternative zu KG? Anti-Over-Engineering-Gate für zukünftige Skill-Erweiterungen.**

## Grundfrage

Dynasty-Depot arbeitet heute mit:

- Strukturierte APIs (defeatbeta, Shibui-SQL, Yahoo) für Fundamentals
- XML-Parsing für Form-4 Insider-Filings (`insider-intelligence` Skill)
- Manuelle Kurationen für Analyst-Consensus, Moat-Rating
- Tavily-RAG für News/Earnings im Morning-Briefing (deterministic embeddings, kein uncertainty-aware retrieval)

**Nach dem 6-Paper-Ingest Phase 1 (FINSABER + GT-Score + FinReflectKG + Labre + Bayesian RAG + FinDPO) liegt auf dem Tisch:** Gibt es einen Use-Case, der KG- oder Bayesian-RAG-Architektur **erzwingt** oder **signifikant verbessert**?

## Entscheidungs-Matrix (Use-Case → Architektur-Wahl)

| Use-Case | Heutige Architektur | KG-Mehrwert | Bayesian-RAG-Mehrwert | Empfehlung |
|---|---|---|---|---|
| **Form-4 Insider-Pflichtdaten** | XML-Direkt-Parsing | ❌ Over-Engineering | ❌ keine Retrieval-Aufgabe | **Status quo** |
| **Einzel-Metrik-Lookup (Revenue, FCF)** | API-Fetch | ❌ | ❌ | **Status quo** |
| **Moat-Rating (manuell)** | Curated (Morningstar) | ❌ | ❌ | **Status quo** |
| **Analyst-Consensus-Check** | Web-UI / Yahoo | ❌ | ❌ | **Status quo** |
| **10-K MD&A Narrativ-Extraktion** (heute nicht genutzt) | — | ✅ (Entity-Graph) | ✅ (Retrieval für QA) | **Kein Pfad ohne Sinnstiftung** |
| **Cross-Entity-Queries (Supplier-Cluster, ESG-Themen)** (heute nicht genutzt) | — | ✅ (Multi-Hop) | ⚠️ (limitiert) | **Kein Pfad ohne konkreten Analyse-Bedarf** |
| **Morning-Briefing Quality-Signal** | Tavily deterministic | ⚠️ (overkill) | ✅ (Soft-Alert-Parallele) | **Bleib bei n.v.-Markierung + Soft-Alert-Schema; kein Rewrite** |
| **Form-4-Cross-Reference mit 10-K** (hypothetisch) | — | ✅ (Multi-Doc-Joins) | ⚠️ | **FUTURE — prüfen bei konkretem Bedarf** |

## Die drei Architekturen im Vergleich

### A. Strukturierter-Daten-Parsing (heute)

**Wo sinnvoll:** Form-4 XML, SEC-API, Shibui-SQL, Yahoo-API.

**Eigenschaften:**
- Schnellste, zuverlässigste Methode
- Keine LLM-Kosten
- Audit-Trail trivial (Raw-Data verfügbar)
- **Limitation:** Nur nutzbar, wenn Schema von Quelle vorgegeben und stabil

**Verdikt für Dynasty-Depot:** Bleibt Primär-Architektur für alle strukturierbaren Daten.

### B. Knowledge-Graph-Extraction (FinReflectKG-Pattern)

**Wo sinnvoll:** Narrative Dokumente (10-K MD&A, Earnings-Call-Transcripts, Analyst-Reports) — WENN Cross-Entity-Queries über mehrere Dokumente hinweg nötig sind.

**Eigenschaften:**
- Agentic-Reflection-Pattern gewinnt über Single-Pass (+22,5pp All-Rules-Compliance)
- Entropy-Drift-Monitoring Pflicht (Labre)
- LLM-as-a-Judge-Evaluation für Quality-Assessment
- **Limitation:** 2-3× Inferenz-Cost pro Chunk; nicht realtime-fähig

**Verdikt für Dynasty-Depot:**
- **Form-4:** ❌ nicht gerechtfertigt — XML reicht
- **10-K-Narrative:** offen — heute kein operativer Bedarf, aber nicht ausgeschlossen für 2028+

### C. Uncertainty-Aware Retrieval (Bayesian RAG)

**Wo sinnvoll:** Frage-Antwort-Systeme auf große Dokumenten-Corpora, bei denen Hallucination-Kosten hoch sind.

**Eigenschaften:**
- Epistemische Unsicherheit $\sigma_i$ ergänzt Mean-Relevance $\mu_i$
- In-Scoring statt post-hoc Kalibrierung
- 15ms Latency produktionsreif
- **Limitation:** braucht Self-hosted Embedding-Modelle (MC-Dropout configurable)

**Verdikt für Dynasty-Depot:**
- **Morning-Briefing heute:** ❌ nicht gerechtfertigt — v3.0.3 Soft-Alert + n.v.-Markierung erreicht äquivalente Transparenz mit 3-Quellen-Triangulation
- **Zukunfts-QA-Modul:** offen

## Qualitäts-Gates für jede zukünftige KG-/RAG-Erweiterung

Vor einer Architektur-Erweiterung muss folgendes erfüllt sein:

### Gate 1: Sinnhaftigkeits-Check

1. **Konkrete Frage, die heute nicht beantwortbar ist?** — z.B. "welche Satelliten haben Zulieferer-Exposure zu TSMC?", dann ja. Bei spekulativer "könnte vielleicht nützlich sein" → nein.
2. **Wiederkehrender Bedarf?** — einmalige Ad-hoc-Frage rechtfertigt keine Infrastruktur.
3. **Kein API-Fetch-Ersatz möglich?** — z.B. Yahoo hat Sektor-Daten; dann API, nicht KG.

### Gate 2: Operationalisierungs-Check

1. **Self-hosted-Capability verfügbar?** — Bayesian RAG braucht Dropout-Model-Weights; Tavily/OpenAI-APIs sind raus.
2. **Evaluation-Plan definiert?** — LLM-as-a-Judge-Pattern + CheckRules + Entropy-Monitor.
3. **Maintenance-Budget realistisch?** — KG braucht Re-Extraction bei jedem neuen Filing (quarterly/annual) + Schema-Evolution.

### Gate 3: Anti-Over-Engineering-Check

1. **Codex-Review Pflicht** (memory `feedback_codex_over_advisor.md`): Jede Architektur-Erweiterung braucht externe Bestätigung gegen Own-Bias ("LLM-Hype-FOMO").
2. **3-Monats-Observation-Period:** Vor Produktions-Adoption: 3 Monate Parallelbetrieb mit bestehender Architektur.
3. **Rollback-Plan:** Jede Erweiterung muss ohne Daten-/State-Verlust zurücknehmbar sein.

## Drei konkrete Szenarien für Phase 2 (nach 6-Paper-Ingest Hard-Checkpoint)

### Szenario 1: "Insider-Intelligence bleibt auf Form-4 XML"

- **Status:** aktuell
- **Entscheidung:** ✅ bleibt
- **Codex Round 2 (Abend 2026-04-20):** FinReflectKG aus 🔴- auf 🟡-Cluster verschoben, weil Form-4 bereits XML = kein KG-Use-Case

### Szenario 2: "Neue Skill: 10-K-KG für Cross-Entity-Analyse"

- **Status:** hypothetisch, nicht priorisiert
- **Auslöser:** konkrete wiederkehrende Frage, die Form-4 + API nicht beantwortet (z.B. "welche Satelliten nennen China-Supply-Chain in Risk-Factors?")
- **Architektur-Empfehlung:** FinReflectKG-Pattern (Reflection-Modus) + Labre-Entropy-Monitor + LLM-as-a-Judge-Evaluation
- **Realistischer Zeitrahmen:** frühestens 2027+
- **Entscheidungsgate Phase 2.5:** Codex-Skill-Audit-Gate (wie im Handover angekündigt)

### Szenario 3: "Morning-Briefing v3.2 — Bayesian RAG auf Tavily-Output"

- **Status:** hypothetisch, blockiert durch Tavily-API-Limitation
- **Blockade:** Tavily gibt keine Embeddings + keine Dropout-Config; kein MC-Dropout möglich
- **Workaround:** nur bei Wechsel auf selbst-gehostete Embeddings (BGE, Sentence-BERT) — großer Aufwand
- **Entscheidung:** ❌ aktuell nicht verfolgen; v3.0.3 Soft-Alert-Schema ist ausreichend

## Track-5-Spezifische Reflektion (nachträgliche Cross-Prüfung)

Die beiden Pre-Paper-Pläne (Track 5a EDGAR + Track 5b FRED) werden durch 6-Paper-Ingest nicht obsolet, aber im Licht geprüft:

| Track | Vor-Paper-Ingest | Post-Paper-Ingest (inkl. Phase 1b Einordnung) |
|---|---|---|
| **5a EDGAR-Skill-Promotion** | Klassischer Scraper | FinReflectKG zeigt, dass KG-Alternative machbar — aber nicht empfohlen für Dynasty-Depot (Form-4-Fokus reicht). 5a bleibt. |
| **5b FRED Macro-Regime-Filter** | Regime-Detection als Pre-Decision-Layer | FINSABER (B19) + GT-Score (B20) verstärken wissenschaftlichen Anker. Phase-1b-Papers sind **orthogonal** — keine Änderung. |

## Offene Fragen (explizit adressiert in Phase 2 oder später)

> **Governance-Hinweis (2026-04-20 Nacht):** Alle drei Fragen sind **heute ungeklärt, aber nicht release-blockierend**. Sie adressieren Architektur-Entscheidungen, die erst bei konkretem Trigger-Event (Szenario 2 / 3 oder externer Konsumption) sinnvoll beantwortbar sind. Heutige Antworten wären spekulativ. Re-Evaluation am Re-Review-Trigger (siehe Frontmatter).

1. **Wann ist ein Dataset groß genug für einen KG-Ansatz?** — FinReflectKG nutzt S&P-100 × 10-K = ~100 Dokumente. Dynasty-Depot hat 11 Satelliten + 9 Ersatzbank = 20 Dokumente. **Zu klein für eigenen KG, aber genug für Konsumption eines externen KG** (z.B. FinReflectKG-Dataset selbst). *Status: ungeklärt, nicht release-blockierend — braucht konkreten Konsumptions-Use-Case.*
2. **Lizenz-/Legal-Fragen bei LLM-Extraction aus SEC-Filings:** SEC-Filings sind Public Domain, aber Extraktionen könnten Copyright-Implikationen haben. **Zu klären vor Produktion.** *Status: ungeklärt, nicht release-blockierend — braucht Produktions-Intent (Szenario 2-Aktivierung).*
3. **Integration mit bestehendem Score-Archiv (`score_history.jsonl`):** Falls KG-Befunde in DEFCON einfließen, wie werden sie versioniert? **Offene Design-Frage.** *Status: ungeklärt, nicht release-blockierend heute — aber Design-Klarheit Pflicht vor operativer KG-Adoption (Point-in-Time-Append-only-Natur von `score_history.jsonl` + strikte §18/§28.2 Sync-Regeln).*

## Versions-Historie

| Version | Datum | Änderung |
|---|---|---|
| v0.1 | 2026-04-20 | Erstellt aus 6-Paper-Ingest Phase 1b. Drei Architekturen (A/B/C), Entscheidungsmatrix pro Use-Case, drei Qualitäts-Gates, drei konkrete Szenarien. Codex Round 2 Verdikte einbezogen. |
| v0.1 `draft-frozen` | 2026-04-20 Nacht | Status-Markierung: keine v1.0-Ratifikation ohne Usage-Evidence. Szenario 1+3 faktisch bestätigt, Szenario 2 als `future-arch` mit Re-Review-Trigger. Q1-Q3 bleiben ungeklärt, explizit nicht release-blockierend. Codex-Verdikt Option D (Opus 4.7 + Codex Combined Review). |

## Backlinks

- [[Arun-et-al-2025-FinReflectKG]] — primäre Source (KG-Architektur B)
- [[Labre-2025-FinReflectKG-Companion]] — Praktiker-Caveats (Entropy-Monitor)
- [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]] — primäre Source (RAG-Architektur C)
- [[Knowledge-Graph-Finance-Architecture]] — Konzeptseite (KG-Primitive)
- [[Agentic-Reflection-Pattern]] — Extraction-Methode für KG
- [[RAG-Uncertainty-Quantification]] — Alternative-Architektur (C statt B)
- [[LLM-as-a-Judge-Evaluation]] — Evaluations-Methode (Gate 2)
- [[insider-intelligence]] — Skill, zu dem die Szenarien 1+2 Stellung nehmen
- [[dynastie-depot-skill]] — Haupt-Skill, bleibt architektonisch unberührt
- [[Backtest-Methodik-Roadmap]] — parallele Synthesis (Backtest-Gate statt Architektur-Gate)

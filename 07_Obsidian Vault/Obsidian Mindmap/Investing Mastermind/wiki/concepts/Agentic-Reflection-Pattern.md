---
title: "Agentic-Reflection-Pattern (Critic-Corrector-Loop)"
type: concept
tags: [agentic-llm, self-reflection, critic-corrector, multi-agent, iterative-refinement, reflexion]
created: 2026-04-20
updated: 2026-04-20
sources: [Arun-et-al-2025-FinReflectKG, Labre-2025-FinReflectKG-Companion]
related: [Knowledge-Graph-Finance-Architecture, LLM-as-a-Judge-Evaluation, LLM-Investing-Bias-Audit, Knowledge-Graph-Architektur-Roadmap]
wissenschaftlicher_anker: "Arun et al. (2025) — FinReflectKG Section 4.3.3; Inspiriert von Reflexion (Shinn et al. 2023, Li et al. 2024)"
konfidenzstufe: methoden-standard
---

# Agentic-Reflection-Pattern (Critic-Corrector-Loop)

> **Generisches Multi-Agent-Pattern: Extraction-LLM → Feedback-LLM (Critic) → Correction-LLM → Stopp bei leerem Issue-Set. Anwendbar über Finance-KG hinaus — überall, wo LLM-Output strukturell validierbar ist.**

## Kern-Idee

Klassische LLM-Extraction (Single-Pass) liefert oft plausible, aber unvollständig schema-konforme Outputs. Das **Agentic-Reflection-Pattern** trennt die Rollen:

1. **Extraction-LLM** — generiert initialen Output (breit, keinste Sorge um Schema-Compliance)
2. **Feedback-LLM (Critic)** — prüft Output gegen Schema + Business-Regeln; emittiert strukturiertes JSON mit Issues + Suggestions
3. **Correction-LLM** — wendet Suggestions an; produziert refined Output
4. **Stopp** bei $F_c^{(t)} = \emptyset$ (keine Issues mehr) oder $t = n_{max}$

## Formaler Loop

Für Chunk $c$, Schema $S$, Reflection-Mode $\phi_{re}$:

$$T_c^{(1)} = \text{Extract}(c, S, \phi_{re})$$
$$F_c^{(t)} = \text{Feedback}(c, T_c^{(t-1)}, S, \phi_{re})$$
$$T_c^{(t)} = \text{Correct}(c, T_c^{(t-1)}, F_c^{(t)}, S, \phi_{re})$$

## Struktur des Feedback-JSON

Aus FinReflectKG Box 4.1:
```json
{
  "triple_number": "Triple N",
  "triple": ["We", "ORG", "Impacted_By", "supply chain disruptions", "RISK_TYPE"],
  "issue": "Indirect reference to an entity in the triple. RISK_TYPE is not a valid preconfigured category",
  "suggestion": "replace We with NVDA as this information comes from Nvidia's 10-K file; substitute RISK_TYPE with RISK_FACTOR from the configured entity types"
}
```

## Empirische Effekte (Finance-KG-Domain)

| Metrik | Single-Pass | Reflection | Δ |
|---|---|---|---|
| Relationship-Schema-Compliance | 64,6% | 84,2% | +19,6pp |
| Alle 4 CheckRules gleichzeitig | 42,3% | 64,8% | +22,5pp |
| Triples/Chunk | 13,3 | 15,8 | +18,8% |
| Entity-Coverage-Ratio | 0,30 | 0,53 | +77% |

**Kosten:** 2-3× Inferenz-Runden (Critic + Correction). Nicht geeignet für Realtime-Szenarien (News-Feeds mit Sub-Sekunden-Latenz).

## Das Reflection-Entropy-Paradox (Labre 2025)

Reflection erreicht höhere Coverage, aber **geringere semantische Diversität** (Shannon Relationship-Entropy: 5,54 → 4,32, -22%).

**Interpretation:** Critic-LLM kanonisiert aggressiv — `supplies`, `is supplier of`, `provides to` → alle gemappt auf `Supplies`. Das ist korrekt gemäß Schema, reduziert aber implizit die Graph-Varianz. **Risiko:** Seltene, aber semantisch legitime Unterschiede verloren.

**Labre's Mitigation (Vorschlag):** Pre-Correction-Entropy-Check; bei >X% Entropy-Drop gegen Multi-Pass-Baseline → Feedback-Prompt lockern.

## Abgrenzung zu "Chain-of-Thought" (CoT)

| CoT (Wei et al. 2022) | Agentic-Reflection |
|---|---|
| Single-LLM, einmalig, linear | Multi-LLM, iterativ, zyklisch |
| "Denke Schritt für Schritt" | "Extrahiere → Kritisiere → Korrigiere → bis leer" |
| Verbessert Reasoning-Qualität | Verbessert Struktur-Compliance |
| Ad-hoc, kein State | Persistenter Issue-Stack |

CoT und Agentic-Reflection sind **orthogonal kombinierbar** — Extraction-LLM kann intern CoT nutzen, das Reflection-Pattern ergänzt die inter-LLM-Koordination.

## Generalisierbarkeit jenseits Finance-KG

Das Pattern ist anwendbar, wo ein formales Validierungs-Schema existiert:

- **Code-Generation:** Extractor schreibt → Linter-LLM kritisiert → Fixer-LLM repariert
- **Structured-Data-Extraction:** generic ETL mit Schema-Checks
- **Regulatorische-Compliance-Prüfung:** Draft → Rule-Check → Revision
- **Financial-Report-Generation:** Data → Narrative → Fact-Check → Revision

**Limitations:** Funktioniert nur, wenn Schema/Regeln explizit kodifizierbar sind. Bei offenem Kreativ-Output (z.B. "schreibe gutes Essay") hat Critic keine klare Prüfbasis.

## Anwendung auf Dynasty-Depot (heute: null)

DEFCON-Scoring ist regelbasiert, nicht LLM-Extraction. Kein direkter Anwendungsfall.

**Hypothetisch:** Bei zukünftiger Integration einer 10-K-KG-Pipeline (siehe [[Knowledge-Graph-Architektur-Roadmap]]) wäre Agentic-Reflection die empfohlene Extraction-Architektur — mit Labre-Entropy-Monitor als Qualitäts-Gate.

## Dos & Don'ts

**Do:**
- Schema-Validierung explizit kodifizieren (CheckRules)
- Feedback als strukturiertes JSON (nicht Freitext)
- Stopp-Kriterien definieren (leerer Issue-Set oder max-Iterations)
- Entropy-Drift monitoren (Labre-Caveat)

**Don't:**
- Reflection als Allheilmittel für schlechte Extraction-Prompts nutzen (löst symptomatisch, nicht strukturell)
- Bei Realtime-Anforderungen Reflection einsetzen (zu hoher Latency-Cost)
- Single-Pass-Output ohne Compliance-Check produktionsstellen

## Backlinks

- [[Arun-et-al-2025-FinReflectKG]] — Quelle (Section 4.3.3)
- [[Labre-2025-FinReflectKG-Companion]] — Entropy-Paradox + Mitigation
- [[Knowledge-Graph-Finance-Architecture]] — Ziel-Architektur
- [[LLM-as-a-Judge-Evaluation]] — komplementäre Methode (Output-Evaluation statt Extraction)
- [[LLM-Investing-Bias-Audit]] — Querbezug: Audit-Pattern auch für Selection-Strategies

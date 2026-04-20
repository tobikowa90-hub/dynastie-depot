---
title: "LLM-Preference-Optimization-Finance (DPO statt SFT)"
type: concept
tags: [dpo, direct-preference-optimization, sft, llm-alignment, llama-3, lora, finance-sentiment]
created: 2026-04-20
updated: 2026-04-20
sources: [Iacovides-Zhou-Mandic-2025-FinDPO]
related: [Sentiment-Strength-Logit-Extraction, LLM-Investing-Bias-Audit, News Sentiment Analysis, Li-Kim-Cucuringu-Ma-2026-FINSABER]
wissenschaftlicher_anker: "Iacovides, Zhou, Mandic (2025) — FinDPO Paper; Rafailov et al. (2023) — Original DPO; Chu et al. (2025) — SFT Memorizes / RL Generalizes"
konfidenzstufe: methoden-referenz
---

# LLM-Preference-Optimization-Finance (DPO statt SFT)

> **Post-Training-Alignment via Direct Preference Optimization — RL-frei, ressourcen-effizient, besser generalisierend als Supervised Fine-Tuning. Finance-spezifische Anwendung via FinDPO (Llama-3-8B + LoRA, Imperial College).**

## Kern-Idee

Klassisches Post-Training für Finance-LLMs: **Supervised Fine-Tuning (SFT)** — Maximiere Likelihood der Ground-Truth-Antwort auf gelabelten Paaren (Input-Text, Sentiment-Label). Funktioniert, aber führt zu **Memorization-Tendenz** (Chu et al. 2025: "SFT Memorizes, RL Generalizes").

**DPO (Rafailov et al. 2023):** Optimiere direkt auf Präferenz-Paaren (preferred, dispreferred) — ohne Reward-Model, ohne RL-Komplexität. DPO-Loss:

$$\mathcal{L}_{DPO} = -\mathbb{E}\left[\log\sigma\left(\beta \cdot \left(\log\frac{\pi_\theta(y^w|\tilde{x})}{\pi_{ref}(y^w|\tilde{x})} - \log\frac{\pi_\theta(y^l|\tilde{x})}{\pi_{ref}(y^l|\tilde{x})}\right)\right)\right]$$

**Intuition:** Erhöhe Wahrscheinlichkeit der preferred Response $y^w$, senke dispreferred $y^l$. $\beta$ = KL-Divergenz-Strafe ggü. Reference-Model.

## Drei Ansätze im Vergleich

| Methode | Training-Ziel | Generalisierung | Compute | Stabilität |
|---|---|---|---|---|
| **SFT / Instruction-Tuning** | Max. Likelihood Ground-Truth | Memorization-Risiko | Mittel | Hoch |
| **RLHF (PPO/REINFORCE)** | Max. Reward – KL(π‖π_ref) | Gut | **Sehr hoch** (Reward-Model-Training) | Instabil |
| **DPO** | Loss über preferred/dispreferred Paare | Gut (empirisch) | Mittel | Stabil |

DPO "implicitly optimizes the same objective as RLHF" (Rafailov 2023), aber in geschlossener Form ohne Reward-Model.

## FinDPO-spezifische Entscheidungen

1. **Base-Model:** Llama-3-8B-Instruct (ref. policy $\pi_{ref}$)
2. **LoRA-Fine-Tuning:** $r=16$, $\alpha=16$, Dropout 0,05 → 41,9M trainierbare Parameter (0,52% des Base-Models)
3. **Hardware:** Einzelne A100 40GB, 4,5h Training
4. **Preference-Pair-Generation:** Ground-Truth-Label = preferred; Random-Wrong-Label ODER Policy-Prediction-wenn-falsch = dispreferred
5. **Datasets:** FPB (4.840 Samples) + TFNS (11.930) + NWGI (16.200) = 32.970 Pairs

## Empirische Überlegenheit (FinDPO)

| Benchmark | SFT SOTA (FinGPT v3.3) | FinDPO | Δ |
|---|---|---|---|
| FPB F1 | 0,879 | 0,865 | -1,4pp |
| TFNS F1 | 0,903 | 0,872 | -3,1pp |
| NWGI F1 | 0,643 | **0,833** | **+19pp** |
| **Average** | **0,762** | **0,846** | **+11%** |

**Interpretation:** FinDPO ist nicht durchgängig besser auf allen Benchmarks, aber **deutlich besser bei NWGI** (dem realistischsten der drei Datasets: 16.200 längere Finanz-News-Artikel, nicht kurze Tweets). Das ist konsistent mit der Generalisierungs-Hypothese — DPO-Modelle **extrapolieren** besser auf schwierigere/größere Samples.

## Warum "Finance"-spezifisch?

Preference-Optimization ist domain-agnostic, aber Finance hat spezifische Anforderungen:

1. **Nuancierte Sprache** — "beat expectations" vs. "missed guidance" sind struktur-ähnlich, aber polar sentiment-gegenteilig
2. **Generalisation auf unerwartete Events** — Finance-Markte produzieren regelmäßig Ereignisse, die nicht im Training-Set waren (COVID, Silicon-Valley-Bank-Run, etc.)
3. **Quantitative Hinweise in Text** — "+5% YoY" vs. "down sharply" mischen Numerik und Narrativ
4. **Regulierter Output-Use** — Sentiment-Signal geht in Portfolio-Decisions, Auditpflicht

DPO's Robustheit gegen Memorization ist in Finance besonders wertvoll — der Markt präsentiert ständig Out-of-Distribution-Samples.

## Grenzfall: Overconfidence-Problem (Leng et al. 2025)

DPO-Modelle tendieren zu **Overconfidence** — ordnen preferred Klasse oft 100% Wahrscheinlichkeit zu, allen anderen 0%. FinDPO adressiert das explizit:

**Mitigation:** Temperature-Scaling (Guo et al. 2017) nach DPO-Training, kalibriert auf Training-Set (nicht Portfolio-Corpus — Data-Leakage-Vermeidung). Temperature-Parameter $T$ minimiert Negative-Log-Likelihood.

Das ermöglicht erst den Logit-to-Score-Konverter — siehe [[Sentiment-Strength-Logit-Extraction]].

## Anwendung auf Dynasty-Depot (heute: null)

**DEFCON ist Long-Only, kein Sentiment-Signal als Haupt-Faktor.** Block "Sentiment" = 10 von 100 Pt., manuell via Analyst-Konsensus + PT-Abstand + Sell-Ratio. DPO-Pipeline wäre **Overkill** für diese Dimension.

**Hypothetischer Zukunfts-Use-Case (2028+):**

- Analyst-Report-Sentiment automatisieren (heute manuelle Lesung der Consensus-Charts)
- News-Sentiment-Block als 4. Sub-Komponente im Sentiment-Block (aktuell fehlend)

**Hürden:**
- Finance-DPO-Modelle benötigen gelabelte Finance-Corpora (kostspielig für Non-US)
- FINSABER-Audit-Pflicht (B19) vor operativer Adoption
- Transaction-Cost-Sensitivität nicht übertragbar auf Long-Only-Sparplan-Strategie

## Dos & Don'ts

**Do:**
- LoRA für Ressource-Effizienz (0,5-1% trainierbare Params reichen)
- Temperature-Scaling nach DPO-Training
- Preference-Pairs aus Policy-Errors generieren ("fehler-gesteuertes Training")

**Don't:**
- DPO ohne Out-of-Distribution-Evaluation als SOTA feiern (FINSABER-Pattern anwenden)
- DPO-Modelle ohne Kalibrierung in Portfolio einspeisen (Overconfidence → Over-Trading)
- Sentiment-Signal als Primärfaktor in Long-Only-Strategie (Sentiment ~1M Half-Life, Long-Hold >12M)

## Backlinks

- [[Iacovides-Zhou-Mandic-2025-FinDPO]] — primäre Source
- [[Sentiment-Strength-Logit-Extraction]] — komplementäres Konzept (Output-Nutzung)
- [[LLM-Investing-Bias-Audit]] — Validation-Pflicht vor Adoption (FINSABER-Pattern)
- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — Benchmark-Framework für LLM-Trading-Claims
- [[News Sentiment Analysis]] — bestehendes Konzept, wird durch DPO-Kontext erweitert

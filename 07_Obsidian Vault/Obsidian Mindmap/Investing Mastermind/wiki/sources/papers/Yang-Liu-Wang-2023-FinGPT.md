---
title: "FinGPT: Open-Source Financial Large Language Models"
date: 2023
type: source
subtype: academic-paper
tags: [llm-finance, open-source, data-centric-pipeline, finllm, lora, sentiment-analysis, source-only]
url: https://arxiv.org/abs/2306.06031
venue:
  conference: "International Symposium on Large Language Models for Financial Services (FinLLM 2023), IJCAI Workshop, 2023"
  preprint_v1: "arXiv:2306.06031v1, Juni 2023 (zur Konferenz-Submission)"
  preprint_v2: "arXiv:2306.06031v2, November 2025 (revidierte Fassung — Update gegenüber Conference-Version, enthält erweiterte Empirie)"
  citation_default: "Bei Zitation kanonisch die Konferenz-Fassung (FinLLM 2023 @ IJCAI) verwenden; arXiv-v2 nur bei expliziter Referenz auf revidierte Magnituden."
authors: "Hongyang Yang (AI4Finance Foundation), Xiao-Yang Liu (Columbia University), Christina Dan Wang (NYU Shanghai)"
status: processed
defcon_relevanz: "SOURCE-ONLY. Open-Source-Pendant zu BloombergGPT — End-to-End-Framework (5-Layer: Data Source / Engineering / LLMs / Tasks / Applications) für Finance-LLMs. Operative Konsequenz für DEFCON: KEINE direkte Score-Anbindung, weil DEFCON Long-Only ist und keine LLM-Sentiment-Pipeline als Hauptfaktor verwendet. **Konzeptioneller Wert:** Begründet Open-Source-Approach für künftige Finance-LLM-Adoption (Transparenz, Customization, Educational), gegenüber proprietären Black-Boxes. Komplementär zu FinDPO ([[Iacovides-Zhou-Mandic-2025-FinDPO]]) — FinGPT etabliert die Architektur, FinDPO refined das Training-Verfahren (DPO statt SFT). Beide gelten unter FINSABER-Bias-Audit (B19) erst als evidence-grade nach 20J-Hold-Out + Bull/Bear-Subsample-Test."
sources: []
related:
  - "[[Iacovides-Zhou-Mandic-2025-FinDPO]]"
  - "[[Jadhav-Mirza-2025]]"
  - "[[Li-Kim-Cucuringu-Ma-2026-FINSABER]]"
  - "[[LLM-Investing-Bias-Audit]]"
  - "[[news-sentiment-analysis|News Sentiment Analysis]]"
  - "[[DEFCON-System]]"
  - "[[Wissenschaftliche-Fundierung-DEFCON]]"
raw_path: "../../../raw/papers/Yang et al. (2023).pdf"
aliases:
  - "FinGPT 2023"
  - "Yang Liu Wang FinGPT"
  - "Open Source Finance LLM"
---

# Yang, Liu & Wang (2023) — FinGPT: Open-Source Finance LLM

## Abstract (eigene Worte)

Die AI4Finance Foundation präsentiert **FinGPT** — ein Open-Source-Framework für Finance-LLMs als Alternative zum proprietären BloombergGPT. Kern-Innovation: **data-centric approach** statt model-centric — automatic data curation pipeline + LoRA (Low-Rank Adaptation) für ressourceneffizientes Fine-Tuning. End-to-End-Framework in 5 Layern:

1. **Data Source Layer** — News, SEC Filings, Earnings Calls, Social Media, Market Data, Trends
2. **Data Engineering Layer** — Real-time NLP-Processing, Cleaning, Preprocessing, Tokenization
3. **LLMs Layer** — Base-Models (Llama, GPT, Falcon) + Domain-Adaptation via LoRA + RLHF
4. **Tasks Layer** — Sentiment Analysis, NER, Numerical Reasoning, Information Extraction, Summarization, RAG
5. **Applications Layer** — Robo-advising, Quant Trading, Fraud Detection, ESG Scoring, Credit Scoring, Education

Drei zentrale Finance-Spezifika, die generische LLMs nicht handhaben:

- **Hohe Temporal-Sensitivität** — Markt-Information-Window oft <1h; klassisches Pre-Train-Approach versagt
- **Konstante Dynamik** — Retraining-Frequenz wäre ökonomisch unbezahlbar; Adaptation-Layer-Approach (LoRA) löst das
- **Niedriger Signal-to-Noise** — Mehr Filtering und Information-Extraction nötig als General-Domain-LLMs

Open-Source-Begründung (jenseits Datenzugangs-Demokratisierung):

- **Transparenz** für Audit + Validierung
- **Customization** durch Researchers + Practitioners
- **Educational Value** — Studenten + Junior-Analysten lernen am Code
- **Forschungs-Beschleunigung** durch Community-Beiträge
- **Long-Term Robustness** durch dezentralen Maintenance

## DEFCON-Konsequenzen (zero direct, indirect Architecture)

### Was FinGPT NICHT für DEFCON ist

- **Kein Score-Element** — DEFCON hat keinen LLM-Sentiment-Pfad als Haupt-Faktor
- **Kein operativer Skill** — insider-intelligence + non-us-fundamentals + quick-screener sind klassische API-Wrapper, keine LLMs
- **Kein 2026-Adoption-Item** — DEFCON-Stack ist deterministisch optimiert, LLM-Layer ist Over-Engineering für 4-Min-Score-Routine

### Was FinGPT KONZEPTIONELL beiträgt

1. **Open-Source-Prinzip** als Selection-Filter für künftige LLM-Tooling-Adoption — bevor proprietäre Bloomberg-/OpenAI-Stacks evaluiert werden, soll Open-Source-Alternative betrachtet werden (siehe Memory `feedback_correctness_over_runtime.md`-Pattern: deterministisches und auditierbares Tooling first).

2. **Data-Centric-Architektur** als Anker für künftige Skill-Erweiterungen — Skill-Datenpipelines sollen Cleaning + Provenance + Versionierung explizit machen (analog zu video_ingest.py mit run.log + SHA256-Provenance).

3. **5-Layer-Trennung** als Design-Pattern — DEFCON's Skill-Architektur (dynastie-depot Hauptskill + Satelliten) ist analog 5-Layer (Data via Skills → Logic via SKILL.md-Workflows → Output via Briefing).

### Komplementarität zu FinDPO + FINSABER

```
FinGPT (B-was-eigentlich):  Architektur, Open-Source-Pipeline → "wie baut man ein Finance-LLM?"
FinDPO  (B24):               Training-Verfahren-Refinement      → "wie alignt man's besser?"
FINSABER (B19):              Bias-Audit-Framework               → "wie weiß man, ob's wirklich performt?"
```

→ Konzeptioneller Stack — keiner der drei ist allein operativ, alle drei zusammen wären Mindest-Infrastruktur falls künftig LLM-Sentiment-Pipeline gebaut werden soll. Aktuell: nicht priorisiert, kein Score-Pfad.

## Backlinks

- [[Iacovides-Zhou-Mandic-2025-FinDPO]] — Training-Refinement (B24)
- [[Jadhav-Mirza-2025]] — komplementäre LLM-Survey (B11)
- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — Bias-Audit (B19)
- [[LLM-Investing-Bias-Audit]] — Concept-Page
- [[news-sentiment-analysis|News Sentiment Analysis]] — operatives LLM-Anwendungsfeld
- [[DEFCON-System]] — kein direkter Score-Pfad
- [[Wissenschaftliche-Fundierung-DEFCON]] — Source-only-Quelle
- [[hongyang-yang|Hongyang Yang]], [[xiao-yang-liu|Xiao-Yang Liu]], [[christina-dan-wang|Christina Dan Wang]] — Author-Entities

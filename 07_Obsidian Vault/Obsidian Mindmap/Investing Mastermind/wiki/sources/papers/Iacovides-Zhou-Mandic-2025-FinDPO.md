---
title: "FinDPO: Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs"
date: 2025
type: source
subtype: academic-paper
tags: [sentiment-analysis, llm-finance, dpo, direct-preference-optimization, long-short-portfolio, algorithmic-trading, llama-3, transaction-costs]
url: https://arxiv.org/abs/2507.18417
venue: "arXiv preprint 2507.18417v1 (2025); Author affiliation: Imperial College London"
authors: "Giorgos Iacovides (Imperial), Wuyang Zhou (Imperial), Danilo Mandic (Imperial College London)"
status: processed
defcon_relevanz: "Keine DEFCON-Scoring-Änderung. Zwei indirekte Relevanzen: (1) Validation-Bezug zu FINSABER (B19): FinDPOs 67% p.a. Return bei 5bps Transaction Costs ist ein weiterer Datenpunkt im LLM-Investing-Benchmark-Raum — laut FINSABER verschwinden solche Outperformances oft bei 20-J/100+-Symbol-Replikation mit Bias-Mitigation. Hier gilt dies zu prüfen, bevor FinDPO als SOTA-Referenz zitiert wird. (2) Logit-to-Score-Idee als genereller Architektur-Anker: DPO-aligned LLMs können Continuous-Sentiment-Scores liefern statt nur Klassen — das ist für keine Dynasty-Depot-Komponente heute operativ relevant (DEFCON ist Long-Only, kein Sentiment-Signal als Haupt-Faktor), aber konzeptionell wichtig für zukünftige Sentiment-Blöcke im DEFCON-System (Block 'Sentiment' aktuell 10 Pt., manuelle Analysten-Analyse — eine automatisierte DPO-Pipeline wäre denkbar)."
related: "[[LLM-Preference-Optimization-Finance]], [[Sentiment-Strength-Logit-Extraction]], [[LLM-Investing-Bias-Audit]], [[Li-Kim-Cucuringu-Ma-2026-FINSABER]], [[News Sentiment Analysis]]"
raw: "[[FinDPO: Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs]]"
aliases:
  - "FinDPO: Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs"

---

# Iacovides, Zhou, Mandic — FinDPO (arXiv 2507.18417, 2025)

## Abstract (eigene Worte)

Die Imperial-College-Autoren ersetzen das De-facto-Standard-Supervised-Fine-Tuning (SFT) für Finance-Sentiment durch **Direct Preference Optimization (DPO)** — ein Post-Training-Alignment-Verfahren, das Modelle auf Präferenz-Paaren (preferred vs. dispreferred Antwort) trainiert, **ohne** RL-Komplexität. FinDPO = Llama-3-8B-Instruct + DPO + LoRA (41,9M trainierbare Parameter = 0,52% des Base-Models) → trainiert auf 32.970 gelabelten Samples (FPB + TFNS + NWGI). Ergebnisse: **SOTA-F1 0,846 Durchschnitt** (+11% über FinGPT v3.3 SOTA). **Novel logit-to-score-Konverter** extrahiert kontinuierliche Sentiment-Scores aus causal-LLM-Logits → ermöglicht erstmals Long-Short-Portfolio-Konstruktion mit causal-LLM als Sentiment-Signal. Portfolio-Evaluation: **67% annualisierte Returns bei 5bps Transaction Costs, Sharpe 2,0** — einzige getestete Methode, die unter realistischen Kosten signifikant positiv bleibt (S&P-500 baseline 11,34% p.a., 0,62 Sharpe; alle anderen Sentiment-Methoden → negativ bei 5bps).

## Fünf Hauptbeiträge

1. **Erstes DPO-aligned Finance-Sentiment-Modell** (statt SFT-Standard)
2. **Ressourcen-effizient** — einzelne A100 40GB, 4,5h Training; LoRA r=16, α=16
3. **Logit-to-Score-Konverter** — Softmax über Logits der Sentiment-Tokens → kontinuierliche Scores; Temperature-Scaling gegen DPO-Overconfidence (Leng et al. 2025)
4. **SOTA auf 3 Benchmarks** — FPB 0,865 / TFNS 0,872 / NWGI 0,833 (vs. FinGPT v3.3 Avg 0,762 → +11%)
5. **Long-Short-Portfolio-Robustheit** — robust gegen Transaction-Costs, strukturell getestet (0 bis 5 bps)

## DPO vs. SFT — methodischer Kern

| Ansatz | Training-Ziel | Generalisierung | Compute-Kosten |
|---|---|---|---|
| Supervised Fine-Tuning (SFT / FinGPT, Instruct-FinGPT) | Maximiere Likelihood der Ground-Truth-Antwort | **Memorization-Tendenz** (Chu et al. 2025 "SFT Memorizes, RL Generalizes") | mittel |
| RLHF (klassische Preference-Alignment) | Maximiere Reward subject to KL-constraint | gute Generalisierung | sehr hoch (reward model + PPO) |
| **DPO (FinDPO)** | Direkter Loss über preferred/dispreferred Paare | gute Generalisierung (empirisch validiert) | mittel — **keine Reward-Model-Training nötig** |

DPO-Loss-Form (Section 3):
$$\mathcal{L}_{DPO} = -\mathbb{E}\left[\log\sigma\left(\beta \cdot \left(\log\frac{\pi_\theta(y^w|\tilde{x})}{\pi_{ref}(y^w|\tilde{x})} - \log\frac{\pi_\theta(y^l|\tilde{x})}{\pi_{ref}(y^l|\tilde{x})}\right)\right)\right]$$

Intuition: Erhöhe Wahrscheinlichkeit der preferred Response $y^w$, senke dispreferred $y^l$ — skaliert mit dem Grad, wie stark das Policy-Modell von Human-Preferences abweicht ($\beta$-Parameter).

## Quantitative Ergebnisse (Transaction-Cost-Sensitivität)

| Method | 0bps CumReturn | 5bps CumReturn | 5bps Sharpe |
|---|---|---|---|
| S&P 500 Baseline | 83,1% | 83,1% | 0,62 |
| HIV-4 (Lexikon) | 90,1% | **-179,5%** | -1,85 |
| VADER (Lexikon) | 82,8% | **-184,6%** | -1,92 |
| LMD (Lexikon) | 139,9% | **-131,8%** | -1,35 |
| FinBERT (SFT) | 199,2% | **-74,5%** | -0,74 |
| FinLlama (SFT, prior SOTA) | 260,7% | **-17,1%** | -0,24 |
| **FinDPO (DPO)** | **747,1%** | **459,0%** | **2,03** |

**Interpretation:** Alle Nicht-DPO-Sentiment-Methoden **negativer als S&P-500-Baseline** bei realistischen 5bps-Kosten. Nur FinDPO bleibt profitabel. Das ist ein **Transaction-Cost-Robustheit-Argument**, nicht nur F1-Score-Verbesserung.

## Validierungs-Bezug zu FINSABER (B19)

**Kritischer Cross-Check:** FINSABER (Li/Kim/Cucuringu/Ma 2026, B19) zeigt, dass LLM-Investing-Vorteile systematisch in Vorpapern überschätzt werden — bei 20-J/100+-Symbol-Evaluation mit Bias-Mitigation verschwinden sie weitgehend.

FinDPO-Portfolio-Evaluation: **Februar 2015 bis Juni 2021** (~6,4 Jahre), S&P-500-Universe mit 417 effektiven Tickern. **Moderate Länge, faire Breite.** Aber:

| FINSABER-Audit-Frage | FinDPO-Status |
|---|---|
| Survivorship Bias | ✅ S&P-500-Konstituenten werden nach "Artikel vorhanden im Zeitraum" gefiltert (417 statt 500) — aber: keine delisted Aktien explizit eingeschlossen |
| Look-Ahead Bias | ✅ Temperature-Calibration auf Training-Set, nicht auf Portfolio-Corpus (Section 4.2 Data-Leakage-Vermeidung) |
| Data-Snooping | ⚠️ 5bps-Schwelle wurde im Paper selbst ausgewählt — keine Hold-Out-Set für Cost-Level-Selection |
| Regime-Asymmetrie | ⚠️ 2015-2021 Zeitraum enthält Bull-dominated Phase + COVID-Crash 2020 — Bull/Bear-Subsample-SR nicht reportet |

**Verdikt:** FinDPO ist methodisch besser als die meisten Pre-2024-LLM-Trading-Papers, aber **noch nicht FINSABER-kompatibel gegen-evaluiert** (20-J Hold-Out, Bull/Bear-Subsample-Separation). **Hypothetischer Zukunfts-Validierungs-Pfad (nicht geplant, nicht priorisiert):** Falls FinDPO jemals als Sentiment-Signal im Dynasty-Depot erwogen würde, müsste der FinDPO-Code gegen das FINSABER-Benchmark-Framework gelaufen werden. Dies ist **kein operativer Handlungsauftrag** — Dynasty-Depot ist Long-Only und bezieht Sentiment manuell über Analyst-Consensus, nicht über LLM-Klassifikation. Bis auf Weiteres: Interessantes SOTA-Paper, aber nicht belastbare "Evidenz" im DEFCON-Sinn.

## Relevanz für Dynasty-Depot

**DEFCON ist Long-Only, kein Sentiment-Signal als Haupt-Faktor** (Block "Sentiment" = 10 von 100 Pt., manuell via Analyst-Konsensus + PT-Abstand + Sell-Ratio). FinDPO's Long-Short-Konstruktion ist **orthogonal** zu DEFCON.

**Zukünftige konzeptuelle Anwendung** (frühestens 2028+, falls überhaupt):

| DEFCON-Sentiment-Block (10 Pt.) heute | Mit DPO-Pipeline potenziell |
|---|---|
| Analyst-Konsensus (3 Pt.) — Strong-Buy-%-Verteilung | Analyst-Report-Sentiment via DPO-Klassifikation |
| PT-Abstand zu aktuellem Kurs (3 Pt.) | unverändert (ist strukturell, kein Text) |
| Sell-Ratio-Check (4 Pt.) — Analyst-Bias-Korrektiv | Sell-Recommendation-Sentiment via DPO-Score |

**Ergebnis:** Kein operativer Use-Case heute. Aber als Forschungskontext für spätere Sentiment-Block-Revisionen vorgemerkt.

## Abgrenzung — Was FinDPO NICHT liefert

- **Keine Knowledge-Graph-Komponente** — pure Text-Klassifikation + Logit-Extraction, kein strukturiertes Reasoning
- **Keine Uncertainty-Quantifizierung** — DPO-Modelle sind overconfident (Leng et al. 2025); Temperature-Scaling adressiert nur Kalibrierung, nicht Retrieval-Uncertainty (vgl. Bayesian RAG)
- **Keine Moat-/Fundamental-Faktoren** — reiner Sentiment-basierter L/S
- **Keine Long-Only-Spezifika** — das Paper ist L/S, die Long-Komponente einzeln bewertet niedriger Sharpe als die vollen L/S-Portfolios

## Backlinks

- [[FinDPO_ Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs]] — Raw-Dokument (arxiv-HTML-Export in `raw/`)
- [[LLM-Preference-Optimization-Finance]] — Konzeptseite (DPO vs. SFT für Finance-LLMs)
- [[Sentiment-Strength-Logit-Extraction]] — Konzeptseite (logit-to-score-Konverter)
- [[LLM-Investing-Bias-Audit]] — Validation-Pflicht vor Adoption (FINSABER-Pattern)
- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — komplementäres Paper (empirische Bias-Evaluation)
- [[News Sentiment Analysis]] — bestehendes Konzept, wird durch DPO-Kontext erweitert
- [[Wissenschaftliche-Fundierung-DEFCON]] — Befund B24
- [[Giorgos Iacovides]], [[Wuyang Zhou]], [[Danilo Mandic]] — Author-Entities

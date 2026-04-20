---
title: "Sentiment-Strength-Logit-Extraction"
type: concept
tags: [logit-extraction, continuous-sentiment, causal-llm, portfolio-construction, temperature-scaling, softmax]
created: 2026-04-20
updated: 2026-04-20
sources: [Iacovides-Zhou-Mandic-2025-FinDPO]
related: [LLM-Preference-Optimization-Finance, News Sentiment Analysis, LLM-Investing-Bias-Audit]
wissenschaftlicher_anker: "Iacovides, Zhou, Mandic (2025) — FinDPO Remark 2; Guo et al. (2017) — Temperature Scaling"
konfidenzstufe: methoden-referenz
---

# Sentiment-Strength-Logit-Extraction

> **Novel Technique: Extrahiere kontinuierliche Sentiment-Scores aus causal-LLM-Logits via Softmax über die Sentiment-Klassen-Tokens. Ermöglicht erstmals Ranking-fähige Sentiment-Outputs aus Generative-LLMs — Voraussetzung für Long-Short-Portfolio-Konstruktion.**

## Kern-Idee

Causal-LLMs (wie Llama-3, GPT) sind trainiert auf Next-Token-Prediction. Für Klassifikations-Aufgaben (Sentiment: positive/negative/neutral) gibt das Modell normalerweise einen **diskreten Token** aus — `positive`, `negative`, oder `neutral`. Das ist binär/ternär und **nicht rangierbar**.

**Limitation:** Für Portfolio-Konstruktion braucht man **kontinuierliche Sentiment-Stärke** — nicht nur "positiv", sondern "wie positiv auf einer Skala?"

## Die Logit-to-Score-Technik (FinDPO Remark 2)

1. Forward-Pass mit Finance-Text als Input
2. Extrahiere **Logits** des ersten generierten Tokens (= Sentiment-Klasse)
3. Fokussiere auf Logits nur der Sentiment-Tokens: `[logit_positive, logit_negative, logit_neutral]`
4. Softmax über diese 3 Werte → normalisierte Wahrscheinlichkeitsverteilung
5. Linear-Projection: $s = p_{positive} - p_{negative}$ → kontinuierlicher Score in $[-1, +1]$

$s = -1$: stark negativ. $s = +1$: stark positiv. $s \approx 0$: neutral oder ambig.

## Das Overconfidence-Problem

DPO-aligned Models sind stark überconfident (Leng et al. 2025) — typischerweise $p_{preferred} = 1,0$, alle anderen $= 0,0$. Ohne Kalibrierung kollabiert die Technik auf drei diskrete Werte (-1, 0, +1), was keine Rangierbarkeit gibt.

**Mitigation: Temperature-Scaling** (Guo et al. 2017):

$$p_i = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$

Mit $T > 1$: "weichere" Verteilung, differenzierbare Intensitäten. $T$ wird auf Training-Set optimiert (NLL minimieren).

**Wichtig:** Kalibrierung auf Training-Set, NICHT auf Portfolio-Corpus — sonst Data-Leakage, falsche Performance-Claims im Backtest (siehe FINSABER-Look-Ahead-Bias).

## Warum das für Portfolios entscheidend ist

Long-Short-Portfolio-Konstruktion benötigt Ranking:

- **Top 35%** der positivsten Sentiments → Long-Position
- **Bottom 35%** der negativsten Sentiments → Short-Position

Ohne kontinuierliche Scores ist dieses Ranking nicht machbar — alle "positiv"-klassifizierten Stocks wären gleich-gewichtet im Long-Bucket. Mit Logit-Extraction entsteht echte Differenzierung.

## Empirische Effekte (FinDPO 2015-2021, S&P 500)

Die Logit-to-Score-Technik ist die technische Voraussetzung für FinDPO's Portfolio-Performance:

| Scenario | Ohne Logit-to-Score (binär) | Mit Logit-to-Score + Temp-Scaling |
|---|---|---|
| Differenzierbare Ranks | ❌ | ✅ |
| Long-Short-Konstruktion | unmöglich | ermöglicht |
| Portfolio-Sharpe 2015-2021 (0 bps) | n.a. | 3,41 |
| Portfolio-Sharpe bei 5 bps | n.a. | 2,03 |

Ohne diese Technik gäbe es **keine** kontinuierlichen Scores aus causal-LLMs → FinDPO-Paper-Kern-Innovation.

## Abgrenzung zu anderen Ansätzen

| Ansatz | Continuous? | Architektur |
|---|---|---|
| **Classification-Head (FinLlama)** | ✅ | LLM + Linear-Layer trainiert explizit für Regression |
| **Probability-Output Standard-Classifier (FinBERT)** | ✅ | BERT-Style, discrete ±probability |
| **Logit-to-Score (FinDPO)** | ✅ | Causal-LLM, Softmax post-hoc extrahiert |
| Direkte Klassifikation | ❌ | nur Token-Output |

FinDPO's Ansatz hat **einen strukturellen Vorteil:** Das Base-LLM behält seine generative Fähigkeiten komplett — Classification ist "Bonus-Feature" via Softmax. FinLlama hingegen opfert Generativität für Classification-Head.

## Caveats (eigene Analyse)

1. **Tokenizer-Abhängig:** Funktioniert nur, wenn Sentiment-Labels in einem einzelnen Token repräsentiert sind. Bei Multi-Token-Labels (z.B. "strongly positive") ist Logit-Extraction komplexer.
2. **$T$-Tuning ist sensibel:** Zu kleines $T$ → weiterhin binary-ähnlich; zu großes $T$ → alle Scores sind ~0.
3. **Benchmark-Dependency:** Technik getestet auf Llama-3-8B-DPO — Transfer auf Claude/GPT nicht validiert.

## Anwendung auf Dynasty-Depot (heute: null)

DEFCON's Sentiment-Block nutzt Analyst-Consensus (Strong-Buy-%) — kein Text-Sentiment. Logit-to-Score wäre **für zukünftige News-Sentiment-Integration** relevant:

**Hypothetischer Use-Case (frühestens 2028+):**

- Nachtrag-Block "News-Sentiment" (5 Pt. additiv?) in DEFCON
- Pipeline: FinDPO-artige Model → Logit-Extraction → Score pro Ticker → DEFCON-Mapping

**Wie weit weg?** Sehr weit. Setzt voraus:
1. Selbst-gehostetes FinDPO-Model (nicht Tavily/OpenAI)
2. News-Corpus mit Ticker-NER-Pipeline
3. FINSABER-Audit bestanden
4. DEFCON-Block-Integration ohne Double-Counting (Analyst-Consensus + News-Sentiment sind redundant — **Applied-Learning-Falle**)

Realistische Einschätzung: Diese Technik bleibt Wissenschaftskontext, nicht Roadmap.

## Dos & Don'ts

**Do:**
- Temperature-Scaling nach DPO immer einsetzen
- Kalibrierung auf Training-Set (nicht Portfolio-Corpus)
- Single-Token-Sentiment-Labels wählen, um Logit-Extraction zu vereinfachen

**Don't:**
- Ungekalibrierte DPO-Output in Portfolios einspeisen (Overconfidence → Over-Trading)
- Technik auf Nicht-DPO-Models anwenden ohne Validierung
- Logit-Werte als absolute Wahrscheinlichkeiten interpretieren

## Backlinks

- [[Iacovides-Zhou-Mandic-2025-FinDPO]] — primäre Source (Remark 2)
- [[LLM-Preference-Optimization-Finance]] — Schwester-Konzept (DPO-Training-Seite)
- [[News Sentiment Analysis]] — potenzielle Ziel-Domäne
- [[LLM-Investing-Bias-Audit]] — Pflicht-Validation vor Portfolio-Use

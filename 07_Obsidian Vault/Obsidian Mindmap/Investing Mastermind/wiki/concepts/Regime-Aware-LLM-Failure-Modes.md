---
title: "Regime-Aware Strategy Failure Modes (Bull/Bear-Asymmetrie)"
type: concept
tags: [regime, bull, bear, llm-investing, risk-management, validation, method]
created: 2026-04-20
updated: 2026-04-20
sources: [Li-Kim-Cucuringu-Ma-2026-FINSABER]
related: [LLM-Investing-Bias-Audit, Factor-Information-Decay, Backtest-Methodik-Roadmap, DEFCON-System]
wissenschaftlicher_anker: "Li, Kim, Cucuringu, Ma (2026, KDD '26) — FINSABER Section: Regime Analysis"
konfidenzstufe: methoden-standard
---

# Regime-Aware Strategy Failure Modes

> **FINSABER's empirisch dokumentierte Asymmetrie: Selection-Strategien sind systematisch zu konservativ in Bull-Markets (underperform passive) und zu aggressiv in Bear-Markets (heavy losses). Konsequenz für Track 5b FRED Macro-Regime-Filter: wissenschaftlicher Anker für die geplante Sparraten-Modulation. Konsequenz für DEFCON: Bull/Bear-Subsample-Performance prüfen.**

## Kern-Befund

In FINSABER's 20-Jahres / 100+ Symbol-Eval zeigen **alle untersuchten LLM-Investing-Strategien** (FinMem, FinAgent, FinRobot, TradExpert, FinCon, TradingAgents, MarketSenseAI 2.0) ein konsistentes Asymmetrie-Muster:

| Regime | Verhalten | Konsequenz |
|---|---|---|
| **Bull-Market** | zu konservativ | unterperformt passive Buy-and-Hold-Benchmarks |
| **Bear-Market** | zu aggressiv | erleidet disproportionale Verluste |
| **Trend-Wechsel** | falsche Reaktion | Risk-Off-Heuristik fehlt |

**Quantifizierung (komprimiert):** Detail-Zahlen in FINSABER Tabellen — übergreifender Befund: Net-Asymmetrie macht passive-Benchmark-Schlag in jedem Regime fragil.

## Warum Strategien dieses Muster zeigen

FINSABER's Diagnose (Section: Regime Analysis):
1. **Fehlende explizite Trend-Detection** — die meisten Frameworks lassen Regime-Klassifikation der LLM-Inferenz allein, statt sie als pre-Decision-Layer zu etablieren
2. **Sentiment-Inputs sind im Bull/Bear-Übergang lagging** — News reflektiert bereits eingetroffene Marktbewegung, nicht den Wechsel selbst
3. **Risk-Controls werden architektur-versteckt** — komplexe Multi-Agent-Frameworks "diluten" die Risk-Disziplin, statt sie zu verstärken

## DEFCON-Implikation

DEFCON hat **explizite Risk-Controls** (CapEx-FLAG, ROIC<WACC-Malus, Insider-FLAG, Quality-Trap-Interaktionsterm), die regelbasiert greifen. **Aber:** Regime-Awareness ist nicht explizit eingebaut.

**Self-Audit-Fragen:**
- Hat DEFCON v3.7 in der Bull-Phase 2024-25 vs. SPY underperformt? (Datenlage: Forward-Records erst seit 17.04.2026)
- Ist die Sparraten-Modulation (D2/FLAG → 17,81€/0€) regime-anti-zyklisch (mehr in Crash, weniger in Hype)?
  - **Heuristik-Antwort:** ja, indirekt, weil DEFCON-Score sich zyklisch mit Bewertung bewegt (Quality-Trap-Term)
  - **Empirische Antwort:** offen, frühestens 2027 evaluierbar

## Verbindung zu Track 5b FRED Regime-Filter

Der geplante Macro-Regime-Filter (`docs/superpowers/plans/2026-04-20-track5b-fred-regime-filter.md`) ist eine **direkte Operationalisierung** des FINSABER-Befunds:

| Track-5b-Element | FINSABER-Bezug |
|---|---|
| FRED-basierte Regime-Klassifikation | explizite Pre-Decision-Trend-Detection-Layer |
| Sparraten-Modulation in Risk-On/Off | regime-aware Risk-Control |
| Grid-Search 1620 Combos | Multiple-Testing-Risk → braucht GT-Score-Patch (siehe [[Composite-Anti-Overfitting-Objective]]) |
| `forward_6m_hit_rate` Sekundär-Diagnose | Bull/Bear-Subsample-Validation |

**Wissenschaftlicher Anker:** Track 5b ist nicht heuristisch, sondern adressiert eine empirisch dokumentierte Failure-Mode aller untersuchten LLM-Investing-Strategien. FINSABER's Empfehlung: *"Regime-awareness and adaptive risk management are more critical than increasing architectural complexity."*

## Long-Only ≠ Immune

Naheliegender Einwand: "Wir sind Long-Only, also kann uns Bear-Aggressivität nicht treffen — wir kaufen sowieso nur."

**FINSABER's Gegen-Argument (implizit):**
- Long-Only-Strategien können in Bear "zu aggressiv" sein, wenn sie in Drawdown nachkaufen ohne Risk-Off-Filter
- Sparplan in Bear ist wertvoll **wenn** Picks Drawdown-resistent sind; **schädlich**, wenn Picks selbst Bear-anfällig (z.B. CapEx-FLAG-Ticker)
- DEFCON's CapEx-FLAG → 0€ Sparrate ist genau ein Bear-Aggressivität-Filter; aber ohne Macro-Regime-Filter unvollständig

→ **Long-Only-Annahme entbindet uns NICHT vom Regime-Audit.**

## Operationalisierung im Dynasty-Depot

- **§29.2 Erweiterung** — AQR-Bench-Check um Bull/Bear-Subsample-SR-Trennung erweitern
- **Track 5b Plan-Diff** — FINSABER als "Empirischer Anker" im Plan-Header markieren (Phase 3 Action)
- **`backtest-ready-forward-verify` Schema** — `regime_tag` Feld (Bull/Bear/Neutral basierend auf Track-5b-Filter, sobald aktiv)
- **CORE-MEMORY §5 Lektion** — Bull/Bear-Asymmetrie als Validation-Pflicht bei DEFCON-Future-Reviews

## Dos & Don'ts

**Do:**
- Bull/Bear-Subsample bei jeder retrospektiven SR-Analyse trennen
- Track 5b FRED-Regime-Filter als wissenschaftlich fundiert kommunizieren (nicht als heuristisch)
- "Long-Only-Immunität" explizit hinterfragen — DEFCON CapEx-FLAG ist Beleg, dass Risk-Off-Filter auch bei Long-Only nötig sind

**Don't:**
- Annehmen, regelbasiertes Composite (DEFCON) sei automatisch regime-aware
- Track 5b als "nice-to-have-Optimierung" abtun — es adressiert empirisch dokumentierte Failure-Mode
- Bull-Underperform mit "kalibriert für Risk-Adjusted-Returns" wegrationaliesieren ohne Bull-Subsample-SR-Beleg

## Backlinks

- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — Source (Section: Regime Analysis)
- [[LLM-Investing-Bias-Audit]] — komplementäres Konzept (Bias-Audit-Pattern)
- [[Factor-Information-Decay]] — Cadence-Validation (Half-Life-Logik)
- [[Backtest-Methodik-Roadmap]] — v2.1 Validation-Framework
- [[DEFCON-System]] — Zielsystem für Bull/Bear-Subsample-Audit
- [[CapEx-FLAG]] — bestehender expliziter Risk-Off-Filter (regime-awareness-relevant)

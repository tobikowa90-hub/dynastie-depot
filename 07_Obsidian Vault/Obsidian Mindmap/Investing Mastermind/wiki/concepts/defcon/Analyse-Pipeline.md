---
title: "Analyse-Pipeline"
type: concept
tags: [konzept, pipeline, workflow]
created: 2026-04-10
updated: 2026-04-14
sources: []
related: [DEFCON-System, CapEx-FLAG, ROIC-vs-WACC, Tariff-Exposure-Regel, Non-US-Scoring, Update-Klassen-DEFCON]
---

# Analyse-Pipeline — Stufe 0 → Entscheidung

```
Impuls / Idee
     ↓
[STUFE 0]  !QuickCheck / Quick-Screener
           P/FCF ≤35 + ROIC ≥15% + Moat-Proxy
           → 🟢 weiter | 🟡 Watchlist | 🔴 aussortieren
     ↓ nur 🟢
[STUFE 2]  !Analysiere [TICKER]
           100-Punkte DEFCON-Score
           → Score ≥ 80 + kein FLAG → weiter
     ↓ nur Score ≥ 80
[STUFE 3]  !CAPEX-FCF-ANALYSIS
           6 Excel-Sheets (Executive Summary, Historisch,
           Szenarien, DCF, Peer-Vergleich, Risiko)
     ↓
[ENTSCHEIDUNG] Einstieg / Watchlist / Veto
```

## Skill-Hierarchie (v2.0 — 08.04.2026)

`dynastie-depot` ist der Monolith. Innerhalb von `!Analysiere` werden keine weiteren Skills geladen — alle Module werden direkt als Tool-Calls genutzt.

| Befehl | Skill |
|--------|-------|
| `!QuickCheck` | quick-screener |
| `!EarningsPreview` | earnings-preview |
| `!EarningsRecap` | earnings-recap |
| `!InsiderScan` | insider-intelligence |
| `!PortfolioRisk` | risk-metrics-calculation |

## Verlinkungen

- [[DEFCON-System]] — Scoring-Matrix (Stufe 2)
- [[CapEx-FLAG]] — Automatische FLAGs (score-unabhängig)
- [[quick-screener]] — Skill für Stufe 0 (!QuickCheck)
- [[insider-intelligence]] — Form-4-Automatisierung (!InsiderScan)
- [[non-us-fundamentals]] — yfinance für ASML/RMS/SU (!NonUSScan)
- [[dynastie-depot-skill]] — Übergeordneter Monolith mit allen Befehlen
- [[Chain-of-Thought Prompting]] — Strukturprinzip hinter !Analysiere: erst Reasoning, dann Score
- [[LLM-Based Stock Rating]] — Forschungsgrundlage für den Analyse-Workflow (JPM 2024)

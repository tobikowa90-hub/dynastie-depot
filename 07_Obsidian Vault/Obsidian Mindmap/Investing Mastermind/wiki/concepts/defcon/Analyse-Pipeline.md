---
title: "Analyse-Pipeline"
type: concept
tags: [konzept, pipeline, workflow]
created: 2026-04-10
updated: 2026-04-19
sources: [llms-for-equity-stock-ratings, arXiv-1711.04837]
related: [DEFCON-System, CapEx-FLAG, ROIC-vs-WACC, Tariff-Exposure-Regel, Non-US-Scoring, Update-Klassen-DEFCON]
wissenschaftlicher_anker: "B7 (alle 4 Paper) — Fundamentals > Sentiment > Technicals als Datenhierarchie | B10 (JPM 2024) — Chain-of-Thought vor Scoring verbessert Konsistenz und Genauigkeit"
konfidenzstufe: peer-reviewed
aliases:
  - "analyse-pipeline"

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
| Portfolio-Risk-Audit | `03_Tools/portfolio_risk.py` (Python-Tool, quarterly) |

## Verlinkungen

- [[DEFCON-System]] — Scoring-Matrix (Stufe 2)
- [[CapEx-FLAG]] — Automatische FLAGs (score-unabhängig)
- [[quick-screener]] — Skill für Stufe 0 (!QuickCheck)
- [[insider-intelligence]] — Form-4-Automatisierung (!InsiderScan)
- [[non-us-fundamentals]] — yfinance für ASML/RMS/SU (!NonUSScan)
- [[dynastie-depot-skill]] — Übergeordneter Monolith mit allen Befehlen
- [[Chain-of-Thought Prompting]] — Strukturprinzip hinter !Analysiere: erst Reasoning, dann Score
- [[LLM-Based Stock Rating]] — Forschungsgrundlage für den Analyse-Workflow (JPM 2024)
- [[Score-Archiv]] — Pipeline-Ausgabe landet im History-Layer
- [[Backtest-Ready-Infrastructure]] — Dachkonzept für persistente Analyse-Historie

## Archiv-Write (Pflicht, Schritt 7 — seit 2026-04-17)

Nach Output-Abschnitt 6 "Depot-Einordnung" folgen zwei verbindliche Schritte in SKILL.md:

**Schritt 6b — FLAG-Resolution-Check:**
```bash
python 03_Tools/backtest-ready/archive_flag.py list --ticker <T> --aktiv
# Für jeden offenen FLAG: prüfen ob Metrik normalisiert, ggf. resolve
```

**Schritt 7 — Archiv-Write (seit 19.04.2026 via Skill orchestriert):**

Draft-JSON (`{"record": {...}, "skill_meta": {...}}`) nach `03_Tools/backtest-ready/_drafts/<TICKER>_<YYYYMMDD-HHMM>.json` schreiben, dann:

```
Skill(skill="backtest-ready-forward-verify", args="<pfad-zum-draft>")
```

Der Skill orchestriert Phasen P1-P6 (Schema-Validation → Freshness + STATE.md-Tripwire → §28.2 Δ-Gate conditional → Dry-Run → Append → git add). Stdout-Report mit 6 Fällen (OK / freshness / PFLICHT / STOP / duplicate / FAIL) — dynastie-depot-Handler routet weiter. Der Score-Record wird via Pydantic-Schema ([[Score-Archiv]]) validiert (Arithmetik, DEFCON-Konsistenz, Quality-Trap-Interaktion) und an `05_Archiv/score_history.jsonl` angehängt. Keine Ausnahme — jeder verpasste Append = irreversibler Historie-Verlust.

Commit-Disziplin §18: Alle sechs Dateien (log.md + CORE-MEMORY.md + Faktortabelle + STATE.md + score_history.jsonl + ggf. flag_events.jsonl) in einem git-Commit.

## Wissenschaftliche Fundierung (nachträglich 19.04.2026)

Die 5-Block-Analyse-Pipeline (Fundamentals/Moat/Quality/Insider/Technicals) mappt auf AQR-Kanon (Aghassi 2023):

- **Fundamentals** (Fwd P/E, P/FCF, Valuation-Z) → **Value**-Faktor, siehe [[Factor-Investing-Framework]]
- **Moat + Quality-Fundamentals** → **Quality (QMJ)** + **Defensive (BAB)**, siehe [[QMJ-Faktor]], [[Moat-Taxonomie-Morningstar]]
- **Technicals** → **Momentum**-Faktor (UMD)
- **Insider** → non-AQR-Edge (kein direkter Faktor-Anker, Dynasty-Depot-spezifisch)

**Seven-Sins-Pre-Flight (§29.5)** greift ab sofort bei Migration-Events (§28), bei Live-Analysen Backlog 2028.

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Factor-Investing-Framework]], [[Seven-Sins-Backtesting]]

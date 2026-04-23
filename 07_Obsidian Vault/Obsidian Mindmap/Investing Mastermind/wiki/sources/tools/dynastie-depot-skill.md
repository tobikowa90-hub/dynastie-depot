---
tags: [skill, tool, defcon, analyse, workflow, befehlsreferenz]
status: aktiv
version: "3.7.2"
stand: 2026-04-19
---

# Dynastie-Depot Skill — DEFCON v3.7 (Skill-Paket v3.7.2)

> Der übergeordnete Analyse-Skill des Dynasty-Depots. Alle Workflows, Scoring-Skalen und Regeln. Aktivierung bei JEDEM Gespräch über Aktienanalyse, Portfolio, DEFCON, Sparplan, Rebalancing oder Steuer.
>
> **Seit 19.04.2026 (v3.7.2):** Schritt 7 (Archiv-Write) delegiert an Satelliten-Skill [[backtest-ready-forward-verify]] — nicht mehr strikt Monolith. Andere Workflows (!Analysiere, !Rebalancing, etc.) bleiben inline.

## Befehls-Übersicht

| Befehl | Funktion | Dauer |
|--------|----------|-------|
| `!Analysiere [TICKER]` | 100-Punkte-DEFCON-Vollanalyse | ~20–25 min |
| `!CAPEX-FCF-ANALYSIS [TICKER]` | Excel-Tiefenanalyse, 6 Sheets | ~25–30 min |
| `!Rebalancing` | Sparplan-Drift-Check + Vorschlag | ~10 min |
| `!QuickCheck [TICKER\|ALL]` | Ampel-Check, kein Deep Dive | ~3–5 min |
| `!EarningsPreview [TICKER]` | Earnings-Preview (48h vorher) | — |
| `!EarningsRecap [TICKER]` | Earnings-Recap (48h nachher) | — |
| `!InsiderScan [TICKER\|ALL]` | Form-4-Scan via insider_intel.py | — |
| `!NonUSScan [TICKER\|ALL]` | Fundamentals ASML/RMS/SU | — |

## Skill-Hierarchie (v3.0 — 19.04.2026)

**Grundprinzip (v3.7.2 revidiert):** `dynastie-depot` ist der **Haupt-Skill** für Scoring + Workflows. Innerhalb von `!Analysiere` werden Module **grundsätzlich** als Tool-Calls genutzt — mit einer Ausnahme: **Schritt 7 (Archiv-Write)** delegiert an den Satelliten-Skill `backtest-ready-forward-verify`, weil die Persistence-Pipeline (Freshness / Tripwire / §28.2 Δ-Gate / Dry-Run / Append / git add) mechanisch durchgesetzt werden muss statt in Prosa. Skill-Load-Overhead dort akzeptiert — Pipeline-Disziplin > Token.

| Befehl / Phase | Eigenständiger Skill | Bedingung |
|----------------|---------------------|-----------|
| `!QuickCheck` | [[quick-screener]] | Stufe-0-Vorfilter oder monatlicher Check |
| `!EarningsPreview` | earnings-preview | 48h vor Earnings |
| `!EarningsRecap` | earnings-recap | 48h nach Earnings |
| `!InsiderScan` | [[insider-intelligence]] | Standalone ohne !Analysiere |
| `!NonUSScan` | [[non-us-fundamentals]] | Non-US-Satelliten |
| `!Analysiere` Schritt 7 | [[backtest-ready-forward-verify]] | Automatisch am Ende jeder Vollanalyse — programmatisch, kein Trigger-Word |
| Portfolio-Risk-Audit | `03_Tools/portfolio_risk.py` (Python-Tool) | Quartalsweise manuell — kein Skill |

## Skill-Dateien

| Datei | Wann lesen |
|-------|-----------|
| `SKILL.md` | Immer — Workflows, Scoring-Skalen, Regeln |
| `manifest.md` | Strategische Fragen, Rebalancing, Steuer |
| `capex-fcf-template.md` | Bei !CAPEX-FCF-ANALYSIS |
| `sources.md` | Jede Analyse — Quellen-URLs pro Metrik |
| `Beispiele.md` | Vor !Analysiere — Kalibrierungsanker |
| `config.yaml` | Portfolio-State: Scores, FLAGS, Positionen |

## !CAPEX-FCF-ANALYSIS — 6 Excel-Sheets

Trigger: nur bei Score ≥ 80 aus Stufe 2.

1. Executive Summary
2. Historische CapEx/FCF-Daten (5–10 Jahre)
3. Szenario-Analyse (Bull / Base / Bear)
4. DCF-Bewertung
5. Peer-Vergleich
6. Risiko-Dashboard

## !Rebalancing — Workflow

**Sparplan-Formel (v3.4 korrigiert):**
```
Gewichte: D4/D3 (kein 🔴 FLAG) = 1.0 | D2 (kein 🔴 FLAG) = 0.5 | D1 / 🔴 FLAG = 0.0
Einzelrate = 285€ / Σ Gewichte × Eigengewicht
```

**Rechenbeispiel (Stand 19.04.2026, v3.7: 7× D4/D3, 2× D2 (V+TMO), 2× 🔴 FLAG):**
- Nenner = (7 × 1.0) + (2 × 0.5) = **8.0**
- D4/D3-Rate = 285 / 8.0 × 1.0 = **35,63€**
- D2-Rate (V, TMO) = 285 / 8.0 × 0.5 = **17,81€**
- 🔴 FLAG-Rate (MSFT, APH) = **0€**

## Kalibrierungsanker (vor jeder Analyse pflichtlesen!)

| Ticker | Score | DEFCON | Lektion |
|--------|-------|--------|---------|
| [[AVGO]] | 84 | 🟢 4 | Fabless-Modell = CapEx/OCF <15%, Top-Referenz (v3.7) |
| MKL | 82 | 🟢 4 | Float-Modell = FCF-Sonderregel, Versicherung |
| SNPS | 76 | 🟡 3 | Goodwill-Malus durch Ansys-Akquisition (v3.5) |
| [[TMO]] | 64 | 🟠 2 | ROIC bereinigt 17,18% > WACC 10,44% (Regel-4), fcf_trend_neg strukturell disclosed (18.04.) |
| [[V]] | 63 | 🟠 2 | Technicals-Kollaps + GAAP ROIC <WACC; 18.04. Forward ersetzte Algebra-Projektion 86 |

## Verhaltensregeln (unantastbar)

1. **Quellenpflicht** — jede Zahl mit Web-Quelle belegen
2. **Konservativ scoren** — bei Grenzfällen den niedrigeren Score
3. **Kalibrieren** — vor jeder Analyse Beispiele.md lesen
4. **Kein Raten** — bei Unsicherheit nachfragen
5. **FLAG heilig** — überschreibt jeden Score
6. **EUR/USD explizit** — Währung immer angeben
7. **Steuer-Bewusstsein** — bei Verkaufs-Fragen: 26,375% Abgeltungsteuer, FIFO

## Verlinkungen

- [[Analyse-Pipeline]] — Stufe 0 → 1 → 2 → Entscheidung
- [[DEFCON-System]] — Scoring-Matrix und Schwellen
- [[CapEx-FLAG]] — FLAG-Regeln (heilig, score-unabhängig)
- [[defeatbeta]] — US-Fundamentals API (Primär)
- [[Shibui-SQL]] — Technicals API (Primär)
- [[OpenInsider]] — Insider-Pflichtquelle
- [[quick-screener]] — Stufe-0 Skill
- [[insider-intelligence]] — Form-4-Automatisierung
- [[non-us-fundamentals]] — yfinance für ASML/RMS/SU
- [[Non-US-Scoring]] — IFRS-Addendum
- [[Steuer-Architektur]] — Tax-Mechaniken

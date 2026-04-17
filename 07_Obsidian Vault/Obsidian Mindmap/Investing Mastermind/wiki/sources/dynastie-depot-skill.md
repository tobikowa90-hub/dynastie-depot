---
tags: [skill, tool, defcon, analyse, workflow, befehlsreferenz, monolith]
status: aktiv
version: "3.4"
stand: 2026-04-07
---

# Dynastie-Depot Skill — DEFCON v3.4 Monolith

> Der übergeordnete Analyse-Skill des Dynasty-Depots. Alle Workflows, Scoring-Skalen und Regeln. Aktivierung bei JEDEM Gespräch über Aktienanalyse, Portfolio, DEFCON, Sparplan, Rebalancing oder Steuer.

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

## Skill-Hierarchie (v2.0 — 08.04.2026)

**Grundprinzip:** `dynastie-depot` ist der Monolith. Innerhalb von `!Analysiere` werden **keine weiteren Skills geladen** — alle Module werden direkt als Tool-Calls genutzt. Jeder zusätzliche Skill-Load kostet Token und verliert DEFCON-Kontext.

| Befehl | Eigenständiger Skill | Bedingung |
|--------|---------------------|-----------|
| `!QuickCheck` | [[quick-screener]] | Stufe-0-Vorfilter oder monatlicher Check |
| `!EarningsPreview` | earnings-preview | 48h vor Earnings |
| `!EarningsRecap` | earnings-recap | 48h nach Earnings |
| `!InsiderScan` | [[insider-intelligence]] | Standalone ohne !Analysiere |
| `!NonUSScan` | [[non-us-fundamentals]] | Non-US-Satelliten |
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

**Rechenbeispiel (Stand 17.04.2026, v3.7: 8× D4/D3, 1× D2 TMO, 2× 🔴 FLAG):**
- Nenner = (8 × 1.0) + (1 × 0.5) = **8.5**
- D4/D3-Rate = 285 / 8.5 × 1.0 = **33,53€**
- D2-Rate (TMO) = 285 / 8.5 × 0.5 = **16,76€**
- 🔴 FLAG-Rate (MSFT, APH) = **0€**

## Kalibrierungsanker (vor jeder Analyse pflichtlesen!)

| Ticker | Score | DEFCON | Lektion |
|--------|-------|--------|---------|
| [[AVGO]] | 86 | 🟢 4 | Fabless-Modell = CapEx/OCF <15%, Top-Referenz |
| MKL | 82 | 🟢 4 | Float-Modell = FCF-Sonderregel, Versicherung |
| SNPS | 79 | 🟡 3 | Goodwill-Malus durch Ansys-Akquisition (-3 Pt.) |
| [[TMO]] | 65 | 🟡 3 | ROIC < WACC + Akquisitionsschuld = Malus trotz Moat |

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

---
title: "LLM-Investing-Bias-Audit (FINSABER-Pattern)"
type: concept
tags: [llm-investing, backtest, bias-audit, survivorship, look-ahead, data-snooping, validation, method]
created: 2026-04-20
updated: 2026-04-20
sources: [Li-Kim-Cucuringu-Ma-2026-FINSABER]
related: [Regime-Aware-LLM-Failure-Modes, PBO-Backtest-Overfitting, Seven-Sins-Backtesting, Backtest-Methodik-Roadmap, Score-Archiv, Backtest-Ready-Infrastructure, DEFCON-System]
wissenschaftlicher_anker: "Li, Kim, Cucuringu, Ma (2026, KDD '26) — FINSABER-Framework"
konfidenzstufe: methoden-standard
---

# LLM-Investing-Bias-Audit (FINSABER-Pattern)

> **Audit-Pattern für jede Strategie, die als Selection-Output funktioniert (LLM-Inferenz oder regelbasiertes Composite). Drei Bias-Quellen + Regime-Asymmetrie. Operative Pre-Flight für jede retrospektive Analyse — auch für DEFCON, weil DEFCON als Ticker-Selektor und Sparrate-Modulator ein Selection-Strategy-Charakter hat.**

## Kern-Idee

FINSABER zeigt empirisch: Die meisten LLM-Investing-Vorteile aus 2023-2025-Vorpapern verschwinden, sobald Survivorship/Look-Ahead/Data-Snooping kontrolliert und 20-J-Universen mit 100+ Symbolen genutzt werden. Diese drei Bias-Quellen + die Regime-Asymmetrie (siehe [[Regime-Aware-LLM-Failure-Modes]]) bilden ein **strukturiertes Audit-Pattern**, das auf jede Selection-Strategy anwendbar ist — unabhängig davon, ob sie LLM-basiert oder regelbasiert (wie DEFCON) ist.

## Die drei Bias-Quellen

### 1. Survivorship Bias

**Definition:** Backtest enthält nur heute aktive Aktien — delisted/bankrupt/merged Aktien fehlen systematisch. Auch "preinclusion bias" wenn historische Investments aus heutiger Index-Membership abgeleitet werden.

**Quantifizierung (Literatur):** 0,1-0,9% p.a. Verzerrung (Grinblatt/Titman, Elton et al.); selbst kleine Verzerrungen können Performance-Persistenz fälschen (Brown et al.).

**Audit-Frage für DEFCON:**
- Welche Ticker hat der `quick-screener` historisch abgelehnt? Existiert ein Reject-Set?
- Sind unsere 11 Satelliten + Ersatzbank das Ergebnis einer survivor-biased-Top-Down-Auswahl?
- Wird bei Slot-16-Suche heute aktive S&P-500-Membership als Ausgangspunkt genommen?

**Mitigation:**
- `quick-screener` Reject-Historie persistieren (aktuell nicht)
- Slot-Suche-Methodik dokumentieren — wenn Survivorship-bias unvermeidbar, explizit markieren

### 2. Look-Ahead Bias

**Definition:** Strategie nutzt Information, die zum Decision-Zeitpunkt nicht bekannt war. Inkludiert: Feature-Selection auf Full-Period-Outcomes, Symbol-Auswahl über zukünftige Performance, Schwellen-Tuning auf gesamtem Sample.

**Audit-Frage für DEFCON:**
- Werden Backfill-Records mit aktuellem v3.7-Wissen für Pre-v3.7-Ticker geschrieben? *(Antwort: ja, 24 von 27 Records sind Backfill — bei Backtest nur `source=forward` nutzen)*
- Wird Earnings-getriebene Re-Analyse (DEFCON v3.7) für Daten vor v3.7-Definition rückwirkend angewendet?

**Mitigation:**
- Forward-Records ab 17.04.2026 als saubere Basis
- `source` Feld trennt forward/backfill (bereits implementiert)
- Portfolio-Return-Persistenz seit 19.04.2026 statt 2028-Backfill

### 3. Data-Snooping Bias (Multiple-Testing)

**Definition:** Wiederholtes Testen auf demselben Datensatz produziert Overfitting. In Finanzen besonders kritisch wegen kleiner Sample-Sizes und niedrigem Signal-Noise-Verhältnis.

**Quantifizierung:** Bailey 2014 (Deflated Sharpe) zeigt, dass jede zusätzliche Trial-Iteration die SR-Konfidenz drückt; PBO/CSCV ([[PBO-Backtest-Overfitting]]) formalisiert die Wahrscheinlichkeit.

**Audit-Frage für DEFCON:**
- Wie viele v3.x-Iterationen gab es zwischen v3.0 und v3.7? **8 Versionen in ~3 Monaten.** Iterations-Anzahl nicht offen-gelegt im git log.
- Hold-Out überhaupt definiert? *(Aktuell: nein — alle Forward-Daten werden für Live-Verify genutzt)*
- §28.2 Migration-Δ-Gate adressiert das Drift-Problem partiell, aber kein formales Hold-Out

**Mitigation:**
- §29.4 t-Stat ≥ 3 Hurdle für jede neue Sub-Komponente (bereits in INSTRUKTIONEN)
- §29.1 PBO < 0,05 ab erster Parameter-Variation (bereits geplant)
- Hold-Out-Definition erwägen für Review 2028 (offen)

## DEFCON-Self-Audit-Checkliste (FINSABER-Pattern)

Vor **jeder** retrospektiven Analyse, jedem Major-Versions-Bump, oder Skill-Self-Audit:

- [ ] **Survivorship:** Reject-Set rekonstruiert oder explizit als unrekonstruierbar dokumentiert
- [ ] **Look-Ahead:** Nur `source=forward` oder Backfill explizit deklariert
- [ ] **Data-Snooping:** Iterations-Count seit letztem Hold-Out offen-gelegt; PBO/CSCV ggf. berechnet
- [ ] **Regime-Asymmetrie:** Bull/Bear-Subsample-SR getrennt geprüft (siehe [[Regime-Aware-LLM-Failure-Modes]])

## Abgrenzung: FINSABER ≠ LLM-Sicherheitsproblem

DEFCON ist regelbasiertes Composite-Scoring, nicht LLM-Inferenz. FINSABER's Befunde sind dennoch übertragbar, weil:

| Bias-Quelle | Mechanismus | Trifft zu auf… |
|---|---|---|
| Survivorship | Selection-Output basiert auf survivor-skewed Universe | jede Selection-Strategie |
| Look-Ahead | Backtest-Setup nutzt Zukunfts-Information | jede retrospektive Analyse |
| Data-Snooping | Wiederholtes Testen auf demselben Datensatz | jede Optimization-Suche |
| Regime-Asymmetrie | Strategie reagiert falsch auf Trend-Wechsel | Selection- + Allocation-Strategien |

→ Audit-Methode ist **bias-quellen-orientiert**, nicht "LLM-vs-Rule"-orientiert. Codex Round 2 (A3) bestätigt: "Tragfähig — wenn klar als Selbst-Audit des regelbasierten Composite-Outputs formuliert."

## Operationalisierung im Dynasty-Depot

- **§29.5 Erweiterung** — Seven-Sins-Pre-Flight um FINSABER-Audit-Fragen ergänzen (Reject-Set, Iteration-Count, Hold-Out-Definition)
- **Mögliche §33 "Skill-Self-Audit"** — DEFCON als Selection-Strategy formell dokumentieren, jährliche Audit-Cadence (Codex Round 2 Empfehlung — Phase 2.5 Codex-Gate vor Adoption)
- **`backtest-ready-forward-verify` Schema** — `bias_flags` Feld in `score_history.jsonl` (survivorship-checked, lookahead-checked, snooping-checked Boolean)
- **Aktivierungs-Trigger:** sofort wirksam für jede neue Migration; PBO/CSCV-Pflicht ab Review 2028 oder erstem Parameter-Tuning

## Dos & Don'ts

**Do:**
- Audit-Fragen vor jeder retrospektiven Analyse beantworten (auch wenn Antwort "Reject-Set unrekonstruierbar" ist)
- Iteration-Count für Major-Versions offen-legen (z.B. v3.7 = 8 Iterationen in 3 Monaten)
- Bull/Bear-Subsample getrennt evaluieren

**Don't:**
- Bias-Audit als "LLM-Sicherheitsdebatte" abtun (gilt für jede Selection-Strategy)
- Data-Snooping-Bias mit "Sample zu klein für PBO" wegrationaliesieren (gerade dann ist Audit relevant)
- Regime-Asymmetrie ignorieren, weil "Long-Only macht Bear weniger schlimm" (FINSABER zeigt: Risk-Off-Heuristik fehlt auch Long-Only-Strategien)

## Backlinks

- [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] — Source-Zusammenfassung
- [[Regime-Aware-LLM-Failure-Modes]] — komplementäres Konzept (Bull/Bear-Asymmetrie)
- [[PBO-Backtest-Overfitting]] — formalisiert Sin #4 (Data-Snooping)
- [[Seven-Sins-Backtesting]] — FINSABER konkretisiert Sins #1-#4
- [[Backtest-Methodik-Roadmap]] — v2.1 Validation-Framework
- [[Score-Archiv]] — Datenbasis für Audit (source=forward)
- [[DEFCON-System]] — Zielsystem, das auditiert wird

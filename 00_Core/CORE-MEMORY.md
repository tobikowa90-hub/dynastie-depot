# 🧠 CORE-MEMORY.md — Institutionelles Gedächtnis
**Version:** 1.9 (v3.7 + Topic-Auflösung §1→§12/§13) | **Stand:** 25.04.2026

## Verweise
- [STATE.md](STATE.md) — Hub + Last-Audit
- [PORTFOLIO.md](PORTFOLIO.md) — Live-Portfolio-State
- [PIPELINE.md](PIPELINE.md) — Pipeline-SSoT (ersetzt altes §9b)
- [SYSTEM.md](SYSTEM.md) — Infra/Briefing/Backtest
- [INSTRUKTIONEN.md §5](INSTRUKTIONEN.md) — Sentiment/Scoring-Kontext
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail pro Ticker

> Dieses Dokument speichert alle wichtigen Entscheidungen, Erkenntnisse und
> strategischen Weichenstellungen aus den Projektthreads.
> Für Strategie → KONTEXT.md | Für Workflows → INSTRUKTIONEN.md
> Per-Ticker-Chronik → §12 | System-Lifecycle → §13

---

## 2. Strategische Entscheidungen (dauerhaft bindend)

### Allokations-Entscheidung (März 2026)
**Beschluss:** 60/35/5 → **65/30/5** (ETF/Satelliten/Gold)
**Grund:** Mehr Diversifikation, weniger Single-Stock-Risiko, höhere wissenschaftliche Basis im ETF-Block
**Bindend:** Ja — keine Änderung ohne expliziten Beschluss

### Gewichtungs-Entscheidung Satelliten
**Beschluss:** Alle 11 Positionen gleichgewichtet 2,73% (APH 2,70% Ausgleich)
**Vorher:** TMO 2,5%, APH 2,5%, COST 3,5% — ungleichgewichtet
**Bindend:** Ja

### Slot-Anzahl
**Beschluss:** 16 Slots maximum (4 ETFs + 11 Aktien + 1 Gold)
**Slot 12–16 belegt:** Alle vergeben. Nächste Entscheidung: Juni 2026
**Bindend:** Ja — kein Overcrowding

### CRWD und PLTR Entfernung
**Beschluss:** Beide entfernt — kein Wide Moat, Hyper-Growth-Angreifer-Profil passt nicht zur Strategie
**Datum:** März 2026
**Gelernt:** Strategie-Fit > kurzfristige Rendite

### GOOGL struktureller Ausschluss
**Beschluss:** Kein Einstieg trotz Score 72 — 🔴 FLAG CapEx FY26 ~75% OCF
**Datum:** 01.04.2026 (FLAG permanent bis Auflösung)
**Gelernt:** FLAG überschreibt Score. Kein Kompromiss.

---

## 3. Aktive Positions-Entscheidungen (Historisch, pre-v3.7 — aktuelle Positions-Realität in `00_Core/PORTFOLIO.md` + `Faktortabelle.md`)

> ⚠️ **Historische Entscheidungs-Narrative (04.04.–16.04.).** Aktuelle Live-Scores/DEFCON/Sparraten → `00_Core/PORTFOLIO.md`. v3.7-Shifts: MSFT 60→59, TMO 62→63 (D2 bestätigt), APH 61→63 (FLAG bleibt), ASML 66→68 (Post-Q1 Vollanalyse). Weitere Shifts 18.04.: V Vollanalyse 63/D2, 5 Tickers Threshold-Drift-Fix D4→D3, Nenner 8.5→8.0. Section bleibt als Entscheidungs-Logik-Archiv erhalten.

### MSFT — DEFCON 2, FLAG aktiv (Re-Analyse 08.04.2026)
- **Score:** 60/100 (↓ von 77, −17 Punkte) | **DEFCON:** 🟠 2 | **FLAG:** 🔴 CapEx/OCF Q2 FY26: 83.6% (bereinigt ~63%)
- **Sparrate:** 0 € (FLAG + DEFCON 2 → doppelte Absicherung) seit 26.03.2026
- **Score-Verfall:** ROIC 7.5% vs. WACC 13.35% (−5.85 PP) = strukturell unter Kapitalkosten. CapEx FY26 auf Kurs $100–120B. FCF FY25: $71.6B (↓ von $74.1B)
- **Trigger für FLAG-Auflösung:** Q3 FY26 Earnings 29.04.2026 — bereinigtes CapEx/OCF muss <60% fallen (Finance Leases raus)
- **Nach FLAG-Auflösung:** Score-Update nötig — bei Score ≥65 → DEFCON 3 volle Rate; bei Score 50–64 → DEFCON 2 Sockelbetrag 50%
- **Worst Case:** Score <50 → DEFCON 1 → Ersatz-Analyse (GOOGL FLAG aktiv → ZTS/VEEV-Alternative)
- **Ersatz bereit:** GOOGL (FLAG aktiv!) → kein sofortiger Tausch möglich
- **Moat-Status:** 19/20 unverändert — Wide Moat strukturell intakt (Azure, M365, Switching Costs)

### TMO — DEFCON 2, Clario-Watch
- **Score:** 62/100 | **DEFCON:** 🟠 2 | **Stand:** 16.04.2026 (v3.5 RS-Shift: -3P, D3→D2)
- **Sparrate:** 50% (D2, kein 🔴 FLAG → Gewicht 0.5)
- **Verbesserungen seit 02.04.:** Net Debt/EBITDA 3.6x → 2.57x ✅ | Fwd P/E 27x → 19.9x ✅ | P/FCF 35x → 29.2x ✅
- **Schwächen:** ROIC 2.6% Q (Goodwill $49.4B) | FCF -13.4% YoY | Unter 200MA
- **Trigger für DEFCON 4:** FCF Yield >4% (= FCF >$7.3B bei aktuellem Kurs) + ROIC Aufwärtstrend
- **Trigger für ZTS-Aktivierung:** Score <50 oder Moat-Downgrade oder FCF weiter rückläufig nach Q1
- **Entscheidung:** Q1 Earnings 23.04.2026 — alles oder nichts
- **Gelernt:** ROIC < WACC ist harter Malus auch bei Wide Moat. Goodwill-bereinigter ROIC wäre deutlich höher, aber GAAP-Basis ist Scoring-Pflicht.

### APH — DEFCON 3, FLAG aktiv (Analyse 09.04.2026 | Tariff-Check 15.04.2026)
- **Score:** 61/100 | **DEFCON:** 🟡 3 | **FLAG:** 🔴 aktiv (Score-basiert, nicht Tariff-Schwelle)
- **Sparrate:** 0 € (FLAG überschreibt — Score 61 = DEFCON 3, aber FLAG aus Gesamtbewertung)
- **Tariff-Check 15.04.2026:** Revenue China FY2025 = **14.7%** ($4.58B / $31.1B) — knapp unter 15%-Notiz-Schwelle. Kein Revenue-FLAG ausgelöst.
- **Supply-Chain:** Produktionsstandorte CN/MY bestätigt (Q1 2025 Earnings Call, Adam Norwitt). Kombinierte Exposure CN+MY+VN ~17–22% → Risk-Map-Notiz-Pflicht aktiv (15–35%-Band).
- **China-Trend:** Rückgang von 23% (2023) → 20% (2024) → 14.7% (2025) — strukturell positiv durch CommScope-Akquisition + Diversifikation.
- **Management-Mitigation:** „Purpose built" dezentrale Struktur, Pricing Power bestätigt (Q1 2025 Call).
- **FLAG-Klärung:** FLAG bleibt aktiv — Basis ist Score 61 (DEFCON 3 mit Sparrate 0€ nach FLAG-Logik). Kein separater Tariff-FLAG nach Regelwerk (Revenue <15%).
- **Nächste Aktion:** Q2 2026 Earnings (23.07.2026) — Revenue-Trend China + Manufacturing-Mitigation beobachten.

---

## 4. Score-Register

→ **Aktueller State:** [`Faktortabelle.md`](Faktortabelle.md) — Live-Score + DEFCON + FLAG pro Ticker
→ **Portfolio-Snapshot:** [`PORTFOLIO.md`](PORTFOLIO.md) — Section "Portfolio-State (11 Satelliten)"
→ **Vollständige Historie:** `05_Archiv/score_history.jsonl` — alle Score-Records append-only (ab 17.04.2026 forward, Backfill-Records aus damaliger Section-4-Tabelle)
→ **FLAG-Events:** `05_Archiv/flag_events.jsonl` — Trigger + Resolution append-only
→ **Write-Tooling:** `03_Tools/backtest-ready/archive_score.py` + `archive_flag.py`

*Score-Register-Tabelle seit 2026-04-17 in JSONL-Archiv migriert. Backfill-Stand: 24 Score-Records + 2 FLAG-Events (MSFT/GOOGL capex_ocf). Vormals an dieser Stelle stehende 24-Zeilen-Tabelle: archiviert im git-Commit pre-Phase-2 (siehe Commit-Historie 17.04.2026) und maschinenlesbar in `score_history.jsonl` rekonstruiert.*

---

## 5. Scoring-Lektionen (gelernte Regeln)

### Goodwill-Malus
M&A-Akquisitionen verzerren ROIC nach unten und die Bilanz nach oben.
→ Net Debt/EBITDA >3x = 0/3 Punkte im Bilanz-Block
→ Non-GAAP bereinigter ROIC darf als Zusatzinformation genannt werden, aber GAAP-Wert ist Scoring-Basis
→ **Referenz:** SNPS (Ansys $26.88B Goodwill = -3 Punkte), SPGI (IHS Markit $44B)

### ROIC < WACC = harter Malus
Auch bei Wide Moat: Wenn das Unternehmen kein Kapital oberhalb seiner Kapitalkosten verzinst, ist das ein fundamentales Problem.
→ Score: 2/8 bei ROIC ~WACC, 0–1 bei ROIC < WACC
→ **Referenz:** TMO (ROIC 9,37% vs. WACC 9,99%)

### FLAG ist absolut
Ein aktives FLAG überschreibt jeden Score. Es gibt keine "Score ist ja trotzdem gut"-Argumentation.
→ CapEx/OCF >60% = FLAG, auch bei DEFCON 4 Score
→ **Referenz:** MSFT (Score 60, DEFCON 2, FLAG aktiv = Sparrate komplett gestoppt, 0 €)

### Cashless Exercise ≠ Insider-Selling
Transaktionen mit Code M+S, gleicher Tag, Expiry ≤30d = automatische Ausübung aus Plan.
→ Kein diskretionäres Signal, kein FLAG-Trigger
→ **Referenz:** FICO-Analyse 03.04.2026

### Datenlücken → konservativ scoren
Wenn Insider-Daten oder Technicals nicht verifizierbar sind: Pflichtmalus.
→ Insider 3/10, Technicals 5/10 als Minimum bei unvollständiger Datenlage
→ **Referenz:** EXPN (Non-US, LSE-Ticker)

### TTM-Verzerrung bei Kurscrash
Bei Titeln mit >40% Kursrückgang: TTM-Metriken verzerren nach oben.
→ Forward-Metriken als Primärbasis, TTM als Kontext
→ **Referenz:** FICO (TTM P/FCF 34x vs. Fwd P/FCF ~19x bei -52% Crash)

### Pre-Processing Layer (v3.3 — 06.04.2026)
Vier Regeln müssen vor jedem Scoring angewendet werden:
- **Regel 1:** SBC/OCF ≥15% → Dokumentationspflicht (kein Score-Malus, nur Transparenz)
- **Regel 2:** Finance Lease Obligations >$5B → manueller 8-K-Check vor CapEx-FLAG (Shibui kann Lease-Payments nicht isolieren)
- **Regel 3:** CapEx-Qualität → Growth vs. Maintenance aus Earnings Call — kein automatisches Veto, nur Risk-Map-Notiz
- **Regel 4:** M&A Amortization → Proxy: NOPAT + (D&A × 0,65) / Invested Capital. Nur bei Goodwill >30% Assets aktiv. Pflichthinweis "Proxy, nicht GAAP".

### API-Sanity-Check-Lücke IFRS (v3.3 — 06.04.2026)
Shibui Finance hat keine primäre Coverage für ASML, RMS, SU (Euronext-Titel).
→ Non-US: EODHD API als Primärquelle, Toleranz ±1,5% (IFRS-Ermessen)
→ US: Shibui + defeatbeta, Toleranz ±0,5%
→ Hermès (RMS) + Schneider (SU): nur halbjährliche Berichte — Sanity-Check H1/H2

### SEC EDGAR 10b5-1 Footnote-Luecke (v1.0 Insider-Modul)
Viele Insider-Verkaeufe (besonders bei Broadcom) erscheinen im Form-4-XML als "diskretionaer",
obwohl sie faktisch nach RSU-Vesting stattfinden. Das liegt daran, dass nicht alle Unternehmen
das 10b5-1-Stichwort explizit in den Filing-Footnotes verwenden.
→ **OpenInsider Gegencheck bleibt HEILIG** — besonders bei AVGO, wo Tan/Brazeal/Spears
  regelmaessig hohe Post-Vesting-Verkaeufe taetigen.
→ Bei FLAG-Trigger durch Insider-Modul: Immer manuell auf openinsider.com Spalte "X"/"M" pruefen
  bevor FLAG aktiviert wird.
→ **Referenz:** AVGO 06.04.2026 — Modul zeigt $123M FLAG, aber viele Transaktionen sind
  vermutlich Post-Vesting (Code F/S am gleichen Tag wie A/M).

### Non-US Kalibrierungsanker: ASML (06.04.2026)
**Erster vollständiger DEFCON-Anker für IFRS/Euronext-Titel.**
- Score 68 = Wide-Moat-Monopol zu Premium-Bewertung (Fwd P/E 38x, P/FCF ~41x)
- Fundamentals 28/50 als Referenz: wie teuer ein Monopol sein darf bevor Score kippt
- Moat 19/20 als Non-US-Referenz für "bestes vorstellbares europäisches Unternehmen"
- Routing: Shibui für Technicals (ASML.NASDAQ ADR) + Web für IFRS-Fundamentals
- eodhd_intel.py: in Cowork-Session blockiert (yfinance nicht installierbar in Sandbox) → bei Code-Session verwenden
- **Fazit:** Ein 68er Non-US-Score bei tadelloser Qualität = Bewertungsproblem, kein Qualitätsproblem. Referenz für zukünftige ASML/RMS/SU-Analysen.

### Tariff Exposure als Scoring-Malus (v3.1)
Bei Unternehmen mit signifikanter Produktion in Risikoländern (Malaysia, Thailand, China):
→ Tariff Exposure Score als Minus im Fundamental-Block
→ **Referenz:** AVGO (~35% Revenue US-Halbleiter, Produktion Malaysia/Thailand = -1 Punkt)

### 4-Paper-Triage für §29 Retrospective-Gate (v3.7 — 19.04.2026)
**Trigger:** User-geführte Triage 4 akademischer Paper (Bailey 2015 PBO/CSCV, Aghassi 2023 AQR Fact/Fiction, Flint/Vermaak 2021 Decay, Palomar 2025 Portfolio Optimization Ch 6 + 8).
**Befund:** Keine der 4 Paper rechtfertigt Scoring-Schema-Änderung — Applied-Learning-Regel "Paper-Ingest ≠ System-Update" in allen 4 Fällen bestätigt. Wert liegt in neuem §29-Gate-Framework, nicht in DEFCON-Modifikation.
**Regel:**
→ `valuation_z_score` als Watch-Metric **verworfen** nach 3× Oszillation — Evidence-Mismatch (AQR-Value-Spread ist Long-Short-Cross-Section, unser Signal wäre Single-Ticker-MR mit schwächerer akademischer Basis). Statt Column: einzeilige !Analysiere-Checklist (Fwd P/E gegen eigene 5J-Range, keine Score-Wirkung).
→ §28.3 war bereits belegt ("Nicht-Migration-Trigger") — neues §29 für Retrospective-Gate statt §28.4. Thematisch sauber (§28 = Migration-Workflow, §29 = Retrospective-Validation).
→ Seven-Sins-Gate (§29.5) greift **bereits jetzt** bei Migration-Events — nicht erst 2028.
→ Harvey/Liu/Zhu t-Stat ≥ 3 Hurdle (§29.4) greift **bereits jetzt** prospektiv auf alle neuen DEFCON-Sub-Komponenten.
→ Risk-Metrics-Skill existiert bereits (`anthropic-skills:risk-metrics-calculation`) — Portfolio-Return-Persistenz-Setup JETZT starten (Sin #2 Look-Ahead proaktiv vermeiden), Aktivierung erst 2028.
**Präzedenz:** 4-Paper-Triage-Workflow-Disziplin — Vault-first, dann System; Advisor-Validierung bei Oszillation; Locked-Wording vor Execution.

### R5 Portfolio-Return-Persistenz aktiviert (v3.7.2 — 19.04.2026)
**Trigger:** Phase 3 Paper-Integration systemweit (Spec 976e67a, Plan ee61535).
**Befund:** `portfolio_returns.jsonl` + `benchmark-series.jsonl` live. Daily-Schema v1.0 mit `schema_version` pro Record, Cashflow-Trennung, Duplicate-Date-Guard auf beiden JSONL-Files, **Trading-Date statt Wall-Clock** (Codex-Fix #1: Look-Ahead-Prevention via yfinance `common.index[-1]`). Erster Record: date=2026-04-17 (Friday, Session-Start am Sonntag), Portfolio 10.173,42 EUR, SPY 710,14 — notional-Start 10.000€.
**Regel:**
→ Jeder Handelstag (oder Montag wenn über Weekend gelaufen): `python 03_Tools/portfolio_risk.py --persist daily --cashflow <euro>`. Sparraten-Tage explizit mit `--cashflow 285.00`.
→ Cashflow-Trennung: `portfolio_return` ist reine Marktbewegung, `portfolio_value_gross` = `V_prev * (1+r) + cashflow_net` (post-cashflow NAV).
→ Git-Commit der JSONL-Dateien zusammen mit STATE-Update pflicht (§18 Sync-Pflicht — alle sechs).
→ **Interim-Gate 2027-10-19** (18M Dry-Run `risk-metrics-calculation` + PBO-Smoke-Test) adressierbar erst nach 540+ Records.
→ **Review-Gate 2028-04-01:** Vollaktivierung §29.6 (Palomar Ch 6 Metriken: Sortino/Calmar/Max-DD/CVaR/IR).
**Codex-Code-Review-Gate:** 5/5 Findings akzeptiert + applied — (1) trading-date, (2) dual-file duplicate-guard, (3) hard-fail on missing ticker via common-date intersection, (4) mixed-currency caveat im Docstring + Schema-Doc, (5) schema-doc post-cashflow-NAV-Wording.
**Mixed-Currency-Caveat:** USD+EUR-Titel werden aktuell lokalwährungs-gemittelt (synthetischer Local-Return-Index). FX-Conversion vor §29.2 AQR-Benchmark-Vergleich pflicht → Interim-Gate 2027-10-19.
**Präzedenz:** Sin #2 Look-Ahead-Prevention operational durch frühen Persistenz-Start (Codex-Scope-Review 19.04. identifizierte R5 als Blind-Spot in R1-R4-Liste). Codex-Code-Review 19.04. identifizierte zusätzlich Wall-Clock-Date-Bias (Sonntag-Tag mit Freitag-Daten) — Fix via yfinance-Trading-Date bestätigt die Wichtigkeit des Post-Hoc-Reviews.

### R1 §30 Live-Monitoring aktiviert (v3.7.2 — 19.04.2026)
**Trigger:** Phase 4 Paper-Integration systemweit (Spec 976e67a, Commit c1f0f21 Draft + Post-Codex-Revisions).
**Befund:** §30 Live-Monitoring & Cadence aktiv in INSTRUKTIONEN.md (v1.11). Monthly-Refresh pflicht für aktive Investment-FLAGs (Flint-Vermaak Investment-Half-Life ~1M).
**Regel:**
→ **Aktuelle Scope:** MSFT CapEx/OCF 83.6% → Monthly-Refresh pflicht (erster Refresh ~19.05.2026, Zwischen-Refresh vor Q3-Earnings 29.04. nicht nötig — Earnings-Trigger deckt ab)
→ **TMO** fcf_trend_neg bleibt **Schema-Watch**, keine §30-Pflicht (Q1 23.04. = natürliches Resolve-Gate)
→ **§30-Ausweitung** auf weitere Faktor-Klassen (Quality/Value/Momentum) erfordert Applied-Learning-Re-Review — Re-Review-Entscheidung dokumentiert als eigene CORE-MEMORY §5-Lektion (Codex-Wächter 19.04.)
→ **Drei-Ebenen-Semantik-Trennung:** "Aktiver FLAG" (§30, flag_events.jsonl-Trigger, Monthly-Refresh pflicht) ≠ "Schema-Watch" (schema-getriggert-nicht-aktiviert, kein flag_events-Pfad) ≠ PORTFOLIO.md "Aktive Watches" (allgemeine Beobachtungsnotiz, kein FLAG-Mechanik)
→ **FLAG-Events ändern nur FLAG-Status, niemals Score-Komponenten/-gewichte** — §30 ist Monitoring-Cadence-Regel, kein Scoring-Change
→ **Forward-dating-Pflicht:** Monthly-Refresh-Events in flag_events.jsonl nur mit aktuellem Refresh-Datum (kein Backfill ohne Kennzeichnung — §29.5 Sin #2)
**Codex-Review-Revisions appliziert (5/5):** Score-Unverändbarkeit (§30.3.5), Schema-Watch-Klarstellung (§30.1), Applied-Learning-Re-Review-Ablage (§30.4), Drei-Ebenen-Disambiguierung (§30.1), Forward-Dating-Anker (§30.3.3).
**Präzedenz:** Applied-Learning "Paper-Ingest ≠ System-Update" in Monitoring-Layer operationalisiert. §30-Entscheidung ist NICHT Score-Update — die Monthly-Refresh ist neue Cadence-Regel, nicht neue DEFCON-Logik.

### Phase-2-System-Konsequenzen der wissenschaftlichen Fundierung (20.04.2026)

**Auslöser:** User-Frage "Fließt die Wissenschaftliche-Fundierung-DEFCON automatisch in jede Analyse ein, oder ist das toter Content?" — ergab, dass §4 Befunde-Priming nur B1-B11 abfragte (stale seit Phase-1a+1b-Ingest = B12-B24). Codex-konsultiertes Setup (`codex-rescue` Agent `af272d556e2707209`): Hybrid A+B+C-Architektur.

**Systemkonsequenzen (Phase 2, docs + SKILL.md-Output-Only, KEIN Scoring-Impact):**

1. **Status-Matrix in [[Wissenschaftliche-Fundierung-DEFCON]] §Status-Matrix** — kanonische Klassifikation jedes Befunds (B1-B24+) mit 4 Labels: `active-scoring` / `meta-gate` / `design-rejected` / `future-arch`. Single Source of Truth; ohne Status-Label kein Phase-1-Complete bei zukünftigem Ingest.
2. **INSTRUKTIONEN §4 Befunde-Router** — Mini-Tabelle B1-B11 durch Status-Router ersetzt (Aktion pro Label, Pflicht-Abfolge 4 Schritte, §4 wächst nicht mehr mit neuen Papers mit).
3. **INSTRUKTIONEN §2 Pipeline-Schritt [BEFUNDE]** — Status-Matrix-Check explizit zwischen Stufe 1 und Stufe 2 sichtbar; kein Filter-Tor, sondern Pflicht-Vorbereitung für Scoring.
4. **INSTRUKTIONEN §29.5 Regime-Audit-Addendum (B19 FINSABER)** — Bull/Bear-Subsample-SR-Trennung + Symbol-Breite + Zeitfenster-Deklaration bei Migration-/Retrospective-Events.
5. **INSTRUKTIONEN §29.6 Composite-Objective-Alignment (B20 GT-Score)** — Downside-Risk-Komponente konzeptuell deckungsgleich mit Palomar Sortino/CVaR; GT-Score als In-the-Loop-Objective, Palomar als Einzel-Metrik-Rechnung.
6. **INSTRUKTIONEN §33 NEU Skill-Self-Audit-Gate** — Gates 1/2/3 aus [[Knowledge-Graph-Architektur-Roadmap]] kodifiziert, Scope = KG/RAG/Agentic-Reflection/DPO-Architekturen; Decision-Output ADOPT/DEFER/REJECT; 3 Beispiel-Anwendungen aus Phase-1b (Form-4-KG REJECT, 10-K-KG DEFER, Bayesian-RAG-Briefing DEFER). §§31-32 als Track-5b/5a-Reservierung dokumentiert.
7. **SKILL.md dynastie-depot — Schritt 2.5 Befunde-Check + Output-Template-Erweiterung** — pro DEFCON-Block "**Befunde angewendet:**"-Zeile im Analyse-Output; Transparenz-Only, kein Score-Impact.

**Szenario-Entscheidungen aus [[Knowledge-Graph-Architektur-Roadmap]] v0.1** (via §33 Skill-Self-Audit-Gate):
- **Szenario 1 (Form-4 Insider bleibt XML):** **REJECT** — Gate 1 negativ (XML genügt, Schema stabil); Status quo bestätigt.
- **Szenario 2 (10-K-KG für Cross-Entity-Queries):** **DEFER** frühestens 2027+ — Gate 1/2/3 alle conditional; Re-Review bei konkretem Multi-Hop-Bedarf.
- **Szenario 3 (Bayesian RAG im Morning-Briefing):** **DEFER** bis Self-hosted-Embedding-Wechsel — Gate 2 negativ (Tavily-API erlaubt kein MC-Dropout).

**Constraint eingehalten:** Kein Touch an `01_Skills/dynastie-depot/config.yaml`; keine DEFCON-Parameter-Änderung; keine v3.8-Migration nötig (v3.7 bleibt). Skill-Version **bleibt v3.7.2** (Output-Format-Erweiterung ohne Funktions-Änderung, §28.3 Nicht-Migration-Trigger).

**Phase-2.5 Codex-Gate:** Separates Codex-Review bestätigt Layer-Trennung Docs/Audit ↔ Skill-Output ↔ config.yaml unberührt (ausstehend zum Zeitpunkt der Lektions-Anlage).

**Applied Learning:** Wissenschaftliche Fundierung wird **aktiv** genutzt, wenn (1) jeder Befund per Status-Matrix klassifiziert ist, (2) der Router in §4 mechanisch auf das Status-Label reagiert, (3) der Analyse-Output die Anwendung sichtbar macht. Dead reference wird so strukturell unmöglich — B25+ landet automatisch in der Matrix oder Phase-1 gilt als incomplete.

**Präzedenz:** Erste formale Aktivierung der wissenschaftlichen Fundierung auf Workflow-Ebene. Vorher waren Papers Anker für §§ (retroaktiv), jetzt sind sie Input-Layer des Scoring-Starts (proaktiv).

---

## 6. System-Upgrades & Versionsverlauf

Nur Versions-Changelog. Narrative Meilensteine stehen in §13.

| Datum | Komponente | Version | Kurz-Delta |
|---|---|---|---|
| 2026-03-31 | Rebalancing_Tool | v3.1 FINAL | Allokation 65/30/5, Gleichgewichtung 11 Satelliten (2,73%) |
| 2026-04-01 | config.md Struktur | — | Single-Source-of-Truth etabliert |
| 2026-04-03 | DEFCON-Scoring | v3.1 | SBC/Revenue, Accruals, GM-Trend, Pricing Power, Relative Stärke, 200MA Slope, DCF-Anker, EPS-Revision, PT-Dispersion, Tariff Exposure |
| 2026-04-15 | Rebalancing_Tool | v3.4 | Sparraten-Logik überarbeitet (D4/D3=1.0, D2=0.5, D1/FLAG=0€) |
| 2026-04-16 | DEFCON-Scoring | v3.5 | Scoring-Audit-Fix (PT-Upside Double-Counting, Relative-Stärke 0–3) |
| 2026-04-17 | DEFCON-Scoring | v3.7 | System-Gap-Release (v3.6 verworfen) — QT-Interaktionsterm, OpM TTM, Analyst-Bias, Cap 50 |
| 2026-04-17 | dynastie-depot Skill | v3.7.1 | Backtest-Ready Forward-Pipeline, Schritt 6b + 7 |
| 2026-04-18 | DEFCON-Schema | v3.7 | Threshold-Drift-Fix 80/65/50 (D3/D4-Labels) |
| 2026-04-19 | backtest-ready-forward-verify | v3.7.2 / semver 1.0.0 | Skill deployed — Pipeline-Kapsel P1-P6 |
| 2026-04-22 | system_audit | v1.0 | Drift-Audit-Tool + `/SystemAudit` |
| 2026-04-24 | CLAUDE.md | Routing-Refactor Tier 1 | Routing-Table + APPLIED-LEARNING + TOKEN-RULES |
| 2026-04-24 | 00_Core Struktur | Tier 2 | STATE-Split + CORE-MEMORY §1→§12/§13 |
| 2026-04-24 | dynastie-depot Skill | v3.7.3 | 00_Core-Refactor-Adoption |
| 2026-04-24 | backtest-ready-forward-verify | semver 1.0.1 | 00_Core-Refactor-Adoption |

---

## 7. Steuer-Erinnerungen

- **Freistellungsauftrag:** ING 1.500–1.600€ (Vorabpauschale), Scalable 400–500€ (Dividenden)
- **FIFO-Klon-Strategie:** 10–15 Jahre vor Entnahme starten
- **NV-Bescheinigung Kind:** bis 13.384€/Jahr (Stand 2026) steuerfrei
- **Lombardkredit:** Alternative zu Verkauf — immer erst prüfen bevor verkauft wird
- **Rebalancing:** Niemals durch Verkauf — immer Sparplan umleiten

---

## 8. Nächste offene Entscheidungen

| Entscheidung | Wann | Optionen |
|-------------|------|---------|
| MSFT FLAG auflösen oder Veto? | 29.04.2026 (Q3 Earnings) | Auflösung wenn CapEx/OCF <60% / Veto wenn nicht |
| TMO DEFCON 4 oder Tausch? | 23.04.2026 (Q1 Earnings) | Aufstieg wenn FCF >4%, Net Debt/EBITDA <3.0x |
| Slot 16 — PEGA Einstieg? | Mai 2026 (Earnings) | PEGA Score 85 — Earnings-Check entscheidend |
| Sparplan-Booster-Strategie | Juni 2026 | 9.500€ Bausparvertrag + 2.000€ Steuererstattung einsetzen |

---

## 10. API-Audit-Log (Quarterly Sanity Check)

**Format:** Datum | Ticker | OCF-Abweichung | CapEx-Abweichung | Status
**Toleranz:** US ±0,5% | Non-US (IFRS) ±1,5%
**Nächster Check:** Mai 2026 (Q2-Check: V, BRK.B, TMO)

| Datum | Ticker | OCF | CapEx | SBC | Status |
|-------|--------|-----|-------|-----|--------|
| 07.04.2026 | ASML | IFRS 16 vs. ASC 842 Δ ~10% strukturell (Leasingzahlungen) — kein API-Drift | Δ ≤ 3.5% (yfinance addiert Intangibles) — plausibel | n/a | ✅ RESOLVED — FLAG-Schlussfolgerung unter beiden Standards identisch: Clean |
| — | RMS | — | — | — | ⏳ PENDING — H1 2026 Bericht (Juli/August) |
| — | SU | — | — | — | ⏳ PENDING — H1 2026 Bericht (Juli/August) |

### 21.04.2026 Mittag — Drift-Audit-Sweep (pre-Provenance-Plan-Execution)

**Scope:** Systemweiter Drift-Scan aller persistierten Stores + config.yaml als Vorbereitung auf Provenance-Gate-Plan-Execution (TMO Q1 23.04.).

| Store | Result |
|-------|--------|
| `05_Archiv/score_history.jsonl` | **12/27 FAIL** → migriert via `migrate_defcon_drift.py` → **27/27 PASS** (alle defcon_level-Drift, keine Score-/Block-Drift) |
| `05_Archiv/flag_events.jsonl` | 2/2 PASS (keine Drift) |
| `dynastie-depot/config.yaml` Satelliten Score+DEFCON | 11/11 == PORTFOLIO.md (keine Cross-Source-Divergenz) |
| `05_Archiv/portfolio_returns.jsonl` | 1 Record (17.04.) — **stale seit 4 Tagen** (R5-Phase-3 aktiv aber Daily-Append-Cron existiert nicht, Manual-Trigger-Pflicht vergessen) → Backlog-Item (Auflösung in Track 4 ETF/Gold-Erweiterung) |
| `05_Archiv/benchmark-series.jsonl` | 1 Record (17.04.) — stale analog (siehe oben) |

**NICHT durchgeführt in diesem Sweep:** Markdown-Cross-Source-Validation, Existence-Check (CLAUDE.md/STATE.md-Pfade), Skill-Version-Check, Vault-Backlink-Integrity, docs/superpowers-vs-STATE-Referenzen. **Grund:** dedizierte Exhaustive-Validation via `03_Tools/system_audit.py` in Session 22.04. (Phase D+E).

**Lesson Learned:** „Drift-Check" war bisher implizit Spot-Check (Sampling prominenter Zeilen). 12/27 silent-Drift beweist, dass nur exhaustive Schema-Validation aller Records zuverlässig ist → §27.4 Vertikal-Drift-Klausel.

### 22.04.2026 — System-Audit-Tool v1.0 deployed (Phase E 18/19)

**Scope:** Exhaustive Drift-Audit via `03_Tools/system_audit.py` + Slash-Command `/SystemAudit` + INSTRUKTIONEN §27.5 Migration-Regression-Guard. Spec v0.2 ratified `82482d7`; Plan `docs/superpowers/plans/2026-04-21-system-audit-tool.md` Tasks 1-18 done (Task 19 Acceptance-Matrix offen).

| Check | Kategorie | Status Baseline |
|-------|-----------|----------------|
| Check-1 `jsonl_schema` | Core | ✅ PASS 31/31 |
| Check-1.5 `store_freshness` | Core | ✅ PASS 2/2 (WARN-Severity bei Daily-Persist-Stale) |
| Check-2 `markdown_header` | Core | ❌ FAIL 1/3 — Future-Date-Bug (Long-Term-Gate-Rows als Event gewertet); Follow-up-Task #2 |
| Check-3 `cross_source` | Core | ⚠️ WARN 22/22 (Watch-informativ) |
| Check-4 `existence` | Core | ❌ FAIL 54/186 — CLAUDE.md-Pfadreferenzen ohne `00_Core/`-Prefix; deferred Post-Task-17-Cleanup-Welle |
| Check-5 `skill_version` | Core | ⚠️ WARN 1/2 (ZIP-Packaging ausstehend) |
| Check-6 `pipeline_ssot` | Core | ✅ PASS 3/3 |
| Check-7 `log_lag` | Core | ✅ PASS 1/1 |
| Check-8 `vault_backlinks` | Optional | ✅ PASS (29ms) |
| Check-9 `status_matrix` | Optional | ✅ PASS |

**Pragmatischer Regression-Gate:** `--minimal-baseline` (Check-1 + Check-6 + Check-7) = 3/3 PASS, rc=0. Das sind die 3 strukturellen Invarianten, die ein `migrate_*.py`-Run nicht brechen darf. `--core` erst nach Check-3-Fix + existence-Cleanup als Gate hochgezogen (Rollback-Pfad in §27.5-Body dokumentiert).

**Plan-Header-Notices dokumentiert 2 Spec-Drifts (Spec v0.2 frozen):**
1. Task 15 Baseline-Smoke rc==0 → rc∈{0,1} (Codex-Reconciliation Option 2, Commit `486f2c1`).
2. Task 17 Regression-Guard `--core` → `--minimal-baseline` (User-Entscheidung A pragmatisch per SESSION-HANDOVER, Commit `ab7ae19`).

**Codex-Reconciliation-Verdikt:** RECONCILED. Keine Spec-v0.3-PR nötig. Erster echter Tool-Einsatz: Pre-TMO-Q1 23.04.2026 + jede Folge-Migration.

**Lesson:** Tool-Bugs (Check-3 + Check-5) wurden nur durch Live-Baseline-Run im temp-Repo entdeckt — in-process Fixtures waren synthetisch und haben den Future-Date-Bug nicht getriggert. Generalisiert: synthetische Test-Fixtures decken Parser-Bugs nicht ab, die erst mit realem Content triggern. → Applied Learning Kandidat.

### 22.04.2026 Spät — Task 19 Verification + Fix-Welle E (Phase E ~95%, Closure pending CR-Re-Run)

**Scope:** Acceptance-Matrix gegen Spec §12 (11 Items), 2. obligatorischer 4-Wege-Review-Pass (Codex + CodeRabbit). Final-Closure aufgehoben bis CodeRabbit-Re-Run nach Cooldown.

**Acceptance-Matrix-Resultat:** 9/11 ✅ PASS, 2 dokumentierte WARNs.
- ⚠️ Item 2 (`--core` rc=0): Drift, `--core` rc=1 wegen bekannter Tool-Bugs Check-3 + Check-5 → `--minimal-baseline` rc=0 ist pragmatischer Regression-Gate per §27.5 + Plan-Header-Notice Task 17. Codex-Verdikt: legitim dokumentiert.
- ⚠️ Item 9 (`--full` 9 Checks): Tatsächlich 10 Checks im Output (1.5 als verstecktem Sub-Check + Optional 8/9 + Check-10). Codex-Verdikt: Notation-Drift, kein substantive Issue. **Check-10 status_matrix Over-Strict-Bug entdeckt** (Regex `\bB(\d+)\b` fängt narrative B-Refs in Status-Matrix-Section als Duplicates → Codex-Empfehlung Regex-Scope auf `### Matrix`-Subsection einengen, Post-Closure-Welle).

**Codex-Reconciliation-Verdikt:** **RECONCILED_WITH_FOLLOWUPS**.
- Plan-Header-Notices nach `feedback_spec_section_drift.md`-Pattern PASS.
- §27.5-Wortlaut konsistent zu §27.4-Präzedenz PASS.
- 3 Codex-Follow-ups: (a) Backlog Check-3+existence-Cleanup → §27.5 Guard auf `--core` hochziehen; (b) Post-Closure Check-10 Regex-Scope; (c) §27.5-Kommentar-Update nach (a).

**CodeRabbit-Pass:** 6 Findings in Run-1, davon 4 sichtbar (tail-Truncation): 3 valide auf `_smoke_temp_repo.py` ✅ FIXED in Fix-Welle E `e3ba381` (Docstring-Korrektheit „60s"→„120s" Inkonsistenz zur assert delta<120, `import re` Modul-Level-Hub, redundanter Inline-Import-Block aus `smoke_seeded_drift()` entfernt). 1 Finding `flag_events.jsonl:2` pre-existing OOS. Re-Runs: Run-2 zeigte 1 Finding (Subset, Non-Determinismus); Run-3 rate-limited (~46 min). 2 truncated Findings unklar → Re-Verify als Backlog-Punkt gegen `e3ba381` als neue Base.

**Closure-Entscheidung (advisor-validiert):** Final-Commit `log(phase-e-done)` aufgehoben — Closure-mit-2-unbekannten-CodeRabbit-Findings widerspricht `feedback_correctness_over_runtime.md`. Re-Run nach Cooldown ist „one cache miss buys certainty".

**Commits dieser Sub-Session (2):** `e3ba381` (Fix-Welle E) + dieser Sync-Welle-Commit.

**Lesson:** Bei Multi-Tool-Reviews (Codex + CodeRabbit) Run-Output IMMER in File persistieren (`> /tmp/cr_*.txt 2>&1`), nicht nur tail-Inspect. Run-1 Truncation hätte vermieden werden können — Bash-tail wegen Grenzwert + Re-Run Non-Determinismus + Rate-Limit = perfect storm. → Applied Learning Kandidat: „Review-Tool-Output frühzeitig File-persistieren".

**Next:** CodeRabbit-Re-Run gegen `e3ba381` nach Cooldown (>22.04. ~23:23 UTC). Bei keinen neuen Blockern: Final-Commit `log(phase-e-done)` + Banner 19/19 + Übergang zu Phase F (Provenance-Plan-Execution) bzw. direkt Phase G (TMO Q1 23.04.).

### 22.04.2026 Spät-Nacht — Phase E 19/19 DONE ✅ + Pfad-2-Entscheidung

**CodeRabbit-Re-Run (post-Cooldown 23:25 UTC gegen `e3ba381`):** **1 Finding total**, nitpick-severity.
- `03_Tools/Output/PORTFOLIO-RISK-2026-04-17.md:39`: „Top-3 Risk-**Treiber**" vs „Risk Drivers" (DE/EN-Mix)
- **Scope:** Out-of-Scope Phase E — File ist Auto-Output von `portfolio_risk.py` vom 17.04., nicht von Tasks 15-19 berührt
- **Triage:** dokumentieren + close (Ästhetik-Nitpick, Projekt ist bewusst DE/EN-gemischt; Fix müsste im Generator sein, nicht im Auto-Output)
- 2 truncated Findings aus Run-1 haben sich durch Fix-Welle E aufgelöst (wären sonst wieder aufgetaucht)

**Phase E Final-Status:**
- Tasks 1-19 substantive done
- Codex-Pass RECONCILED_WITH_FOLLOWUPS (3 deferred Follow-ups)
- CodeRabbit-Pass: 4 Phase-E-Findings in Fix-Welle E fixed (`e3ba381`), 1 OOS-Nitpick + 1 pre-existing OOS dokumentiert
- Acceptance-Matrix Spec §12: 9/11 ✅ + 2 dokumentierte WARNs

**Pfad-2-Entscheidung (Provenance-Plan-Timing):** User-Kontext „Weekly-Limit bei 93%, Reset Do 23.04. 22:00 CEST" + TMO-Earnings-Zeit **Do 14:30 CEST (8:30 AM ET, pre-market + Conference-Call gleichzeitig)** = Minimal-Modus-Fenster deckt TMO-Analyse-Zeit vollständig ab. **Entscheidung:** TMO Q1 mit Old-Pipeline Pre-Reset, Provenance-Plan-Execution Post-Reset (Do Abend 22:00+ oder Fr 24.04.), Retro-Migration des TMO-Records im neuen Format. Lektion: „Critical vor TMO Q1"-Formulierung war Self-Imposed-Gate — Provenance-Gate-Nutzen ist in zukünftigen Appends, nicht retrospektiv.

**Vault-Hygiene-Zwischen-Commit (`09e629f`):** `.obsidian/graph.json` untrackt + gitignored (analog `workspace.json` `5623f03`), 3 leere User-Stub-Files gelöscht (`2026-04-21.md` 0 B, `Unbenannt.base` 41 B, `Unbenannt.canvas` 2 B — User-Bestätigung „versehentlich angeklickt"). Ermöglicht sauberen git-Status für Phase-E-Closure.

**Commits dieser Sub-Session (2):** `09e629f` (Vault-Hygiene) + Closure-Commit (dieser).

**Konsolidierungstag Fr 24.04.** geplant (User-Initiative, nach intensiver 5-Tages-Arbeitsphase 18.-22.04.): Backlog-Cleanup-only — Check-3-Fix + existence-Cleanup + Daily-Persist-Auto-Hook-Baustein + Morning-Briefing-v3.0.4-Hotfix + Tavily-Key-Rotation. Kein Neu-Scope. Entspricht Applied-Learning-Verhindung des „Deferred-deferred-deferred"-Anti-Patterns (3x-Aufschub von Check-3 + existence-Cleanup war Warning-Signal).

### IFRS 16 vs. ASC 842 — Strukturelle OCF-Differenz (Non-US Pflicht-Wissen)
Bei ASML (und allen IFRS-Titeln die auch US-ADR haben): yfinance zieht IFRS-EU-Meldung (ASML.AS Amsterdam).
Unter IFRS 16 → Leasingzahlungen (Tilgung) als Finanzierungs-CF → senkt OCF vs. US GAAP (ASC 842).
Differenz ~€1,2B/Jahr = normal für ASML-Leasingbasis. **Kein Fehler, kein Alert.**
→ Toleranz für Non-US OCF-Check: ±15% akzeptabel wenn Differenz mit Leasingbasis erklärbar.
→ CapEx-Toleranz bleibt ±1,5% (PP&E-Zahlen konvergieren unter beiden Standards).

---

## 11. Backtest-Ready Infrastructure (aktiviert 2026-04-17)

**Ziel:** Ab sofort jede `!Analysiere`-Ausgabe und jedes FLAG-Event maschinenlesbar append-only archivieren, damit 2028+ ein methodisch-seriöser Backtest möglich wird.

**Aktive Komponenten:**
- **Score-Archiv:** `05_Archiv/score_history.jsonl` — ein Record pro Vollanalyse/Delta/Rescoring (source=forward) + Backfill-Records aus Section-4-Rekonstruktion (source=backfill).
- **FLAG-Event-Log:** `05_Archiv/flag_events.jsonl` — Trigger + Resolution pro FLAG (4 Typen: capex_ocf, fcf_trend_neg, insider_selling_20m, tariff_exposure).
- **Write-Tooling:** `03_Tools/backtest-ready/` — schemas.py (14 Pydantic-Modelle + 4 Cross-Validators), archive_score.py, archive_flag.py (trigger/resolve/list).
- **Write-Pflicht:** SKILL.md Schritt 7 (Archiv-Write) + Schritt 6b (FLAG-Resolution-Check). Sync-Pflicht §18 auf 6 Dateien erweitert.

**Backfill-Stand 2026-04-17 (einmalig):**
- 24 Score-Records aus CORE-MEMORY Section 4 rekonstruiert. Sub-Score-Breakdown nicht rekonstruierbar — Block-gesamt als Fractional-Split 50/20/10/10/10, Sub-Scores 0 als ehrliche "nicht-rekonstruierbar"-Platzhalter. `defcon_version: "historical"` (nicht v3.7, da Backfill aus unterschiedlichen Scoring-Versionen stammt). `moat.rating: "narrow"` einheitlich → Quality-Trap-Validator deaktiviert bei Backfill.
- 2 FLAG-Records: `MSFT_capex_ocf_2026-01-15` (wert=83.6, Trigger-Datum Proxy Q2 FY26 Earnings), `GOOGL_capex_ocf_2026-03-15` (wert=null, Rohwert nicht dokumentiert, schwelle=60).
- **Nicht archiviert:** APH (score-basiert, nicht in FLAG-Typ-enum), AVGO (insider_selling Status=REVIEW_PENDING — keine Schätzung per Spec §9.2). Dokumentiert in `05_Archiv/_parser_errors.log`.
- **Override MSFT:** Emoji-DEFCON "🟡 3" bei GOOGL Score 72 → Validator-konsistent zu L4 angepasst (Score 70+ → L4 per Neueinstieg-Tabelle). Real-Portfolio-DEFCON 3 wegen FLAG ist nicht im Schema abgebildet (Limitation: FLAG-getriebener Effective-Downgrade ist Meta-Regel, nicht Score-Konsistenz).

**Interim-Review-Gates (Delta-Semantik):**
- **Trigger 1 — erster echter Delta-Lauf:** Sobald ein Forward-Record mit `analyse_typ: "delta"` ins Archiv läuft → Kurz-Review (20 Min): Welche Metriken fehlen? Trägt das Null-Pattern (SKILL.md Schritt 7) oder braucht es Carry-Forward-Logik?
  - **Befund 1 (2026-04-18, V Pre-Earnings-Experiment):** Delta-Pattern setzt eine **Forward-Vollanalyse** als Baseline voraus. Gegen einen Backfill-Placeholder (Sub-Scores = 50/20/10/10/10-Split, metriken_roh alle null) liefert das Null-Pattern + `LAST_VALUE IGNORE NULLS`-Resolver nur weitere Nullen → keine nutzbare Zeitreihe. **Konsequenz:** Erster Lauf pro Ticker **immer** `analyse_typ: "vollanalyse"`, auch wenn Baseline nur 1 Tag alt ist — Delta erst sinnvoll ab zweitem Lauf gegen echten Forward-Record.
  - **Befund 2 (2026-04-18, γ-Fix Schema-SKILL DEFCON-Threshold-Drift):** `schemas.py _check_defcon_level` benutzte alte Thresholds (70/60/50) während SKILL.md Neueinstieg + Bestandsüberwachung seit v3.x mit 80/65/50 arbeitet. Forward-Record `2026-04-18_V_vollanalyse` wurde mit falschem defcon_level=4 (Score 72) akzeptiert — unter Schema war das konsistent, unter SKILL wäre D3 korrekt. **Fix commit 18.04.:** `schemas.py` + `archive_score.py` Smoke-Tests auf neue Thresholds (Sub-Sum 80 statt 79). Impact: 5 Tickers (BRK.B/VEEV/SU/COST/RMS) in STATE.md/Faktortabelle von D4 auf D3 umgelabelt (Sparrate bei D3/D4-Übergang laut SKILL-Bestand identisch → keine operative Änderung); APH D3→D2 (FLAG überschreibt Sparrate weiter).
  - **Befund 3 (2026-04-18, V Scoring-Review via Advisor):** Drei Sub-Score-Korrekturen aufgedeckt, die den Score 72 auf 63 drückten: (a) Moat `pricing_power_bonus` ohne explizite Transcript-Belegung (SKILL-Regelbruch) — -1; (b) Insider `ownership` als Gradient statt Threshold gescored (V <1% → 1/3 nicht 2/3) — -1; (c) ROIC `Goodwill-Ausnahme` auf Nicht-M&A-Compounder angewendet (Regel-4-Gating GW/Assets 19,95% <30% greift nicht) — -7. **Konsequenz:** `2026-04-18_V_rescoring` Append mit Score 63/D2, Begründung in `notizen`. Erstes Rescoring-Präzedenzfall im Archiv. Gleichzeitig Diskussion: v3.5→v3.7-Algebra-Projektionen vom 17.04. für 8/11 nicht-verifizierte Tickers könnten stille Überschätzungen enthalten — bei jedem Earnings-Trigger Voll-Forward-Lauf, nicht Algebra.
  - **Befund 4 (2026-04-18, TMO FLAG-Entscheidung via Advisor — Schema-Validator ≠ SKILL-Regel-Semantik):** TMO Pre-Earnings-Vollanalyse lieferte Score 64/D2. `fcf_trend_neg` war **schema-technisch getriggert** (FY25 FCF 6293M vs FY24 7267M = -13,4% YoY, zusätzlich CapEx FY25 +8,9% YoY — beide Indikatoren erfüllten die mechanische Trigger-Regel). Advisor-Review verwarf den mechanischen Trigger und empfahl **Option B (struktureller Disclosure statt FLAG-Aktivierung)** aus drei Gründen: (a) **WC-Noise**: Working-Capital-Delta FY25 -1766M (vs -334M FY24, Δ = -1432M) erklärt den FCF-Rückgang -974M **überproportional** — der operative Cashflow-Kern ist intakt, der Einbruch ist Bilanz-Timing, kein Trend-Signal; (b) **4-Jahres-Plateau**: FY22-25 FCF $6,911M → $6,927M → $7,267M → $6,293M zeigt keinen Mehrjahres-Abwärtstrend, sondern Schwankungen um ein Plateau; (c) **Profitabilität intakt**: Operating Income FY25 +5,1% YoY (8110M vs 7717M) — Margin-Story lebt. **Konsequenz:** (1) Record `2026-04-18_TMO_vollanalyse` mit `flags.aktiv_ids=[]` + expliziter Begründung in `notizen`; kein FlagEvent-Write. (2) Q1 FY26 Earnings 23.04. = **natürlicher Resolve-Gate**: WC-Unwind + FCF-Recovery bestätigt → Disclosure bleibt Notiz; fehlende Reversibilität → `fcf_trend_neg`-Trigger dann nachtragen. **Systemische Lektion:** Schema-Validatoren sind notwendig aber nicht hinreichend — die SKILL-Regel-Semantik (Mehrjahres-Trend, strukturelle Erklärung, Operating-Income-Parallelität) überschreibt einzelperiodische Schema-Trigger. FLAG-Entscheidungen immer Advisor-gegengeprüft bei Borderline-Metriken. Applied Learning: "fcf_trend_neg mechanisch ≠ strukturell — WC-Delta + Multi-Year-Trajectory + OpInc-Parallelität vor FLAG-Aktivierung prüfen" (→ CLAUDE.md bei Promotion).
- **Trigger 2 — 2026-10-17 (6 Monate Forward-Betrieb):** Wurde `delta` überhaupt genutzt? Falls 0 Delta-Records bei ≥20 Vollanalysen → Kategorie aus Schema entfernen. Falls genutzt → Null-Pattern-Erfahrung auswerten, ggf. SKILL.md Schritt 0 um definierte Delta-Auslöser erweitern.
- **Definition A vs. B (SKILL.md ↔ INSTRUKTIONEN:474):** Harmonisierung verschoben auf Trigger 2 — beide Definitionen bleiben nebeneinander stehen, bis reale Nutzung den Konflikt entscheidet.

**Review-Termin 2028-04-01 (Gesamt-Backtest):**
- Hat die Forward-Historie (+2 Jahre seit 17.04.2026) genug Sample-Size für Return-Prediction oder Threshold-Kalibrierung?
- Welcher der 4 Fundierungs-Paper (arXiv-1711.04837, Gu-Kelly-Xiu-2020, Morningstar-Wide-Moat, Buffetts-Alpha) lässt sich als Benchmark anlegen?
- Haben Scoring-Version-Sprünge Regime-Wechsel produziert, die Backtest-Vergleiche invalidieren?

Entscheidungsmatrix wird in `07_Obsidian Vault/.../synthesis/Backtest-Methodik-Roadmap.md` dokumentiert (Phase 4 pending).

**Dokumentation:**
- Spec: `docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md` (v3.7-realigned 17.04.2026)
- Plan: `docs/superpowers/plans/2026-04-17-backtest-ready-infrastructure.md` (356 Zeilen, 4 Phasen + 0 + 0.5)
- README: `03_Tools/backtest-ready/README.md`

---

## 12. Per-Ticker-Chronik

Analyse-spezifische Chronik pro Satellit (Live-Verify, Vollanalysen, Earnings-Updates, FLAG-Transitions). Sortierung innerhalb Sub-§ chronologisch aufsteigend. Format: `- TT.MM.JJJJ — Kurz-Titel (Key-Fakten).` Volle Prosa bleibt in `log.md`-History.

### 12.1 AVGO

- 17.04.2026 — v3.7-Backtest-Rekalibrierung Score 85→84, DEFCON 4 bestätigt, FLAG (Insider $123M 06.04.) bleibt aktiv (Detail §13 [Scoring] v3.7-Ratifikation; Methoden-Anker §5 10b5-1-Footnote-Lücke + Tariff-Exposure-Kalibrierung).

### 12.2 APH

- 15.04.2026 — Tariff-Check abgeschlossen (Revenue China FY25 = 14,7% <15% → kein Revenue-FLAG; Supply-Chain CN/MY Risk-Map-Notiz; China-Trend strukturell rückläufig 23%→14,7% in 2J). Score-basierter FLAG bleibt aktiv.

### 12.3 ASML

- 16.04.2026 — Q1 2026 Earnings Recap (EPS $7,15 Beat +7,99%, Rev €8,77B +13,2% YoY, GM 53,0%, FY26-Guidance angehoben €36–40B; Kurs −2,4% trotz Beat — Booking-Disclosure-Entfall + China-Exportkontroll-Unsicherheit; Score 68 unverändert, kein FLAG, Sparrate voll).
- 17.04.2026 — Live-Verify v3.7 Schritt-2-Backtest (OpM TTM 36,1% → 2 Pt., Fwd P/E FY26 39,52 → Fwd-P/E-Subscore hart 0, Fwd P/E FY27 30,30 Grenzfall, P/FCF ~48x → P/FCF-Subscore hart 0; beide QT-Zweige triggern hart; Approximation 66 ±2-Toleranz bestätigt, DEFCON 3 live-verified).
- 17.04.2026 — Post-Q1 Vollanalyse (Pfad B Non-US/IFRS, Anker für Beispiele.md): Score **68/100 🟡 DEFCON 3** (+2 vs. Approximation, innerhalb Toleranz). Fundamentals 28/50 (QT-P/E + QT-P/FCF beide 0, Bilanz 8/8, CapEx 8/8, ROIC-Spread +17,19pp, FCF-Yield 2/8, OpM 2/2), Moat 20/20 (GM-Bonus), Technicals 7/10, Insider 7/10 (AFM-Carry-Forward), Sentiment 6/10 (B11-Bias-Malus). WACC 9,29% via FRED DGS10 4,29% + 5% ERP (GuruFocus 18,21% verworfen). Kein FLAG, Sparrate voll 33,53€. Einziger Depot-Anker mit beidseitiger QT-Aktivierung.

### 12.4 BRK.B

- 15.04.2026 — DEFCON v3.4 Vollanalyse (Score 75/100 🟢 4, Screener-Exception P/B 1,44x statt P/FCF; Moat 19/20 — Float $686B, BNSF Efficient Scale, 60J Capital-Allocation-Track-Record; Book Value CAGR +10% p.a. 5J; Goodwill 6,8%; Insider 9/10 — Greg Abel Open-Market $15,3M/90d; Schwächen ROIC 5,6–7,8% GAAP Insurance-Exception, Tech 4/10 unter 200MA, Buybacks $0 FY25; kein FLAG, Sparrate voll).

### 12.5 COST

- 15.04.2026 — DEFCON v3.4 Vollanalyse (Score 69/100 🟢 4 Bestandsposition, Screener-Exception: ROIC 5,6% GAAP → Membership Yield 15,2% als ökonomischer Return > WACC 12,3%; Moat 19/20 — Membership-Loyalty; CapEx/OCF 21,3% Clean, FCF $7,2B FY25; Schwächen P/FCF 53x, FCF-Yield 1,88%, Fwd P/E 51x, GM <15% Kostenführer-Modell; kein FLAG, Sparrate voll).

### 12.6 MSFT

- 17.04.2026 — v3.7-Backtest-Rekalibrierung Score 60→59, DEFCON 2, CapEx-FLAG bleibt aktiv (Detail §13 [Scoring] v3.7-Ratifikation; FLAG-History + CapEx-Finance-Lease-Exception in §3; Pre-Processing Regel 2 + SKILL.md Screener-Exception #5 bereinigter Pfad). Score-Update-Trigger: Q3 FY26 Earnings 29.04.2026 (FLAG-Review, bereinigtes CapEx/OCF <60% = Auflösung).

### 12.7 RMS

- 15.04.2026 — Q1 2026 Earnings + DEFCON v3.4 Re-Analyse (Score 71→**69** 🟢 4 bestätigt; Q1 Revenue €4,07B +6% CER (−1% reported) → Miss vs. +7–8%; Kurs −8,4%, 52W-Tief €1.529; Treiber Mittlerer Osten −6% Iran-Krieg, FX-Headwind €290M; Leder +9%, ROIC 24% >> WACC 6,5% Spread +17,5pp — Screener-Exception #3 überschreibt Score-Downgrade-Mechanik; Insider-Käufe +€7,67M/90d; kein FLAG, Sparrate voll; Re-Check H1 2026 Juli/Aug).
- 17.04.2026 — Live-Verify v3.7 Schritt-2-Backtest (OpM TTM 41,05% → 2 Pt., Fwd P/E 34,91 → Fwd-P/E-Subscore hart 0, P/FCF ~38x → P/FCF-Subscore hart 0; beide QT-Zweige triggern hart wie ASML; Approximation 68 ±2-Toleranz bestätigt, D4 durch Screener-Exception geschützt; post −8,4%-Drop Fwd P/E ~39→34,9 → weitere Korrektur <30 könnte Score +1 bringen).

### 12.8 SU

- 15.04.2026 — DEFCON v3.4 Vollanalyse (Score 71/100 🟢 4; Highlights CapEx/OCF 25,2% 4J-stabil, ROIC 10,48% > WACC 8,96% Spread bestätigt, FCF +41%/3J €3,26B→€4,59B, Kurs +12,6% über 200D-MA — einziger Satellit über 200MA, 22 Analysten Strong-Buy 0% Sell; Schwächen P/FCF 37,7x, FCF-Yield 2,65%, Goodwill 40,2% AVEVA-M&A, Moat Narrow; kein FLAG, Sparrate voll).

### 12.9 TMO

- 17.04.2026 — Live-Verify v3.7 Schritt-2-Backtest (OpM TTM 18,17% → 1 Pt., Fwd P/E FY26 20,80 <22 → Standard-Skala, P/FCF 29,3x + Wide Moat → **nur** P/FCF-Zweig triggert max 1 Cap (Screener-Exception #4 differenzierte QT); Score-Rekonstruktion 67-1+0-2 = 64 → Score 63 ±1-Toleranz bestätigt; D2 live-verified, Sparrate 16,76€ korrekt).
- 18.04.2026 — Pre-Earnings-Vollanalyse + fcf_trend_neg Schema-Watch-Entscheidung (Score 64/D2; Advisor-Review verwirft mechanischen `fcf_trend_neg`-Trigger wegen WC-Noise FY25 ΔWC −1.766M erklärt FCF-Rückgang −974M überproportional, 4J-FCF-Plateau $6,9–7,3B, OpInc +5,1% YoY intakt → Option B struktureller Disclosure statt FLAG-Aktivierung; kein flag_events-Write; Q1 23.04. = natürlicher Resolve-Gate). Detail §11.Befund 4.
- 23.04.2026 — Q1 FY26 Forward-Vollanalyse, Beat + Guidance-Raise, **fcf_trend_neg-Resolve-Gate CLEAR** (Adj EPS $5,44 vs $5,24 +3,8%, Rev $11,01B +1,4% Beat / +1% organic; **FCF $825M +121% YoY**, OCF $1.192M +64,9%, ΔWC −$1.112M vs −$1.425M WC-Unwind-These bestätigt; Guidance Top+Bottom hochgesetzt Rev $47,3–48,1B, FCF-Guide FY26 $6,9–7,4B, Organic 3–4% → H2-Akzeleration; Score **64→67 Δ+3 (§28.2 log-only-Fenster)**: Fundamentals +2 (fwd_pe 6→7, fcf_yield 3→4), Sentiment +1 (eps_revision_delta +1); **D2→D3**, Screener-Exception #4 weiter aktiv; Sparraten-Kaskade Nenner 8,0→8,5, TMO 17,81€→**33,53€** +15,72€; neue Watches Organic-Akzeleration Q2, Clario-Integration, Net-Debt/EBITDA-Post-Clario, Analytical-Instruments-Margin-Drift −10bps). Detail §13 [Ticker]-Zeile.

### 12.10 V

- 15.04.2026 — DEFCON v3.4 Vollanalyse (Score **86/100** 🟢 4, Kalibrierungsanker auf AVGO-Niveau; Highlights CapEx/OCF ~6% Fabless, Moat 19/20 — GuruFocus 9/10 Wide 4 überlappende Quellen, FCF $21,6B FY25, Revenue $40B +11,4%; Schwächen ROIC ~9,9% GAAP knapp unter WACC ~10,5% Goodwill-Verzerrung Visa-Europe, Fwd P/E 23x, unter 200MA; Insider sauber diskret. $201K/90d; kein FLAG, Sparrate voll).
- 18.04.2026 — Forward-Rescoring (Score **72→63 🟠 D2**, erster Rescoring-Präzedenzfall; Advisor-Review deckt 3 Sub-Score-Korrekturen auf: (a) Moat `pricing_power_bonus` ohne Transcript-Belegung −1, (b) Insider `ownership` Threshold-Korrektur V <1% → 1/3 statt 2/3 −1, (c) ROIC `Goodwill-Ausnahme` auf Nicht-M&A-Compounder fehlapplziert Regel-4-Gating GW/Assets 19,95% <30% greift nicht −7; `2026-04-18_V_rescoring` Archive-Append mit Begründung in `notizen`). Detail §11.Befund 3.

### 12.11 VEEV

- 17.04.2026 — v3.7-Backtest-Rekalibrierung Score 74→74 unverändert, DEFCON 4 (Detail §13 [Scoring] v3.7-Ratifikation).
- 18.04.2026 — Threshold-Drift-Fix D4→D3-Label (Sparrate bei D3/D4-Übergang identisch → keine operative Änderung; Detail §13 [Scoring] 18.04. + §11.Befund 2).

---

## 13. System-Lifecycle-History

Chronologische Meilenstein-Liste. Topic-Prefix für Grep-Filterung. Sortierung aufsteigend. Format: Tabelle.

| Datum | Topic | Meilenstein |
|---|---|---|
| 15.04.2026 | [Tools] | Rebalancing_Tool_v3.4 — Sparraten-Logik überarbeitet (D4/D3=1.0, D2=0.5, D1/FLAG=0€); Drift-Warnschwelle typ-abhängig; Ziel-Allokation exakt 100% |
| 15.04.2026 | [Vault] | Vault-Audit — 10 neue Seiten (4 Autoren + 6 Ersatzbank), 7 Orphans gefixt, 61→71 Notes, Frontmatter standardisiert |
| 15.04.2026 | [Meta] | System-Integration v4.0 — SKILL.md v4.0 (15 Regeln), 6 INSTRUKTIONEN-Lücken geschlossen, MCP-Session-Check + Tool Search verankert, System-Reife ~95% |
| 16.04.2026 | [Scoring] | DEFCON v3.5 Scoring-Audit & Fix — 7-Fragen-Audit (5×A, 1×B PT-Upside Double-Counting, 1×C); PT-Upside aus Technicals entfernt, Relative-Stärke als 0–3 Scored Metric promotet, Fundamentals-Floor min 0; Anker rekalibriert AVGO 86→85, SNPS 79→76, TMO 65→62 D2, FICO 70→67, SPGI 77→74 |
| 17.04.2026 | [Scoring] | v3.6 verworfen, v3.7 "System-Gap-Release" ratifiziert — (1) Quality-Trap Interaktionsterm (QT-Zweige hart 0 bei Wide Moat × teure Bewertung), (2) OpM TTM max 2 Pt., (3) Analyst-Bias-Kalibrierung Sentiment, (4) Fundamentals-Cap 50; Sparraten Nenner 8,5 → 33,53€/16,76€/0€; System-Reife ~92% |
| 17.04.2026 | [Tools] | Skill v3.7.1 deployed — Backtest-Ready Forward-Pipeline aktiv Phase 1/4; Schritt 6b FLAG-Resolution + Schritt 7 Archiv-Write; 14 Pydantic-Modelle; §18 Sync-Pflicht 6 Dateien |
| 17.04.2026 | [Vault] | 3 Foundation-Papers integriert (Piotroski 2000 F-Score, Novy-Marx 2013 GP Premium, Sloan 1996 Accruals) — 7→10 Quellen, 11→14 Befunde (B12/B13/B14), 70→76 wiki-Notes, kein Scoring-Impact |
| 17.04.2026 | [Scoring] | Zwischenbilanz Live-Verify 3/11 (TMO/ASML/RMS) — alle Approximationen ±-Toleranz bestätigt; Fix-1 Interaktionsterm funktioniert design-konform (ASML/RMS beide Zweige, TMO nur P/FCF); v3.7 empirisch validiert |
| 17.04.2026 | [Tools] | Skill-Audit + Tools-Sync Phase 2 (Post-ASML-Update) — 4 _extern-Skills konsolidiert nach `portfolio_risk.py`; Kategorie-A-Fixes in config.yaml (ASML 66→68 etc.), INSTRUKTIONEN (TMO-Anker 62→63), Faktortabelle (v3.4→v3.7), Vault-Sync 6 Entities, Rebalancing/Satelliten-Monitor via openpyxl synchronisiert |
| 18.04.2026 | [Scoring] | Schema-SKILL-Threshold-Drift gefixt — `schemas.py _check_defcon_level` auf 80/65/50 Bands (vormals 70/60/50); 5 Tickers (BRK.B/VEEV/SU/COST/RMS) D4→D3 umgelabelt (Sparrate identisch), APH D3→D2 (FLAG überschreibt). Detail §11.Befund 2 |
| 19.04.2026 | [Tools] | `backtest-ready-forward-verify` Skill deployed (v3.7.2) — Pipeline-Kapsel P1-P6 (Draft-Read + Schema / Freshness / Tripwire / §28.2 Δ-Gate / Dry-Run / Append + git-add); 6 Stdout-Fälle; MigrationEvent self-validating |
| 19.04.2026 | [Tools] | Track 3 Paper-Integration systemweit abgeschlossen — 5 Phasen: 11 Satelliten mit Factor-Exposure-Block (Aghassi 2023), 6 defcon-Concepts, 2 Skills + 3 Tool-Dokus, R5 `portfolio_returns.jsonl` + `benchmark-series.jsonl` Daily-Schema v1.0 (erster Record 17.04. Portfolio 10.173,42 EUR), §30 Live-Monitoring; 13 Codex-Findings appliziert; Skill bleibt v3.7.2 |
| 20.04.2026 | [Briefing] | Morning-Briefing v3.0.3 deployed auf Probe + T1/T3/T4 PASS + Soft-Alert-Rebase — Lever 1 Yahoo-Gap-Elimination (BRK.B/RMS.PA/SU.PA `n.v.`), Soft-Alert <180/180–400/>400s; T1 262s, T4 ~10s, T3 ~270s (dreifache Homonym-Absicherung RMS.PA/SU.PA vs Suncor); Gate A beim Prod-Deploy |
| 20.04.2026 | [Briefing] | Prod-Deploy v3.0.3 — RemoteTrigger `trig_01PyAVAxFpjbPkvXq7UrS2uG` via ccr full-replace, updated_at 14:36 UTC, next_run 21.04. 10:01; `allowed_tools` um `mcp__tavily__tavily_search` erweitert; Discoverability-Edits Post-6-Paper-Ingest (Update-Klassen-DEFCON + DEFCON-System + Depot-State-April Banner-Drift-Fix) |
| 20.04.2026 | [Briefing] | 🔴 v3.0.3 Manual-Run FAIL → Rollback v2.1 — schwere Datenfabrikation (Oster-EOD-Lag falsch als "stale" interpretiert → Yahoo-intraday-Fallback improvisiert → Phantom-Kurse AVGO $317,79 −21,8%); Rollback 15:13 UTC auf v2.1-Content, allowed_tools auf `[Bash,Read,Glob,Grep]`; Gate A ausgesetzt; Anti-Hallucination-Lesson: auch Datenpfade explizit verbieten |
| 20.04.2026 | [Vault] | KG-Roadmap v0.1 `draft-frozen` — Codex-Option-D statt v1.0-Ratifikation; Re-Review-Trigger = Cross-Entity-/10-K-Narrativ-Bedarf ODER Score-Archiv-Interim-Gate 2026-10-17; Track 5a/5b + v3.0.3-Prod-Deploy nicht blockiert; erste Anwendung `draft-frozen` für Synthesis-Docs |
| 21.04.2026 | [Scoring] | Drift-Migration `score_history.jsonl` 12/27 → 27/27 PASS (`ca76114`) — `migrate_defcon_drift.py` idempotent+atomar; 12 `defcon_level`-Drifts seit 18.04.-Threshold-Migration gefixt (alle pre-18.04.-Backfills Score 71–76 D4→D3, 61–63 D3→D2); Motivation für Systemhygiene-Pivot TOP-Priority |
| 21.04.2026 | [Tools] | Score-Append Provenance-Gate Spec + Plan v2 ratifiziert (`206c0a1`) — Architektur Variante E (Hybrid Pipeline-Gate B + Schema-Guard D), 5 Codex-Sparring-Runden; 4 Patches (Task 0 Pre-Execution-Baseline, Task 2.7 Re-Validate-Sweep, Task 3.1a-d Granularitäts-Split, Task 6 CORE-MEMORY-§10-Timing-Fix); 7 Tasks/40 Steps |
| 21.04.2026 | [Meta] | §27.4 Vertikal-Drift-Klausel + Applied Learning 12/20 + Systemhygiene-Pivot TOP-Priority (`ca76114` + `8e835ab`) — Präzedenzfall 12/27 Drift → Re-Validate-Pflicht bei Schema-/Threshold-Migrationen; Memory `feedback_exhaustive_drift_check.md` Tier 1 13/13; externes `codebase-memory-mcp` verworfen → internes `03_Tools/system_audit.py` bauen |
| 22.04.2026 | [Tools] | system_audit.py v1.0 + `/SystemAudit` deployed (Phase E 19/19 DONE) — 9 Checks Core+Optional, `--minimal-baseline` 3/3 PASS pragmatischer Regression-Gate; Acceptance-Matrix 9/11 PASS + 2 dokumentierte WARNs; 2 Plan-Header-Notices (Spec-Drift Task 15 + Task 17); Codex RECONCILED_WITH_FOLLOWUPS (3 Follow-ups); CodeRabbit 4 Phase-E-Findings gefixt (Fix-Welle E `e3ba381`) + 1 OOS-Nitpick |
| 23.04.2026 | [Ticker] | TMO Q1 FY26 Beat + Guidance-Raise → Score 64→67, D2→D3, fcf_trend_neg-Resolve-Gate CLEAR, Sparraten-Kaskade Nenner 8,0→8,5 (Detail §12.9) |
| 23.04.2026 | [Tools] | `portfolio_risk.py` `--as-of`-Backfill-Flag + Atomic-Write — Daily-Persist-Lücke seit 17.04. retroaktiv adressierbar; Cashflow-Separation + trading-date-Anker bleibt |
| 23.04.2026 | [Tools] | Audit-Tool Severity-Icons + Batch-Output-Grouping — `system_audit.py` Output-Hygiene (Severity ✅/⚠️/❌ Icons pro Check, Batch-Grouping nach Kategorie Core/Optional); Check-10 status_matrix Over-Strict-Regex Scope auf `### Matrix`-Subsection eingeengt |
| 23.04.2026 | [Tools] | `06_Skills-Pakete` Orphan-ZIPs → `05_Archiv/skills-legacy/` — v3.7.1-Paket als neue SSoT, Legacy-Pakete archiviert (Informationsverlust-Aversion: archiviert, nicht gelöscht) |
| 24.04.2026 | [Meta] | CLAUDE.md Routing-Refactor Tier 1 deployed + Applied-Learning v2.5 (12→14/20) — 97→86 Zeilen, 2 neue SSoT `APPLIED-LEARNING.md` + `TOKEN-RULES.md`, `## Routing-Table` (9 Trigger × 4 Spalten + 3 Edge-Cases + Hybrid-Match-Regel), 11/11 AC PASS (2 dokumentierte Abweichungen); 8 Commits Baseline `d025c7f` |
| 24.04.2026 Session 3 | [Meta] | 00_Core Perfect-Organization Tier 2 — Brainstorm + Spec v0.3 ratifiziert (3-fach Review Claude+Codex+Advisor). Scope **B** (a+b+c zusammen, d Vault + e §215 deferred). Decision-Cascade: **G2** 4-File-Split + **H1** Hub-Pure + **R2** §1-Auflösung + **V-Kompakt** §12/§13 mit `[Topic]`-Prefix + **L2** Outbound-only Verweise-Köpfe. Skill-Versions separat (dynastie-depot v3.7.2→v3.7.3 DEFCON-gekoppelt; backtest-ready-forward-verify 1.0.0→1.0.1 eigene Kette). Codex-Spec-Review 8 Findings (2 Blocker + 5 Should + 1 Nice — alle resolved); Advisor 4-Punkte (PORTFOLIO Size-AC inline gefixt, 3 deferred zu §10.2 für Plan-Session). DEFCON v3.7 unverändert |
| 24.04.2026 Session 4 | [Meta] | 00_Core Tier 2 Plan v1.1 ratifiziert (Codex-Pre-Execution-reviewed). 10 Tasks / 103 bite-sized Steps / 1920 Z. Codex-Verdikt RECONCILED_WITH_FOLLOWUPS: F1 🔴 AC #18 explicit + F2 🟡 Atomarity-Drift + F3 🟡 Step 9.7 Hard-Pause + F4 ℹ️ Ticker-Reconciliation — alle inline resolved. 3 Advisor-Klärungen User-resolved zu §10.2 → Spec v0.3 → **v0.4**: (1a) PORTFOLIO=Primärquelle direkt editierbar · (2b) Back-Ref-Scope 10 Files (4 neu + 6 Peers) · (3a) §18 Multi-Event-Union-Regel formal Vertragsteil |
| 24.04.2026 | [Meta] | 00_Core Perfect-Organization Tier 2 — STATE-Split (159 Z → Hub ≤40 Z + PORTFOLIO + PIPELINE + SYSTEM), CORE-MEMORY §1 → §12 Per-Ticker + §13 System-Lifecycle, `## Verweise`-Block auf 10 Files, §18 Trigger-basiert + Union-Regel, Scoring-neutral (AC #18), Feature-Branch `refactor/00core-perfect-organization`; dynastie-depot v3.7.3 + backtest-ready-forward-verify 1.0.1 Adoption-Bumps |
| 25.04.2026 | [Meta] | 00_Core Perfect-Organization Tier 2 — Execution-Plan vollständig ausgeführt (Sessions 5-7, Tasks 0-9). 14 atomare Commits + 1 Codex-F1-Fix + 1 AC#15-Alignment + 1 Review-PASS-Commit + Merge `--no-ff` in main. Review-Gates: Claude-Self (AC #1-#18) + Codex-Reconciliation RECONCILED_WITH_FOLLOWUPS (1 🟡 inline-fixed) + CodeRabbit 26-Findings/0-Fix (alle out-of-scope/pre-existing/deferred) + User-Sign-off. Merge-Conflict-Resolution für STATE/CORE-MEMORY/SESSION-HANDOVER (main hatte 2 Sessions narrative auf pre-Hub-Split-Layer, Re-Migration zu §13 inline). Scoring-neutral. Follow-up #13 Vault-Concept-Sanierung deferred |

---
*🦅 CORE-MEMORY.md v1.9 (§12 Per-Ticker + §13 System-Lifecycle, §1/§9b entfernt) | Dynastie-Depot | Stand: 25.04.2026*
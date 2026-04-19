# Paper-Integration systemweit — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task (inline batch execution). Steps use checkbox (`- [ ]`) syntax for tracking.
>
> **Execution-Modus:** Inline (CLAUDE.md Applied-Learning: "Subagents nur für Code+Tests — Markdown/YAML direkt editieren").

**Spec:** `docs/superpowers/specs/2026-04-19-paper-integration-design.md` (commit `976e67a`)

**Goal:** 4 wissenschaftliche Papers (Aghassi/Bailey/Flint-Vermaak/Palomar) operativ in Vault-Cross-Links, Skills, INSTRUKTIONEN, Monitoring-Cadence (R1 §30) und Portfolio-Return-Persistenz (R5) integrieren — ohne Scoring-Kern zu ändern.

**Architektur:** 4-Layer-Trennung (Scoring-Kern ⊥ Monitoring ⊥ Dokumentation ⊥ Validation). Phase 1a/1b = Dokumentation, Phase 2 = Dokumentation, Phase 3 = Infrastruktur, Phase 4 = Monitoring. 5 Codex-Checkpoints: Phase 1b (Konsistenz-Pass), Phase 3 (Code + Schema + Look-Ahead), Phase 4 (§30-Formulierung).

**Tech Stack:** Markdown (Vault), Python (portfolio_risk.py), JSONL (portfolio_returns.jsonl + benchmark-series.jsonl), Git (force-add für docs/superpowers).

---

## Task 1: Phase 1a — Factor-Exposure Template + 11 Satelliten

**Files:**
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/ASML.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/AVGO.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/MSFT.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/V.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/TMO.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/VEEV.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/SU.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/BRKB.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/COST.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/RMS.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/APH.md`

**Reference-Daten:** 
- `00_Core/STATE.md` (Scores, DEFCON, FLAGs)
- `00_Core/Faktortabelle.md` (Detail-Metriken pro Ticker: Fwd P/E, P/FCF, ROIC, Moat, Beta, 6M-RelStärke)
- `00_Core/CORE-MEMORY.md §5` (Ticker-spezifische Lektionen)

- [ ] **Step 1: Read reference data (common for all Ticker)**

Read die drei Referenz-Dateien einmal um Factor-Ratings konsistent ableiten zu können. Ersatzbank-Pages NICHT anfassen.

- [ ] **Step 2: Write Factor-Exposure-Block für ASML als Template-Referenz**

Append diesen Block ans Ende von `ASML.md` (vor letzter Zeile falls Footer existiert, sonst ganz unten):

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]] (AQR-Kanon): Value / Quality / Momentum / Defensive / Investment. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** moderat — Fwd P/E FY27 ≈ 30 (Grenzfall gegen 5J-Range), EV/EBITDA im oberen Bereich aber EUV-Monopol rechtfertigt Premium
- **Quality:** stark — ROIC ~30% > WACC 8-9%, Moat wide (EUV-Monopol, 100% Marktanteil), QMJ-Profil (siehe [[QMJ-Faktor]])
- **Momentum:** schwach — Q1 17.04. Vollanalyse ergab 68, Kurs-Drawdown aus 2024/25 nicht voll zurückerholt
- **Defensive:** moderat — Beta 1,1–1,3, hohe Zyklik im Semi-Capex (Investment-Klasse), aber Customer-Concentration bei Top-3 Foundries stützt Cash-Flow-Stabilität
- **Investment:** schwach — CapEx/OCF ~20-25% hoch wegen EUV-R&D, aber strategisch nötig; kein klassischer "Overspending"-Investment-FLAG

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Factor-Information-Decay]]
```

- [ ] **Step 3: Write Factor-Exposure-Block für AVGO**

Append an `AVGO.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E hoch, bewertet als AI-Play; P/FCF oberhalb 5J-Median
- **Quality:** stark — ROIC stark > WACC, Moat wide (Networking + Software-Post-VMware), Customer-Stickiness
- **Momentum:** stark — Kurs-Rally 2025-26 anhaltend, Q3 FY26 Trigger steht aus
- **Defensive:** schwach — Insider $123M/90d trotz wahrscheinlichem Post-Vesting, Kunden-Konzentration
- **Investment:** moderat — VMware-Integration-CapEx elevated, aber operativ kontrolliert

Quellen: [[Aghassi-2023-Fact-Fiction]]
```

- [ ] **Step 4: Write Factor-Exposure-Block für MSFT**

Append an `MSFT.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E hoch (AI-Capex-Phantasy), Multiple-Expansion
- **Quality:** moderat — ROIC solide, aber CapEx/OCF 83.6% FLAG aktiv ([[CapEx-FLAG]]) reduziert Earnings-Quality temporär
- **Momentum:** moderat — Kurs-Konsolidierung nach Rally, Q3 FY26 am 29.04.
- **Defensive:** moderat — Moat wide (Azure + Office), aber CapEx-Intensität steigt
- **Investment:** **stark (negativ)** — CapEx/OCF 83.6% → aktiver Investment-FLAG ([[CapEx-FLAG]]). Flint-Vermaak Investment-Half-Life ~1M → §30 Monthly-Refresh pflicht

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Factor-Information-Decay]], [[Flint-Vermaak-2021-Decay]]
```

- [ ] **Step 5: Write Factor-Exposure-Block für V (Visa)**

Append an `V.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** moderat — Fwd P/E leicht unterhalb 5J-Median nach 18.04.-Rescoring auf 63
- **Quality:** stark — ROIC >30%, Moat wide (Netzwerk-Effekt), geringe CapEx-Intensität, QMJ-Profil
- **Momentum:** schwach — 6M RelStärke -14pp vs SPY, Kurs unter fallendem 200MA; Crowd-Sell-Ratio 0%
- **Defensive:** stark — Beta ~0,9, Cash-Flow-Stabilität, wenig Konjunkturabhängigkeit
- **Investment:** n.a. — kein Investment-FLAG, CapEx sehr niedrig

Quellen: [[Aghassi-2023-Fact-Fiction]], [[QMJ-Faktor]]
```

- [ ] **Step 6: Write Factor-Exposure-Block für TMO**

Append an `TMO.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** moderat — Fwd P/E leicht über 5J-Median, Quality-Premium gerechtfertigt
- **Quality:** stark — ROIC >20%, Moat wide (Life-Sciences-Instrumentierung), QMJ-Profil
- **Momentum:** schwach — Rücksetzer 2025, Q1 23.04. FLAG-Resolve-Gate entscheidet
- **Defensive:** moderat — Beta moderat, zyklisch via Biotech-Kunden
- **Investment:** **schema-getriggert (nicht aktiviert)** — fcf_trend_neg FY25 WC-Noise; Schema-Watch, kein aktiver FLAG. §30 daher NICHT automatisch pflicht (siehe [[Factor-Information-Decay]])

Quellen: [[Aghassi-2023-Fact-Fiction]], [[QMJ-Faktor]], [[Flint-Vermaak-2021-Decay]]
```

- [ ] **Step 7: Write Factor-Exposure-Block für VEEV**

Append an `VEEV.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E hoch, SaaS-Premium
- **Quality:** stark — ROIC stark, Vertical-SaaS-Monopol in Life Sciences, QMJ-Profil
- **Momentum:** moderat — Earnings-getriebene Bewegungen, kein klarer Trend
- **Defensive:** moderat — Customer-Retention hoch, aber Sektor-Zyklik
- **Investment:** n.a. — Asset-light, sehr niedrige CapEx

Quellen: [[Aghassi-2023-Fact-Fiction]], [[QMJ-Faktor]]
```

- [ ] **Step 8: Write Factor-Exposure-Block für SU (Suncor)**

Append an `SU.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** stark — Fwd P/E niedrig, P/FCF klar unter 5J-Median; klassischer Value-Faktor
- **Quality:** moderat — ROIC ölpreisabhängig, Moat narrow (Oil-Sands-Kostenposition)
- **Momentum:** moderat — Commodity-getrieben
- **Defensive:** schwach — hohe Ölpreis-Sensitivität, Beta >1
- **Investment:** moderat — CapEx in Oil-Sands strukturell hoch, aber Integration FCF-positiv

Quellen: [[Aghassi-2023-Fact-Fiction]]
```

- [ ] **Step 9: Write Factor-Exposure-Block für BRK.B**

Append an `BRKB.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** moderat — P/B historisch nah am Median, Fwd P/E nicht dramatisch
- **Quality:** stark — operative Töchter + Versicherungs-Float, Buffett-Faktorlogik (siehe [[Buffett-Faktorlogik]], [[QMJ-Faktor]])
- **Momentum:** moderat — Kurs-Stabilität
- **Defensive:** stark — Insurance-Exception-Profil, Rezessions-resilient, Cash-Reserve
- **Investment:** n.a. — Holding-Struktur, CapEx-Logik via Töchter nicht direkt ableitbar

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Buffetts-Alpha]], [[Buffett-Faktorlogik]]
```

- [ ] **Step 10: Write Factor-Exposure-Block für COST**

Append an `COST.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E hoch, Premium-Retailer-Bewertung
- **Quality:** stark — Membership-Yield-Modell (Screener-Exception #2, siehe [[Moat-Taxonomie-Morningstar]]), Customer-Retention >90%
- **Momentum:** moderat — Earnings-stabil
- **Defensive:** stark — Recession-resilient, stabile Mitgliederbasis
- **Investment:** moderat — CapEx-Expansion für neue Stores, aber operativ kontrolliert

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Moat-Taxonomie-Morningstar]]
```

- [ ] **Step 11: Write Factor-Exposure-Block für RMS (Hermès)**

Append an `RMS.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E sehr hoch, Luxury-Premium historisch gerechtfertigt
- **Quality:** stark — ROIC stark, Moat wide (Marke + Scarcity-Pricing), Screener-Exception #1 akzeptiert
- **Momentum:** moderat — Stable nach Rücksetzer 2024
- **Defensive:** stark — Customer-Loyalty, Pricing-Power
- **Investment:** n.a. — niedrige CapEx/OCF-Ratio

Quellen: [[Aghassi-2023-Fact-Fiction]]
```

- [ ] **Step 12: Write Factor-Exposure-Block für APH (Amphenol)**

Append an `APH.md`:

```markdown

## Factor-Exposure (Aghassi 2023)

Einordnung nach [[Factor-Investing-Framework]]. Strikt dokumentativ, keine Score-Wirkung.

- **Value:** schwach — Fwd P/E hoch, Multi-Expansion in Electronics-Cycle
- **Quality:** moderat — ROIC solide, Moat narrow-wide (Connector-Spezialisierung), diversifizierte End-Märkte
- **Momentum:** moderat — Cyclical, Earnings-getrieben
- **Defensive:** schwach — zyklische End-Märkte (Automotive, Industrial)
- **Investment:** moderat — M&A-aktiv, CapEx für Kapazitätserweiterung

Quellen: [[Aghassi-2023-Fact-Fiction]]
```

- [ ] **Step 13: Acceptance-Check — alle 11 Pages haben Block**

Run:
```bash
grep -l "Factor-Exposure (Aghassi 2023)" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/"*.md | wc -l
```
Expected: `11` (exakt 11 Treffer)

- [ ] **Step 14: Acceptance-Check — kein doppelter Block**

Run:
```bash
grep -c "Factor-Exposure (Aghassi 2023)" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/"*.md
```
Expected: jede Zeile zeigt `:1` (genau einmal pro Datei)

- [ ] **Step 15: Commit Phase 1a**

```bash
git add "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/"*.md
git commit -m "$(cat <<'EOF'
feat(vault): paper-integration phase 1a — satellites + factor-exposure blocks

- 11 Satelliten-Pages (ASML/AVGO/MSFT/V/TMO/VEEV/SU/BRKB/COST/RMS/APH) bekommen standardisierten 5-Zeilen-Factor-Exposure-Block nach Aghassi 2023
- Werte: stark/moderat/schwach/n.a. mit 1-Satz-Begründung
- Strikt dokumentativ — keine Score-Wirkung
- MSFT: Investment=stark(negativ) → §30-Anker für Phase 4
- TMO: Investment=schema-getriggert (nicht aktiviert) → Schema-Watch-Kategorie
- V/TMO/VEEV/COST/BRKB: QMJ-Profil expliziert
- Cross-Links zu Factor-Investing-Framework, Factor-Information-Decay, QMJ-Faktor, Buffett-Faktorlogik

Spec: docs/superpowers/specs/2026-04-19-paper-integration-design.md (976e67a)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: Phase 1b — defcon-Concepts Cross-Links

**Files:**
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/DEFCON-System.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/Score-Archiv.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/Backtest-Ready-Infrastructure.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/CapEx-FLAG.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/FLAG-Event-Log.md`
- Modify: `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/Analyse-Pipeline.md`

- [ ] **Step 1: DEFCON-System — Wissenschaftliche Fundierung anhängen**

Append an `DEFCON-System.md`:

```markdown

## Wissenschaftliche Fundierung (nachträglich 19.04.2026)

Der DEFCON-Score wird durch 4-Paper-Framework (18./19.04.2026) methodisch validiert:

- **Aghassi 2023** — Factor-Mapping (Value/Quality/Momentum/Defensive/Investment) validiert 5-Block-Scoring-Struktur, siehe [[Factor-Investing-Framework]]
- **Bailey 2015** — PBO-Gate für spätere Strategy-Selection/Parameter-Tuning (Review 2028), siehe [[PBO-Backtest-Overfitting]]
- **Flint-Vermaak 2021** — Half-Life-Konsistenz der Earnings-Trigger-Cadence (3M) mit Value/Quality/Momentum-Half-Lives (3-5M), siehe [[Factor-Information-Decay]]
- **Palomar 2025** — Seven Sins of Backtesting als Pre-Flight für Migration-Events (§28/§29.5), siehe [[Seven-Sins-Backtesting]]

→ Operatives Retrospective-Gate: INSTRUKTIONEN.md §29 (6 Sub-Gates, §29.4+§29.5 sofort aktiv)
```

- [ ] **Step 2: Score-Archiv — Paper-Anker + §29-Rückverweis**

Append an `Score-Archiv.md`:

```markdown

## Retrospective-Validation (§29 + Papers)

Das Score-Archiv ist die Datengrundlage für §29-Retrospective-Analysen (ab 2028):

- **§29.1 (PBO/CSCV)** — erfordert score_history.jsonl mit sauberen Forward-Records; PBO<0,05 als Reject-Schwelle, siehe [[Bailey-2015-PBO]] / [[PBO-Backtest-Overfitting]]
- **§29.2 (AQR-Benchmark)** — Aggregiertes Portfolio-SR gegen AQR/Ilmanen-Band, siehe [[Aghassi-2023-Fact-Fiction]]
- **§29.5 (Seven-Sins-Pre-Flight)** — Sin #2 Look-Ahead pflicht via `source="forward"` Records, siehe [[Seven-Sins-Backtesting]]

→ Schema-Disziplin (siehe §18 + §28) schützt die Retrospective-Datenbasis.
```

- [ ] **Step 3: Backtest-Ready-Infrastructure — §29-Anker + Palomar-Methods**

Append an `Backtest-Ready-Infrastructure.md`:

```markdown

## Wissenschaftliche Fundierung (nachträglich 19.04.2026)

Die Backtest-Ready-Infrastruktur ist Operationalisierung der in §29 spezifizierten Retrospective-Gates:

- **Persistenz-Disziplin** validiert durch Palomar Ch 8.2 Sin #2 (Look-Ahead-Prevention), siehe [[Seven-Sins-Backtesting]]
- **CSCV-Vorbereitung** (Bailey) — score_history.jsonl ist Input-Format für spätere PBO-Rechnung, siehe [[PBO-Backtest-Overfitting]]
- **Komplementäre Methoden** (Palomar Ch 8.4): Walk-forward + k-fold + randomized nur im Retrospective-Kontext, nie Live, siehe [[Palomar-Methods-Reference]]

→ Interim-Gate 2027-10-19: 18-Monats-Dry-Run mit `risk-metrics-calculation` + PBO-Smoke-Test.
→ Review-Gate 2028-04-01: Volle §29-Aktivierung nach 24+ Monaten Return-Serie.
```

- [ ] **Step 4: CapEx-FLAG — Flint-Vermaak-Anker + §30-Bezug**

Append an `CapEx-FLAG.md`:

```markdown

## Wissenschaftliche Fundierung (nachträglich 19.04.2026)

Der CapEx-FLAG triggert Investment-Klasse-Beobachtung. Per Flint-Vermaak 2021 hat der Investment-Faktor die schnellste Half-Life aller AQR-Kanon-Faktoren (~1 Monat):

- **Konsequenz:** Earnings-Trigger-Cadence (~3M) ist zu träge für aktive CapEx-FLAGs
- **Monthly-Refresh-Pflicht** für aktive Investment-FLAGs → INSTRUKTIONEN.md §30 (ab Phase 4)
- **Aktuelle Scope:** MSFT CapEx/OCF 83.6% FLAG aktiv → §30 pflicht
- **Schema-Watch:** TMO fcf_trend_neg schema-getriggert, bewusst nicht aktiviert (WC-Noise) → §30 nicht automatisch

Quellen: [[Flint-Vermaak-2021-Decay]], [[Factor-Information-Decay]]
```

- [ ] **Step 5: FLAG-Event-Log — Seven-Sins-Anker (Sin #2)**

Append an `FLAG-Event-Log.md`:

```markdown

## Wissenschaftliche Fundierung (nachträglich 19.04.2026)

Das FLAG-Event-Log ist Point-in-Time-Dokumentation und dient §29.5 Sin #2 Look-Ahead-Prevention:

- **Sin #2 (Look-Ahead):** FLAG-Trigger muss in dem Moment persistiert werden, in dem die Daten vorlagen — keine rückwirkende "Ich hätte es wissen müssen"-Einträge
- **Sin #3 (Storytelling):** Trigger-Rationale wird ex-ante im flag_events.jsonl-`notizen`-Feld dokumentiert, nicht post-hoc
- **Kategorien-Trennung:** "Aktiver FLAG" vs. "Schema-Watch" (§30) — schema-getriggert-aber-nicht-aktiviert bekommt eigene Event-Klasse

Quellen: [[Palomar-2025-Portfolio-Optimization]], [[Seven-Sins-Backtesting]]
```

- [ ] **Step 6: Analyse-Pipeline — Aghassi-Mapping + §29-Anker**

Append an `Analyse-Pipeline.md`:

```markdown

## Wissenschaftliche Fundierung (nachträglich 19.04.2026)

Die 5-Block-Analyse-Pipeline (Fundamentals/Moat/Quality/Insider/Technicals) mappt auf AQR-Kanon (Aghassi 2023):

- **Fundamentals** (Fwd P/E, P/FCF, Valuation-Z) → **Value**-Faktor, siehe [[Factor-Investing-Framework]]
- **Moat + Quality-Fundamentals** → **Quality (QMJ)** + **Defensive (BAB)**, siehe [[QMJ-Faktor]], [[Moat-Taxonomie-Morningstar]]
- **Technicals** → **Momentum**-Faktor (UMD)
- **Insider** → non-AQR-Edge (kein direkter Faktor-Anker, Dynasty-Depot-spezifisch)

**Seven-Sins-Pre-Flight (§29.5)** greift ab sofort bei Migration-Events (§28), bei Live-Analysen Backlog 2028.

Quellen: [[Aghassi-2023-Fact-Fiction]], [[Factor-Investing-Framework]], [[Seven-Sins-Backtesting]]
```

- [ ] **Step 7: Acceptance-Check — alle 6 defcon-Concepts haben §29 + Paper-Anker**

Run:
```bash
grep -l "§29\|Seven-Sins\|Aghassi\|Bailey\|Flint-Vermaak\|Palomar" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/"*.md | wc -l
```
Expected: `6` (alle 6 defcon-Concepts haben min. 1 Anker)

---

## Task 3: Phase 1b — Bestehende Konzept-Pages + Index/Log

**Files:**
- Modify: `wiki/concepts/Moat-Taxonomie-Morningstar.md`
- Modify: `wiki/concepts/QMJ-Faktor.md`
- Modify: `wiki/concepts/Buffett-Faktorlogik.md`
- Modify: `wiki/concepts/FCF-Primacy.md`
- Modify: `wiki/concepts/Update-Klassen-DEFCON.md`
- Modify: `wiki/concepts/F-Score-Quality-Signal.md`
- Modify: `wiki/concepts/Gross-Profitability-Premium.md`
- Modify: `wiki/concepts/Accruals-Anomalie-Sloan.md`
- Modify: `wiki/synthesis/Investing-Mastermind-Index.md` (als index.md Äquivalent)
- Modify: `Investing Mastermind/index.md`
- Modify: `Investing Mastermind/log.md`

**Pfad-Prefix (zur Kürzung):** `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/`

- [ ] **Step 1: Moat-Taxonomie-Morningstar — Aghassi QMJ-Anker**

Append an `wiki/concepts/Moat-Taxonomie-Morningstar.md`:

```markdown

## Wissenschaftliche Fundierung (19.04.2026)

Morningstar-Moat-Rating ist qualitative Variante des akademischen **Quality (QMJ)**-Faktors:
- Aghassi 2023 validiert Quality als robuster Faktor mit SR-Hurdle-Überschreitung (t-Stat >>3)
- Moat-Breite (wide/narrow/none) korreliert mit QMJ-Komponenten (Profitability/Growth/Safety/Payout)
- → [[Aghassi-2023-Fact-Fiction]], [[QMJ-Faktor]], [[Factor-Investing-Framework]]
```

- [ ] **Step 2: QMJ-Faktor — Aghassi-Validierung**

Append an `wiki/concepts/QMJ-Faktor.md`:

```markdown

## Aghassi 2023 Validation

Aghassi et al. 2023 bestätigen QMJ (Quality minus Junk) als einen der 4 Kanon-Faktoren mit:
- **SR ~0,5** stand-alone US-Stocks 1926-2020
- **t-Stat >>3** (Harvey/Liu/Zhu-Hurdle bestanden)
- **~25% Decay post-publication** (McLean/Pontiff), aber Kern-Premium stabil

→ Siehe [[Aghassi-2023-Fact-Fiction]], [[Factor-Investing-Framework]]
```

- [ ] **Step 3: Buffett-Faktorlogik — Aghassi QMJ+BAB**

Append an `wiki/concepts/Buffett-Faktorlogik.md`:

```markdown

## Moderne Faktor-Decomposition (Aghassi 2023)

Buffett-Alpha wird in akademischer Faktor-Sprache dekomponiert in:
- **QMJ (Quality)** — Buffett's "wonderful companies at fair price"
- **BAB (Betting against Beta)** — Low-Beta-Präferenz bei Leverage-Amplifikation
- **Defensive** — Versicherungs-Float als low-cost leverage

Aghassi 2023 validiert diese Faktoren als persistent. → [[Aghassi-2023-Fact-Fiction]], [[QMJ-Faktor]], [[Buffetts-Alpha]]
```

- [ ] **Step 4: FCF-Primacy — Palomar-Metriken-Anker**

Append an `wiki/concepts/FCF-Primacy.md`:

```markdown

## Portfolio-Risk-Metriken (Palomar 2025)

FCF als Primary-Cashflow-Kennzahl ist Basis für spätere Sortino/Calmar/Max-DD-Berechnung (Palomar Ch 6):
- Sortino nutzt Downside-FCF-Volatilität
- Calmar normalisiert auf Max-DD
- → Phase 3 R5 persistiert Portfolio-Return-Serie auf FCF-basierter Bewertung

Aktivierung der Risk-Metriken: Review 2028-04-01. → [[Palomar-2025-Portfolio-Optimization]], [[Palomar-Methods-Reference]]
```

- [ ] **Step 5: Update-Klassen-DEFCON — Flint-Vermaak Half-Life**

Append an `wiki/concepts/Update-Klassen-DEFCON.md`:

```markdown

## Wissenschaftliche Fundierung: Faktor-Half-Life (Flint-Vermaak 2021)

Update-Klassen-Cadence wird durch Flint-Vermaak 2021 Half-Life-Tabelle gestützt:

| DEFCON-Block | Faktor-Analog | Half-Life | Unsere Cadence | Status |
|---|---|---|---|---|
| Fundamentals | Value | 3-4M | Earnings (~3M) | ✅ aligned |
| Moat/Quality | Quality | 4-5M | Earnings + Jahresanalyse | ✅ konservativ |
| Technicals | Momentum | 3M | Earnings + Monitor | ✅ aligned |
| **CapEx-FLAG** | **Investment** | **~1M** | Earnings (zu träge bei aktiven FLAGs) | ⚠️ §30 Monthly-Refresh |
| Insider | — | Real-time | OpenInsider | ✅ aligned |

→ [[Flint-Vermaak-2021-Decay]], [[Factor-Information-Decay]], INSTRUKTIONEN §30
```

- [ ] **Step 6: F-Score-Quality-Signal — Aghassi Quality-Anker**

Append an `wiki/concepts/F-Score-Quality-Signal.md`:

```markdown

## Aghassi 2023 Context

F-Score (Piotroski 2000) ist frühe Operationalisierung des Quality-Faktors. Aghassi 2023 validiert Quality akademisch, aber:
- Piotroski-spezifische 9-Signale sind NICHT in DEFCON v3.7 integriert (Session 2 verworfen)
- DEFCON-Quality-Logik nutzt eigene Metrik-Kombination (ROIC>WACC + Moat)
- F-Score bleibt Referenz-Konzept, kein Live-Score-Input

→ [[Aghassi-2023-Fact-Fiction]], [[Piotroski-2000]]
```

- [ ] **Step 7: Gross-Profitability-Premium — Aghassi QMJ-Komponente**

Append an `wiki/concepts/Gross-Profitability-Premium.md`:

```markdown

## Aghassi 2023 Context

Gross Profitability (Novy-Marx 2013) ist eine QMJ-Unterkomponente nach Aghassi-Framework. Im DEFCON-System:
- Nicht als eigenständige Score-Column integriert (Session 2 verworfen)
- Indirekt abgedeckt via ROIC>WACC + Moat-Rating

→ [[Aghassi-2023-Fact-Fiction]], [[QMJ-Faktor]], [[Novy-Marx-2013]]
```

- [ ] **Step 8: Accruals-Anomalie-Sloan — Seven-Sins-Disziplin**

Append an `wiki/concepts/Accruals-Anomalie-Sloan.md`:

```markdown

## Seven-Sins-Disziplin (Palomar 2025)

Accruals-Anomalie (Sloan 1996) ist klassisches Look-Ahead-Bias-Risiko (Palomar Sin #2):
- Wer Quality-Signale aus Accruals konstruiert, muss Point-in-Time-Disziplin wahren
- DEFCON v3.7 nutzt keine Accruals-Score-Column (Session 2 verworfen)
- Als Diagnose-Linse bleibt Sloan relevant

→ [[Palomar-2025-Portfolio-Optimization]], [[Seven-Sins-Backtesting]], [[Sloan-1996]]
```

- [ ] **Step 9: index.md update**

Read current `Investing Mastermind/index.md` → append neue Concepts/Papers zur Liste wenn fehlen. Minimal-Edit: Stelle sicher dass alle 9 neuen Seiten (4 Sources + 5 Concepts) im Index sichtbar sind.

Run:
```bash
grep -c "Bailey-2015-PBO\|Aghassi-2023-Fact-Fiction\|Flint-Vermaak-2021-Decay\|Palomar-2025-Portfolio-Optimization\|PBO-Backtest-Overfitting\|Factor-Investing-Framework\|Factor-Information-Decay\|Seven-Sins-Backtesting\|Palomar-Methods-Reference" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/index.md"
```
Expected: ≥9 Treffer (alle 9 Seiten referenziert)

Falls Einträge fehlen: ergänze sie alphabetisch in der Concept/Source-Sektion.

- [ ] **Step 10: log.md update**

Append an `Investing Mastermind/log.md`:

```markdown

## 2026-04-19 — Paper-Integration systemweit (Track 3)

**Phase 1a+1b abgeschlossen:**
- 11 Satelliten-Pages mit Factor-Exposure-Block (Aghassi 2023)
- 6 defcon-Concepts mit §29-Rückverweisen + Paper-Ankern
- 8 bestehende Concept-Pages mit "Wissenschaftliche Fundierung"-Abschnitt
- index.md + log.md aktualisiert

**Phase 2-4 pending:** Skill-Verankerung, R5 Portfolio-Return-Persistenz, R1 §30 Monthly-Refresh

**Spec:** docs/superpowers/specs/2026-04-19-paper-integration-design.md
```

- [ ] **Step 11: Acceptance-Check — "Wissenschaftliche Fundierung"-Abschnitte in 8 Concepts**

Run:
```bash
grep -l "## Wissenschaftliche Fundierung\|## Aghassi 2023 Context\|## Aghassi 2023 Validation\|## Moderne Faktor-Decomposition\|## Portfolio-Risk-Metriken\|## Seven-Sins-Disziplin" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/"*.md | wc -l
```
Expected: ≥8 (die 8 aus Steps 1-8)

---

## Task 4: Phase 1b Codex-Konsistenz-Pass

- [ ] **Step 1: Run rg-basierte Checks und sammle Ergebnisse**

Run und dokumentiere Output:
```bash
# Check 1: Anzahl Pages mit Factor-Exposure
grep -l "Factor-Exposure (Aghassi 2023)" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/"*.md

# Check 2: Orphans — neue Concept/Source-Pages ohne Backlinks in anderen Files
grep -r "PBO-Backtest-Overfitting" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/" --include="*.md" -l | wc -l

# Check 3: §29-Rückverweise in defcon-Concepts
grep -l "§29" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/"*.md
```

- [ ] **Step 2: Delegate Konsistenz-Review an Codex**

Invoke codex:codex-rescue subagent mit:

> `--resume Phase 1b Konsistenz-Pass. Prüfe: (1) Alle 11 Satelliten-Pages haben exakt 1 Factor-Exposure-Block mit identischem Header und 5 Zeilen; (2) Alle 6 defcon-Concepts in wiki/concepts/defcon/ haben §29-Rückverweis und min. 1 Paper-Anker; (3) Backlink-Vollständigkeit: die 9 neuen Paper/Concept-Pages sollten je min. 2 Backlinks aus anderen Dateien haben (nicht nur self-referenziell); (4) index.md listet alle 9 neue Seiten. Gib Liste der Abweichungen zurück — kein Fix, nur Befund.`

- [ ] **Step 3: Apply Codex-Befund-Fixes (falls nötig)**

Wenn Codex Abweichungen findet: fix direkt (jeweils minimaler Edit). Wenn keine Abweichungen: Skip.

- [ ] **Step 4: Commit Phase 1b**

```bash
git add "07_Obsidian Vault/"
git commit -m "$(cat <<'EOF'
feat(vault): paper-integration phase 1b — concept cross-links + index/log

- 6 defcon-Concepts mit §29-Rückverweisen + Paper-Ankern
- 8 bestehende Concepts (Moat-Taxonomie, QMJ, Buffett-Faktorlogik, FCF-Primacy, Update-Klassen-DEFCON, F-Score, Gross-Profitability, Accruals-Anomalie) mit "Wissenschaftliche Fundierung"-Abschnitt
- index.md + log.md aktualisiert
- Codex-Konsistenz-Pass bestanden

Spec: docs/superpowers/specs/2026-04-19-paper-integration-design.md (976e67a)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: Phase 2 — Skills + Tool-Dokus + INSTRUKTIONEN-Querverweise

**Files:**
- Modify: `01_Skills/dynastie-depot/SKILL.md`
- Modify: `01_Skills/backtest-ready-forward-verify/SKILL.md`
- Modify: `03_Tools/backtest-ready/README.md`
- Modify: `03_Tools/portfolio_risk.py` (Header-Kommentar)
- Modify: `03_Tools/briefing-sync-check.ps1` (Header-Kommentar)
- Modify: `03_Tools/morning-briefing-prompt-v2.md` (Header-Kommentar)
- Modify: `00_Core/INSTRUKTIONEN.md` (§§18/27/28/29)

- [ ] **Step 1: dynastie-depot SKILL — Fundamentals-Review-Schritt mit Aghassi-Zitat**

Grep für existierenden Fundamentals-Review-Bullet in `01_Skills/dynastie-depot/SKILL.md` und ergänze (inline-Referenz, kein eigener Abschnitt):

Suche Zeile wie "Fundamentals-Review" oder "Moat-Validation" und ergänze daneben Anker:
```
(→ Faktor-Kanon nach Aghassi 2023, siehe Vault [[Factor-Investing-Framework]])
```

Moat-Validation-Schritt analog:
```
(→ Morningstar-Moat = qualitative QMJ-Variante, siehe [[QMJ-Faktor]] / [[Aghassi-2023-Fact-Fiction]])
```

- [ ] **Step 2: backtest-ready-forward-verify SKILL — §29-Querverweis an Schritt 7**

In `01_Skills/backtest-ready-forward-verify/SKILL.md` bei Schritt 7 (oder dem finalen Persistierungs-Schritt) ergänzen:

```markdown
**Retrospective-Gate-Vorbereitung:** Jede forward-Persistierung hier speist §29-Retrospective-Analyse (Review 2028). Seven-Sins-Pre-Flight (§29.5) greift zusätzlich bei Migration-Events (§28).
```

- [ ] **Step 3: backtest-ready/README.md — Paper-Kontext-Header**

Nach dem Titel-Header in `03_Tools/backtest-ready/README.md`:

```markdown

> **Wissenschaftlicher Kontext (19.04.2026):** Diese Infrastruktur operationalisiert die Retrospective-Validation-Gates aus INSTRUKTIONEN.md §29. Relevante Papers: Bailey 2015 (PBO/CSCV), Aghassi 2023 (AQR-Benchmark), Flint-Vermaak 2021 (Half-Life), Palomar 2025 (Seven Sins + Risk-Metrics). Review 2028-04-01.
```

- [ ] **Step 4: portfolio_risk.py — Header-Kommentar**

Top-of-file in `03_Tools/portfolio_risk.py`:

```python
"""
portfolio_risk.py — Portfolio-Risk-Aggregator (Dynasty-Depot)

Wissenschaftlicher Kontext (19.04.2026): Basis für Palomar 2025 Ch 6 Risk-Metrics
(Sortino/Calmar/Max-DD/CVaR/IR). Aktivierung Review 2028-04-01 nach 24+ Monaten
sauberer Return-Serie (Phase 3 R5).
"""
```

- [ ] **Step 5: briefing-sync-check.ps1 — Header-Kommentar**

Top-of-file in `03_Tools/briefing-sync-check.ps1`:

```powershell
# briefing-sync-check.ps1 — STATE/CORE-MEMORY/Faktortabelle → Remote-Trigger-Sync
# Kontext (19.04.2026): Unterstützt §18 Sync-Pflicht und §29.5 Sin #2 Look-Ahead-Prevention
# (Point-in-Time-Persistenz kritisch für spätere Retrospective-Validation).
```

- [ ] **Step 6: morning-briefing-prompt-v2.md — Header-Kommentar**

Ergänze im Header-Frontmatter-Bereich:

```markdown
<!-- Wissenschaftlicher Kontext (19.04.2026): Briefing-Output ist Input für §18 Sync-Pflicht.
Die Faktortabelle-Einträge im Briefing werden eines Tages §29-Retrospective-Analyse speisen
(Bailey CSCV-Datenbasis). Point-in-Time-Disziplin daher kritisch. -->
```

- [ ] **Step 7: INSTRUKTIONEN §18 — Anker zu §29.5 Sin #2**

In `00_Core/INSTRUKTIONEN.md` §18-Bereich die Sync-Pflicht-Beschreibung ergänzen:

Suche die Stelle "Sync-Pflicht bei Score/FLAG/Sparraten-Änderung" und ergänze am Ende des Absatzes:

```
**Wissenschaftlicher Anker:** Die Point-in-Time-Persistenz aller sechs Dateien schützt vor §29.5 Sin #2 (Look-Ahead Bias). Jeder Record muss zum Zeitpunkt der Daten-Sichtung geschrieben werden, nicht rückwirkend. → §29.5 / [[Seven-Sins-Backtesting]]
```

- [ ] **Step 8: INSTRUKTIONEN §27 — Anker zu §29.4 t-Hurdle**

In `00_Core/INSTRUKTIONEN.md` §27 "Scoring-Hygiene"-Bereich am Ende:

```
**Wissenschaftlicher Anker:** Double-Counting-Vermeidung und Bonus-Cap-Check verhindern False-Positives unterhalb §29.4 t-Stat ≥ 3 Hurdle (Harvey/Liu/Zhu). Jede neue Sub-Komponente muss t≥3 erreichen. → §29.4 / [[Aghassi-2023-Fact-Fiction]]
```

- [ ] **Step 9: INSTRUKTIONEN §28 — Anker zu §29.1 PBO + §29.5 Seven-Sins**

In `00_Core/INSTRUKTIONEN.md` §28 "Scoring-Version-Migration-Workflow"-Bereich:

```
**Wissenschaftlicher Anker:** §28.2 Δ-Gate und §28.4 Forward-Verify greifen in die Validation-Ebene ein, die §29 retrospektiv absichert: §29.1 (PBO/CSCV nach Bailey) für Parameter-Variations und §29.5 (Seven-Sins-Pre-Flight) für jeden Migration-Event ab sofort aktiv. → §29.1 / §29.5 / [[Bailey-2015-PBO]] / [[Seven-Sins-Backtesting]]
```

- [ ] **Step 10: INSTRUKTIONEN §29 — Rückverweise-Liste ergänzen**

In `00_Core/INSTRUKTIONEN.md` §29 am Ende vor dem Fußzeilen-Separator:

```markdown

### 29.8 Rückverweise

Andere §§ die auf §29-Gates verweisen:
- §18 Sync-Pflicht → §29.5 Sin #2 (Look-Ahead)
- §27 Scoring-Hygiene → §29.4 t-Hurdle
- §28 Migration-Workflow → §29.1 PBO + §29.5 Seven-Sins
- §30 Live-Monitoring → §29.3 Half-Life (ab Phase 4)
```

- [ ] **Step 11: Commit Phase 2**

```bash
git add 01_Skills/dynastie-depot/SKILL.md 01_Skills/backtest-ready-forward-verify/SKILL.md 03_Tools/backtest-ready/README.md 03_Tools/portfolio_risk.py 03_Tools/briefing-sync-check.ps1 03_Tools/morning-briefing-prompt-v2.md 00_Core/INSTRUKTIONEN.md
git commit -m "$(cat <<'EOF'
feat(skills+instruktionen): paper-integration phase 2 — skill anchors + cross-refs

- dynastie-depot SKILL: Aghassi-Anker an Fundamentals-Review + QMJ-Link an Moat-Validation
- backtest-ready-forward-verify SKILL: §29-Retrospective-Gate-Hinweis an Schritt 7
- 03_Tools/backtest-ready/README.md: Paper-Kontext-Header (Bailey/Aghassi/Flint-Vermaak/Palomar)
- portfolio_risk.py + briefing-sync-check.ps1 + morning-briefing-prompt-v2.md: inline Paper-Kontext-Kommentare
- INSTRUKTIONEN §§18/27/28: Wissenschaftliche Anker zu §29.4/29.5/29.1
- INSTRUKTIONEN §29.8: Rückverweise-Liste

Spec: docs/superpowers/specs/2026-04-19-paper-integration-design.md (976e67a)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### ⚠️ Manuelle Aktion nach Task 5 (User-Entscheidung)

**Phase 2 editiert `01_Skills/dynastie-depot/SKILL.md` und `01_Skills/backtest-ready-forward-verify/SKILL.md`.** Diese Skills sind als ZIP-Pakete deployed:

- `06_Skills-Pakete/dynastie-depot_v3.7.2.zip` (aktuell 57k, Stand 19.04. 01:20)
- `06_Skills-Pakete/backtest-ready-forward-verify.zip` (aktuell 10k, Stand 19.04. 01:20)

**Entscheidung notwendig (User):**

| Option | Wann sinnvoll |
|--------|---------------|
| **Sofort repack + redeploy** nach Phase 2 | Wenn Skills bald live verwendet werden und Paper-Kontext im aktiven Skill-Output sichtbar sein soll |
| **Repack erst nach Phase 4 (konsolidiert)** | Empfohlen — Phase 4 editiert SKILL erneut (Monatsrefresh-Trigger). Ein konsolidiertes Repack spart Overhead. |

**Falls Repack: User führt manuell aus** — ZIP-Repack-Commands sind user-side (z.B. über Datei-Explorer oder bestehende Build-Skripte). Claude pausiert hier, wenn User so entscheidet.

---

## Task 6: Phase 3 — R5 Portfolio-Return-Persistenz (Implementation)

**Files:**
- Create: `05_Archiv/portfolio_returns.jsonl`
- Create: `05_Archiv/benchmark-series.jsonl`
- Create: `05_Archiv/schema-portfolio-returns.md` (Schema-Doku)
- Modify: `03_Tools/portfolio_risk.py` (neuer `--persist daily`-Modus)

- [ ] **Step 1: Read current portfolio_risk.py state**

Read `03_Tools/portfolio_risk.py` vollständig. Identifiziere:
- Bestehenden Argparse-Parser (für `--persist daily`-Flag-Integration)
- Bestehende Preis-Fetch-Logik (defeatbeta-MCP oder yfinance)
- Bestehende Position-Weight-Berechnung

- [ ] **Step 2: Write Schema-Doku in 05_Archiv/schema-portfolio-returns.md**

```markdown
# portfolio_returns.jsonl — Schema v1.0

**Stand:** 19.04.2026 | **Aktiviert:** Phase 3 R5 Paper-Integration

## Record-Schema (append-only JSONL, ein Record pro Tag)

```json
{
  "schema_version": "1.0",
  "date": "YYYY-MM-DD",
  "portfolio_value_gross": 1234.56,
  "cashflow_net": 0.00,
  "portfolio_return": 0.00234,
  "benchmark_value": 5678.90,
  "benchmark_return": 0.00152,
  "positions": [
    {"ticker": "AVGO", "weight_eod": 0.12, "price_eod": 234.56, "value_eod": 148.27}
  ]
}
```

## Felder

- `schema_version`: "1.0" (Major-Bump bei Breaking-Change)
- `date`: ISO-Date. Eindeutig pro Record.
- `portfolio_value_gross`: Gross-Position-Value in EUR (vor Cashflow)
- `cashflow_net`: Netto-Einzahlung/Auszahlung am Tag (+ Spar-Einzahlung, − Entnahme). Kritisch für Return-Rekonstruktion.
- `portfolio_return`: Time-Weighted Daily Return (Cashflow-bereinigt)
- `benchmark_value`: Benchmark-NAV (SPY oder Multifactor-Index)
- `benchmark_return`: Daily Benchmark Return
- `positions[]`: Alle Satelliten + ETF + Gold zum EoD

## Benchmark-Handling

Benchmark wird parallel täglich persistiert in `05_Archiv/benchmark-series.jsonl`. Keine retrospektive Rekonstruktion — Point-in-Time-Disziplin (§29.5 Sin #2).

## Quellen-Fundierung

- Palomar 2025 Ch 6 — Sortino/Calmar/Max-DD/CVaR/IR basieren auf diesem Schema
- §29.5 Sin #2 — Look-Ahead-Prevention via Point-in-Time-Persistenz
- §29.6 Portfolio-Return-Metrik-Layer — Aktivierung Review 2028-04-01 nach 24+ Monaten

## Write-Path

`03_Tools/portfolio_risk.py --persist daily` (ab Phase 3). Append-only, nie Edit. Git-Tracking pflicht.
```

- [ ] **Step 3: Implement --persist daily mode in portfolio_risk.py**

Füge nach existierendem Argparse-Block folgenden Pfad hinzu (Pseudocode, konkrete Implementation-Details aus bestehender Struktur ableiten):

```python
import json
from pathlib import Path
from datetime import date

def persist_daily_snapshot(
    positions: list[dict],
    benchmark_value: float,
    benchmark_return: float,
    portfolio_return: float,
    cashflow_net: float = 0.0,
    archive_path: Path = Path("05_Archiv/portfolio_returns.jsonl"),
    benchmark_path: Path = Path("05_Archiv/benchmark-series.jsonl")
) -> None:
    """Append daily snapshot to portfolio_returns.jsonl + benchmark-series.jsonl."""
    today = date.today().isoformat()
    portfolio_value_gross = sum(p["value_eod"] for p in positions)
    
    record = {
        "schema_version": "1.0",
        "date": today,
        "portfolio_value_gross": round(portfolio_value_gross, 2),
        "cashflow_net": round(cashflow_net, 2),
        "portfolio_return": round(portfolio_return, 5),
        "benchmark_value": round(benchmark_value, 2),
        "benchmark_return": round(benchmark_return, 5),
        "positions": positions
    }
    
    # Duplicate-Date-Guard
    if archive_path.exists():
        with archive_path.open("r", encoding="utf-8") as f:
            for line in f:
                existing = json.loads(line)
                if existing.get("date") == today:
                    raise ValueError(f"Duplicate date {today} in {archive_path}. Delete/edit manually if intentional.")
    
    with archive_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    
    bench_record = {
        "schema_version": "1.0",
        "date": today,
        "benchmark": "SPY",  # TODO: aus Konfiguration
        "value": round(benchmark_value, 2),
        "daily_return": round(benchmark_return, 5)
    }
    with benchmark_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(bench_record, ensure_ascii=False) + "\n")
    
    print(f"✓ Snapshot {today} appended — Portfolio {portfolio_value_gross:.2f} EUR (r={portfolio_return:.4%}), Benchmark SPY={benchmark_value:.2f} (r={benchmark_return:.4%})")


# In main-Argparse:
# parser.add_argument("--persist", choices=["daily"], help="Persistenz-Modus")
# 
# if args.persist == "daily":
#     persist_daily_snapshot(positions=..., benchmark_value=..., ...)
```

**Wichtig:** Die konkrete Datenquelle für Positions/Benchmark ist aus bestehender portfolio_risk.py-Struktur zu ermitteln (defeatbeta/yfinance/Shibui). `cashflow_net` als CLI-Argument `--cashflow` (Default 0.0).

- [ ] **Step 4: Create empty portfolio_returns.jsonl + benchmark-series.jsonl**

```bash
touch "05_Archiv/portfolio_returns.jsonl"
touch "05_Archiv/benchmark-series.jsonl"
```

- [ ] **Step 5: Test — ersten Snapshot erstellen**

Run:
```bash
cd "C:/Users/tobia/OneDrive/Desktop/Claude Stuff"
python 03_Tools/portfolio_risk.py --persist daily --cashflow 0.0
```

Expected:
- Output: `✓ Snapshot 2026-04-19 appended — Portfolio ... EUR (r=...), Benchmark SPY=... (r=...)`
- `05_Archiv/portfolio_returns.jsonl` hat 1 Record
- `05_Archiv/benchmark-series.jsonl` hat 1 Record

- [ ] **Step 6: Verify — JSON-Validität + Schema-Konformität**

Run:
```bash
python -c "import json; rec = json.loads(open('05_Archiv/portfolio_returns.jsonl').readline()); assert rec['schema_version']=='1.0' and 'positions' in rec and 'cashflow_net' in rec and 'benchmark_return' in rec; print('Schema OK:', rec['date'])"
```

Expected: `Schema OK: 2026-04-19` (oder Tagesdatum)

- [ ] **Step 7: Verify — Duplicate-Date-Guard**

Run Snapshot erneut:
```bash
python 03_Tools/portfolio_risk.py --persist daily --cashflow 0.0
```

Expected: Raises `ValueError: Duplicate date ...`

---

## Task 7: Phase 3 — Codex-Review + CORE-MEMORY + STATE + Commit

- [ ] **Step 1: Delegate Code-Review an Codex**

Invoke codex:codex-rescue subagent mit:

> `--resume Phase 3 R5 Code-Review. Datei: 03_Tools/portfolio_risk.py (neue persist_daily_snapshot-Funktion). Schema-Datei: 05_Archiv/schema-portfolio-returns.md. Erster Test-Snapshot in portfolio_returns.jsonl. Prüfe: (1) Look-Ahead-Bias — keine retrospektive Rekonstruktion, nur Point-in-Time; (2) Cashflow-Trennung sauber (Sparraten-Einzahlung separat von Marktbewegung); (3) Duplicate-Date-Guard funktional; (4) Benchmark parallel zum Portfolio-Snapshot persistiert (nicht on-demand); (5) Schema-Versioning pro Record vorhanden; (6) Output-Pfade konsistent mit §18 Sync-Pflicht. GO / GO-MIT-FIXES / NEEDS-REWORK.`

- [ ] **Step 2: Apply Codex-Fixes (falls nötig)**

- [ ] **Step 3: CORE-MEMORY §5 — Phase-3-Aktivierungs-Lektion**

In `00_Core/CORE-MEMORY.md` §5 anhängen:

```markdown

### R5 Portfolio-Return-Persistenz aktiviert (v3.7.2 — 19.04.2026)
**Trigger:** Phase 3 Paper-Integration systemweit (Spec 976e67a).
**Befund:** portfolio_returns.jsonl + benchmark-series.jsonl aktiv. Daily-Schema v1.0 mit schema_version pro Record, Cashflow-Trennung, Duplicate-Date-Guard.
**Regel:**
→ Jeder Handelstag: `python 03_Tools/portfolio_risk.py --persist daily --cashflow <euro>` laufen lassen. Sparraten-Tage explizit mit `--cashflow 285.00`.
→ Git-Commit der JSONL-Dateien zusammen mit STATE-Update pflicht (§18).
→ **Interim-Gate 2027-10-19** (18M Dry-Run risk-metrics-calculation + PBO-Smoke-Test) adressierbar erst nach 540+ Records.
→ **Review-Gate 2028-04-01:** Vollaktivierung §29.6 (Palomar Ch 6 Metriken).
**Präzedenz:** Sin #2 Look-Ahead-Prevention operational durch frühen Persistenz-Start (Codex-Scope-Review 19.04. identifizierte R5 als Blind-Spot in R1-R4-Liste).
```

- [ ] **Step 4: STATE.md — R5-Status-Bullet aktualisieren**

In `00_Core/STATE.md` Abschnitt "System-Zustand" den Interim-Gate-Bullet ergänzen/ersetzen:

```markdown
- **R5 Portfolio-Return-Persistenz aktiv** (seit 19.04.2026): `05_Archiv/portfolio_returns.jsonl` + `benchmark-series.jsonl` Daily-Schema v1.0. Interim-Gate 2027-10-19 (18M-Dry-Run + PBO-Smoke-Test). Review-Aktivierung 2028-04-01.
```

- [ ] **Step 5: Commit Phase 3**

```bash
git add 03_Tools/portfolio_risk.py 05_Archiv/schema-portfolio-returns.md 05_Archiv/portfolio_returns.jsonl 05_Archiv/benchmark-series.jsonl 00_Core/CORE-MEMORY.md 00_Core/STATE.md
git commit -m "$(cat <<'EOF'
feat(infra): paper-integration phase 3 — portfolio-return persistence (daily snapshot)

- portfolio_risk.py: neuer --persist daily Modus mit Cashflow-Trennung + Duplicate-Date-Guard
- 05_Archiv/portfolio_returns.jsonl: Daily-Schema v1.0 (schema_version pro Record)
- 05_Archiv/benchmark-series.jsonl: eigene Benchmark-Zeitreihe (SPY), parallel persistiert
- 05_Archiv/schema-portfolio-returns.md: Schema-Doku
- CORE-MEMORY §5: R5-Aktivierungs-Lektion (Sin #2 Look-Ahead-Prevention)
- STATE.md: R5-Status-Bullet
- Codex-Code-Review bestanden

Wissenschaftliche Basis: Palomar 2025 Ch 6 (künftige Sortino/Calmar/Max-DD/CVaR/IR-Berechnung).
Interim-Gate 2027-10-19, Review-Gate 2028-04-01.

Spec: docs/superpowers/specs/2026-04-19-paper-integration-design.md (976e67a)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 8: Phase 4 — §30 Live-Monitoring & Cadence (Draft)

**Files:**
- Modify: `00_Core/INSTRUKTIONEN.md` (neue §30)

- [ ] **Step 1: Write §30 Draft in INSTRUKTIONEN.md**

In `00_Core/INSTRUKTIONEN.md` nach §29 (vor Fußzeilen-Separator) einfügen:

```markdown

## 30. Live-Monitoring & Cadence

> **Status:** `[AKTIV seit 19.04.2026]` für MSFT CapEx/OCF-FLAG. Weitere Faktor-Klassen nur nach Applied-Learning-Re-Review.

Monatliche Refresh-Pflicht für **aktive Investment-FLAGs** zwischen Earnings-Terminen. Wissenschaftliche Basis: Flint-Vermaak 2021 — Investment-Faktor-Half-Life ≈ 1 Monat. Earnings-Trigger-Cadence (~3M) ist zu träge, wenn ein Investment-Signal bereits ausgelöst wurde.

### 30.1 Trigger-Definition

**"Aktiver FLAG"** (R1 pflicht) = binär ausgelöst in `05_Archiv/backtest-ready/flag_events.jsonl` ohne nachfolgenden `resolve`-Event.

**"Schema-Watch (nicht FLAG-aktiv)"** (R1 NICHT automatisch) = schema-getriggert per FLAG_RULES, aber bewusst nicht aktiviert (z.B. TMO fcf_trend_neg FY25: WC-Delta erklärt FCF-Rückgang, kein struktureller Trend). Schema-Watch ist semantisch separat von STATE.md "Aktive Watches" (= allgemeine Beobachtungsnotizen).

### 30.2 Aktuelle Scope (Stand 19.04.2026)

| Ticker | Kategorie | §30 Pflicht |
|--------|-----------|-------------|
| MSFT | Aktiver FLAG (CapEx/OCF 83.6%) | ✅ Monthly-Refresh |
| TMO | Schema-Watch (fcf_trend_neg WC-Noise) | ❌ Nicht automatisch (Q1 23.04. = natürliches Resolve-Gate) |

### 30.3 Monthly-Refresh-Workflow

1. **Trigger-Prüfung:** Aktueller FCF, CapEx, OpCF abrufen (Shibui oder yfinance)
2. **FLAG-Re-Evaluation:** Threshold-Check gegen FLAG_RULES — hält FLAG? Auflösung?
3. **FLAG-Event append** bei Zustandsänderung: `archive_flag.py resolve` oder erneuter `trigger`
4. **CORE-MEMORY §5:** Zwischenupdate mit FLAG-Zustand
5. **Kein Re-Score** der Ticker-Gesamt-DEFCON-Bewertung — nur Investment-Block-Observation

### 30.4 Constraints (Applied-Learning-Wächter)

- **Keine Auto-Rescore** — §30 prüft nur bestehende FLAG-Trigger, keine neue Punkte-Logik
- **Keine Ausweitung** auf andere Faktor-Klassen (Quality/Value/Momentum) ohne Applied-Learning-Re-Review
- **Ausweitung auf andere Ticker** innerhalb Investment-Klasse zulässig, sobald neue aktive Investment-FLAGs entstehen

### 30.5 Wissenschaftliche Fundierung

- [[Flint-Vermaak-2021-Decay]] — Investment-Half-Life ~1M
- [[Factor-Information-Decay]] — Operative Konsequenzen
- **Rückverweis:** §29.3 (Temporal-Konsistenz-Gate) — wissenschaftlicher Anker
```

- [ ] **Step 2: INSTRUKTIONEN-Fußzeile v-Bump**

Suche letzte Zeile mit `INSTRUKTIONEN.md v1.10` und ersetze:

```
*🦅 INSTRUKTIONEN.md v1.11 (§28-30 Migration + Retrospective-Gate + Live-Monitoring) | Dynastie-Depot v3.7 | Stand: 19.04.2026*
```

- [ ] **Step 3: Commit §30-Draft (vorläufig, vor Codex-Review)**

```bash
git add 00_Core/INSTRUKTIONEN.md
git commit -m "docs(instruktionen): §30 Live-Monitoring & Cadence draft (pre-codex-review)"
```

---

## Task 9: Phase 4 — Codex-Review §30 + Apply Fixes

- [ ] **Step 1: Delegate §30-Review an Codex**

Invoke codex:codex-rescue subagent mit:

> `--resume Phase 4 §30-Formulierungs-Review. Ziel: §30 wird neue Live-Monitoring-§ in INSTRUKTIONEN.md mit Monthly-Refresh-Pflicht für aktive Investment-FLAGs. Prüfe: (1) Versteckte Scoring-Änderung? — §30.4 sagt "keine Auto-Rescore, keine neue Punkte-Logik"; ist das hart genug formuliert?; (2) "Aktiver FLAG" vs "Schema-Watch" Disambiguierung klar?; (3) Applied-Learning-Wächter gegen §30-Ausweitung präzise?; (4) Kollision mit STATE.md "Aktive Watches"?; (5) §29.3-Rückverweis korrekt (Half-Life-Kontext)?; (6) MSFT-vs-TMO-Unterscheidung sauber?; (7) Monthly-Refresh-Workflow Schritte vollständig oder Lücke?; (8) v-Bump v1.10→v1.11 passt? GO / GO-MIT-FIXES / NEEDS-REWORK. Lies 00_Core/INSTRUKTIONEN.md zur Review.`

- [ ] **Step 2: Apply Codex-Fixes**

Falls Codex Änderungen verlangt: Edit `00_Core/INSTRUKTIONEN.md` §30 entsprechend.

- [ ] **Step 3: CORE-MEMORY §5 — Phase-4-Aktivierungs-Lektion**

In `00_Core/CORE-MEMORY.md` §5 anhängen:

```markdown

### R1 §30 Live-Monitoring aktiviert (v3.7.2 — 19.04.2026)
**Trigger:** Phase 4 Paper-Integration systemweit (Spec 976e67a).
**Befund:** §30 Live-Monitoring & Cadence aktiv. Monthly-Refresh pflicht für aktive Investment-FLAGs (Flint-Vermaak Investment-Half-Life ~1M).
**Regel:**
→ Aktuelle Scope: MSFT CapEx/OCF 83.6% → Monthly-Refresh pflicht (erster Refresh ~19.05.2026)
→ TMO fcf_trend_neg bleibt Schema-Watch, keine §30-Pflicht (Q1 23.04. = natürliches Resolve-Gate)
→ §30-Ausweitung auf weitere Faktor-Klassen erfordert Applied-Learning-Re-Review (Codex-Wächter 19.04.)
→ Semantik-Trennung: "Aktiver FLAG" (binär in flag_events.jsonl) vs. "Schema-Watch" (schema-getriggert, nicht aktiviert) vs. STATE.md "Aktive Watches" (allgemeine Beobachtung)
**Präzedenz:** Applied-Learning "Paper-Ingest ≠ System-Update" in Monitoring-Layer operationalisiert — §30 ist Monitoring-Cadence-Regel, kein Scoring-Change.
```

- [ ] **Step 4: dynastie-depot SKILL — Monatsrefresh-Trigger-Hinweis**

In `01_Skills/dynastie-depot/SKILL.md` an geeigneter Stelle (z.B. Workflow-Übersicht oder Trigger-Liste) ergänzen:

```markdown
**§30 Live-Monitoring (ab 19.04.2026):** Monatlicher Refresh aktiver Investment-FLAGs (aktuell: MSFT CapEx-FLAG). Aufruf: `!MonatsRefresh <TICKER>` oder manuell per CORE-MEMORY-Lektion. Kein Re-Score, nur FLAG-Trigger-Prüfung.
```

- [ ] **Step 5: STATE.md — §30-Bullet im System-Zustand**

In `00_Core/STATE.md` Abschnitt "System-Zustand" ergänzen:

```markdown
- **§30 Live-Monitoring aktiv** (seit 19.04.2026): Monthly-Refresh pflicht für MSFT CapEx-FLAG (Flint-Vermaak Investment-Half-Life ~1M). TMO Schema-Watch (keine §30-Pflicht).
```

- [ ] **Step 6: Commit Phase 4 finalisiert**

```bash
git add 00_Core/INSTRUKTIONEN.md 00_Core/CORE-MEMORY.md 00_Core/STATE.md 01_Skills/dynastie-depot/SKILL.md
git commit -m "$(cat <<'EOF'
feat(instruktionen): §30 Live-Monitoring — Monthly-Refresh for active Investment-FLAGs (R1)

- §30 5 Sub-Sections: Trigger-Definition, Scope, Workflow, Constraints, Fundierung
- "Aktiver FLAG" (binär in flag_events.jsonl) vs "Schema-Watch" (schema-getriggert, nicht aktiviert) disambiguiert
- MSFT CapEx/OCF 83.6% → §30 pflicht; TMO fcf_trend_neg → Schema-Watch, keine §30-Pflicht
- Applied-Learning-Wächter: Ausweitung auf weitere Faktor-Klassen erfordert Re-Review
- dynastie-depot SKILL + CORE-MEMORY §5 + STATE.md aktualisiert
- INSTRUKTIONEN-Version v1.10 → v1.11
- Codex-§30-Formulierungs-Review bestanden

Wissenschaftliche Basis: Flint-Vermaak 2021 Investment-Faktor-Half-Life ~1M → Earnings-Cadence 3M zu träge für aktive FLAGs.

Spec: docs/superpowers/specs/2026-04-19-paper-integration-design.md (976e67a)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### ⚠️ Manuelle Aktion nach Task 9 (User-Pflicht)

**Phase 4 editiert erneut `01_Skills/dynastie-depot/SKILL.md` (Monatsrefresh-Trigger-Hinweis).** Kumulativ zusammen mit Phase-2-Edits ist jetzt ein **ZIP-Repack + Redeploy** sinnvoll:

**Empfohlene Aktion:**

1. **Version-Bump entscheiden:** `dynastie-depot_v3.7.2.zip` → `dynastie-depot_v3.7.3.zip` (wenn substantiell, z.B. §30-Integration) oder replace v3.7.2 in-place
2. **Repack dynastie-depot:** Source ist `01_Skills/dynastie-depot/` → ZIP das gesamte Verzeichnis neu nach `06_Skills-Pakete/dynastie-depot_v<version>.zip`
3. **Repack backtest-ready-forward-verify:** Source ist `01_Skills/backtest-ready-forward-verify/` → ZIP nach `06_Skills-Pakete/backtest-ready-forward-verify.zip` (bestehendes File überschreiben)
4. **Redeploy (je nach User-Setup):** Entweder über Claude-Code-Plugin-Loader oder manuelles Kopieren in das aktive Skill-Verzeichnis
5. **Commit Repack:** `git add 06_Skills-Pakete/*.zip && git commit -m "chore(skills): repack dynastie-depot + backtest-ready-forward-verify after Phase 2+4 Paper-Integration"`

**Claude pausiert hier** und wartet auf User-GO nach erfolgreichem Repack + Redeploy, bevor Task 10 (System-Audit) startet.

---

## Task 10: System-Audit

**Zweck:** Multi-Source-Drift-Check (CLAUDE.md Applied-Learning #2) nach Abschluss aller Phasen. Sicherstellen, dass alle Wahrheitsquellen konsistent sind, Versionsnummern aligned, und keine widersprüchlichen Einträge zurückbleiben.

**Files (Audit-Targets):**
- `00_Core/STATE.md` — Status-Bullets, FLAGs, Trigger
- `00_Core/CORE-MEMORY.md` — §5-Lektionen (R5 + R1 + existierend)
- `00_Core/INSTRUKTIONEN.md` — §§29/30 konsistent, v-Footer
- `00_Core/KONTEXT.md` — ggf. Scope-Bezug zu §29/§30
- `00_Core/Faktortabelle.md` — Ticker-Einträge konsistent mit Satelliten-Vault-Pages
- `07_Obsidian Vault/.../wiki/synthesis/Backtest-Methodik-Roadmap.md`
- `07_Obsidian Vault/.../wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md`
- `07_Obsidian Vault/.../Investing Mastermind/log.md`
- `CLAUDE.md` — Applied-Learning-Counter aktuell (9/20 oder 10/20?), 4-Dim-Gate-Bullet passt

- [ ] **Step 1: Multi-Source-Drift-Check via Grep**

Run die folgenden Checks und dokumentiere Ergebnisse. Ziel: Widersprüche aufspüren.

```bash
# Check A: §30 in allen relevanten Dateien referenziert?
echo "=== §30 References ==="
grep -rln "§30\|Paragraph 30\|Live-Monitoring & Cadence" 00_Core/ CLAUDE.md "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/" --include="*.md"

# Check B: Alle 4 Papers in allen Wahrheitsquellen erwähnt?
echo "=== Paper Coverage ==="
for paper in "Bailey-2015-PBO" "Aghassi-2023-Fact-Fiction" "Flint-Vermaak-2021-Decay" "Palomar-2025-Portfolio-Optimization"; do
    echo "--- $paper ---"
    grep -rln "$paper" 00_Core/ "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/" --include="*.md" | wc -l
done

# Check C: Version-Konsistenz
echo "=== Versions ==="
grep "INSTRUKTIONEN.md v" 00_Core/INSTRUKTIONEN.md | tail -1
grep "dynastie-depot" 01_Skills/dynastie-depot/SKILL.md | head -3
grep "^# Dynasty" 00_Core/STATE.md 00_Core/CORE-MEMORY.md

# Check D: R5-Schema-Version consistent
echo "=== R5 Schema ==="
head -1 05_Archiv/portfolio_returns.jsonl
head -1 05_Archiv/benchmark-series.jsonl

# Check E: Interim-Gates
echo "=== Interim-Gates ==="
grep -rln "2027-10-19\|2027-10-17" 00_Core/ --include="*.md"

# Check F: FLAG-Semantik — aktiv vs. schema-getriggert
echo "=== FLAG Semantik ==="
grep -rln "Schema-Watch\|aktiver FLAG\|schema-getriggert" 00_Core/ --include="*.md"
```

- [ ] **Step 2: Faktortabelle-Satelliten-Cross-Check**

Verifiziere dass jede Satelliten-Ticker-Row in `00_Core/Faktortabelle.md` konsistent mit aktuellem STATE.md Score ist. Keine neuen Score-Änderungen erwartet (Track 3 ist kein Scoring-Change), aber Format/Links können driften.

Read `00_Core/Faktortabelle.md` und vergleiche Ticker-Einträge mit `00_Core/STATE.md` Portfolio-State-Tabelle. Expected: identische Scores, DEFCON-Level, FLAGs.

- [ ] **Step 3: CLAUDE.md Applied-Learning-Counter-Check**

Read `CLAUDE.md` und verifiziere:
- Counter ist aktuell (8/20, 9/20, oder 10/20 je nachdem was durch Track 3 hinzukam)
- "Backtest-Validation = 4-Dim-Gate"-Bullet passt zu §29.1-5
- Historie-Zeile aktualisiert wenn nötig

**Falls ein neues Bullet aus Track 3 gerechtfertigt ist** (z.B. "§30 Cadence für aktive Investment-FLAGs"), hinzufügen und Counter +1. Oder bewusst NICHT hinzufügen (Codex-Feedback einholen bei Unsicherheit).

- [ ] **Step 4: Vault-Synthesen-Update-Check**

Verifiziere dass die beiden Synthesen (`Backtest-Methodik-Roadmap.md` und `Wissenschaftliche-Fundierung-DEFCON.md`) §30 erwähnen wo passend:

```bash
grep -l "§30\|Live-Monitoring\|Monthly-Refresh" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/"*.md
```

Falls 0 Treffer: minimal-Edit in `Wissenschaftliche-Fundierung-DEFCON.md` mit §30-Erwähnung (Flint-Vermaak operative Konsequenz).

- [ ] **Step 5: log.md Closing-Entry**

In `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/log.md` Final-Closing-Entry anhängen:

```markdown

## 2026-04-19 — Track 3 Paper-Integration systemweit ABGESCHLOSSEN

**5 Phasen fertig:**
- Phase 1a: 11 Satelliten-Pages mit Factor-Exposure-Block
- Phase 1b: 6 defcon-Concepts + 8 bestehende Concepts mit Paper-Ankern
- Phase 2: 2 Skills + 3 Tool-Dokus + INSTRUKTIONEN §§18/27/28/29 Querverweise
- Phase 3: R5 Portfolio-Return-Persistenz aktiv (portfolio_returns.jsonl + benchmark-series.jsonl Daily-Schema v1.0)
- Phase 4: §30 Live-Monitoring & Cadence aktiviert (MSFT CapEx-FLAG Monthly-Refresh)

**Commits:** 5 Phasen-Commits + Spec (976e67a) + Plan + System-Audit-Fixes (falls nötig)

**Skills repacked:** dynastie-depot + backtest-ready-forward-verify (Phase 2 + 4 Edits)

**Interim-Gate 2027-10-19** (PBO-Smoke-Test + 18M-Dry-Run risk-metrics-calculation).
**Review-Gate 2028-04-01** (Volle §29.1-3/6 Aktivierung).

**Applied-Learning-Regel gewahrt:** Keine Scoring-Kern-Änderungen, nur Monitoring/Dokumentation/Infrastruktur/Validation-Vorbau.
```

- [ ] **Step 6: STATE.md Closing-Update**

Verifiziere dass `00_Core/STATE.md` am Ende des Track 3 alle Status-Bullets sauber aktualisiert sind:
- R5 Portfolio-Return-Persistenz aktiv
- §30 Live-Monitoring aktiv (MSFT pflicht, TMO Schema-Watch)
- Interim-Gate 2027-10-19
- DEFCON-Version unverändert (v3.7.2 — kein Scoring-Change!)

- [ ] **Step 7: Audit-Findings-Commit (falls Drift gefunden)**

Falls Step 1-6 Inkonsistenzen gefunden haben, inline fixen und committen:

```bash
git add 00_Core/ CLAUDE.md "07_Obsidian Vault/"
git commit -m "$(cat <<'EOF'
chore(audit): track-3 system-wide consistency check — drift-fixes

Multi-Source-Drift-Check (CLAUDE.md Applied-Learning #2) nach Track 3:
- [Fixed items based on Step 1-6 findings]

Spec: docs/superpowers/specs/2026-04-19-paper-integration-design.md (976e67a)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Falls keine Drift: Skip Commit, notify User "System-Audit clean, keine Drift gefunden".

- [ ] **Step 8: Codex-Final-Audit-Review**

Invoke codex:codex-rescue subagent mit:

> `--resume Final System-Audit nach Track 3 Paper-Integration (5 Phasen). Prüfe Multi-Source-Konsistenz: (1) §30 in allen relevanten Dateien erwähnt (INSTRUKTIONEN, STATE, CORE-MEMORY, SKILL, Vault-Synthese); (2) Alle 4 Papers haben konsistente Referenzen in 00_Core/ und Vault; (3) Versions-Disziplin (DEFCON v3.7.2 unverändert, INSTRUKTIONEN v1.11, Skills repacked oder nicht?); (4) Applied-Learning-Counter in CLAUDE.md passt zur Realität; (5) Keine widersprüchlichen Einträge zwischen STATE.md und CORE-MEMORY §5 + §6 Versionsverlauf; (6) R5 Persistenz läuft ohne Look-Ahead-Verletzung. Gib Audit-Bericht zurück mit Befund + etwaigen Korrektur-Hinweisen. Am Ende: SYSTEM-CLEAN / CORRECTIONS-NEEDED.`

- [ ] **Step 9: Apply Codex-Final-Fixes (falls nötig)**

---

## Task 11: Final Sync + Push

- [ ] **Step 1: Running-Check aller Phasen**

```bash
git log --oneline -10
```

Expected (Top-Commits sollten beinhalten):
- `phase 4 — §30 Live-Monitoring + Monthly-Refresh`
- `phase 3 — portfolio-return persistence`
- `phase 2 — skill anchors + cross-refs`
- `phase 1b — concept cross-links + index/log`
- `phase 1a — satellites + factor-exposure blocks`
- `docs(spec): paper-integration systemweit` (976e67a)

- [ ] **Step 2: STATE.md Final-Kohärenz-Check**

Open `00_Core/STATE.md` und verifiziere:
- R5-Bullet vorhanden
- §30-Bullet vorhanden
- Interim-Gate 2027-10-19 passt
- Keine alten Widersprüche

- [ ] **Step 3: Push origin main**

User-Approval einholen: "Track 3 komplett committed. Soll ich origin main pushen? (Phase 1a-4 + Spec werden sichtbar)"

Nach User-GO:
```bash
git push origin main
```

Expected: `X commits pushed to origin/main`

- [ ] **Step 4: Final-Log**

```bash
git log --oneline origin/main..HEAD
```

Expected: leer (alle lokal synced)

- [ ] **Step 5: Acceptance-Gesamt-Check**

Verifikation aller Acceptance-Kriterien aus Spec:

```bash
# Phase 1a
echo "=== Phase 1a ==="
grep -l "Factor-Exposure (Aghassi 2023)" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/entities/satelliten/"*.md | wc -l
echo "Expected: 11"

# Phase 1b
echo "=== Phase 1b ==="
grep -l "§29" "07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/"*.md | wc -l
echo "Expected: 6"

# Phase 2
echo "=== Phase 2 ==="
grep -c "§29" 00_Core/INSTRUKTIONEN.md
echo "Expected: >=10 (alte §29-Referenzen + neue Anker in §§18/27/28)"

# Phase 3
echo "=== Phase 3 ==="
test -s "05_Archiv/portfolio_returns.jsonl" && echo "portfolio_returns.jsonl has content" || echo "FAIL"
test -s "05_Archiv/benchmark-series.jsonl" && echo "benchmark-series.jsonl has content" || echo "FAIL"

# Phase 4
echo "=== Phase 4 ==="
grep -c "## 30\. Live-Monitoring" 00_Core/INSTRUKTIONEN.md
echo "Expected: 1"
```

---

## Self-Review (nach Plan-Write, nicht im Execution-Pfad)

**Spec coverage check (gegen docs/superpowers/specs/2026-04-19-paper-integration-design.md):**

| Spec-Item | Task |
|-----------|------|
| A: 11 Satelliten-Cross-Links | Task 1, 2 |
| A: 6 defcon-Concepts | Task 2 |
| A: ~10 bestehende Concepts | Task 3 |
| A: index.md + log.md | Task 3 Steps 9-10 |
| B: dynastie-depot SKILL | Task 5 Step 1 |
| B: backtest-ready-forward-verify SKILL | Task 5 Step 2 |
| B: Tool-READMEs + inline-Kommentare | Task 5 Steps 3-6 |
| C: INSTRUKTIONEN §§18/27/28/29 | Task 5 Steps 7-10 |
| R4: Factor-Exposure pro Satellit (5-Zeilen, stark/moderat/schwach/n.a.) | Task 1 |
| R5: portfolio_returns.jsonl Daily-Schema | Task 6 |
| R5: benchmark-series.jsonl | Task 6 Step 2+5 |
| R5: Daily-Schema mit schema_version pro Record | Task 6 Step 2+3 |
| R5: Cashflow-Trennung | Task 6 Step 3 |
| R5: Codex-Review pflicht | Task 7 Step 1 |
| R1: §30 Live-Monitoring | Task 8 |
| R1: MSFT pflicht, TMO Schema-Watch | Task 8 Step 1 §30.2 |
| R1: Applied-Learning-Wächter | Task 8 Step 1 §30.4 |
| R1: Codex-Review §30 | Task 9 |
| Phase 1b Codex-Konsistenz-Pass | Task 4 |
| System-Audit (Multi-Source-Drift-Check) | Task 10 |
| ZIP-Repack-User-Hinweis (Skill-Deployables) | Callout nach Task 5, Callout + Pause nach Task 9 |
| Push-Sync | Task 11 |

**Placeholder-Scan:** Keine TBD/TODO/fill-in. Einzelner `# TODO: aus Konfiguration` in Task 6 Step 3 zur Benchmark-Ticker-Konfiguration — OK, weil Executor das adaptiv aus portfolio_risk.py bestehender Logik ableiten muss (kontextabhängig).

**Type-Konsistenz:** `persist_daily_snapshot()` in Task 6 konsistent referenziert. `portfolio_returns.jsonl` / `benchmark-series.jsonl` durchgängig.

**Execution-Reihenfolge:** B1.5 — Phase 1a → 1b → 2 → 3 → 4 → System-Audit → Push. Strictly sequential. Abhängigkeiten:
- Task 4 (Codex-Konsistenz-Pass) braucht Task 2+3 completed
- Task 7 (Codex-Code-Review) braucht Task 6 (Code committed vor Review)
- Task 9 (Codex-§30-Review) braucht Task 8 (§30-Draft committed vor Review)
- Manueller ZIP-Repack-Pause-Gate nach Task 9 (User-Pflicht, vor Task 10)
- Task 10 (System-Audit) braucht alle vorherigen + Skill-Repack entschieden
- Task 11 (Push) braucht Task 10 clean

---

*🦅 Dynasty-Depot Track 3 | Paper-Integration systemweit | Implementation Plan v1.0 — 19.04.2026*

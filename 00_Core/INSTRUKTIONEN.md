# ⚙️ INSTRUKTIONEN.md — Handlungsanweisungen & Skill-Guidance
**Version:** 1.15 (§0 De-Monolith-Pilot 2026-06-09 — §0-Volltext ausgelagert nach `CODE_GUIDELINES.md`, hier Stub + Sub-Anchors; Routing-Anker in CLAUDE.md umgebogen. Vorher 1.14: §0.5/§0.6 NEU 2026-05-13)
> Dieses Dokument beschreibt das WIE — User-Workflows, Befehle, Meta-Regeln.
> Scoring-Technik → [SKILL.md](../01_Skills/dynastie-depot/SKILL.md) | Strategie → KONTEXT.md | Gedächtnis → CORE-MEMORY.md

## Verweise
- [STATE.md](STATE.md) — Hub
- [PORTFOLIO.md](PORTFOLIO.md) — Portfolio-State (Primär, §22 Sparplan-Formel-Anwendung)
- [PIPELINE.md](PIPELINE.md) — Pipeline-Items (§18 Event-Typ "Pipeline")
- [SYSTEM.md](SYSTEM.md) — System-Zustand (§18 Event-Typ "System", §27.5 Guard-Pfad)
- [CORE-MEMORY.md](CORE-MEMORY.md) — Lektionen + Per-Ticker + Lifecycle
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail
- [RETROSPECTIVE-GATE.md](RETROSPECTIVE-GATE.md) — §29 Detail-Spec (4-Dimensionen-Framework, Future-Activation 2028)
- [`../03_Tools/morning-briefing-spec.md`](../03_Tools/morning-briefing-spec.md) — §24+§25 Detail-Spec (Briefing-Trigger v3.1.1 + Sync-Workflows)

---

## §0. Code-Verhaltens-Regeln (Präambel) — Stub

> ⚠️ **VERHALTENSREGEL — vor jedem Code-/File-Edit:** Vollständige Regeln ausgelagert nach [`CODE_GUIDELINES.md`](CODE_GUIDELINES.md) (09.06.2026, De-Monolith-Pilot, Token-Effizienz per-Trigger-Load). **Zwingend laden + befolgen** vor Code-/File-Edit-Operationen — **nicht** bei Markdown-Sync/Wiki/reinen Lese-Vorgängen oder trivialen Edits. Wird via CLAUDE.md Routing-Table „Code-Edit-Session" geladen. Hier nur Stub + Sub-Anchors für Cross-Reference-Erhalt.

- **§0.1 Think Before Coding** — Annahmen explizit, Rückfrage statt Raten, einfachere Alternative pushen, bei Konfusion stoppen → `CODE_GUIDELINES.md §0.1`
- **§0.2 Simplicity First** — Minimum-Code, keine spekulative Abstraktion/Flexibilität/Error-Handler → `CODE_GUIDELINES.md §0.2`
- **§0.3 Surgical Changes** — nur Nötiges anfassen, kein Drive-by-Refactor, eigene Orphans entfernen, Stil matchen → `CODE_GUIDELINES.md §0.3`
- **§0.4 Goal-Driven Execution** — verifizierbare Ziele, Test-first bei Bug/Refactor → `CODE_GUIDELINES.md §0.4`
- **§0.5 Pre-Refactor-Caller-Scan** — `Grep` auf Symbol codebase-weit vor Signatur-Edit mit externen Aufrufern → `CODE_GUIDELINES.md §0.5`
- **§0.6 Approach-Reset-Schwelle** — nach 2 strukturell-identischen Fehlversuchen Stop → Codex/Plan/User → `CODE_GUIDELINES.md §0.6`

**Konflikt-Auflösung:** Bei Konflikt zwischen §0 und einem späteren spezifischen § gewinnt der spezifische §. §0 ist Default-Verhalten, kein Override. (Bezugs-Tabelle §27.5/§29.5/§18-Carve-out + Karpathy-Upstream-Watch → `CODE_GUIDELINES.md`.)

---

## 1. Befehls-Übersicht

| Befehl | Funktion | Dauer |
|--------|----------|-------|
| `!Analysiere [TICKER]` | 100-Punkte-DEFCON-Vollanalyse | ~20–25 min |
| `!CAPEX-FCF-ANALYSIS [TICKER] [NAME]` | Excel-Tiefenanalyse, 6 Sheets | ~25–30 min |
| `!Rebalancing` | Sparplan-Drift-Check + Vorschlag | ~10 min |
| `!QuickCheck [TICKER\|ALL]` | Ampel-Check, kein Deep Dive | ~3–5 min |
| `!Briefing` | Manuelles Morning Briefing (Kurs-Check, FLAGs, Earnings) | ~3-5 min |
| `!EarningsPreview [TICKER]` | Earnings-Vorbereitung (48h vor Call) | ~5-10 min |
| `!EarningsRecap [TICKER]` | Press-Release-Recap Tag 0 post-Call (kein Score-Move, siehe §19.1) | ~5-10 min |
| `!EarningsCalendar` | Wöchentlicher Earnings-Überblick | ~2-3 min |
| `!InsiderScan` | Form-4-Scan der 8 US-Satelliten (standalone, ohne `!Analysiere`) | ~5 min |
| `!ParaSync18 <event-type> [--also …]` | §18-Multi-File-Sync-Orchestrator vor `git commit` (§18.0) | ~1-3 min |
| `!SyncBriefing` | Briefing-relevante `00_Core/`-Änderungen ins Repo pushen (Pflicht-Review-Gate, kein Auto-Commit) | ~2-3 min |
| `!BriefingCheck` | Vorab-Check ob 10:00-Briefing-Trigger aktuelle Daten liest | ~30s |
| `!SessionClose` | Session-Ende-Workflow: lokale Commits autonom, Push nur nach Freigabe (§25.5) | ~3-5 min |

---

## 2. Analyse-Pipeline (Stufe 0 → Entscheidung)

```
Impuls / Idee
     ↓
[STUFE 0]  Quick-Screener      → 🟢 weiter | 🟡 Watchlist | 🔴 aussortieren
     ↓ nur 🟢
[STUFE 1]  Stock Report        → Intelligence-Report (Datei)
     ↓
[BEFUNDE]  Status-Matrix-Check → active-scoring identifizieren (§4 Router)
     ↓
[STUFE 2]  !Analysiere         → DEFCON 100-Punkte-Score
     ↓ nur Score ≥ 80 + kein FLAG
[STUFE 3]  !CAPEX-FCF-ANALYSIS → Excel-Tiefenanalyse
     ↓
[ENTSCHEIDUNG] Einstieg / Watchlist / Veto
```

**Grundprinzip:** Jede Stufe 0/1/2/3 ist ein Tor. Wer es nicht passiert, kommt nicht weiter.

**[BEFUNDE]-Schritt** ist **kein** Filter-Tor, sondern **Pflicht-Vorbereitung** für Stufe 2: Status-Matrix in [[Wissenschaftliche-Fundierung-DEFCON]] lesen, die für diesen Ticker relevanten `active-scoring`-Befunde identifizieren. Ohne diesen Schritt kein konsistentes DEFCON-Scoring (B10 Chain-of-Thought-Prinzip). Details siehe §4 Befunde-Router.

---

## 3. STUFE 0 — Quick-Screener

### Drei harte Filter:

| Filter | 🟢 Grün | 🟡 Gelb | 🔴 Rot |
|--------|---------|---------|--------|
| P/FCF | ≤ 35 | 35–45 | > 45 |
| ROIC | ≥ 15% | 12–15% | < 12% |
| Moat-Proxy | GM > 40% + CAGR > 8% | Eines knapp verfehlt | Eines deutlich verfehlt |

**Sonderregeln:**
- BRK.B, MKL, FFH.TO → P/B statt P/FCF (Float-Modelle)
- COST → strukturell niedrige GM — Exception aktiv
- Versicherungen → Combined Ratio statt ROIC

---

## 4. STUFE 2 — DEFCON-Scoring (100-Punkte-Matrix)

### Befunde-Router (Pflicht vor jedem Scoring-Start)

**Single Source of Truth:** Die kanonische **Status-Matrix** in `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` §Status-Matrix klassifiziert jeden wissenschaftlichen Befund (aktuell B1–B28, jeder zukünftige Befund BxN) mit einem von sechs Status-Labels. §4 ist **nur der Router** — Befund-Content wird nicht hier dupliziert.

| Status | Aktion in !Analysiere |
|--------|-----------------------|
| `active-scoring` | **Pflicht-Anwendung** im zugehörigen DEFCON-Block; Nennung im Output-Block "Befunde angewendet" (SKILL.md-Template) |
| `active-scoring-validation` | **Optional-Nennung** als Validation-Suffix zur bestehenden Block-Begründung (z.B. „Insider-Block: B26-validated"). Kein neuer Score-Pfad, keine Migration nötig (eingeführt 26.04.2026 — Codex-Re-Klassifikation B26) |
| `design-context` | **Kein eigenständiger Score-Pfad** (verändert keinen Block-Score, keinen Subscore, kein Gate-Verhalten). Im !Analysiere-Output **zulässig ausschließlich als nicht-scorender Architektur-Anker in Klammer-Notation mit `design-context`-Suffix + Erklärtext** (vgl. Insider-/Sentiment-Block-Templates in SKILL.md Schritt 3 — z.B. `[+ B27 Ke/Huddart/Petroni \`design-context\`: 24-Monats-Window deferred]`, `[+ B28 Tetlock \`design-context\`: Mean-Reversion-Architektur-Anker]`). Außerhalb des Outputs auch in Skill-Roadmap-Diskussionen, Konsolidierungstag-Reviews, Wiki-Synthesis-Updates referenzierbar. Migration zu `active-scoring` nur via §28.1 + §29.4-Hurdle (eingeführt 26.04.2026 — Codex-Re-Klassifikation B27, B28; präzisiert in Pre-Phase-C 27.04.2026) |
| `meta-gate` | **Nicht verwenden** in per-Ticker-Analyse — feuert ausschließlich bei Migration (§28), Retrospective (§29: B15→§29.1, B16→§29.2/4, B17→§29.3, B18/B19→§29.5, B20→§29.1+6, **B25→§29.7**), Skill-Self-Audit (§33) |
| `design-rejected` | **Nicht reaktivieren** — bei Rückfrage "warum fehlt X?" Rejection-Begründung aus Status-Matrix zitieren (nicht ad-hoc einführen) |
| `future-arch` | **Keine Adoption im aktiven Scoring** — Bewertung ausschließlich via §33 Skill-Self-Audit-Gate |

**Pflicht-Abfolge bei jedem Scoring-Start:**

1. **Status-Matrix lesen** (Synthesis-Link oben) — verifizieren, welche Befunde `active-scoring` sind und welchen DEFCON-Block sie adressieren.
2. **Ticker-Befunde-Mapping**: Aus den `active-scoring`-Befunden alle identifizieren, die für diesen Ticker substantiv greifen (z.B. B4 Moat-Quellen greift nur bei Ticker mit nicht-trivialem Moat-Rating; B6 Quality-Trap greift nur wenn Wide Moat + teure Bewertung kombiniert vorliegen).
3. **B10 Chain-of-Thought**: Vor der Punktvergabe pro DEFCON-Block die zutreffenden Befunde durchdenken. Reasoning vor Score, nicht Score vor Reasoning.
4. **Output-Block "Befunde angewendet"** pro DEFCON-Block die angewandten Befund-IDs listen (SKILL.md-Template — reine Transparenz, kein Score-Impact).

**Neue Befunde (B29+):** Werden in der Synthesis-Matrix klassifiziert, nicht in §4 dupliziert. §4 bleibt Router, wächst nicht mit neuen Papers mit. B25-B28 wurden 26.04.2026 in der Synthesis-Matrix eingetragen (Codex-Re-Klassifikation: B26 → `active-scoring-validation`, B27/B28 → `design-context`, B25 → `meta-gate` mit §29.7-Mapping).

### Scoring-Skalen, DEFCON-Schwellen, FLAGs

> **Alle Scoring-Details → [SKILL.md](../01_Skills/dynastie-depot/SKILL.md) §Scoring-Skalen / §DEFCON-Schwellenwerte / §FLAG-Regeln**
>
> Dort verbindlich: Block-Gewichtung (50/20/10/10/10), Detailskalen (Fwd P/E, P/FCF, CapEx/OCF, ROIC, FCF-Yield, Bilanz, OpM TTM), Quality-Trap-Interaktion v3.7, Fundamentals-Cap 50, Bonus-Metriken, DEFCON-Schwellen-Tabellen (Neueinstieg + Bestand), automatische FLAGs.

---

## 5. Sentiment-Scoring (v3.7-Kalibrierung)

> **Detailskalen → [SKILL.md §Sentiment (10 Punkte)](../01_Skills/dynastie-depot/SKILL.md)**
>
> Strong-Buy-Ratio / Sell-Ratio / PT-Upside — v3.7-Kalibrierung (B11: Crowd-Consensus-Malus, Extrem-Consensus-Warnung).

**Wissenschaftliche Anker (4 Layer, kein Score-Effekt — `design-context` + `active-scoring`-Validation):**
- **B11 Jadhav/Mirza 2025** — `active-scoring`: Crowd-Consensus-Bias-Korrektur (Sell-Ratio dreistufig + >60% Strong-Buy-Malus)
- **B19 FINSABER 2026** — `meta-gate`: Bull/Bear-Asymmetrie + Skill-Self-Audit (§29.5/§33)
- **B24 FinDPO 2025** — `future-arch`: DPO-Pipeline für künftige Sentiment-Block-Architektur (orthogonal heute)
- **B28 Tetlock 2007** — `design-context` (eingeführt 26.04.2026): Mean-Reversion-Anker. **Operative Konsequenz** — Score-Stabilität gegen Tagesnachrichten: Score-Updates an strukturelle Trigger gebunden (Earnings, FLAG-Events, Watch-Resolves), NICHT an kurzfristige Sentiment-Schwankungen. Tetlock zeigt empirisch (5-10-Tage-Reversion zu Fundamentals nach Media-Pessimism-Schock), warum kurzfristiges Sentiment Mean-reverted und kein Score-relevantes Signal sein darf. Anker für `feedback_score_stability_over_drift`-Memory (geplant Konsolidierungstag).

---

## 6. Insider-Scoring — Pflichtregeln

> **Scoring-Skala + Cashless-Exercise-Ausnahme → [SKILL.md §Insider (10 Punkte)](../01_Skills/dynastie-depot/SKILL.md)**
>
> Kurz: OpenInsider HEILIG, 10b5-1 "M"-Check bei Verkäufen >$20M, Fallback SEC EDGAR Form 4.

**Wissenschaftliche Anker (Validation + Roadmap — kein Score-Effekt):**
- **B26 Lakonishok-Lee 2001** — `active-scoring-validation` (eingeführt 26.04.2026): Primärquelle für die operative Heuristik (Buy>Sell-Asymmetrie, Aggregate-Predictability, Small-Cap-Concentration, Contrarian-Timing). Bestätigt die seit insider-intelligence-v1 operativen Filter (Form-4-X/M-Filter via OpenInsider, Buy-Side höher gewichtet, $5M-Cluster-Schwelle für Buys vs $20M-FLAG-Schwelle für Sells). **Keine Architektur-Änderung — primär-empirische Validation.**
- **B27 Ke/Huddart/Petroni 2003** — `design-context` (eingeführt 26.04.2026): **Deferred-Pipeline-Note für insider-intelligence v2.** Sell-Detection-Window aktuell 6 Monate (~2 Quartale). Q-9 bis Q-3 Pre-Earnings-Break-Sell-Zone wird strukturell verfehlt (Legal-Jeopardy + ITSFEA 1988 unterdrücken Q-2/Q-1-Sells, Insider verkaufen 9-3 Quartale früher). Pipeline-Erweiterung auf 24-Monats-Lookback wartet auf §29-Backtest-Gate-Kriterien (Score-Archiv ausreichend gefüllt + §29.7 M&P-Discount-Plausibility-Check). **Kein Live-Score-Change** bis v2-Deploy. Bridge-Befund: Insider-Trades führen Earnings-Disclosures bis zu 2 Jahre — Insider-Block ist strukturell informativer als Sentiment-EPS-Revision-Delta + Fundamentals-fcf_trend-Watches.

---

## 7. Kalibrierungsanker (vor jeder Analyse pflichtlesen!)

| Ticker | Score | DEFCON | Lektion |
|--------|-------|--------|---------|
| AVGO | 84 | 🟢 4 | Fabless-Modell = CapEx/OCF <15%, Referenz für Top-Score (post-17.04. Forward-Vollanalyse 85→84) |
| MKL | 82 | 🟢 4 | Float-Modell = FCF-Sonderregel, Versicherungs-Exception |
| SNPS | 76 | 🟡 3 | Goodwill-Malus durch Ansys-Akquisition (-3 Punkte) |
| SPGI | 74 | 🟡 3 | ROIC-Verzerrung durch M&A-Goodwill → Non-GAAP ~82 |
| TMO | 63 | 🟠 2 | ROIC < WACC + Akquisitionsschuld = harter Malus trotz Wide Moat (v3.7 post-Fix-3/OpM: D2-bestätigt, 62→63 post-17.04.) |
| EXPN | 61 | 🟡 3 | Datenlücken erzwingen konservatives Scoring |
| FICO | 67 | 🟡 3 | TTM-Verzerrung durch Kurscrash (-52%); Forward-Metriken deutlich besser (VEEV-Ersatz-Referenz) |

---

## 8. Datenquellen-Logik

> **API-Routing + Quellen-Reihenfolge → [SKILL.md §API-Routing-Regel](../01_Skills/dynastie-depot/SKILL.md) + `01_Skills/dynastie-depot/sources.md` (kanonische URLs pro Metrik)**
>
> Kurz: US → defeatbeta + Shibui + SEC EDGAR. Non-US → EODHD. Datenkonflikt: SEC > Drittanbieter.

---

## 9. !Rebalancing — Workflow

1. `config.yaml` lesen → aktuellen Portfolio-State laden
2. Drift prüfen: Weicht eine Position >10% von Zielgewichtung ab?
3. Sparplan-Vorschlag erstellen mit **formeller Berechnungsformel:**

**Tier-Modell (Umstrukturierung 2026-06-07, löst flaches Equal-Weight-Modell ab):**
`effektive Rate = satelliten_tier_raten[tier] × DEFCON-Modulation × FLAG`
**Tier-Basis (config.yaml `satelliten_tier_raten`):** Tier 1 = 40€ | Tier 2 = 32€ | Tier 3 = 18€ (Optimal-Fall D3/D4 clean)
**Modulation:** D3/D4 → ×1,0 | D2 → ×0,5 (Sockelbetrag) | D1 → 0€ | 🔴 FLAG → 0€ (heilig, überschreibt DEFCON score-unabhängig)

**Rechenbeispiel (Stand 2026-06-07, 13-Roster):**
- SOLL-Σ = Tier1 4×40 (AMZN/MSFT/NOW/AVGO) + Tier2 3×32 (V/KYCCF/ASML) + Tier3 6×18 (RMS/BRK.B/TMO/APH/SU/ZETA) = 160 + 96 + 108 = **364€** (== config.yaml brokers.scalable.sparrate_eur)
- Funded-Σ (moduliert) = NOW 40 + [ASML 32 + KYCCF 32 + V 16] + [RMS/BRK.B/TMO/SU/ZETA je 18 = 90] = **210€**; AMZN/MSFT/AVGO/APH = 0€ (FLAG)
- Differenz SOLL−Funded = 154€ → Rebalancing-Tool lenkt **freies Kapital value-based** auf untergewichtete Positionen (voller Monatsbeitrag deployed, nur Verteilung verschiebt sich)

4. **Steuer-Bremse**: Niemals durch Verkauf rebalancen → Sparplan umleiten
5. US-Cap prüfen: Bleibt US-Exposure unter 63%?

---

## 10. !QuickCheck — Workflow

Für jede Position:

| Check | Grün | Gelb | Rot |
|-------|------|------|-----|
| Earnings-Drift | Keine Überraschung | Miss <5% | Miss >10% |
| Kurs-Drift | <10% unter 200MA | 10–20% | >20% |
| Konsensus-Drift | Stabil/upgrade | Seitwärts | Downgrade |
| Moat-Drift | Wide bestätigt | Nicht geprüft | Downgrade |
| Score-Alter | <6 Monate (score_valid_until) | 4–6 Monate | >6 Monate / abgelaufen |

**Deep-Dive-Trigger (→ automatisch !Analysiere):**
- ≥1 roter Checkpunkt
- FLAG neu aktiv
- Moat-Downgrade auf Narrow/None
- `score_valid_until` überschritten (180 Tage seit score_datum)

**Moat-Drift — drei objektive Auslöser (sofortiger !Analysiere, score-unabhängig):**
1. **Morningstar-Downgrade** Wide → Narrow (Quelle: GuruFocus term/moat-score/TICKER)
2. **Marktanteilsverlust >10%** im Kernsegment — dokumentiert in Earnings Call oder Pressebericht
3. **Gross Margin Rückgang >5 Prozentpunkte** über 4 aufeinanderfolgende Quartale (Shibui + Macrotrends)

**Rhythmus:**
- `!QuickCheck ALL` → 1× monatlich (erster Montag des Monats)
- `!QuickCheck [TICKER]` → innerhalb 48h nach Earnings

---

## 11. CapEx-FCF-Analyse — 6 Excel-Sheets

Trigger: nur bei Score ≥ 80 aus Stufe 2

1. Executive Summary
2. Historische CapEx/FCF-Daten (5–10 Jahre)
3. Szenario-Analyse (Bull / Base / Bear)
4. DCF-Bewertung
5. Peer-Vergleich
6. Risiko-Dashboard

---

## 12. config-Pflege-Pflicht

> **Sync-Pflicht-Vertrag → §18 v2 (Trigger-basiertes File-Set-Mapping).**
>
> Score / DEFCON / FLAG / Sparraten-Änderungen schreiben das vollständige Score-Event-File-Set fort: `PORTFOLIO.md` + `Faktortabelle.md` + `CORE-MEMORY.md` + `log.md` + `score_history.jsonl` + **`01_Skills/dynastie-depot/config.yaml`** (+ `flag_events.jsonl` bei FLAG-Trigger/Resolve). Per-File-Inhalt + atomarer Commit: §18.1 + §18.3.
>
> Watchlist-Status (PORTFOLIO „Aktive Watches") + Termine (PORTFOLIO „Nächste kritische Trigger" / PIPELINE Long-Term-Gates) sind Teil des PORTFOLIO/PIPELINE-Sets — kein separater Pflege-Pfad.

---

## 13. Verhaltensregeln

> **Vollständige 7 Regeln → [SKILL.md §Verhaltensregeln](../01_Skills/dynastie-depot/SKILL.md)**
>
> Kurz: Quellenpflicht · Konservativ scoren · Kalibrieren (Beispiele.md) · Kein Raten · EUR/USD explizit · FLAG heilig · Steuer-Bewusstsein (26,375%, FIFO).

---

## 14. Non-US Scoring Addendum (ASML / RMS / SU)

> **IFRS-Anpassungen + API-Routing → [SKILL.md §API-Routing-Regel (Non-US)](../01_Skills/dynastie-depot/SKILL.md) + §21 unten (Kurzreferenz)**
>
> EODHD ist Datenquelle für Non-US (Euronext-Primär, EUR). IFRS-Nuancen pro Block (IFRS 16 Leasing, Goodwill, SBC) siehe §21 Kurzreferenz. Insider: AFM (ASML) / AMF (RMS, SU) manuell — kein Form 4.

---

## 15. Tariff Exposure

> **FLAG-Regeln + Quellen-Reihenfolge → [SKILL.md §FLAG Typ 4: Tariff Exposure](../01_Skills/dynastie-depot/SKILL.md)**
>
> Schwellen: <15% kein FLAG | 15–35% Notiz Risk Map | >35% FLAG aktiv.

---

## 16. Non-US API Sanity Check

> **Vollständiger Workflow (Rotationsplan, IFRS-Zeilen-Mapping, FLAG-Protokoll) → [SKILL.md §Quarterly API Sanity Check](../01_Skills/dynastie-depot/SKILL.md)**
>
> Non-US-Rhythmus: Nach jedem Earnings-Zyklus. Toleranz: ±1,5% CapEx, ~15% OCF (IFRS-16-Leasingeffekt strukturell). Tool: `python 01_Skills/non-us-fundamentals/eodhd_intel.py detail [TICKER]`.

---

## 17. Skill-Hierarchie & Aktivierungslogik (v2.1 — 25.04.2026)

**Grundregel:** `dynastie-depot` ist der Monolith. Innerhalb von `!Analysiere` werden Module (defeatbeta, Shibui, insider_intel.py, WebSearch) **als direkte Tool-Calls** genutzt — kein manuelles Skill-Chaining. Jeder Ad-hoc-Skill-Load kostet Token und verliert DEFCON-Kontext.

**Eine dokumentierte Ausnahme:** `backtest-ready-forward-verify` wird in dynastie-depot **Schritt 7** programmatisch invoked (`Skill(skill="backtest-ready-forward-verify", args="<draft-pfad>")`) zum Schreiben von `score_history.jsonl`. Pipeline-Kapsel (Freshness / Tripwire / §28.2 Δ-Gate / Dry-Run / Append / git add) ist im Skill gekapselt — kein Inline-CLI in dynastie-depot. Trigger seit v3.7.2 (19.04.2026), kanonisch dokumentiert in SKILL.md Schritt 7 + SYSTEM.md.

### Wann wird welcher Skill eigenständig aktiviert?

| Befehl / Trigger | Skill | Aktivierungs-Modus |
|---|---|---|
| `!QuickCheck [TICKER\|ALL]` | `quick-screener` | Manuell (User-Trigger) |
| `!EarningsPreview [TICKER]` | `earnings-preview` | Manuell (48h vor Earnings) |
| `!EarningsRecap [TICKER]` | `earnings-recap` | Manuell (48h nach Earnings) |
| `!EarningsCalendar` | `earnings-calendar` | Manuell (wöchentlicher Überblick) |
| `!InsiderScan` | `insider-intelligence` | Manuell (Standalone-Scan ohne !Analysiere) |
| `!Analysiere` Schritt 7 | **`backtest-ready-forward-verify`** | **⚙️ Programmatisch** (aus dynastie-depot SKILL.md Schritt 7, jsonl-Write-Pflicht) |
| `!SessionClose` | `session-closure` | Manuell (Session-Ende, Strict-Trigger; siehe §25.5) |
| `!ParaSync18 <event-type> [--also …]` | `paragraph-18-sync` | Manuell oder file-pattern-Auto-Trigger via CLAUDE.md Routing-Table (siehe §18.0) |
| `!SlimRefactor <config>` | `core-slim-refactor` | Manuell (YAML-driven 8-Phase Markdown-Section-Refactor — Pattern A/B/C; siehe SYSTEM.md Skill-Registry) |
| §18.7 Post-openpyxl-Write (file-pattern, kein `!`-Trigger) | `xlsx-smoke-test-runner` | Library-Mode (`from verify_wrapper import verify_after_write`) — vor `git add` xlsx |
| Portfolio-Risk-Audit | `03_Tools/portfolio_risk.py` | Quartalsweise manuell (Python-Tool, kein Skill) |
| Dokument-Konflikt / 10-K-Text | `sec-edgar-skill` | Eskalations-Fallback (manuell) |

### Warum kein manuelles Skill-Chaining innerhalb !Analysiere?

Ein Ad-hoc-Skill-Load liest die jeweilige SKILL.md ohne Kenntnis von:
- DEFCON-Scoring-Skalen und Kalibrierungsankern
- FLAG-Logik und deren Überschreibungsregeln
- `01_Skills/dynastie-depot/config.yaml` (aktuelle Positionen, DEFCON-Status)
- Kontext der laufenden Analyse (welcher Ticker, welche Daten schon geladen)

→ Ergebnis wäre generische Analyse statt kontextbewusster DEFCON-Score.
→ `backtest-ready-forward-verify` Step-7-Invocation ist davon ausgenommen, weil sie **keinen Scoring-Kontext braucht** — sie schreibt lediglich den fertigen `ScoreRecord` deterministisch ins Archiv.
→ Pipeline-Stufen, Skill-Architektur-Tabelle: `01_Skills/dynastie-depot/PIPELINE.md` (skill-internes Pipeline-Doc).

### 17.1 Memory-Guard-Rail — Routing- und Live-State-Vorrang (PF-1 Option C)

> Kanonische Voll-Spec; CLAUDE.md führt nur die kompakte normative Routing-Zeile + Pointer hierher. Empirisch fundiert (QuickCheck-VRT 2026-05-16: claude-mem capturt korrekte Reasoning-Trajektorie, aber append-only ohne Single-Fact-Verdikt — Interim-Memory-Fragment darf nicht als kanonisches Verdikt missverstanden werden).

1. Bei jeder Anfrage, die Routing-Auswahl, Trigger-Auswahl, §-Ausführung oder Prioritätsauflösung erfordert, ist die Route ausschließlich aus folgenden route-determining Inputs zu bestimmen: (a) Routing-Table in `CLAUDE.md`, (b) explizite User-Nachricht, (c) Live-Dateien mit absolutem Vorrang: `PORTFOLIO.md`, `STATE.md`, `INSTRUKTIONEN.md`. `autoMemory`, `claude-mem`, folder-memory und `context-mode-search` sind keine route-determining Inputs.

2. Recalled `autoMemory`, `claude-mem` Observation-Summary, folder-memory-Blöcke und `context-mode-search`-Treffer dürfen keine Route wählen, unterdrücken, umpriorisieren, erweitern oder in ihrer Reihenfolge verändern.

3. Memory darf erst nach abgeschlossenem Route-Match aus den autoritativen Quellen gemäß Punkt 1 konsultiert werden.

4. Memory ist strikt advisory. Es darf niemals Live-Dateien oder Live-Zustände überschreiben, relativieren oder faktisch verdrängen, insbesondere nicht `SYSTEM.md`, `log.md`, `score_history.jsonl`, den §18-Sync-State, Score-Werte, FLAG-Werte oder Trigger-Bedingungen.

5. Bei Konflikt zwischen Memory und Live-Dateien oder Routing-Regeln ist Memory zu ignorieren. Maßgeblich sind die Live-Dateien. Der Konflikt ist in `log.md` unter `mem-conflict` zu protokollieren.

6. **Referenz-Korpus-Index-Korollar (ADR-0001, PIPELINE #82, NEU 2026-06-07):** Live-State (Scores, Faktortabelle, DEFCON-Status, FLAGs) wird **niemals** in einen `ctx_index`/`ctx_search`-Referenz-Korpus aufgenommen — egal in welcher Datei, auch nicht Vault-Score-Seiten. Schutz durch **Exklusion, nicht durch Frische** (kein Re-Index-Modell ist echtzeitig; ein Snippet im Sync-Fenster könnte einen veralteten Score liefern). `ctx_search`-Treffer sind wie Memory strikt advisory (Punkt 4) und nie Override gegen Live-Dateien. Betriebsregel: `TOKEN-RULES.md §Referenz-Korpus-Index`; Tiefenbegründung: `docs/adr/0001-no-live-state-in-reference-index.md`.

---

## 18. Sync-Pflicht — Trigger-basiertes File-Set-Mapping (v2.4, 2026-05-11)

Pflicht-Listen pro **Event-Typ** statt pauschaler 6er-Liste. Kern-Invariante: Score/FLAG/Sparraten-Change = 8 Pflicht-Files (5 manuell + `score_history.jsonl` via Skill + 2 xlsx-Tools) + 1 conditional (`flag_events.jsonl` bei FLAG-Trigger/Resolve). Mehraufwand vs. v2.1: +2 xlsx-Tools (`Rebalancing_Tool_v3.4.xlsx` + `Satelliten_Monitor_v2.0.xlsx`) — User-Direktive 28.04.2026 spätabends: xlsx-Tools sind operative Live-State-Quelle für Sparplan-Werte und Depot-Übersicht (Zero-Token-Lookup-Pflicht). Seit v2.4 (11.05.2026): jeder xlsx-Sync löst verpflichtenden Post-Write-Smoke-Test §18.7 aus (fail-close vor `git add`).

### §18.0 Auto-Invoke-Disziplin `paragraph-18-sync` (NEU 2026-05-23 spätabends, v2.5 → v2.5.1 2026-05-24)

**Normativ verbindlich:** Sobald ein Working-Tree-Diff (Pre-Edit oder Pre-Commit) **EINES** der folgenden Files berührt, MUSS der Skill `paragraph-18-sync` via `!ParaSync18 <event-type> [--also …]` aufgerufen werden — vor `git commit`, kein Edit-only-Pfad, kein silent Sync via Hand-Edit.

**Trigger-File-Set:**
- `00_Core/PIPELINE.md` · `PORTFOLIO.md` · `CORE-MEMORY.md` · `Faktortabelle.md` · `SYSTEM.md` · `STATE.md` (Critical-Alert-Slot)
- `07_Obsidian Vault/**/log.md`
- `05_Archiv/score_history.jsonl` · `flag_events.jsonl`
- `01_Skills/dynastie-depot/config.yaml`
- `01_Skills/*/SKILL.md` (jede Version-Edit = system-zustand-Event)
- `03_Tools/Rebalancing_Tool_v*.xlsx` · `Satelliten_Monitor_v*.xlsx` · `Watchlist_Ersatzbank_Monitor_v*.xlsx`

**Event-Type-Inferenz aus Datei-Pattern:**
- Score/FLAG/Sparraten-spezifische Files (PORTFOLIO/Faktortabelle/score_history/flag_events/config.yaml/2 xlsx) → `score-flag-sparraten`
- PIPELINE.md-Edit → `pipeline-item`
- SYSTEM.md-Edit oder SKILL.md-Version-Bump → `system-zustand` (+`--version-bump` falls CORE-MEMORY §6 betroffen)
- STATE.md-Alert-Slot → `critical-alert`
- Multi-Event-Aktion → Multi-Event-Union via `--also` (§18.2)

**Defense-in-Depth (3 Layer — empirische Stärke-Ordnung seit v2.5.1):**
1. **L3 = primary safeguard:** Pre-Commit-Hook `paragraph-18-sync-reminder` (`.pre-commit-config.yaml`, `verbose: true` seit 2026-05-24) — advisory WARN bei staged §18-Files; Bypass nur via ENV `PARA18_VERIFIED=1` nach manuellem `!ParaSync18`-Validator-Pass. **Wirkt deterministisch** (file-pattern-Match → stderr), unabhängig von Modell-Disziplin.
2. **L2 = backup:** Tier-3 INSTRUKTIONEN §18.0 (dieser Eintrag) + CLAUDE.md Routing-Table-Row "§18-File-Touch (auto)" — normative SSoT, aber empirisch nicht selbst-tragend bei n=2.
3. **L1 = backup:** Tier-1 Memory `feedback_paragraph18_skill_auto_invoke_on_sync_files.md` — Session-übergreifender advisory Prior, ebenfalls empirisch nicht selbst-tragend bei n=2.

**Lapsus-Empirie (n=2 Reinfälle, dokumentiert):**
- **Skip #1:** core-slim-refactor v0.1.1 Build-Session 2026-05-23 abends-spät — Edit-only-Pfad statt `!ParaSync18`-Vorlauf. User-Direktive 23:48 GMT+2: "Skill ja umsonst gebaut sonst". v2.5-Bump = Königsweg-Verankerung.
- **Skip #2:** 97d582a Pre-Flight-Session 2026-05-24 ~00:08 GMT+2 — beim ersten log.md-Touch (P5/P6) wurde `!ParaSync18` NICHT autonom emittiert; Sync-Reflex blieb intern. Befund 97d582a-Commit-Message wörtlich: "Memory + INSTRUKTIONEN §18.0 unter regulären Bedingungen NICHT stark genug für Autonom-Emission ohne expliziten Prompt-Anker".
- **L3-Silent-Befund 24.05.:** Hook lief, war aber unsichtbar — pre-commit-Framework unterdrückt stderr von passing Hooks (exit 0) per Default. Triangulation T1 (Hook direkt = Output), T2 (Framework default = `Passed` only), T3 (`--verbose` = Output sichtbar). Fix: `verbose: true` im YAML-Block (persistent, scoped).
- **v2.5.1-Bump = L3-Promotion zu primary safeguard** + n=2-Empirie + Pre-Edit-Reflex-Verschärfung (siehe L1 Memory: user-facing `!ParaSync18 ... --dry-run` als ERSTER output bei §18-File-Edit-Intention, nicht intern).

**Routing-Table Spiegel (CLAUDE.md):** Eigene Row "§18-File-Touch (auto, file-pattern-driven)" zusätzlich zur expliziten `!ParaSync18`-Row — file-pattern-Match triggert IDENTISCHEN Skill-Call.

### 18.1 Event-Typ-Mapping

| Event-Typ | Pflicht-Files |
|---|---|
| **Score / FLAG / Sparraten-Change** | `log.md` + `CORE-MEMORY.md` + `Faktortabelle.md` + **`PORTFOLIO.md`** + `score_history.jsonl` + **`01_Skills/dynastie-depot/config.yaml`** + **`03_Tools/Rebalancing_Tool_v3.4.xlsx`** + **`03_Tools/Satelliten_Monitor_v2.0.xlsx`** (+ `flag_events.jsonl` bei FLAG-Trigger/Resolve) |
| **Pipeline-Item** (neuer Plan, Gate-Passage, Status-Transition, Done/Deferred) | **`PIPELINE.md`** + `log.md` (+ `SESSION-HANDOVER.md` Pflicht bei Session-Abschluss; mid-Session optional) |
| **System-Zustand-Change** (DEFCON-Version, MCP-Change, Briefing-Status, neuer Backlog-Eintrag, Infra-Deploy) | **`SYSTEM.md`** + `log.md` (+ `CORE-MEMORY.md §6` bei Versionsprung) |
| **Critical-Alert-Slot** (Hub) | `STATE.md` Hub-Edit (nur Alert-Slot); kein Bi-Sync erzwungen |

**Kanonische Schreibwege:**
- `score_history.jsonl` (05_Archiv/) — append-only via Skill `backtest-ready-forward-verify` (v1.0.1, dynastie-depot v3.7.3 Schritt 7; orchestriert Pipeline-Kapsel: Freshness / Tripwire / §28.2 Δ-Gate / Dry-Run / Append / git add).
- `flag_events.jsonl` (05_Archiv/) — append-only via `archive_flag.py` (nur bei FLAG-Trigger oder Resolution). SKILL.md Schritt 6b.
- `Faktortabelle.md` — Score + FLAG-Spalte (manuell, im selben Sync-Commit).
- `01_Skills/dynastie-depot/config.yaml` — TMO/Ticker-Block (`score`, `defcon`, `score_datum`, `score_valid_until`, `flag_hinweis`, `sparrate_hinweis`, `scoring_notiz`, `naechste_pruefung`, `earnings_trigger`, `substitute_activation_rule`) manuell sync. **Bei reinem Score-Change OHNE FLAG-Trigger ebenfalls Pflicht** — Lücke 25.04. nach 7-Tage-Drift TMO 23.04. (post-Q1) entdeckt.
- `03_Tools/Rebalancing_Tool_v3.4.xlsx` — formel-basiert, Pflicht-Felder pro Ticker: Spalte N (`DEFCON Score`, z.B. `'DEFCON 2 (64)'`) + Spalte O (`FLAG-Status`-Text mit Datum/Pfad-Note). Sparraten-Berechnung läuft formel-basiert über DEFCON-Spalte (parsed `LEFT(N18,8)="DEFCON X"`), Output passt sich automatisch an wenn N/O korrekt. Sync via `openpyxl` (siehe Memory `feedback_xlsx_tools_in_sync_set.md` für Edit-Pattern).
- `03_Tools/Satelliten_Monitor_v2.0.xlsx` — display-orientiert (statische Strings). Pflicht-Felder bei Score/FLAG/Sparraten-Change: (a) R2 Stand-Stempel (Spalte O), (b) R3 Header-Sparraten-Zeile (Spalte B: D3/D4-Rate, D2-Sockelbetrag, Nenner mit Pfad-Note), (c) Ticker-Zeile (Spalte L Score-String, Spalte M Δ-Note, Spalte N Status/FLAG-Text), (d) R3 H Eingefroren-Liste, (e) R3 K Ergebnis-Liste, (f) R24/R25 Footer (Eingefroren-Liste + Volle-Rate-Liste mit Σ-Check). Sync via `openpyxl`.

### 18.2 Multi-Event-Union-Regel (bindender §18-Vertrags-Teil)

**Regel:** Wenn eine Aktion **mehrere** Event-Typen berührt (z.B. Score-Change, der gleichzeitig einen Pipeline-Item-Status vorrückt ODER einen System-Zustand-Eintrag erzeugt), werden **alle zugehörigen File-Sets aktualisiert (Union, keine Auswahl)**.

**Rationale:** verhindert, dass `backtest-ready-forward-verify` einen Score-Append PASS ablegt, während PIPELINE.md oder SYSTEM.md stale bleiben. Der Skill sieht Fan-Out nicht — Responsibility liegt beim Analysten (analog §27.4 Drift-Check).

**Beispiel:** TMO Q1 23.04.-Vollanalyse = Score-Event + Pipeline-Item-Gate-Passage (Resolve-Gate CLEAR) → beide Sets (Score-File-Set + PIPELINE.md) aktualisiert.

**Präzedenzfall:** Memory `feedback_exhaustive_drift_check.md` (21.04.2026 — 12/27 silent defcon-Drift).

### 18.3 Commit-Granularität

Alle zum Event-Set gehörenden Files in **einem** Commit bündeln (atomar). Pipeline-Items können separat committet werden, wenn der Score-Event-Commit schon draußen ist.

**Wissenschaftlicher Anker:** Point-in-Time-Persistenz aller Pflicht-Files schützt vor §29.5 Sin #2 (Look-Ahead Bias). Jeder Record muss zum Zeitpunkt der Daten-Sichtung geschrieben werden, nicht rückwirkend. → §29.5 / [[Seven-Sins-Backtesting]]

### 18.4 Stand-Footer-Konvention (seit 2026-04-26)

Alle 8 `00_Core/`-Files (`PORTFOLIO`, `STATE`, `CORE-MEMORY`, `Faktortabelle`, `PIPELINE`, `SYSTEM`, `INSTRUKTIONEN`, `KONTEXT`) tragen `**Stand:** DD.MM.YYYY` ausschließlich im **Footer-Versions-Banner** am Datei-Ende, nicht im Header. Beim Stand-Update wird nur die letzte Footer-Zeile editiert — Header und Body bleiben unberührt. Vorteil: Konsistenz beim File-Touch (Stand-Pflege ist mechanisch, nicht inhaltlich) + within-Session KV-Cache-Stabilität bei Re-Reads nach Stand-Edit.

### 18.5 Provenance-Gate für Score-Appends (seit 2026-04-28, v3.7.4)

Score-Append läuft via `backtest-ready-forward-verify` Skill, das nun Phase P3.5 (Provenance-Gate, fail-close) zwischen P2b und P3 ausführt. Bei `FAIL phase=P3.5` gibt es keinen `--force`-Bypass — Recovery durch Workflow-Korrektur (Pflicht-Touch-Files berühren / `analyse_typ` umklassifizieren / `quellen`-Felder mit echten Quellen oder legitimen `*_carryover`-Suffixen befüllen / Versions-Drift via Migration-Pipeline lösen). Carryover-Token-Whitelist in `03_Tools/backtest-ready/provenance_gate.py::CARRYOVER_SOURCE_TOKENS` + `CARRYOVER_SOURCE_PREFIXES` + `CARRYOVER_REASON_TERMINAL`.

### 18.6 Log-Rollover-Convention (seit 2026-05-10)

Vault `log.md` wird **quartalsweise** in `archive/log/log-YYYY-Qn.md` ausgelagert (Roll-over-Termine: 1. April / 1. Juli / 1. Oktober / 1. Januar). Initial-Cut 2026-05-10: alles ≤ 2026-04-30 → `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/archive/log/log-bis-2026-04.md`. Aktiver `log.md` startet ab Mai 2026 (~1270 Z.).

**Roll-over-Mechanik:**
- Cut-Boundary: erster Eintrag des neuen Quartals = neue erste Zeile in `log.md`. Alle vorherigen Einträge → neues archive-File mit Header `# Wiki Log — Archiv bis YYYY-MM-DD` + Read-only-Hinweis + Pointer auf `../../log.md`.
- Aktiver Log behält den Original-Header (`# Wiki Log` + Append-only-Hinweis), zusätzlich Pointer auf zuletzt erstelltes Archiv-File.
- Roll-over selbst wird als letzter Eintrag (`## [YYYY-MM-DD] system-event | log.md Quartals-Rollover`) im aktiven `log.md` protokolliert.

**Sync-Set bei Roll-over** (System-Zustand-Change-Event-Typ §18.1, scoring-neutral): `log.md` (gekürzt + Roll-over-Notiz) + neues `archive/log/log-YYYY-Qn.md` + `INSTRUKTIONEN.md §18.6` (Datum-Update) + `CORE-MEMORY.md §13` (Lifecycle-Eintrag) + `SYSTEM.md §System-Zustand` (Bullet-Update). Optional WIKI-SCHEMA.md Z.23 + SESSION-HANDOVER.md History-Block falls deren Wortlaut noch alte Singular-Form verwendet.

**Rationale:** Log-Datei wuchs auf 2830 Z. (10.05.2026); tägliche Reads in §18-Sync-Welle + tail-Inspektionen wurden teuer. Quartalsweise (statt monatlich) hält Archive-Fragmentierung bei 4 Files/Jahr und liefert je ~700-1500 Z. pro Archiv-Datei. Externe Vault-Wikilinks zu `log.md` sind Null (Gemini Cross-Sync-Audit 2026-05-10, 96% PROCEED) — Risk frei. CORE-MEMORY §13 bleibt kondensierte Lifecycle-SSoT, log.md ist die volle Erzählung.

### 18.7 xlsx Post-Write Smoke-Test Stufe 1 (seit 2026-05-11, v2.4)

Verpflichtender Post-Write-Validation-Step für die xlsx-Sync-Welle. Adressiert silent-Korruptions-Risiken durch `openpyxl`-Writes auf Formel-/Conditional-Format-tragenden xlsx-Dateien (Rebalancing v3.4: 249 Formeln + 6 CF; Satelliten-Monitor v2.0: 13 Formeln + 5 CF + §G Σ-Check via Hook auf `brokers.scalable.sparrate_eur`-Anker — Live-State 2026-05-25 post User-Update + Variante-G-Entscheidung, vorher 218/6 bzw 12/5 + Excel-Σ-Plan).

**Reihenfolge:** Smoke-Test läuft **nach** Provenance-Gate §18.5 (P3.5 PASS), **nach** `openpyxl`-Write der Pflicht-Zellen, **vor** `git add` der xlsx-Files. Damit greift §18.3-Commit-Atomarität wie geplant — Smoke-Test ist Pre-Stage-Gate, nicht Post-Commit-Audit.

**Scope:** verpflichtender Smoke-Test (Punkte A-F gemäß Checklist) auf `03_Tools/Rebalancing_Tool_v3.4.xlsx` + `03_Tools/Satelliten_Monitor_v2.0.xlsx`. Minimal-Check-Annex (nur Punkt A + Existenz) auf `03_Tools/Watchlist_Ersatzbank_Monitor_v1.1.xlsx` — Hochstufung erst nach Watchlist-Tool-Update.

**Failure-Mode (fail-close, analog §18.5-Pattern):** Bei jedem Fail-Signal (Repair-Prompt, Formel-Fehler `#REF!`/`#NAME?`/`#VALUE!`/`#N/A`-Treffer, Pflicht-Zell-Stale, Conditional-Format-Bruch, ungewollter Save-Prompt) → STOP, kein `git add`, Recovery durch Re-Edit des openpyxl-Write-Scripts. **Kein `--force`-Bypass**. Recovery-Pfade: Pflicht-Zell-Adresse korrigieren / Sheet-Name verifizieren / Toleranz-Ausnahme für `=NA()`-Zellen prüfen / Conditional-Format-Re-Apply via Backup-Restore wenn nötig.

**Checklist-SSoT:** `03_Tools/xlsx-smoke-test.md` — enthält 6-Punkte-Manual-Checklist + Excel-Desktop-Fallback (Linux/Remote ohne Excel-Installation) + partielle-Fallback-Validitäts-Klausel + Stufe-2-Roadmap (Programmatic-Audit-Modul, DEFERRED — Detail dort §Stufe-2-Roadmap).

**Cross-Reference Memory `feedback_xlsx_tools_in_sync_set.md`:** Edit-Pattern-Helper (nicht-normativ, Konvenienz für openpyxl-Code-Snippets der Pflicht-Zell-Writes). Pflicht-Zell-Liste normativ ausschließlich in §18.1 (Sync-Vertrag) und §18.7 / `xlsx-smoke-test.md` (Verify-Pflicht). Bei Drift gewinnt §18-Spec über Memory.

**Wissenschaftlicher Anker:** Post-Write-Validation entspricht §29.5-Sin-#3 (Data-Snooping-Schutz via Point-in-Time-Integrität): xlsx-Drift in Sparplan-/Score-Lookup-Zellen würde operativ unsichtbare Look-Ahead-Inkonsistenz erzeugen (User-Entscheidung auf veralteten/gebrochenen xlsx-Zahlen). Fail-close ist konservativer als optional-Check.

**Änderungsprotokoll:**
- v1.5 → v1.6 (2026-04-17): Erweitert auf 6 Dateien durch Backtest-Ready Infrastructure (§26).
- v1.6 → v1.7 (2026-04-19): Schritt 5 (score_history.jsonl) wird via Skill `backtest-ready-forward-verify` orchestriert — Pipeline-Kapsel statt Inline-CLI-Call in dynastie-depot Schritt 7.
- v1.7 → v1.8 (2026-04-21): Zusatz-Trigger für STATE.md Pipeline-SSoT-Section ergänzt (Plan-Commit / Gate-Passage / Status-Transition). Kein Impact auf die 6-File-Liste selbst.
- v1.8 → v2.0 (2026-04-24): 00_Core Hub-Split — pauschale 6er-Liste → Trigger-basiertes Event-Mapping (§18.1) + Multi-Event-Union-Regel (§18.2). STATE.md = Hub (Critical-Alert-Slot), Live-State migriert in PORTFOLIO.md. Pipeline-Items in PIPELINE.md, System-Items in SYSTEM.md.
- v2.0 → v2.1 (2026-04-25): `config.yaml` aus „Bei FLAG-Change manuell sync"-Sub-Note in das Score-Event-File-Set hochgezogen — Lücke aufgedeckt durch TMO 23.04.-Drift (Score 64→67, kein FLAG-Trigger ⇒ alte Klausel griff nicht ⇒ config.yaml stale für 7 Tage bis 25.04.-Finalize-Commit `bb9986e`). Kein Set-Wachstum bei FLAG-Events (config.yaml ohnehin schon im Set), aber +1 manueller File bei reinen Score/Sparraten-Changes.
- v2.1 → v2.2 (2026-04-28): §18.5 Provenance-Gate-Klausel ergänzt (Pipeline-Phase P3.5 fail-close, kein `--force`-Bypass). Schicht B `provenance_gate.py` + Schicht D `_check_vollanalyse_block_coverage` + SSoT `versions.py::DEFCON_ACTIVE_VERSION` deployed.
- v2.2 → v2.3 (2026-04-28 spätabends): xlsx-Tools `Rebalancing_Tool_v3.4.xlsx` + `Satelliten_Monitor_v2.0.xlsx` ins Score/FLAG/Sparraten-Pflicht-Set hochgezogen. Anlass User-Direktive: xlsx-Tools sind operative Live-State-Quelle für Sparplan-Werte + Depot-Übersicht (Zero-Token-Lookup). Drift seit 23.04. (Satelliten-Monitor R3-Header + R24/R25 Footer noch auf 23.04.-Stand) bei V Rescoring-Revert (`b8cf4ae`/`1069e8d` 28.04. spätabends) durch User-Korrektur aufgedeckt. Mehraufwand: 2 xlsx-Edits pro Score-Event via `openpyxl` (Edit-Pattern siehe Memory `feedback_xlsx_tools_in_sync_set.md`).
- v2.3 → v2.4 (2026-05-11): §18.7 xlsx Post-Write Smoke-Test Stufe 1 verpflichtend eingeführt (fail-close, kein `--force`-Bypass, analog §18.5-Provenance-Gate-Pattern). Anlass: openpyxl-Writes können silent Cross-Sheet-Formeln / Conditional Formats brechen — aktuell kein Post-Write-Validation-Step. 6-Punkte-Manual-Checklist in `03_Tools/xlsx-smoke-test.md` (Repair-Prompt-Detect, Formel-Fehler-Scan, Pflicht-Zell-Cross-Check Rebalancing + Satelliten-Monitor, Conditional-Format-Stichprobe, Read-only-Close-Verify) + Excel-Desktop-Fallback für Linux/Remote + partielle-Fallback-Validitäts-Klausel + Stufe-2-Roadmap (DEFERRED `system_audit/checks/xlsx_integrity.py`). Watchlist v1.1 als Minimal-Check-Annex (Punkt A + Existenz, 0 Formeln/0 CF). Validiert via Gemini Cross-Sync-Audit + Codex-Round-2-Sparring (96% Konfidenz, >95%-Gate APPROVE).

---

## 19. Daten-Update-Klassen (wissenschaftlich fundiert)

| Klasse | Trigger | Frequenz | Felder | Halbwertszeit |
|--------|---------|----------|--------|---------------|
| **A** | Quartalsweise | ~90 Tage | FCF, ROIC, GM, Debt/EBITDA | 18–33 Monate |
| **B** | Earnings-getriggert | 14 Tage nach Earnings | Alle Fundamentals, Score, Guidance | 60% Verfall Monat 1 |
| **C** | Event-getriggert | Sofort | Insider >$20M, Moat-Downgrade, Makro >50 Bps | — |
| **D** | Monatlich | 1×/Monat | Sentiment, Short Interest | — |

Basis: SSRN 2022. 80% DEFCON-Score >12 Monate Halbwertszeit.

### 19.1 Earnings-Call-Wait-Discipline (NEU 2026-04-28 spätabends, post V Q2 Reinfall)

**Regel:** Klasse-B-Vollanalyse läuft strikt **Tag +1 morgens nach Earnings Call**, nicht am Press-Release-Tag selbst. Tag 0 ist FLAG-Quick-Check + Press-Release-Pre-Brief only — kein Score-Move, kein D-Stufen-Wechsel, kein Sparraten-Kaskaden-Sync.

**Ausnahme — Issuer ohne Quarterly Earnings Call:** **BRK.B** hält keinen Q-Call ab. Trigger = 10-Q-/10-K-Filing auf SEC EDGAR; Tag 0 = Filing-Tag = Vollanalyse direkt möglich (kein Wait-State, kein earnings-recap-Skill, defeatbeta-Transcript-Leer-Return ist erwartet). Annual Letter (Feb/März) + Annual Meeting (Mai) sind separate Pflicht-Trigger unabhängig vom Quartals-Zyklus.

**Tag-0-Workflow (Press-Release-Tag, ~15-30 Min):**

| Schritt | Tool | Output |
|---|---|---|
| 1. Press-Release-Recap | Skill `_extern/earnings-recap` (yfinance-basiert) | Beat/Miss-Headlines (EPS estimate vs actual, surprise %) + 4-Quartals-Trend-Tabelle (Revenue/Margins/EPS) + Stock-Price-Reaction |
| 2. FLAG-Quick-Check | manuell + Press-Release-PDF | CapEx/OCF, FCF-Trend, Insider-Selling-Disclosures, Tariff-Exposure-Updates. Bei FLAG-Trigger: `archive_flag.py trigger` sofort (Sparplan-Konsequenz zeitkritisch). Bei FLAG-Resolution: `archive_flag.py resolve`. Kein Score-Move trotzdem. |
| 3. Headline-Notiz | manuell | CORE-MEMORY §12.<ticker> Pre-Call-Snapshot-Eintrag (1-2 Sätze: Beat/Miss-Magnitude, Guidance grob, ggf. FLAG-Trigger) |

**Tag-+1-Workflow (Folgetag morgens, ~30-45 Min):**

Standard `dynastie-depot` Vollanalyse (Schritte 0-7) — mit folgenden Pflicht-Quellen, die am Tag 0 noch nicht verfügbar waren:
- **Earnings Call Transcript** via `mcp__defeatbeta-api__get_stock_earning_call_transcript` (US) oder Quartr (Non-US) — Pricing-Power-Confirmation-Suche (Suchbegriffe „pricing", „price increase", „raised prices") → Moat +1 Bonus möglich
- **Forward-Guidance-Detail** aus Call-Q&A (oft präziser als Press-Release)
- **Zacks-EPS-Revisions-Refresh** (12-72h post-Call typisch verfügbar)
- **Management-Tone / Q&A-Insights** in Risk-Map

**Schritt 7 (ScoreRecord-Append) und §18-Sync laufen ausschließlich am Tag +1**, nicht am Tag 0. Damit ist 8-File-Sync atomar und eindeutig auf einen Workflow-Tag zugeordnet.

**Cross-Reference Backfill-Eligibility (NEU 09.05.2026 post-AVGO §32 Closure):** Skip-Window-Carryover (SKILL.md Schritt 0, Bullet 4) ist nur zulässig, wenn der unmittelbar vorhergehende Score-Record `analyse_typ="vollanalyse"` war und vollständige Coverage gemäß Schritt 6c / Schritt 7 aufwies (vollständige `scores` + vollständige `metriken_roh`). Bei `analyse_typ="backfill"` oder bei `analyse_typ="rescoring"` mit unvollständiger Coverage gilt trotz `<14d` Live-Pull-Pflicht. Präzedenz: AVGO 30.04.2026, Codex-R1 HIGH-3 + R2 APPROVE Master-Reading.

**Outlier-Caveat:** Wenn Press-Release-Day einen FLAG-Trigger erzeugt (Insider >$20M, CapEx/OCF >60%, FCF-Trend-neg etc.), erfolgt der FLAG-Event-Append (`archive_flag.py trigger`) am Tag 0 sofort — **ohne** Score-Move. Score-/D-Stufen-Anpassung kommt am Tag +1 mit der vollen Vollanalyse. Diese Trennung ist sauber, weil `flag_events.jsonl` und `score_history.jsonl` orthogonale SSoTs sind.

**Sync-Set-Trennung Tag 0 vs Tag +1:**
- **Tag 0 Sync-Set (FLAG-Trigger-Fall):** `flag_events.jsonl` + `log.md` + ggf. `PORTFOLIO.md` (FLAG-Spalte + Sparrate auf 0€) + `Faktortabelle.md` (FLAG-Spalte) + `config.yaml` (FLAG-Sub-Block). Score bleibt unverändert.
- **Tag 0 Sync-Set (kein FLAG-Trigger):** `log.md` (Pre-Call-Snapshot-Notiz) + ggf. `CORE-MEMORY.md §12.<ticker>` (Headline-Notiz). Sonst nichts.
- **Tag +1 Sync-Set (Score-Event):** Volle 8-File-Pflicht-Liste gemäß §18.1 v2.3 + ggf. `flag_events.jsonl` (Resolve, falls FLAG am Tag 0 noch aktiv war).

**Begründung (V Q2 28.04. Reinfall als Präzedenz):** Mittags-Vollanalyse vor Call führte zu drei Methodology-Drifts (HIGH-1 ROIC SKILL-Wortlaut, HIGH-2 Carryover-Proxy-Kurs, MEDIUM-2 Insider carryover-rounding). Hauptursache war **Reviewer-Disziplin-Lücke unter Zeitdruck** („heute Abend noch fertig"-Mentalität), nicht fehlende Daten. Tag-+1-Slot bietet:
- Schritt 6c Pre-Flight ohne Zeitdruck
- Codex-Review **vor** Sync-Commit (statt danach mit Revert-Aufwand)
- Transcript-Daten verfügbar → Pricing-Power-Bonus erfassbar
- Zacks-EPS-Revisions teilweise refreshed

Token-Aufwand-Vergleich V-Reinfall: ~100-130k für Mittags-Lauf + Codex-Review + Revert + Spec-Erweiterung. Mit Wait-Discipline: ~40-60k für sauberen Single-Pass-Lauf am Tag +1. Token-Save **~50-70%** + keine operativen Drift-Risiken.

**Wissenschaftlicher Anker:** Bricolage-Avoidance + Look-Ahead-Bias-Vermeidung (§29.5 Sin #2). Press-Release-only-Vollanalyse läuft auf unvollständiger Datenbasis (Pricing-Power-Bonus systematisch ausgeschlossen → konservativer Moat-Score-Bias).

---

## 20. Ersatzbank-Aktivierungsprotokoll

| Phase | Trigger | Aktion |
|-------|---------|--------|
| Vorbereiten | DEFCON 2 (Score <65) | Ersatz identifizieren + analysieren |
| Ausführen | DEFCON 1 (<50) ODER Veto | Sparplan umleiten |
| Bedingung | — | Ersatz Score ≥80 + kein FLAG |
| Fallback | Kein geeigneter Ersatz | ETF-Budget erhöhen |

---

## 21. Non-US Scoring Kurzreferenz

ASML/RMS/SU — IFRS-Besonderheiten:
- **IFRS 16 Leasing:** ROU-Asset-Zugänge nicht als CapEx zählen — nur Cash-CapEx
- **RMS:** "Adjusted FCF" ≠ Shibui free_cash_flow — TTM-Backrechnung aus info.freeCashflow
- **SU:** "Net cash from operations" (nach Steuern!) — IFRS-16 ROU-Zugänge nicht mitzählen
- **Insider:** AFM (ASML) / AMF (RMS, SU) — manuell, kein Form 4
- **Toleranz:** ±1,5% CapEx, bis ~15% OCF (IFRS 16-Effekt)

---

## 22. Sparplan-Formel (3-Tier, aktuell 2026-06-07 — Umstrukturierung Phase A)

**Formel:** `effektive Rate = satelliten_tier_raten[tier] × DEFCON-Modulation × FLAG`
**Tier-Basis:** T1 40€ | T2 32€ | T3 18€ (Optimal D3/D4 clean) | **Modulation:** D3/D4 ×1,0 · D2 ×0,5 · D1 0 · 🔴 FLAG 0 (heilig)

| Position | Tier | Score | DEFCON | Modulation | Rate |
|----------|------|-------|--------|-----------|------|
| NOW | T1 | — (O3) | 🟡 3\* | ×1,0 | 40€ |
| AVGO | T1 | 56 | 🟠 2 | 🔴 FLAG | 0€ |
| MSFT | T1 | 50 | 🟠 2 | 🔴 FLAG | 0€ |
| AMZN | T1 | 42 | 🔴 1 | 🔴 FLAG/D1 | 0€ |
| ASML | T2 | 68 | 🟡 3 | ×1,0 | 32€ |
| KYCCF | T2 | — (O3) | 🟡 3\* | ×1,0 | 32€ |
| V | T2 | 64 | 🟠 2 | ×0,5 | 16€ |
| RMS | T3 | 68 | 🟡 3 | ×1,0 | 18€ |
| BRK.B | T3 | 71 | 🟡 3 | ×1,0 | 18€ |
| TMO | T3 | 67 | 🟡 3 | ×1,0 | 18€ |
| APH | T3 | 61 | 🟠 2 | 🔴 FLAG | 0€ |
| SU | T3 | 69 | 🟡 3 | ×1,0 | 18€ |
| ZETA | T3 | — (O3) | 🟡 3\* | ×1,0 | 18€ |

\* NOW/KYCCF/ZETA = DEFCON-3-Platzhalter (Owner-Conviction-Add ohne Score, volle Tier-Rate bis O3-Vollanalyse).
**SOLL-Σ:** 4×40 + 3×32 + 6×18 = **364€** (== config.yaml brokers.scalable.sparrate_eur) | **Funded-Σ:** 40 + 80 + 90 = **210€** | **Differenz 154€** (FLAG-frozen AMZN/MSFT/AVGO/APH 138€ + V-D2-Sockel 16€) → Rebalancing-Tool value-based.

> **SSoT:** config.yaml `satelliten_tier_raten` + `sparplan_verteilung`. Das flache Equal-Weight-Modell (285€/Σ-Gewichte, volle Rate 35,63€/D2 17,81€) ist seit 2026-06-07 historisch abgelöst (Governance-Override UMSTRUKTURIERUNG-2027 §6.1).

---

## 23. Tariff Exposure Scoring

**Quelle:** 10-K "Geographic Revenue" + Manufacturing Locations
**Malus:** -1 Punkt Fundamentals bei >20% Revenue CN/TW/MY/TH/VN
**FLAG:** >35% → 🔴 FLAG aktiv, -3 Punkte, Sparrate 0€

---

## 24. Morning Briefing (Scheduled Trigger v3.1.1, prod live seit 07.05.2026)

> **Detail-Spec ausgelagert (09.05.2026, PIPELINE #16 Variante A):** [`03_Tools/morning-briefing-spec.md §24`](../03_Tools/morning-briefing-spec.md). Inline-Drift-Refresh §24-Header v2.1→v3.1.1 (Stand 07.05. PIPELINE #49 Stufe 2). Live-Stand-Detail (Allow-List-Regex / Bracket-Reservation / AIDefence-Hook v3.2.0) → SYSTEM.md §Briefing-Status.

**Trigger-ID:** `trig_01PyAVAxFpjbPkvXq7UrS2uG` | **Frequenz:** Mo-Fr 10:00 MESZ (Cron `0 8 * * *` UTC) | **Modell:** `claude-sonnet-4-6` | **Token-Budget:** ~12-18k/Tag werktags
**Prompt-Datei:** `03_Tools/morning-briefing-prompt-v3.md` (v3.1.1 prod; v3.2.0 Probe-Cutover PENDING)
**Rollback-Backup:** `03_Tools/morning-briefing-prompt-v2.md` (30-Tage-Recovery-Window)
**Scope:** 13 Satelliten + Ersatzbank. ⚠️ Briefing-Universe-Integration der neuen Satelliten NOW/KYCCF/ZETA (KYCCF=JP→yfinance-Pfad, NOW/ZETA=US→Shibui) + Ersatzbank-Refresh = offene operative Aufgabe (Umstrukturierung-2027 Phase A, gekoppelt an O3-Scoring; bis dahin briefen die bestehenden 10 Satelliten + Ersatzbank).
**Datenquellen-Tier:** 13 Shibui (`stock_data_query` P1) + 3 Yahoo-curl (BRK.B/RMS/SU, Yahoo 403 known).

**Manueller Trigger:** `!Briefing` (identischer Output) oder Desktop App → Routines.

**Voraussetzung:** Faktortabelle aktuell (§18) + GitHub-Repo gepusht (`!SyncBriefing`).

Detail (Critical-Guards SUNCOR-TRAP/BERKSHIRE-GAP/HERMES-GAP/ANTI-HALLUCINATION/KEIN-RETRY, Schwellenwerte-Tabelle Kurs/Earnings/Score-Alter, API-Update-Regel `ccr`-Replace, Known Limitations Yahoo 403 / Push-Notifications / `RemoteTrigger run` Noop) → `03_Tools/morning-briefing-spec.md §24`.

---

## 25. Briefing-Sync Shortcuts (GitHub ↔ Local)

> **Detail-Spec ausgelagert (09.05.2026, PIPELINE #16 Variante A):** [`03_Tools/morning-briefing-spec.md §25`](../03_Tools/morning-briefing-spec.md).

Der 10:00-Briefing-Trigger liest `00_Core/` aus dem **GitHub-Repo** — nicht aus dem lokalen Arbeitsverzeichnis. Lokale `00_Core/`-Änderungen müssen vor 10:00 gepusht sein.

### `!BriefingCheck`
Vorab-Check ob Trigger aktuelle Daten liest. `git fetch origin main --quiet` + `git diff --stat origin/main -- 00_Core/`. Detail-Output-Schema → Spec.

### `!SyncBriefing`
Briefing-relevante `00_Core/`-Änderungen ins Repo pushen mit **Pflicht-Review-Gate** (kein Auto-Commit). `git add` 8 Hub-Split-Pfade explizit (parallel zu `briefingFiles`-Set in `03_Tools/briefing-sync-check.ps1` — SSoT-Brücke). Commit-Schema: `Briefing-Sync: <Inhalt>`. Detail-Workflow → Spec.

### Reminder (Scheduled Task `briefing-sync-reminder`)
Werktags 09:50, 10-Min-Puffer vor 10:00-Trigger, kein Auto-Push.

### Wann nötig
Nach DEFCON-Analyse (Score/FLAG-Änderung) / CORE-MEMORY-Eintrag / Sparraten-Änderung in SESSION-HANDOVER / vor Session-Ende mit unpushed Score-Updates.

### Wann **kein** Push nötig
Reine Skill-/Tool-/Vault-Änderungen (`01_Skills/`, `03_Tools/`, `07_Obsidian Vault/`) — Briefing liest diese nicht. WIP-Analysen erst nach Abschluss pushen.

### 25.5 Session-Closure-Workflow (21.05.2026, session-closure v0.2.0)

**Strict-Trigger:** `!SessionClose` (deutsch, PascalCase, kein Fuzzy-Match). Phrasen-Varianten („Session beenden", „push & weg") → Rückfrage statt Auto-Activation (analog `!Analysiere`-Disziplin).

**Sicherheits-Boundary (normativ):** Skill darf lokale Commits autonom ausführen; `git push` ausschließlich nach expliziter User-Freigabe.

**SSoT:** Workflow, Refuse-Conditions, Banner-Konventionen, Push-Safety-Checks in `01_Skills/session-closure/SKILL.md` v0.2.0 + `references/`. §25.5 verankert nur Trigger-Strictness + Sicherheits-Boundary — keine Workflow-Duplikation.

**Cross-Refs:** CLAUDE.md Routing-Table · SYSTEM.md §System-Zustand · CORE-MEMORY.md §6 + §13.

---

## 26. Archiv-Sync (Backtest-Ready-Pipeline)

**Trigger:** Nach jeder `!Analysiere` (Vollanalyse/Delta/Rescoring) UND bei jedem FLAG-Trigger oder FLAG-Resolution.

**→ CLI-Usage + Exit-Codes:** [`03_Tools/backtest-ready/README.md`](../03_Tools/backtest-ready/README.md)

### Workflow (4 Schritte)

1. **Score-JSON generieren** (SKILL.md Schritt 7) — `ScoreRecord` gemäß `schemas.py`. Pflichtfelder: `schema_version: "1.0"`, `record_id: YYYY-MM-DD_TICKER_TYP`, `source: "forward"`, `defcon_version` aktuell, `score_datum` (heute, max. 3 Tage zurück), vollständige 5-Block-`scores` + `score_gesamt` + `defcon_level`, `kurs`, `market_cap`, `flags`, `metriken_roh`, `quellen`.
2. **Archivieren** — `archive_score.py --file <tempfile.json>`. Keine Ausnahme, kein Record darf verloren gehen.
3. **FLAG-Events archivieren** (nur bei Trigger/Resolution, SKILL.md Schritt 6b) — `archive_flag.py trigger` oder `resolve`. Schwellen aus `FLAG_RULES` automatisch.
4. **Git-Commit** — vollständiges Score-Event-File-Set §18 v2.1 atomar in einem Commit (6 Pflicht-Files inkl. `config.yaml`, + conditional `flag_events.jsonl` bei FLAG-Trigger/Resolve, + Multi-Event-Union per §18.2 falls weitere Event-Typen mit-betroffen).

### Fehler-Klassen

- **Forward-Window-Violation** (`score_datum` >3 Tage alt) → `analyse_typ: "rescoring"` setzen oder heutiges Datum + Hinweis in `notizen`.
- **Duplicate record_id** → kein `--force`; stattdessen `analyse_typ` auf `delta` ändern.
- **FLAG-Schwelle-Mismatch** → Schwellen sind hardcoded in `schemas.py`; Schwellen-Änderung = `schema_version`-Bump (additiv 1.1, breaking 2.0).
- **Validation-Fail (exit 1)** → JSON korrigieren, erneut ausführen.
- **IO-Fail (exit 2)** → Archiv-Korruption prüfen.

### Nicht archiviert

`!QuickCheck`, Stufe-0-Screener-Outputs, Rohdaten aus `insider_intel.py`/`eodhd_intel.py` (nur finale 100-Punkte-Scores).

---

## 27. Scoring-Hygiene & Daten-Integrität

Systemische Regeln zur Qualitätssicherung von Scoring-Erweiterungen und Multi-Source-Konsistenz. Promotion aus Applied Learning am 18.04.2026 — bewährt über mehrere Session-Zyklen.

### 27.1 Double-Counting-Vermeidung bei Scoring-Erweiterungen

**Regel:** Bei jeder Scoring-Erweiterung (neuer Bonus, neuer Malus, neuer Sub-Score) zuerst prüfen ob Sub-Signale bereits im System dekomponiert sind.

**Typische Falle:** Aggregat-Scores (F-Score, Altman-Z, etc.) auf ein System aufsetzen, das ihre Einzelfaktoren bereits abbildet. Ergebnis: derselbe Effekt wird doppelt bestraft/belohnt.

**Pflichtcheck vor Erweiterung:**
1. Liste alle Komponenten des neuen Aggregats auf.
2. Grep alle DEFCON-Sub-Scores (Fundamentals, Moat, Technicals, Insider, Sentiment) auf Überschneidungen.
3. Bei Überschneidung: entweder neuer Score nur **orthogonale** Signale nutzt, oder Überschneidung mit Hard-Cap auf Block-Ebene neutralisieren (siehe §27.2).

**Präzedenzfall:** v3.7 Quality-Trap-Interaktion — implementiert als Deckel auf Fwd-P/E + P/FCF-Subscores, nicht als additiver Moat-Malus (vermeidet Double-Counting mit bestehender Fundamentals-Dekomposition).

### 27.2 Bonus-Cap-Check bei neuen Bonus-Regeln

**Regel:** Vor Rollout eines neuen Bonus (Punkte +X) Punkteverteilung Top-Namen simulieren.

**Typische Falle:** Bonus wirkt nur in der Mitte der Score-Verteilung, weil Top-Namen bereits am Block-Cap (Fundamentals 50, Moat 20, etc.) anstehen. Ergebnis: asymmetrische Verzerrung zugunsten von B-Namen, Top-Namen verlieren Bonus-Headroom.

**Pflichtcheck:**
1. Für alle aktuellen 13 Satelliten durchrechnen: Block-Score + potenzieller Bonus.
2. Wenn ≥3 Top-Namen am Cap hängen bleiben → Bonus entweder ins Block-Cap integrieren oder als Tie-Breaker statt Score-Boost.
3. Dokumentieren in Scoring-Lektionen (CORE-MEMORY §5).

**Präzedenzfall:** v3.7 Fundamentals-Cap 50 — bewusst akzeptiert dass Top-Namen (AVGO 84) weniger Bonus-Headroom haben; dafür Score-Inflation strukturell ausgeschlossen.

### 27.3 Primärquellen vs. Navigations-/Projektions-Layer

**Regel (v2, 2026-04-24 00_Core-Refactor):** Nach dem Refactor gilt eine Drei-Ebenen-Klassifikation statt der alten Projektions-Dichotomie.

**Primärquellen (direkt editierbar, Single-Source-of-Truth):**
- `Faktortabelle.md`
- `CORE-MEMORY.md` (inkl. §12 Per-Ticker, §13 System-Lifecycle)
- `score_history.jsonl` (ausschließlich via `archive_score.py` / `backtest-ready-forward-verify`-Skill)
- `flag_events.jsonl` (ausschließlich via `archive_flag.py`)
- **`PORTFOLIO.md`** (NEU — Portfolio-Tabelle + Watches + 30-Tage-Trigger, direkt editierbar, kein Projektions-Verbot)
- **`PIPELINE.md`** (NEU — Pipeline-SSoT, direkt editierbar bei Plan-Commits/Gate-Passagen)
- **`SYSTEM.md`** (NEU — System-Zustand, direkt editierbar bei Infra-Änderungen)

**Navigations-/Hub-Layer:**
- `STATE.md` (Hub) — Navigation + Critical-Alert + Last-Audit-Block. Darf direkt editiert werden (handgepflegter Alert-Slot; Last-Audit-Block script-geschrieben).

**Reine Projektion (aus Primärquellen ableiten, niemals selbst fortschreiben):**
- Briefing-Tabellen (Morning Briefing Prompts)
- Dashboard-Summaries (`dynasty-depot-dashboard` Artifact)

**Pflichtreihenfolge bei Score/FLAG/Sparraten-Änderung:**
1. Primärquellen zuerst (Faktortabelle.md, CORE-MEMORY.md, score_history.jsonl via Skill).
2. PORTFOLIO.md synchron nachziehen.
3. Briefing-Projektionen laufen automatisch beim nächsten Briefing-Trigger.

**Präzedenzfall:** 24.04.2026 — 00_Core-Refactor entkoppelt Live-State (PORTFOLIO) vom Navigations-Hub (STATE) und räumt mit der Projektions-Aspiration auf, die in der Praxis nie gelebt wurde (Portfolio-Tabelle wurde immer direkt editiert).

### 27.4 Multi-Source-Drift-Check vor "fertig"-Meldung

**Regel:** Vor Abschluss einer Systemänderung **alle Wahrheitsquellen greppen** — config.yaml-Fix allein reicht nie.

**Pflicht-Suchliste:**
- `00_Core/INSTRUKTIONEN.md` (§§)
- `00_Core/CORE-MEMORY.md` (§4 Score-Tabelle, §5/§12/§13 Scoring-Lektionen + Per-Ticker + Lifecycle)
- `01_Skills/dynastie-depot/config.yaml`
- `01_Skills/dynastie-depot/SKILL.md`
- `00_Core/STATE.md` (Hub + Last-Audit), `00_Core/PORTFOLIO.md`, `00_Core/PIPELINE.md`, `00_Core/SYSTEM.md`, `Faktortabelle.md`
- `07_Obsidian Vault/.../wiki/entities/satelliten/*.md`
- `03_Tools/Rebalancing_Tool_v3.4.xlsx`, `Satelliten_Monitor_v2.0.xlsx`

**Präzedenzfall:** 18.04.2026 Schema-SKILL-Threshold-Drift — Fix in schemas.py alleine hätte 5 Vault-Pages und beide Tools veraltet zurückgelassen. Kaskaden-Sync war Pflicht.

**Zweite Klasse — Vertikal-Drift (Schema-Migration auf Altdaten):** Bei Wortwahl „Drift-Check"/„Hygiene"/„System-Sanity"-Auftrag ODER bei jedem Schema-/Threshold-Migration-Commit zusätzlich Re-Validate-Sweep aller persistierten Records (`05_Archiv/*.jsonl`) gegen aktuelles Schema durchführen. Spot-Check über Wahrheitsquellen (oben) deckt nur Horizontal-Drift; vertikale Drift entsteht silent wenn Validator-Threshold tickt aber alte Records nicht migriert werden. **Resultat als „N/M PASS" explizit ausschreiben**, niemals weichgespültes „sieht gut aus". Bei FAIL: idempotente Snap-to-Schema-Migration als separater Commit VOR weiterer Arbeit.

**Präzedenzfall (vertikal):** 21.04.2026 Pre-Check vor Provenance-Gate-Plan — 12/27 Records in `score_history.jsonl` waren seit 18.04.-Threshold-Migration silent inkonsistent, nie aufgefallen, weil zwischendurch nur Spot-Check auf Forward-Pfad lief (`feedback_exhaustive_drift_check.md`).

**Dritte Klasse — Methodology-Drift (Quellen-Hard-Ausschluss):** Bei Score-Berechnungs-Inputs (ROIC, Forward-P/E, FCF-Yield) immer Quellen-Hierarchie aus `01_Skills/dynastie-depot/sources.md §5` + Hard-Ausschluss-Register §7 prüfen. Beispiel: StockAnalysis ist für ROIC + Forward-P/E **hart ausgeschlossen** (Non-GAAP-Drift, Präzedenz AVGO/MSFT 30.04.2026). Score-Drift +5 bis +30 Punkte möglich, wenn das missachtet wird.

**Wissenschaftlicher Anker:** Double-Counting-Vermeidung und Bonus-Cap-Check verhindern False-Positives unterhalb §29.4 t-Stat ≥ 3 Hurdle (Harvey/Liu/Zhu). Jede neue Sub-Komponente muss t≥3 erreichen. → §29.4 / [[Aghassi-2023-Fact-Fiction]]

### 27.5 Migration-Regression-Guard (22.04.2026, system-audit v1.0)

**Regel:** Nach jedem Lauf eines `03_Tools/backtest-ready/migrate_*.py`-Helpers MUSS
`python 03_Tools/system_audit.py --minimal-baseline` Exit-Code 0 zeigen
(strukturelle Integrity: `jsonl_schema` + `pipeline_ssot` + `log_lag`).
Ein FAIL nach Migration bedeutet: Migration unvollständig oder neuer Schema-Drift
eingeführt. Der Migration-Commit darf nicht gepusht werden, bevor dieser
Regression-Guard grün ist.

**Scope-Entscheidung `--minimal-baseline` statt `--core`:** Plan 2026-04-21
sah `--core` vor; in Praxis blockiert pre-existing Drift in Check-3
(`markdown_header` Future-Date-Bug, Follow-up-Task) und Check-5 (`existence`,
~54 CLAUDE.md-Pfadreferenzen deferred auf Post-Task-17-Follow-up-Welle) den
Baseline-Gate. `--minimal-baseline` isoliert die 3 Checks, die Migrationen
tatsächlich gefährden können, ohne Drift-Noise. Sobald Check-3-Fix + existence-
Cleanup committed sind, wird der Guard auf `--core` hochgezogen (Migration-
Kommentar in dieser Regel).

**Rationale:** Drift-Migration 21.04.2026 (12/27 defcon-silent-Drift) bewies,
dass einzelne Migrations-Helper nur ihre Ziel-Klasse fixen. Der Audit-Gesamtblick
fängt Cross-Store-Drift, die ein spezialisiertes Tool nicht sieht. Schema-Re-
Validation (Check-1) + Pipeline-Plan-Existenz (Check-6) + log-Aktualität (Check-7)
sind die minimalen strukturellen Invarianten, die ein Migrations-Run nicht
brechen darf.

### 27.6 Earnings-Calendar-Drift-Check (Stufe 2 — earnings_calendar.py v2.0, 06.05.2026)

**Regel:** Earnings-Termin-Drift-Check läuft (a) automatisch im SessionStart-Hook (`briefing-sync-check.ps1`) als additive fail-soft-Sektion, (b) manuell on-demand via `python 03_Tools/earnings_calendar.py --check [--smoke-test] [--json]`. Tool pullt yfinance-Future-Dates UND mergt Override-YAML (`03_Tools/earnings_schedule_overrides.yaml`, earliest-wins-Union) für die 13 Satelliten + diff gegen PORTFOLIO „Nächster Trigger"-Spalte.

**Override-YAML:** SSoT für Earnings-Termine, die yfinance nicht oder unzuverlässig liefert (insbesondere Schneider/Hermès Q1+Q3 Trading-Updates und ASML-Sondertermine). Pflege 1×/Jahr nach IR-Calendar-Release der Non-US-Issuer (typisch November/Dezember für Folgejahr). `type`-Field treibt §19.1-Tag-0/Tag-+1-Decision: `trading_update_q*` = Tag 0 direkt (analog BRK.B), `half_year_*` / `annual_results` = Tag +1 mit Earnings-Call, `capital_markets_day` = Strategy-Update kein Score-Move.

**Output-Modi:**
- Markdown (default): menschen-lesbarer CLI-Report mit Drift-Tabelle + Smoke-Test + Drift-Liste
- `--json`: maschinen-lesbares Schema (orientiert an `system_audit/types.py::CheckResult`-Shape ohne Hard-Import). Konsumiert von `briefing-sync-check.ps1`.

**Exit-Verhalten:** 0 = clean, 1 = Smoke-Test-FAIL nur mit `--smoke-test`-Flag (BRK.B-Anker bricht — Tool-Bug oder Yahoo-Datenstand-Problem), 2 = Drift im `--alert-window` (default 10d).

**Hook-Integration (M2-konform):** SessionStart-Owner bleibt `briefing-sync-check.ps1` (single-owner-rule). Drift-Block ist additive im selben Process, fail-soft (Tool-Crash, broken YAML, missing Python alle abgefangen — Hook bleibt Exit 0).

**Scope Stufe 2:** Tool diffed weiterhin **nur** gegen PORTFOLIO „Nächster Trigger"-Spalte. STATE-Critical-Alerts + PIPELINE-Kritische-Triggers-10d/30d sind nicht im Tool-Diff abgedeckt — Operator muss bei detektierter PORTFOLIO-Drift STATE + PIPELINE manuell mitziehen (Single-Sync-Welle). Auto-PIPELINE-Stub-Erzeugung + Late-Recovery-Workflow sind separater Track (Skill-Layer, nicht Calendar-Tool — Spec §5 Out-of-Scope).

**Trigger:** Drift im `--alert-window` → manuell PORTFOLIO + STATE Critical-Alerts + PIPELINE-Kritische-Triggers-10d/30d auf konkretes Datum konkretisieren. Detail in `00_Core/SYSTEM.md §Earnings-Calendar-Status` Stufe-2-Sub-Block.

**Rationale:** Erweitert v1.0 (PIPELINE #24 deployed 30.04.) um (a) Coverage-Lücke bei Non-US-Quartalen ohne Earnings-Call (SU Q1 30.04. verpasst) und (b) Trigger-Lücke (manueller On-demand-Aufruf). Hook-Integration adressiert Mental-Off-Switch-Risiko strukturell statt prozedural. Codex-Sparring-Trail in Spec `docs/superpowers/specs/2026-05-06-earnings-calendar-stufe2-coverage-trigger-design.md`.

### 27.7 Carryover-Discipline-Asymmetrie (NEU 09.05.2026, PIPELINE #23 Closure)

**Regel:** `_carryover`-markierte Quellen (Source-Token Whole-Word, Source-Prefix `ir_`, oder Reason-Token terminal — Whitelist `03_Tools/backtest-ready/provenance_gate.py::CARRYOVER_SOURCE_TOKENS` / `CARRYOVER_SOURCE_PREFIXES` / `CARRYOVER_REASON_TERMINAL`) erlauben semantisch ausschließlich **unveränderte Übernahme** des Sub-Score-Werts vom letzten primary-source-Run. **Up-Scoring** (Sub-Score steigt vs letztem primary-source-Wert) ist bei `_carryover`-Markierung Workflow-Verstoß. **Down-Scoring** (konservative Korrektur z.B. nach Reviewer-Feedback) bleibt erlaubt — Disziplin gilt asymmetrisch.

**Pflichtcheck pro Block:** Bei `quellen.<block>` mit legitimem `*_carryover`-Suffix gilt `scores.<block>.<sub_score> ≤ letzter_primary_source_<sub_score>`. Aufwertung erfordert explizite neue Datenerhebung (Form-4-Re-Pull, Earnings-Call-Transcript-Re-Read, Live-WACC-Pull, Live-Insider-Scan etc.) — und damit Wechsel von `*_carryover`-Quelle auf Live-Source-Token. Keine Mischung „Carryover plus Up-Score-Begründung aus anderem Block" (z.B. Buyback-Disziplin als Insider-Up-Score-Begründung — gehört zum Sentiment-Block, nicht Insider).

**Operationalisierung:** Reviewer-Disziplin (manuell beim Pre-Append-Audit, Cross-Reference SKILL.md Schritt 6c). Programmatischer `provenance_gate.py`-Check für Carryover-Up-Score-Asymmetrie aktuell **deferred** (PIPELINE #23 — INSTRUKTIONEN-Klarstellung reicht für Reviewer-Disziplin; Code-Erweiterung erfordert vorhergehende primary-source-Werte als zweite Eingabe und ist out-of-scope für aktuelle pipeline_gate-Architektur).

**Präzedenzfall (V Q2 28.04.2026 Reinfall, Codex-MEDIUM-2):** 28.04.-Vollanalyse-Record hatte Insider-Score 5→6 mit Begründung „carryover-rounding clean record + Q2-Buyback-Disziplin Ø $320,66 = Management-Conviction-Signal". `quellen.insider="openinsider_form4_skip_window_pre_score_carryover"` ist Carryover-Markierung ohne neue Datenerhebung. Buyback-Disziplin ist Company-Action und gehört semantisch zu Sentiment-Block (PT-Upside / EPS-Revision-Momentum), nicht Insider (Net Buy / Ownership / kein-$20M-Selling). Korrekt wäre: Insider 5/10 unverändert mit `_carryover`-Markierung, ggf. Sentiment-Sub-Score-Anpassung mit eigener Live-Source-Begründung.

**Cross-Reference:** SKILL.md Schritt 6c Pre-Flight-Klausel + INSTRUKTIONEN §19.1 Cross-Reference Backfill-Eligibility (Schritt 0 Bullet 4). Carryover-Asymmetrie ist orthogonal zur Backfill-Eligibility — Backfill-Eligibility prüft ob Skip-Window-Carryover ÜBERHAUPT zulässig ist (vorhergehender Record vollanalyse mit voller Coverage); Carryover-Asymmetrie regelt zusätzlich, dass innerhalb erlaubter Carryover-Übernahme kein Up-Score zulässig ist.

### 27.8 DCF-Malus Bull-Source-Pflicht (NEU 09.05.2026, PIPELINE #34 Closure)

**Regel:** Wenn der Technicals-Sub-Score `dcf_relation_delta < 0` (DCF-Malus aktiv, Kurs > Bull-DCF +20% per SKILL.md §Technicals Bull/Bear-Anker), MUSS im ScoreRecord `metriken_roh.bull_dcf_source` ein literal-Quellen-Label tragen (Beispiele: `"alphaspread_bull_band_2026-04-30"`, `"internal_capex_fcf_bull_$520"`, `"morningstar_bull_band_2026-04-30"`). Optionales Feld `metriken_roh.bull_dcf_value_usd` (float) hält den Bull-Band-Wert für spätere Backtest-Auswertung.

**Heuristic/Empty Reject:** Werte wie `None`, `""`, `"   "`, `"unknown"`, `"tbd"`, `"todo"`, `"placeholder"`, `"none"`, `"na"`, `"n/a"`, `"?"`, `"heuristic"` ODER alles, was die Substring `"heuristic"` enthält (z.B. `"base_x_115_heuristic"`), werden fail-close abgelehnt. Whitelist siehe `03_Tools/backtest-ready/schemas.py::BULL_DCF_HEURISTIC_BLACKLIST` + Helper `_is_heuristic_bull_dcf_source`.

**Doppelte Verteidigungslinie:**
1. **Schema-Validator** (`schemas.py::ScoreRecord._check_dcf_malus_source`, model_validator mode="after"): Pydantic-seitig fail-close bei Forward-Records.
2. **Provenance-Gate Check #9** (`provenance_gate.py::check_provenance`): Vor Pydantic-Validation, gibt domain-spezifische Reason-String an Caller (Backtest-Ready-Forward-Verify Skill).

**Skip-Conditions (beide Layer):** `source == "backfill"` (historische Records ohne Bull-Source-Doku zulässig) ODER `dcf_relation_delta >= 0` (kein Malus aktiv). Forward + Vollanalyse + Malus-aktiv = Bull-Source pflicht.

**Präzedenzfall (AVGO 30.04.2026, Codex-R1-HIGH-5 REJECT):** Vollanalyse-Draft hatte `Bull = AlphaSpread Base $256 × 1,15 = $294` als heuristischen Bull-Band-Uplift angenommen — kein dokumentierter Bull-Band aus capex-fcf-template oder externer Bull-DCF-Quelle. Codex-R1 REJECTED den +1-DCF-Bonus-Pfad als regelwidrig (SKILL.md verlangt actual Bull/Bear-Band). Final-Score 53/D2 ohne DCF-Malus-Aktivierung. Diese Regel macht den Schutz schema-side enforced für künftige Vollanalysen.

**Cross-Reference:** SKILL.md §Technicals Bull/Bear-DCF-Block (Stand 09.05.2026 mit Bull-Source-Pflicht-Note) + `01_Skills/dynastie-depot/capex-fcf-template.md` Sheet 2 (Vorlage Bull/Base/Bear-Szenarien) + Schema-Smoke-Tests `schemas.py::_smoke_tests` Cases M1-M5 + Provenance-Gate-Smoke-Tests `provenance_gate.py::_smoke_tests` Case 10a-10f.

---

## 28. Scoring-Version-Migration-Workflow

Systemischer Workflow für DEFCON-Versionssprünge (v3.x → v3.y). Promotion aus Applied Learning am 18.04.2026 — belegt durch zwei Migrationen binnen 14 Tagen (v3.4→v3.5, v3.5→v3.7), beide mit orphan-References + nachgelagerten Fan-Out-Fixes.

**Regel:** Jeder Version-Bump durchläuft die folgende 7-Step-Checklist **vor** dem finalen Commit. Kein Ad-hoc-Rollout.

### 28.1 Pflicht-Checklist

**Step 1 — Paper/Evidence-Check**
Schriftlich begründen: *Welche Primärquelle* (Paper, Backtest-Befund, Präzedenz-Lektion aus CORE-MEMORY §5) rechtfertigt die Änderung? Ohne Evidenz kein Bump — Ästhetik zählt nicht (Applied Learning v1.0 Bullet #4).

**Step 2 — Redundanz-Check (§27.1)**
Neue/geänderte Sub-Scores gegen alle bestehenden DEFCON-Blöcke greppen. Double-Counting ausschließen.

**Step 3 — Algebra-Projektion n≥5**
Auf 5+ Sample-Tickern **rechnerisch** neue Score-Projektion erstellen. Verteilung prüfen: keine Score-Inflation, keine strukturelle Asymmetrie zwischen Top-/Mid-Namen (§27.2).

**Step 4 — Forward-Verify-Sample**
Auf 2-3 Tickern die **empirische** Forward-Vollanalyse mit neuer Version laufen (`03_Tools/backtest-ready/`). Delta-Check Algebra vs. Forward nach gestuftem Schema in §28.2. **Schritte 1-6 auf Branch, Step 4 muss grün (Δ≤5) sein bevor Step 7 Fan-Out beginnt** — sonst wird fehlerhafte Migration über 7 Oberflächen geschmiert.

**Step 5 — Orphan-Grep alter Version-Strings**
```bash
# ripgrep — ODER-Alternation mit -e (mehrere Patterns), nicht \|
rg -n -e "v3\.4" -e "3\.4\.1" 01_Skills/ 00_Core/ "07_Obsidian Vault/"
rg -n -e "3\.4\.1" -e "3\.5" -e "3\.6" 03_Tools/   # Vorgänger-Versionen anpassen
```
Alle Treffer prüfen: bewusster Historie-Bezug oder veraltete Referenz? Veraltete → fixen.

**Step 6 — Anchor-Rekalibrierung (§7)**
Bestehende Kalibrierungsanker auf neue Scoring-Skala umrechnen. Dokumentieren welche Anker verschoben, welche gleich blieben.

**Step 7 — Fan-Out-Gate (7 Oberflächen)**
Nur starten wenn Step 4 grün. Vor Commit alle folgenden Stellen synchronisiert:
1. `00_Core/INSTRUKTIONEN.md` — §§ mit versionierten Regeln
2. `01_Skills/dynastie-depot/SKILL.md` — frontmatter `version:` + inline v-References *(andere Skills: `insider-intelligence`, `quick-screener`, `non-us-fundamentals` — werden durch Step 5 Orphan-Grep abgedeckt, nicht durch Positiv-Sync)*
3. `01_Skills/dynastie-depot/config.yaml` — Schwellen, Gewichte, FLAG-Trigger
4. `03_Tools/*.xlsx` — Rebalancing-Tool + Satelliten-Monitor (Scoring-Formeln, Threshold-Zellen)
5. `00_Core/Faktortabelle.md` — Migration-Note mit Datum + Delta
6. `07_Obsidian Vault/.../wiki/entities/satelliten/*.md` — Scores + Scoring-Version-Tag
7. `00_Core/CORE-MEMORY.md` — §5 Scoring-Lektion + §1 Meilenstein-Eintrag

**Final:** §27.4 Drift-Check-Gate (grep alter Version-Strings verifiziert leer bei nicht-historischen Kontexten).

### 28.2 Algebra-≠-Forward-Diskrepanz (gestuft)

**Regel — gestufte Abweichungs-Toleranz:**

| Δ (Algebra vs. Forward) | Aktion |
|---|---|
| **≤2 Punkte** | Akzeptiert — innerhalb Proxy/Timing-Noise |
| **3-5 Punkte** | In CORE-MEMORY §5 als Lektion loggen, Migration fortsetzen |
| **>5 Punkte** | **Blockiert** — Ursache identifizieren bevor Step 7 Fan-Out |

**Typische Ursachen:**
- Proxy-Mapping-Drift: Algebra nutzt annahme-basierte Inputs, Forward zieht Live-Daten (z.B. WC-Schwankungen, FX, Quarter-Cuts).
- FLAG-Trigger bei Live-Daten, die in der Algebra-Projektion nicht aktivierbar waren.
- Scoring-Regel hängt an Daten-Frische (z.B. `fcf_trend_neg` multi-quarter).

**Pflicht:** Diskrepanz in CORE-MEMORY §5 als Lektion loggen. Bei systematischer Ursache (z.B. Proxy-Fehler) Algebra-Layer nachbessern, nicht nur den Einzelfall fixen.

**Präzedenzfall:** 18.04.2026 V-Forward — Algebra projizierte 86, Forward lieferte 63 (Δ23). Ursache: Algebra ignorierte WC-Working-Capital-Dekomposition, die in Forward `fcf_trend_neg` triggerte. Regel-Bug, nicht Ticker-Einzelfall.

### 28.3 Nicht-Migration-Trigger

**Regel:** Ein Scoring-Bump ist **keine** Migration wenn:
- Nur einzelne Kalibrierungsanker auf aktualisierte Fundamentals rekalibriert werden (Quartals-Normalpflege).
- Ein Bugfix einer bestehenden Regel ohne Skalen-/Gewichts-Änderung (z.B. Schwellwert-Copy-Paste-Fehler in config.yaml).
- Ein neuer FLAG ohne Score-Impact hinzugefügt wird (reine Disclosure).

Für diese Fälle reicht: Commit + zugehöriges Hub-Set-Update (PORTFOLIO bei Score/Sparrate, SYSTEM bei Infra) + CORE-MEMORY §5 Lektion, keine Step-1-7-Pflicht.

**Präzedenzfall:** 18.04.2026 TMO `fcf_trend_neg`-Disclosure (Option B) — struktureller FLAG ohne Score-Penalty, kein Version-Bump.

**Wissenschaftlicher Anker:** §28.2 Δ-Gate und §28.4 Forward-Verify greifen in die Validation-Ebene ein, die §29 retrospektiv absichert: §29.1 (PBO/CSCV nach Bailey) für Parameter-Variations und §29.5 (Seven-Sins-Pre-Flight) für jeden Migration-Event ab sofort aktiv. → §29.1 / §29.5 / [[Bailey-2015-PBO]] / [[Seven-Sins-Backtesting]]

---

## 29. Retrospective-Analyse-Gate

> **Detail-Spec ausgelagert (09.05.2026, PIPELINE #16 Variante A):** [`00_Core/RETROSPECTIVE-GATE.md`](RETROSPECTIVE-GATE.md). Hier nur Stub + Sub-Section-Anchors für Cross-Reference-Erhalt aus §28 / §18 / §27 / §30 / §4.
>
> **`[FUTURE-ACTIVATION: 2028-04-01]` für §29.1-3 + §29.6 + §29.7. §29.4 (t-Hurdle) + §29.5 (Seven-Sins-Gate) aktiv bereits jetzt bei Migration-Events.**

Systemischer Gate für jede retrospektive Analyse der `score_history.jsonl` (Strategy-Selection, Parameter-Tuning, Portfolio-Return-Validation). §28 (Migration-Workflow) ist **komplementär**, nicht konkurrierend: §28 schützt Versions-Sprünge, §29 schützt Retrospective-Auswertungen.

### 29.1 Methoden-Gate — Overfitting (Bailey et al. 2015)
PBO < 0,05 via CSCV. Implementierung: `03_Tools/backtest-ready/pbo_cscv.py` (S=16, N≥10). Komplementär: walk-forward + GT-Score (Sheppert 2026, B20). → `RETROSPECTIVE-GATE.md §29.1`

### 29.2 External-Benchmark-Gate (Aghassi et al. 2023)
Aggregierte Satelliten-SR im AQR/Ilmanen-Multifaktor-Band. Mapping: Fundamentals→Value/HMLDEVIL, Moat+Quality→QMJ/BAB, Technicals→UMD/Momentum, Insider→non-AQR-Edge. → `RETROSPECTIVE-GATE.md §29.2`

### 29.3 Temporal-Konsistenz (Flint & Vermaak 2021)
Score-Cadence ↔ Faktor-Half-Life. Investment-Klasse (1M-Half-Life) als Watch (MSFT-CapEx, TMO-fcf_trend_neg). → `RETROSPECTIVE-GATE.md §29.3`

### 29.4 Neue-Parameter-Gate — Harvey/Liu/Zhu-Hurdle
**SOFORT aktiv** (nicht 2028): t-Stat ≥ 3 für jede neue DEFCON-Sub-Komponente. Ergänzt §28.1 Step 1. → `RETROSPECTIVE-GATE.md §29.4`

### 29.5 Seven-Sins-Pre-Flight-Gate (Palomar 2025 Ch 8.2)
**SOFORT aktiv bei Migration-Events.** 7-Punkt-Checkliste (Survivorship / Look-Ahead / Storytelling / Overfitting / Turnover / Outliers / Asymmetric — Sin #7 n.a. Long-Only) + B19 FINSABER-Regime-Audit-Addendum (Bull/Bear-Subsample / Symbol-Breite / Zeitfenster). → `RETROSPECTIVE-GATE.md §29.5`

### 29.6 Portfolio-Return-Metrik-Layer (Palomar 2025 Ch 6)
Sortino/CVaR/Calmar/Max-DD/IR via `risk-metrics-calculation`-Skill gegen `05_Archiv/portfolio_returns.jsonl`. GT-Score-Composite-Alignment (B20). Aktivierung: 2028-04-01 ODER ≥24M sauberer Return-Serie. Interim-Gate 2027-10-19. → `RETROSPECTIVE-GATE.md §29.6`

### 29.7 M&P-Discount-Gate — Post-Publication-Decay (McLean & Pontiff 2016, B25)
Externe In-sample-Claims × **0,42**-Discount vor §29.4-Hurdle. NICHT auf eigenes `score_history.jsonl` (post-publication forward-only seit 17.04.2026). Aktivierung: 2028-04-01 ODER erste DEFCON-Parameter-Variation. → `RETROSPECTIVE-GATE.md §29.7`

### 29.8 Aktivierungs-Reihenfolge bei Review 2028
§29.5 → §29.1 → §29.2 → §29.3 → §29.6 → §29.7. → `RETROSPECTIVE-GATE.md §29.8`

### 29.9 Rückverweise
- §18 Sync-Pflicht → §29.5 Sin #2 (Look-Ahead)
- §27 Scoring-Hygiene → §29.4 t-Hurdle
- §28 Migration-Workflow → §29.1 PBO + §29.5 Seven-Sins + §29.7 M&P-Discount
- §30 Live-Monitoring → §29.3 Half-Life (ab Phase 4)
- §4 Befunde-Router → `meta-gate`-Befunde (B15, B16, B17, B18, B19, B20, B25) → §29-Layer (B25 → §29.7)

---

## 30. Live-Monitoring & Cadence

> **Status:** `[AKTIV seit 19.04.2026]` für MSFT CapEx/OCF-FLAG. Weitere Faktor-Klassen nur nach Applied-Learning-Re-Review.

Monatliche Refresh-Pflicht für **aktive Investment-FLAGs** zwischen Earnings-Terminen. Wissenschaftliche Basis: Flint-Vermaak 2021 — Investment-Faktor-Half-Life ≈ 1 Monat. Earnings-Trigger-Cadence (~3M) ist zu träge, wenn ein Investment-Signal bereits ausgelöst wurde.

### 30.1 Trigger-Definition

**"Aktiver FLAG"** (R1 pflicht) = binär ausgelöst in `05_Archiv/backtest-ready/flag_events.jsonl` ohne nachfolgenden `resolve`-Event.

**"Schema-Watch (nicht FLAG-aktiv)"** (R1 NICHT automatisch) = schema-getriggert per FLAG_RULES, aber bewusst nicht aktiviert (z.B. TMO fcf_trend_neg FY25: WC-Delta erklärt FCF-Rückgang, kein struktureller Trend). **Kein aktiver FLAG, kein R1, kein flag_events-Pfad.** Schema-Watch ist semantisch separat von PORTFOLIO.md "Aktive Watches" (= allgemeine Beobachtungsnotizen, seit 00_Core Hub-Split aus STATE.md migriert).

**Drei-Ebenen-Disambiguierung:** (1) "Aktiver FLAG" (§30, Monthly-Refresh pflicht, flag_events.jsonl-Trigger) ≠ (2) "Schema-Watch" (schema-getriggert-aber-nicht-aktiviert, kein flag_events) ≠ (3) PORTFOLIO.md "Aktive Watches" (allgemeine Beobachtungsnotizen, kein FLAG-Pfad).

### 30.2 Aktuelle Scope (Stand 19.04.2026)

| Ticker | Kategorie | §30 Pflicht |
|--------|-----------|-------------|
| MSFT | Aktiver FLAG (CapEx/OCF 83.6%) | ✅ Monthly-Refresh |
| TMO | Schema-Watch (fcf_trend_neg WC-Noise) | ❌ Nicht automatisch (Q1 23.04. = natürliches Resolve-Gate) |

### 30.3 Monthly-Refresh-Workflow

1. **Trigger-Prüfung:** Aktueller FCF, CapEx, OpCF abrufen (Shibui oder yfinance)
2. **FLAG-Re-Evaluation:** Threshold-Check gegen FLAG_RULES — hält FLAG? Auflösung?
3. **FLAG-Event append** bei Zustandsänderung: `archive_flag.py resolve` oder erneuter `trigger`. **Nur forward-datierte Events (Refresh-Datum = Event-Datum), kein Backfill ohne explizite Kennzeichnung** (§29.5 Sin #2 Look-Ahead-Prevention).
4. **CORE-MEMORY §5:** Zwischenupdate mit FLAG-Zustand
5. **Kein Re-Score** der Ticker-Gesamt-DEFCON-Bewertung — nur Investment-Block-Observation. **FLAG-Events ändern nur FLAG-Status, niemals Score-Komponenten/-gewichte/-penalties.**

### 30.4 Constraints (Applied-Learning-Wächter)

- **Keine Auto-Rescore** — §30 prüft nur bestehende FLAG-Trigger, keine neue Punkte-Logik
- **Keine Ausweitung** auf andere Faktor-Klassen (Quality/Value/Momentum) ohne Applied-Learning-Re-Review — Re-Review-Entscheidung **dokumentiert in CORE-MEMORY §5** als Lektion
- **Ausweitung auf andere Ticker** innerhalb Investment-Klasse zulässig, sobald neue aktive Investment-FLAGs entstehen
- **Keine Score-Änderung via §30** — FLAG-Events ändern nur FLAG-Status, nie Score-Komponenten oder Gewichte

### 30.5 Wissenschaftliche Fundierung

- [[Flint-Vermaak-2021-Decay]] — Investment-Half-Life ~1M
- [[Factor-Information-Decay]] — Operative Konsequenzen
- **Rückverweis:** §29.3 (Temporal-Konsistenz-Gate) — wissenschaftlicher Anker

---

## 33. Skill-Self-Audit-Gate (Anti-Creep für KG/RAG/Agentic-Architekturen)

> **Status:** `[AKTIV seit 2026-04-20]` für zukünftige Architektur-Erweiterungen. **Nicht retroaktiv** — bestehende Skills (insider-intelligence, dynastie-depot, backtest-ready-forward-verify, quick-screener, non-us-fundamentals) bleiben unberührt.
>
> **Numerierung:** §§31-32 reserviert für Track 5b Macro-Regime-Filter und Track 5a EDGAR-Skill-Promotion (nicht ausgeführt). §33 jetzt als Phase-1b-Paper-Ingest-Konsequenz.

Systemischer Gate vor jeder neuen Skill-Erweiterung in Richtung Knowledge-Graph-Extraction, Uncertainty-Aware-Retrieval (Bayesian RAG) oder Agentic-Reflection-Pattern. Wissenschaftliche Basis: B19-B24 (Phase-1b-Ingest 2026-04-20) + Synthesis [[Knowledge-Graph-Architektur-Roadmap]] v0.1.

**Scope — gilt bei jedem Proposal für:**
- Knowledge-Graph-Extraktion aus unstrukturierten Dokumenten (10-K MD&A, Earnings-Transkripte, Analyst-Reports)
- LLM-basierte Retrieval-Augmented-Generation mit Unsicherheits-Quantifizierung (MC-Dropout, Bayesian RAG)
- Agentic-Reflection-Loops (Critic-Corrector-Pattern) in Scoring/Analyse
- DPO-Alignment oder vergleichbare Preference-Optimization für Sentiment-Blocks
- Alles, was über heutige API/XML-Direkt-Parsing-Architektur hinausgeht

**Nicht-Scope:**
- Scoring-Parameter-Änderungen (→ §28 Migration-Workflow)
- Daten-Quellen-Ergänzungen (→ §8 Datenquellen-Logik)
- Runtime-Optimierungen (→ memory `feedback_correctness_over_runtime.md`)

### 33.1 Gate 1 — Sinnhaftigkeits-Check

Vor Architektur-Erweiterung schriftlich begründen:

1. **Konkrete Frage, die heute nicht beantwortbar ist?** — Valide: "Welche Satelliten haben Zulieferer-Exposure zu TSMC?" (nur via Multi-Hop-Cross-Entity-Query). Invalide: "Könnte vielleicht nützlich sein für Cross-Reference."
2. **Wiederkehrender Bedarf?** — Einmalige Ad-hoc-Frage rechtfertigt keine Infrastruktur-Investition.
3. **Kein API-/XML-Ersatz möglich?** — Yahoo/Shibui/SEC-EDGAR liefern strukturierte Daten; dann API, nicht KG.

### 33.2 Gate 2 — Operationalisierungs-Check

1. **Self-hosted-Capability verfügbar?** — Bayesian RAG braucht Dropout-fähige Embedding-Modelle (Tavily/OpenAI-APIs sind raus). KG-Extraktion braucht LLM-Inferenz-Budget 2-3×/Chunk.
2. **Evaluation-Plan definiert?** — LLM-as-a-Judge-Pattern + CheckRules + Entropy-Monitor (B22 Labre). Ohne Eval-Plan keine Adoption.
3. **Maintenance-Budget realistisch?** — KG braucht Re-Extraction bei jedem neuen Filing (quarterly/annual) + Schema-Evolution. Bayesian RAG braucht Embedding-Re-Training-Cadence.

### 33.3 Gate 3 — Anti-Over-Engineering-Check

1. **Codex-Review Pflicht** (memory `feedback_codex_over_advisor.md`): Jede Architektur-Erweiterung braucht externe Bestätigung gegen Own-Bias ("LLM-Hype-FOMO").
2. **3-Monats-Observation-Period:** Vor Produktions-Adoption 3 Monate Parallelbetrieb mit bestehender Architektur.
3. **Rollback-Plan:** Jede Erweiterung muss ohne Daten-/State-Verlust zurücknehmbar sein.

### 33.4 Decision-Output

Jeder Gate-Durchgang endet mit einer von drei Entscheidungen:

- **ADOPT:** Alle 3 Gates grün, Codex-Review PASS. Implementation via §28 Migration-Workflow.
- **DEFER:** Mindestens ein Gate conditional/blockierend. Proposal in [[Knowledge-Graph-Architektur-Roadmap]] als `future-arch`-Szenario archivieren mit Re-Review-Datum.
- **REJECT:** Sinnhaftigkeits-Check (Gate 1) negativ. Proposal abgeschlossen; nicht wieder aufrollen ohne neue Evidenz.

### 33.5 Dokumentation

Jeder §33-Durchgang wird geloggt in:
- **CORE-MEMORY §5** als Lektion (Datum, Proposer, Decision, Rationale)
- **[[Knowledge-Graph-Architektur-Roadmap]]** als Szenario-Eintrag (Anhang Versions-Historie)

### 33.6 Beispiel-Anwendung (Phase-1b 2026-04-20)

Drei Szenarien wurden bei Paper-Ingest evaluiert:

| Szenario | Gate 1 | Gate 2 | Gate 3 | Decision |
|----------|--------|--------|--------|----------|
| Form-4 Insider-Daten via KG | ❌ (XML genügt, Schema stabil) | — | — | **REJECT** |
| 10-K-KG für Cross-Entity-Queries | ⚠️ (hypothetisch, kein akuter Bedarf) | ⚠️ (Budget unklar, Eval-Plan offen) | ⚠️ (3M-Period nicht gestartet) | **DEFER** (frühestens 2027+) |
| Morning-Briefing via Bayesian RAG | ✅ (Quality-Signal wertvoll) | ❌ (Tavily-API erlaubt kein MC-Dropout) | — | **DEFER** (bei Self-hosted-Embedding-Wechsel) |

### 33.7 Rückverweise

- **§28.1 Step 1** (Paper/Evidence-Check) — §33-Gates komplementär zu §28 für Skill-Architektur-Wechsel (nicht Scoring-Parameter)
- **§29.5 Regime-Audit-Addendum** (B19 FINSABER) — Skill-Self-Audit-Dimension
- **Status-Matrix** in [[Wissenschaftliche-Fundierung-DEFCON]] §Status-Matrix — `future-arch`-klassifizierte Befunde werden nur über §33 bewertbar
- **`feedback_codex_over_advisor.md`** — Codex-Review-Pflicht aus Gate 3.1

Quelle: [[Knowledge-Graph-Architektur-Roadmap]] / [[Arun-et-al-2025-FinReflectKG]] / [[Labre-2025-FinReflectKG-Companion]] / [[Ngartera-Nadarajah-Koina-2026-Bayesian-RAG]] / [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] / [[Iacovides-Zhou-Mandic-2025-FinDPO]]

---
*🦅 INSTRUKTIONEN.md v1.13 (§12 → §18-Pointer · §17 v2.1 backtest-ready-forward-verify-Programmatic-Ausnahme · §18 v2.1 config.yaml im Score-Event-Set · §26.4 Wording-Fix) | Dynastie-Depot v3.7 / Skill-Paket v3.7.3 | Stand: 25.04.2026*

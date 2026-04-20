# ⚙️ INSTRUKTIONEN.md — Handlungsanweisungen & Skill-Guidance
**Version:** 1.11 (§28-30 Migration + Retrospective-Gate + Live-Monitoring) | **Stand:** 19.04.2026
> Dieses Dokument beschreibt das WIE — User-Workflows, Befehle, Meta-Regeln.
> Scoring-Technik → [SKILL.md](../01_Skills/dynastie-depot/SKILL.md) | Strategie → KONTEXT.md | Gedächtnis → CORE-MEMORY.md

---

## 1. Befehls-Übersicht

| Befehl | Funktion | Dauer |
|--------|----------|-------|
| `!Analysiere [TICKER]` | 100-Punkte-DEFCON-Vollanalyse | ~20–25 min |
| `!CAPEX-FCF-ANALYSIS [TICKER] [NAME]` | Excel-Tiefenanalyse, 6 Sheets | ~25–30 min |
| `!Rebalancing` | Sparplan-Drift-Check + Vorschlag | ~10 min |
| `!QuickCheck [TICKER\|ALL]` | Ampel-Check, kein Deep Dive | ~3–5 min |
| `!Briefing` | Manuelles Morning Briefing (Kurs-Check, FLAGs, Earnings) | ~3-5 min |

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

**Single Source of Truth:** Die kanonische **Status-Matrix** in `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` §Status-Matrix klassifiziert jeden wissenschaftlichen Befund (aktuell B1–B24, jeder zukünftige Befund BxN) mit einem von vier Status-Labels. §4 ist **nur der Router** — Befund-Content wird nicht hier dupliziert.

| Status | Aktion in !Analysiere |
|--------|-----------------------|
| `active-scoring` | **Pflicht-Anwendung** im zugehörigen DEFCON-Block; Nennung im Output-Block "Befunde angewendet" (SKILL.md-Template) |
| `meta-gate` | **Nicht verwenden** in per-Ticker-Analyse — feuert ausschließlich bei Migration (§28), Retrospective (§29), Skill-Self-Audit (§33) |
| `design-rejected` | **Nicht reaktivieren** — bei Rückfrage "warum fehlt X?" Rejection-Begründung aus Status-Matrix zitieren (nicht ad-hoc einführen) |
| `future-arch` | **Keine Adoption im aktiven Scoring** — Bewertung ausschließlich via §33 Skill-Self-Audit-Gate |

**Pflicht-Abfolge bei jedem Scoring-Start:**

1. **Status-Matrix lesen** (Synthesis-Link oben) — verifizieren, welche Befunde `active-scoring` sind und welchen DEFCON-Block sie adressieren.
2. **Ticker-Befunde-Mapping**: Aus den `active-scoring`-Befunden alle identifizieren, die für diesen Ticker substantiv greifen (z.B. B4 Moat-Quellen greift nur bei Ticker mit nicht-trivialem Moat-Rating; B6 Quality-Trap greift nur wenn Wide Moat + teure Bewertung kombiniert vorliegen).
3. **B10 Chain-of-Thought**: Vor der Punktvergabe pro DEFCON-Block die zutreffenden Befunde durchdenken. Reasoning vor Score, nicht Score vor Reasoning.
4. **Output-Block "Befunde angewendet"** pro DEFCON-Block die angewandten Befund-IDs listen (SKILL.md-Template — reine Transparenz, kein Score-Impact).

**Neue Befunde (B25+):** Werden in der Synthesis-Matrix klassifiziert, nicht in §4 dupliziert. §4 bleibt Router, wächst nicht mit neuen Papers mit.

### Scoring-Skalen, DEFCON-Schwellen, FLAGs

> **Alle Scoring-Details → [SKILL.md](../01_Skills/dynastie-depot/SKILL.md) §Scoring-Skalen / §DEFCON-Schwellenwerte / §FLAG-Regeln**
>
> Dort verbindlich: Block-Gewichtung (50/20/10/10/10), Detailskalen (Fwd P/E, P/FCF, CapEx/OCF, ROIC, FCF-Yield, Bilanz, OpM TTM), Quality-Trap-Interaktion v3.7, Fundamentals-Cap 50, Bonus-Metriken, DEFCON-Schwellen-Tabellen (Neueinstieg + Bestand), automatische FLAGs.

---

## 5. Sentiment-Scoring (v3.7-Kalibrierung)

> **Detailskalen → [SKILL.md §Sentiment (10 Punkte)](../01_Skills/dynastie-depot/SKILL.md)**
>
> Strong-Buy-Ratio / Sell-Ratio / PT-Upside — v3.7-Kalibrierung (B11: Crowd-Consensus-Malus, Extrem-Consensus-Warnung).

---

## 6. Insider-Scoring — Pflichtregeln

> **Scoring-Skala + Cashless-Exercise-Ausnahme → [SKILL.md §Insider (10 Punkte)](../01_Skills/dynastie-depot/SKILL.md)**
>
> Kurz: OpenInsider HEILIG, 10b5-1 "M"-Check bei Verkäufen >$20M, Fallback SEC EDGAR Form 4.

---

## 7. Kalibrierungsanker (vor jeder Analyse pflichtlesen!)

| Ticker | Score | DEFCON | Lektion |
|--------|-------|--------|---------|
| AVGO | 85 | 🟢 4 | Fabless-Modell = CapEx/OCF <15%, Referenz für Top-Score |
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

**Gewichte:** D4/D3 (kein 🔴 FLAG) = 1.0 | D2 (kein 🔴 FLAG) = 0.5 | D1 / 🔴 FLAG = 0.0

**Formel:** `Einzelrate = Aktien-Budget (285€) / Σ Gewichte × Eigengewicht`

**Rechenbeispiel (aktueller Stand 17.04.2026: 8× D4/D3 + 1× D2 aktiv, 2× 🔴 eingefroren):**
- Nenner = (8 × 1.0) + (1 × 0.5) = **8.5**
- D4/D3-Einzelrate = 285€ / 8.5 × 1.0 = **33,53€**
- D2-Einzelrate (TMO) = 285€ / 8.5 × 0.5 = **16,76€**
- 🔴/D1-Rate (MSFT, APH) = **0€**
- Summencheck: 8 × 33,53€ + 16,76€ + 0 + 0 = 285€ ✓

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

Nach **jeder** `!Analysiere`-Analyse, Sparplan-Änderung oder FLAG-Update:
- Score + DEFCON in `mainconfig.md` aktualisieren
- FLAGS setzen oder aufheben
- Watchlist-Status aktualisieren
- Termine eintragen
- Neue Version hochladen

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

## 17. Skill-Hierarchie & Aktivierungslogik (v2.0 — 08.04.2026)

**Grundregel:** `dynastie-depot` ist der Monolith. Innerhalb von `!Analysiere`
werden **keine weiteren Skills geladen** — alle Module (defeatbeta, Shibui,
insider_intel.py, WebSearch) werden direkt als Tool-Calls genutzt.
Jeder zusätzliche Skill-Load kostet Token und verliert DEFCON-Kontext.

### Wann wird welcher Skill eigenständig aktiviert?

| Befehl | Skill | Bedingung |
|--------|-------|-----------|
| `!QuickCheck [TICKER\|ALL]` | `quick-screener` | Stufe-0-Vorfilter oder monatlicher Check |
| `!EarningsPreview [TICKER]` | `earnings-preview` | 48h vor Earnings |
| `!EarningsRecap [TICKER]` | `earnings-recap` | 48h nach Earnings |
| `!EarningsCalendar` | `earnings-calendar` | Wöchentlicher Überblick |
| `!InsiderScan` | `insider-intelligence` | Standalone-Scan ohne !Analysiere |
| Portfolio-Risk-Audit | `03_Tools/portfolio_risk.py` | Quartalsweise manuell (Correlation / Component Risk / Stress-Test) — kein Skill |
| Dokument-Konflikt / 10-K-Text | `sec-edgar-skill` | Eskalations-Fallback |

### Warum kein Skill-Chaining innerhalb !Analysiere?

Ein Skill-Load liest die jeweilige SKILL.md ohne Kenntnis von:
- DEFCON-Scoring-Skalen und Kalibrierungsankern
- FLAG-Logik und deren Überschreibungsregeln
- config.yaml (aktuelle Positionen, DEFCON-Status)
- Kontext der laufenden Analyse (welcher Ticker, welche Daten schon geladen)

→ Ergebnis wäre generische Analyse statt kontextbewusster DEFCON-Score.
→ Vollständige Dokumentation: `01_Skills/dynastie-depot/PIPELINE.md`

---

## 18. Sync-Pflicht: log.md + CORE-MEMORY.md + Faktortabelle.md + STATE.md + score_history.jsonl (+ flag_events.jsonl)

**Trigger:** Score/FLAG-Änderung, neue Analyse, Systemänderung, Sparraten-Änderung.

**Reihenfolge (alle sechs, immer):**
1. `log.md` (Vault) — technisches Protokoll
2. `CORE-MEMORY.md` (00_Core) — strategisches Gedächtnis (Section 1: Analysen, Section 3: FLAGs, Section 4: Scores)
3. `Faktortabelle.md` — Score + FLAG aktualisieren. Bei FLAG-Änderung: config.yaml manuell sync.
4. `STATE.md` — Portfolio-Tabelle + Watches + Trigger-Liste (Single-Entry-Point seit 17.04.2026).
5. `score_history.jsonl` (05_Archiv/) — append-only Score-Archiv via `archive_score.py` (jedes `!Analysiere`; vollanalyse/delta/rescoring). SKILL.md Schritt 7. **Orchestriert via Skill `backtest-ready-forward-verify` (seit 19.04.2026, v3.7.2):** Pipeline-Disziplin (Freshness / Tripwire / §28.2 Δ-Gate / Dry-Run / Append / git add) mechanisch durchgesetzt. 6-File-Sync-Pflicht unverändert.
6. `flag_events.jsonl` (05_Archiv/) — append-only FLAG-Event-Log via `archive_flag.py` (nur bei FLAG-Trigger oder Resolution). SKILL.md Schritt 6b.

**Nie nur eine der sechs Dateien aktualisieren.** Verlässt STATE.md den aktuellen Stand → Session-Start unbrauchbar. Verpasst JSONL-Append → irreversibler Historie-Verlust für 2028-Backtest-Review.

**Wissenschaftlicher Anker:** Die Point-in-Time-Persistenz aller sechs Dateien schützt vor §29.5 Sin #2 (Look-Ahead Bias). Jeder Record muss zum Zeitpunkt der Daten-Sichtung geschrieben werden, nicht rückwirkend. → §29.5 / [[Seven-Sins-Backtesting]]

**Änderungsprotokoll:**
- v1.5 → v1.6 (2026-04-17): Erweitert auf 6 Dateien durch Backtest-Ready Infrastructure (§26).
- v1.6 → v1.7 (2026-04-19): Schritt 5 (score_history.jsonl) wird via Skill `backtest-ready-forward-verify` orchestriert — Pipeline-Kapsel statt Inline-CLI-Call in dynastie-depot Schritt 7.

---

## 19. Daten-Update-Klassen (wissenschaftlich fundiert)

| Klasse | Trigger | Frequenz | Felder | Halbwertszeit |
|--------|---------|----------|--------|---------------|
| **A** | Quartalsweise | ~90 Tage | FCF, ROIC, GM, Debt/EBITDA | 18–33 Monate |
| **B** | Earnings-getriggert | 14 Tage nach Earnings | Alle Fundamentals, Score, Guidance | 60% Verfall Monat 1 |
| **C** | Event-getriggert | Sofort | Insider >$20M, Moat-Downgrade, Makro >50 Bps | — |
| **D** | Monatlich | 1×/Monat | Sentiment, Short Interest | — |

Basis: SSRN 2022. 80% DEFCON-Score >12 Monate Halbwertszeit.

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

## 22. Sparplan-Formel (aktuell 17.04.2026, v3.7)

**Formel:** `Einzelrate = 285€ / Σ Gewichte × Eigengewicht`
**Gewichte:** D4/D3 (kein 🔴)=1,0 | D2 (kein 🔴)=0,5 | D1/🔴 FLAG=0,0

| Position | Score | DEFCON | Gewicht | Rate |
|----------|-------|--------|---------|------|
| AVGO | 84 | 🟢 4 | 1,0 | 33,53€ |
| ASML | 68 | 🟡 3 | 1,0 | 33,53€ |
| MSFT | 59 | 🟠 2 | 0,0 | 0€ (🔴 FLAG) |
| RMS | 68 | 🟢 4 | 1,0 | 33,53€ |
| VEEV | 74 | 🟢 4 | 1,0 | 33,53€ |
| SU | 69 | 🟢 4 | 1,0 | 33,53€ |
| BRK.B | 75 | 🟢 4 | 1,0 | 33,53€ |
| V | 86 | 🟢 4 | 1,0 | 33,53€ |
| TMO | 63 | 🟠 2 | 0,5 | 16,76€ |
| APH | 63 | 🟡 3 | 0,0 | 0€ (🔴 FLAG) |
| COST | 69 | 🟢 4 | 1,0 | 33,53€ |

**Summe:** 8×1,0 + 1×0,5 = 8,5 | **Volle Rate:** 33,53€ | **D2-Rate (TMO):** 16,76€ | **Eingefroren (MSFT, APH):** 0€
**Check:** 8×33,53 + 1×16,76 = 268,24 + 16,76 = 285,00€ ✓

---

## 23. Tariff Exposure Scoring

**Quelle:** 10-K "Geographic Revenue" + Manufacturing Locations
**Malus:** -1 Punkt Fundamentals bei >20% Revenue CN/TW/MY/TH/VN
**FLAG:** >35% → 🔴 FLAG aktiv, -3 Punkte, Sparrate 0€

---

## 24. Morning Briefing (Scheduled Trigger v2.1)

**Trigger-ID:** `trig_01PyAVAxFpjbPkvXq7UrS2uG`
**Frequenz:** Taeglich 10:00 Uhr MESZ (Cron `0 8 * * *` UTC, ~10-15 Min Jitter)
**Modell:** claude-sonnet-4-6 | **Repo:** github.com/tobikowa90-hub/dynastie-depot
**Token-Budget:** ~12-18k/Tag (Mo-Fr), ~2-3k/Tag (Sa-So)
**Prompt-Datei:** `03_Tools/morning-briefing-prompt-v2.md` (Single Source of Truth)

**Scope:** 11 Satelliten + 5 Ersatzbank mit Score (MKL, SNPS, SPGI, RACE, ZTS) = 16 Symbole

**Datenquellen (2 Tiers):**

| Tier | Symbole | Quelle | Status |
|------|---------|--------|--------|
| Shibui | ASML, AVGO, MSFT, TMO, VEEV, V, APH, COST, MKL, SNPS, SPGI, RACE, ZTS (13) | `stock_data_query` P1-Pattern mit `g.code IN(...)` | ✅ Live |
| Yahoo curl | BRK.B (`BRK-B`), RMS (`RMS.PA`), SU (`SU.PA`) (3) | `curl` in Bash | ❌ HTTP 403 — Yahoo blockiert Cloud-IPs. V3-Backlog. |

**Critical Guards im Prompt:**
- 🚨 SUNCOR-TRAP: Shibui `code='SU'` = Suncor Energy. Schneider Electric ist NICHT in Shibui. Nie 'SU' in Shibui-Query.
- 🚨 BERKSHIRE-GAP: BRK.B ist nicht in Shibui indexiert (bestaetigt).
- 🚨 HERMES-GAP: RMS ist nicht in Shibui.
- 🚨 ANTI-HALLUCINATION: Bei fehlenden Daten exakter Fehlertext, keine erfundenen Gruende.
- 🚨 KEIN RETRY: Keine Symbol-Varianten bei Query-Fehlschlag.

**Schwellenwerte:**
| Trigger | Schwelle | Empfehlung |
|---------|----------|------------|
| Kurs-Drop | >10% seit Score | !QuickCheck |
| Kurs-Drop | >20% seit Score | !Analysiere |
| Earnings | <7 Tage | Countdown + !QuickCheck |
| Score-Alter | >90 Tage | Update empfohlen |
| Score-Alter | >180 Tage | !Analysiere dringend |

**Manueller Trigger:** `!Briefing` (identischer Output) oder Desktop App → Routines → Jetzt ausfuehren

**Voraussetzung:** Faktortabelle muss aktuell sein (Sync-Pflicht §18). GitHub-Repo muss gepusht sein (`!SyncBriefing`).

**API-Update-Regel (KRITISCH):** RemoteTrigger-Update ersetzt `ccr`-Objekt KOMPLETT (kein Merge). Immer alle 3 Felder (`environment_id`, `session_context`, `events`) zusammen senden. JSON-Nesting: `parent_tool_use_id`, `session_id`, `type`, `uuid` gehoeren auf **data-Level**, NICHT in message.

**Known Limitations v2.1:**
- BRK.B/RMS/SU-Kurse nicht verfuegbar (Yahoo 403 von Cloud-IPs). Zeigt ehrlich "n.v.".
- Push-Notifications: Kein Routines-Toggle in Claude iOS App. Wartet auf Anthropic-Update.
- `RemoteTrigger run` API-Endpoint ist Noop fuer Cron-basierte Trigger — manuell nur via Desktop App "Jetzt ausfuehren".

---

## 25. Briefing-Sync Shortcuts (GitHub ↔ Local)

**Problem:** Der 10:00-Morning-Briefing-Trigger läuft als Remote-Session auf claude.ai und liest `00_Core/` aus dem **GitHub-Repo** — nicht aus dem lokalen Arbeitsverzeichnis. Jede lokale Änderung an Faktortabelle/CORE-MEMORY/SESSION-HANDOVER muss vor 10:00 gepusht sein, sonst analysiert der Trigger veraltete Daten.

### `!BriefingCheck`

**Zweck:** Schneller Vorab-Check: *Liest der Trigger heute aktuelle Daten?*

**Schritte (Claude führt aus):**
1. `git fetch origin main --quiet`
2. `git diff --stat origin/main -- 00_Core/` — zeigt welche Briefing-Quellen lokal vom Remote abweichen
3. Wenn Unterschiede: Liste ausgeben + Empfehlung `!SyncBriefing`
4. Wenn keine Unterschiede: `✅ Trigger liest aktuellen Stand — kein Push nötig`

**Ausgabeformat:**
```
BriefingCheck [Datum HH:MM]
  Faktortabelle.md     [X Zeilen divergent] / [✅ identisch]
  CORE-MEMORY.md       [X Zeilen divergent] / [✅ identisch]
  SESSION-HANDOVER.md  [X Zeilen divergent] / [✅ identisch]
Empfehlung: [!SyncBriefing ausführen] / [Kein Handeln nötig]
```

### `!SyncBriefing`

**Zweck:** Briefing-relevante `00_Core/`-Änderungen ins Repo pushen — mit Review-Gate.

**Schritte (Claude führt aus):**
1. `git status --short 00_Core/` — welche Dateien modified
2. `git diff 00_Core/` — vollständigen Diff anzeigen
3. **Review-Gate:** User bestätigt *explizit* mit `ja`/`push` bevor committed wird — nie automatisch
4. Nach Bestätigung: `git add 00_Core/Faktortabelle.md 00_Core/CORE-MEMORY.md 00_Core/SESSION-HANDOVER.md 00_Core/INSTRUKTIONEN.md`
5. `git commit -m "Briefing-Sync: <kurze Begründung aus Diff abgeleitet>"`
6. `git push origin main`
7. Verifikation: `git log -1 --format="%h %s"` ausgeben

**Wichtig:**
- **Nur `00_Core/` wird synchronisiert** — keine Skills, Tools, Vault
- **Nie `git add .`** — Pfade explizit
- **Review-Gate ist Pflicht** — kein Auto-Commit
- **Commit-Message-Schema:** `Briefing-Sync: <Inhalt>` (z.B. `Briefing-Sync: RMS 71→69, Sparraten-Logik D3=voll`)

### Reminder (Scheduled Task `briefing-sync-reminder`)

- **Frequenz:** Werktags 09:50
- **Verhalten:** Prüft `00_Core/` auf uncommitted/unpushed Änderungen. Bei Treffern: Reminder-Output für nächste Claude-Code-Session. Kein Auto-Push.
- **Warum 09:50:** 10 Minuten Puffer vor Remote-Trigger um 10:00
- **Manueller Start:** `scheduled-tasks → briefing-sync-reminder → Run now`

### Wann `!SyncBriefing` nötig ist

- Nach jeder DEFCON-Analyse (Score/FLAG-Änderung)
- Nach `CORE-MEMORY.md`-Einträgen (institutionelles Gedächtnis)
- Nach Sparraten-Änderungen in `SESSION-HANDOVER.md`
- Spätestens abends vor Session-Ende, wenn Score-Updates vom Tag noch nicht gepusht sind

### Wann **kein** Push nötig ist

- Reine Skill-/Tool-/Vault-Änderungen (`01_Skills/`, `03_Tools/`, `07_Obsidian Vault/`) — Briefing liest diese nicht
- Work-in-Progress-Analysen (Score noch nicht final) — erst nach Abschluss pushen

---

## 26. Archiv-Sync (Backtest-Ready-Pipeline)

**Trigger:** Nach jeder `!Analysiere` (Vollanalyse/Delta/Rescoring) UND bei jedem FLAG-Trigger oder FLAG-Resolution.

**→ CLI-Usage + Exit-Codes:** [`03_Tools/backtest-ready/README.md`](../03_Tools/backtest-ready/README.md)

### Workflow (4 Schritte)

1. **Score-JSON generieren** (SKILL.md Schritt 7) — `ScoreRecord` gemäß `schemas.py`. Pflichtfelder: `schema_version: "1.0"`, `record_id: YYYY-MM-DD_TICKER_TYP`, `source: "forward"`, `defcon_version` aktuell, `score_datum` (heute, max. 3 Tage zurück), vollständige 5-Block-`scores` + `score_gesamt` + `defcon_level`, `kurs`, `market_cap`, `flags`, `metriken_roh`, `quellen`.
2. **Archivieren** — `archive_score.py --file <tempfile.json>`. Keine Ausnahme, kein Record darf verloren gehen.
3. **FLAG-Events archivieren** (nur bei Trigger/Resolution, SKILL.md Schritt 6b) — `archive_flag.py trigger` oder `resolve`. Schwellen aus `FLAG_RULES` automatisch.
4. **Git-Commit** — alle sechs Dateien §18 in einem Commit.

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
1. Für alle aktuellen 11 Satelliten durchrechnen: Block-Score + potenzieller Bonus.
2. Wenn ≥3 Top-Namen am Cap hängen bleiben → Bonus entweder ins Block-Cap integrieren oder als Tie-Breaker statt Score-Boost.
3. Dokumentieren in Scoring-Lektionen (CORE-MEMORY §5).

**Präzedenzfall:** v3.7 Fundamentals-Cap 50 — bewusst akzeptiert dass Top-Namen (AVGO 84) weniger Bonus-Headroom haben; dafür Score-Inflation strukturell ausgeschlossen.

### 27.3 Projection-Layer ≠ Wahrheitsquelle

**Regel:** STATE.md, Briefing-Tabellen, Dashboard-Summaries sind **Projektionen** aus State+Narrative — nie selbst als Primärquelle fortschreiben.

**Typische Falle:** STATE.md direkt editieren ohne zuerst Faktortabelle/CORE-MEMORY/score_history.jsonl zu aktualisieren. Ergebnis: Drift zwischen Primär- und Projektions-Layer, Session-Start-Informationen werden unzuverlässig.

**Pflichtreihenfolge bei Änderungen:**
1. Primärquelle zuerst (Faktortabelle.md, CORE-MEMORY.md, score_history.jsonl via archive_score.py).
2. Projektion synchron nachziehen (STATE.md).
3. Kein STATE.md-Edit ohne parallele Primärquellen-Änderung (Ausnahme: reine Layout/Navigation).

**Präzedenzfall:** 17.04.2026 — STATE.md-Einführung begleitet von §18 Sync-Pflicht-Erweiterung (alle sechs Dateien, immer, ein Commit).

### 27.4 Multi-Source-Drift-Check vor "fertig"-Meldung

**Regel:** Vor Abschluss einer Systemänderung **alle Wahrheitsquellen greppen** — config.yaml-Fix allein reicht nie.

**Pflicht-Suchliste:**
- `00_Core/INSTRUKTIONEN.md` (§§)
- `00_Core/CORE-MEMORY.md` (§4 Score-Tabelle, §5 Scoring-Lektionen)
- `01_Skills/dynastie-depot/config.yaml`
- `01_Skills/dynastie-depot/SKILL.md`
- `00_Core/STATE.md`, `Faktortabelle.md`
- `07_Obsidian Vault/.../wiki/entities/satelliten/*.md`
- `03_Tools/Rebalancing_Tool_v3.4.xlsx`, `Satelliten_Monitor_v2.0.xlsx`

**Präzedenzfall:** 18.04.2026 Schema-SKILL-Threshold-Drift — Fix in schemas.py alleine hätte 5 Vault-Pages und beide Tools veraltet zurückgelassen. Kaskaden-Sync war Pflicht.

**Wissenschaftlicher Anker:** Double-Counting-Vermeidung und Bonus-Cap-Check verhindern False-Positives unterhalb §29.4 t-Stat ≥ 3 Hurdle (Harvey/Liu/Zhu). Jede neue Sub-Komponente muss t≥3 erreichen. → §29.4 / [[Aghassi-2023-Fact-Fiction]]

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

Für diese Fälle reicht: Commit + STATE.md-Update + CORE-MEMORY §5 Lektion, keine Step-1-7-Pflicht.

**Präzedenzfall:** 18.04.2026 TMO `fcf_trend_neg`-Disclosure (Option B) — struktureller FLAG ohne Score-Penalty, kein Version-Bump.

**Wissenschaftlicher Anker:** §28.2 Δ-Gate und §28.4 Forward-Verify greifen in die Validation-Ebene ein, die §29 retrospektiv absichert: §29.1 (PBO/CSCV nach Bailey) für Parameter-Variations und §29.5 (Seven-Sins-Pre-Flight) für jeden Migration-Event ab sofort aktiv. → §29.1 / §29.5 / [[Bailey-2015-PBO]] / [[Seven-Sins-Backtesting]]

---

## 29. Retrospective-Analyse-Gate

> **`[FUTURE-ACTIVATION: 2028-04-01]` für §29.1-4 + §29.6. §29.5 Seven-Sins-Gate aktiv bereits jetzt bei Migration-Events.**

Systemischer Gate für jede retrospektive Analyse der `score_history.jsonl` (Strategy-Selection, Parameter-Tuning, Portfolio-Return-Validation). Aktivierung: Review 2028-04-01 ODER erste DEFCON-Parameter-Variation. §28 (Migration-Workflow) ist **komplementär**, nicht konkurrierend: §28 schützt Versions-Sprünge, §29 schützt Retrospective-Auswertungen.

**4-Dimensionen-Gate-Framework** (jede Dimension unabhängig validierbar):

### 29.1 Methoden-Gate — Overfitting (Bailey et al. 2015)

**Regel:** Vor jedem Strategy-Selection/Parameter-Tuning gegen `score_history.jsonl` PBO < 0,05 berechnen via CSCV.

**Implementierung:** `03_Tools/backtest-ready/pbo_cscv.py` bei Aktivierung. S=16 Default (12.780 Logits), N≥10 Trials, T≥2×Modellwahl-Fenster. CRAN R-Package `pbo` als Referenz-Implementierung.

**Komplementär:** walk-forward + k-fold + randomized backtests nach Palomar Ch 8.4 als Cross-Check (keine Ersetzung).

**In-the-Loop-Alternative (Sheppert 2026, B20):** GT-Score Composite-Objective (Performance × Significance × Consistency × Downside-Risk) als **Objective-Function während** Strategy-Selection — komplementär, nicht ersetzend zu PBO. PBO ist Post-hoc-Filter (Kandidat → Test), GT-Score ist In-the-Loop-Objective (Kandidat-Generierung optimiert bereits gegen Anti-Overfitting-Aggregat). Bei DEFCON-Parameter-Tuning ab 2028: beide Layer lauffähig — GT-Score als Tie-Break innerhalb PBO-Kandidatenmenge.

Quelle: [[Bailey-2015-PBO]] / [[PBO-Backtest-Overfitting]] / [[Sheppert-2026-GT-Score]] / [[Composite-Anti-Overfitting-Objective]]

### 29.2 External-Benchmark-Gate (Aghassi et al. 2023)

**Regel:** Aggregierte Satelliten-Portfolio-SR muss im Band der AQR/Ilmanen-Multifaktor-Benchmark liegen (Ilmanen et al. 2021 Century-Dataset). Bei signifikanter Abweichung: Ursache identifizieren (DEFCON-Mapping-Fehler, Selektions-Bias, echter Out-of-Band-Effekt).

**DEFCON-Faktor-Mapping** (Referenz für Benchmark-Auswahl):
- Fundamentals (Fwd P/E, P/FCF) → Value (HMLDEVIL)
- Moat + Quality-Fundamentals → Quality (QMJ) / Defensive (BAB)
- Technicals → Momentum (UMD)
- Insider → non-AQR-Edge, keine Benchmark

**Nicht anwendbar pro Ticker** — AQR-Value-Spread ist Long-Short-Cross-Section-Instrument, nicht Single-Stock.

Quelle: [[Aghassi-2023-Fact-Fiction]] / [[Factor-Investing-Framework]]

### 29.3 Temporal-Konsistenz (Flint & Vermaak 2021)

**Regel:** Score-Cadence muss mit der Faktor-Half-Life des dominanten DEFCON-Block konsistent sein.

| Faktor-Analog | Optimale Cadence | Unsere Cadence | Status |
|---|---|---|---|
| Value | 3-4M | Earnings-Trigger ~3M | ✅ aligned |
| Quality | 4-5M | Earnings-Trigger + jährliche Vollanalyse | ✅ konservativ |
| Momentum | 3M | Earnings-Trigger + Monitor | ✅ aligned |
| Investment | **1M** | Earnings-Trigger (zu träge bei aktiven FLAGs) | ⚠️ Watch |
| Insider | Real-time | OpenInsider | ✅ aligned |

**Investment-Watch:** MSFT-CapEx-FLAG + TMO-fcf_trend_neg sind Investment-Klasse. Bei Review 2028 prüfen, ob Monthly-Fundamentals-Refresh aktiviert werden muss.

Quelle: [[Flint-Vermaak-2021-Decay]] / [[Factor-Information-Decay]]

### 29.4 Neue-Parameter-Gate — Harvey/Liu/Zhu-Hurdle

**Regel:** Jede neue DEFCON-Sub-Komponente (neuer FLAG, Sub-Score, Metrik) muss **t-Stat ≥ 3** erreichen (nicht 2,0). Begründung: 121 unabh. Trials genügen für t=2-False-Positive, 393 für t=3. Academic Finance hat 400+ publizierte Faktoren — die meisten wären bei t≥3 verworfen.

**Aktivierungs-Trigger:** SOFORT (nicht 2028) — prospektiv auf alle zukünftigen DEFCON-Erweiterungen anwendbar. Ergänzt §28.1 Step 1 (Paper/Evidence-Check) um formale Signifikanz-Schwelle.

Quelle: [[Aghassi-2023-Fact-Fiction]] (zitiert Harvey/Liu/Zhu 2016)

### 29.5 Seven-Sins-Pre-Flight-Gate (Palomar 2025 Ch 8.2)

**Regel:** Vor jeder retrospektiven Analyse UND vor jedem Migration-Event (§28) folgende 7-Punkt-Checkliste:

- [ ] **Sin #1 Survivorship Bias:** Reject-Set aus Quick-Screener-Historie rekonstruieren (sonst explizit dokumentieren)
- [ ] **Sin #2 Look-Ahead Bias:** Nur `source=forward` Records, oder Backfill explizit deklariert
- [ ] **Sin #3 Storytelling Bias:** Rationale ex-ante in CORE-MEMORY §5, nicht post-hoc
- [ ] **Sin #4 Overfitting:** → §29.1 PBO<0,05
- [ ] **Sin #5 Turnover & Transaction Cost:** Sparplan-Gebühren + Spread modelliert
- [ ] **Sin #6 Outliers:** COVID 2020, Liberation Day 2026, GFC 2008 explizit behandelt
- [ ] **Sin #7 Asymmetric Pattern & Shorting:** **n.a.** (Dynasty-Depot ist strikt Long-Only)

**Aktivierungs-Trigger:** SOFORT bei Migration-Events. Bei retrospektiven Analysen ab 2028.

Quelle: [[Palomar-2025-Portfolio-Optimization]] / [[Seven-Sins-Backtesting]]

**Regime-Audit-Addendum (B19 FINSABER-Extension, 2026-04-20):**

Ergänzung zu Sin #4 (Overfitting) + Sin #6 (Outliers) bei Migration- und Retrospective-Events. FINSABER zeigt, dass LLM-Backtest-Vorteile unter realistischer Evaluation (20-Jahres-Fenster, 100+ Symbole, Bias-Mitigation) verschwinden und dass Bull/Bear-Subsample-SR-Divergenzen systematisch sind.

- [ ] **Bull/Bear-Subsample-SR-Trennung:** Score-Performance in Bull-Phasen (SPY > 200MA) und Bear-Phasen (SPY < 200MA) getrennt ausweisen. Divergenzen >2σ SR dokumentieren.
- [ ] **Symbol-Breite-Deklaration:** Backtest-Universum explizit benennen. Bei Universen <100 Symbole ("Dynasty-Satelliten-Cluster n=11") keine Skalierungs-Ansprüche formulieren.
- [ ] **Zeitfenster-Deklaration:** Backtest-Zeiträume <5 Jahre als "Proof-of-Concept" einordnen, nicht als strategische Evidenz.

**Aktivierungs-Trigger:** SOFORT bei Migration-Events (identisch mit §29.5-Kern). Skill-Self-Audit-Dimension in §33 adressiert.

Quelle: [[Li-Kim-Cucuringu-Ma-2026-FINSABER]] / [[LLM-Investing-Bias-Audit]] / [[Regime-Aware-LLM-Failure-Modes]]

### 29.6 Portfolio-Return-Metrik-Layer (Palomar 2025 Ch 6)

**Regel:** Bei Aktivierung `risk-metrics-calculation`-Skill (bestehend) gegen `05_Archiv/portfolio_returns.jsonl` (Phase 3, in Aufbau): Sortino/CVaR/Calmar/Max-DD/IR nach Palomar-Ch-6-Formel-Konventionen berechnen.

**Voraussetzung:** portfolio_returns.jsonl-Persistenz ab Q2 2026 aktiv (Phase 3 dieses Plans).

**Aktivierungs-Trigger:** Review 2028-04-01 ODER ≥24 Monate sauberer Return-Serie.

**Interim-Gate:** 2027-10-19 Dry-Run für Data-Quality-Check.

**Composite-Objective-Alignment (B20 GT-Score, 2026-04-20):** Die Downside-Risk-Komponente des GT-Score-Composite-Objectives (Performance × Significance × Consistency × Downside-Risk) ist konzeptuell deckungsgleich mit Palomar Sortino/CVaR/Max-DD — downside-deviation-basierte Risk-Metriken. Bei §29.1/§29.6-Co-Aktivierung (ab 2028-04-01): GT-Score operationalisiert die vier Dimensionen als **In-the-Loop-Objective** während Strategy-Selection; Palomar liefert die mathematische Berechnungs-Konvention für die Einzel-Metrik-Ebene. Gemeinsamer Zweck: Score-Serie gegen Downside-Asymmetrien absichern, nicht nur Mean-Return optimieren.

Quelle: [[Palomar-2025-Portfolio-Optimization]] / [[Palomar-Methods-Reference]] / [[Sheppert-2026-GT-Score]] / [[Composite-Anti-Overfitting-Objective]]

### 29.7 Aktivierungs-Reihenfolge bei Review 2028

1. §29.5 Sünden-Pre-Flight (Sin #1-#6) — wenn nicht alle grün: Stopp
2. §29.1 Methoden-Gate (PBO/CSCV, walk-forward Cross-Check)
3. §29.2 External-Benchmark (AQR/Ilmanen-Band)
4. §29.3 Temporal-Konsistenz (Cadence vs. Half-Life)
5. §29.6 Portfolio-Return-Metriken
6. Dann Options A–D aus [[Backtest-Methodik-Roadmap]] anwendbar

### 29.8 Rückverweise

Andere §§ die auf §29-Gates verweisen:
- §18 Sync-Pflicht → §29.5 Sin #2 (Look-Ahead)
- §27 Scoring-Hygiene → §29.4 t-Hurdle
- §28 Migration-Workflow → §29.1 PBO + §29.5 Seven-Sins
- §30 Live-Monitoring → §29.3 Half-Life (ab Phase 4)

---

## 30. Live-Monitoring & Cadence

> **Status:** `[AKTIV seit 19.04.2026]` für MSFT CapEx/OCF-FLAG. Weitere Faktor-Klassen nur nach Applied-Learning-Re-Review.

Monatliche Refresh-Pflicht für **aktive Investment-FLAGs** zwischen Earnings-Terminen. Wissenschaftliche Basis: Flint-Vermaak 2021 — Investment-Faktor-Half-Life ≈ 1 Monat. Earnings-Trigger-Cadence (~3M) ist zu träge, wenn ein Investment-Signal bereits ausgelöst wurde.

### 30.1 Trigger-Definition

**"Aktiver FLAG"** (R1 pflicht) = binär ausgelöst in `05_Archiv/backtest-ready/flag_events.jsonl` ohne nachfolgenden `resolve`-Event.

**"Schema-Watch (nicht FLAG-aktiv)"** (R1 NICHT automatisch) = schema-getriggert per FLAG_RULES, aber bewusst nicht aktiviert (z.B. TMO fcf_trend_neg FY25: WC-Delta erklärt FCF-Rückgang, kein struktureller Trend). **Kein aktiver FLAG, kein R1, kein flag_events-Pfad.** Schema-Watch ist semantisch separat von STATE.md "Aktive Watches" (= allgemeine Beobachtungsnotizen).

**Drei-Ebenen-Disambiguierung:** (1) "Aktiver FLAG" (§30, Monthly-Refresh pflicht, flag_events.jsonl-Trigger) ≠ (2) "Schema-Watch" (schema-getriggert-aber-nicht-aktiviert, kein flag_events) ≠ (3) STATE.md "Aktive Watches" (allgemeine Beobachtungsnotizen, kein FLAG-Pfad).

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
*🦅 INSTRUKTIONEN.md v1.12 (§4 Router-Umbau + §2 Befunde-Check + §29.5/.6 B19/B20-Extensions + §33 Skill-Self-Audit) | Dynastie-Depot v3.7 | Stand: 20.04.2026 Phase-2-Complete*

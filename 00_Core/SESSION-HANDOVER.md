# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 16.04.2026 | **Für:** Neue Cowork-Session

---

## ▶️ TRIGGER

```
Session starten
```

---

## 📋 Übergabe-Kontext

Bitte lies zuerst die vier Core-Dateien wie gewohnt (CORE-MEMORY, KONTEXT, INSTRUKTIONEN, Faktortabelle).
Danach gilt folgender Kontext aus der letzten Session:

---

## ✅ PRIO 1 ERLEDIGT — DEFCON v3.5 implementiert (16.04.2026)

Das Scoring-System-Audit ist abgeschlossen. DEFCON v3.5 ist live.

**Audit-Ergebnis:** 5×A, 1×B (PT-Upside Double-Counting — gefixt), 1×C (Gewichtsanpassung zurückgestellt auf 6 Monate)
**v3.5-Fix:** PT-Upside aus Technicals entfernt, Relative Stärke vs S&P500 als 0-3 Scored Metric (war: ±1 Tiebreaker)
**Anker-Shifts:** AVGO 86→85, SNPS 79→76, TMO 65→62 (⚠️ D3→D2), FICO 70→67, SPGI 77→74, MKL 82 (unverändert)

👉 **Die Satelliten-Queue ist jetzt entsperrt.** Alle Re-Analysen laufen unter v3.5.

---

## 🚀 Offene Analyse-Queue (v3.5 live — ENTSPERRT)

| Priorität | Aufgabe | Kontext |
|-----------|---------|---------|
| 🔴 1 | **!Analysiere MSFT** | Earnings 29.04. — FLAG-Review CapEx/OCF (zuletzt 65.3%). Bei <60% → FLAG auflösen, D3 volle Rate aktivieren |
| 🔴 2 | **!Analysiere AVGO** | Tariff-Exposure MY/TH ~35% Grenzfall. Insider-FLAG-Pflichtcheck: OpenInsider-Spalte „X"/„M" manuell verifizieren (Post-Vesting wahrscheinlich, aber nicht voreilig auflösen) |
| 🟡 3 | **!Analysiere COST** | Retail, US-lastig, Tariff-Ketteneffekte |
| 🟡 4 | **!Analysiere V** | Kein Tariff-Risiko, Konsumrückgang-Check |
| 🟡 5 | **!Analysiere APH** | Produktion CN/MY — Tariff-Exposure prüfen |
| 🟢 6 | **!Analysiere BRK.B** | Holding, defensiv |
| 🟢 7 | **!Analysiere VEEV** | SaaS, kein Tariff-Risiko |
| 🟢 8 | **!Analysiere RMS** | Luxury, EUR, Preismacht |
| 🟢 9 | **!Analysiere SU** | Industrie, EUR |

**Hinweis Liberation Day:** Bei jedem Satelliten Tariff-Exposure prüfen (CN/TW/MY/TH/VN >35% = FLAG). Kurse seit 02.04. teilweise -10–20% → Forward-Metriken als Primärbasis.

---

## 📅 Kritische Termine

| Datum | Ereignis | Aktion |
|-------|----------|--------|
| **23.04.2026** | TMO Q1 Earnings | FCF >$7.3B → DEFCON 4 / sonst ZTS-Aktivierung prüfen (TMO v3.5 Score 62, D🟠2 — Sparrate bereits auf 50% reduziert) |
| **28.04.2026** | SPGI Earnings | QuickCheck SPGI (Score 79, Watchlist) |
| **29.04.2026** | MSFT Q3 Earnings | FLAG-Auflösung wenn CapEx/OCF <60% |
| **Mai 2026** | PEGA Earnings | Slot-16-Entscheidung |
| **01.05.2026** | Sparplan | !Rebalancing live testen (erster echter Lauf, noch nie gelaufen) |
| **Juni 2026** | Sparplan-Booster | 9.500€ Bausparvertrag + 2.000€ Steuererstattung |

---

## ⚙️ System-Status

| Komponente | Status |
|-----------|--------|
| defeatbeta MCP | ✅ WSL2 Ubuntu-24.04 — produktiv (Daten bis 03.04.2026) |
| Shibui Finance SQL | ✅ Primärquelle Technicals + FLAG-Historie |
| insider_intel.py | ✅ Form-4-Scanner 8 US-Satelliten |
| eodhd_intel.py / yfinance | ✅ Non-US Fundamentals (Cowork-Session: Web-Fallback) |
| SKILL.md | ✅ v3.5 — PT-Upside-Fix, Relative Stärke als Scored Metric |
| Briefing-Sync | ✅ Dreifach abgesichert (SessionStart/End-Hook + Claude-App-Push + Scheduled Task 09:54). Shortcuts: `!BriefingCheck`, `!SyncBriefing` (INSTRUKTIONEN.md §25) |
| Shibui SQL column | ⚠️ `code` nicht `ticker` — immer `WHERE code = 'TICKER'` |

---

## 🔬 2026-04-16 — Backtest-Ready / Scoring-System-Audit (PAUSIERT)

**Status:** ✅ Audit abgeschlossen 16.04.2026, DEFCON v3.5 implementiert — Backtest-Ready-Spec v1.1 ist nächster Schritt (nach Satelliten-Queue)
**Session-Typ:** Brainstorming + Spec-Entwurf (kein Code geschrieben)

### Wiedereinstiegs-Befehl (zuerst ausführen)

Nach dem Standard-Session-Start-Ritual:

```
Lies den Abschnitt "2026-04-16 Backtest-Ready / Scoring-System-Audit"
aus SESSION-HANDOVER.md, dann den pausierten Spec unter
docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md

Danach superpowers:brainstorming-Skill starten für das Thema:
"DEFCON v3.4 Strukturreview / Scoring-System-Audit"
```

### Kontext (sehr kurz)

1. Brainstorming zu "Formales Backtesting des DEFCON-Systems" gestartet
2. Gegen formales Backtesting entschieden: n=11 zu klein, System zu jung
3. Alternativer Ansatz: **"Backtest-Ready"-Infrastruktur** bauen (append-only Score-Archiv + FLAG-Event-Log + Vault-Integration), Review 2028-04-01
4. Spec v1.0 geschrieben — 95% korrekt, 10 bekannte Fehler für v1.1-Update identifiziert (siehe unten)
5. **🚨 Kritische Entdeckung:** DEFCON v3.4 scort "Ø PT-Upside" **zweimal** — einmal in Technicals (Schwelle >20%), einmal in Sentiment (Schwelle >15%). Zwei Deutungen:
   - (a) Intentionales Ordinal-Encoding (abgestuftes Signal)
   - (b) Echtes Double-Counting (Kategorienfehler: Analyst-PTs sind konzeptionell Sentiment)
6. **Strategischer Einwand:** Wenn v3.4 strukturell unsauber sein könnte, macht es keinen Sinn, 2 Jahre Archiv-Records auf verzerrter Basis zu bauen — **besser erst Audit, dann ggf. v3.5, dann Infrastruktur**
7. Implementation gestoppt, Audit als neues Mini-Projekt davor geschaltet

### Plan für nächste Session

#### Schritt 1: Scoring-System-Audit (timeboxed 2 Arbeitstage)

Fokussiertes Brainstorming, das folgende Fragen beantworten muss:

1. **PT-Upside-Duplikation:** Ordinal-Encoding oder Double-Counting? Entscheidung mit Begründung.
2. **Weitere Naming-Kollisionen** zwischen den 5 Blöcken systematisch suchen
3. **Theoretische Redundanzen** innerhalb eines Blocks prüfen:
   - Fwd P/E vs. P/FCF bei profitablen Firmen (strukturelle Korrelation)
   - CapEx/OCF vs. FCF Yield (mechanisch verknüpft)
   - Net Debt/EBITDA vs. Current Ratio vs. Goodwill/Assets (Bilanz-Triade)
4. **Block-Gewichtung 50/20/10/10/10** gegen die 4 Paper prüfen:
   - Befund B7 aus `Wissenschaftliche-Fundierung-DEFCON.md`: "Fundamentals > Sentiment > Technicals"
   - Passt Moat=20 zur Morningstar-Evidenz, oder ist es überhöht?
   - Sollte Sentiment eher 15 statt 10 sein (Gu-Kelly-Xiu zeigt hohe Prognosekraft)?
5. **Kategorien-Hygiene:** Sind alle Metriken im konzeptuell richtigen Block?
6. **Malus-Stacking:** Können SBC (-4) + Accruals (-2) + Tariff (-3) kumuliert zu negativen Fundamentals führen? Intendiert?
7. **Kalibrierungsanker-Reproduzierbarkeit:** Würden AVGO=86, MKL=82, SNPS=79 bei unabhängigem zweitem Durchlauf identisch rauskommen?

**Audit-Output:** Report mit jeder Finding klassifiziert als:
- **A** — strukturell sauber, bleibt
- **B** — nachweislich falsch, muss in v3.5
- **C** — unklar, braucht Design-Entscheidung

#### Schritt 2: Entscheidung v3.5-Scope

- **Minimal-Fix:** Nur PT-Upside (plus Ersatz-Metrik im Technicals-Block)
- **Konsolidierter Fix:** PT-Upside + weitere Funde
- **Status quo:** Audit zeigt v3.4 ist methodisch sauber

#### Schritt 3: v3.5-Implementation (nur falls nötig)

- `SKILL.md`, `Beispiele.md` (neue Anker!), `INSTRUKTIONEN.md`, `KONTEXT.md`, `CORE-MEMORY.md` updaten
- Vault: `Wissenschaftliche-Fundierung-DEFCON.md` erweitern
- ZIP-Paket: `06_Skills-Pakete/dynastie-depot_v3.5.0.zip`

#### Schritt 4: Re-Analyse der 11 Satelliten unter v3.5

ASML, AVGO, MSFT, RMS, VEEV, SU, BRK.B, V, TMO, APH, COST

#### Schritt 5: Backtest-Ready-Spec v1.1 + Implementation

Bestehenden Spec an v3.5 anpassen + die 10 v1.0-Fehler fixen → writing-plans-Skill → Phase 1 bauen. Die 11 Re-Analysen aus Schritt 4 werden die ersten Forward-Records im Archiv.

### Bekannte Fehler im Spec v1.0 (für v1.1-Update, nicht nochmal suchen)

**Kritisch (muss fixiert werden):**

1. **Arithmetik AVGO-Beispielrecord §4.1:** `eps_revisions_up_90d: 4` triggert `+1` → `sentiment.gesamt` müsste 10 sein, `score_gesamt` 87 statt 86. Fix: Rohwert auf 2 reduzieren.
2. **Moat-Schema fehlt `rating_base_score: int` (0-20):** Ohne Basiswert kein Arithmetik-Check möglich (Wide = 17-20 Bereich).
3. **Malus-Konvention ambig:** `sbc_malus`, `accruals_malus`, `tariff_malus` — Empfehlung: **negative Zahlen**, damit einfache Summe funktioniert.
4. **`metriken_roh` unvollständig:** Fehlen u.a. `ath_distanz_pct`, `pt_upside_consensus_pct`, `konsensus_rating`, `sell_ratio_pct`, `ownership_pct`, `net_buy_6m_usd`, `max_single_sale_90d_usd`, `trend_200ma_richtung`. **Für spätere Rekalibrierung fatal.**
5. **Widerspruch §4.1 ↔ §9.2:** "record_id unique" vs. "Duplikate als Sub-Record anhängen". Fix: Duplikate verwerfen, in `_parser_errors.log`.
6. **`analyse_typ: "rescoring"` erfunden/undefiniert:** Enum reduzieren auf `["vollanalyse", "delta"]`.

**Klarheit:**

7. **§12 Phase-Abhängigkeit:** Phase 3 hängt von Phase 2 ab (nicht parallel). Fix: "Phase 3 ← Phase 2. Phase 4 parallel zu 2+3."
8. **§10.4 Benchmark-Liste:** Nennt nur AEX, CAC40 — fehlt DAX (SAP), TSX (FFH.TO), FTSE MIB (RACE). Fix: regelbasiert ("primärer Heimatindex").
9. **§6.5:** "Shibui oder yfinance" → "Shibui primär, yfinance Fallback".
10. **Datums-Placeholder:** Mal `2026-04-XX`, mal `[YYYY-MM-DD]` → vereinheitlichen auf `[YYYY-MM-DD]`.

### Kontext-Dateien (Lese-Reihenfolge beim Wiedereinstieg)

1. **Dieser Abschnitt** — Kurz-Refresher
2. **`docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md`** — Pausierter Spec v1.0
3. **`01_Skills/dynastie-depot/SKILL.md`** — v3.4 Scoring-System, zu auditieren
4. **`01_Skills/dynastie-depot/Beispiele.md`** — Kalibrierungsanker AVGO=86, MKL=82, SNPS=79
5. **`07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md`** — 4 Paper + 7 Befunde
6. **`07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/wiki/concepts/defcon/`** — Alle DEFCON-Konzeptseiten

### Spec-Entscheidungen, die versionsunabhängig bestehen bleiben

Diese müssen nach dem Audit NICHT neu diskutiert werden:

- ✅ Zwei getrennte JSONL-Dateien (`score_history.jsonl` + `flag_events.jsonl`)
- ✅ Append-only, niemals UPDATE
- ✅ Point-in-Time-Backfill via `git show <sha>:pfad`, nie Working Tree
- ✅ Best-Effort-Parser mit `_parser_errors.log`
- ✅ FLAG-Events paired (trigger + resolution, gemeinsame `flag_id`)
- ✅ `flag_id`-Format: `TICKER_FLAGTYP_YYYY-MM-DD`
- ✅ `fcf_trend_neg`-FLAG deterministisch: "FCF YoY negativ in ≥3 von 4 Quartalen UND CapEx YoY positiv"
- ✅ Vier neue Vault-Seiten (Score-Archiv, FLAG-Event-Log, Backtest-Ready-Infrastructure, Backtest-Methodik-Roadmap)
- ✅ System-Integration in CLAUDE.md, INSTRUKTIONEN.md, CORE-MEMORY.md, KONTEXT.md
- ✅ 4 Implementation-Phasen: Forward-Pipeline → Backfill → Event-Study → Vault/System
- ✅ Review-Termin 2028-04-01
- ✅ YAGNI: kein formaler Backtest, keine Statistik-Tests, keine Automatisierung, kein Dashboard, kein SQL

### Merksätze

- **Audit timeboxed auf 2 Arbeitstage** — bei Scope-Creep: offene Fragen in "Anomalien für 2028-Review" parken
- **Anker-Vorsicht:** AVGO=86, MKL=82, SNPS=79 wurden *mit* PT-Upside-Duplikation kalibriert — jede v3.5-Änderung verschiebt die Anker. Akzeptieren, nicht vermeiden
- **Spec nicht verwerfen:** v1.0 ist zu 95% korrekt, wird auf v1.1 upgedatet, nicht neu geschrieben
- **"Alles OK" ist ein wertvolles Audit-Ergebnis:** Auditiertes v3.4 ist qualitativ höherwertig als ungeprüftes v3.4
- **Wenn v3.5 kommt:** Die 11 Re-Analysen werden die ersten Forward-Records — kein Leerlauf

---

*🦅 SESSION-HANDOVER.md v1.4 | Dynastie-Depot | Bereinigt 16.04.2026 — DEFCON v3.5 live*

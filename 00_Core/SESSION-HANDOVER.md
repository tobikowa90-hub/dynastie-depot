# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 17.04.2026 | **Für:** Neue Session (Claude Code empfohlen)

---

## ▶️ TRIGGER

```
Session starten
```

Danach: `Starte v3.7-Implementation`

---

## 🎯 HEUTIGE SESSION — Was zu tun ist

**v3.7 „System-Gap-Release" implementieren.** Wissenschaftlich fundierte Schließung von 3 operativen Lücken. **Parameter stehen fest** (User-ratifiziert 17.04.2026). Backtest ist vorberechnet. Keine Diskussion mehr über Schwellen — nur Umsetzung + Live-Verifikation.

---

## 📐 FINALE v3.7-PARAMETER (unverhandelbar)

### Fix 1 — Quality-Trap-Malus (Moat-Block, B6/Morningstar)
| Trigger | Wirkung |
|---------|---------|
| Wide Moat (17-20) + Fwd P/E > 30 ODER P/FCF > 35 | **-3 Moat-Punkte** |
| Wide Moat + Fwd P/E 22-30 ODER P/FCF 22-35 | **-1 Moat-Punkt** |
| Screener-Exceptions (BRK.B P/B, COST Membership) | nicht betroffen |

### Fix 2 — Operating Margin als Fundamentals-Metrik (B8/Gu-Kelly-Xiu)
| OpM (TTM) | Score (max. 2 Pt.) |
|-----------|---------------------|
| > 30% | 2 |
| 15-30% | 1 |
| < 15% | 0 |

- Exceptions: COST (~4% Membership-Modell), BRK.B (Holdings) → keine Bewertung
- **Cap:** Fundamentals-Block hart bei 50. Top-Namen verlieren Bonus-Headroom — gewollt.
- Quelle: `get_stock_annual_income_statement` (defeatbeta)

### Fix 3 — Analyst-Bias-Kalibrierung (Sentiment-Block, B11/Jadhav-Mirza)
| Strong-Buy Anteil | Score |
|-------------------|-------|
| < 40% | 4 |
| 40-60% | 2 |
| **> 60%** | **1** (Crowd-Consensus-Malus — nur extreme Fälle) |

> **Begründung Schwelle > 60% (nicht > 50%):** B11 adressiert Crowd-Consensus-Extremfälle, nicht jede breite Coverage. Bei > 50% hätten 8/11 Satelliten den Malus kassiert → Pauschalabzug statt Differenzierung. > 60% fängt nur die echten Ausreißer (SU 22/0, ASML, AVGO, MSFT).

| Sell-Ratio | Score |
|------------|-------|
| < 3% | 1 (Risky Consensus) |
| 3-10% | 3 (Healthy Dissent) |
| > 10% | 0 |

---

## 📊 BACKTEST-VORHERSAGEN (alle 11 Satelliten)

| Ticker | v3.5 | v3.7 | Δ | DEFCON-Change | Ursachen-Kette |
|--------|------|------|---|----------------|-----------------|
| **ASML** | 68 🟡 3 | **64 🟠 2** | **-4** | **D3→D2** ⚠️ | QT -3 (Fwd P/E 38x) + OpM +1 − Bias -2 (nur wenn SB ≥60%) |
| **COST** | 69 🟢 4 | 66 🟢 4 (knapp) | -3 | bleibt D4 | QT -3 (P/FCF 53x); SB unter 60% → kein Bias-Malus |
| **SU** | 71 🟢 4 | 69 🟢 4 | -2 | bleibt D4 | QT -1 + OpM +1 − Bias -2 (22 Buy 0 Sell = extreme) |
| **RMS** | 69 🟢 4 | 68 🟢 4 | -1 | bleibt D4 | QT -3 + OpM +2; SB unter 60% |
| **AVGO** | 85 🟢 4 | 84 🟢 4 | -1 | bleibt D4 | OpM +1 (Cap) − Bias -2 (SB ~65%) |
| **MSFT** | 60 🟠 2 | 59 🟠 2 | -1 | stabil | QT -1 + OpM +2 − Bias -2 |
| **VEEV** | 74 🟢 4 | 74 🟢 4 | 0 | stabil | QT -1 + OpM +1 |
| **V** | 86 🟢 4 | 86 🟢 4 | 0 | stabil | OpM +1 (Cap); SB ~55% → kein Bias-Malus |
| **BRK.B** | 75 🟢 4 | 75 🟢 4 | 0 | Screener-Exceptions | alle drei Exceptions aktiv |
| **TMO** | 62 🟠 2 | 63 🟠 2 | +1 | stabil | OpM +1; SB unter 60% |
| **APH** | 61 🟡 3 | 63 🟡 3 | +2 | FLAG überschreibt | OpM +1, Narrow = kein QT |

**Haupt-Impact:** ASML D3→D2 = Sparrate 38€ → 19€. Position gehalten, Nachkauf gedrosselt. Wissenschaftlich begründet durch Triple-Signal (Bewertung + Consensus + Quality-Trap). **Disziplin, nicht Panik.**

---

## 🛠️ AUSFÜHRUNGS-PLAN (8 Schritte, ~2h)

### 1. Dokument-Updates (~30 Min)
- [ ] `00_Core/INSTRUKTIONEN.md` §4 DEFCON-Matrix (Moat-Malus-Regel), §5 Fundamentals-Skalen (Operating Margin-Tabelle), §6 Insider-Scoring unverändert, **Sentiment-Block erweitern**
- [ ] `01_Skills/dynastie-depot/SKILL.md` Scoring-Skalen (gleiche 3 Regeln)
- [ ] `07_Obsidian Vault/.../wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` Änderungsprotokoll (v3.7-Eintrag)

### 2. Backtest-Live-Verifikation (~45 Min)
**Kritisch:** Vorhersagen gegen echte Daten prüfen. Besonders ASML, COST, SU.
- [ ] ASML: Fwd P/E + P/FCF (AlphaSpread/Yahoo), Operating Margin (defeatbeta), Strong-Buy% (Zacks/Yahoo)
- [ ] COST: P/FCF bestätigen (erwartet ~53x)
- [ ] SU: Strong-Buy% verifizieren (22 Buy/0 Sell-Erwartung — extreme Consensus)
- [ ] Alle anderen: nur Operating Margin + Strong-Buy-Anteil abrufen (1-2 Min pro Ticker)

### 3. Score-Register aktualisieren (~15 Min)
- [ ] `00_Core/CORE-MEMORY.md` Section 4 (Score-Register) — neue Zeilen-Updates alle 11 Satelliten
- [ ] `00_Core/Faktortabelle.md` Haupttabelle

### 4. Sparraten-Neuberechnung (~10 Min)
**ASML Gewicht 1.0 → 0.5 ist der einzige Shift.**
- Neuer Nenner: 7×1.0 + 2×0.5 = 8.0 (7 volle D4 + ASML-D2 + TMO-D2)
- Einheits-Rate: 285€ / 8.0 × 1.0 = **35,63€** (volle Rate)
- D2-Rate: 285€ / 8.0 × 0.5 = **17,81€** (ASML, TMO)
- **Eingefroren:** AVGO FLAG, MSFT FLAG, APH FLAG → 0€
- Check: 7 × 35,63 + 2 × 17,81 = 249,41 + 35,62 = **285,03€** ✓ (Rundung)
- [ ] `03_Tools/Rebalancing_Tool_v3.4.xlsx` Sparraten-Sheet aktualisieren

### 5. config.yaml (~5 Min)
- [ ] Scores + DEFCON + score_datum = 2026-04-17 für alle 11 Positionen
- [ ] ASML: `defcon: 2, weight: 0.5`

### 6. Vault-Sync (~10 Min)
- [ ] Entity-Seiten: ASML, COST, RMS, SU, AVGO (größte Shifts) — Score-Frontmatter + „Wissenschaftliche-Basis"-Block
- [ ] `log.md` Eintrag (Format: `## [2026-04-17] edit | DEFCON v3.7 System-Gap-Release`)
- [ ] `index.md` — kein neuer Content, nur v3.5 → v3.7 Hinweis

### 7. Meilenstein-Log (~5 Min)
- [ ] CORE-MEMORY Section 1: Neuer Eintrag 17.04.2026 — v3.7-Release abgeschlossen, 3 Gap-Closures, ASML D3→D2
- [ ] Faktortabelle Header: Stand auf 2026-04-17, v3.5 → v3.7

### 8. Briefing-Sync (~5 Min)
- [ ] `git status --short 00_Core/`
- [ ] `!SyncBriefing` — User bestätigt mit „ja/push"
- [ ] Trigger liest v3.7-Stand ab 18.04. 10:00 MESZ

---

## ⚠️ WICHTIGE HINWEISE

### Was NICHT zu tun ist
- **Keine Schwellen-Diskussion.** Parameter sind final. Wenn Live-Daten anders aussehen als Backtest: Datenwerte aktualisieren, nicht Schwellen.
- **Keine Paper-Hunt-Sessions.** Vault-Evidenz ist komplett. Gap-Closures stützen sich auf bereits ingestete Paper (Morningstar B6, Gu-Kelly-Xiu B8, Jadhav-Mirza B11).
- **Keine F-Score / GP/TA / Accrual-Bonus-Einführung.** v3.6 wurde verworfen (Double-Counting + Redundanz). Die 3 Papers (Piotroski/Novy-Marx/Sloan) stehen im Vault als Audit-Stärke, nicht als Scoring-Regel.

### Was passieren kann (vorbereiten)
- **Operating Margin Abweichung vom Backtest:** defeatbeta-Werte können sich leicht von Schätzungen unterscheiden. Kein Drama — dokumentieren und weiter.
- **Strong-Buy-Ratio von Yahoo oft anders als Zacks.** Primärquelle: Yahoo Finance Analysis-Tab. Wenn Zacks deutlich abweicht: manueller Cross-Check.
- **ASML-Kurs kann bis morgen bewegt haben.** Falls Fwd P/E unter 30 gefallen: Quality-Trap -1 statt -3 → Score vermutlich 66-67 statt 64. Re-rechnen, DEFCON kann wechseln.

### Applied Learning (frisch, beachten!)
- Paper-Ingest ≠ System-Update: Wissenschaft validiert, erzwingt keine neuen Regeln
- Double-Counting-Falle: Aggregat-Scores (z.B. F-Score) prüfen ob Sub-Signale schon dekomponiert
- Bonus-Cap-Check: Bei neuen Boni Punkteverteilung Top-Namen prüfen

---

## 📚 KONTEXT-TIEFE (falls Nachlese nötig)

- **Gestern-Vault-Arbeit:** 3 Foundation-Papers ingested (Piotroski/Novy-Marx/Sloan) → B12/B13/B14 als Validation-Befunde. 6 neue Notes.
- **v3.6 verworfen** (Begründung in `Wissenschaftliche-Fundierung-DEFCON.md` Änderungsprotokoll 17.04.).
- **v3.7 Gaps identifiziert in Gap-Analyse** (nicht persistent gespeichert — nur in dieser Session). Ausgangspunkt: System-Reife 85%, Ziel: ~92%.
- **Briefing-Sync-Schwelle** ist jetzt 5 unpushed Commits (war: 1). Script in `03_Tools/briefing-sync-check.ps1`.

---

## ✅ DEFINITION OF DONE (v3.7-Release)

- [ ] Alle 3 Scoring-Regeln in INSTRUKTIONEN.md + SKILL.md verankert
- [ ] 11 Satelliten mit v3.7-Scores in Faktortabelle + CORE-MEMORY + config.yaml
- [ ] Sparraten neu berechnet und im Rebalancing-Tool
- [ ] Vault: Entity-Seiten + log.md + Synthese-Protokoll
- [ ] CORE-MEMORY Meilenstein-Eintrag
- [ ] `!SyncBriefing` ausgeführt
- [ ] Kein Merge-Konflikt, kein Orphan im Vault

**Danach:** v3.7 ist live. Nächste Session kann regulär `!QuickCheck ALL` unter v3.7 ausführen.

---

---

## 📦 BACKTEST-READY INFRASTRUCTURE (nach v3.7)

**Status:** Design abgeschlossen, Plan gespeichert, wartet auf Durchführung nach v3.7.

- **Design-Spec:** `docs/superpowers/specs/2026-04-16-backtest-ready-infrastructure-design.md` (v3.4 → muss auf v3.7 aktualisiert werden)
- **Implementation-Plan:** `docs/superpowers/plans/2026-04-17-backtest-ready-infrastructure.md`
- **Sequenz:** v3.7 zuerst → dann Spec auf v3.7 updaten → dann 4-Phasen-Implementation

### Schema-Impact durch v3.7
Neue Felder im JSONL-Schema (additiv, schema_version 1.0 bleibt):
- `scores.moat.quality_trap_malus` (0/-1/-3)
- `scores.fundamentals.operating_margin` (0/1/2)
- `metriken_roh.operating_margin_pct`, `strong_buy_pct`
- Sentiment-Schwellen geändert (Feldnamen bleiben)

### Brainstorming-Entscheidungen (ratifiziert 17.04.)
- Three-Layer-Architektur: State (Faktortabelle) / Narrative (log, CORE-MEMORY) / History (JSONL)
- Copy-then-Redirect: Score-Register (Section 4) → Pointer nach Backfill
- Option B Rohdaten: Scores + Inputs flach im Record (für Re-Scoring mit anderen Schwellen)
- Pydantic-Schema mit Validatoren, Python CLI-Tools, append-only JSONL in 05_Archiv/

### Spec-Entscheidungen (versionsunabhängig — nicht neu diskutieren)
- ✅ Zwei JSONL: `score_history.jsonl` + `flag_events.jsonl` (append-only, niemals UPDATE)
- ✅ Point-in-Time-Backfill via `git show <sha>:pfad`, nie Working Tree
- ✅ FLAG-Events paired (`flag_id` = `TICKER_FLAGTYP_YYYY-MM-DD`)
- ✅ `fcf_trend_neg` deterministisch: FCF YoY neg. in ≥3/4 Quartalen UND CapEx YoY positiv
- ✅ 4 Implementation-Phasen + Review 2028-04-01
- ✅ YAGNI: kein formaler Backtest, kein Dashboard, kein SQL

### Bekannte Fehler im Spec v1.0 (für v1.1 — nicht nochmal suchen)

**Kritisch:**
1. Arithmetik AVGO-Record §4.1: `eps_revisions_up_90d: 4` → `sentiment.gesamt` müsste 10, `score_gesamt` 87 statt 86. Fix: Rohwert auf 2.
2. Moat-Schema fehlt `rating_base_score: int` (0-20).
3. Malus-Konvention ambig — Empfehlung: **negative Zahlen** für einfache Summe.
4. `metriken_roh` unvollständig (fehlen u.a. `ath_distanz_pct`, `pt_upside_consensus_pct`, `konsensus_rating`, `sell_ratio_pct`, `ownership_pct`, `net_buy_6m_usd`, `max_single_sale_90d_usd`, `trend_200ma_richtung`).
5. Widerspruch §4.1↔§9.2: "unique" vs. "Sub-Record" → Duplikate verwerfen in `_parser_errors.log`.
6. `analyse_typ: "rescoring"` undefiniert → Enum: `["vollanalyse", "delta"]`.

**Klarheit:**
7. §12 Phase-Abhängigkeit: Phase 3 ← Phase 2. Phase 4 parallel zu 2+3.
8. §10.4 Benchmark-Liste: regelbasiert ("primärer Heimatindex") statt Enumeration.
9. §6.5: "Shibui primär, yfinance Fallback".
10. Datums-Placeholder vereinheitlichen auf `[YYYY-MM-DD]`.

---

*🦅 SESSION-HANDOVER v2.1 | Dynastie-Depot | Stand: 17.04.2026 | Für v3.7-Implementation + Backtest-Infrastruktur*

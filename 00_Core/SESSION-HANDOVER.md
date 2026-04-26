# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-26 — Paper-Ingest Phase A (14 Source-Pages) committed. **Nächste Session: Codex-Fixes + Phase B+C abschließen.**

### 🟢 Resume-Stand

**Branch:** `main`. Paper-Ingest Phase A1+A2+A3 done — 14 Source-Pages in `wiki/sources/papers/` + 14 Raw-PDFs in `raw/papers/` committed. Codex-Review identifizierte 4 Must-Fix + 3 Should-Fix + 3 Nice-to-have.

**Standing-Dirty (NICHT mitcommitted):** `app.json`, `wiki/concepts/PORTFOLIO.md`, gelöschte `.canvas`/`.base`-Files, plus stash + xlsx + .code-workspace.

### 🎯 Hauptauftrag nächste Session: Codex-Fixes + Phase B+C

#### **Sofort vor Phase B1: Must-Fix (3 Quick-Wins)**

3. **Alias-Fix `[[2iQ-Insider-Meta-Review]]`** — File heißt `2iQ-Insider-Meta-Review-2021.md`, fehlender Alias bricht 2 Backlinks in `Lakonishok-Lee-2001.md:22+66`. Lösung: Alias `"2iQ-Insider-Meta-Review"` zu Frontmatter der 2iQ-Page hinzufügen.
4. **Alias-Fix `[[Hou-Xue-Zhang-q-Factor]]`** — File heißt `Hou-Xue-Zhang-2015-q-Factor.md`, bricht Backlinks in `Fama-French-2015-Five-Factor.md:54` + `Fama-French-2006-Profitability.md:68`. Lösung: Alias hinzufügen.
10. **Cleanup `>>>>`-Artefakt** in `2iQ-Insider-Meta-Review-2021.md:33` (Ingest-Rauschen).

#### **Phase B1 — absorbiert die governance-kritischen Fixes (Must-Fix #1+#2):**

1. **Status-Matrix B25-B28 in `wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md`** eintragen (Codex-FAIL: Pages klassifizieren B25-B28 bereits, aber SSoT kennt sie nicht)
   - B25 McLean/Pontiff = `meta-gate` (§29.7-Erweiterung "M&P-Discount")
   - B26 Lakonishok/Lee = `active-scoring-validation` (Insider-Block-Validation)
   - B27 Ke/Huddart/Petroni = `design-context` (Window-Erweiterung deferred auf insider-intelligence v2)
   - B28 Tetlock = `design-context` (Mean-Reversion-Anker, kein Live-Score-Change)
   
   ⚠️ **Codex-Hinweis (WARN):** B26-B28 als `active-scoring` klassifiziert in Pages, aber Fließtext sagt selbst „kein Live-Score-Change". Status auf `active-scoring-validation` / `design-context` re-klassifizieren — passt zur tatsächlichen Wirkung. **Entscheidung in B1 fällen.**

2. **§29.7 / M&P-Discount** entweder im DEFCON-SSoT (`INSTRUKTIONEN.md` §29) formal anlegen ODER in `McLean-Pontiff-2016.md:70` als unverabschiedete Idee zurückstufen. Empfehlung: **anlegen** (passt zur §29-Backtest-Validation-Architektur, sauberer Layer 7).

3. **SKILL.md Schritt-2.5 Backlinks** für B25-B28 (`01_Skills/dynastie-depot/SKILL.md`).

4. **INSTRUKTIONEN.md §-Updates**: §29 (B25 + Discount), Insider-Block (B26+B27 deferred-Pipeline-Note), Sentiment-Block (B28 Mean-Reversion-Anker für `feedback_score_stability`-Memory).

#### **Phase B2 — Concept-Pages (5 neu + 2 Updates):**

- Neu: `Post-Publication-Decay`, `Insider-Trading-Primary-Signal`, `Earnings-Foreknowledge-Window`, `Media-Pessimism-Sentiment`, `Noise-Trader-Model`
- Mauboussin-Special: Concept-Updates `Moat-Taxonomie-Morningstar` + `ROIC-vs-WACC` mit CAP-Verweis; ggf. neue `Competitive-Advantage-Period`-Page
- Optional: `Quality-Investing-Multidimensional` (4-Pillars-Framing aus QMJ + Amundi)

#### **Phase B3 — Entity-Pages (~25 Autoren, kompakt):**

McLean, Pontiff, Lakonishok, Lee, Ke, Huddart, Petroni, Tetlock, Asness, Frazzini, Pedersen, Mauboussin, Callahan, Lepetit, Cherief, Ly, Sekine, Fama, French, Harvey (Cam), Liu (Yan), Zhu (Heqing), Moskowitz, Hou, Xue, Zhang (Lu), Yang (Hongyang), Liu (Xiao-Yang), Wang (Christina Dan), Hable.

#### **Phase C — Synthesis + Final:**

- Synthesis-Update: `Wissenschaftliche-Fundierung-DEFCON.md` Quellen-Übersicht von 20 auf **34 Paper** erweitern + B-Befunde-Counter B25-B28 aufnehmen
- `index.md` Update — alle 14 neuen Source-Pages + 5+ neue Concept-Pages + ~25 Entity-Pages eintragen
- `log.md` Eintrag (ein zusammenhängender Bulk-Ingest-Eintrag)
- WIKI-SCHEMA Auto-Lint: alle neuen/geänderten Pages auf Orphans + broken Links prüfen
- Commit + Push

#### **Should-Fix (in Phase B mit erledigen):**

5. `McLean-Pontiff-2016.md:30` — Tabelle `-31% / -55%` vs Headline `26% / 58% / 32%`: Rechenbasis erklären oder angleichen
6. `Tetlock-2007.md:41` + `Lakonishok-Lee-2001.md:22` — Confidence-Markierung wo Primärquelle nicht textextrahierbar
7. FinGPT-Venue bibliografisch entmischen (Konferenz 2023 vs. arXiv v2 Nov 2025)

#### **Nice-to-have (deferred):**

8. Repo-weite Schema-Drift-Entscheidung (House-Schema vs. WIKI-SCHEMA `medium/created/updated/sources`)
9. Year-only `date`-Felder → ISO-8601
10. JEL-Codes + Sample-Period-Metadaten für SOURCE-ONLY-Academics

### Codex-Review-Verdikt (Stand 26.04.)

**14 Files Form-Konformität:** PASS (raw_path), WARN (Schema-Drift House vs. WIKI-SCHEMA), PASS (aliases vorhanden)
**Inhaltliche Akkuratesse:** Großteils PASS bei B-Papers; einige WARN bei Magnitude-Spezifika ohne Primär-Beleg
**DEFCON-Mapping:** **2× FAIL** (Status-Matrix-Eintrag + §29.7-Anchor) → muss vor Phase B-Workflow gefixt werden
**Cross-Refs:** **2× FAIL** (2iQ + Hou-Xue-Zhang Alias-Mismatch) → 2-Minuten-Fix
**Tonalität:** PASS, kleinere Normativ-zu-früh-Hinweise
**Risiken:** Hauptpunkt = vorauseilende Aktivierungs-Sprache vor SSoT-Eintrag

### Standing-Focus (unverändert)

- 28.04. V Q2 FY26 — D2-Entscheidung (Technicals-Reversal?)
- 29.04. MSFT Q3 FY26 — FLAG-Review (CapEx/OCF bereinigt <60% = Auflösung)

### Wichtige Notizen

**Files-Layout post-Ingest:** `raw/papers/` enthält jetzt 26 Files (12 alt + 14 neu). Mislabeled-Duplikat (`Lakonishok & Lee.pdf` ≡ `Ke, Huddart, Petroni.pdf`) wurde gelöscht im Vorlauf. Empty `Neuer Ordner` aufgeräumt. F/F 2004 Draft (Matrix #14) als Sibling-Note in `Fama-French-2006-Profitability.md` gefoldet (User-Decision: „nur ein Auszug aus #12").

**Lakonishok-Lee PDF ist image-only** — Text aus 2iQ-Sekundärquelle + Wissensbasis synthesisiert (Codex-WARN: Confidence-Markierung in Page deutlicher setzen).

**CodeRabbit-CLI** läuft via WSL Ubuntu (`feedback_coderabbit_via_wsl.md`).

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `CORE-MEMORY.md §13` + `PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*

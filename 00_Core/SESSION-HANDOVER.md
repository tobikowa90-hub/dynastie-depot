# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-27 — Paper-Ingest Phase A: Codex-Fixes + Phase B (Status-Matrix B25-B28, §29.7 M&P-Discount, 6 Concept-Pages, 30 Entity-Pages) committed. **Nächste Session: Phase C (Synthesis-Update Quellen 20→34, index.md, log.md, Lint, Final-Commit) — nach Codex-Review.**

### 🟢 Resume-Stand

**Branch:** `main`. Phase A (14 Source-Pages) committed in `b8306df` (gestern). Phase B heute durchgezogen — gegliedert in 3 Sub-Commits empfohlen oder einen Bulk-Commit:

**Commit-Block 1 — Codex Quick-Wins + Should-Fixes:**
- `2iQ-Insider-Meta-Review-2021.md` — Alias `2iQ-Insider-Meta-Review` ergänzt + `>>>>` Cleanup line 33 (Codex Must-Fix #3, #10)
- `Hou-Xue-Zhang-2015-q-Factor.md` — Alias `Hou-Xue-Zhang-q-Factor` ergänzt (Codex Must-Fix #4)
- `McLean-Pontiff-2016.md` — Magnitude-Klärung Tabelle (-31%/-55% raw vs 26%/58% headline aufgelöst, Codex Should-Fix #5) + §29.7 „angelegt" statt „geplant"
- `Lakonishok-Lee-2001.md` — Confidence-Markierung deutlicher (image-only-Trap-Hinweis verstärkt, Codex Should-Fix #6) + Status-Tag `active-scoring-validation`
- `Tetlock-2007.md` — Confidence-Markierung Magnitude-Tabelle (sekundär-zitierte bps-Werte, Codex Should-Fix #6) + Status-Tag `design-context`
- `Ke-Huddart-Petroni-2003.md` — Status-Tag `design-context`
- `Yang-Liu-Wang-2023-FinGPT.md` — Venue-Feld YAML-strukturiert: conference vs. preprint_v1/v2 entmischt (Codex Should-Fix #7)

**Commit-Block 2 — Phase B1 Status-Matrix + §29.7:**
- `wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` — 2 neue Status-Labels (`active-scoring-validation` + `design-context`), B25-B28 in Status-Matrix + Befunde-Matrix, 4-Dim-Validation-Gate erweitert um §29.7-Zeile, Header-Counter 24 → 28 Befunde, Sources-Frontmatter um 4 Pages erweitert, Änderungsprotokoll-Eintrag 2026-04-26
- `00_Core/INSTRUKTIONEN.md` — neuer §29.7 M&P-Discount-Gate (Renumber alt §29.7 → §29.8, alt §29.8 → §29.9), §4 Befunde-Router um 6 Status-Labels erweitert, §5 Sentiment um 4-Layer-Anker (B11/B19/B24/B28), §6 Insider um B26-Validation + B27-deferred-Pipeline-Note
- `01_Skills/dynastie-depot/SKILL.md` — Schritt 2.5 erweitert: 6 Status-Labels statt 4, Backlinks B25-B28, Insider/Sentiment-Block-Output-Templates ergänzen B26/B27/B28-Befund-IDs

**Commit-Block 3 — Phase B2 Concept-Pages (6 neu + 2 Updates):**
- Neu in `wiki/concepts/`: `Post-Publication-Decay.md` (B25), `Insider-Trading-Primary-Signal.md` (B26+B27), `Earnings-Foreknowledge-Window.md` (B27), `Media-Pessimism-Sentiment.md` (B28), `Noise-Trader-Model.md` (DSSW 1990), `Competitive-Advantage-Period.md` (Mauboussin CAP — Bonus zur Auflösung der Backlinks aus den 2 Updates)
- Update: `Moat-Taxonomie-Morningstar.md` + `defcon/ROIC-vs-WACC.md` mit CAP-Verweis

**Commit-Block 4 — Phase B3 Entity-Pages (30 neu kompakt):**
- B25: r-david-mclean, jeffrey-pontiff
- B26: josef-lakonishok, inmoo-lee
- B27: bin-ke, steven-huddart, kathy-petroni
- B28: paul-tetlock
- Mauboussin: michael-mauboussin, dan-callahan
- QMJ: clifford-asness, andrea-frazzini, lasse-pedersen
- Amundi 4-Pillars: jean-baptiste-lepetit, nazim-cherief, thy-ly, takaya-sekine
- FF: eugene-fama, kenneth-french
- HLZ-q-Factor: kewei-hou, chen-xue, lu-zhang
- Harvey-Liu-Zhu: campbell-harvey, yan-liu, heqing-zhu
- FinGPT: hongyang-yang, xiao-yang-liu, christina-dan-wang
- 2iQ: robert-hable
- Momentum-Anker: tobias-moskowitz

**Standing-Dirty (NICHT mitcommitted, gleiche Liste wie gestern):** `app.json`, `wiki/concepts/PORTFOLIO.md`, gelöschte `.canvas`/`.base`-Files in `Obsidian Mindmap/`, plus stash + xlsx + .code-workspace.

### 🎯 Phase C — Nächste Session

**Reihenfolge nach Codex-Review (Zwischen B + C):**

1. **C-1 Synthesis-Update**: `wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` — Quellen-Übersicht von 20 auf 34 Paper erweitern (= +14 aus Phase A: B25-B28 + 10 SOURCE-ONLY-Anker). Neue Tabellen-Zeilen: McLean-Pontiff, Lakonishok-Lee, Ke-Huddart-Petroni, Tetlock + Mauboussin-Callahan, Asness-Frazzini-Pedersen-QMJ, Fama-French-2015, Fama-French-2006, Hou-Xue-Zhang, Harvey-Liu-Zhu, Amundi-4-Pillars, 2iQ-Meta, FinGPT, plus 2 weitere SOURCE-ONLY-Pages (siehe Phase-A-Commit für vollständige Liste).

2. **C-2 index.md Update**: alle Phase-A + Phase-B-neuen Pages eintragen — 14 Source-Pages, 6 neue Concept-Pages, 30 Entity-Pages.

3. **C-3 log.md Bulk-Eintrag**: ein zusammenhängender Eintrag für die gesamte Phase A+B (oder zwei Einträge: A am 26.04., B am 27.04.). WIKI-SCHEMA Auto-Lint danach: Orphans + broken Links prüfen, sofort fixen. Final-Commit + Push.

### 🔍 Codex-Review-Verdikt Phase B (Commit 7e4712e — durchgeführt 27.04.2026)

**Cluster 1 — Codex-Round-1-Fix-Implementierung:**
- #3 Alias `[[2iQ-Insider-Meta-Review]]` → **PASS**
- #4 Alias `[[Hou-Xue-Zhang-q-Factor]]` → **PASS**
- #10 `>>>>` Cleanup → **PASS**
- #5 McLean-Pontiff Magnitude → **WARN → Must-Fix appliziert in Follow-Up-Commit:** `defcon_relevanz`-Field referenzierte fälschlich „32%" als operativen Discount, korrekt sind 58% (Faktor 0,42). 32pp ist nur der publication-effect lower bound (= 58% − 26%), NICHT der operative Discount. Korrigiert.
- #6 Confidence-Markierungen → **N/V** (Codex declined commands, manuell zu verifizieren in Phase C)
- #7 FinGPT Venue-Entmischung → **N/V** (Codex declined commands, manuell zu verifizieren in Phase C)

**Cluster 2-4 (Status-Matrix, §29.7-Renumber, 6 Concept-Pages, 30 Entity-Stubs):** **N/V — Codex-Coverage unvollständig** durch declined commands auf Vault-Dateien. Empfehlung für Phase-C-Start: dedizierter zweiter Codex-Run gegen `7e4712e..HEAD` für Cluster 2-4 BEVOR die C-Files (Synthesis-Counter-Update, index.md, log.md) erstellt werden — sonst propagieren etwaige Schema-/Backlink-Drifts in die C-Synthesis 1:1.

**Hauptrisiko Phase C:** Beim Synthesis-Update 20→34 konsistente Nutzung von `58%` (operativer M&P-Discount) statt `32%` (publication-effect lower bound) prüfen. Beide Zahlen sind zulässig, aber kontextuell verschieden — präzises Vokabular Pflicht.

### Standing-Focus (unverändert)

- 28.04. V Q2 FY26 — D2-Entscheidung (Technicals-Reversal?)
- 29.04. MSFT Q3 FY26 — FLAG-Review (CapEx/OCF bereinigt <60% = Auflösung)

### Wichtige Notizen

- **Bonus-Concept-Page** `Competitive-Advantage-Period.md` zusätzlich zur Handover-Liste angelegt — beide Updates (Moat-Taxonomie + ROIC-vs-WACC) verlinken auf die Page; ohne sie wären 2 Backlink-Orphans entstanden.
- **Optional Quality-Investing-Multidimensional Page** aus dem Handover NICHT angelegt — bestehende `QMJ-Faktor.md` deckt das 4-Pillars-Framing strukturell ab, deferred bis Bedarf.
- **Score-Archiv unangetastet** — kein DEFCON-Trigger in dieser Session, kein `score_history.jsonl`-Append.
- **CodeRabbit-CLI** läuft via WSL Ubuntu (`feedback_coderabbit_via_wsl.md`).

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `CORE-MEMORY.md §13` + `PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*

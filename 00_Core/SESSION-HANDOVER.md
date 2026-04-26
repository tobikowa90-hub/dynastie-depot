# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-26 — Phase-2 system-audit auf main (`ac43929`). Status-Matrix-Pre-Step `2add408` clean. **Nächste Session: Paper-Ingest** (15 Papers, 4 neue Bs). Übernächste: Deferred-Liste.

### 🟢 Resume-Stand

**Branch:** `main`. Pre-Resume-Checks:
1. `git status --short` — clean (außer Standing-Dirty: stash + xlsx + .code-workspace)
2. `python "03_Tools/system_audit/_smoke_test.py"` → 20 [OK]
3. `python "03_Tools/system_audit.py" --full --no-write` → 10/16 PASS (status_matrix 24/24, vault_backlinks/markdown_header/existence FAIL = deferred)

### 🎯 Hauptauftrag nächste Session: Paper-Ingest

**User-Vorbereitung:** PDFs der 15 Papers werden manuell in `07_Obsidian Vault/Obsidian Mindmap/Investing Mastermind/raw/papers/` abgelegt. Token-effizient: kein WebFetch im Skill-Lauf.

**Selektions-Matrix (aus Brainstorm 26.04. festgezurrt — 15/15 IN, 4 neue Bs, 11 SOURCE-ONLY):**

| # | Paper | B-Action | Block |
|---|-------|----------|-------|
| 1 | QMJ — Asness/Frazzini/Pedersen 2013 | SOURCE-ONLY | Fundamentals + Moat |
| 2 | Measuring the Moat — Mauboussin/Callahan | **SOURCE-ONLY** (Decision: B, kein active-scoring) | Moat |
| 3 | Amundi Quality 2021 | SOURCE-ONLY | Fundamentals |
| 4 | Fama/French 5-Factor 2015 | SOURCE-ONLY | Fundamentals |
| 5 | McLean/Pontiff 2016 — Post-Pub-Decay | **NEW B25 meta-gate** | §29 Backtest |
| 6 | Harvey/Liu/Zhu 2016 — t≥3 Hurdle | SOURCE-ONLY (anchors B16) | §29 Backtest |
| 7 | Lakonishok/Lee 2001 — Insider Primary | **NEW B26 active-scoring** | Insider |
| 8 | Ke/Huddart/Petroni — Insider/EPS-Bridge | **NEW B27 active-scoring** | Insider→Fundamentals |
| 9 | Tetlock 2007 — Sentiment | **NEW B28 active-scoring** | Sentiment |
| 10 | FinGPT 2023 | SOURCE-ONLY | LLM/Infra |
| 11 | Value+Momentum Everywhere — Asness 2013 | SOURCE-ONLY (anchors B7) | Technicals |
| 12 | F/F 2006 — Profitability+Investment | SOURCE-ONLY | Fundamentals |
| 13 | Hou/Xue/Zhang 2015 — q-Factor | SOURCE-ONLY | §29-Roadmap |
| 14 | F/F 2004 Draft | SOURCE-ONLY | Fundamentals |
| 15 | 2iQ Insider Meta-Review | SOURCE-ONLY (`source-type: industry-meta`) | Insider |

**Quelle:** `c:\Users\tobia\OneDrive\Desktop\Gemini Research & Feedback\Priorisierte Ergänzungsliste für Dynastie-Depot Literatur-Ingest (10–20 Paper).md` (Gemini-Research-Output mit ausführlichen Begründungen pro Paper).

**Workflow (19.04.-Style, lessons-learned eingeflossen):**
1. Pro Paper: `wiki/sources/papers/<short-name>.md` mit Frontmatter (`url`, `raw_path` falls PDF in raw/papers/, `defcon_relevanz`, `related`-Wikilinks) + Markdown-Summary (Abstract, Kern-Zahlen-Tabelle, Strukturierte Sektionen).
2. Für 4 neue Bs (B25-B28): Status-Matrix-Eintrag in `wiki/synthesis/Wissenschaftliche-Fundierung-DEFCON.md` + Backlinks von SKILL.md (Schritt 2.5 Befunde-Check) + INSTRUKTIONEN.md §-Updates.
3. Backlinks systemweit: Concept-Pages (`QMJ-Faktor`, `Moat-Taxonomie-Morningstar`, `News-Sentiment-Analysis`, `Insider-Signal` usw.).
4. Schema-Erweiterung (Mini): `raw_path: ../../../raw/papers/<file>.pdf` als optional-Frontmatter-Feld. Backwards-kompatibel.

**Mauboussin-Decision (User 26.04.):** SOURCE-ONLY + Concept-Page-Update für `Moat-Taxonomie-Morningstar` und `ROIC-vs-WACC` mit CAP-Konzept-Verweis. KEIN neues B (CAP-Estimation passt nicht in 4-Min-Score-Routine).

### Übernächste Session: Deferred-Liste

Inhalt + Priorisierung steht in `00_Core/PIPELINE.md` (#1, #8-#14) + Audit-Drift-Liste aus `--full --no-write`-Run. Strategie: erst Core-Drifts (3-4 SKILL.md Frontmatter + Stand-Header), dann Vault-Optional-FAILs (vault_backlinks 11 broken + markdown_header/existence-Drift), dann Phase-2-Internals (Codex-Minor-findings, Task-4/5/7 deferred), dann PIPELINE-#9-#14.

### Standing-Focus (unverändert)

- 28.04. V Q2 FY26 — D2-Entscheidung
- 29.04. MSFT Q3 FY26 — FLAG-Review

### Wichtige Notizen

**Stash@{0}** unangetastet (pre-phase2-resume vault drift + xlsx 26.04.). **CodeRabbit-CLI** läuft via WSL Ubuntu (Memory `reference_coderabbit_via_wsl.md`, Pattern `wsl.exe -d Ubuntu -e bash -lc '...'`).

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `CORE-MEMORY.md §13` + `PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*

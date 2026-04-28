# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-28 Spätnachmittag (vor Compact). Provenance-Gate Plan v3.1 Tasks 0/0.5/1/2 committed. Codex-Round-1+Round-2-Sparring ergab 1 HIGH (SKILL.md Pre-Flight-Klausel) + 1 MEDIUM (Plan-File-Drift) + 2 LOWs. Joint-Confidence aktuell 92% — V/MSFT-Live-Runs benötigen vor Execution 4 Reconcile-Items (Variante C: Mini-Patches A+B sofort, Task 6.5 nach Task 6, V-Pre-Append-Audit als Workflow-Notiz). **Resume-Trigger nach Compact: „Provenance-Gate Plan weiter — Tasks 3-6.5 ausstehend"**.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `5f4a6c5` (Task 2 Schicht D Block-Coverage-Validator). Working tree clean.

**Bereits committed in dieser Session (28.04.):**
| Commit | Task | Was |
|---|---|---|
| `5d97ddc` | 0.5 | TMO #28 Block-Coverage-Backfill via Migration-Helper (5 Felder gefüllt: gm_trend +0.5 / rel_strength -16 / kurs_vs_200ma -2.13 / ma200_slope rising) |
| `ef6979c` | 1 | versions.py SSoT + schemas Refactor |
| `5f4a6c5` | 2 | Schicht D Validator + Tests D1-D4 + archive_score-Fixture-Patch |

**Smoke-Test-Status (zuletzt grün):** schemas 14/14 ✓ + archive_score 5/5 ✓ + skill 6/6 ✓ + Re-Validate-Sweep jsonl 28/28 PASS ✓.

---

### 📋 Offene Tasks (Resume-Reihenfolge)

| # | Task | Tool | Geschätzt |
|---|---|---|---|
| **A+B** | Mini-Patches: Doc-Typo + Plan-File D1-D4 Inline-Edit (Sammelcommit) | direkt Edit | 5 min |
| 3 | provenance_gate.py Schicht B (3.1a-3.1d) + 9/9 Smoke-Tests + Commit | subagent oder direkt | 45-60 min |
| 4 | backtest-ready-forward-verify SKILL.md Phase P3.5 + Authoritative-Sources + Commit | direkt Markdown | 15-20 min |
| 5 | _smoke_test.py Case 7+8 (P3.5 fail-close + Pipeline-Sequence) + Commit | subagent oder direkt | 30-40 min |
| 6 | SYSTEM.md + INSTRUKTIONEN §18.5 + CORE-MEMORY §10 + log.md Union-Scope + Commit | direkt Markdown | 20-30 min |
| **6.5** | **NEU: dynastie-depot SKILL.md Pre-Flight-Klausel + ma200_slope-Threshold** | direkt Markdown | 15-20 min |
| Verification | VC.1 + VC.2 End-to-End | inline | 10 min |
| First-Live-Run | !Analysiere V Q2 FY26 (heute 28.04. AMC ~22:00, Daten morgen früh) — **mit manuellem Pre-Append-Audit** | dynastie-depot Skill | ~2-3h |

---

### 🔧 Mini-Patches A+B (Sammelcommit, ~5 min)

**Patch A — Doc-Typo (LOW, Codex-Round-1):**
- File: `03_Tools/backtest-ready/migrate_tmo_28_block_coverage.py`
- Z. 64: `# TMO 6M -9.38% vs SPY 6M +6.55% (anchor 2026-10-22 → 2026-04-22)` → `2025-10-22 → 2026-04-22`

**Patch B — Plan-File D1-D4 Inline-Edit (MEDIUM, Codex-Round-1):**
- File: `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md`
- Step 2.1 (~ Z. 475-477+): D1/D2/D3/D4 Record-IDs umstellen
  - `2026-04-21_D1_vollanalyse` → `2026-04-21_AVGO_vollanalyse`
  - `2026-04-21_D2_vollanalyse` → `2026-04-22_AVGO_vollanalyse`
  - `2026-04-21_D3_rescoring` → `2026-04-23_AVGO_rescoring`
  - `2026-04-21_D4_vollanalyse` → `2026-04-24_AVGO_vollanalyse`
- Begründung: RECORD_ID_RE schemas.py:48 `[A-Z]{1,5}` für Ticker-Slot — "D1" enthält Ziffer, fail. Repo-Konvention: Plans inline-gepatcht (Patch-Note im Header), NICHT Header-Notice.
- Plan-Header optional: Patch-Note v3.1.1 mit Hinweis auf D1-D4-Korrektur.

**Sammelcommit-Message:**
```
fix(provenance-gate): codex-sparring resolution — doc-typo + plan-file-drift

Mini-Patches aus Codex-Round-1-Sparring:
- migrate_tmo_28_block_coverage.py:64 Anchor-Typo (2026-10-22 -> 2025-10-22)
- Plan v3.1 Step 2.1 D1-D4 Record-IDs auf AVGO+Datum (RECORD_ID_RE
  erlaubt nur [A-Z]{1,5} fuer Ticker-Slot; Code/Tests bereits in
  Commit 5f4a6c5 gefixt, Plan-Markdown drifted bis dahin).

Spec/Code unverändert, nur Doku.
```

---

### 🆕 Task 6.5 NEU — Pre-Flight-Klausel + ma200_slope-Threshold

**Codex-Round-2 HIGH-Befund:** TMO #28 zeigt `scores.technicals.gesamt=6` trotz null Roh-Werte pre-Migration. `quellen.insider` markiert `_carryover` explizit, `quellen.technicals` aber NICHT. Workflow-Bug kann morgen bei V Q2 / MSFT Q3 wieder auftreten — Provenance-Gate (Block-Coverage) hat keine Greifkraft.

**Was zu ergänzen:**

1. **`01_Skills/dynastie-depot/SKILL.md` Schritt 3 Output-Template-Erweiterung** (NEU `Score-Konsistenz-Pre-Flight v3.7.4`):
   ```markdown
   **Score-Konsistenz-Pre-Flight (v3.7.4, eingeführt 28.04.2026):**
   Vor Schritt 7 (Archiv-Write) prüfen: Ein Sub-Score != 0 ist NUR
   zulässig wenn (a) der korrespondierende Rohwert in `metriken_roh`
   nicht null ist, ODER (b) `quellen.<block>` enthält explizit ein
   legitimes `_carryover`-Suffix (Source-Token Whole-Word, Source-Prefix
   `ir_`, oder Reason-Token terminal — Carryover-Whitelist analog
   provenance_gate.py).

   Verstöße = Workflow-Bug. Beispiel: TMO #28 (23.04.) hatte
   `scores.technicals.trend_lage=3` aber `metriken_roh.kurs_vs_200ma_pct=null`,
   `quellen.technicals="yfinance_pre_briefing_22_04"` (kein _carryover) —
   Sub-Scores wurden offenbar vom 18.04.-Snapshot copy-paste übernommen
   ohne Roh-Werte-Update. Migration via Task 0.5 heilte metriken_roh,
   Algebra-Drift bleibt bis Score-Reconstruction-Tool ausstehend.
   ```

2. **`01_Skills/dynastie-depot/SKILL.md` Technicals-Section ma200_slope-Threshold-Doc:**
   ```markdown
   **ma200_slope-Threshold-Konvention (Schema-Literal {rising, falling, flat}):**
   - 21-Trading-Days-Slope `> +0.1%` → `rising`
   - 21-Trading-Days-Slope `< -0.1%` → `falling`
   - sonst `flat`
   Reproduzierbar via `yfinance.history(period='1y', end=<datum>)`,
   200MA via `rolling(200).mean()`, Slope = `MA200(t) / MA200(t-21) - 1`.
   ```

**Sync-Pflicht:** §18.2-Union-Scope = SKILL-File-Edit. Aber: kein Score/FLAG/Sparraten-Change → KEIN PORTFOLIO/CORE-MEMORY/Faktortabelle/score_history/config.yaml-Sync. Sync-Set: `01_Skills/dynastie-depot/SKILL.md + 00_Core/log.md` (System-Event-Pflicht).

**Commit-Message:**
```
fix(skill): dynastie-depot Pre-Flight-Klausel + ma200_slope-Threshold

Codex-Round-2 HIGH (Punkt 1+3, 28.04.): TMO #28 enthüllte Workflow-Bug —
Sub-Scores wurden offenbar vom Vor-Snapshot copy-paste übernommen ohne
Roh-Werte-Update; quellen markiert das nicht als _carryover. Pre-Flight-
Klausel in Schritt 3 Output-Template + ma200_slope-Threshold-Konvention
in Technicals-Section schließen die Drift-Lücke vor V/MSFT-Live-Runs.

Joint-Confidence-Lift: 92% -> 95%+ (mit V-Pre-Append-Audit).

Spec: docs/superpowers/specs/2026-04-21-score-append-provenance-gate-design.md (Folge-Hardening)
```

---

### 🛡️ V-Pre-Brief: Manueller Pre-Append-Audit (HIGH, Codex-4. Punkt)

**Im V_pre-earnings_2026-04-28.md (vor !Analysiere V Q2 morgen früh)** Workflow-Notiz ergänzen:

> **Pre-Append-Audit (Provenance-Gate-Hardening 28.04.2026):**
> Vor Schritt 7 prüfen pro Block (fundamentals/moat/technicals/insider/sentiment):
> - Wenn ein Sub-Score != 0 → korrespondierender Rohwert in `metriken_roh` darf nicht null sein, ODER `quellen.<block>` enthält legitimes `*_carryover`-Suffix.
> - Bei Verstoß → Sub-Score auf 0 setzen ODER Rohwert nachtragen ODER `quellen` mit `_carryover`-Markierung versehen.
> - Beispiel-Verstoß: TMO #28 (23.04.) — Pre-Flight-Klausel ab v3.7.4 fängt das.

Identische Notiz für MSFT Q3 (29.04. AMC) im `02_Analysen/MSFT_pre-earnings_2026-04-29.md`.

---

### 📊 Codex-Sparring-Bilanz (Session 28.04.)

- **Round 1** (Single-Pass): 0 HIGHs, 1 MEDIUM (Plan-File-Drift), 2 LOWs (Doc-Typo + 1 OK), 4 PASSes. Code-Diff der 3 Commits clean.
- **Round 2** (Reconcile auf 3 offene Punkte + 95%-Frage): **1 NEUER HIGH** (SKILL.md Pre-Flight-Klausel war Round-1 nicht aufgefallen, weil Frame anders war), 1 MEDIUM (Plan-Inline-Edit empfohlen), 1 LOW (ma200_slope-Doc), **1 NEUER 4. Punkt** (V/MSFT manueller Pre-Append-Audit) zum 95%-Lift.
- **Bilanz:** Reconcile-Round-2 fand HIGH dass Round-1 nicht hatte — Single-Pass-Default ist NICHT immer ausreichend bei semantischen Live-Run-Risk-Fragen. Memory-Hook `feedback_codex_sparring_heuristic.md` validiert: HIGH-Count ≥2 NACH Reconcile = ehrliche Heuristik.

---

### 📅 Critical Operational

- **HEUTE 28.04. AMC ~22:00:** V Q2 FY26 Earnings — Pre-Brief in `02_Analysen/V_pre-earnings_2026-04-28.md`. **First-Live-Run mit Provenance-Gate UND Pre-Flight-Klausel** geplant für 29.04. morgens.
- **MORGEN 29.04. AMC ~22:30:** MSFT Q3 FY26 Earnings — FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung).
- **30.04. morgens:** !Analysiere MSFT als Second-Live-Run.
- **01.05.:** Sparplan-Tag (EXUSA 825€ + reguläre Allokation). User-Action.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€, DEFCON v3.7
- AVGO 84 (FLAG Insider seit 27.04.), TMO 67 D3 (post-Q1-Upshift 23.04.), MKL 82
- 3 FLAGs aktiv: AVGO Insider, APH Score, MSFT CapEx
- Tavily-Key live PROD + Probe; Connector-UUID `0da14a12-...`

### Memory-Hooks aktiv

- feedback_review_via_codex_not_advisor.md — 2 Codex-Rounds in Session 28.04.
- feedback_codex_sparring_heuristic.md — **VALIDIERT**: Round-1-Single-Pass fand 0 HIGHs, Round-2-Reconcile fand 1 HIGH (Live-Run-Risk-Frame). Diff-Re-Review-Heuristik ist die billigste 2nd-Order-Versicherung.
- feedback_windows_python_crlf_text_mode.md — Migration-Helper byte-level Line-Ending-Preservation (0 ungewollte CRLF↔LF-Konvertierungen empirisch belegt).
- feedback_pre_commit_diff_inspection.md — alle 3 Commits via `git diff --cached --stat` vor commit verifiziert.
- feedback_onedrive_edit_collision.md — keine Kollisionen, alle Edits straight-through.

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `00_Core/CORE-MEMORY.md` §13 + `00_Core/PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*

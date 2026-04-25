# CodeRabbit-Findings — 00_Core-Refactor Tier 2

**Datum:** 2026-04-25 (Session 7, Step 9.5-9.6)
**Base-Commit:** `5f1b9f2` (last main-Commit before 2026-04-24 00:00)
**HEAD:** `920a602` (post-Codex-F1-Fix)
**Branch:** `refactor/00core-perfect-organization`
**CodeRabbit-Version:** 0.4.3 (WSL `/home/tobiatobia/.local/bin/coderabbit`)
**Run-Mode:** `coderabbit review --plain --type committed --base-commit 5f1b9f2 --config /dev/null`
**Findings total:** 26
**Raw-Output:** `coderabbit-raw.txt` (744 Zeilen)

## Triage-Summary

| Decision | Count |
|---|---|
| Fix (in-scope, blocker/regression) | 0 |
| Decline (out-of-scope, pre-existing, _extern, oder Vault-Sanierung #13 covered) | 26 |

**Verdict:** Kein 🔴 Blocker. Kein 🟡 Should mit Refactor-Drift-Bezug.
Alle 26 Findings betreffen entweder (a) `_extern/`-Skills (read-only Mirror), (b) pre-existing Skill/Vault-Inhalte ohne Bezug zum 00_Core-Refactor, (c) bereits bekannte Codex-Followups (Hygiene-Welle), oder (d) Verbesserungs-Vorschläge die Scope-Expansion erfordern.

---

## Decline-Liste (26)

### Out-of-scope: `_extern/` Read-Only Skills (3)

- **F1: `01_Skills/_extern/earnings-recap/SKILL.md:95-112`** — Edge case in price reaction calculation.
  **Decline:** `_extern/` ist read-only Skill-Mirror, untouched durch 00_Core-Refactor.
- **F8: `01_Skills/_extern/sec-edgar-skill/SKILL.md:316-325`** — Error handling try/except scope.
  **Decline:** `_extern/`, untouched.
- **F26: `01_Skills/_extern/sec-edgar-skill/SKILL.md:341-350`** — Invalid `Company.docs.search()` API call.
  **Decline:** `_extern/`, untouched.

### Out-of-scope: Vault-Daten / Video-Ingest-MDs (3)

- **F3: `07_Obsidian Vault/.../chapters.json:74-76`** — `1398` vs `1398.0` JSON type-consistency.
  **Decline:** Vault-Datenfile, kosmetisch, nicht Refactor-Scope.
- **F4: `07_Obsidian Vault/.../index.md:72-74`** — Chronologische Sortierung der Video-Einträge.
  **Decline:** Vault-Navigation, nicht Refactor-Scope.
- **F25: `07_Obsidian Vault/.../jake-van-clief…md:40-41`** — `manual_review: false` Inkonsistenz.
  **Decline:** Vault-Video-MD, nicht Refactor-Scope.

### Out-of-scope: Pre-existing Skills (untouched durch 00_Core-Refactor) (5)

- **F15: `01_Skills/quick-screener/SKILL.md:86-100`** — Plausibilitäts-Check Beispiele.
  **Decline:** quick-screener untouched.
- **F18: `01_Skills/non-us-fundamentals/SKILL.md:48-54`** — Ersatz-Ticker Spalte erklären.
  **Decline:** non-us-fundamentals untouched.
- **F19: `01_Skills/non-us-fundamentals/SKILL.md:236-239`** — yfinance Schema-Drift dokumentieren.
  **Decline:** non-us-fundamentals untouched.
- **F21: `01_Skills/non-us-fundamentals/SKILL.md:159-165`** — ROIC-Proxy Validierung.
  **Decline:** non-us-fundamentals untouched.
- **F24: `01_Skills/non-us-fundamentals/SKILL.md:147-158`** — RMS CapEx Workaround flagging.
  **Decline:** non-us-fundamentals untouched.

### Out-of-scope: Anderer Spec/Plan (claude-md-routing — separater Refactor) (3)

- **F6: `docs/superpowers/plans/2026-04-24-claude-md-routing-refactor.md:39-54`** — Resume-Recovery git-grep fragility.
  **Decline:** Anderer Refactor-Plan, nicht 00_Core-Scope.
- **F14: `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md:151-168`** — Routing-Table Default-Row.
  **Decline:** Anderer Spec.
- **F17: `docs/superpowers/specs/2026-04-24-claude-md-routing-refactor-design.md:246-258`** — AC #10 Diff-Cosmetic-Tolerance.
  **Decline:** Anderer Spec.

### Pre-existing Issues (nicht durch Refactor eingeführt) (3)

- **F12: `00_Core/APPLIED-LEARNING.md:19-32`** — 2 Bullets > 15 Wörter (Self-Consistency).
  **Decline:** APPLIED-LEARNING.md ist explizit unberührt durch 00_Core-Refactor (Spec §9 AC #5 Peer-Liste 6 Files schließt APPLIED-LEARNING aus). Pre-existing Drift, nicht Task-9-Scope.
- **F16: `00_Core/APPLIED-LEARNING.md:13`** — Header sagt "Stand: 14/20", Spec sagt "12 Bullets".
  **Decline:** Bezieht sich auf claude-md-routing-refactor Spec, pre-existing seit dort `+2 v2.5`-Bullets. Nicht 00_Core-Scope.
- **F2: `docs/superpowers/specs/_artifacts/2026-04-24-post-migration-refs.txt:165-177`** — `__pycache__`-Hits ausschließen.
  **Decline:** Artefakt-Grep-Snapshot ist Pre/Post-symmetrisch (Pre hatte ebenfalls keine `__pycache__`-Exclusion). Re-Runs würden symmetrisch updaten — kosmetisch, kein Refactor-Korrektheits-Issue. Tatsächliche `__pycache__`-Treffer sind Build-Artefakte (legitim grep-flagged).

### Already-Deferred Followups (Codex-Session-4 oder Hygiene-Welle) (2)

- **F22: `01_Skills/backtest-ready-forward-verify/SKILL.md:131-134`** — Parameter-Name `state_md_content` vs PORTFOLIO.md-Inhalt.
  **Decline-as-Deferred:** Verwandt aber **distinkt** zu Codex-Session-4 F3 (Test-Fixture-Namen `state_*` in `_smoke_test.py:450-471,505-507`). Beides sind Naming-Hygiene auf demselben semantischen Drift (`state_*` → `portfolio_*`), aber in verschiedenen Dateien (Skill-SKILL.md-Docstring vs Test-Fixture). Funktion akzeptiert beide Inhalt-Formate (Smoke `[5/6] PASS`), kein Verhalten-Impact. Defer beide gemeinsam auf nächste Hygiene-Welle (zusammen mit Codex-Followup `03_Tools/backtest-ready/README.md:130` v3.7.2-Doku-Drift).
- **F23: `07_Obsidian Vault/.../wiki/concepts/CLAUDE-md-Konstitution.md:50`** — Tier-2 STATE-Split-Status veraltet.
  **Decline-as-Deferred:** Bereits abgedeckt durch PIPELINE.md #13 Vault-Concept-Seiten-Sanierung (AC #17 Follow-up). Keine separate Aktion in Task 9 nötig.

### Style/Refactor-Suggestions (Verbesserung, kein Refactor-Mangel) (7)

- **F5: `00_Core/TOKEN-RULES.md:23-24`** — Sync-Pflicht-Bullet sub-strukturieren.
  **Decline:** Bullet wurde in `920a602` (Codex-F1-Fix) gerade auf §18 v2 umgestellt; Sub-Bullet-Aufteilung würde §Regeln-Pattern (1 Bullet = 1 Regel) brechen. Detailbreakdown lebt korrekt in INSTRUKTIONEN §18 (verlinkt). Future Refinement-Kandidat.
- **F7: `03_Tools/system_audit/checks/pipeline_ssot.py:50-59`** — SKIP → FAIL bei fehlendem PIPELINE.md.
  **Decline:** Semantik-Change am Audit-Behavior. PIPELINE.md existiert; SKIP ist intentionaler Fallback für hypothetische Tooling-Pfade. Spec §9 AC #3/#9 verifizieren Existenz separat. Future-Refinement, kein Refactor-Mangel.
- **F9: `00_Core/SYSTEM.md:19`** — Lange Morning-Briefing-Bullet aufsplitten.
  **Decline:** Inhalt 1:1 aus altem STATE.md migriert (kein Refactor-Eingriff). Strukturelle Restrukturierung wäre Scope-Erweiterung über die reine STATE-Split-Migration hinaus. Future-Cleanup.
- **F10: `00_Core/CORE-MEMORY.md:48-50`** — §3-Note nach §13 verschieben.
  **Decline:** §3 wurde in Codex Session-4 F1-Fix (`0e45989`) explizit drift-fixed; aktuelle Note ist intentionaler historischer Pointer. Größere Restrukturierung (§3 → §13) hätte Tier-2-Spec ändern müssen — Out-of-spec.
- **F11: `00_Core/INSTRUKTIONEN.md:557-583`** — 3-Tier-Modell explizit machen (§27.3 v2).
  **Decline:** §27.3 v2 wurde in Task-6 (`9cce107`) reformuliert + Codex-reconciled. Aktuelle Wording ist konsistent zur Spec §6 Primary/Hub/Projection-Dreiteilung. Future-Refinement-Vorschlag.
- **F13: `00_Core/INSTRUKTIONEN.md:294-308`** — Multi-Event-Union enforcement-Mechanismus fehlt.
  **Decline:** Spec §18.2 + §10.2 (User-Antwort 3 = "Union als formaler §18-Vertrag, Verantwortung beim Analysten") sind explizit ratifizier — keine Auto-Enforcement vorgesehen. Audit-Check-Vorschlag wäre Scope-Expansion (separater Task).
- **F20: `00_Core/PORTFOLIO.md:31`** — Change-Log-Narrativen nach CORE-MEMORY §12 verschieben.
  **Decline:** Plan Task-1 / Spec §6.1 PORTFOLIO-Design enthält intentional Change-Log-Snippets als operative Kontext-Ankündigung (komplementär zu CORE-MEMORY §12 für Per-Ticker-Detail). AC #2 Size-Cap 90 Zeilen wird gehalten (57). Future-Refinement bei Größen-Pressure.

---

## Folge-Aktionen

- **Keine Fix-Commits** — alle Findings declined.
- **AC #15 Re-Verification:** Bereits durch Codex-F1-Fix (`920a602`) als PASS bestätigt; CodeRabbit-Run touched diesen AC nicht.
- **AC #16 progressiv:** Dieses Artefakt + `codex-reconciliation-report.md` + bevorstehendes `user-signoff.md` erfüllen sequenziell AC #16 Review-Gate-Documentation.
- **Optional:** Mehrere Decline-Findings (F5/F7/F9/F11/F13/F20) sind legitime Refinement-Vorschläge. Können bei Bedarf in PIPELINE.md als 🔵 Long-Term-Hygiene-Task aufgenommen werden — User-Entscheidung in Step 9.7.

---

*🦅 CodeRabbit-Findings v1.0 | Dynasty-Depot 00_Core-Refactor Tier 2 | Step 9.6 Triage*

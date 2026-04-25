# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-25 Abend — Phase 2 Plan-File geschrieben + Codex-Plan-Review GO-WITH-FIXES alle 12 Findings addressed (Plan v1.1); Implementation auf nächste Session via subagent-driven-development geschoben

## Verweise
- [STATE.md](STATE.md) — Hub (Critical-Alerts + Last-Audit + Navigation)
- [PORTFOLIO.md](PORTFOLIO.md) — Live-State (default-load bei Session-Start)
- [PIPELINE.md](PIPELINE.md) — offene Pläne + Long-Term-Gates
- [SYSTEM.md](SYSTEM.md) — DEFCON / Briefing / Audit / Infra
- [CORE-MEMORY.md §13](CORE-MEMORY.md#13-system-lifecycle-history) — System-Lifecycle-Chronik (kanonische Initiative-Historie)
- [Faktortabelle.md](Faktortabelle.md) — Score-Detail pro Ticker

---

## 🔄 RESUME-INPUT (next session — Phase 2 Implementation via subagent-driven-development)

**Auftrag:** Plan-File geschrieben + Codex-Reviewed (GO-WITH-FIXES, alle 12 Findings addressed). Nächste Session: **Implementation via `superpowers:subagent-driven-development`** des Plans `docs/superpowers/plans/2026-04-25-system-audit-rework.md` (v1.1). 8 Tasks, 7 Commits, ~25 neue Tests, CORE 8→14 Checks.

### Plan-File-Status

**Lokation:** `docs/superpowers/plans/2026-04-25-system-audit-rework.md` (v1.1)

**Plan-Sequenz (final, post-Codex-Review):**
1. **PyYAML-Dependency-Preflight** (Orchestrator-Gate, vor §18 wegen yaml-Hard-Import) — Sweep-Spec §228 Caveat explizit zitiert als Begründung
2. **§18-Parity** (F1+F2+F4) — README.md / briefing-sync-check.ps1 / SKILL.md / INSTRUKTIONEN.md
3. **Skill-Frontmatter-Completeness** (F8) — schließt skill_version.py:82 silent-continue-Lücke
4. **Header-Freshness** (F6+F9) — Placeholder-FAIL + 30d-WARN, header-zone scoped (erste 12 Zeilen, P2-06)
5. **Top-Level-Governance-Parity** (F11) — Slash-Doku-Count + Flag-Coverage gegen live CORE
6. **Cross-Source-Reverse** (F18 NEU) — Vault entities/satelliten/ → config.yaml, FRONTMATTER-only ticker-extraction (P2-08)
7. **Pointer-Completeness** (F12 narrowed) — CLAUDE.md ## Pointer-section-scoped backtick-Pfade existence (P2-03+P2-09)
8. **Defer-Doku** — Modus-Restrukturierung / Plan-vs-Live-Drift / ZIP-Mtime → PIPELINE Backlog

**Acceptance:** CORE 8→14, Smoke-Tests 59→84 (25 neu), Sweep-Coverage F1-F18 von 0/8 auf 8/8.

### Codex-Plan-Review-Findings (alle addressed in Plan v1.1)

**Codex-Review agentId:** `a2862e6a730e2ecca`

| Severity | Finding | Status |
|----------|---------|--------|
| BLOCK | P2-01 Zahlen-Inkonsistenz (5 vs 6 Module, CORE-Total) | DONE — Goal+Acceptance reconciled |
| BLOCK | P2-02 Task 6 PORTFOLIO-Claim ohne Code | DONE — Scope-Narrowing auf Vault only mit Begründung (config→PORTFOLIO bereits durch existing cross_source.py abgedeckt) |
| BLOCK | P2-03 Task 7 Section-Level fehlt | DONE — Scope auf Pointer-Tabelle existence narrowed + Section-Anchor implementiert |
| SHOULD | P2-04 Governance --no-write-WARN ohne Spec-Backing | DONE — uniform error außer --minimal-baseline (einzige spec-gestützte Exception) |
| SHOULD | P2-05 _live_core_count Reentrancy doc | DONE — module-cache + sys.path-Mutation kommentiert |
| SHOULD | P2-06 Header-Freshness Body-Match-Risk | DONE — HEADER_SCAN_LIMIT_LINES=12 |
| SHOULD | P2-07 §18-Parity 80-char-Heuristik | DONE — line-based co-occurrence statt proximity-window |
| SHOULD | P2-08 TICKER_RE FP-Risk | DONE — Frontmatter-only ticker-extraction, kein Filename-Stem-Fallback |
| SHOULD | P2-09 Pointer Section-Scoping | DONE — `_extract_pointer_section`, regression-test added |
| SHOULD | P2-10 Test-Count-Delta | DONE — 84 final (25 neu, vorher overschätzt ~95) |
| SHOULD | P2-11 OneDrive per-Task | DONE — Pre-Commit-Edit-Checkpoint 3-Step-Protokoll im Pre-Task |
| INFO | P2-12 Sequence-Reorder Spec §228 Quote | DONE — explizit zitiert in Empirische Sequenz |

### TODO Session-Start (Implementation via Subagent)

**Tool:** `Skill(skill="superpowers:subagent-driven-development")` mit Plan-Argument `docs/superpowers/plans/2026-04-25-system-audit-rework.md`.

**Pre-Task-Checks (ohne Subagent, manuell vor Spawn):**
1. `git status --short` — soll wieder die übliche pre-existing-dirty-Liste (STATE.md, Rebalancing_Tool.xlsx) zeigen + nichts unter `03_Tools/system_audit/`
2. `python "03_Tools/system_audit/_smoke_test.py"` — 59/59 PASS Baseline grün
3. `python 03_Tools/system_audit.py --core --no-write` — rc=1 mit 4/8 PASS + 2 known-WARN + 2 known-FAIL (PIPELINE Item #4 bestätigt)

**Sequenz:** 8 Tasks à frischer Subagent. Two-Stage-Review zwischen Tasks. Zwischen Task 5 + Task 6 ein Live-Run-Checkpoint (`--core --no-write`) zum Validieren dass keine Regressionen entstanden sind.

**OneDrive-Edit-Collision-Risk:** Plan operationalisiert das Pre-Commit-3-Step-Protokoll in der Pre-Task-Section. Subagent-Driver muss vor jedem Task-Commit den Check applizieren — sonst Sync-Konflikt-Risiko bei `_smoke_test.py` und `__init__.py` (in 7 von 8 Tasks editiert).

### Code-Pattern-Hinweise für Subagent-Implementation

Identisch zu Plan-File §"Code-Vorbild" — `skill_version.py:58-147` ist die Referenz. AuditContext / CheckResult / FailureDetail / Status-Eskalation alle dort dokumentiert.

### Standing-Pre-existing-Dirty
- `00_Core/STATE.md` — Last-Audit-Timestamp älter, wird durch finale Audit-Run nach Task 8 aktualisiert
- `00_Core/SESSION-HANDOVER.md` — wird mit dieser Session-Ende aktualisiert
- `03_Tools/Rebalancing_Tool_v3.4.xlsx` — pre-existing dirty, weiterhin ungeklärt

### Memory-Updates (bereits persistiert)
- `feedback_review_via_codex_not_advisor.md` — Reviews/Second-Opinions immer Codex, nie advisor()
- `feedback_onedrive_edit_collision.md` — Edit-Collision-Pattern (vor Edit Editor-Status checken)

### Wichtige Calibration-Notiz
F3 (`_forward_verify_helpers.py:25, 257-259`) bleibt **INFO, nicht FIX** — SKILL.md Z126 + Code-Kommentar dokumentieren Teil-Gate-Trade-off explizit konsistent. Codex-RECONCILED VALID. Nicht als §18-Verletzung re-klassifizieren — auch nicht als score_event_parity-Failure (Plan-Code achtet darauf, weil File nicht in `score_event_parity.py`-Audit-Targets-Liste).

---

## Standing-Focus 30 Tage (unverändert seit Tier-2-Finalize)

- **28.04. V Q2 FY26** — D2-Entscheidung (Technicals-Reversal-Gate)
- **29.04. MSFT Q3 FY26** — FLAG-Review (CapEx/OCF bereinigt <60%)

---

## 📜 Handover-Policy (seit 2026-04-25 — Tier 2 Follow-up)

Nur **aktiver** RESUME-INPUT-Block in dieser Datei. Historie kanonisch in:
- **`git log`** — jeder Session-Ende-`handover:`-Commit ist die Banner-Chronik
- **`CORE-MEMORY.md` §13** — System-Lifecycle-History
- **`PIPELINE.md`** — Strikethrough-DONE-Items mit Datum + Commit-Hash

Pflege-Pflicht: Bei Session-Ende den aktiven Block durch den neuen ersetzen — nicht anhängen.

---

*🔁 SESSION-HANDOVER.md v2.0 | Dynasty-Depot | Slim-Resume — Policy B*

# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-27 ~19:40 — **Phase 3.5 Probe-Trigger-Update v3.0.6 DEPLOYED + GET-Verify PASS (9/9 Marker)**. Manual-Run via Desktop App queued für heute 20:00 MESZ (User-Action). Resume nach Run mit Output-Verify B1-B9.

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** `1a3cf51` (v3.0.6-Hotfix-Commit, lokal + origin/main synchron). Vorgänger-Chain: `6011a5d` (handover-Doc) → `b51205a` (Phase-1) → `91d0f02` → `e777ff2`.

**v3.0.6-Hotfix-Plan-File:** `docs/superpowers/plans/2026-04-27-briefing-v3.0.6-hotfix.md` (18 Tasks). Nicht ins Repo committed (Standing-Convention: Plan-Files separater Commit oder gar nicht — Plan wird in nächster Session bei Resume reaktiviert).

**v3.0.5-Plan-File:** `docs/superpowers/plans/2026-04-27-briefing-v3.0.5-implementation.md` (8 Phasen, weiterhin gültig — Phase 1+2 DONE, Phase 3 FAIL→3.5 Hotfix, Phase 4-6 queued nach Probe-Re-Test).

### Was diese Session GETAN hat

**Phase 3 Adversarial-Test (T-Stale-Shibui) — FAIL mit 4 echten Cracks:**
1. WebSearch-Fallback bei Tavily-Domain-Block (Anti-Fallback v3.0.4 nicht stark genug)
2. Saturday-Score-Date-Substitut für V (Anti-Improvisation v3.0.4 nicht stark genug)
3. SCHRITT 4.8 Self-Check-Gate hat Unmapped-Tool nicht gefangen
4. Tag-Schema-Erfindung `[websearch@<domain>]` ad-hoc

**Codex-Review-Pass (2 Runden Single-Pass):**
- Round 1 (4× HIGH + 1× MEDIUM): alle FAILs bestätigt + neuer FAIL-4 (Tag-Erfindung als eigenständiges Vergehen)
- Round 2 Diff-Re-Review (1× HIGH + 2× MEDIUM): Empty-Results-Anti-Inferenz + EU-Feiertag-Edge + Regex-Konsistenz

**v3.0.6 Hotfix-Edits committed + pushed (`1a3cf51`):** 9 Edits (7× Prompt + 2× Spec):
- Critical-Guards 3 neue Bullets (Tools verboten / Domain-Subset-Retries verboten / Score-Datum-Substituts verboten)
- SCHRITT 4.8 Tool-Provenance-Check-Bullet
- §4.5(E) Tool-Nicht-Verfügbar-Klasse + Domain-Block-Hinweis + Empty-Results-Anti-Inferenz
- §6F-4 Calendar-Mismatch-Sub-Case (Listing-Markt-Feiertag NYSE/Euronext Paris)
- Spec §9 T6 Anti-Fabrikation-Sub-Assert (6) + Regex-Konsistenz `tavily@`

**Phase-3-Pre-Step (Probe-Tavily-Key-Swap) DONE:** Probe-Trigger `trig_01XYuQ5mugsvZGZD4K52rjXh` hat seit 15:27 UTC neuen Tavily-Key `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`. Shibui-Connector unverändert.

### NEXT-SESSION-RESUME — Manual-Run-Output-Verify + Phase 4-6

**Trigger:** „Phase 3.5 Output verifizieren" oder Output-Paste direkt.

**Stand JETZT (19:40):**
- Probe-Trigger v3.0.6 ist deployed (`updated_at: 2026-04-27T17:38:50Z`). 9/9 v3.0.6-Marker im GET-Roundtrip verifiziert.
- Tavily-Connector unverändert mit neuem Key `tvly-dev-4er43M-...`.
- Body-Konstruktion-Erkenntnis (für Memory): RemoteTrigger update mit `body` als Inline-Record-Object funktioniert auch bei ~25k-char-Bodies, wenn JSON sauber escaped (ASCII-mode `\uXXXX` für Umlaute, sauberer Newline-Escape `\n`). Vorherige Versuche failten weil Body unsauber war. Phase-1+2-Split (kleiner Test → full body) hat bestätigt dass Tool-Call-Frontend records korrekt klassifiziert.

**User-Action heute 20:00 MESZ:**
1. Claude Desktop App → Routines → tavily-probe → Run now.
2. Vollständigen Output reinpasten (Briefing-Header bis "NAECHSTES GROSSES EVENT").

**Resume-Step danach:**
1. Output-Verify gegen 9 B1-B9-Asserts (Plan Task 17): kein WebSearch-Fallback (B1), kein Domain-Subset-Retry (B2), kein Saturday-Substitut (B3), SCHRITT-4.8-Tool-Provenance (B4), Allow-List-Tags only (B5), tool-unavailable-Header bei mapped-tool-fail (B6), Empty-Results = `Keine material News` ohne Inferenz (B7), §6F-4 Calendar-Mismatch wörtlich (B8), Provenance-Tags konsistent (B9).
2. Bei PASS → Phase 4-6 (T6 voll-test + T1/T3/T4 Retest + Prod-Deploy v3.0.6) per `docs/superpowers/plans/2026-04-27-briefing-v3.0.5-implementation.md`.
3. Sync-Pflicht (Plan Task 18) am Ende: log.md + CORE-MEMORY.md (§13 Lifecycle) + SYSTEM.md + PIPELINE.md.

### Operativ unverändert

- 11 Satelliten, Sparraten 285€, V 28.04. / MSFT 29.04. Earnings-Briefs in `02_Analysen/`
- Pre-Earnings-Briefs ready: `02_Analysen/V_pre-earnings_2026-04-28.md`, `02_Analysen/MSFT_pre-earnings_2026-04-29.md`
- DEFCON v3.7 unverändert, alle Scores unverändert, FLAG-Status unverändert
- Tavily-Key live in PROD + Probe (alter Key revoked)

### Critical Operational (zeitkritisch — verdrängt v3.0.6-Probe-Re-Test wenn Konflikt)

- **28.04.** V Q2 FY26 Earnings (~22:00 MEZ) — D2-Entscheidung. Brief ready.
- **29.04.** MSFT Q3 FY26 Earnings (~22:30 MEZ) — FLAG-Review CapEx/OCF. Brief ready.

### Wichtige Erkenntnisse + Memory-Hooks

- **OneDrive Edit-Collision** (Memory `feedback_onedrive_edit_collision.md`) — Diff-Verify nach Edits beachten. War in dieser Session nicht relevant.
- **Pre-Commit-Diff-Inspection** (Memory `feedback_pre_commit_diff_inspection.md`) — vor Commit `git diff --cached` prüfen. War kritisch in `1a3cf51`-Commit (Standing-Dirty draußen).
- **Codex-Sparring-Heuristik** (Memory `feedback_codex_sparring_heuristic.md`) — Single-Pass-Default + Diff-Re-Review-Pfad bei HIGH-Count ≥2. Beide Runden in dieser Session waren effektiv.
- **Codex-statt-advisor** (Memory `feedback_review_via_codex_not_advisor.md`) — bestätigt, weiter so.
- **NEU für Memory (sollten als Auto-Memory geschrieben werden):** Tool-Call-Inline-Pattern für RemoteTrigger update mit großem body — full ccr-Schema-replace inkl. environment_id + session_context + events.data.{parent_tool_use_id, session_id, type, uuid} nötig, da partial-update auf ccr-Subtree als full-replace interpretiert wird.

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `CORE-MEMORY.md §13` + `PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*

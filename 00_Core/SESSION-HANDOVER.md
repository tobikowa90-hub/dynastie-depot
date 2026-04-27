# 🔁 Session-Übergabeprompt — Dynastie-Depot

**Aktualisiert:** 2026-04-27 ~22:00 — **Track-5a/5b-Decision A1-Final via superpowers-Brainstorming + Codex-Sparring DONE.** Mini-Sweep „Pipeline verschlanken" + Pipeline-DONE-Cleanup auch durch. Resume-Trigger ab hier: **„!Analysiere V"** (29.04. morgens nach AMC-Release) ODER **„5a Skill-Promotion"** (post-Earnings 30.04.+).

### 🟢 Resume-Stand

**Branch:** `main`. **HEAD:** zuletzt `e6521b2` (PIPELINE-Cleanup) + heutige Decision-Commits. Push synchron mit `origin/main`.

**Heutige Commits 27.04.** (chronologisch): `0e5300c` (v3.0.6 Phase-3.5 Sync) → `33d9933` (SNPS) → `caddd0c` (Vault-Cleanup) → `db66d99` (KONTEXT/Faktortabelle Watchlist-Reconcile) → `c08ed89` (Rebalancing) → `9d74a40` (Watchlist-XLSX-Sync) → `f1194e8` (Mini-Sweep A-F) → `e6521b2` (PIPELINE-DONE-Cleanup) → Decision-Commit (Track-5a/5b A1-Final).

### Was diese Session GETAN hat

**1. Phase 3.5 Probe-E2E-Verify PASS (Briefing v3.0.6)** — Manual-Run #2 ~20:50 MESZ via Tavily-Connector-UI-Reattach (UUID-Rotation `4a633350-...` → `0da14a12-...`) lieferte alle 9 B1-B9-Marker (6 hart). Auto-Memory `feedback_tavily_connector_uuid_rotation.md` geschrieben.

**2. QuickCheck-Sweep 22 Tickers** (Option B / 10 high-priority) — Score-Drifts erkannt + reconciled: SNPS 79→76, SPGI 79→74, FICO 70→67, EXPN 74→61. KONTEXT.md/Faktortabelle/INSTRUKTIONEN §7 gezogen.

**3. Rebalancing Mai-Plan** — ING/Scalable Live-Beträge eingelesen (Depotwert 10.384,20€ + Cash 1.550,53€). User-Entscheidung: 01.05. Sparplan EXUSA 825€ + reguläre Allokation. V Q2 Earnings 28.04. AMC abwarten, dann Re-Eval.

**4. Mini-Sweep „Pipeline verschlanken" (Items A-F)** — AVGO §7-Anker 85→84, BRI 4→5-Layer Vault-Sub-Drift, PIPELINE #11/#14 triagiert (Frozen/monitor-only), SystemAudit `--core` 9/14 PASS, SESSION-HANDOVER aktualisiert.

**5. PIPELINE-DONE-Cleanup** — 6 DONE-Items + 1 DONE-Trigger entfernt (#1/#4/#5/#12/#13/#15 + 23.04. TMO-Trigger). Numbering-Convention dokumentiert (Stable, keine Renumber bei DONE-Removal — Gaps zeigen auf CORE-MEMORY §13 + git log). v1.0 → v1.1.

**6. Track-5a/5b A1-Final-Decision via Brainstorming-Skill + Codex-Sparring** — Decision-Spec `docs/superpowers/specs/2026-04-27-track5a-5b-decision.md`. Codex-Verdict A1: bei aktuellem Sparraten-Volumen 285€/Monat realistisch <20bps/Jahr Alpha aus Regime-aware DCA → 5b Effort/Reward kollabiert. **5a freigegeben** für Execution post-V/MSFT-Earnings (~2-3h, 9 Tasks per existierendem Plan); **5b deferred** mit Re-Activation-Triggern (Sparrate >1.000€/Monat ODER Depotwert >50.000€ ODER Regime-Aware-Schmerz). Dashboard v2 entkoppelt — Architektur bleibt unverändert, Sequenzierung post-5a. PIPELINE.md v1.1 → v1.2.

### NEXT-SESSION-RESUME — V/MSFT Earnings + 5a Skill-Promotion

**Trigger-Kandidaten:**
- **„!Analysiere V"** — 29.04. morgens nach 28.04. AMC-Release. Pre-Brief `02_Analysen/V_pre-earnings_2026-04-28.md`. D2-Entscheidung (Technicals-Reversal?).
- **„!Analysiere MSFT"** — 30.04. morgens nach 29.04. AMC-Release. Pre-Brief `02_Analysen/MSFT_pre-earnings_2026-04-29.md`. FLAG-Review CapEx/OCF (bereinigt <60% = Auflösung, >60% = Veto-Verschärfung).
- **„5a Skill-Promotion"** — post-Earnings (30.04.+). Plan-File `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md` (9 Tasks). Skill-Move `_extern/sec-edgar-skill/` → `01_Skills/sec-edgar-skill/`, EdgarTools-Install + `set_identity('Tobias Kowalski tobikowa90@gmail.com')`. Eskalations-Fallback (NICHT auto in `!Analysiere`). ~2-3h. Execution via `superpowers:executing-plans` oder `superpowers:subagent-driven-development`.
- **„Phase-4-6 Briefing v3.0.6"** — wenn Earnings durch und 5a optional fertig: T6 voll-Test + T1/T3/T4-Retest gegen v3.0.6 + Prod-Deploy auf `trig_01PyAVAxFpjbPkvXq7UrS2uG`.

**Earnings-Kalender:**
- **28.04.** V Q2 FY26 AMC (~22:00 MESZ) + Conf Call 23:00 MESZ.
- **29.04.** MSFT Q3 FY26 AMC (~22:30 MESZ).
- **28.04.** SNPS + SPGI Q1 (parallel — kein direkter Re-Bewertungs-Druck, beide Watchlist-Status; ggf. Faktortabelle-Update bei klarem Beat/Miss).
- **01.05.** Sparplan-Tag — EXUSA 825€ + reguläre Allokation + ING-Überweisung 1.107,72€ (User-Action).

### Operativ unverändert

- 11 Satelliten, Sparraten 285€, DEFCON v3.7
- AVGO Score 84 (post-17.04. Forward), MKL 82, SNPS 76 (post-Drift), SPGI 74 (post-Drift), TMO 63 (post-Q1-Upshift)
- FLAG-Status unverändert
- Tavily-Key live in PROD + Probe; Connector-UUID `0da14a12-...`; alter Key revoked

### Critical Operational

- **28.04.** V Q2 FY26 Earnings — D2-Entscheidung
- **29.04.** MSFT Q3 FY26 Earnings — FLAG-Review CapEx/OCF
- **30.04.+** 5a Skill-Promotion freigegeben (post-Earnings) → dann Phase-4-6 Briefing v3.0.6 → dann Dashboard v2
- **01.05.** Sparplan-Tag (EXUSA 825€ + reguläre Allokation)

### Memory-Hooks aktiv

- `feedback_tavily_connector_uuid_rotation.md` (NEU 27.04.) — Key-Rotation = Pflicht-UI-Reattach, nicht nur Body-Update
- `feedback_review_via_codex_not_advisor.md` — Reviews via Codex (heute genutzt für 5a/5b-Sparring, single-pass ausreichend)
- `feedback_codex_sparring_heuristic.md` — Single-Pass Default; heute 1× Pass mit klarem Verdict, kein Reconcile-Loop nötig
- `feedback_onedrive_edit_collision.md`, `feedback_pre_commit_diff_inspection.md` — Standing-Practices

---

## 📜 Handover-Policy

Nur **aktiver** RESUME-INPUT-Block. Historie kanonisch in `git log` (handover-Commits) + `CORE-MEMORY.md §13` + `PIPELINE.md`. Bei Session-Ende: aktiven Block ersetzen, nicht anhängen.

*🔁 SESSION-HANDOVER.md v2.0 | Slim-Resume — Policy B*

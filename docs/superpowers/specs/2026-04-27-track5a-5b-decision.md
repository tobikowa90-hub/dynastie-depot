# Track 5a/5b Decision Spec — A1-Final

**Datum:** 2026-04-27
**Brainstorming-Skill:** `superpowers:brainstorming` (Sparring-Loop Claude ↔ Codex ↔ User)
**Status:** decided
**Entscheidungsträger:** User (Tobias) mit Codex-Adversarial-Review

---

## Decision

**A1-Final:** 5a SEC EDGAR Skill-Promotion ja, 5b FRED Macro-Regime-Filter deferred mit harten Re-Activation-Triggern.

## Rahmen

User-Priorisierung (explizit): (1) Speed-of-Implementation, (2) Strategic Value, (3) Maintenance-Burden „so wenig wie möglich aber soviel wie nötig", (4) Scientific Anchor (Bonus, kein Muss).

## Erwogene Approaches

| | Approach | Verworfen weil |
|---|----------|----------------|
| A1 | 5a YES, 5b NO | (gewählt) |
| A2-revised | 5a + 5b + Excel-Hook über bestehendes Rebalancing_Tool | 5b strategisch nicht gerechtfertigt bei aktuellem Volumen (siehe Codex-Sparring) |
| A3 | 5b first, 5a später | „No-Enforcer"-Manual-Multiplikation verstößt Maintenance-Filter |

## Codex-Sparring-Verdict (2026-04-27 abend)

| # | Stress-Test | Verdict | Befund |
|---|-------------|---------|--------|
| 1 | Empirical Strategic Value 5b | 🔴 CHALLENGE | Bei 285€/Monat-Volumen Regime-aware DCA realistisch <20bps/Jahr, evtl. nahe null nach Friktionen. B19-Bull/Bear-Asymmetrie überträgt sich nicht 1:1 auf monatlich-DCA |
| 2 | Backtest Look-Ahead-Risk | 🟢 CONFIRM | Plan-Lösung via ALFRED-Vintages + Release-Lag-Logik vertretbar wenn konsequent implementiert (ISM-Revisions sind versteckter Kanal) |
| 3 | Regime-Flip-Frequency | 🔴 CHALLENGE | Empirisch 1-3/Jahr mit Clustering um Rezessionen, ISM volatil. Ohne Hysterese-Smoothing wird Composite instabil — fehlt im aktuellen 5b-Plan |
| 4 | Excel-Hook Failure-Modes | 🟡 CONFIRM-mit-Caveat | „User vergisst Zelle einzutragen" ist real → STATE.md/JSONL-Read allein reicht nicht, braucht Empfohlener-vs-Eingetragener-Vergleich. Formel-Korruption durch geschützte Spalte abdeckbar |
| 5 | 5a-Sequenzierung | 🟢 CONFIRM | Standalone-5a kontraproduktiv; Bundle mit 5b oder Defer bis echter Konflikt — beste Sequenz |

**Codex-Final:** „A2-revised ist operativ durchdacht, aber Stress-Test 1 zeigt das strategische Fundament ist schwach. 5a macht Sinn als leichtgewichtige Hygiene (2-3h), danach Defer 5b bis mehr Kapitalvolumen die Regime-Modulation materiell macht."

## Begründung A1-Final

### Pro 5a
- 9 Tasks, ~2-3h Effort, kein User-Action nötig (Skill liegt schon in `_extern/`)
- Eskalations-Fallback für Daten-Konflikte in `!Analysiere` (10-K-Textsuche, Form-4, defeatbeta-Konflikt) — opt-in, kein Maintenance-Tax
- B21-B24 Sci-Anchor deferred, aber XBRL-Primär-Architektur via `edgartools` ist solide
- Dashboard v2 unabhängig — entkoppelt sich von 5a-Frage

### Pro 5b-Defer (statt -Reject)
- Regime-aware DCA wird strategisch wertvoll bei höherem Sparraten-Volumen oder größerem Depotwert (compoundende Skalierung)
- Plan ist gut spezifiziert (15 Tasks, FRED/ALFRED-Logik, Grid-Search), Re-Activation jederzeit möglich
- Codex-Caveat (Hysterese-Smoothing fehlt) wird vor Re-Activation in Plan ergänzt
- Defer mit klaren Triggern verhindert „wir haben es vergessen"-Drift

### Re-Activation-Trigger 5b (mind. einer)
1. Sparrate > 1.000€/Monat (≈ 3.5x current)
2. Depotwert > 50.000€ (≈ 5x current ~10.000€)
3. Konkret aufgetretener Regime-Aware-Schmerz (z.B. Drawdown wo Reduktion sichtbar besser gewesen wäre, oder Bull-Phase wo Erhöhung sichtbar besser gewesen wäre)

Bei Re-Activation: vor Implementation Plan-Update mit Hysterese-Smoothing-Layer (Stress-Test #3 Caveat) + Empfohlener-vs-Eingetragener-Detector (Stress-Test #4 Caveat).

## Implementations-Konsequenzen

| File | Aktion |
|------|--------|
| `00_Core/PIPELINE.md` | #6 (5a) → 🔴 ready ab post-Earnings 30.04.+; #7 (5b) → 🔵 Deferred mit Re-Activation-Triggern; #7a (Decision-Point) → DONE; #7b (Dashboard v2) entkoppelt |
| `07_Obsidian Vault/.../log.md` | Decision-Eintrag mit Codex-Sparring-Befund |
| `00_Core/SESSION-HANDOVER.md` | Resume-Trigger nach Earnings: „5a Skill-Promotion" |

## Out of Scope

- Implementation 5a — separater Plan-Run via `superpowers:executing-plans` gegen existierendes `docs/superpowers/plans/2026-04-20-track5a-edgar-skill-promotion.md`
- 5b-Plan-File bleibt unverändert in `docs/superpowers/plans/` archiviert; Re-Activation-Update kommt erst bei Trigger
- Dashboard v2 eigene Planung post-5a

---

*Spec finalisiert 2026-04-27 ~21:50 MESZ nach Codex-Sparring-Round (single-pass, 2× CHALLENGE konsistent → kein Reconcile-Loop nötig).*

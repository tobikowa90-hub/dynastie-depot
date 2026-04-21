# Score-Append Provenance-Gate — Design Spec

**Datum:** 2026-04-21
**Status:** draft (Spec-Review pending)
**Scope-ID:** A1 (nur Schmerzpunkt #2 — Score-Append)
**Architektur-Variante:** E (Hybrid: Pipeline-Gate B + reduziertes Schema-Guard D)
**Nachfolge-Artefakt:** Implementation-Plan in separater Session

---

## 1. Kontext

### 1.1 Auslöser
Brainstorm-Session 2026-04-21, ausgelöst durch Frage nach Integration externer Tools (Context7, Token-Optimizer, Obsidian-Skills). Der Filter über 33 Tool-Kandidaten ergab: der stärkste Hebel ist **nicht in der Liste** — ein intern baubarer Pre-Append-Gate an score_history.jsonl adressiert belegte Schmerzpunkte direkter als jedes externe Tool.

### 1.2 Belegte Schmerzpunkte im Projekt
1. **v3.0.3-Morning-Briefing-Halluzination** (Remote-Trigger-Run, Agent erfand Yahoo-Fallback für US-Ticker).
2. **V-Backfill-Projektion** (17.04.2026): V-Score 86 wurde als `analyse_typ="vollanalyse"` persistiert, war aber tatsächlich ein Rescoring ohne frische Forward-Analyse. Advisor-Review am 18.04. ergab Forward-Score 63 (D2) — echte Vollanalyse.
3. **Multi-Source-Drift** (Memory-Regel `feedback_multi_source_drift_check`).

### 1.3 Scope-Entscheidung (Codex-Sparring Runde 2)
- **In-Scope:** Schmerzpunkt #2 (Score-Append-Provenance-Gate).
- **Out-of-Scope:**
  - #1 Morning Briefing: Remote-Trigger läuft in Anthropic-Cloud, lokaler Validator kann Run nicht gaten. Adressiert durch v3.0.4 Prompt-Guard §3a.
  - #3 Multi-Source-Drift: Governance/Behavior-Regel, kein deterministischer Gate-Punkt. Bleibt in Memory + INSTRUKTIONEN §27.4.

### 1.4 Sparring-Chronik (Codex-Runden 1-5)
| Runde | Entscheidung | Ergebnis |
|---|---|---|
| 1 | Welcher der 3 Schmerzpunkte validator-geeignet? | #2 als einziger mit deterministischem Gate-Punkt |
| 2 | Scope-Breite (A1/A2/A3/B) | **A1: nur #2** |
| 3 | Architektur-Variante (D/B/A) | **Variante E = B + reduziertes D** |
| 4 | Completeness-Definition + Kurs-Referenz-Platzierung | **D2 (Block-Coverage) + K2 (nur in B)** |
| 5 | Sektion-3-Details (Data Flow, Tests, Mapping) | **P3.5 vor P3**, Platzhalter-Blacklist statt Regex, Integration-Test Pflicht |

---

## 2. Goal

Verhindern, dass Rescoring- oder unvollständige Forward-Runs fälschlich als `analyse_typ="vollanalyse"` in `05_Archiv/score_history.jsonl` persistiert werden.

Deterministischer fail-close Gate vor dem Append-Call, plus Schema-Sicherheitsnetz gegen direkte `archive_score.py`-Aufrufe.

---

## 3. Non-Goals

- Morning-Briefing-Halluzinations-Prävention (Remote-Cloud-Problem, nicht lokal gatebar).
- Multi-Source-Drift-Prevention (kein deterministischer Gate-Punkt, bleibt Governance).
- Backfill-Run-Validierung (eigene Pipeline `backfill_scores.py`, eigenes Scope).
- `--force`-Override-Flag: bewusst nicht implementiert (analog bestehender archive_score.py-Policy). Recovery bei Schema-Drift über Migration/Fixup-Command, nicht via Gate-Bypass.

---

## 4. Architektur

**Variante E: zwei disjunkte Schichten mit bewusster Redundanz.**

```
Draft-JSON
    │
    ▼
┌───────────────────────────────────────────────────┐
│  Skill-Pipeline (backtest-ready-forward-verify)   │
│                                                   │
│  P1   parse_wrapper(args)                         │
│  P2a  check_freshness(repo_root)                  │
│  P2b  parse_state_row (tripwire)                  │
│  P3.5 ★ check_provenance() ─ NEU, fail-close      │ ← Schicht B
│  P3   build_migration_event (Δ-Gate, conditional) │
│  P4   archive_score.py --dry-run ──────┐          │
│  P5   archive_score.py (real append)   │          │
│  P6   git add                          │          │
└─────────────────────────────────────────┼─────────┘
                                          │
                                          ▼
                            ┌──────────────────────┐
                            │ ScoreRecord.         │
                            │   model_validate     │ ← Schicht D
                            │ + Block-Coverage     │   (NEU)
                            │ + bestehende Checks  │
                            └──────────────────────┘
                                          │
                                          ▼
                                  score_history.jsonl
```

### 4.1 Schicht B — Pipeline-Gate mit Kontext
- Eingabe: Pipeline-Zustand (P2a-Freshness-Ergebnis) + Record-Draft + `skill_meta`.
- Prüft Provenance-Behauptung gegen Pipeline-Evidenz.
- Kann Skill-Pipeline-Kontext nutzen, den Pydantic-Validatoren nicht sehen.

### 4.2 Schicht D — Schema-Guard (reduziert)
- Eingabe: nur `ScoreRecord`-Felder (kein Pipeline-Kontext).
- Minimale Plausibilitäts-Hürde für Direkt-CLI-Aufruf (`archive_score.py --file draft.json`).
- **Explizit kein** Freshness-Beweis-Anspruch (das macht B).

### 4.3 Reihenfolge P3.5 **vor** P3
P3 kann wegen `skill_meta`-Parse-Fehler abbrechen. Wenn P3.5 nach P3 läuft, entfällt der blocking Provenance-Check bei Δ-Gate-Fail. Reihenfolge: P2b → **P3.5** → P3 → P4.

---

## 5. Komponenten

### 5.1 `03_Tools/backtest-ready/versions.py` (NEU)
Single Source of Truth für DEFCON-Version.

```python
"""Dynasty-Depot: DEFCON version constants. Single source of truth."""
from typing import Final

DEFCON_ACTIVE_VERSION: Final[str] = "v3.7"
```

Referenziert von: `schemas.py` (bei `_check_forward_version`), `provenance_gate.py`, SKILL.md-Text.

### 5.2 `03_Tools/backtest-ready/provenance_gate.py` (NEU)

```python
def check_provenance(
    record_dict: dict,
    freshness_missing: list[str],
    skill_meta: dict | None,
) -> tuple[bool, list[str]]:
    """Pipeline-Gate P3.5. Fail-close bei erster Verletzung.

    Returns: (passed, reasons). passed=False → FAIL phase=P3.5.
    """
```

**Prüflogik (in Reihenfolge, fail-close bei erster Verletzung):**

| # | Bedingung | FAIL-Kriterium | Fehlermeldung |
|---|---|---|---|
| 1 | `source="backfill"` | — (skip) | — |
| 2 | `analyse_typ="vollanalyse"` + `freshness_missing != []` | True | `vollanalyse requires fresh session (missing: {files}); reclassify as rescoring or complete workflow` |
| 3 | `analyse_typ="vollanalyse"` + `kurs.referenz != "close_of_score_datum"` | True | `vollanalyse requires fresh kurs (referenz='{actual}')` |
| 4 | `analyse_typ="rescoring"` + `skill_meta is None` | True | `rescoring requires skill_meta for Δ-Gate` |
| 5 | `analyse_typ="delta"` + `source != "forward"` | True | `delta is forward-only` |
| 6 | `defcon_version != versions.DEFCON_ACTIVE_VERSION` | True | `defcon_version '{actual}' drift vs. active '{expected}'` |
| 7 | Platzhalter in `quellen`-Feldern | True | `placeholder source '{value}' in quellen.{field}` |
| 8 | `skill_meta` gesetzt + `skill_meta["migration_to_version"] != defcon_version` | True | `skill_meta.migration_to_version='{meta}' inconsistent with record.defcon_version='{record}' (recycled skill_meta)` |

**Platzhalter-Policy (feldspezifisch, Check #7):**

```python
PLATZHALTER_BLACKLIST: Final[frozenset[str]] = frozenset({
    "unknown", "tbd", "todo", "placeholder", "none", "na", "n/a", "?"
})

def is_placeholder(value: str) -> bool:
    stripped = value.strip().lower()
    return stripped in PLATZHALTER_BLACKLIST or bool(re.fullmatch(r"\?+", stripped))
```

Gilt **nur** für die 5 Pflicht-`quellen`-Felder (`fundamentals`, `technicals`, `insider`, `moat`, `sentiment`), **nicht** für `notizen` o.ä.

### 5.3 `03_Tools/backtest-ready/schemas.py` — Erweiterung

Neue Validator-Methode in `ScoreRecord`:

```python
@model_validator(mode="after")
def _check_vollanalyse_block_coverage(self) -> ScoreRecord:
    """Schicht D (K2: KEIN Kurs-Referenz-Check, KEIN Freshness-Beweis-Anspruch).

    Bei source='forward' + analyse_typ='vollanalyse':
    Mindestens 1 Rohmetrik muss in jedem der 5 Score-Blöcke befüllt sein.
    """
    if self.source != "forward" or self.analyse_typ != "vollanalyse":
        return self

    # Block-Mapping: Rohmetrik-Felder → Score-Block
    BLOCK_FIELDS: dict[str, tuple[str, ...]] = {
        "fundamentals": (
            "fwd_pe", "p_fcf", "net_debt_ebitda", "current_ratio",
            "goodwill_pct_assets", "capex_ocf_pct_gaap", "capex_ocf_pct_bereinigt",
            "roic_gaap_pct", "roic_bereinigt_pct", "wacc_pct",
            "fcf_yield_pct", "sbc_revenue_pct", "sbc_ocf_pct",
            "accruals_ratio_pct", "tariff_exposure_pct",
            "operating_margin_ttm_pct",
        ),
        "moat": ("gm_trend_3j_pct_p_a",),
        "technicals": (
            "rel_strength_sp500_6m_pct", "kurs_vs_200ma_pct", "ma200_slope",
        ),
        "insider": (),  # Roh-Felder für insider werden nicht in metriken_roh geführt
        "sentiment": (
            "eps_revisions_up_90d", "eps_revisions_down_90d", "pt_dispersion_pct",
        ),
    }

    empty_blocks: list[str] = []
    for block, fields in BLOCK_FIELDS.items():
        if not fields:
            continue  # insider: Roh-Metriken nicht in metriken_roh → skip
        filled = any(getattr(self.metriken_roh, f) is not None for f in fields)
        if not filled:
            empty_blocks.append(block)

    if empty_blocks:
        raise ValueError(
            f"vollanalyse block-coverage violation: no raw metrics filled in blocks: "
            f"{empty_blocks}. Fill at least one field per block or reclassify analyse_typ."
        )
    return self
```

**Besonderheit `insider`:** Keine Roh-Felder in `metriken_roh` (alle Insider-Daten sind Sub-Scores, keine Rohwerte). Block wird vom Coverage-Check übersprungen. Dokumentieren im Inline-Kommentar.

### 5.4 `01_Skills/backtest-ready-forward-verify/SKILL.md` — Update

- Phase-Tabelle (Section 4): P3.5-Zeile einfügen **vor P3**, P3 entsprechend verschieben.
- Invocation-Block: neue Phase im Pipeline-Diagramm.
- Report-Format (Section 6): neue Line für P3.5-FAIL.
- Version-Referenz: `versions.DEFCON_ACTIVE_VERSION` statt hard-coded String.

---

## 6. Data Flow

```
P1 parse_wrapper(args)
   → record_dict, skill_meta
   [FAIL P1 bei Parse-Fehler]

P2a check_freshness(repo_root)
   → freshness_missing: list[str]
   [WARNING im Report, nicht blockierend]

P2b parse_state_row(ticker, STATE.md)
   → validates record gegen STATE.md
   [FAIL P2b bei Drift]

P3.5 check_provenance(record_dict, freshness_missing, skill_meta)  ← NEU
    → (passed, reasons)
    [FAIL P3.5 bei passed=False — blockiert vor P3/P4/P5/P6]

P3 build_migration_event(skill_meta, forward_score) [conditional]
   → injiziert migration_event in record_dict
   [STOP-Signal bei |Δ|>5, nicht blockierend auf Archiv-Ebene]

P4 archive_score.py --dry-run
   → ScoreRecord.model_validate (inkl. neuer Block-Coverage-Check = Schicht D)
   [FAIL P4 bei Schema-Verletzung]

P5 archive_score.py (real append)
   [FAIL P5 bei Runtime-Fehler]

P6 git add 05_Archiv/score_history.jsonl
   [FAIL P6, manuelle Recovery]
```

---

## 7. Error Handling

### 7.1 Exit-Code-Konvention
- `0` — Erfolg
- `1` — Validation/Drift/Duplicate/Provenance-Fail
- `2` — IO-Fehler

### 7.2 Recovery-Matrix

| Phase | Fehler | Recovery |
|---|---|---|
| P3.5 | freshness-missing + vollanalyse | Workflow vervollständigen (STATE/Faktortabelle/log.md touch) ODER `analyse_typ` auf `rescoring` korrigieren |
| P3.5 | kurs-referenz ≠ `close_of_score_datum` | Frischen EOD-Kurs ziehen + Referenz setzen |
| P3.5 | rescoring ohne skill_meta | `skill_meta` mit `migration_from_version` / `migration_to_version` / `expected_algebra_score` setzen |
| P3.5 | delta + source=backfill | Delta ist per Definition forward — `source="forward"` setzen |
| P3.5 | defcon-version-drift | Record-Version korrigieren; bei Schema-Migration via separater Migration/Fixup-Pipeline (nicht Gate-Bypass) |
| P3.5 | platzhalter in quellen | Echte Quelle eintragen (z.B. `shibui`, `defeatbeta`, `yahoo_eod`, `openinsider+sec_edgar`) |
| P3.5 | skill_meta-recycling | `migration_to_version` an `defcon_version` angleichen; bei absichtlicher Migration: beide auf neue Version setzen |
| P4 (D) | block-coverage violation | Min. 1 Rohmetrik in jedem Score-Block (außer insider) befüllen; bei bewusst unvollständiger Analyse: `analyse_typ="rescoring"` |

### 7.3 Kein `--force`-Flag
Bewusste Entscheidung (Codex Runde 5): Override entwertet Schutzwirkung. Recovery nach Schema-Drift läuft über separaten Migration/Fixup-Command, nicht via Gate-Bypass.

---

## 8. Test-Strategie

### 8.1 Unit-Tests in `provenance_gate.py`
Smoke-Tests analog zu existierendem `archive_score.py::_smoke_tests()`:

| # | Szenario | Erwartung |
|---|---|---|
| 1 | Valid vollanalyse, freshness_missing=[], fresh kurs, alle 5 quellen gesetzt | passed=True, reasons=[] |
| 2 | vollanalyse + freshness_missing=["STATE.md"] | passed=False, matched reason |
| 3 | vollanalyse + kurs.referenz="close_2026-04-15" (stale) | passed=False |
| 4 | rescoring ohne skill_meta | passed=False |
| 5 | delta mit source="backfill" | passed=False |
| 6 | Backfill-Record | passed=True (skip) |
| 7 | defcon_version="v3.5" + active="v3.7" | passed=False |
| 8 | quellen.insider="unknown" | passed=False |
| 9 | skill_meta.migration_to_version="v3.7" + record.defcon_version="v3.5" | passed=False |

### 8.2 Unit-Tests in `schemas.py`
Neue Test-Cases in `_smoke_tests()`:

| # | Szenario | Erwartung |
|---|---|---|
| D1 | vollanalyse mit min. 1 Rohmetrik in jedem der 4 geprüften Blöcke | parses OK |
| D2 | vollanalyse mit 0 Rohmetriken im fundamentals-Block | `ValidationError: block-coverage violation` |
| D3 | rescoring mit 0 Rohmetriken | parses OK (Skip-Condition) |
| D4 | Backfill mit 0 Rohmetriken | parses OK (Skip-Condition) |

### 8.3 Integration-Test (Pflicht, nicht optional)
In `01_Skills/backtest-ready-forward-verify/_smoke_test.py`:
- Synthetischer Vollanalyse-Draft mit Provenance-Fail (z.B. `freshness_missing=["STATE.md"]`).
- Durchläuft P1 → P2a → P2b → P3.5.
- Assert: Exit-Code 1, Error-Output enthält `FAIL phase=P3.5`, P4/P5/P6 nicht ausgeführt (keine Mutation an `score_history.jsonl`).

Rationale (Codex Runde 5): Bei fail-close hängt die Schutzwirkung an korrekt verdrahteter Pipeline. Unit-Tests der Einzelfunktionen garantieren das nicht.

---

## 9. §-Mapping / Datei-Änderungen

| Datei | Änderung | Status |
|---|---|---|
| `03_Tools/backtest-ready/versions.py` | **NEU** — Single Source of Truth für `DEFCON_ACTIVE_VERSION` | Neu erstellen |
| `03_Tools/backtest-ready/provenance_gate.py` | **NEU** — `check_provenance()` + Smoke-Tests | Neu erstellen |
| `03_Tools/backtest-ready/schemas.py` | `_check_vollanalyse_block_coverage`-Validator + Test-Cases D1-D4 | Erweitern |
| `01_Skills/backtest-ready-forward-verify/SKILL.md` | Phase-Tabelle (Section 4): P3.5 vor P3; Version-Referenz auf `versions.py`; Report-Format (Section 6) um P3.5-Line | Update |
| `01_Skills/backtest-ready-forward-verify/_smoke_test.py` | Integration-Test Pflicht: Provenance-Fail-Szenario, Exit-Code-Assertion | Erweitern |
| `00_Core/INSTRUKTIONEN.md §18` | Sync-Pflicht erweitern: „Provenance-Gate fail-close in P3.5 ist Teil der Append-Pipeline" | Update (bei Go-Live) |
| `00_Core/STATE.md` System-Zustand | Zeile: „Provenance-Gate aktiv seit YYYY-MM-DD" | Update (bei Go-Live) |
| `00_Core/CORE-MEMORY.md §10` Audit-Log | Go-Live-Eintrag mit First-Run-Nachweis | Append (bei Go-Live) |

### 9.1 Bewusst KEINE Änderung
- `config.yaml`: keine konfigurativen Parameter (Platzhalter-Liste hard-coded, Version in `versions.py`).
- `00_Core/Faktortabelle.md` Legende: P3.5-Status nicht user-facing sichtbar, keine Legende-Änderung nötig.
- Neuer INSTRUKTIONEN-§: Applied-Learning-Stufe reicht bis Evidenz nach 3-4 realen Läufen; Promotion zu neuem § erst bei belegtem systemischem Bedarf.

---

## 10. Offene Punkte / Follow-ups

- **Live-Test-Trigger:** First-Run ist nächste `!Analysiere`-Vollanalyse nach Deploy. Kandidat: TMO Q1 am 23.04.2026 (bereits in STATE.md Trigger-Liste).
- **Versions-Evolution:** Bei Migration v3.7 → v3.8 muss `versions.py::DEFCON_ACTIVE_VERSION` aktualisiert werden. Einzige Code-Stelle, keine Cross-File-Suche nötig.
- **Evidence-basierte Promotion zu INSTRUKTIONEN-§:** Nach 3-4 realen Anwendungen Applied-Learning-Scan: wurde Gate tatsächlich verwendet? Wurde ein realer Fehler verhindert? Bei Ja → INSTRUKTIONEN §-Promotion.
- **§33 Skill-Self-Audit (B19) erfüllt:** Status-Matrix in `07_Obsidian Vault/.../Wissenschaftliche-Fundierung-DEFCON.md` wurde während Brainstorming konsultiert. Ergebnis: keine blockierenden Befunde, zwei Future-Compatibility-Notes (s.u.). Audit-Log-Eintrag in CORE-MEMORY §10 bei Go-Live.
- **Future-Compatibility B20 (Sheppert GT-Score):** SKILL.md `backtest-ready-forward-verify` erwähnt B20 als Future-Option für §29.1-Aktivierung (In-the-Loop-Acceptance-Check neben §28.2 Δ-Gate). P3.5-Provenance-Gate und B20-GT-Score sind **disjunkte** Phasen: P3.5 prüft Provenance-Behauptungen (Append-Time), B20 prüft Overfitting-Robustheit via Composite-Objective (Parameter-Loop-Time). Bei §29.1-Aktivierung (Review 2028 oder erste Parameter-Variation) können beide koexistieren — ggf. als neue Phase P3.7 nach P3 Δ-Gate. Nicht Teil dieses Specs.
- **Future-Compatibility B18 (Palomar Seven Sins):** §29.5 Seven-Sins-Pre-Flight ist SOFORT aktiv bei Migration-Events (§28), nicht bei Standard-Forward-Appends. Unser P3.5 läuft bei jedem Append. Falls bei Migration-Runs zusätzliche Seven-Sins-Pre-Flight-Checks gebraucht werden, wären sie eine separate Migration-Pipeline-Phase, nicht Erweiterung von P3.5.
- **Implementation-Plan:** Wird in separater Session via `superpowers:writing-plans`-Skill erstellt.

---

## 11. Design-Prinzipien (als Self-Check festgehalten)

- **Disjunkte Verantwortung B ↔ D:** B prüft Pipeline-Kontext, D prüft nur Record-Felder. Keine überlappenden Prüfungen außer bewusster Redundanz.
- **Fail-close beide Schichten:** Kein Override-Flag, kein Weitergang bei erster Verletzung.
- **Single Source of Truth für Version:** Nur `versions.py` kennt die aktive DEFCON-Version.
- **Bypass-Resistenz gegen zwei realistische Wege:** (1) Direkt-CLI-Aufruf an `archive_score.py` → D greift; (2) Pipeline-Kontext-Lüge (synthetisch aufgeblasene `metriken_roh`) → B greift via Freshness-Check + Version-Konsistenz.
- **Minimal invasive Integration:** Keine Schema-Migration der 27 existierenden Records, kein Breaking Change, keine neuen Pflichtfelder in `ScoreRecord`.
- **Evidence-basierte Promotion:** Applied Learning jetzt, INSTRUKTIONEN erst bei belegtem Bedarf (konsistent zu Memory-Regel „keine Regeln auf Vorrat").

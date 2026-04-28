# Score-Append Provenance-Gate — Design Spec

**Datum:** 2026-04-21 (Spec v1) · **Refresh:** 2026-04-28 (Spec v2)
**Status:** v2 — Plan-v3-aligned, drift-patch + carryover-policy + STATE→PORTFOLIO-sweep
**Scope-ID:** A1 (nur Schmerzpunkt #2 — Score-Append)
**Architektur-Variante:** E (Hybrid: Pipeline-Gate B + reduziertes Schema-Guard D)
**Nachfolge-Artefakt:** Implementation-Plan `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (Plan v3)

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

### 1.4 Sparring-Chronik (Codex-Runden 1-7)
| Runde | Entscheidung | Ergebnis |
|---|---|---|
| 1 | Welcher der 3 Schmerzpunkte validator-geeignet? | #2 als einziger mit deterministischem Gate-Punkt |
| 2 | Scope-Breite (A1/A2/A3/B) | **A1: nur #2** |
| 3 | Architektur-Variante (D/B/A) | **Variante E = B + reduziertes D** |
| 4 | Completeness-Definition + Kurs-Referenz-Platzierung | **D2 (Block-Coverage) + K2 (nur in B)** |
| 5 | Sektion-3-Details (Data Flow, Tests, Mapping) | **P3.5 vor P3**, Platzhalter-Blacklist statt Regex, Integration-Test Pflicht |
| 6 | Plan-v3-Drift-Refresh (28.04.) Round 1 — Plan-v2 vs aktueller Repo-Stand | A+ mit 2 HIGHs: §18-Union-Scope (Task 6) + Carryover-Policy für legitime `*_carryover`-Suffixe |
| 7 | Plan-v3-Drift-Refresh (28.04.) Round 2 — HIGH-Resolution | parse_state_row-Helper bereits auf PORTFOLIO migriert (verifiziert via Recon-Agent); Carryover-Policy = Substring-Whitelist (Option C, User-approved) |
| 8 | Spec-v2 Single-Pass-Review (28.04.) — Carryover-Bypass-Hardening | HIGH: naive `any(tok in stripped...)` umgehbar via Reason-Token-Kombination (`pre_gate_xyzzy_carryover`). Verschärft auf Whole-Word-Source-Match + Source-Prefix (`ir_`) + Terminal-Reason-Match. Tests 8e-8i ergänzt für Bypass-Coverage |

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
| 7 | Platzhalter in `quellen`-Feldern (mit Carryover-Whitelist) | True | `placeholder source '{value}' in quellen.{field}` |
| 8 | `skill_meta` gesetzt + `skill_meta["migration_to_version"] != defcon_version` | True | `skill_meta.migration_to_version='{meta}' inconsistent with record.defcon_version='{record}' (recycled skill_meta)` |

**Platzhalter-Policy mit Carryover-Whitelist (Check #7, v2 Refresh 28.04.):**

Der V1-Draft (21.04.) prüfte nur eine flache `PLATZHALTER_BLACKLIST` (`unknown`, `tbd`, `?` etc.). Das fängt aber legitime Carryover-Suffixe nicht sauber ab. Forward-Workflows generieren regelmäßig Quellen-Strings wie `gurufocus_carryover` (Wert aus letztem Run übernommen, da neue Quelle nicht refresht wurde) oder `skip_window_delta_lt_14d_pre_score_carryover` (Workflow-Grund-Carryover bei Pre-Score-Bridge). Diese sind **legitim** und dürfen nicht als Platzhalter blockieren.

**Codex-Review Spec-v2 (28.04.) HIGH-Finding:** Erste Iteration nutzte naive Substring-Whitelist (`any(tok in stripped ...)`) — das wäre durch Reason-Tokens kombinatorisch umgehbar gewesen (`pre_gate_xyzzy_carryover` würde via `pre_gate`-Substring akzeptiert). Das untergräbt den Schutzzweck. **Verschärfte Policy v2:** Source-Tokens müssen als ganzes Token im Stem vorkommen (split auf `_`); Reason-Tokens müssen am Stem-Ende stehen (terminal); `ir_`-Prefix als special-case (Company-IR-Pages: `ir_apple_carryover` etc.).

```python
PLATZHALTER_BLACKLIST: Final[frozenset[str]] = frozenset({
    "unknown", "tbd", "todo", "placeholder", "none", "na", "n/a", "?",
})

# Source-Tokens: echte Datenquellen, müssen als Whole-Word im Stem vorkommen
# (split('_') enthält den Token genau)
CARRYOVER_SOURCE_TOKENS: Final[frozenset[str]] = frozenset({
    "gurufocus", "defeatbeta", "shibui", "openinsider", "sec_edgar",
    "yahoo", "zacks", "yfinance", "alphaspread", "tavily",
    "stocktitan", "benzinga", "afm", "amf", "eodhd",
})

# Source-Prefixes: dynamische Source-Familien (Company-IR-Pages)
# Stem muss mit diesem Prefix beginnen
CARRYOVER_SOURCE_PREFIXES: Final[tuple[str, ...]] = ("ir_",)

# Reason-Tokens: Workflow-Begründungen, müssen am Stem-Ende stehen
# (Stem == Token ODER Stem endet auf '_' + Token)
CARRYOVER_REASON_TERMINAL: Final[frozenset[str]] = frozenset({
    "skip_window", "pre_score", "pre_gate", "bridge", "carry_from",
})

_RE_QUESTION_MARKS = re.compile(r"\?+")


def _is_placeholder(value: str) -> bool:
    """True wenn value (case-insensitive, getrimmt) ein Platzhalter ist.

    Carryover-Policy (v2 Refresh 28.04., Codex-HIGH-Hardening):
    - Bare PLATZHALTER_BLACKLIST-Treffer (`unknown`, `tbd`, `?`...) → True.
    - Pure `?+` → True.
    - `*_carryover`-Suffix → akzeptiert (False) NUR wenn:
      (a) Stem enthält Source-Token als Whole-Word (split auf `_`), z.B.
          `gurufocus_carryover` → tokens=['gurufocus'] → match; ODER
      (b) Stem startet mit Source-Prefix (`ir_`), z.B.
          `ir_apple_carryover` → startswith('ir_') → match; ODER
      (c) Stem endet auf Reason-Token (terminal), z.B.
          `skip_window_delta_lt_14d_pre_score_carryover` → endswith('_pre_score') → match;
          `bridge_carryover` → stem == 'bridge' → match.
    - `_carryover` allein, `xyzzy_carryover`, `pre_gate_xyzzy_carryover`,
      `gurufocus` mit nicht-Whole-Word-Match → True (kein anerkannter Stamm).
    """
    stripped = value.strip().lower()
    if stripped in PLATZHALTER_BLACKLIST:
        return True
    if _RE_QUESTION_MARKS.fullmatch(stripped):
        return True
    if not stripped.endswith("_carryover"):
        return False  # kein Carryover, kein Platzhalter (z.B. 'gurufocus' selbst)

    stem = stripped[: -len("_carryover")]
    if not stem:
        return True  # bare "_carryover"

    # (a) Source-Token als Whole-Word im Stem
    stem_tokens = stem.split("_")
    if any(t in CARRYOVER_SOURCE_TOKENS for t in stem_tokens):
        return False

    # (b) Source-Prefix
    if any(stem.startswith(p) for p in CARRYOVER_SOURCE_PREFIXES):
        return False

    # (c) Reason-Token terminal (Stem == Token oder Stem endet auf '_' + Token)
    for r in CARRYOVER_REASON_TERMINAL:
        if stem == r or stem.endswith("_" + r):
            return False

    return True  # Carryover ohne anerkannten Stamm → Platzhalter
```

**Akzeptiert (passed=True):** `gurufocus`, `gurufocus_carryover`, `skip_window_delta_lt_14d_pre_score_carryover`, `defeatbeta_carryover`, `openinsider+sec_edgar`, `yfinance_carryover`, `bridge_carryover`, `ir_apple_carryover`.

**Lehnt ab (passed=False):** `unknown`, `tbd`, `?`, `???`, `_carryover`, `unknown_carryover`, `xyzzy_carryover`, `placeholder`, `n/a`, **`pre_gate_xyzzy_carryover`** (Reason nicht terminal — Codex-HIGH-Bypass-Test), **`skip_window_xyzzy_carryover`** (Reason nicht terminal), **`gurufocusxyz_carryover`** (kein Whole-Word-Match — `gurufocusxyz` ist ein anderer Token).

Gilt **nur** für die 5 Pflicht-`quellen`-Felder (`fundamentals`, `technicals`, `insider`, `moat`, `sentiment`), **nicht** für `notizen` o.ä.

### 5.3 `03_Tools/backtest-ready/schemas.py` — Erweiterung

Neue Validator-Methode in `ScoreRecord`:

```python
@model_validator(mode="after")
def _check_vollanalyse_block_coverage(self) -> ScoreRecord:
    """Schicht D (K2: KEIN Kurs-Referenz-Check, KEIN Freshness-Beweis-Anspruch).

    Bei source='forward' + analyse_typ='vollanalyse':
    Mindestens 1 Rohmetrik muss in jedem der 4 geprüften Score-Blöcke befüllt sein.
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
            # Dual-Naming: _sync_rel_staerke_alias spiegelt _pct ↔ _staerke,
            # aber any() prüft beide Felder direkt — funktioniert auch wenn
            # Sync-Validator (mode=after, sequenziell vor diesem) den Alias
            # nicht populiert hat.
            "rel_strength_sp500_6m_pct", "rel_staerke_sp500_6m_pct",
            "kurs_vs_200ma_pct", "ma200_slope",
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

**Besonderheit `technicals` Dual-Naming (v2 28.04.):** Der bestehende `_sync_rel_staerke_alias`-Validator (mode=after, läuft sequenziell VOR `_check_vollanalyse_block_coverage` per Pydantic v2-Reihenfolge) spiegelt die EN/DE-Aliase `rel_strength_sp500_6m_pct` ↔ `rel_staerke_sp500_6m_pct`. Block-Coverage-Validator prüft trotzdem **beide Field-Aliase** in der Tuple — `any()` deckt den Fall ab, dass der Alias-Sync (z.B. bei zukünftigen Refactors oder bei Test-Fixtures, die nur ein Feld setzen) nicht greift. Defensiv günstiger, kein Risiko von Eigenkonsistenz-Verlust.

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

P2b parse_state_row(ticker, state_md_content)
   → validates record gegen PORTFOLIO.md (Funktionsname stabil aus Legacy-Zeit STATE.md;
     Inhalt wird aus PORTFOLIO.md Portfolio-Tabelle parsed seit 00_Core-Split 22.04.2026)
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
| P3.5 | freshness-missing + vollanalyse | Workflow vervollständigen (PORTFOLIO/Faktortabelle/log.md touch) ODER `analyse_typ` auf `rescoring` korrigieren |
| P3.5 | kurs-referenz ≠ `close_of_score_datum` | Frischen EOD-Kurs ziehen + Referenz setzen |
| P3.5 | rescoring ohne skill_meta | `skill_meta` mit `migration_from_version` / `migration_to_version` / `expected_algebra_score` setzen |
| P3.5 | delta + source=backfill | Delta ist per Definition forward — `source="forward"` setzen |
| P3.5 | defcon-version-drift | Record-Version korrigieren; bei Schema-Migration via separater Migration/Fixup-Pipeline (nicht Gate-Bypass) |
| P3.5 | platzhalter in quellen | Echte Quelle eintragen (z.B. `shibui`, `defeatbeta`, `yahoo_eod`, `openinsider+sec_edgar`); legitime Carryover-Suffixe (`gurufocus_carryover` etc.) sind via Whitelist akzeptiert — nur bare/unknown-Carryover blockieren |
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
| 2 | vollanalyse + freshness_missing=["PORTFOLIO.md"] | passed=False, matched reason |
| 3 | vollanalyse + kurs.referenz="close_2026-04-15" (stale) | passed=False |
| 4 | rescoring ohne skill_meta | passed=False |
| 5 | delta mit source="backfill" | passed=False |
| 6 | Backfill-Record | passed=True (skip) |
| 7 | defcon_version="v3.5" + active="v3.7" | passed=False |
| 8 | quellen.insider="unknown" / Variants TBD/?/N/A/PLACEHOLDER | passed=False (alle Variants) |
| 8c | quellen.fundamentals="gurufocus_carryover" (legitimer Source-Token whole-word) | passed=True |
| 8d | quellen.fundamentals="xyzzy_carryover" (kein anerkannter Stamm) | passed=False |
| 8e | quellen.fundamentals="skip_window_delta_lt_14d_pre_score_carryover" (Reason terminal) | passed=True |
| 8f | quellen.fundamentals="pre_gate_xyzzy_carryover" (Reason nicht terminal — Bypass-Test, Codex-HIGH) | passed=False |
| 8g | quellen.fundamentals="bridge_carryover" (Reason als kompletter Stem) | passed=True |
| 8h | quellen.fundamentals="ir_apple_carryover" (Source-Prefix) | passed=True |
| 8i | quellen.fundamentals="gurufocusxyz_carryover" (kein Whole-Word-Source-Match) | passed=False |
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
- Synthetischer Vollanalyse-Draft mit Provenance-Fail (z.B. `freshness_missing=["PORTFOLIO.md"]`).
- Durchläuft P1 → P2a → P2b → P3.5.
- Assert: Exit-Code 1, Error-Output enthält `FAIL phase=P3.5`, P4/P5/P6 nicht ausgeführt (keine Mutation an `score_history.jsonl`).

Rationale (Codex Runde 5): Bei fail-close hängt die Schutzwirkung an korrekt verdrahteter Pipeline. Unit-Tests der Einzelfunktionen garantieren das nicht.

**Test-Mock-Konvention (v2 28.04.):** `check_freshness` ist Live-Helper, der `git status` gegen `REQUIRED_TOUCH_FILES` (PORTFOLIO.md / Faktortabelle.md / log.md) prüft. Tests mocken den Output direkt durch synthetische `freshness_missing`-Listen, statt den Helper zu instrumentieren — das prüft die **Gate-Logik**, nicht den Helper. Konsistente Schreibweise: `freshness_missing=["PORTFOLIO.md"]` (nicht historisch `["STATE.md"]`).

---

## 9. §-Mapping / Datei-Änderungen

| Datei | Änderung | Status |
|---|---|---|
| `03_Tools/backtest-ready/versions.py` | **NEU** — Single Source of Truth für `DEFCON_ACTIVE_VERSION` | Neu erstellen |
| `03_Tools/backtest-ready/provenance_gate.py` | **NEU** — `check_provenance()` + Carryover-Whitelist + Smoke-Tests | Neu erstellen |
| `03_Tools/backtest-ready/schemas.py` | `_check_vollanalyse_block_coverage`-Validator + Test-Cases D1-D4 | Erweitern |
| `01_Skills/backtest-ready-forward-verify/SKILL.md` | Phase-Tabelle (Section 4): P3.5 vor P3; Version-Referenz auf `versions.py`; Report-Format (Section 6) um P3.5-Line | Update |
| `01_Skills/backtest-ready-forward-verify/_smoke_test.py` | Integration-Test Pflicht: Provenance-Fail-Szenario, Exit-Code-Assertion | Erweitern |
| `00_Core/INSTRUKTIONEN.md` neue §18.5 | Provenance-Gate-Klausel + §18-Versionsbump v2.1→v2.2 | Update (bei Go-Live) |
| `00_Core/SYSTEM.md` System-Zustand | Bullet: „Provenance-Gate aktiv seit YYYY-MM-DD" (NICHT STATE.md — System-Status liegt in SYSTEM.md seit 00_Core-Split 22.04.) | Update (bei Go-Live) |
| `00_Core/CORE-MEMORY.md §10` Audit-Log | Go-Live-Eintrag mit Pre-Check-Resultat | Append (bei Go-Live) |
| `00_Core/log.md` | §18.2-Union-Pflicht für System-Event (Go-Live ist System-Zustand-Change) | Append (bei Go-Live) |

### 9.1 Bewusst KEINE Änderung
- `01_Skills/dynastie-depot/config.yaml`: keine konfigurativen Parameter (Platzhalter-Liste hard-coded, Version in `versions.py`, Carryover-Whitelist hard-coded). Kein FLAG/Score/Sparraten-Change durch Provenance-Gate-Deploy.
- `00_Core/Faktortabelle.md` Legende: P3.5-Status nicht user-facing sichtbar, keine Legende-Änderung nötig.
- `00_Core/STATE.md`: ist Hub seit 22.04. — kein System-Status-Eintrag (der gehört in SYSTEM.md). Hub-Critical-Alerts werden separat per Trigger-Mechanik gepflegt.
- Neuer INSTRUKTIONEN-§ als kompletter Block: Applied-Learning-Stufe reicht bis Evidenz nach 3-4 realen Läufen; §18.5 ist Sub-Section, keine §-Promotion.

---

## 10. Offene Punkte / Follow-ups

- **Pre-Gate-Audit-Subjekt (v2 28.04.):** TMO Q1 am 23.04.2026 ist als Record #28 bereits **ohne Gate appendiert** (forward + vollanalyse + alle 5 quellen-Felder befüllt, alle 4 metriken_roh-Blöcke gefüllt). Fungiert als Pre-Gate-Audit-Baseline für Plan-v3-Step-0.1 Pre-Check (28/28 PASS erwartet) + Task-2.7-Re-Validate-Sweep (Block-Coverage muss passieren).
- **First-Live-Run nach Deploy:** nächste `!Analysiere`-Vollanalyse nach Plan-v3-Execution. Kandidaten: V Q2 28.04. (heute) ODER MSFT Q3 29.04. (morgen). Eigener CORE-MEMORY §10-Eintrag mit Pipeline-Sequenz-Result.
- **Versions-Evolution:** Bei Migration v3.7 → v3.8 muss `versions.py::DEFCON_ACTIVE_VERSION` aktualisiert werden. Einzige Code-Stelle, keine Cross-File-Suche nötig.
- **Evidence-basierte Promotion zu INSTRUKTIONEN-§-Block:** Nach 3-4 realen Anwendungen Applied-Learning-Scan: wurde Gate tatsächlich verwendet? Wurde ein realer Fehler verhindert? Bei Ja → ggf. eigener § (statt Sub-§18.5).
- **§33 Skill-Self-Audit (B19) erfüllt:** Status-Matrix in `07_Obsidian Vault/.../Wissenschaftliche-Fundierung-DEFCON.md` wurde während Brainstorming konsultiert. Ergebnis: keine blockierenden Befunde, drei Future-Compatibility-Notes (s.u.). Audit-Log-Eintrag in CORE-MEMORY §10 bei Go-Live.
- **Future-Compatibility B20 (Sheppert GT-Score):** SKILL.md `backtest-ready-forward-verify` erwähnt B20 als Future-Option für §29.1-Aktivierung (In-the-Loop-Acceptance-Check neben §28.2 Δ-Gate). P3.5-Provenance-Gate und B20-GT-Score sind **disjunkte** Phasen: P3.5 prüft Provenance-Behauptungen (Append-Time), B20 prüft Overfitting-Robustheit via Composite-Objective (Parameter-Loop-Time). Bei §29.1-Aktivierung (Review 2028 oder erste Parameter-Variation) können beide koexistieren — ggf. als neue Phase P3.7 nach P3 Δ-Gate. Nicht Teil dieses Specs.
- **Future-Compatibility B18 (Palomar Seven Sins):** §29.5 Seven-Sins-Pre-Flight ist SOFORT aktiv bei Migration-Events (§28), nicht bei Standard-Forward-Appends. Unser P3.5 läuft bei jedem Append. Falls bei Migration-Runs zusätzliche Seven-Sins-Pre-Flight-Checks gebraucht werden, wären sie eine separate Migration-Pipeline-Phase, nicht Erweiterung von P3.5.
- **Future-Compatibility B27 (Ke-Huddart-Petroni-2003 Insider-Sell-Window 24M):** Phase-B paper-ingest 22.04.2026 — Erweiterung des `insider-intelligence`-Skills auf 24-Monats-Sell-Window deferred (v2). Aktueller Block-Coverage-Validator nimmt insider-Block **explizit** aus (keine Roh-Felder in `metriken_roh`, weil alle Insider-Daten Sub-Scores sind). Bei `insider-intelligence v2`-Aktivierung würde diese Skip-Annahme falsch — dann muss Block-Coverage-Validator um insider-Block-Mapping (z.B. `insider_sell_volume_24m_usd`, `insider_buy_count_24m`) erweitert werden. Nicht Teil dieses Specs, aber als Future-Compat-Note dokumentiert.
- **Implementation-Plan:** `docs/superpowers/plans/2026-04-21-score-append-provenance-gate.md` (v3, refresh 28.04.2026).

---

## 11. Design-Prinzipien (als Self-Check festgehalten)

- **Disjunkte Verantwortung B ↔ D:** B prüft Pipeline-Kontext, D prüft nur Record-Felder. Keine überlappenden Prüfungen außer bewusster Redundanz.
- **Fail-close beide Schichten:** Kein Override-Flag, kein Weitergang bei erster Verletzung.
- **Single Source of Truth für Version:** Nur `versions.py` kennt die aktive DEFCON-Version.
- **Bypass-Resistenz gegen zwei realistische Wege:** (1) Direkt-CLI-Aufruf an `archive_score.py` → D greift; (2) Pipeline-Kontext-Lüge (synthetisch aufgeblasene `metriken_roh`) → B greift via Freshness-Check + Version-Konsistenz.
- **Minimal invasive Integration:** Keine Schema-Migration der 28 existierenden Records, kein Breaking Change, keine neuen Pflichtfelder in `ScoreRecord`.
- **Whitelist statt Blacklist für Carryover:** `*_carryover`-Suffix ist nur akzeptiert, wenn der Stamm einem bekannten Source/Reason-Token entspricht. Vermeidet sowohl false positives (legitime Carryover blockieren Forward-Run) als auch silent acceptance (`xyzzy_carryover` würde nicht-existente Quelle durchlassen).
- **Evidence-basierte Promotion:** Applied Learning jetzt, INSTRUKTIONEN-§-Promotion erst bei belegtem Bedarf (konsistent zu Memory-Regel „keine Regeln auf Vorrat").

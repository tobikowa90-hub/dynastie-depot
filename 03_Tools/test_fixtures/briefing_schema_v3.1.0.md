# Briefing Schema Test-Fixture v3.1.0

**Status:** Synthetische Schema-Test-Referenz für v3.1.0-Plan Phase-3-Test-Suite. Referenziert von `docs/superpowers/specs/2026-05-06-briefing-v3.1.0-control-plane-design.md` §4.3 + §7.3.2.
**Strategie:** Hybrid (Schema synthetisch / State live) — User-Decision C in Spec §1. Diese Datei ist Schema-Seite. State-Tests laufen gegen Live-PORTFOLIO mit Drift-Akzeptanz.

## §1 Allow-List-Regex (kanonisch v3.1.0)

```
\[(file:[^\]]+|tavily@[a-z0-9.\-]+,\d{4}-\d{2}-\d{2}|shibui_[a-z_]+@\d{4}-\d{2}-\d{2}(; score_date=\d{4}-\d{2}-\d{2})?|Yahoo 403 known)\]
```

Codex-PASS 5/5 Tag-Forms verifiziert (Spec §6.3.1, R2 Narrow-Recheck).

## §2 Tag-Format-Beispiele PASS (pro Allow-List-Branch)

### Branch 1 — `file:[^\]]+`
- `[file:Faktortabelle.md/Score-Tabelle]`
- `[file:Faktortabelle.md/Update-Kalender]`
- `[file:PORTFOLIO.md vs file:Faktortabelle.md]`
- `[file:PORTFOLIO.md/Watches]`

### Branch 2 — `tavily@<domain>,<date>`
- `[tavily@reuters.com,2026-05-06]`
- `[tavily@bloomberg.com,2026-05-06]`
- `[tavily@spglobal.com,2026-05-05]`
- `[tavily@ft.com,2026-05-06]`
- `[tavily@finance.yahoo.com,2026-05-06]`

### Branch 3 — `shibui_<...>@<date>(; score_date=<date>)?`
- `[shibui_stock_quotes@2026-05-05]`
- `[shibui_stock_quotes@2026-05-05; score_date=2026-04-28]`

### Branch 4 — `Yahoo 403 known` (literal string only)
- `[Yahoo 403 known]`

## §3 §6F-Mismatch-Klassen-Output-Strings (Source-Mismatch — Source liefert technisch, aber Wert passt nicht)

Diese Klassen sind disjunkt von §4 (§4.5(E) Tool-Status-Outputs).

| #     | Klasse                  | Output-Template (Beispiel mit konkreten Werten)                                                                                                                                  |
|-------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 6F-1  | Lag                     | `Kurs — n.v. (source-lag: [shibui_stock_quotes@2026-05-04])` — DELTA folgt SCHRITT-3a-Branches                                                                                   |
| 6F-2  | Schema-Drift            | `Kurs — n.v. (schema-drift: [shibui_stock_quotes@2026-05-05])`                                                                                                                  |
| 6F-3  | Auth-Access-Fail        | `Kurs — n.v. (access-fail: [shibui_stock_quotes@2026-05-05])` — Cascade-Quelle, der eigentliche Tool-Status fließt parallel über §4.5(E) (z.B. NEWS-SIGNAL-Auth-Fehler-String)   |
| 6F-4  | Cross-Source-Mismatch (Calendar-Mismatch v3.0.6) | `Delta — n.v. (cross-source-mismatch: shibui_stock_quotes@2026-05-04; score_date=2026-05-02 nicht handelbar im Listing-Markt)`                            |
| 6F-5  | File-Sync-Drift         | `[FIELD] — n.v. (file-sync-drift: [file:PORTFOLIO.md vs file:Faktortabelle.md])`                                                                                                |
| 6F-6  | Missing-File-Row        | `Earnings — n.v. (missing-file-row: [file:Faktortabelle.md/Update-Kalender])`                                                                                                   |

## §4 §4.5(E) Tool-Status-Output-Strings (Tool-Erreichbarkeit — Source liefert nicht oder gar nicht)

- Tool-Unavailable (v3.0.6): `NEWS-SIGNAL: n.v. (tool-unavailable)`
- Tool-Error (Generic MCP): `Cohort: n.v. (tool-error)` / `<TICKER> — n.v. (tool-error)`
- Auth-Error (HTTP 401/403): `NEWS-SIGNAL: Auth-Fehler — Key rotieren`
- Rate-Limit (HTTP 429): `NEWS-SIGNAL: Rate-Limit erreicht (Budget ausgeschoepft)`
- Bad Request (HTTP 400/422): `Cohort: n.v. (bad request)` / `<TICKER> — n.v. (bad request)`
- Tavily 5xx: `Cohort: n.v. (Tavily <code>)` / `<TICKER> — n.v. (Tavily <code>)`
- Parse-Error: `Cohort: n.v. (parse-error)` / `<TICKER> — n.v. (parse-error)`
- Empty-Result valid: `Cohort: Keine material News` / `<TICKER> — keine News`
- Materialitaets-Filter rejects all: `Cohort: Keine material News` / `<TICKER> — keine material News`

## §5 Anti-Fabrikations-FAIL-Examples (NICHT erlaubt im Output — auch nicht in Failure-Modi)

| Verbotenes Tag-Pattern               | Grund                                                              |
|--------------------------------------|--------------------------------------------------------------------|
| `[websearch@reuters.com,2026-05-06]` | WebSearch ist kein Source-Klasse (Anti-Fallback v3.0.6 Critical-Guards) |
| `[yahoo@finance.yahoo.com,...]`      | Yahoo nur als Literal-String `[Yahoo 403 known]` erlaubt            |
| `[manual@user-input]`                | Manueller Override hat keinen Tag                                   |
| `[fallback@bloomberg.com,...]`       | Fallback-Pfad existiert nicht                                       |
| `[earnings_calendar@2026-05-06]`     | Hook-Output ist Operator-Awareness, nicht Cron-Briefing-Source (v3.1.0 Hook-Output-Disclaimer) |
| `[hook_systemMessage@2026-05-06]`    | Hook-Bridge geht ausschliesslich via File-State, nicht via Tag      |
| `[curl@reuters.com,...]`             | curl ist verboten (v3.0.6 Critical-Guards)                          |
| `[forbes@2026-05-06]`                | Domain ausserhalb der Allow-List in §4.5(A)/(C)                     |
| `[user_provided@...]`                | Keine Source-Klasse                                                 |
| `[drift_section@...]`                | Hook-Output-Variante (v3.1.0 Hook-Output-Disclaimer)                |
| `[tavily@FORBES.COM,2026-05-06]`     | Domain MUSS lowercase sein (Regex `[a-z0-9.\-]+`)                   |
| `[tavily@reuters.com,06-05-2026]`    | Datum MUSS YYYY-MM-DD sein (Regex `\d{4}-\d{2}-\d{2}`)              |
| `[shibui_stock_quotes@2026-5-5]`     | Datum MUSS Zero-Padded YYYY-MM-DD sein                              |

## §6 Reviewer-Test-Schritt (Spec §9 T6 (6) Anti-Fabrikation)

```
# Pseudo-Code für T6-Reviewer
def t6_anti_fabrication(briefing_output: str) -> bool:
    allow = re.compile(r"\[(file:[^\]]+|tavily@[a-z0-9.\-]+,\d{4}-\d{2}-\d{2}|shibui_[a-z_]+@\d{4}-\d{2}-\d{2}(; score_date=\d{4}-\d{2}-\d{2})?|Yahoo 403 known)\]")
    all_tags = re.findall(r"\[[^\]]+\]", briefing_output)
    for tag in all_tags:
        if not allow.fullmatch(tag):
            return False  # FAIL — fabricated tag
    # §6F-Klassen-Labels werden separat über grep auf bekannte Strings geprueft (siehe §3 oben)
    return True
```

Manual-Reviewer-Step: grep über kompletten Briefing-Output mit Allow-List-Regex als Filter. Jeder gefundene Tag-Pattern, der nicht matcht = Assert-FAIL. Auch in Failure-Modus-Outputs (Yahoo-403, Tool-Unavailable, Schema-Error etc.) gilt die Allow-List unverändert.

---

*Test-Fixture v3.1.0 — Stand: 2026-05-06 — Synthetische Schema-Referenz, kein State-Snapshot*

---
tags: [core-position, flag-aktiv, analysepflicht]
ticker: GOOGL
name: Alphabet Inc.
rolle: Core-Position (seit 26.08.2026) — vorher MSFT-Ersatz
score: 72
score_datum: 2026-03-26
score_valid_until: 2026-09-22
defcon: 3
flag: "CapEx/OCF — aktiv, Trigger 2026-03-15 ohne Resolve"
ausschluss_aufgehoben: 2026-09-04
---

# GOOGL — Alphabet Inc.

> **Ausschluss aufgehoben am 04.09.2026 · FLAG 🔴 bleibt aktiv**
> Das ist kein Widerspruch — siehe unten.

## Statuswechsel 04.09.2026 (Stufe 0, Owner-Entscheidung)

Der **strukturelle Ausschluss vom 01.04.2026 ist förmlich aufgehoben.** Begründung: Der Owner baut GOOGL seit dem 26.08.2026 bewusst als **Core-Position** auf; seit dem 01.09.2026 besteht eine Position, der Sparplan läuft mit 50 €/Monat. Ein Ausschlussvermerk, der einer laufenden Owner-Entscheidung widerspricht, ist keine Regel, sondern eine Altlast.

Aufgehoben wurde an drei Stellen im selben Vorgang: diese Vault-Seite · `config.yaml flags_watchlist` (Handelsregel „kein Einstieg, kein Nachkauf") · Chronik-Eintrag in `CORE-MEMORY.md` und `log.md`.

**Der CapEx/OCF-FLAG bleibt davon unberührt und bleibt aktiv.** Die Unterscheidung ist der Kern der Entscheidung:

| | Was es ist | Status |
|---|---|---|
| **Ausschluss** | *Handelsregel* — „nicht kaufen" | **aufgehoben 04.09.2026** |
| **FLAG** | *Urteilsstand* — „Risiko offen, Evidenz fehlt" | **aktiv**, Trigger `GOOGL_capex_ocf_2026-03-15` ohne Resolve |

Einen Ausschluss hebt eine Owner-Entscheidung auf. Einen FLAG löst nur **frische Evidenz** auf — das ist Analysearbeit, keine Datenpflege. Bis dahin gilt die konservative Lesart: ein Trigger ohne Resolve ist aktiv.

**Wirkung des FLAG in der Zielarchitektur:** Klasse `core` trägt `flag_wirkung: analysepflicht`, nicht `rate_null`. Der offene FLAG stoppt also keine Rate, sondern macht GOOGL **analysepflichtig** — der Titel landet im Analyse-Backlog, wo er hingehört. GOOGL steht deshalb bewusst **nicht** in `config.yaml flags_aktiv` (das würde Rate 0 bedeuten und dem laufenden Sparplan widersprechen).

## FLAG-Detail (unverändert)

CapEx FY26 auf Kurs ~75 % OCF, strukturell über der 60-%-Schwelle. Trigger vom 15.03.2026 in `flag_events.jsonl`, kein Resolve-Event.

**Dringlichkeit:** Der Score 72 stammt vom 26.03.2026 und **verfällt am 22.09.2026** — als erster im ganzen Roster, danach folgt der Oktober-Cluster. GOOGL ist damit der Titel mit offenem FLAG, laufender Rate, frischer Position und ablaufendem Score zugleich. Die Vollanalyse ist vor dem 22.09. fällig; sie entscheidet zugleich über den FLAG-Resolve.

**Lernlektion (korrigiert 04.09.2026):** Die alte Fassung dieser Seite schrieb „FLAG überschreibt Score. Auch Score 72 + DEFCON 3 = 0 € = kein Einstieg." Das galt für die Klasse `satellit` mit `flag_wirkung: rate_null`. Für eine Core-Position gilt es nicht — dort wirkt der FLAG als Analysepflicht. **Die FLAG-Wirkung hängt an der Klasse des Titels, nicht am FLAG.**

## Verlinkungen

- [[CapEx-FLAG]]
- [[MSFT]] — Position, für die GOOGL bis 26.08.2026 als Ersatz geführt wurde
- [[AMZN]] — Sibling CapEx/OCF-FLAG-Hyperscaler (TTM 99,2 % — schärfer als GOOGL ~75 %)

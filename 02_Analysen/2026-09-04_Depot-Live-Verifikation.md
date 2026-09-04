# Depot-Live-Verifikation 04.09.2026 — Entscheidungs- und Befundgrundlage für Spec v1.6

**Zweck:** Vollständige Übergabe für das Schreiben von `03_Tools/depot-architecture-spec.md` v1.6.
Alles hier ist gegen die Scalable-API bzw. die realen Repo-Dateien verifiziert. **Die nächste Session muss nichts davon neu abfragen.**

**Vorgänger:** `02_Analysen/2026-08-26_Depot-Reconciliation.md` · Spec v1.5 (Commit `a07b4db`)
**Stand der Live-Daten:** Bewertung 2026-09-03 21:00 UTC · Inventar 2026-09-03 05:32 UTC
**Kanal:** MCP-Connector „Scalable Capital". **CLI `sc` war tot** (`no_session`; `sc login` ist `human_only`) — die beiden Kanäle laufen unabhängig ab.

---

## 1 · Live-Daten (verifiziert)

### 1.1 Depot gesamt

| | Wert |
|---|---:|
| Gesamt | **32.132,01 €** |
| davon Wertpapiere | 32.127,94 € |
| davon Cash | 4,07 € |
| Sparplan-Ist (19 Pläne) | **1.068 €/Mt** |

Spec-v1.5-Zahl war 30.124 € (Stand 26.08.) → **+2.008 € / +6,7 % in acht Tagen.**

**Warnung zu Performance-Kennzahlen:** `MAX` = `ONE_YEAR` = `YEAR_TO_DATE` = 2.238,47 €. Der Broker kennt das Depot erst ab dem Übertrag 17.08.2026. Die Performance-Serie ist **nicht** die Depot-Historie.

### 1.2 Positionen (24: 6 ETF · 17 Aktien · 1 Gold)

| Ticker | Typ | Wert € | Sparplan |
|---|---|---:|---:|
| IWDA | ETF | 7.668,93 | 208 |
| NOW | Aktie | 5.103,46 | — |
| EIMI | ETF | 3.791,72 | 120 |
| EXUS | ETF | 3.125,21 | 80 |
| AVGC | ETF | 2.784,31 | 85 |
| ADBE | Aktie | 993,62 | 35 |
| GOLD (EWG2) | Gold | 866,93 | 80 |
| MSFT | Aktie | 788,55 | 50 |
| ZETA | Aktie | 784,70 | — |
| VEEV | Aktie | 683,76 | 20 |
| AMZN | Aktie | 636,27 | 50 |
| V | Aktie | 592,19 | 35 |
| ASML | Aktie | 564,26 | 35 |
| TMO | Aktie | 537,32 | 20 |
| BRK.B | Aktie | 483,66 | 20 |
| SU | Aktie | 466,62 | 20 |
| AVGO | Aktie | 433,46 | — |
| APH | Aktie | 410,17 | 20 |
| WQTM | ETF | 405,67 | 70 |
| RMS | Aktie | 391,76 | 20 |
| COST | Aktie | 357,59 | — |
| JEDI | ETF | 153,34 | — |
| META | Aktie | 53,73 | 50 |
| GOOGL | Aktie | 50,71 | 50 |

**Ohne Sparplan, mit Position:** NOW · AVGO · ZETA · COST · JEDI
**Neu seit 01.09.:** META und GOOGL haben erstmals Positionen (Sparpläne gelaufen)
**Nicht im Depot:** KYCCF (Roster-Eintrag verwaist)
**Offene Sell-Limits (in keiner Repo-Datei):** COST @880 (+10,6 % entfernt) · JEDI @90 (+32 % entfernt)
**Split:** APH hatte am 03.09. `SWAP_OUT` 2,90389 → `SWAP_IN` 5,80778 Stk (1:2). Ältere Stückzahlen sind nicht vergleichbar.

### 1.3 Entnahme-Topf „Hochzeit" — tranchenscharf belegt

**Einzahlung:** `DEPOSIT` 9.000,00 € am **11.08.2026**. Investiert am **13.08.2026** in einer Order-Welle, Summe centgenau.

| Ticker | Stk | Einstand € | Wert 03.09. € | |
|---|---:|---:|---:|---:|
| IWDA | 24,387411 | 3.150 | 3.115,43 | −1,1 % |
| NOW | 18,284878 | 2.000 | 2.282,87 | +14,1 % |
| EIMI | 37,072344 | 1.750 | 1.765,92 | +0,9 % |
| AVGC | 46,285492 | 1.190 | 1.183,17 | −0,6 % |
| EXUS | 22,216796 | 910 | 899,22 | −1,2 % |
| **Σ** | | **9.000** | **9.246,62** | **+2,7 %** |

**Zieldatum 07.08.2027 · Zielwert 10.000–11.000 €** → fehlen 753–1.753 €. NOW trägt die Rendite praktisch allein.
Der Topf ist zu **78 % ETF** — deshalb verzerrte er vor allem die ETF-Quote, nicht die von NOW.

### 1.4 Quoten — die Basis entscheidet das Ergebnis

| Basis | ETF | Aktien | Gold | Basis € |
|---|---:|---:|---:|---:|
| Depot gesamt | 55,8 % | 41,5 % | 2,7 % | 32.128 |
| nur NOW-Tranche raus *(falsch)* | 60,1 % | 37,0 % | 2,9 % | 29.845 |
| **ganzer Topf raus (maßgeblich)** | **47,9 %** | **48,3 %** | **3,8 %** | **22.881** |

Gegen 60/35/5 bei Toleranz 1,5 / 4,0 pp und Warnfaktor 3:
**ETF −12,1 pp ROT · Aktien +13,3 pp ROT · Gold −1,2 pp OK**

**NOW-Einzeltitel:** 15,88 % (Gesamtdepot) · **12,33 %** (Dynastie-Basis) · **7,90 %** nach Entnahme 07.08.2027 (bei konstanten Kursen + 12 Monaten Sparplan) → der Entnahmetermin ist der Auflösungsmechanismus, nicht Verwässerung.

**Herkunft der Drift — kein Disziplinproblem:** Aktien-Überhang 3.040 €; Überschuss der Aktienrate 51 €/Mt → **59 Monate** hätte der Aufbau über die Rate gedauert. Es ist Bestand: ING-Übertrag brachte fast nur ETF (8.444,88 €), die Einzelaktien wurden bei Scalable gebaut und haben outperformt.

**Konvergenz-Regel (ceteris paribus, gleiche Rendite beider Blöcke):** Der Bestandsanteil eines Blocks konvergiert gegen seinen **Raten-Anteil**. ETF-Rate 563/1068 = 52,7 % < Ziel 60 % → Ziel wird unter diesen Annahmen nicht erreicht. Bei Aktien-Outperformance schlechter, bei ETF-Outperformance erreichbar. Stabilisierungs-Floor wäre eine ETF-Rate von **641 €**.

### 1.5 Urteil-Layer

`score_history.jsonl`: 37 Records, 26 Ticker. **Ohne Record (Depot):** ADBE · META · NOW · ZETA.

| Ticker | Score | Datum | verfällt |
|---|---:|---|---|
| GOOGL | 72 | 2026-03-26 | **2026-09-22** |
| ASML · COST · RMS · SU · VEEV | 68/69/68/69/74 | 2026-04-17 | 2026-10-14 |
| TMO | 67 | 2026-04-23 | 2026-10-20 |
| V | 64 | 2026-04-28 | 2026-10-25 |
| MSFT | 50 | 2026-04-29 | 2026-10-26 |
| APH | 61 | 2026-04-30 | 2026-10-27 |
| BRK.B | 71 | 2026-05-04 | 2026-10-31 |
| AMZN | 42 | 2026-05-15 | 2026-11-11 |
| AVGO | 56 | 2026-06-04 | 2026-12-01 |

`flag_events.jsonl`: 4 Events, alle `trigger`, kein `resolve` — MSFT (2026-01-15) · GOOGL (2026-03-15) · AVGO (2026-04-27) · AMZN (2026-05-15). **APH fehlt** (FLAG seit 2026-04-09 in `config.yaml`, score-basiert).

**AVGO:** Q3-FY26-Call lief am **03.09.2026 (amc)**; `earnings_calendar.py --check` nennt als nächsten Termin 09.12. → **Tag +1 ist der 04.09.**, §19.1-Vollanalyse + FLAG-Resolve-Gate fällig. Letzte abgeschlossene Analyse war der 13.06. (83 Tage).

---

## 2 · Owner-Entscheidungen dieser Session

| # | Frage | Entscheidung |
|---|---|---|
| 1 | Woran misst `allokation_drift`? | **Wertbasiert.** 60/35/5 gilt für den Depotwert; die Sparraten-Verteilung ist das Instrument und darf bewusst abweichen (Gold-Rate 7,5 % ist korrekter Aufholmodus bei Bestand 3,8 %). |
| 2 | `budget.monatlich_eur` | **1.068 €** (Ist übernehmen). Rolle korrigiert: **keine** Eingangsgröße der Ratenrechnung — §3 begründet das Feld heute mit §7.2, das ist aber die von §7.4 verworfene Normierungsformel. Unter `additiv` ist es die **Erhaltungs-Invariante der §7.4-Staffel**: Σ aller Raten nach Umleitung == budget. |
| 3 | GOOGL-Ausschluss | **Förmlich aufheben** — Chronik-Eintrag mit Datum und Begründung; Vault-Entity **und** `config.yaml flags_watchlist` ziehen mit. Der CapEx/OCF-FLAG bleibt aktiv und erzwingt über Klasse `core` die Analysepflicht. |
| 4 | Zählt der Entnahme-Topf in den US-Cap? | **Nein** — konsistent aus allen Dynastie-Quoten heraus (Allokation, `cap_single_stock`, `cap_us`). |
| 5 | Zieldatum Entnahme | **07.08.2027** (Hochzeit). |
| 6 | Modellierung | **Kein Tranchen-/Klassen-Konstrukt.** Ein Block, fünf statische Datenzeilen, eine Subtraktion in `depot check`. |

### 2.1 Vorgesehener Regelwerk-Block

```yaml
entnahme_2027:
  zweck: "Hochzeitsfeier"
  ziel_datum: 2027-08-07
  eingezahlt:  {betrag_eur: 9000, am: 2026-08-11, investiert_am: 2026-08-13}
  zielwert_eur: [10000, 11000]
  zaehlt_in_quoten: false          # raus aus Allokation, cap_single_stock, cap_us
  tranchen:
    - {ticker: IWDA, stk: 24.387411, einstand_eur: 3150}
    - {ticker: NOW,  stk: 18.284878, einstand_eur: 2000}
    - {ticker: EIMI, stk: 37.072344, einstand_eur: 1750}
    - {ticker: AVGC, stk: 46.285492, einstand_eur: 1190}
    - {ticker: EXUS, stk: 22.216796, einstand_eur:  910}
```

Dazu: Check `entnahme_ziel` (Fortschritt gegen 10–11 k, Warnung ~3 Monate vor dem Termin) und ein Carve-out in `niemals_durch_verkauf` — die geplante Entnahme ist kein Tausch.

### 2.2 Steuer-Lage (Owner-Angabe, korrigiert die Doku)

- **ING-Depot durch den Übertrag auf 0** — nicht gekündigt, aber leer. `KONTEXT.md` §7 („ING 1.500–1.600 € / Scalable 400–500 €") ist damit überholt.
- **Ab 2027 kann der volle Freibetrag bei Scalable liegen**, ab der Heirat **2.000 €**.
- Merker: verfügbar ≠ hinterlegt — der erhöhte Freistellungsauftrag muss erteilt werden.
- **Offener Beleg (FIFO-Risiko):** Die ETF-Tranchen des Topfs werden 2027 FIFO gegen die ING-Altbestände abgerechnet (IWDA 34 · EIMI 40 · EXUS 53 Stk, übertragen 17.08.). Deren echter Einstand ist **über die API nicht abrufbar** — `get_transaction_details` liefert für `TRANSFER_IN` nur `averagePrice` = Übertragswert (IWDA 128,615 = 4.372,91/34). Quelle ist die ING-Übertragungsanzeige bzw. das Scalable-Steuerreporting. Ohne diesen Beleg ist unklar, ob die 2.000 € 2027 reichen.

### 2.3 Konzentrations-Kappung als Ernte-Mechanismus (Owner-Vorschlag)

Der Einzelpositions-Cap ist der Auslöser für Gewinnmitnahme; der Erlös geht in den ETF-Core.

**Warum es trägt:** kein Markttiming (Auslöser ist Positionsgröße, nicht Kursziel — verträglich mit `KONTEXT.md` §1) · erntet strukturell nur Gewinner · verkauft nur den Überhang, nie die Kernposition · der Erlös hat ein definiertes Ziel.

**Abgrenzung, die in die Spec muss:**

> **Block-Rebalancing** — ETF/Aktien/Gold zurück auf Zielquote → **verboten** (`KONTEXT.md` §7, `Rebalancing_Tool` B23), Sparplan umleiten.
> **Konzentrations-Kappung** — Einzelposition über Cap → **erlaubt**, Risikokontrolle gegen idiosynkratisches Risiko.

`config.yaml system_regeln.substitute_activation_global.steuer_regel` kennt bereits einen zulässigen Verkaufspfad („Bei unvermeidbarem Verkauf: Abgeltungsteuer 26,375 % + FIFO + Freibetragscheck"). Die Kappung wäre der zweite. `niemals_durch_verkauf: true` muss entsprechend präzisiert statt als Pauschal-Flag geführt werden.

**Heutige Bindung:** Bei 10 % (Dynastie-Basis 22.881 € → 2.288 €) ist **nur NOW** gebunden (12,33 %, Owner-Ausnahme bis 07.08.2027). Nächstgrößte Position ADBE 4,3 %. Die Regel liegt vorerst still — als Leitplanke richtig, kostet heute nichts.

---

## 3 · Befunde für v1.6

### H14 — xlsx-Parameterblatt ist eine nicht inventarisierte Regelwerk-Quelle **(HIGH)**

`03_Tools/Rebalancing_Tool_v4.0.xlsx` → Blatt `Parameter & Regeln` hält u. a.:

| Zelle | Parameter | Wert | auch woanders? |
|---|---|---|---|
| B4 | Sparrate monatlich | 1031 | ja (`config.yaml`) |
| B5/B6/B7 | Zielanteile | 0.597 / 0.353 / 0.05 | ja |
| B8/B9 | Drift-Toleranz ETF-Gold / Aktien | 0.015 / 0.04 | **nein** (Spec zitiert B8/B9) |
| **B10** | **Single-Stock-Cap** | **0.1** | **nein — einzige Quelle** |
| B11 | US-Hard-Cap | 0.63 | ja |
| B12 | Max Aktien Slots | 13 | ja |
| B15 | Drift-Warnschwelle | 3 | nein (Spec zitiert B15) |
| B23 | „NIEMALS durch Verkauf rebalancen" | — | ja (`KONTEXT.md` §7) |
| B65 | Nachkauf-Schwelle | 300 | nein (Spec zitiert B65) |

**Zwei Konsequenzen:** (a) §2.1 inventarisiert ausschließlich `config.yaml` — das xlsx-Parameterblatt wurde nie durchgegangen. (b) Diese Datei wandert in **Stufe 1 Schritt 7** nach `05_Archiv/`; ohne vorherige Extraktion archiviert die Migration geltende Regeln. §3 nennt für `single_stock_max_pct` als einziges der Tool-Parameter **keine Quelle** — B10 nachtragen.

### H15 — `KONTEXT.md` fehlt vollständig als Migrations-Sync-Ziel **(HIGH)**

Die Datei kommt in der ganzen Spec nicht vor, wird aber von der Routing-Table bei **jeder** Strategie-/Allokationsfrage geladen. Es gilt dasselbe Argument wie bei R4-C1 zu `CLAUDE.md`.

Doku-Drift, verifiziert:

| § | steht dort | Ist |
|---|---|---|
| 2 | „ING (IWDA+EIMI+EXUS) + Scalable" | ING leer seit 17.08. |
| 3 | Broker-Spalte ING · „~1031 € · 20 Positionen" | alles Scalable · 1.068 € · 24 Positionen |
| 4 | IWDA 206 / EIMI 123 / EXUS 82, alle ING | 208 / 120 / 80, alle Scalable |
| 4b | „In-Kind Herbst 2026, IWDA-**Verkauf** 2027" | am 17.08. passiert — **IWDA wurde mit übertragen statt verkauft** (die §4b-Steuerplanung „+369 € G/V steuerfrei" ist damit offen) |
| 5 | 13 Satelliten | 17 Aktienpositionen |
| 7 | ING 1.500–1.600 € / Scalable 400–500 € | ab 2027 alles Scalable, ab Heirat 2.000 € |

**Nötige Schichtenzuordnung (analog §2.1 für `config.yaml`):** §1 Philosophie · §8 Psychologie · §9 Bus-Faktor → **Doktrin**, bleibt handgeschrieben · §3 Caps · §5 Roster · §6 Ersatzbank · §7 Freibeträge → **Regelwerk** · §2 Broker · §3 Raten/Positionszahlen · §4 ETF-Zuordnung → **Zustand**, entfällt.

### H10 — `config.yaml` hat drei FLAG-Blöcke, die Spec kennt einen **(HIGH)**

§1.1 führt „`config.yaml flags_aktiv`" als eine FLAG-Quelle. Real existieren `flags_aktiv`, `flags_review` (leer) und `flags_watchlist`. **GOOGL steht in `flags_watchlist`** mit `wirkung: "Kein Einstieg, kein Nachkauf bis FLAG aufgehoben"` — bei laufendem 50-€-Sparplan und Position seit 01.09. Der GOOGL-Widerspruch ist damit **dreifach** (Vault-Entity · `flags_watchlist` · offener jsonl-Trigger), nicht zweifach wie in §9.3.

Zusatz: §2.1 ordnet `flags_watchlist` dem **Urteil** zu („wird aus `flag_events.jsonl` abgeleitet"). Der Eintrag ist aber eine Handelsregel → **Regelwerk**. Fehlklassifikation.

### H11 — §7.4 verankert ein basisabhängiges Rechenbeispiel **(MEDIUM)**

§7.4 schreibt: AVGOs eingefrorene 40 € gehen über Staffel-Stufe 2 an den größten Unterhang, „Ziel Gold (2,7 % gegen 5 %)". Auf der maßgeblichen Basis liegt Gold bei 3,8 % **innerhalb** der Toleranz; größter Unterhang ist **ETF-Core mit −12,1 pp**. Die Regel stimmt, das eingefrorene Beispiel nicht — es ist eine Live-Zahl ohne Stichtag, die als Konstante gelesen wird.

### H1 — ZETA fehlt in der Override-Liste **(MEDIUM)**

Position 784,70 €, kein Sparplan, kein FLAG, `ohne_score: basis_voll` fordert 18 €. Strukturell identisch mit dem NOW-Fall aus §3.3 („Rate 0 ohne FLAG"), steht aber weder in §3 `overrides` noch in §3.3. Ohne Override meldet `rate_abweichung` dauerhaft FAIL. COST trifft dasselbe, ist aber über die offene Roster-Frage (§3.1) nachgelagert.

### M5 — §1.1 widerspricht sich bei GOOGL **(MEDIUM)**

„Ungescort mit Sparplan, aber noch ohne Position: GOOGL und META" vs. zwei Sätze später „Alphabet (72) … hat gültige Records". Empirisch: GOOGL Score 72, 26.03.2026, Zeile 12. Wirklich ohne Record: **ADBE, META, NOW, ZETA**.

### M6 — Verfall hat ein hartes Datum **(MEDIUM)**

§1.1 „Aktuell ist kein Score verfallen" gilt noch, aber **GOOGL verfällt am 22.09.2026** — der Titel mit offenem Trigger, aufzuhebendem Ausschluss, 50 €/Mt und seit 01.09. erstmals Position. Danach Oktober-Cluster.

### Kleinere Korrekturen

- §5: Broker-Performance ist nicht die Depot-Historie (MAX = 1Y = YTD, weil Depot erst ab 17.08. bekannt). Nicht mit `transactions` vermengen.
- §1.1 / §3.3 / §6.1: alle Live-Zahlen mit **Stichtag** markieren (NOW „14,5 %", Depotwert, META-Positionsstatus sind acht Tage alt gewesen und waren falsch).
- §5: `holdings`/`savings_plans` genügen nicht — **offene Orders** sind Owner-Absicht und fehlen im Live-Layer (COST @880, JEDI @90 stehen in keiner Repo-Datei).
- §7.1 `roster_fremd`: sollte auf **Position ∪ Sparplan ∪ offene Order** prüfen, sonst gilt ein nur beabsichtigter Abgang als vollzogen.

---

## 4 · Bewusst offen — gehört als Frage in §11, nicht als Antwort in die Spec

1. **`allokation_drift`: FAIL, WARN oder INFO?** In dieser Session wurden beide Seiten vertreten („ROT, Handlungsbedarf" ↔ „der Check ist falsch konstruiert"). Kern der Frage: In einem System, das Rebalancing durch Verkauf ausschließt und Satelliten-Rotation über 30 Jahre vorsieht, ist eine Blockabweichung in der Aufbauphase möglicherweise der erwartete Zustand — dann wäre FAIL die eingebaute „Warnung, die immer leuchtet". **Owner-Entscheidung.**
2. **Cap-Parameter:** Höhe (B10 sagt 10 % — nach der Entnahmetopf-Trennung neu zu bewerten) · Bezugsgröße (Gesamtdepot vs. Aktienblock; 10 % des Depots = 28,6 % des Aktienblocks) · **Hysterese** (bei exakt 10 % kappen heißt bei jedem Anstieg neu verkaufen — Band z. B. 12 % → zurück auf 10 %) · **Steuerjahr-Kopplung** (Freibetrag ist jährlich → Q4-Termin statt Sofort-Mechanik).
3. **Ernte-Auslöser:** Reicht der Cap allein, oder braucht es einen zweiten (Thesenerfüllung, Bewertung)? Der einzige dokumentierte Präzedenzfall geht andersherum — `KONTEXT.md` §5: „VEEV+COST-Erlös finanziert mit", also Erlös in **neue Satelliten** statt in ETF.
4. **NOW-Override:** `cap_single_stock` mit `review_am: 2027-08-07` — läuft exakt ab, wenn die Entnahme den Cap-Verstoß auflöst (12,33 % → 7,90 %).

---

## 5 · Korrektur-Log dieser Session

Sechs Fehlaussagen, **eine Wurzel**: vom Teilausschnitt aufs Ganze geschlossen.

| # | Behauptung | Ursache | Status |
|---|---|---|---|
| 1 | „Drift löst sich auf" | nur NOW-Tranche statt 9 k aus der Basis genommen | korrigiert |
| 2 | VEEV als Exit-Kandidat | Roster-Notiz gelesen, laufenden Sparplan ignoriert | zurückgezogen |
| 3 | Verkauf als Drift-Reaktion | `KONTEXT.md` nicht gelesen (Routing-Table-Verstoß) — §7 verbietet es in einer Zeile | zurückgezogen |
| 4 | NOW braucht 18 Monate Verwässerung | Entnahmetermin nicht bekannt | korrigiert |
| 5 | „Single-Stock-Cap nirgends verankert" | Grep ohne `.xlsx` — steht in B10 | korrigiert |
| 6 | „998 € Freibetrag 2026 ungenutzt" | Abfragefenster begann erst 25.07.; Nachprüfung lief in `upstream_unavailable` | **unbelegt, aus der Spec entfernt** |

Zusatz-Präzisierung: „60 % sind mit der heutigen Rate unerreichbar" gilt nur **ceteris paribus** (gleiche Rendite beider Blöcke). Zu absolut formuliert.

---

## 6 · Nächste Schritte

1. **Spec v1.6 schreiben** — Abschnitt 2 (Entscheidungen), Abschnitt 3 (Befunde), Abschnitt 4 (als §11-Punkte). Schlanker Kern, drei Punkte bewusst offen.
2. **Codex-R5** auf H14/H15 und die sechs Entscheidungen (nicht `advisor()` — Memory `feedback_review_via_codex_not_advisor`).
3. **AVGO Q3 FY26 Tag +1** — überfällig seit 04.09. morgens; FLAG-Resolve-Gate. Sync noch nach altem §18.
4. **Stufe 0** — `flag_events.jsonl` vervollständigen: APH-Trigger nachtragen (`flag_typ: score_basiert`, `event_datum: 2026-04-09`, Grund → `config.yaml` Z. 410, via `archive_flag.py trigger`) · AMZN-Divergenz in `flags_aktiv` klären · GOOGL-Ausschluss an drei Stellen aufheben.
5. **Vor Q3/2027:** ING-Einstandsdaten für IWDA/EIMI/EXUS besorgen (FIFO-Risiko der Entnahme).

---

## 7 · Tier-2-Vorschlag für `00_Core/APPLIED-LEARNING.md`

> ⚠️ Die Datei steht bei **21/20 — Kurator-Regel bereits fällig.** Dieser Bullet ist ein Vorschlag, kein Auto-Eintrag; bitte zusammen mit einer Kuratierungsrunde einpflegen.

```markdown
- **Vom Teilausschnitt aufs Ganze schließen ist die dominante Fehlerklasse — nicht falsches Rechnen.** In einer Session entstanden sechs falsche Aussagen aus derselben Wurzel: Teil-Basis (nur eine von fünf Tranchen aus dem Quoten-Nenner), Teil-Datei (Roster-Notiz statt laufendem Sparplan), Teil-Verzeichnis (Grep ohne `.xlsx` → „Regel existiert nicht", obwohl sie in `Rebalancing_Tool` B10 steht), Teil-Zeitfenster (Freibetrags-Auslastung aus einem 6-Wochen-Ausschnitt), fehlender Kontext (`KONTEXT.md` nicht gelesen, dann dessen veraltete Steuer-Tabelle geglaubt). Jede einzelne Rechnung war korrekt. Regel: **vor jeder Aussage über Abwesenheit oder Vollständigkeit den Ausschnitt explizit benennen** — welcher Nenner, welche Dateitypen, welcher Zeitraum, welche Quellen. Ein negativer Befund („gibt es nicht") ist erst belastbar, wenn der Suchraum benannt ist; bei Widerspruch zum Nutzergedächtnis zuerst den Suchraum anzweifeln. Korollar für Migrationen: eine Datei, die archiviert werden soll, wird vorher inventarisiert — die drei xlsx-Tools halten Regelwerte, die in keiner `.md`/`.yaml` stehen.
```

---

*🦅 Depot-Live-Verifikation · 04.09.2026 · Grundlage für Spec v1.6 · keine SSoT verändert, kein Score-/FLAG-/Sparraten-Event*

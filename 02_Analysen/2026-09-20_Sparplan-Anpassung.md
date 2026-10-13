# Sparplan-Anpassung — Zielrichtung 60/35/5

> ⚠️ **ÜBERHOLT (14.10.2026):** Owner hat die Sparpläne danach selbst in der App angepasst (bewusste Entscheidungen: 20 Pläne / 1.100 €, u. a. GOOGL/META 100 €, AVGO 30 € + APH 25 € trotz FLAG). Live-Stand = Scalable-CLI. Dokument bleibt nur als Begründungs-Historie.

**Stichtag:** 2026-09-20 · **Status:** Vorschlag, **nicht ausgeführt**. Keine SSoT verändert, keine Broker-Mutation.
**Vorgänger:** `2026-08-26_Depot-Reconciliation.md` (Ist-Aufnahme + Owner-Strategie §F)

## Quellen

| Seite | Quelle | Stand |
|---|---|---|
| IST Sparpläne | Scalable CLI `sc broker savings-plans` | 2026-09-20, 19 Pläne / 1.068 € |
| IST Bestand | Scalable CLI `sc broker holdings` | 2026-09-20, 31.880,08 € / 24 Positionen |
| Regelwerk | `03_Tools/Rebalancing_Tool_v4.0.xlsx` Blatt *Parameter & Regeln* | Juni-Roster |
| Scores/FLAGs | `00_Core/PORTFOLIO.md` + `config.yaml` | 04.09. (AVGO), sonst Juni |
| Owner-Strategie | Reconciliation §F.1 (Interview 26.08.) | 26.08. |

**Owner-Entscheidungen dieser Session:** Core-4 auf je 70 € aus ETF-Rate gegenfinanziert · 3-Tier reaktiviert mit zweigeteiltem FLAG (Core-4 ausgenommen, Satelliten hart 0) · ASML zurückfahren · VEEV bleibt definitiv · JEDI Exit über Kurs, kein Sparplan · ZETA bei Scalable **nicht sparplanfähig** (Broker-Restriktion, kein Regelverstoß).

---

## A · Vorschlag — 8 Änderungen, budgetneutral

| Titel | ISIN | Ist | Neu | Δ | Begründung |
|---|---|---|---|---|---|
| Alphabet | US02079K3059 | 50 | **70** | +20 | Core-4-Aufbau |
| Microsoft | US5949181045 | 50 | **70** | +20 | Core-4-Aufbau (FLAG bleibt dokumentiert, ohne Ratenwirkung) |
| Amazon | US0231351067 | 50 | **70** | +20 | Core-4-Aufbau (dito) |
| Meta | US30303M1027 | 50 | **70** | +20 | Core-4-Aufbau |
| iShares Core MSCI World | IE00B4L5Y983 | 208 | **186** | −22 | Gegenfinanzierung des Core-4-Ausbaus innerhalb der 60% (§F.2) |
| ASML | NL0010273215 | 35 | **16** | −19 | T2 × D3 = 32, halbiert wegen Dispositions-Status zum Jahreswechsel (§F.1) |
| Visa | US92826C8394 | 35 | **16** | −19 | T2 × D2-Sockel 50% (Score 64) — Regelwert, bisher nicht angewandt |
| Amphenol | US0320951017 | 20 | **0** | −20 | 🔴 FLAG Score 61 < 65, Satellit → hart 0. **Plan löschen** |

**Unverändert (11):** EIMI 120 · AVGC 85 · EXUS 80 · WQTM 70 · Gold EWG2 80 · Adobe 35 · Hermès 20 · Schneider 20 · Berkshire B 20 · Thermo Fisher 20 · Veeva 20
**Ohne Sparplan (bleibt so):** AVGO (FLAG) · NOW (Cap) · ZETA (nicht sparplanfähig) · JEDI (Exit geplant) · COST (Take-Profit)

**Σ 1.068 €/Mt unverändert.** Danach 18 Pläne (Amphenol entfällt).

### Verifikation

| Check | Ergebnis |
|---|---|
| Budgetneutral | 1.068 € exakt ✅ |
| US-Hard-Cap 63% | 55,7% → **58,1%** ✅ (Abstand schrumpft auf 4,9pp) |
| Single-Stock-Cap 10% | kein Plan treibt eine Position darüber; NOW bleibt 0 ✅ |
| FLAG-Regel Satelliten | AVGO 0 · APH 0 ✅ (Core-4 per Owner-Beschluss ausgenommen) |
| Alle 19 Ist-Pläne abgedeckt | ✅ |
| Block-Split gegen Ziel | ❌ **siehe B** |

---

## B · Der Befund, der nicht wegzurechnen ist

Die 35%-Satellitenquote ist per Sparplan **derzeit strukturell nicht erreichbar.**

| Block | Ist-Rate | Neu | Ziel |
|---|---|---|---|
| Core-Block (ETF + Core-4) | 71,4% | **76,9%** | 59,7% |
| Satelliten | 21,1% | **15,6%** | 35,3% |
| Gold | 7,5% | 7,5% | 5,0% (Aufholzuschlag gewollt) |

**Ursache:** Von 11 Roster-Satelliten sind 5 nicht bespielbar — AVGO (FLAG), APH (FLAG), NOW (Cap 15,2%), ZETA (Broker), KYCCF (nicht mehr im Depot). Die verbleibenden tragen nach Tier-Basis nur 112 €; mit den ungescorten Owner-Positionen Adobe + Veeva sind es 167 €. Das Satelliten-Budget von 377 € lässt sich regelkonform nicht platzieren — die Differenz landet zwangsläufig im ETF-Block.

**Was das über ein Jahr bedeutet:** Bei 12.816 € Zufluss sinkt der Satellitenanteil im Bestand von 35,5% auf rund 30% (vor Kursbewegung). Der Bestand hält die Quote noch, die Rate trägt sie nicht mehr.

**Die drei Hebel — alle liegen im Scoring, nicht im Sparplan:**

1. **Earnings-Backlog** (stärkster Hebel). Der komplette Juli-Cluster ist unbearbeitet: ASML 15.07. · TMO 22.07. · V 28.07. · MSFT/APH/RMS 29.07. · SU/AMZN 30.07. · BRK.B 01.08. Die Raten oben stehen auf Juni-Scores. Insbesondere **APH** trägt einen rein score-basierten FLAG (61 < 65) — ein Re-Score nach Q2 kann ihn auflösen und 18 € zurückbringen. **V** steht auf D2 (64) aus dem April-Revert; auch das ist ein Kandidat für Bewegung.
2. **Scoring-Backlog:** Adobe, Veeva, NOW, ZETA laufen ohne gültigen Score. Adobe (35 €) und Veeva (20 €) sind aktuell reine Ist-Übernahmen ohne Regelgrundlage — 55 € des Satelliten-Blocks sind damit nicht regelgedeckt.
3. **NOW-Cap:** 15,2% gegen 10%. Löst sich durch Wachstum des Restdepots von selbst, solange der Sparplan bei 0 bleibt.

**Einordnung:** Der Zustand ist nicht falsch, sondern die Folge davon, dass fünf Satelliten gesperrt sind. Mehr ETF statt gesperrter Einzelaktien ist die konservative Auflösung und steht nicht im Widerspruch zum Manifest. Aber es heißt: **Die Zielquote kommt über den Scoring-Nachzug zurück, nicht über eine Sparplan-Umverteilung.**

---

## C · Nicht angefasst / bewusst offen

- **Gold 80 €** bleibt. Lücke auf 5% beträgt 736 € (858 € Ist gegen 1.594 € Ziel); bei 80 € statt Steady-State 53 € schließt sie sich in rund 27 Monaten.
- **Regelwerk-Nachzug** (Reconciliation §F.4.1): `config.yaml` und `PORTFOLIO.md` beschreiben weiterhin eine FLAG-Wirkung, der das Depot bei den Core-4 bewusst nicht folgt. Die hier angewandte Zweiteilung ist noch nirgends normativ hinterlegt — gehört nach `REGELWERK.yaml` (PIPELINE #83).
- **Rebalancing_Tool_v4.0** bleibt inkonsistent (Juni-Roster, kennt Adobe/Alphabet/Meta/Veeva/Costco nicht, KYCCF-Zeile trägt den Veeva-Wert). Nicht nachgeführt — gehört in die Architektur-Phase.
- **Kein §18-Sync ausgelöst.** Analog zum 26.08.-Beschluss: Markdown-/Config-Ebene wird erst in der Architektur-Phase nachgezogen.

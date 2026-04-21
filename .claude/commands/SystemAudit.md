---
description: Run systemweiten Drift-Audit via 03_Tools/system_audit.py. Übergib Flags wie --core, --full, --vault, --json, --no-write, -v als $ARGUMENTS.
---

Run the following command and report the N/M PASS result to the user:

```bash
python 03_Tools/system_audit.py $ARGUMENTS
```

Wenn FAIL: liste pro fehlgeschlagener Kategorie die Anzahl + die ersten 3 FailureDetails (location, expected, actual, hint).
Wenn PASS: zeige die einzeilige Summary + den neuen Last-Audit-Timestamp aus STATE.md.
Wenn Exit-Code 2: IO- oder Tool-intern-Fehler — Stderr zeigen, nicht als "audit-FAIL" kommunizieren.

Default ohne $ARGUMENTS = --core (alle 7 Kern-Checks, schreibt STATE.md Last-Audit-Block).

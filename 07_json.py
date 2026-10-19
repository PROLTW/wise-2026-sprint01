"""Sprint 1 | Pflichtteil 7: JSON laden und Dictionary-Werte prüfen.

START: python 07_json.py
"""

import json
from pathlib import Path

DATEN_DATEI = Path(__file__).parent / "data" / "arbeitsplatz.json"


def lade_arbeitsplatz(pfad):
    with pfad.open(encoding="utf-8") as datei:
        return json.load(datei)


if __name__ == "__main__":
    arbeitsplatz = lade_arbeitsplatz(DATEN_DATEI)
    print(f"Arbeitsplatz: {arbeitsplatz['name']}")

    # TODO 1: Geben Sie "Bereich: [nicht angegeben]" aus, solange
    # der Schluessel 'bereich' fehlt (Tipp: .get mit Ersatzwert).

    # TODO 2: Ergaenzen Sie in der JSON-Datei den Eintrag
    # "bereich": "Vormontage". Ergebnis danach: Bereich: Vormontage.

    # TODO 3: Geben Sie mit if/else "Status: aktiv" oder
    # "Status: inaktiv" aus (Schluessel: 'aktiv').

    # Zusatz: Berechnen Sie aus 'kapazitaet_pro_stunde' mit 3 Stunden
    # einen Wert und geben Sie ihn aus. Was bedeutet hier der Typ int?

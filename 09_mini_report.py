"""Sprint 1 | Pflichtteil 9: Mini-Report aus CSV + JSON.

START: python 09_mini_report.py
Der Report verbindet bekannte Bausteine; keine Projektfachlogik.
"""

import csv
import json
from pathlib import Path

DATEN = Path(__file__).parent / "data"


def status_fuer(menge):
    """TODO 1: Geben Sie klein (<8), mittel (8..19) oder gross (ab 20) zurück."""
    return "noch offen"


def reportzeile(auftrag, menge):
    """TODO 2: Nutzen Sie status_fuer und geben Sie z. B. 'A-01: klein' zurück."""
    return "noch offen"


def mini_report():
    # Einlesen: kleine Einstiegshilfe; vervollständigen Sie nur die TODOs.
    with (DATEN / "arbeitsplatz.json").open(encoding="utf-8") as datei:
        arbeitsplatz = json.load(datei)

    with (DATEN / "auftraege.csv").open(encoding="utf-8", newline="") as datei:
        zeilen = list(csv.DictReader(datei))

    # TODO 3: Geben Sie "Report: Montage / Vormontage" aus.
    # Verwenden Sie die JSON-Schluessel 'name' und 'bereich'.
    # Geben Sie außerdem mit if/else "Status Arbeitsplatz: aktiv" oder "...: inaktiv" aus.

    gesamt = 0
    anzahl_auftraege = 0
    pruefauftraege = 0
    # TODO 4: Gehen Sie mit for durch zeilen.
    # Wandeln Sie in jedem Durchlauf zeile['menge'] in int um.
    # Summieren Sie die Menge in gesamt und zählen Sie anzahl_auftraege hoch.
    # Geben Sie pro Auftrag mit reportzeile "A-01: klein" usw. aus.
    # Erhöhen Sie pruefauftraege, wenn die Menge mindestens 8 beträgt.

    # TODO 5: Geben Sie Anzahl, Gesamtmenge und Zahl der Prüffälle aus.


if __name__ == "__main__":
    mini_report()

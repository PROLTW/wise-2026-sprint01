"""Sprint 1 | Pflichtteil 6: CSV-Dateien einlesen und summieren.

START: python 06_csv.py
Pfad ist relativ zu dieser Python-Datei, nicht zum Terminal-Verzeichnis.
"""

import csv
from pathlib import Path

DATEN_DATEI = Path(__file__).parent / "data" / "auftraege.csv"


def lade_auftraege(pfad):
    """Liest CSV-Zeilen als Dictionaries in eine Liste."""
    auftraege = []
    with pfad.open(encoding="utf-8", newline="") as datei:
        for zeile in csv.DictReader(datei):
            # Beispiel: zeile["artikel"] ist ein Text aus der CSV.
            # TODO 1: Ersetzen Sie 0 durch int(zeile["menge"]).
            menge = 0
            # TODO 2: Ueberlegen Sie: Welcher Eintrag ist Zahl, welcher Text?
            auftraege.append({
                "auftrag": zeile["auftrag"],
                "artikel": zeile["artikel"],
                "menge": menge,
            })
    return auftraege


def gesamtmenge(auftraege):
    """Addiert die Mengen aus allen eingelesenen Datensaetzen."""
    summe = 0
    # TODO 3: Fuegen Sie eine for-Schleife mit summe += ... ein.
    return summe


if __name__ == "__main__":
    auftraege = lade_auftraege(DATEN_DATEI)
    for auftrag in auftraege:
        print(f"{auftrag['auftrag']} {auftrag['artikel']}: {auftrag['menge']}")
    print(f"Gesamtmenge: {gesamtmenge(auftraege)}")

    # TODO 4: Ergaenzen Sie in data/auftraege.csv die Zeile A-04,Nippel,6.
    # Erwartung: vier Zeilen, Gesamtmenge: 42.
    # Zusatz: Berechnen Sie in einer zweiten Schleife, wie viele
    # Auftraege eine Menge von mindestens 10 enthalten.

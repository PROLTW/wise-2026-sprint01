"""Sprint 1 | Pflichtteil 3: list, dict, tuple und set.

START: python 03_sammlungen.py
"""

# Beispiel: [ ] erzeugt eine Liste; Positionen beginnen bei 0.
farben = ["rot", "blau"]
print(f"Beispiel: {farben[0]}")

pruefmengen = [4, 8, 20]
# TODO 1: Erweitern Sie die Liste mit .append(6).
# Schreiben Sie die passende Anweisung hier.

# TODO 2: Geben Sie die Anzahl der Werte (len) und den zweiten Wert aus.
# Soll: Anzahl Pruefmengen: 4
# Soll: Zweite Pruefmenge: 8

arbeitsplatz = {
    "id": "AP-01",
    "name": "Montage",
    # TODO 3: Ergaenzen Sie den Schluessel "aktiv" mit dem Wert True.
}

# TODO 4: Greifen Sie mit einem Schluessel auf das Dictionary zu.
# Soll: Arbeitsplatz: Montage
# Soll: Aktiv: True

schritte = ("lesen", "pruefen")           # tuple: feste Reihenfolge
artikel = {"Nabe", "Felge", "Nabe"}     # set: keine Dopplungen

# TODO 5: Geben Sie schritte[0] und die Anzahl der Elemente in artikel aus.
# Soll: Erster Schritt: lesen
# Soll: Verschiedene Artikel: 2

# Zusatz: Warum ist die Reihenfolge der Ausgabe von artikel als set
# nicht zuverlässig? Probieren Sie sorted(artikel).

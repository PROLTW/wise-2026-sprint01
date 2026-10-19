"""Sprint 1 | Pflichtteil 4: for, while und Zwischensummen.

START: python 04_schleifen.py
"""

mengen = [4, 12, 20]

# Beispiel einer for-Schleife (drei Ausgaben):
for wort in ["Start", "Pruefen", "Ende"]:
    print(f"Schritt: {wort}")

summe = 0
# TODO 1: Schreiben Sie eine zweite for-Schleife über mengen.
# Addieren Sie jede menge zu summe (summe += menge).
# Geben Sie IM Schleifenblock jeweils aus: Zwischenstand: 4 / 16 / 36

print(f"Gesamtmenge: {summe}")

# Beispiel: Hier ist eine sichere while-Schleife vorbereitet.
zaehler = 0
while zaehler < 3:
    # TODO 2: Geben Sie "Runde: 1", dann 2, dann 3 aus.
    # Zählen Sie deshalb beim Ausgeben + 1.
    # Ein pass ist nur ein Platzhalter: Entfernen Sie ihn nach dem Ergänzen.
    pass
    zaehler += 1  # NICHT entfernen: So endet die Schleife.

# TODO 3: Erklären Sie im Beobachtungsblatt, warum die while-Schleife endet.
# Zusatz: Ersetzen Sie 3 durch len(mengen) und erläutern Sie den Vorteil.

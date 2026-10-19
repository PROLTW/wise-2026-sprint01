"""Sprint 1 | Pflichtteil 2: Vergleiche und if / elif / else.

START: python 02_bedingungen.py
"""

menge = 12
GRENZE_MITTEL = 8
GRENZE_GROSS = 20

# Beispiel ohne Bezug zur Aufgabe:
# temperatur = 18
# if temperatur < 10:
#     print("kalt")
# else:
#     print("nicht kalt")

status = "noch offen"

# TODO 1: Schreiben Sie unterhalb dieses Kommentars eine if-elif-else-Kette.
# Regeln: menge >= GRENZE_GROSS -> "gross"
#         sonst menge >= GRENZE_MITTEL -> "mittel"
#         sonst -> "klein"
# Weisen Sie das Ergebnis jeweils der Variablen status zu.
# WICHTIG: Der gross-Fall wird zuerst geprüft.

print(f"{menge}: {status}")

# TODO 2: Ändern Sie die Menge nacheinander auf 4, 8 und 20.
# Notieren Sie Ihre Voraussage VOR dem Start im Beobachtungsblatt.
# Setzen Sie menge am Ende wieder auf 12 zurück.

# TODO 3 (Zusatz): Was ändert sich, wenn >= durch > ersetzt wird?
# Probieren Sie den Grenzwert 8 und machen Sie die Änderung rückgängig.

"""Sprint 1 | Pflichtteil 1: Variablen, Datentypen, Rechnen und Ausgeben.

START: python 01_werte.py
Nur die TODO-Stellen bearbeiten. Jede Datei darf einzeln gestartet werden.
"""

# Ein Wert wird mit = einer Variablen zugewiesen.
name = "Ihr Name"             # str: Text
menge = 6                     # int: ganze Zahl
preis_pro_stueck = 2.50       # float: Kommazahl (in Python mit Punkt)
aktiv = True                  # bool: wahr oder falsch
notiz = None                  # noch kein Wert vorhanden

# Beispiel: Ein f-String setzt den Inhalt einer Variablen in Text ein.
print(f"Hallo, {name}!")
print(f"Artikelmenge: {menge}")

# TODO 1: Ersetzen Sie 0.0 durch menge * preis_pro_stueck.
gesamtwert = 0.0

# TODO 2: Ersetzen Sie False durch den Vergleich menge >= 5.
mindestmenge_erreicht = False

# TODO 3: Schreiben Sie unter diese Zeile eine eigene print-Anweisung.
# Geben Sie den Gesamtwert mit GENAU zwei Nachkommastellen aus.
# Soll: Gesamtwert: 15.00

# TODO 4: Schreiben Sie eine Ausgabe zur booleschen Variablen.
# Soll: Mindestmenge erreicht: True

# TODO 5: Geben Sie "Notiz: None" mit einem f-String aus.
# Zusatz, falls Zeit: Geben Sie type(menge) und type(preis_pro_stueck) aus.

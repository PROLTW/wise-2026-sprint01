# Erste Hilfe – Python lesen, testen und Fehler finden

## Das wichtigste Syntax-Muster

```python
menge = 12                      # = weist einen Wert zu
print(f"Menge: {menge}")        # f-String setzt Werte ein
if menge >= 10:                # : leitet einen Block ein
    print("mindestens zehn")  # genau vier Leerzeichen Einrückung
else:
    print("unter zehn")
```

`==` vergleicht Werte, `=` weist einen Wert zu. `>=` bedeutet *größer oder gleich*. Python unterscheidet Groß-/Kleinschreibung: `Menge` ist nicht `menge`. Zeichenketten stehen in `'...'` oder `"..."`.

## Eingabewerte und Typen

- `12` ist ein `int`, `12.5` ist ein `float`, `"12"` ist ein `str`.
- `int("12")` macht aus dem Text `"12"` die Zahl `12`; `"12" + "2"` ergibt den Text `"122"`.
- `True`, `False` sind `bool`; `None` steht für „noch kein Wert“.
- `f"{preis:.2f}"` zeigt `2.50`, wenn `preis = 2.5` ist.

## Sammlungen

```python
zahlen = [4, 8, 20]                 # list (Reihenfolge, veränderbar)
print(zahlen[0])                    # erstes Element
person = {"name": "Alex"}           # dict (Schlüssel zu Wert)
print(person["name"])
print(person.get("alter", "fehlt"))   # kein KeyError bei fehlendem Schlüssel
schritte = ("lesen", "prüfen")       # tuple (fixe Elemente)
tags = {"rot", "rot", "blau"}        # set (Dopplungen entfallen)
```

## Schleifen und Funktionen

```python
summe = 0
for zahl in [2, 3]:
    summe += zahl                    # entspricht summe = summe + zahl

index = 0
while index < 2:
    print(index)
    index += 1                       # ohne Änderung droht eine Endlosschleife

def verdoppeln(x):
    return x * 2                    # return gibt den Wert zurück

print(verdoppeln(3))                 # print zeigt ihn an
```

## Häufige Fehlermeldungen

| Fehler | Was er meist bedeutet | Was Sie zuerst tun |
| --- | --- | --- |
| `SyntaxError` | Zeichen, Doppelpunkt oder Klammer fehlt | Letzte gezeigte Codezeile und vorherige Zeile anschauen |
| `IndentationError` | Einrückung stimmt nicht | 4 Leerzeichen pro eingerücktem Block, keine Mischung mit Tabs |
| `NameError` | Name nicht definiert oder anders geschrieben | Tippfehler in Variablenbezeichnungen prüfen |
| `TypeError` | Operation passt nicht zum Typ | `type(...)` ausgeben, ggf. `int(...)` verwenden |
| `KeyError` | Dictionary-Schlüssel fehlt | CSV/JSON-Kopfzeile und Schreibweise vergleichen; `.get(...)` prüfen |
| `FileNotFoundError` | Datei am Pfad nicht gefunden | Prüfen, ob der Ordner `data` vorhanden ist und VS Code `starter` geöffnet hat |
| `JSONDecodeError` | JSON enthält z. B. ein fehlendes Komma | Kommas, doppelte Anführungszeichen und Klammern kontrollieren |

**Debugging-Reihenfolge:** (1) speichern, (2) richtigen Dateinamen starten, (3) vollständige Meldung lesen, (4) **eine** Stelle ändern, (5) erneut starten. Der freiwillige technische Schlusscheck am Ende kann `[OFFEN]` melden; kehren Sie dann immer zur einzelnen Datei und ihrer sichtbaren Ausgabe zurück.

**Eigenständig bleiben:** Lesen Sie bei Schwierigkeiten zuerst ein Muster im Arbeitsblatt und verändern Sie es. Eine fertige Lösung einzukopieren hilft beim nächsten Teil kaum.

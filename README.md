# Sprint 1 – Python selbst schreiben (Starterpaket)

**Zielgruppe:** erste praktische Python-Erfahrungen nach Sprint 0 (VS Code und Python funktionieren); keine Zusatzpakete erforderlich. Der Kernteil besteht aus acht Aufgaben; der Mini-Report ist eine freiwillige Vertiefung.

## Wo anfangen?

1. Beziehen Sie das Material über [PROLTW/wise-2026-sprint01](https://github.com/PROLTW/wise-2026-sprint01): per `git clone` oder über **Code → Download ZIP**. Die vollständige Einrichtung von Git, VS Code und Python 3.14 steht im Arbeitsblatt Sprint 0.
2. Öffnen Sie **diesen Ordner `starter`** in VS Code und legen Sie darin eine Python-3.14-Umgebung `.venv` an. Die Einzelaufgaben benötigen keine Zusatzpakete.
3. Öffnen Sie das Arbeitsblatt für Sprint 1 aus Moodle parallel zu VS Code. Im V9-Quellprojekt liegt es unter `lehrmaterial/v9/arbeitsblaetter/02a-sprint01-python-grundlagen.qmd`.
4. Starten Sie im VS-Code-Terminal `python 01_werte.py`. Unter Windows kann der Befehl `py 01_werte.py` heißen, unter Linux/macOS `python3 01_werte.py`.
5. Arbeiten Sie alle `TODO`-Stellen in der jeweiligen Datei mit dem Arbeitsblatt ab. Speichern Sie vor jedem Start (`Strg+S`).
6. Nach jedem Teil starten Sie **die gerade bearbeitete Datei** und vergleichen die sichtbare Ausgabe mit dem Arbeitsblatt. Nach Teil 8 können Sie freiwillig `python tests/selbstcheck.py` als technischen Schlusscheck starten.

**Wichtig:** Der Starter ist syntaktisch lauffähig, aber die TODOs sind noch nicht gelöst. Ihr Lernweg ist: Code lesen → selbst ergänzen → Ausgabe vorhersagen → einzelne Datei starten → Ausgabe erklären. Der freiwillige Schlusscheck prüft nur zusätzliche Ergebnisse; er ersetzt diesen Lernweg nicht. Fehlermeldungen sind Lerngelegenheiten; die Hilfe steht in `HILFE.md`.

## Code-Landkarte

| Datei | Neu eingeführt | Was Sie selbst schreiben |
| --- | --- | --- |
| `01_werte.py` | `str`, `int`, `float`, `bool`, `None`; `print`, f-String | Berechnung, Vergleich und drei Ausgaben |
| `02_bedingungen.py` | Vergleiche und `if`/`elif`/`else` | dreistufige Einordnung |
| `03_sammlungen.py` | `list`, `dict`, `tuple`, `set` | Liste erweitern, Schlüssel lesen, Ausgabe |
| `04_schleifen.py` | `for`, `while`, Akkumulator | for-Summe und while-Ausgaben |
| `05_funktionen.py` | `def`, Parameter, `return` | zwei Funktionen |
| `06_csv.py` + `data/auftraege.csv` | `csv.DictReader`, `int(...)`, Pfade | Umwandlung, Summierung, neue Datenzeile |
| `07_json.py` + `data/arbeitsplatz.json` | `json.load`, `.get(...)` | Schlüsselausgabe, JSON-Ergänzung, Bedingung |
| `08_objekte.py` | `class`, `self`, Methode | Prüf-Methode und Schleifen anwenden |
| `09_mini_report.py` | Pflichtteil 9: Bausteine kombinieren | vollständiger Report aus CSV und JSON |

## Ordnerstruktur

```text
starter/
├── README.md
├── HILFE.md
├── BEOBACHTUNGEN.txt
├── 01_werte.py ... 09_mini_report.py
├── data/
│   ├── auftraege.csv
│   └── arbeitsplatz.json
└── tests/
    └── selbstcheck.py
```

## Was ist die Abgabe?

Packen Sie den bearbeiteten Ordner `starter` als ZIP-Datei. Der Dateiname lautet verbindlich `wi_sprint01-G_gruppennummer.zip`, zum Beispiel `wi_sprint01-G_07.zip`. Laden Sie die Datei in der Moodle-Aktivität für Sprint 1 hoch. Die Abgabe enthält die neun bearbeiteten Pflicht-Dateien `01_werte.py` bis `09_mini_report.py`, die beiden Daten-Dateien und das knapp ausgefüllte `BEOBACHTUNGEN.txt`.

Der technische Schlusscheck `python tests/selbstcheck.py` ist freiwillig. Wenn Sie ihn ausführen, ist `Ergebnis: 9/9 Teile bestanden.` ein hilfreicher Hinweis, ersetzt aber nicht die sichtbaren Läufe und Ihre Erklärungen. Lassen Sie `.venv` und `__pycache__` aus der ZIP heraus. Zeigen Sie in `BEOBACHTUNGEN.txt` zu zwei Aufgaben den Weg **Eingabe → Code → Ausgabe**. Ein lokaler Commit ist sinnvoll, wenn Git in Sprint 0 eingerichtet wurde. **Keine** Fremdbibliotheken, Datenbank, Weboberfläche oder Projektarchitektur.

**Nicht tun:** Für `01` bis `08` brauchen Sie die ältere Datei `prelude.py` nicht. Die neuen Einzelaufgaben sind bewusst unabhängig voneinander.

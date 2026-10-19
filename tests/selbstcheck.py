"""Freiwilliger technischer Schlusscheck fuer Sprint 1 (nur Python-Standardbibliothek).

Aufruf nach Teil 9: python tests/selbstcheck.py
Fuer die Lehrperson/Fehlersuche: python tests/selbstcheck.py --nur 04

Vor der Bearbeitung sind fehlgeschlagene Tests NORMAL. Sie sind Lernhilfen.
"""

import argparse
import ast
import contextlib
import io
import runpy
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def programm_ausgabe(dateiname):
    """Eigenes Skript isoliert und mit Zeitlimit ausführen (Schutz bei while)."""
    try:
        prozess = subprocess.run(
            [sys.executable, str(ROOT / dateiname)],
            cwd=ROOT, capture_output=True, text=True, timeout=5, check=False,
        )
    except subprocess.TimeoutExpired as fehler:
        raise RuntimeError("Zeitlimit überschritten: Prüfen Sie Ihre while-Schleife.") from fehler
    if prozess.returncode:
        letzte_zeile = prozess.stderr.strip().splitlines()[-1] if prozess.stderr.strip() else "Unbekannter Python-Fehler"
        raise RuntimeError(f"Skript konnte nicht starten: {letzte_zeile}")
    return prozess.stdout


def testlauf_mit_menge(dateiname, testmenge):
    """Nur im Selbstcheck eine Menge ändern, ohne Lern-Dateien zu überschreiben."""
    datei = ROOT / dateiname
    quellcode = ast.parse(datei.read_text(encoding="utf-8"), filename=str(datei))
    for anweisung in quellcode.body:
        if isinstance(anweisung, ast.Assign) and any(
            isinstance(ziel, ast.Name) and ziel.id == "menge" for ziel in anweisung.targets
        ):
            anweisung.value = ast.Constant(value=testmenge)
            break
    else:
        raise AssertionError("Eine einfache Zuweisung `menge = ...` muss vorhanden sein.")
    speicher = io.StringIO()
    namensraum = {"__name__": "__main__", "__file__": str(datei)}
    with contextlib.redirect_stdout(speicher):
        exec(compile(ast.fix_missing_locations(quellcode), str(datei), "exec"), namensraum)
    return speicher.getvalue(), namensraum


def funktionen_aus_datei(dateiname):
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(str(ROOT / dateiname), run_name="__lernmodul__")


def pruefe_01():
    ausgabe = programm_ausgabe("01_werte.py")
    assert "Gesamtwert: 15.00" in ausgabe, "Gesamtwert fehlt oder ist nicht auf 2 Stellen formatiert."
    assert "Mindestmenge erreicht: True" in ausgabe, "Vergleich oder bool-Ausgabe fehlt."
    assert "Notiz: None" in ausgabe, "Notiz-Ausgabe fehlt."
    ausgabe_klein, werte = testlauf_mit_menge("01_werte.py", 4)
    assert werte["gesamtwert"] == 10, "Gesamtwert muss aus Menge und Preis berechnet werden."
    assert werte["mindestmenge_erreicht"] is False, "Bei Menge 4 ist der Vergleich False."
    assert "Gesamtwert: 10.00" in ausgabe_klein, "Die Ausgabe muss der Berechnung folgen."


def pruefe_02():
    for menge, status in ((4, "klein"), (8, "mittel"), (12, "mittel"), (20, "gross")):
        ausgabe, _ = testlauf_mit_menge("02_bedingungen.py", menge)
        assert f"{menge}: {status}" in ausgabe, f"Bei Menge {menge} wird {status!r} erwartet."


def pruefe_03():
    ausgabe = programm_ausgabe("03_sammlungen.py")
    for zeile in (
        "Anzahl Pruefmengen: 4",
        "Zweite Pruefmenge: 8",
        "Arbeitsplatz: Montage",
        "Aktiv: True",
        "Erster Schritt: lesen",
        "Verschiedene Artikel: 2",
    ):
        assert zeile in ausgabe, f"Fehlende Ausgabe: {zeile}"


def pruefe_04():
    ausgabe = programm_ausgabe("04_schleifen.py")
    for zeile in ("Zwischenstand: 4", "Zwischenstand: 16", "Zwischenstand: 36", "Gesamtmenge: 36"):
        assert zeile in ausgabe, f"Fehlende Ausgabe: {zeile}"
    for n in (1, 2, 3):
        assert f"Runde: {n}" in ausgabe, f"Runde {n} fehlt."


def pruefe_05():
    mod = funktionen_aus_datei("05_funktionen.py")
    regel = mod["status_fuer"]
    for eingabe, erwartet in ((4, "klein"), (7, "klein"), (8, "mittel"), (19, "mittel"), (20, "gross"), (21, "gross")):
        assert regel(eingabe) == erwartet, f"status_fuer({eingabe}) sollte {erwartet!r} ergeben."
    assert mod["hinweis_fuer"]("Nabe", 12) == "Nabe (12): mittel", "Rückgabetext von hinweis_fuer stimmt nicht."
    ausgabe = programm_ausgabe("05_funktionen.py")
    for zeile in ("4: klein", "8: mittel", "20: gross", "Nabe (12): mittel"):
        assert zeile in ausgabe, f"Kontrollausgabe fehlt: {zeile}"


def pruefe_06():
    mod = funktionen_aus_datei("06_csv.py")
    daten = mod["lade_auftraege"](ROOT / "data" / "auftraege.csv")
    assert len(daten) == 4, "Vier Aufträge erwartet: CSV-Zeile A-04 fehlt."
    assert [x["menge"] for x in daten] == [4, 12, 20, 6], "CSV-Mengen sollen Zahlen 4, 12, 20, 6 sein."
    assert mod["gesamtmenge"](daten) == 42, "Die Summe sollte 42 sein."
    ausgabe = programm_ausgabe("06_csv.py")
    assert "A-04 Nippel: 6" in ausgabe and "Gesamtmenge: 42" in ausgabe, "Neue Zeile oder Summe erscheint nicht."


def pruefe_07():
    mod = funktionen_aus_datei("07_json.py")
    daten = mod["lade_arbeitsplatz"](ROOT / "data" / "arbeitsplatz.json")
    assert daten.get("bereich") == "Vormontage", "In der JSON-Datei fehlt bereich = Vormontage."
    ausgabe = programm_ausgabe("07_json.py")
    assert "Bereich: Vormontage" in ausgabe, "Bereich-Ausgabe fehlt."
    assert "Status: aktiv" in ausgabe, "Bedingte Status-Ausgabe fehlt."


def pruefe_08():
    mod = funktionen_aus_datei("08_objekte.py")
    Auftrag = mod["Auftrag"]
    klein = Auftrag("X", "Test", 4)
    gross = Auftrag("Y", "Test", 12)
    assert klein.braucht_pruefung(8) is False, "Bei 4 und Grenze 8: False."
    assert gross.braucht_pruefung(8) is True, "Bei 12 und Grenze 8: True."
    assert "X: Test (4 Stueck)" == klein.beschreibung(), "Beschreibung stimmt nicht."
    ausgabe = programm_ausgabe("08_objekte.py")
    assert "Pruefen: A-02" in ausgabe and "Pruefen: A-03" in ausgabe, "A-02 und A-03 müssen angezeigt werden."
    assert "A-01: Nabe" in ausgabe, "Objektbeschreibung fehlt."


def pruefe_09():
    ausgabe = programm_ausgabe("09_mini_report.py")
    for zeile in ("Report: Montage / Vormontage", "Status Arbeitsplatz: aktiv", "A-01: klein", "A-02: mittel", "A-03: gross", "A-04: klein", "Auftraege im Report: 4", "Gesamtmenge im Report: 42", "Pruefauftraege: 2"):
        assert zeile in ausgabe, f"Fehlende Report-Zeile: {zeile}"


CHECKS = {
    "01": pruefe_01,
    "02": pruefe_02,
    "03": pruefe_03,
    "04": pruefe_04,
    "05": pruefe_05,
    "06": pruefe_06,
    "07": pruefe_07,
    "08": pruefe_08,
    "09": pruefe_09,
}


def main():
    parser = argparse.ArgumentParser(description="Sprint-1-Selbstcheck ohne Zusatzpakete")
    parser.add_argument("--nur", choices=CHECKS, help="Nur einen Teil pruefen, z.B. --nur 03")
    args = parser.parse_args()

    auswahl = [args.nur] if args.nur else list(CHECKS)
    bestanden = 0
    for nummer in auswahl:
        try:
            CHECKS[nummer]()
        except Exception as fehler:
            # Bewusst eine freundliche Kurzmeldung; Details stehen im Einzelprogramm.
            print(f"[OFFEN] Teil {nummer}: {type(fehler).__name__}: {fehler}")
        else:
            bestanden += 1
            print(f"[OK]    Teil {nummer}")
    print(f"\nErgebnis: {bestanden}/{len(auswahl)} Teile bestanden.")
    return 0 if bestanden == len(auswahl) else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""Sprint 1 | Pflichtteil 5: Funktionen, Parameter und return.

START: python 05_funktionen.py
"""

# Beispiel (anders als Ihre Aufgabe):
def quadrat(zahl):
    return zahl * zahl

print(f"Beispiel-Quadrat: {quadrat(3)}")

GRENZE_MITTEL = 8
GRENZE_GROSS = 20


def status_fuer(menge):
    """Gibt 'klein', 'mittel' oder 'gross' zurueck."""
    # TODO 1: Ersetzen Sie den folgenden return durch if/elif/else.
    # Prüfen Sie zuerst >= GRENZE_GROSS, dann >= GRENZE_MITTEL.
    # Jede Alternative soll den passenden Text mit return zurückgeben.
    return "noch offen"


def hinweis_fuer(artikel, menge):
    """Zum Beispiel: Nabe (12): mittel."""
    # TODO 2: Rufen Sie status_fuer(menge) auf.
    # Geben Sie den kombinierten Text mit return und einem f-String zurück.
    return "noch offen"


if __name__ == "__main__":
    # TODO 3: Machen Sie drei Kontrollaufrufe. Die for-Schleife ist vorbereitet.
    for testmenge in [4, 8, 20]:
        print(f"{testmenge}: {status_fuer(testmenge)}")

    print(hinweis_fuer("Nabe", 12))

    # Zusatz: Testen Sie status_fuer(7), status_fuer(19) und status_fuer(21).

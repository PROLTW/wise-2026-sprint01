"""Sprint 1 | Kernteil 8: erstes Objekt (ca. 20 Minuten).

START: python 08_objekte.py
"""

# Eine Klasse ist ein Bauplan; Auftrag("A-01", "Nabe", 4) ist ein Objekt.
class Auftrag:
    def __init__(self, nummer, artikel, menge):
        self.nummer = nummer
        self.artikel = artikel
        self.menge = menge

    def beschreibung(self):
        return f"{self.nummer}: {self.artikel} ({self.menge} Stueck)"

    def braucht_pruefung(self, grenze):
        # TODO 1: Ersetzen Sie False durch einen passenden Vergleich.
        return False


if __name__ == "__main__":
    auftraege = [
        Auftrag("A-01", "Nabe", 4),
        Auftrag("A-02", "Felge", 12),
        Auftrag("A-03", "Speiche", 20),
    ]

    # TODO 2: Geben Sie fuer jedes Objekt beschreibung() aus.

    # TODO 3: Geben Sie mit if fuer jedes Objekt mit Menge >= 8
    # die Zeile "Pruefen: A-02" bzw. "Pruefen: A-03" aus.
    # Nutzen Sie die Methode braucht_pruefung(8) statt eines
    # direkten Vergleichs im Schleifenblock.

    # Zusatz: Erzeugen Sie ein viertes Auftrag-Objekt und pruefen Sie es.

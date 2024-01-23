from land import Land
from schiff import Schiff

class Containerschiff(Schiff):
    def __init__(self, name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, anzahl_container, leistung_in_kw):
        super().__init__(name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, leistung_in_kw)
        self.anzahl_container = anzahl_container

    def get_anzahl_container(self):
        return self.anzahl_container

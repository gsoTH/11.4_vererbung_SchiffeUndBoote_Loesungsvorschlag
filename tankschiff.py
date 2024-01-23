from land import Land
from schiff import Schiff

class Tankschiff(Schiff):
    def __init__(self, name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, ladegewicht_in_t, leistung_in_kw):
        super().__init__(name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, leistung_in_kw)
        self.ladegewicht_in_t = ladegewicht_in_t

    def get_ladegewicht_in_t(self):
        return self.ladegewicht_in_t

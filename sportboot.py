from land import Land
from besitzer import Besitzer
from boot import Boot

class Sportboot(Boot):
    def __init__(self, name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, leistung_in_kw, besitzer):
        super().__init__(name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, besitzer)
        self.leistung_in_kw = leistung_in_kw

    def get_leistung_in_kw(self):
        return self.leistung_in_kw

    def set_leistung_in_kw(self, value):
        self.leistung_in_kw = value

from wasserfahrzeug import Wasserfahrzeug
from abc import ABC

class Schiff (Wasserfahrzeug, ABC):
    def __init__(self, name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, leistung_in_kw):
        super().__init__(name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern)
        self.land = land
        self.leistung_in_kw = leistung_in_kw

    def get_land(self):
        return self.land
    
    def get_leistung_in_kw(self):
        return self.leistung_in_kw

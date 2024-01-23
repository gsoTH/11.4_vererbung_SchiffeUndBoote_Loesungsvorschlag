from abc import ABC

class Wasserfahrzeug(ABC):
    def __init__(self, name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern):
        self.name = name
        self.laenge_in_metern = laenge_in_metern
        self.breite_in_metern = breite_in_metern
        self.hoehe_in_metern = hoehe_in_metern
        self.tiefgang_in_metern = tiefgang_in_metern

    def get_name(self):
        return self.name

    def get_laenge_in_metern(self):
        return self.laenge_in_metern

    def get_breite_in_metern(self):
        return self.breite_in_metern

    def get_hoehe_in_metern(self):
        return self.hoehe_in_metern

    def get_tiefgang_in_metern(self):
        return self.tiefgang_in_metern

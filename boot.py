from wasserfahrzeug import Wasserfahrzeug
from abc import ABC

class Boot(Wasserfahrzeug, ABC):

    def __init__(self, name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, besitzer):
            super().__init__(name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern)
            self.besitzer = besitzer

    def get_besitzer(self):
        return self.besitzer

    def set_besitzer(self, value):
        self.besitzer = value
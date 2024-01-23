from land import Land
from besitzer import Besitzer
from boot import Boot

class Segelboot(Boot):
    def __init__(self, name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, segelflaeche_in_qm2, besitzer):
        super().__init__(name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, besitzer)
        self.segelflaeche_in_qm2 = segelflaeche_in_qm2

    def get_segelflaeche_in_qm2(self):
        return self.segelflaeche_in_qm2

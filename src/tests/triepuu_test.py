import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os

class Test_Triepuu(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
        self.testipuu = Triepuu()
        self.testipuu.lisaa_sanat(self.tekstinkasittelija.sanakirja3)

    def test_puussa_on_haetut_asiat(self):
        if "kaksi" in self.testipuu.hae_puusta("yksi").lapset.keys():
            tulos1 = True
        else:
            tulos1 = False
        if "kolme" in self.testipuu.hae_puusta("yksi").lapset.keys():
            tulos2 = True
        else:
            tulos2 = False
        self.assertEqual(tulos1, True)
        self.assertEqual(tulos2, False)

    def test_puussa_oikea_maara_lehtia(self):
        self.assertEqual(self.testipuu.get_koko(), 3)
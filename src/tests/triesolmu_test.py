import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
from triesolmu import Triesolmu
import os

class Test_Triepuu(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
        self.testipuu = Triepuu()
        self.testipuu.lisaa_sanat(self.tekstinkasittelija.sanakirja3)

    def test_solmu_on_lehti(self):
        tulos = self.testipuu.juuri.get_lapsi("yksi").get_lapsi("kaksi").get_lapsi("kolme").lehti
        self.assertEqual(tulos, True)

    def test_solmun_lapsi_menee_oikein(self):
        tulos = str(self.testipuu.juuri.get_lapsi("yksi").get_lapsi("kaksi"))
        self.assertEqual(tulos, "(kaksi, dict_keys(['kolme']))")
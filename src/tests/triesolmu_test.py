import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
from triesolmu import Triesolmu
import os

# solmu esiintyy vain triepuun osana ja on luokkana pienehkö, joten testit täysin triviaaleja.

class Test_Triepuu(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
        self.testipuu = Triepuu()
        self.testipuu.lisaa_sanat_test(self.tekstinkasittelija.sanakirja3)

    def test_solmu_on_lehti(self):
        tulos = self.testipuu.get_lapsi("yksi", self.testipuu.juuri)
        tulos = self.testipuu.get_lapsi("kaksi", tulos)
        tulos = self.testipuu.get_lapsi("kolme", tulos).lehti
        self.assertEqual(tulos, True)

    def test_solmun_lapsi_menee_oikein(self):
        tulos = self.testipuu.get_lapsi("yksi", self.testipuu.juuri)
        tulos = str(self.testipuu.get_lapsi("kaksi", tulos))
        self.assertEqual(tulos, "(kaksi, dict_keys(['kolme']). False)")

    def test_lapsimaara(self):
        self.assertEqual(3, self.testipuu.juuri.lapsimaara())

    def test_tulostus(self):
        self.assertEqual(self.testipuu.juuri.__str__(),"on juuri" )
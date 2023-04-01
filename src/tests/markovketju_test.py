import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
from markovketju import Markovketju
import os

class Test_Triepuu(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi2.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
        self.testipuu = Triepuu()
        self.testipuu.lisaa_sanat_test(self.tekstinkasittelija.sanakirja3)
        self.ketju = Markovketju(1)

    def test_lause_1_aste_toimii(self):
        tulos = self.ketju.luo_lause_1_aste("yksi",self.testipuu,1)
        self.assertEqual(tulos, "TEST: yksi kaksi kolme")
        tulos2 = self.ketju.luo_lause_1_aste("yksi",self.testipuu,5)
        tulos2 = tulos2.split()
        self.assertEqual(len(tulos2), 8)

    def test_lause_2_aste_toimii(self):
        aputulos = self.ketju.luo_lause_2_aste("neljä",self.testipuu,1)
        tulos = ["yksi", "kaksi", "kolme"] in aputulos.split()
        self.assertEqual(tulos, False)
        tulos2 = self.ketju.luo_lause_2_aste("kuusi",self.testipuu,0)
        self.assertEqual(tulos2, "TEST: kuusi neljä viisi ")
import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
import os

# yksinkertaiset testit sille että kykenee käsittelemään tekstitiedoston ja antamaan datan halutussa muodossa ulos.
# työn testauksen pääpaino kuitenkin muualla kuin datan esikäsittelijässä.


class Test_Tekstinkasittelija(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)

    def test_alusta_teksti(self):
        self.assertEqual(self.tekstinkasittelija.teksti,
                         "yksi kaksi kolme yksi kaksi kolme")
        self.assertEqual(len(self.tekstinkasittelija.lista), 6)
        self.assertEqual(len(self.tekstinkasittelija.sanakirja2.keys()), 3)
        self.assertEqual(len(self.tekstinkasittelija.sanakirja3.keys()), 3)

    def test_oikeinlainen_sanakirja_muodostuu(self):
        sanakirja3 = self.tekstinkasittelija.sanakirja3
        oletettu3 = {}
        oletettu3["yksi"] = [["yksi kaksi kolme", 2]]
        oletettu3["kaksi"] = [["kaksi kolme yksi", 1]]
        oletettu3["kolme"] = [["kolme yksi kaksi", 1]]

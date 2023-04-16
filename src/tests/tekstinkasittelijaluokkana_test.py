import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
import os


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

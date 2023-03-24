import unittest
from tekstinkasittelija_luokkana import Tekstinkasittelija

class TestTekstigeneraattori(unittest.TestCase):
    def setUp(self):
        self.tekstinkasittelija = Tekstinkasittelija("testi.txt")

    def test_alusta_teksti(self):
        self.assertEqual(self.tekstinkasittelija.teksti, "yksi kaksi kolme yksi kaksi kolme")
        self.assertEqual(len(self.lista), 6)
        self.assertEqual(len(self.sanakirja2.keys()), 3)
        self.assertEqual(len(self.sanakirja3.keys()), 3)
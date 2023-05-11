import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
from markovketju import Markovketju
import os

# pyritty varmistumaan että tekstiä voidaan generoida ja että epäsallittua tekstiä ei pääsisi generoitumaan

class Test_Triepuu(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi2.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
        self.testipuu = Triepuu()
        self.testipuu.lisaa_sanat_test(self.tekstinkasittelija.sanakirja3)
        self.ketju = Markovketju(2)

    def test_luo_lause_test_1_aste_toimii(self):
        tulos = self.ketju.luo_lause_test("yksi", self.testipuu, 1, 1)
        self.assertEqual(tulos, "{PARAMETRIT: yksi, 1, 1}:  yksi kaksi kolme ")
        tulos2 = self.ketju.luo_lause_test("yksi", self.testipuu, 5, 1)
        tulos2 = tulos2.split()
        # param lisää 4
        self.assertEqual(len(tulos2), 9)

    def test_luo_lause_test_2_aste_toimii(self):
        aputulos = self.ketju.luo_lause_test("neljä", self.testipuu, 1, 2)
        tulos = ["yksi", "kaksi", "kolme"] in aputulos.split()
        self.assertEqual(tulos, False)
        tulos2 = self.ketju.luo_lause_test("kuusi", self.testipuu, 0, 2)
        self.assertEqual(
            tulos2, "{PARAMETRIT: kuusi, 0, 2}:  kuusi neljä viisi ")
        # param lisää 4, aloitusmonikko on 3
        self.assertEqual(len(tulos2.split()), 7)

    def test_epasallittua_monikkoa_ei_generaatiossa_2_aste(self):
        # testillä pyritään melko isolla otoksella varmistamaan ettei joukkoon päädy
        # sellaista monikkoa, joka ei opetusdatan perusteella olisi mahdollinen, käytössä 2 asteinen ketju.
        lopputulos = True
        i = 0
        matchit = ["yksi neljä viisi", "kaksi neljä viisi", "yksi kolme neljä", "yksi kolme kuusi", "yksi kolme viisi",
                   "kolme neljä kuusi", "yksi kaksi kuusi", "yksi kaksi viisi", "yksi kaksi neljä"]
        tekstit = []
        while i < 50:
            testi_generaatio = self.ketju.luo_lause_test(
                "yksi", self.testipuu, 50, 2)
            i = i + 1
            tekstit.append(testi_generaatio)
        if any([x in testi_generaatio for x in matchit]):
            lopputulos = False
        self.assertEqual(lopputulos, True)

    def test_epasallittua_monikkoa_ei_generaatiossa_1_aste(self):
        # testillä pyritään melko isolla otoksella varmistamaan ettei joukkoon päädy
        # sellaista monikkoa, joka ei opetusdatan perusteella olisi mahdollinen, käytössä 1 asteinen ketju.
        lopputulos = True
        i = 0
        matchit = ["yksi neljä", "kaksi neljä", "kolme viisi", "kuusi viisi", "neljä kuusi", "kolme kaksi"]
        tekstit = []
        while i < 50:
            testi_generaatio = self.ketju.luo_lause_test(
                "yksi", self.testipuu, 50, 1)
            i = i + 1
            tekstit.append(testi_generaatio)
        if any([x in testi_generaatio for x in matchit]):
            lopputulos = False
        self.assertEqual(lopputulos, True)

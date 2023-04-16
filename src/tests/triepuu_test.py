import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os

class Test_Triepuu(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi.txt")
        tiedostonimi2 = (str(os.getcwd()) + "/src/tests/" + "testi2.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
        self.tekstinkasittelija2 = Tekstinkasittelija(tiedostonimi2)
        self.testipuu = Triepuu()
        self.testipuu2 = Triepuu()
        self.testipuu.lisaa_sanat_test(self.tekstinkasittelija.sanakirja3)
        self.testipuu2.lisaa_sanat_test(self.tekstinkasittelija2.sanakirja3)

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

    def test_olemassa_oleva_monikko_löytyy(self):
        haettava2_on = "kaksi kolme"
        haettava3_on = "kaksi kolme yksi"
        haettava2_ei = "kaksi eilöydy"
        haettava3_ei = "yksi kaksi eilöydy"
        testi1 = self.testipuu.hae_monikko(haettava2_on)
        testi2 = self.testipuu.hae_monikko(haettava3_on)
        testi3 = self.testipuu.hae_monikko(haettava2_ei)
        testi4 = self.testipuu.hae_monikko(haettava3_ei)
        self.assertEqual(testi1, "Löytyi monikko: kaksi kolme")
        self.assertEqual(testi2, "Löytyi monikko: kaksi kolme yksi")
        self.assertEqual(testi3, "Ei vastaavaa monikkoa: kaksi eilöydy")
        self.assertEqual(testi4, "Ei vastaavaa monikkoa: yksi kaksi eilöydy")

    def test_annamonikot_test_toimii(self):
        tulos1 = self.testipuu.annamonikot_test("yksi")
        self.assertEqual(len(tulos1), 1)
        self.assertEqual(tulos1[0][1], 2)

        tulos2 = self.testipuu.annamonikot_test("yksi kaksi")
        self.assertEqual(tulos2[0][0], "yksi kaksi kolme")

        tulos3 = self.testipuu.annamonikot_test("yksi yksi")
        self.assertEqual(tulos3, None)


    def test_kertoimet_oikein(self):
        kerroin1 = self.testipuu2.annamonikot_test("yksi kaksi kolme")[0][1]
        self.assertEqual(kerroin1, 3)
        kerroin2 = self.testipuu2.annamonikot_test("kaksi kolme neljä")[0][1]
        self.assertEqual(kerroin2, 1)
        kerroin3 = self.testipuu2.annamonikot_test("neljä viisi kuusi")[0][1]
        self.assertEqual(kerroin3, 2)
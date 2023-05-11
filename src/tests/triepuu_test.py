import unittest
from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os

# Testit perustuvat isolta osin määritettyihin käsinkirjoitettuihin syötteisiin ja hyvin
# yksinkertaiseen opetudataan. Pyritty varmistumaan että hakutoiminnot toimivat ja oikeat asiat
# ilman ylimääräisiä tallentuvat


class Test_Triepuu(unittest.TestCase):
    def setUp(self):
        tiedostonimi = (str(os.getcwd()) + "/src/tests/" + "testi.txt")
        tiedostonimi2 = (str(os.getcwd()) + "/src/tests/" + "testi2.txt")
        self.tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
        self.tekstinkasittelija2 = Tekstinkasittelija(tiedostonimi2)
        self.testipuu = Triepuu()
        self.testipuu2 = Triepuu()
        self.testipuu_kaksikot = Triepuu()
        self.testipuu.lisaa_sanat_test(self.tekstinkasittelija.sanakirja3)
        self.testipuu2.lisaa_sanat_test(self.tekstinkasittelija2.sanakirja3)
        self.testipuu_kaksikot.lisaa_sanat_test(
            self.tekstinkasittelija2.sanakirja2)

    def test_tallennus_onnistunut_ja_solmuilla_on_oikeita_tietoja(self):
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

    def test_puun_alimmalla_tasolla_oikea_maara_lehtia(self):
        self.assertEqual(self.testipuu.get_koko(), 3)
        self.assertEqual(self.testipuu_kaksikot.get_koko(), 7)

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

    def test_monikon_kerroin_kasvaa(self):
        testipuu_uusi = Triepuu()
        testisanakirja = {}
        testisanakirja["t1"] = [('t1 t2', 1)]
        testipuu_uusi.lisaa_sanat_test(testisanakirja)
        testipuu_uusi.lisaa_sanat_test(testisanakirja)
        self.assertEqual(testipuu_uusi.annamonikot_test("t1")[0][1], 2)

    def test_nelikon_tallenus_ja_haku_onnistuu(self):
        testipuu_uusi = Triepuu()
        testisanakirja = {}
        testisanakirja["t1"] = [('t1 t2 t3 t4', 1), ('t1 t22 t33 t44', 1)]
        testipuu_uusi.lisaa_sanat_test(testisanakirja)
        tulos1 = testipuu_uusi.hae_monikko("t1 t2 t3 t4")
        tulos2 = testipuu_uusi.hae_monikko("t1 t4 t3 t2")
        self.assertEqual(tulos1, "Löytyi monikko: t1 t2 t3 t4")
        self.assertEqual(tulos2, "Ei vastaavaa monikkoa: t1 t4 t3 t2")
        tulos3 = testipuu_uusi.annamonikot_test("t1")
        self.assertEqual(tulos3, [('t1 t2 t3 t4', 1), ('t1 t22 t33 t44', 1)])

    def test_seitsikon_tallennus_ja_haku_onnistuu(self):
        testipuu_uusi = Triepuu()
        testisanakirja = {}
        testisanakirja["t1"] = [('t1 t2 t3 t4 t5 t6 t7', 1)]
        testipuu_uusi.lisaa_sanat_test(testisanakirja)
        tulos1 = testipuu_uusi.hae_monikko("t1 t2 t3 t4 t5 t6 t7")
        self.assertEqual(tulos1, "Löytyi monikko: t1 t2 t3 t4 t5 t6 t7")
        tulos2 = testipuu_uusi.annamonikot_test("t1 t2 t3")
        self.assertEqual(tulos2, [('t1 t2 t3 t4 t5 t6 t7', 1)])
        self.assertEqual(
            testipuu_uusi.juuri.lapset["t1"].lapset["t2"].lapset["t3"].sana, "t3")

    def test_ei_asiaankuulumattomia_monikoita_ja_oikeat_maarat_loytyvat(self):
        testisanakirja = {"1": [('1 2 3', 1), ('1 1 2', 2), ('1 1 3', 1)], "2": [
            ('2 1 3', 1)], "3": [('3 2 1', 1)]}
        testipuu_uusi = Triepuu()
        testipuu_uusi.lisaa_sanat_test(testisanakirja)
        tulos1 = testipuu_uusi.annamonikot_test("1")
        tulos2 = testipuu_uusi.annamonikot_test("1 1")
        tulos3 = testipuu_uusi.annamonikot_test("1 3")
        tulos4 = testipuu_uusi.annamonikot_test("1 2 3")
        tulos5 = list(testipuu_uusi.juuri.lapset.keys())
        tulos6 = list(testipuu_uusi.juuri.lapset["1"].lapset.keys())
        tulos6 = list(
            testipuu_uusi.juuri.lapset["1"].lapset["1"].lapset.keys())
        self.assertEqual(tulos1, [('1 2 3', 1), ('1 1 2', 2), ('1 1 3', 1)])
        self.assertEqual(tulos2, [('1 1 2', 2), ('1 1 3', 1)])
        self.assertEqual(tulos3, None)
        self.assertEqual(tulos4, [('1 2 3', 1)])
        self.assertEqual(tulos5, ['1', '2', '3'])
        self.assertEqual(tulos6, ['2', '3'])

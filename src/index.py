from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju
from kayttoliittyma import Kayttoliittyma
import pickle

# materiaalia voi vaihtaa vaihtamalla kommentteja
# suositus on käyttää 3 sanan monikkoja


def main():

    # tässä käytetään valmiiksi esikäsiteltyjä datoja käytön nopeuttamiseksi. Haluttaessa ajaa teksinkäsittelijää
    # siten että koko prosessi menee raakadatasta maaliin asti on käytettävä index_uusidata.py. Index.py hyödyntää
    # valmiiksi käsiteltyä dataa, mutta luo varsinaiset rakenteet kuitenkin aina alusta.

    # sanakirjasta riippuen alustamisen kesto vaihtelee.

    # valittua dataa voidaan vaihtaa kommenttien avulla.
    # valmiiden sanakirjojen _2 tai _3 pääte kertoo monikoiden pituuden.
    # trump_data_* sisältää Donald Trumpin puheita käsiteltyinä
    # kivi_data_* sisältää Aleksis Kiven Seitsemän Veljestä
    # TL_data_* sisältää Suomen Tieliikennelain
    # kurssi_data sisältää vuoden 2023 Tiralabran nettisivuilta kerättyjä ohjeita kurssilaisille.

    polku = (str(os.getcwd()) + "/src/kasiteltydata/")
    # with open(polku + "novellit_data_3.txt", "rb") as sanakirjatiedosto:
    with open(polku + "trump_data_3.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "kivi_data_3.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "TL_data_3.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "kurssi_data_3.txt", "rb") as sanakirjatiedosto:
        testisanat3 = pickle.load(sanakirjatiedosto)

    # with open(polku + "novellit_data_2.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "trump_data_2.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "kivi_data_2.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "TL_data_2.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "kurssi_data_2.txt", "rb") as sanakirjatiedosto:
        # testisanat2 = pickle.load(sanakirjatiedosto)

    testipuu3 = Triepuu()
    # testipuu2 = Triepuu()

    testipuu3.lisaa_sanat_test(testisanat3)
    # testipuu2.lisaa_sanat_test(testisanat2)

    ketju = Markovketju(2)

    # 3 sanan monikot käytössä
    kayttoliittyma3 = Kayttoliittyma(testipuu3, ketju)
    # 2 sanan monikot käytössä
    # kayttoliittyma2 = Kayttoliittyma(testipuu2, ketju)

    kayttoliittyma3.lausegeneraatio()

if __name__ == "__main__":
    main()

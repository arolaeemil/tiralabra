from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju
from kayttoliittyma import Kayttoliittyma
import pickle

# materiaalia voi vaihtaa vaihtamalla kommentteja
# suositus on käyttää 3 sanan monikkoja


def main():
    # tiedostojen haku laitettu siten, että se toimii WSL kanssa. Tällä hetkellä ohjelma pitää ajaa käyttöohjeiden mukaisesti,
    # ei suoraan ajamalla tämä tiedosto vaikkapa Visual Studio Code:lla.

    # kurssimateriaali: aiheet/useita kohtia
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "aiheita.txt")
    #tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "kurssi.txt")

    # osa suomen tieliikkelaista/koko TL-laki
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "osa_tl_laista.txt")
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "Koko_TL_laki.txt")

    # trumpin puhe jossakin
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "puhe.txt")
    # useampi Donal Trumpin puhe tekstinä
    #tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "puhe_monta.txt")

    # seitsemän veljestä, aleksis kivi
    # HIDAS luoda
    #tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "seitseman_veljesta.txt")

    # kokoelma suomalaisia eroottisia novelleja
    ##tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "novellit.txt")

    ##tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
    ##testisanat2 = tekstinkasittelija.sanakirja2
    ##testisanat3 = tekstinkasittelija.sanakirja3


    polku = (str(os.getcwd()) + "/src/kasiteltydata/")
    with open(polku + "novellit_data.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "trump_data.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "kivi_data.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "TL_data.txt", "rb") as sanakirjatiedosto:
    # with open(polku + "kurssi_data.txt", "rb") as sanakirjatiedosto:
        testisanat3 = pickle.load(sanakirjatiedosto)

    ##testipuu2 = Triepuu()
    testipuu3 = Triepuu()

    testipuu3.lisaa_sanat_test(testisanat3)
    ##testipuu2.lisaa_sanat_test(testisanat2)

    ketju = Markovketju()

    # 3 sanan monikot käytössä
    kayttoliittyma3 = Kayttoliittyma(testipuu3, ketju)
    # 2 sanan monikot käytössä
    ##kayttoliittyma2 = Kayttoliittyma(testipuu2, ketju)

    #print(testipuu3.annamonikot_test("you"))
    #print(testisanat3["you"])

    kayttoliittyma3.lausegeneraatio()

    # ei kannata käyttää markovin ketjun pituutta 2 jos monikoiden pituus on vain 2, tälle tosin ei estoa vielä.
    # kayttoliittyma2.lausegeneraatio()


if __name__ == "__main__":
    main()

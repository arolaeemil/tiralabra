from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju
from kayttoliittyma import Kayttoliittyma

# materiaalia voi vaihtaa vaihtamalla kommentteja
# suositus on käyttää 3 sanan monikkoja


def main():
    # kurssimateriaali: aiheet
    # tiedostonimi = (str(os.getcwd()) + "/src/" + "pitkateksti.txt")

    # osa suomen tieliikkelaista
    # tiedostonimi = (str(os.getcwd()) + "/src/" + "osa_tl_laista.txt")

    # trumpin puhe jossakin
    tiedostonimi = (str(os.getcwd()) + "/src/" + "puhe.txt")

    tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
    testisanat2 = tekstinkasittelija.sanakirja2
    testisanat3 = tekstinkasittelija.sanakirja3
    testipuu2 = Triepuu()
    testipuu3 = Triepuu()

    testipuu3.lisaa_sanat_test(testisanat3)
    testipuu2.lisaa_sanat_test(testisanat2)

    ketju = Markovketju()

    # 3 sanan monikot käytössä
    kayttoliittyma3 = Kayttoliittyma(testipuu3, ketju)
    # 2 sanan monikot käytössä
    kayttoliittyma2 = Kayttoliittyma(testipuu2, ketju)

    kayttoliittyma3.lausegeneraatio()
    # ei kannata käyttää markovin ketjun pituutta 2 jos monikoiden pituus on vain 2, tälle tosin ei estoa vielä.
    # kayttoliittyma2.lausegeneraatio()


if __name__ == "__main__":
    main()

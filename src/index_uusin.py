from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju
from kayttoliittyma import Kayttoliittyma

def main():
    #tiedostonimi = (str(os.getcwd()) + "/src/" + "pitkateksti.txt")
    tiedostonimi = (str(os.getcwd()) + "/src/" + "pitkateksti2.txt")
    tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
    testisanat2 = tekstinkasittelija.sanakirja2
    testisanat3 = tekstinkasittelija.sanakirja3
    testipuu2 = Triepuu()
    testipuu3 = Triepuu()

    testipuu3.lisaa_sanat_test(testisanat3)
    testipuu2.lisaa_sanat_test(testisanat2)

    ketju = Markovketju(1)

    #3 sanan monikot käytössä
    kayttoliittyma3 = Kayttoliittyma(testipuu3, ketju)
    #2 sanan monikot käytössä
    kayttoliittyma2 = Kayttoliittyma(testipuu2, ketju)

    kayttoliittyma3.lausegeneraatio()
    #kayttoliittyma2.lausegeneraatio()


if __name__ == "__main__":
    main()
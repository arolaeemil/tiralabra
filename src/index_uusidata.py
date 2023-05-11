from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju
from kayttoliittyma import Kayttoliittyma
import pickle

# materiaalia voi vaihtaa vaihtamalla kommentteja
# tämän avulla on helpointa käsitellä ja saattaa käyttöön kokonaan uusi materiaali. Haluttassa lisätä
# dataa tarvitsee lisätä tekstitiedosto opetusdatakansioon ja vaihtaa tiedoston nimeä koskevat tiedot
# syntaksin mukaisesti viittaamaan lisättyyn opetusdataan.
# voidaan tehdä myös valinnat sen suhteen käytetäänkö 2 vai 3 sanan monikoita. Suositellaan 3 sanan
# monikoita, mutta kaksikoita varten jätetty syntaksi kommentoituna olemassaolemaan.


def main():

    # kurssimateriaali: aiheet/useita kohtia
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "aiheita.txt")
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "kurssi.txt")

    # osa suomen tieliikkelaista/koko TL-laki
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "osa_tl_laista.txt")
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "Koko_TL_laki.txt")

    # trumpin puhe jossakin
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "puhe.txt")
    # useampi Donal Trumpin puhe tekstinä
    tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "puhe_monta.txt")

    # seitsemän veljestä, aleksis kivi
    # HIDAS luoda
    #tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "seitseman_veljesta.txt")

    # kokoelma suomalaisia eroottisia novelleja
    # tiedostonimi = (str(os.getcwd()) + "/src/opetusdata/" + "novellit.txt")

    tekstinkasittelija = Tekstinkasittelija(tiedostonimi)
    # testisanat2 = tekstinkasittelija.sanakirja2
    testisanat3 = tekstinkasittelija.sanakirja3

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

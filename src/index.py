from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju

#testausta on aika paljon tässä kommentoituna, anteeksi siitä, on väliaikaista
#pisimmällä olevan toiminnallisuuden testausta

def main():
    tiedostonimi = (str(os.getcwd()) + "/src/" + "pitkateksti.txt")
    tekstinkasittelija = Tekstinkasittelija(tiedostonimi)

    testisanat2 = tekstinkasittelija.sanakirja2
    testisanat3 = tekstinkasittelija.sanakirja3
    testipuu2 = Triepuu()
    testipuu3 = Triepuu()
    #print("#listaus alkaa")
    #for sana in testisanat3:
        #print(sana, testisanat3[sana])
    #print("#listaus loppuu")
    #testipuu2.lisaa_sanat_test(testisanat2)
    testipuu3.lisaa_sanat_test(testisanat3)

    #print(testipuu2.get_koko())
    #print(testipuu3.get_koko())

    #haettava2 = "tämä on"
    #haettava3 = "tämä on testi"

    #haettava2_ei = "tämä eilöydy"
    #haettava3_ei = "tämä on eilöydy"

    #testipuu2.hae_monikko(haettava2)
    #testipuu3.hae_monikko(haettava3)

    #testipuu2.hae_monikko(haettava2_ei)
    #testipuu3.hae_monikko(haettava3_ei)

    #print(tekstinkasittelija.sanakirja2.keys())

    #syote1 = "päästään jos data"
    #print(testipuu3.anna_monikko_sanoille(syote1))
    #syote2 = "toisen asteen markovin"
    #print(testipuu3.anna_monikko_sanoille(syote2))

    #syote3 = "jos"
    #print(testipuu3.anna_mahdolliset_monikot_3(syote3))
    #print(testipuu3.anna_mahdolliset_monikot_2(syote3))

    ketju = Markovketju(1)
    #ketjutesti = testipuu3.anna_mahdolliset_monikot_2(syote3)
    #print(ketju.paata_seuraavat_sanat(ketjutesti))

    print(ketju.luo_lause_1_aste("jos",testipuu3,20))

    ketju3 = Markovketju(1)
    #ketjutesti3 = testipuu3.anna_mahdolliset_monikot_2(syote3)
    #print(ketju3.paata_seuraavat_sanat(ketjutesti3))

    print(ketju3.luo_lause_2_aste("jos",testipuu3,20))

if __name__ == "__main__":
    main()
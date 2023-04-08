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

    testipuu3.lisaa_sanat_test(testisanat3)

    ketju3 = Markovketju(1)

    #print(ketju3.luo_lause_2_aste("jos",testipuu3,20))
    #print(ketju3.luo_lause_1_aste("jos",testipuu3,20))

    #print(ketju3.luo_lause_test("jos tämä",testipuu3,20))
    #print("testi1:")
    #print(testipuu3.annamonikot_test("itse"))
    #print("testi2:")
    #print(testipuu3.annamonikot_test("itse tai"))
    #print("testi3:")
    #print(testipuu3.annamonikot_test("itse tai voit"))

    print(ketju3.luo_lause_test("algoritmi",testipuu3,20,2))
    print(ketju3.luo_lause_test("algoritmi",testipuu3,20,1))

    print(ketju3.luo_lause_test("lisko",testipuu3,20,2))
    print(ketju3.luo_lause_test("lisko spock",testipuu3,20,1))

    print(ketju3.luo_lause_test("myös",testipuu3,20,2))
    print(ketju3.luo_lause_test("myös",testipuu3,20,1))

if __name__ == "__main__":
    main()
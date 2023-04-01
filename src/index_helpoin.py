from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os

#testausta on aika paljon tässä kommentoituna, anteeksi siitä, on väliaikaista

def main():
    #tiedostonimi = "helppotesti.txt"
    #tiedostonimi = "/home/eemil/Desktop/tiralabra/tiralabra/src/helppotesti.txt"
    tiedostonimi = (str(os.getcwd()) + "/src/" + "helppotesti.txt")
    #tiedostonimi = (str(os.getcwd()) + "/src/" + "testiteksti.txt")
    tekstinkasittelija = Tekstinkasittelija(tiedostonimi)

    testisanat2 = tekstinkasittelija.sanakirja2
    testisanat3 = tekstinkasittelija.sanakirja3
    testipuu2 = Triepuu()
    testipuu3 = Triepuu()
    #testipuu2.lisaa_sanat(testisanat2)
    #testipuu3.lisaa_sanat(testisanat3)
    #siistimpi metodi
    #print(testisanat2)
    print("#listaus alkaa")
    for sana in testisanat3:
        print(sana, testisanat3[sana])
    print("#listaus loppuu")
    #testipuu2.lisaa_sanat_test(testisanat2)
    testipuu3.lisaa_sanat_test(testisanat3)

    #print(testipuu2.get_koko())
    print(testipuu3.get_koko())

    haettava2 = "tämä on"
    haettava3 = "tämä on testi"

    haettava2_ei = "tämä eilöydy"
    haettava3_ei = "tämä on eilöydy"

    #testipuu2.hae_monikko(haettava2)
    testipuu3.hae_monikko(haettava3)

    #testipuu2.hae_monikko(haettava2_ei)
    testipuu3.hae_monikko(haettava3_ei)

    #print(tekstinkasittelija.sanakirja2.keys())

    syote1 = "tämä on testi"
    print(testipuu3.anna_monikko_sanoille(syote1))
    syote2 = "testi tämä on"
    print(testipuu3.anna_monikko_sanoille(syote2))

    syote3 = "tämä"
    print(testipuu3.anna_mahdolliset_monikot_3(syote3))
    print(testipuu3.anna_mahdolliset_monikot_2(syote3))

if __name__ == "__main__":
    main()
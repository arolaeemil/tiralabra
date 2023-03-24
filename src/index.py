from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os

def main():
    #tiedostonimi = "helppotesti.txt"
    #tiedostonimi = "/home/eemil/Desktop/tiralabra/tiralabra/src/helppotesti.txt"
    tiedostonimi = (str(os.getcwd()) + "/src/" + "helppotesti.txt")
    #tiedostonimi = "testiteksti.txt"
    tekstinkasittelija = Tekstinkasittelija(tiedostonimi)

    #tekstinkasittelija.suorita_tarkastus()
    
    #print(tekstinkasittelija.teksti)
    #print(tekstinkasittelija.lista)
    #print(tekstinkasittelija.parilista)
    #print(tekstinkasittelija.kolmikkolista)
    #print(tekstinkasittelija.sanakirja2)
    #print(tekstinkasittelija.sanakirja3)

    testisanat2 = tekstinkasittelija.sanakirja2
    testisanat3 = tekstinkasittelija.sanakirja3
    testipuu2 = Triepuu()
    testipuu3 = Triepuu()
    testipuu2.lisaa_sanat(testisanat2)
    testipuu3.lisaa_sanat(testisanat3)
    #print(testipuu.juuri.get_lapsi("tämä").get_lapsi("on"))

    #testipuu2.tarkista_puu2()
    #testipuu3.tarkista_puu3()

    print(testipuu3.juuri.get_lapsi("tämä").get_lapsi("on").get_lapsi("testi"))
    print(testipuu3.juuri.get_lapsi("tämä").get_lapsi("on").get_lapsi("testi2").lehti)

    print(testipuu3.juuri.get_lapsi("toistan").get_lapsi("tämä").get_lapsi("on"))
    print(testipuu3.juuri.get_lapsi("toistan").get_lapsi("tämä").get_lapsi("on").lehti)

    print(testipuu3.juuri.get_lapsi("testi2").get_lapsi("tämä"))
    print(testipuu3.juuri.get_lapsi("testi2").get_lapsi("tämä").lehti)

    print("################")

    x = testipuu3.hae_puusta("tämä")
    print(x.lapset.keys())
    x = testipuu3.hae_puusta("on",x)
    print(x.lapset.keys())
    print(testipuu3.hae_puusta("testi",x))

    print("################")
    
    y = testipuu3.hae_puusta("on")
    print(y.lapset.keys())
    y = testipuu3.hae_puusta("testi",y)
    print(y.lapset.keys())
    print(testipuu3.hae_puusta("toistan",y))

    print("################")

    print(testipuu2.get_koko())
    print(testipuu3.get_koko())

    print(tekstinkasittelija.sanakirja2.keys())

if __name__ == "__main__":
    main()
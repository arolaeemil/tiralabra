from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju


class Kayttoliittyma:

    def __init__(self, triepuu, markovketju):
        self.triepuu = triepuu
        self.markovketju = markovketju

    def lausegeneraatio(self):
        # tarvitaan listaus olemassa olevista sanoista, olematon sanaa johtaa virheeseen
        print("sallitut aloitussanat: ")
        sallitut_sanat = self.sallitut_aloitussanat()
        print("lausegeneraatio alkaa, tyhjä merkkijono lopettaa")
        # generoidaan tekstiä loopissa
        while True:
            aloitussana = str(input("Anna aloitussana: "))
            aloitussana = aloitussana.lower()
            if aloitussana == "":
                break
            if len(aloitussana.split()) > 1:
                print("Anna vain yksi sana")
                continue
            if aloitussana not in sallitut_sanat:
                print("Aloitussanaa ei löydy opetusdatasta. Anna uusi sana.")
                continue
            try:
                sanamaara = int(
                    input("Anna lauseen sanamäärä (ensimmäisen monikon lisäksi, 0-100): "))
            except:
                print("epäkelpo muoto sanamäärälle, käytetään oletusarvoa 10")
                sanamaara = 10
            if sanamaara > 100 or sanamaara <= 0:
                print("epäkelpo sanamäärä, käytetään oletusarvoa 10")
                sanamaara = 10
            try:
                aste = int(input("Anna markovin ketjun aste (1 tai 2): "))
            except:
                print("epäkelpo muoto asteelle, käytetään oletusarvoa 2")
                sanamaara = 10
            if aste not in [1, 2]:
                print("epäkelpo aste, käytetään oletusarvoa 2")
                aste = 2
            print(self.markovketju.luo_lause_test(
                aloitussana, self.triepuu, sanamaara, aste))

    def sallitut_aloitussanat(self):
        # listataan juuren lapset
        listaus = self.triepuu.juuri.lapset.keys()
        listaus = sorted(listaus)
        apulistaus = []
        for avain in listaus:
            apulistaus.append(avain)
            if len(apulistaus) > 10:
                print(apulistaus)
                apulistaus = []
        print(apulistaus)
        return listaus
        # print(listaus)

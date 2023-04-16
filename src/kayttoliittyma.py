from tekstinkasittelijaluokkana import Tekstinkasittelija
from triepuu import Triepuu
import os
from markovketju import Markovketju

class Kayttoliittyma:

    def __init__(self, triepuu, markovketju):
        self.triepuu = triepuu
        self.markovketju = markovketju

    def lausegeneraatio(self):
        print("sallitut aloitussanat: ")
        self.sallitut_aloitussanat()
        print("lausegeneraatio alkaa, tyhjä merkkijono lopettaa")
        while True:
            aloitussana = str(input("Anna aloitussana: "))
            if aloitussana == "":
                break
            if len(aloitussana.split()) > 1:
                print("anna vain yksi sana")
                continue
            try:
                sanamaara = int(input("Anna lauseen sanamäärä (ensimmäisen monikon lisäksi, 0-100): "))
            except:
                break
            if sanamaara > 100 or sanamaara <= 0:
                print("epäkelpo sanamäärä, käytetään defaulttia 10")
                sanamaara = 10
            try:
                aste = int(input("Anna markovin ketjun aste (1 tai 2): "))
            except:
                break
            if aste not in [1,2]:
                print("epäkelpo aste, käytetään defaulttia 2")
                aste = 2
            print(self.markovketju.luo_lause_test(aloitussana,self.triepuu,sanamaara,aste))
            
    def sallitut_aloitussanat(self):
        listaus = self.triepuu.juuri.lapset.keys()
        listaus = sorted(listaus)
        apulistaus = []
        for avain in listaus:
            apulistaus.append(avain)
            if len(apulistaus) > 10:
                print(apulistaus)
                apulistaus = []
        print(apulistaus)
        #print(listaus)
 
    
        
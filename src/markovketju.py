from random import *
from triepuu import Triepuu

class Markovketju:

    def __init__(self, aste=1):
        self.aste = aste
        self.lause = ""

    def paata_seuraavat_sanat(self,monikkolista):
        #print(monikkolista)
        if len(monikkolista) == 1:
            val_monikko = monikkolista[0][0]
            return val_monikko
        yhteisluku = 0
        arvontalista = []
        arvontalista.append(0)
        for monikko in monikkolista:
            yhteisluku = yhteisluku + monikko[1]
            arvontalista.append(yhteisluku)
        arpa = randint(0,yhteisluku)
        #print(yhteisluku)
        #print(arvontalista)
        #print(arpa)
        i = 0
        while i <= len(arvontalista):
            if arpa <= arvontalista[1]:
                valittu = i
                break
            if arpa > arvontalista[len(arvontalista)-1]:
                valittu = i
                break
            if arpa <= arvontalista[i+1] and arpa > arvontalista[i-1] and i != 0:
                valittu = i
                break
            i = i + 1
        #print(valittu)
        val_monikko = monikkolista[valittu][0]
        return val_monikko
    
    def luo_lause_1_aste(self,alkusana,triepuu:Triepuu, sanamaara):
        lause = "TEST:"
        monikkolista = triepuu.anna_mahdolliset_monikot_2(alkusana)
        osa_lause = self.paata_seuraavat_sanat(monikkolista)
        lause = lause + " " + osa_lause
        i = 0
        osa_lause = osa_lause.split()
        seur_sana = osa_lause[1]
        while i < sanamaara:
            monikkolista = triepuu.anna_mahdolliset_monikot_2(seur_sana)
            lisa_lause = self.paata_seuraavat_sanat(monikkolista)
            lisa_lause = lisa_lause.split()
            lisa_lause = lisa_lause[1:]
            osa_lause = " "
            for sana in lisa_lause:
                osa_lause = osa_lause + str(sana)
                seur_sana = str(sana)
            lause = lause + osa_lause
            i = i + 1
        return lause
    
    def luo_lause_2_aste(self,alkusana,triepuu:Triepuu, sanamaara):
        lause = "TEST:"
        monikkolista = triepuu.anna_mahdolliset_monikot_3(alkusana)
        osa_lause = self.paata_seuraavat_sanat(monikkolista)
        lause = lause + " " + osa_lause + " "
        i = 0
        osa_lause = osa_lause.split()
        seur_sanat = osa_lause[1] + " " + osa_lause[2]
        while i < sanamaara:
            monikkolista = triepuu.anna_mahdolliset_monikot_2_sanaa(seur_sanat)
            lisa_lause = self.paata_seuraavat_sanat(monikkolista)
            alkuper = lisa_lause
            #print(alkuper)
            alk_len = len(alkuper.split())
            lisa_lause = lisa_lause.split()
            lisa_lause = lisa_lause[2:]
            osa_lause = ""
            seur_sana = ""
            for sana in lisa_lause:
                osa_lause = osa_lause + str(sana) + " "
                #seur_sana = seur_sana + " " + str(sana)
            #osa_lause = osa_lause[0:(len(osa_lause)-1)]
            lause = lause + osa_lause
            seur_sanat = alkuper.split()[alk_len-2] + " " + alkuper.split()[alk_len-1]
            #print(seur_sanat)
            i = i + 1
        return lause
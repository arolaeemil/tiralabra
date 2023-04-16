from random import *
from triepuu import Triepuu

class Markovketju:

    def __init__(self):
        self.lause = ""

    def paata_seuraavat_sanat(self,monikkolista):
        #arpoo annetusta monikkolistasta seuraavan monikon esiintymisenmäärien perusteella
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

    def luo_lause_test(self,alkusana,triepuu:Triepuu, sanamaara, aste):
        #luo lauseen, ottaa huomioon sanamaaran verran sanoja.
        #ensimmäinen 3 sanan monikko otetaan suoraan alkusanan perusteella, loput sanat
        #lisätään käyttäen asteen määrittämää markovketjun astetta
        #lause = "TEST:"
        lause = "{PARAMETRIT: " + alkusana + ", " + str(sanamaara) + ", " + str(aste) + "}: "
        monikkolista = triepuu.annamonikot_test(alkusana)
        osa_lause = self.paata_seuraavat_sanat(monikkolista)
        lause = lause + " " + osa_lause + " "
        i = 0
        osa_lause = osa_lause.split()
        if aste == 2:
            #seur_sanat = osa_lause[1] + " " + osa_lause[2]
            seur_sanat = osa_lause[-2] + " " + osa_lause[-1]
            #laskuri = sanamaara
            #print(seur_sanat)
        if aste == 1:
            #seur_sanat = osa_lause[2]
            seur_sanat = osa_lause[-1]
            #jos käytetään 3 sanan monikoita lisätään 2 sanaa edellisen perusteella asteella 1.
            #laskuri = int(sanamaara/2)
            #korjaus edelliseen kun käytetään 2 sanan monikoita
            #if len(monikkolista[0][0].split()) == 2:
                #laskuri = sanamaara
            #print(seur_sanat)
        #while i < laskuri:
        while True:
            if len(lause.split()) >= sanamaara + 4:
                break
            monikkolista = triepuu.annamonikot_test(seur_sanat)
            if monikkolista == None:
                print("Keskeytyi, ei tiedossa seuraajia sanalle.")
                return lause
            #print("luo_lause_test_116")
            #print(monikkolista)
            lisa_lause = self.paata_seuraavat_sanat(monikkolista)
            alkuper = lisa_lause
            #print(alkuper)
            alk_len = len(alkuper.split())
            lisa_lause = lisa_lause.split()
            if aste == 2:
                lisa_lause = lisa_lause[2:]
                #lisa_lause = lisa_lause[1:]
                #print(lisa_lause)
            if aste == 1:
                lisa_lause = lisa_lause[1:]
                #lisa_lause = lisa_lause[2:]
                #print(lisa_lause)
            osa_lause = ""
            for sana in lisa_lause:
                osa_lause = osa_lause + str(sana) + " "
            lause = lause + osa_lause
            if aste == 2:
                seur_sanat = alkuper.split()[alk_len-2] + " " + alkuper.split()[alk_len-1]
                #print(seur_sanat)
            if aste == 1:
                seur_sanat = alkuper.split()[-1]
                #print(seur_sanat)
            i = i + 1        
        return lause
from random import *
from triepuu import Triepuu


class Markovketju:

    def __init__(self, aste: int):
        self.lause = ""
        self.aste = aste

    def paata_seuraavat_sanat(self, monikkolista):
        # arpoo annetusta monikkolistasta seuraavan monikon esiintymisenmäärien perusteella,
        # jakaa "arpalippuja" frekvenssin perusteella.
        if len(monikkolista) == 1:
            val_monikko = monikkolista[0][0]
            return val_monikko
        yhteisluku = 0
        arvontalista = []
        arvontalista.append(0)
        for monikko in monikkolista:
            yhteisluku = yhteisluku + monikko[1]
            arvontalista.append(yhteisluku)
        arpa = randint(0, yhteisluku)
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
        val_monikko = monikkolista[valittu][0]
        return val_monikko

    def luo_lause_test(self, alkusana, triepuu: Triepuu, sanamaara, aste):
        # luo lauseen, ottaa huomioon sanamaaran verran sanoja.
        # ensimmäinen 3 sanan monikko otetaan suoraan alkusanan perusteella, loput sanat
        # lisätään käyttäen asteen määrittämää markovketjun astetta
        lause = "{PARAMETRIT: " + alkusana + ", " + \
            str(sanamaara) + ", " + str(aste) + "}: "
        monikkolista = triepuu.annamonikot_test(alkusana)
        osa_lause = self.paata_seuraavat_sanat(monikkolista)
        lause = lause + " " + osa_lause + " "
        osa_lause = osa_lause.split()
        i = 0
        seur_sanat = ""
        for i in range(aste,0,-1):
            seur_sanat = seur_sanat + osa_lause[-i]
            seur_sanat = seur_sanat + " "
        seur_sanat = seur_sanat[0:(len(seur_sanat)-1)]
        laskuri = 0
        while True:
            # jos jostakin syystä puuhun olisi päätynyt jotakin outoa ja muusta syystä ketju päättäisi loopata jonkin
            # virheen johdosta jota testeissä ei havaita on varatoiminto asetettu ja yritetään jatkaa lauseen generointia
            # ilmoituksen jälkeen
            if laskuri > 100:
                print("virheestä palautuminen! Arvonta vaikutti loopanneen")
                seur_sanat = seur_sanat.split()[-1]
                laskuri = 0
            # tapa seurata lauseen edistymista eri ketjun asteilla
            if len(lause.split()) >= sanamaara + 4:
                break
            monikkolista = triepuu.annamonikot_test(seur_sanat)
            if monikkolista == None:
                print("Keskeytyi, ei tiedossa seuraajia sanalle.")
                return lause
            lisa_lause = self.paata_seuraavat_sanat(monikkolista)
            alkuper = lisa_lause
            alk_len = len(alkuper.split())
            lisa_lause = lisa_lause.split()
            lisa_lause = lisa_lause[aste:]
            osa_lause = ""
            for sana in lisa_lause:
                osa_lause = osa_lause + str(sana) + " "
            lause = lause + osa_lause            
            seur_sanat = ""
            for i in range(aste,0,-1):
                seur_sanat = seur_sanat + alkuper.split()[alk_len-i]
                seur_sanat = seur_sanat + " "
            seur_sanat = seur_sanat[0:(len(seur_sanat)-1)]
            laskuri = laskuri + 1
        return lause
    
    def get_aste(self):
        return self.aste

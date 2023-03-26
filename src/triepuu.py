from triesolmu import Triesolmu

class Triepuu:

    def __init__(self):
        #puu alkaa juuresta, jolla ei ole sanaa tallennettuna.
        #puulla on myös sen kokoa kuvaava parametri.
        self.juuri = Triesolmu("")
        self.koko = 0

    def lisaa_sanat(self, sanakirja):
        avaimet = sanakirja.keys()
        tama_solmu = self.juuri
        for avain in avaimet:
            self.juuri.lisaa_lapsi(avain, Triesolmu(avain))
            tama_solmu = self.juuri.get_lapsi(avain)
            #print(sanakirja[avain])
            tama_solmu_alku = tama_solmu
            for perakkaiset in sanakirja[avain]:
                sanat = perakkaiset[0].split()
                tama_solmu  = tama_solmu_alku
                #print(sanat)
                for sana in sanat[1:]:
                    tama_solmu.lisaa_lapsi(sana, Triesolmu(sana))
                    tama_solmu  = tama_solmu.get_lapsi(sana)
                tama_solmu.lehti = True
                self.koko = self.koko + 1
    
    #ehkä se parempi metodi?
    def lisaa_sanat_test(self,sanakirja):
        avaimet = sanakirja.keys()
        for avain in avaimet:
            tama_solmu = self.juuri
            sanajonot = sanakirja[avain]
            indeksi = 0
            #yhtä avainta voi vastata lista monkoita. Monikoissa on monikon sanat
            #listan ensimmäisessä alkiossa ja monikon esiintymisenkerrat toisessa.
            for monikko in sanajonot:
                #print(monikko)
                sanajono = self.tee_sanoiksi(sanajonot,indeksi)
                indeksi = indeksi + 1
                montako_sanaa = len(sanajono)
                tama_solmu.lisaa_lapsi(avain,Triesolmu(avain))
                tama_solmu = tama_solmu.get_lapsi(avain)
                #i = 1, sillä sanajonon ensimmäinen sana on avain itse
                i = 1
                while i < montako_sanaa:
                    tama_solmu.lisaa_lapsi(sanajono[i],Triesolmu(sanajono[i]))
                    tama_solmu = tama_solmu.get_lapsi(sanajono[i])
                    i = i + 1
                #ollaanko ensimmäistä kertaa "polun" päässä
                if tama_solmu.lehti == False:
                    self.koko = self.koko + 1
                tama_solmu.lehti = True

    def tee_sanoiksi(self, sanajono, indeksi):
        lista = []
        stringi = sanajono[indeksi][0]
        #print(stringi)
        stringi = stringi.split()
        for alkio in stringi:
            lista.append(alkio)
        return lista

    def hae_puusta(self, avain, solmu=None):
        #ei vielä tehty oikeasti
        if solmu == None:
            solmu = self.juuri
        return solmu.get_lapsi(avain)

    def hae_monikko(self, monikko):
        #metodi kokeilemaan onko sanamonikko puussa
        muodostettu = ""
        tama_solmu = self.juuri
        monikkosplit = monikko.split()
        for sana in monikkosplit:
            if tama_solmu.onko_vastaava_lapsi(sana):
                muodostettu = muodostettu + " " + sana
                tama_solmu = tama_solmu.lapset[sana]
            else:
                print("Ei vastaavaa monikkoa: " + monikko)
                return "Ei vastaavaa monikkoa: " + monikko
        muodostettu = muodostettu[1:]
        print("Löytyi monikko: " + muodostettu)
        return "Löytyi monikko: " + muodostettu

    def etsi_solmu(self, stringi):
        #ei vielä tehty oikeasti, voi olla melko turha
        if len(stringi) == 0:
            return self.juuri     
    
    def on_tyhja(self):
        return self.koko == 0

    
    def get_koko(self):
        return self.koko
    

    #hyvinkin mahdollisesti turhaa
    
    def tarkista_puu2(self):
        #tarkastusmetodi puulle jossa 2 sanan monikoita, tuskin tulee enää käyttöön
        avaimet = self.juuri.lapset.keys()
        solmu = self.juuri
        print(avaimet)
        for avain in avaimet:
            print(solmu.lapset[avain])
    
    def tarkista_puu3(self):
        #tarkastusmetodi puulle jossa 3 sanan monikoita, tuskin tulee enää käyttöön
        avaimet = self.juuri.lapset.keys()
        solmu = self.juuri
        print(avaimet)
        for avain in avaimet:
            #print(solmu.lapset[avain])
            vanha_solmu = solmu
            solmu = solmu.get_lapsi(avain)
            avaimet2 = solmu.lapset.keys()
            for avain2 in avaimet2:
                print(solmu.lapset[avain2])
            solmu = vanha_solmu
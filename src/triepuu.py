from triesolmu import Triesolmu

class Triepuu:

    def __init__(self):
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

    def etsi_solmu(self, stringi):
        if len(stringi) == 0:
            return self.juuri     
    
    def on_tyhja(self):
        return self.koko == 0
    
    def tarkista_puu2(self):
        avaimet = self.juuri.lapset.keys()
        solmu = self.juuri
        print(avaimet)
        for avain in avaimet:
            print(solmu.lapset[avain])
    
    def tarkista_puu3(self):
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

    
    def hae_puusta(self, avain, solmu=None):
        if solmu == None:
            solmu = self.juuri
        return solmu.get_lapsi(avain)
    
    def get_koko(self):
        return self.koko
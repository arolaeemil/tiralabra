class Triesolmu:

    def __init__(self, sana = None):
        #solmussa tieto siitä mikä sana siihen tulee, solmun lapset sanakirjana
        # ja tieto siitä onko solmu lehti
        self.sana = sana
        self.kerroin = 0
        self.lapset = {}
        self.lehti = False

    def on_lehti(self):
        return self.lehti
    
    def lapsimaara(self):
        laskuri = 0
        for avain in self.lapset.keys():
            laskuri += 1
        return laskuri    

    def __str__(self):
        if self.sana != None:
            return f'({self.sana}, {self.lapset.keys()}. {self.lehti})'
        else:
            return "on juuri"
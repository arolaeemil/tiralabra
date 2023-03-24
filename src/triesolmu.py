class Triesolmu:

    def __init__(self, sana = None):
        self.sana = sana
        self.lapset = {}
        self.lehti = False

    def on_lehti(self):
        return self.lehti
    
    def lapsimaara(self):
        laskuri = 0
        for avain in self.lapset.keys():
            laskuri += 1
        return laskuri
    
    def onko_vastaava_lapsi(self, stringi):
        if stringi in self.lapset.keys():
            return True
        else:
            return False
        
    def get_lapsi(self, stringi):
        if self.onko_vastaava_lapsi(stringi):
            return self.lapset[stringi]
        else:
            return
            raise ValueError(f'Ei vastaavaa lasta sanalle {stringi}')

    def lisaa_lapsi(self, stringi, lapsisolmu):
        if not self.onko_vastaava_lapsi(stringi):
            self.lapset[stringi] = lapsisolmu
        else:
            return
            raise ValueError(f'On jo vastaava lapsi sanalle {stringi}')

    def __str__(self):
        if self.sana != None:
            return f'({self.sana}, {self.lapset.keys()})'
        else:
            return "on juuri"
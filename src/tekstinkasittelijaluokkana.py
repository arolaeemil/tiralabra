# tekstinkäsittelijä
class Tekstinkasittelija:

    def __init__(self, tiedostonimi):
        # kerättyjä asioita monenlaisia, sillä ei vielä varmuutta mikä on paras
        # tapa kerätä monikot siten että kaikki tiedot saadaan hyvin talteen
        # ja helposti muutettua puuksi
        self.tiedostonimi = tiedostonimi
        self.sanakirja2 = {}
        self.sanakirja3 = {}
        self.parilista = []
        self.kolmikkolista = []
        self.teksti = ""
        self.lista = []
        self.alusta_teksti()
        self.muodosta_lista()

    def alusta_teksti(self):
        # muokataan teksti järkevään muotoon käsiteltäväksi
        with open(self.tiedostonimi, encoding="utf8") as tiedosto:
            self.rivit = tiedosto.readlines()

        # eri korvaajavaihtoehtoja jätetty tahallaan esimerkeiksi. Jää käyttäjän harteilla tehdä muutoksia
        # haluttaessa vaihtaa sitä millä merkeillä on väliä. Suositus jätetty käytössä olevaksi.

        # korvaajat = [('/', ''), ('Ã¤', 'ä'), ('Ã¶', 'ö'), ('Ã¼', 'ü'), ('.', ''), (',', ''), ('\n', ' ')]

        # pisteet ja pilkut mukana
        # korvaajat = [('/', ''), ('Ã¤', 'ä'), ('Ã¶', 'ö'), ('Ã¼', 'ü'), ('\n', ' ')]

        # piste mukana, pilkku ei, lainausmerkit pois
        korvaajat = [('/', ''), ('Ã¤', 'ä'), ('Ã¶', 'ö'),
                     ('Ã¼', 'ü'), ('\n', ' '), (',', ''), ('“', ''), ('”', ''), ('"', ''), ('’', '')]

        # piste ja pilkku mukana, lainausmerkit pois
        # korvaajat = [('/', ''), ('Ã¤', 'ä'), ('Ã¶', 'ö'),
        # ('Ã¼', 'ü'), ('\n', ' '), ('“', ''), ('”', ''), ('"', '')]

        for rivi in self.rivit:
            for char, korvaaja in korvaajat:
                if char in rivi:
                    rivi = rivi.replace(char, korvaaja)
            self.teksti = self.teksti + rivi
        self.teksti = self.teksti.lower()
        self.lista = self.teksti.split()

    def on_jo_mukana_2(self, sana1, sana2):
        # onko 2 sanan monikko jo mukana
        for alkio in self.parilista:
            if sana1 == alkio[0] and sana2 == alkio[1]:
                alkio[2] = alkio[2] + 1
        return

    def on_jo_mukana_3(self, sana1, sana2, sana3):
        # onko 3 sanan monikko jo mukana
        for alkio in self.kolmikkolista:
            if sana1 == alkio[0] and sana2 == alkio[1] and sana3 == alkio[2]:
                alkio[3] = alkio[3] + 1
        return

    def onko_kirjassa(self, sana, sanajono, kirja):
        # tatkastetaan onko jo listattu sanakirjaan
        if sana not in kirja.keys():
            return False
        kirjaukset = kirja[sana]
        for kirjaus in kirjaukset:
            if sanajono == kirjaus[0]:
                return True
        else:
            return False

    def lisaa_kirjaukseen(self, sana, sanajono, sanakirja):
        # lisataan esiintymiskerta monikolle
        kohta = sanakirja[sana]
        for apukohta in kohta:
            if apukohta[0] == sanajono:
                apukohta[1] = apukohta[1] + 1
        return

    def printtaa_kirja(self, sanakirja):
        # prittausmetodi tarkastusta varten
        laskuri = 0
        for sana in sanakirja.keys():
            print(sana + ": ")
            for kirjaus in sanakirja[sana]:
                print("  " + kirjaus[0] + ", " + str(kirjaus[1]))
                laskuri = laskuri + 1
        print("monikoita yhteensä: " + str(laskuri))
        return

    def muodosta_lista(self):
        # haetaan monikot ja niiden frekrenssit
        for i in range(0, len(self.lista)):
            # parit
            if i < (len(self.lista) - 1):
                stringi2 = self.lista[i] + " " + self.lista[i+1]
                if self.lista[i] not in self.sanakirja2.keys() and self.onko_kirjassa(self.lista[i], stringi2, self.sanakirja2) == False:
                    self.sanakirja2[self.lista[i]] = [[stringi2, 1]]
                    self.parilista.append([self.lista[i], self.lista[i+1], 1])
                elif self.lista[i] in self.sanakirja2.keys() and self.onko_kirjassa(self.lista[i], stringi2, self.sanakirja2) == False:
                    self.sanakirja2[self.lista[i]].append([stringi2, 1])
                    self.parilista.append([self.lista[i], self.lista[i+1], 1])
                else:
                    self.lisaa_kirjaukseen(
                        self.lista[i], stringi2, self.sanakirja2)
                    self.on_jo_mukana_2(self.lista[i], self.lista[i+1])

            # kolmikot
            if i < (len(self.lista) - 2):
                stringi3 = self.lista[i] + " " + \
                    self.lista[i+1] + " " + self.lista[i+2]
                if self.lista[i] not in self.sanakirja3.keys() and self.onko_kirjassa(self.lista[i], stringi3, self.sanakirja3) == False:
                    self.sanakirja3[self.lista[i]] = [[stringi3, 1]]
                    self.kolmikkolista.append(
                        [self.lista[i], self.lista[i+1], self.lista[i+2], 1])
                elif self.lista[i] in self.sanakirja3.keys() and self.onko_kirjassa(self.lista[i], stringi3, self.sanakirja3) == False:
                    self.sanakirja3[self.lista[i]].append([stringi3, 1])
                    self.kolmikkolista.append(
                        [self.lista[i], self.lista[i+1], self.lista[i+2], 1])
                else:
                    self.lisaa_kirjaukseen(
                        self.lista[i], stringi3, self.sanakirja3)
                    self.on_jo_mukana_3(
                        self.lista[i], self.lista[i+1], self.lista[i+2])

from triesolmu import Triesolmu


class Triepuu:

    def __init__(self):
        # puu alkaa juuresta, jolla ei ole sanaa tallennettuna.
        # puulla on myös sen kokoa kuvaava parametri.
        self.juuri = Triesolmu("")
        self.koko = 0

    def lisaa_sanat(self, sanakirja):
        avaimet = sanakirja.keys()
        tama_solmu = self.juuri
        for avain in avaimet:
            self.juuri.lisaa_lapsi(avain, Triesolmu(avain))
            tama_solmu = self.juuri.get_lapsi(avain)
            # print(sanakirja[avain])
            tama_solmu_alku = tama_solmu
            for perakkaiset in sanakirja[avain]:
                sanat = perakkaiset[0].split()
                tama_solmu = tama_solmu_alku
                # print(sanat)
                for sana in sanat[1:]:
                    tama_solmu.lisaa_lapsi(sana, Triesolmu(sana))
                    tama_solmu = tama_solmu.get_lapsi(sana)
                tama_solmu.lehti = True
                self.koko = self.koko + 1

    # ehkä se parempi metodi?
    def lisaa_sanat_test(self, sanakirja):
        avaimet = sanakirja.keys()
        for avain in avaimet:
            tama_solmu = self.juuri
            sanajonot = sanakirja[avain]
            indeksi = 0
            # yhtä avainta voi vastata lista monikoita. Monikoissa on monikon sanat
            # listan ensimmäisessä alkiossa ja monikon esiintymisenkerrat toisessa.
            for monikko in sanajonot:
                # print(monikko)
                tama_solmu = self.juuri
                sanajono = self.tee_sanoiksi(sanajonot, indeksi)
                kerrat = sanajonot[indeksi][1]
                # print(kerrat)
                indeksi = indeksi + 1
                montako_sanaa = len(sanajono)
                if self.onko_vastaava_lapsi(avain, tama_solmu) == True:
                    # print("test1")
                    self.lisaa_kerroin(avain, tama_solmu, kerrat)
                if self.onko_vastaava_lapsi(avain, tama_solmu) == False:
                    # print("test11")
                    self.lisaa_lapsi(avain, Triesolmu(
                        avain), tama_solmu, kerrat)
                tama_solmu = self.get_lapsi(avain, tama_solmu)
                # i = 1, sillä sanajonon ensimmäinen sana on avain itse
                i = 1
                while i < montako_sanaa:
                    if tama_solmu == None:
                        break
                    if self.onko_vastaava_lapsi(sanajono[i], tama_solmu) == True:
                        # print("test2")
                        self.lisaa_kerroin(sanajono[i], tama_solmu, kerrat)
                    if self.onko_vastaava_lapsi(avain, tama_solmu) == False:
                        # print("test22")
                        self.lisaa_lapsi(sanajono[i], Triesolmu(
                            sanajono[i]), tama_solmu, kerrat)
                    ed_solmu = tama_solmu
                    tama_solmu = self.get_lapsi(sanajono[i], tama_solmu)
                    i = i + 1
                # ollaanko ensimmäistä kertaa "polun" päässä
                # print(tama_solmu)
                # if tama_solmu.lehti == True:
                    # print("test4")
                    # tama_solmu.kerroin = tama_solmu.kerroin + kerrat
                if tama_solmu != None:
                    if tama_solmu.lehti == False:
                        self.koko = self.koko + 1
                    tama_solmu.lehti = True
                    ed_solmu.lapset[sanajono[i-1]] = tama_solmu
                # print(tama_solmu)

    def tee_sanoiksi(self, sanajono, indeksi):
        lista = []
        stringi = sanajono[indeksi][0]
        # print(stringi)
        stringi = stringi.split()
        for alkio in stringi:
            lista.append(alkio)
        return lista

    def hae_puusta(self, avain, solmu=None):
        # ei vielä tehty oikeasti
        if solmu == None:
            solmu = self.juuri
        return self.get_lapsi(avain, solmu)

    def hae_monikko(self, monikko):
        # metodi kokeilemaan onko sanamonikko puussa
        muodostettu = ""
        tama_solmu = self.juuri
        monikkosplit = monikko.split()
        for sana in monikkosplit:
            if self.onko_vastaava_lapsi(sana, tama_solmu):
                muodostettu = muodostettu + " " + sana
                tama_solmu = tama_solmu.lapset[sana]
            else:
                print("Ei vastaavaa monikkoa: " + monikko)
                return "Ei vastaavaa monikkoa: " + monikko
        muodostettu = muodostettu[1:]
        print("Löytyi monikko: " + muodostettu)
        return "Löytyi monikko: " + muodostettu

    def etsi_solmu(self, stringi):
        # ei vielä tehty oikeasti, voi olla melko turha
        if len(stringi) == 0:
            return self.juuri

    def onko_vastaava_lapsi(self, stringi, solmu):
        # kokeile löytyykö vastaava lapsisolmu
        # print(solmu.lapset.keys())
        listaus = list(solmu.lapset.keys())
        # print(listaus)
        if stringi in listaus:
            # print("True")
            return True
        else:
            # print("False")
            return False

    def get_lapsi(self, stringi, solmu):
        # hae annetun solmun lapsi jonka avain vastaa stringiä
        if self.onko_vastaava_lapsi(stringi, solmu):
            return solmu.lapset[stringi]
        else:
            return
            raise ValueError(f'Ei vastaavaa lasta sanalle {stringi}')

    def lisaa_lapsi(self, stringi, lapsisolmu, solmu, kerrat):
        # lisaa solmulle lapsi
        # print("###")
        # print(solmu.sana)
        # print(solmu.lapset.keys())
        # print("###")
        if self.onko_vastaava_lapsi(stringi, solmu) == False:
            lapsisolmu.kerroin = kerrat
            solmu.lapset[stringi] = lapsisolmu
        else:
            return
            raise ValueError(f'On jo vastaava lapsi sanalle {stringi}')

    def lisaa_kerroin(self, stringi, solmu, kerrat):
        # print("lol")
        if self.onko_vastaava_lapsi(stringi, solmu) == True:
            # print("onnistui")
            # print(solmu)
            kasiteltava = solmu.lapset[stringi]
            # print(kasiteltava)
            kasiteltava.kerroin = kasiteltava.kerroin + kerrat
        else:
            return
            raise ValueError(f'Ei löydykään lasta {stringi}')

    def on_tyhja(self):
        return self.koko == 0

    def get_koko(self):
        return self.koko

    # varsinainen toiminta

    def taydenna_monikko(self, prefiksi, solmu, lista):
        palautus = ""
        if len(solmu.lapset.keys()) == 0:
            palautus = (prefiksi + " " + solmu.sana, solmu.kerroin)
            # palautus = (prefiksi, solmu.kerroin)
            # print(palautus)
            # print("rekursio loppuu")
            lista.append(palautus)
        # print(palautus)
        # if avain in solmu.lapset.keys():
            # for avain in solmu.lapset.keys():
            # self.taydenna_monikko(prefiksi + " " + avain, avain, self.get_lapsi(avain,solmu))
        if len(solmu.lapset.keys()) > 0:
            prefiksi = prefiksi + " " + solmu.sana
            for avain in solmu.lapset.keys():
                # prefiksi = prefiksi + " " + solmu.sana
                # print(prefiksi)
                lista = self.taydenna_monikko(
                    prefiksi, self.get_lapsi(avain, solmu), lista)
        return lista

    def annamonikot_test(self, sanat):
        # antaa sanoihin sopivat monikot ja niiden frekvenssit
        tuloste = []
        sanat = sanat.split()
        sana_maara = len(sanat)
        sana = sanat[0]
        prefiksi = sana

        if sana not in self.juuri.lapset.keys():
            print("Ei löydy")
            # print(sanat)
            return

        if sana_maara == 1:
            tama_solmu = self.get_lapsi(sana, self.juuri)
            for seur_avain in tama_solmu.lapset.keys():
                # print("yksi valittiin")
                # tama_solmu = self.get_lapsi(seur_avain, self.juuri)
                # tuloste.append(self.taydenna_monikko(prefiksi, tama_solmu, tuloste))
                # print(prefiksi)
                tuloste = self.taydenna_monikko(
                    prefiksi, self.get_lapsi(seur_avain, tama_solmu), tuloste)
            # print(tuloste)
            return tuloste

        else:
            # print("pidempi kuin 1")
            seur_avain = sanat[0]
            tama_solmu = self.get_lapsi(seur_avain, self.juuri)
            indeksi = 1
            seur_avain = sanat[indeksi]
            paluu_solmu = tama_solmu
            while seur_avain in tama_solmu.lapset.keys():
                # prefiksi = prefiksi + " " + tama_solmu.sana
                paluu_solmu = tama_solmu
                tama_solmu = self.get_lapsi(seur_avain, tama_solmu)
                # prefiksi = prefiksi + " " + tama_solmu.sana
                indeksi = indeksi + 1
                if indeksi < len(sanat):
                    prefiksi = prefiksi + " " + tama_solmu.sana
                    seur_avain = sanat[indeksi]
            if seur_avain not in paluu_solmu.lapset.keys():
                print("Ei löydy")
                # print(paluu_solmu)
                # rint(sanat)
                # print(seur_avain)
                return
            # print(tama_solmu)
            # tama_solmu = paluu_solmu
            tuloste = self.taydenna_monikko(prefiksi, tama_solmu, tuloste)
            return tuloste
            # print("paluu")
            # print(paluu_solmu)

    # turhaa?
            print(prefiksi)
            for loppu_avain in tama_solmu.lapset.keys():
                tama_solmu = paluu_solmu
                tama_solmu = self.get_lapsi(loppu_avain, tama_solmu)
                # print("tama")
                # print(tama_solmu)
                # tuloste.append(self.taydenna_monikko(prefiksi, tama_solmu))
                tuloste = self.taydenna_monikko(prefiksi, tama_solmu, tuloste)

        # print(tuloste)
        return tuloste

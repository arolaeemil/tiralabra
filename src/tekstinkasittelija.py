#tekstinkäsittelijä
#pohja tekstinkäsittelijälle, toteutettiin tämän perusteella luokkana

teksti = ""
lista = []
sanakirja2 = {}
sanakirja3 = {}
parilista = []
kolmikkolista = []

def on_jo_mukana_2(sana1, sana2, lista1):
    for alkio in lista1:
        if sana1 == alkio[0] and sana2 == alkio[1]:
            alkio[2] = alkio[2] + 1
    return

def on_jo_mukana_3(sana1, sana2, sana3, lista1):
    for alkio in lista1:
        if sana1 == alkio[0] and sana2 == alkio[1] and sana3 == alkio[2]:
            alkio[3] = alkio[3] + 1
    return

def onko_kirjassa(sana, sanajono, kirja):
    if sana not in kirja.keys():
        return False
    kirjaukset = kirja[sana]
    for kirjaus in kirjaukset:
        if sanajono == kirjaus[0]:
            return True
    else:
        return False

def lisaa_kirjaukseen(sana1, sanajono, sanakirja):
    kohta = sanakirja[sana1]
    for apukohta in kohta:
        if apukohta[0] == sanajono:
            apukohta[1] = apukohta[1] + 1
    return

def printtaa_kirja(sanakirja):
    laskuri = 0
    for sana in sanakirja.keys():
        print(sana + ": ")
        for kirjaus in sanakirja[sana]:
            print("  " + kirjaus[0] + ", " + str(kirjaus[1]))
            laskuri = laskuri + 1
    print("monikoita yhteensä: " + str(laskuri))
    return

tiedostonimi = "testiteksti.txt"
tiedostonimi = "helppotesti.txt"

with open(tiedostonimi) as tiedosto:
    rivit = tiedosto.readlines()
    #print(rivit)

korvaajat = [('/', ''), ('Ã¤', 'ä'), ('Ã¶', 'ö'), ('Ã¼', 'ü'), ('.', ''), (',', ''), ('\n', ' ')]
for rivi in rivit:
    for char, korvaaja in korvaajat:
        if char in rivi:
            rivi = rivi.replace(char, korvaaja)
    teksti = teksti + rivi
teksti = teksti.lower()
#print(teksti)

lista = teksti.split()
#print(lista)

for i in range(0,len(lista)):
##################parit
    if i < (len(lista) - 1):
        #print(lista[i] + " " + lista[i+1])
        if lista[i] not in sanakirja2.keys() and onko_kirjassa(lista[i], lista[i] + " " + lista[i+1], sanakirja2) == False:
            sanakirja2[lista[i]] = [[lista[i] + " " + lista[i+1], 1]]
            parilista.append([lista[i],lista[i+1],1])
        elif lista[i] in sanakirja2.keys() and onko_kirjassa(lista[i], lista[i] + " " + lista[i+1], sanakirja2) == False:
            sanakirja2[lista[i]].append([lista[i] + " " + lista[i+1], 1])
            parilista.append([lista[i],lista[i+1],1])
        else:
            lisaa_kirjaukseen(lista[i], lista[i] + " " + lista[i+1], sanakirja2)
            #sanakirja2[lista[i]][1] = sanakirja2[lista[i]][1] + 1
            on_jo_mukana_2(lista[i], lista[i+1], parilista)

#################kolmikot
    if i < (len(lista) - 2):
        #print(lista[i] + " " + lista[i+1] + " " + lista[i+2])
        #if lista[i] not in sanakirja3.keys():
            #sanakirja3[lista[i]] = [lista[i] + " " + lista[i+1] + " " + lista[i+2], 1]
            #kolmikkolista.append([lista[i],lista[i+1],lista[i+2],1])
        #else:
            #sanakirja3[lista[i]][1] = sanakirja3[lista[i]][1] + 1
            #on_jo_mukana_3(lista[i], lista[i+1], lista[i+2], kolmikkolista)
        #print(lista[i] + " " + lista[i+1])
        if lista[i] not in sanakirja3.keys() and onko_kirjassa(lista[i], lista[i] + " " + lista[i+1] + " " + lista[i+2], sanakirja3) == False:
            sanakirja3[lista[i]] = [[lista[i] + " " + lista[i+1] + " " + lista[i+2], 1]]
            kolmikkolista.append([lista[i],lista[i+1],lista[i+2],1])
        elif lista[i] in sanakirja3.keys() and onko_kirjassa(lista[i], lista[i] + " " + lista[i+1] + " " + lista[i+2], sanakirja3) == False:
            sanakirja3[lista[i]].append([lista[i] + " " + lista[i+1] + " " + lista[i+2], 1])
            kolmikkolista.append([lista[i],lista[i+1],lista[i+2],1])
        else:
            lisaa_kirjaukseen(lista[i], lista[i] + " " + lista[i+1] + " " + lista[i+2], sanakirja3)
            #sanakirja2[lista[i]][1] = sanakirja2[lista[i]][1] + 1
            on_jo_mukana_3(lista[i], lista[i+1], lista[i+2], kolmikkolista)
    

print(teksti)
#print(lista)
print("parilista: ")
print(parilista)
print("parisanakirja: ")
print(sanakirja2)
print("kolmikkolista: ")
print(kolmikkolista)
print("kolmikkosanakirja: ")
print(sanakirja3)
printtaa_kirja(sanakirja2)
printtaa_kirja(sanakirja3)
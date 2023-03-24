from tekstinkasittelija_luokkana import Tekstinkasittelija

def main():
    tiedostonimi = "helppotesti.txt"
    tekstinkasittelija = Tekstinkasittelija(tiedostonimi)

    tekstinkasittelija.suorita_tarkastus()
    
    #print(tekstinkasittelija.teksti)
    #print(tekstinkasittelija.lista)
    #print(tekstinkasittelija.parilista)
    #print(tekstinkasittelija.kolmikkolista)
    #print(tekstinkasittelija.sanakirja2)
    #print(tekstinkasittelija.sanakirja3)

if __name__ == "__main__":
    main()
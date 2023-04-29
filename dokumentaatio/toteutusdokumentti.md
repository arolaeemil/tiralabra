**Sovelluksen toteutus on yleisluontoisesti kuvaillen seuraavanlainen:**

Tekstinkäsittelijä_luokkana ottaa syötteekseen opetusdataa ja pätkii sen samalla tallentaen esiintyvät monikot. Monikot ja niiden esiintyvyydet se palauttaa sanakirjana.

Triepuu:lla on metodit joilla se voi luoda triepuun sille syötettävän sanakirjamuotoisen monikkolistauksen perusteella. Puusta voi myös hakea monikoita sanojen perusteella. Triepuu koostuu triesolmuista. Jokaisella solmulla on sana, kerroin ja sanakirja joka koostuu sen lapsista. Triesolmut linkittyvät toisiinsa sanakirjojen kautta. Puun juurella ei ole sanaa tai kerrointa vaan pelkkä sanakirja lapsistaan.

Markovketju kysyy triepuulta mahdolliset monikot ja frekvenssit sanalla/sanoille ja arpoo frekvenssien avulla seuraavan/seuraavat sanan/sanat. Voidaan asettaa
ketjun aste ja haluttu sanamäärä. Tosin tukee tällä hetkellä lähinnä 1. ja 2. astetta. Korkeammat ketjun asteet johtaisivat tekstin suhteen lähinnä pelkkään opetusdatan
toistamiseen johtuen kielen rakenteesta.

Käyttöliittymä käyttää markovketju-luokkaa saamiensa syötteiden perusteella ja tulostaa tekstiä komentoriville.

**Kehitettävää:**

-voitasiin tehdä ratkaisu jonka avulla opetusdataa ei tarvitsisi käsitellä aina sovellusta käynnistettäessä.

-voisi laittaa generoimaan tekstiä tiedostoon komentorivin sijaan.

-käyttöliittymään opetusdatanvalitsin.

-lisäkehitystä sen suhteen miten erilaiset välimerkit kannattaa huomioida kielessä, jotta saataisiin mahdollisimman paljon käyttäjää tyydyttäviä lauseita.

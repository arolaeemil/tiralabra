Sovelluksen toteutus on karkeasti kuvaillen seuraavanlainen:

Tekstinkäsittelijä_luokkana ottaa syötteekseen opetusdataa ja pätkii sen samalla tallentaen esiintyvät monikot. Monikot ja niiden esiintyvyydet se palauttaa listana.

Triepuu:lla on metodit joilla se voi luoda triepuun sille syötettävän monikkolistan perusteella. Puusta voi myös hakea monikoita sanojen perusteella. Triepuu koostuu
triesolmuista. Jokaisella solmulla on sana, kerroin ja sanakirja joka koostuu sen lapsista. Triesolmut linkittyvät toisiinsa sanakirjojen kautta. Puun juurella ei ole sanaa tai kerrointa vaan pelkkä sanakirja lapsistaan.

Markovketju kysyy triepuulta mahdolliset monikot ja frekvenssit sanalla/sanoille ja arpoo frekvenssien avulla seuravan/seuraavat sanan/sanat. Voidaan asettaa
kerjun aste ja haluttu sanamäärä. Tosin tukee tällä hetkellä lähinnä 1. ja 2. astetta.

**Kehitettävää:**

-testataan pidempiä kuin 3 sanan monikkoja ja ketjun asteita yli 2. asteen. Tosin vaatii paljon opetusdataa jotta ei vain kopioitaisi vanhaa tekstiä.

-pitäisi tehdä päätöksiä sen suhteen miten välimerkit käsitellään siten että lauseista tulee järkevän mielekkäitä ja samaan aikaan monipuolisia. Ideaalitilanteessa
generoitaisiin lauseita, joissa olisi pisteet melko mielekkäissä kohdissa.

-voisi laittaa generoimaan tekstiä tiedostoon komentorivin sijaan kun kehittynyt pidemmälle.

-käyttöliittymään opetusdatanvalitsin.

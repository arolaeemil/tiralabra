**Valittu aihe:** Koneoppiminen, tekstintuotto Markovin ketjujen avulla.

**Projektin kieli:** Python. Parhaiten kykenen vertaisarvioimaan Pythonilla tehdyt projektit.

**Opinto-ohjelma:** Tietojenkäsittelytieteen kandiohjelma.
Dokumentaatio ja koodin kommentointi tullaan tekemään suomeksi.

**Algoritmit ja tietorakenteet:** Ohjelma tulee vaatimaan toiminnallisuuden, jolla halutunpituisia
monikoita voidaan poimia opetusdatasta. Opetusdata tulee olemaan tekstiä, joka syötetään sopivalla
tavalla siistittynä ohjelman osalle joka poimii halutunlaiset monikot. Sanasekvenssien tallentamiseen
suunnitelmana on toteuttaa trie-tietorakenne, jota hyödynnetään varsinaisessa tekstin generoinnissa.
Tavoitteena on että tietorakenne tulee toimimaan tekstin generoimisen suhteen logaritmisessa ajassa
suhteessa tallennettuun tietomäärään. Opetusdatan prosessoinnin ja tallentamisen suhteen tullaan pyrkimään
neliölliseen, korkeintaan kuutiolliseen aikavaativuuteen.

**Mitä ongelmaa ratkaisen ja miksi valitsin kyseiset tietorakenteet:** Ongelmana on tekstin tuottaminen 
opetusdatan perusteella. Kokeillaan kyetäänkö Markovin ketjuja hyödyntäen tuottamaan ihmisen näkökannalta
huvittavaa ja mahdollisesti jollakin muotoa järkevää tekstiä. Tekstintuottoa kokeillaan erilaisilla aineistoilla
ja Markovin ketjujen asteilla. Trie-tietorakenne valittiin, koska se vaikuttaa lupaavalta tavalta tallentaa haluttuja sanamonikoita puurakenteeseen siten, että niiden hakeminen on myöskin tehokasta.

**Ohjelman saamat syötteet:** Tekstiä tullaan generoimaan joko täysin satunnaisesti tai siten, että käyttäjä
saa halutessaan valita ensimmäisen sanan generoitavaan tekstikappaleeseen opetusadatan sallimissa rajoissa. Voidaan myös toteuttaa kyky valita minkätyyppisen opetusdatan perusteella tekstiä generoidaan.

**Lähteet:** Varsinaisia kirjallisia lähteitä ei ole kurssimateriaalin ja Markovin ketjuihin ja trie-tietorakenteeseen kuuluvan yleistiedon lisäksi vielä käytetty. Ohjelman opetusmateriaali tullaan valitsemaan myöhemmin jolloin lähteitä päivitetään. 

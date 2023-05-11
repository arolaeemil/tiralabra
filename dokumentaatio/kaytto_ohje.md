**Alkutoimet:** Aloitettassa sovelluksen käyttö kannattaa alkuun ladata riippuvuudet "poetry install".


**Testit:** Automaattitestit voi ajaa ja luoda testikattavuusraportin kansioon komennolla "poetry run invoke coverage-report". Raportti luodaan kansioon "htmlcov" ja sen nimi on "index.html". Sen voi katsoa vaikka komennolla "sensible-browser index.html".


**Sovelluksen käyttö:** Sovelluksen voi käynnistää "python3 src/index.py" Ohjeita tulostuu käytön edetessä. Alkuun tulostuu myös lista opetusdatan mahdollistamista sanoista. Tämä voi viedä jokseenkin runsaasti komentorivin rivejä. Sovelluksen käyttämän opetusdatan voi valita kommentoimalla/poistemalla kommentteja "src/index.py" tiedostossa. Kannattaa huomioida, että tällä hetkellä sovellus käy datan läpi aina käynnistettäessä jotain isoilla datoilla voi kestää hetki. Dataa on tekstitiedostoina "src/opetusdata" kansiossa.

Index.py:n käyttämä data on esikäsiteltyä prosessin nopeuttamiseksi. Koko prosessin voi ajaa raakatekstistä alkaen index_uusidata.py avulla. Tämän lisäksi on olemassa index_datanesikasittely.py jonka avulla dataa voidaan esikäsitellä ja tallentta sanakirjoiksi tiedostoon käytön nopeuttamiseksi. Esikäsitellyt datat tallentuvat src/kasiteltydata-kansioon.

Jokainen index*-tiedosto sisältää kommentteina runsaasti ohjeita mahdollisia datanvaihtoja varten. Myös koodia on jätetty kommentoiduksi datan vaihtoa ja vastaavaa käyttöä varten.

**Opetusdata:** Sovellus ladattaessa valittuna opetusdatana toimivat Donald Trumpin presidenttinä ja kampanjoidessaan pitämät puheet. Muita vaihtoehtoja ovat suomalaiset aikuisnovellit, Suomen tieliikennelaki, Aleksis Kiven Seitsemän Veljestä ja tiralabra kurssin kurssimateriaali. Mukana on myös muutama lyhennetty aineisto edellisistä muutosten kokeilua varten. Omaa opetusdataa voidaan tehdä yksinkertaisesti tallentamalla haluttu määrä tekstiä yhteen tekstitiedostoon ja lisäämällä se src/opetusdata-kansioon ja tekemällä index*-tiedostojen kommenteissa ohjeistetut muutokset.

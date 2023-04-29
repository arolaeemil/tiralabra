Aloitettassa sovelluksen käyttö kannattaa alkuun ladata riippuvuudet "poetry install".


Automaattitestit voi ajaa ja luoda testikattavuusraportin kansioon komennolla "poetry run invoke coverage-report". Raportti luodaan
kansioon "htmlcov" ja sen nimi on "index.html". Sen voi katsoa vaikka komennolla "sensible-browser index.html".


Sovelluksen voi käynnistää "python3 src/index.py" Ohjeita tulostuu käytön edetessä. Alkuun tulostuu myös lista opetusdatan mahdollistamista sanoista. Tämä voi viedä jokseenkin runsaasti komentorivin rivejä. Sovelluksen käyttämän opetusdatan voi valita kommentoimalla/poistemalla kommentteja "src/index.py" tiedostossa. Kannattaa huomioida, että tällä hetkellä sovellus käy datan läpi
aina käynnistettäessä jotain isoilla datoilla voi kestää hetki. Dataa on tekstitiedostoina "src/opetusdata" kansiossa. 

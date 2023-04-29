Tällä hetkellä on olemassa liki kaikki metodit kattava yksikkötestaus triepuu, triesolmu, tekstinkasittelija_luokkana ja markovketju luokille. Käyttöliittymällä
ei ole omia testejä.

Tekstinkäsittelijän suhteen on olemassa testit lyhyen syötteen sisäänlukemisen oikeellisuudesta. Testattu että sanakirja muodostuu oikein syötteen perusteella siten, että se on halutunlaisessa muodossa ja sisältää oikean määrän monikoita ja että monikoiden frekvenssit menevät oikein. 

Triesolmulla on triviaalit testit metodeihinsa. Triesolmulla ei juurikaan ole omia vastuualueitaan ja se esiintyy aina triepuun osana, joten kovin monimutkaisia asioita ei pelkällä solmulla voi edes testata.

Triepuun testeissä on pyritty testaamaan että oikeat monikot oikeilla kertoimilla löytyvät puusta ja ettei siellä ole sinne kuulumattomia löydöksiä. Tämä pitää sisällään sen että kertoimet päivittyvät kun puuhun lisätään sanajonoja. On myös testattu että puuhun voidaan tallentaa sanaketjuja pituuteen 7 asti ja että ne löytyvät haettaessa. Rakenne mahdollistaa pitkien sanajonojen sijoittamisen, vaikka tällä hetkellä tekstinkäsittelijä ei sellaisia tuotakaan.

Markovketjun suhteen yritetty varmistua siitä ettei muodostu sellaisia sanajonoja, joita ei pitäisi voida muodostaa. Eli että ketju ei loisi sellaisia tekstejä joita
opetusdata ei mahdollista. Testit kokeilevat 1. ja 2. asteen ketjuja sillä tehtiin huomio, että pidemmät ketjun ovat käytännössä datan toistoa. Nämä ovat käyttöliittymän
kautta tällä hetkellä pyydettävissä olevat ketjun asteet.

Taulukko yksikkötestien kattavuudesta alla:

![coverage_report](https://github.com/arolaeemil/tiralabra/blob/main/kuvat/Sieppaa.PNG)

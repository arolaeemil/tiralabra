Tällä hetkellä on olemassa liki kaikki metodit kattava yksikkötestaus triepuu, triesolmu, tekstinkasittelija_luokkana ja markovketju luokille. Käyttöliittymällä
ei ole omia testejä.

Tekstinkäsittelijän suhteen on olemassa testit lyhyen syötteen sisäänlukemisen oikeellisuudesta.

Triesolmulla on triviaalit testit metodeihinsa.

Triepuun testeissä on pyritty testaamaan että oikeat monikot oikeilla kertoimilla löytyvät puusta ja ettei siellä ole sinne kuulumattomia löydöksiä. On myös testattu
että puuhun voidaan tallentaa sanaketjuja pituuteen 7 asti ja että ne löytyvät haettaessa. 

Markovketjun suhteen yritetty varmistua siitä ettei muodostu sellaisia sanajonoja, joita ei pitäisi voida muodostaa. Eli että ketju ei loisi sellaisia tekstejä joita
opetusdata ei mahdollista. Testit kokeilevat 1. ja 2. asteen ketjuja sillä tehtiin huomio, että pidemmät ketjun ovat käytännössä datan toistoa. Nämä ovat käyttöliittymän
kauttaa tällä hetkellä pyydettävissä olevat ketjun asteet.

Taulukko yksikkötestien kattavuudesta alla:

![coverage_report](https://github.com/arolaeemil/tiralabra/blob/main/kuvat/Sieppaa.PNG)

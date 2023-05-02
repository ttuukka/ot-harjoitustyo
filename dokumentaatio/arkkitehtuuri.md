# Arkkitehtuurikuvaus

## Rakenne

Pelin rakenne koostuu kolmesta osasta. Ui sisältää pelin käyttöliittymän, Logic logiikan ja Database pelin kysymykset ja tallennetetut tulokset.

![IMG_3496 Large](https://user-images.githubusercontent.com/128143830/232796760-04dce821-fc62-47cc-98e4-b3b48725550b.jpeg)

### Käyttöliittymä

Käyttöliittymä koostuu kolmesta luokasta Button, Ui ja Quiz.

Button luokan avulla voidaan luoda uusia painikkeita, joille voidaan määrätä sijainti,teksti ja koko.

Ui luokka sisältää pelin kaikki eri näkymät, joita tällä hetkellä on aloitus, kysymys, pisteiden tallentaminen, top10 parhaat pisteet ja pelin lopetus. Tämän lisäsi luokassa on sisällä kaksi metodia, jotka vastaavat tekstin piirtämisestä ja uusien painikkeiden luomisesta

Quiz luokka ottaa vastaan ja käsittelee käyttäjän syötteen ja vaihtaa näkymää tarvittaessa.

### Sovelluslogiikka

Pelin Logiikasta vastaa luokka Logic. Luokka kuvaa pelin sen hetkistä tilannetta. Tämä sisältää pisteet, kysymyksen (joka sisältää myös vastausvaihtoehdot, sekä oikeain vastauksen), kysytyt kysymykset, sekä tiedon onko peli päättynyt.

Luokka sisältää kaikki toiminnallisuudet pelin toimimiseen mm. uusien kysymyksien hakeminen, vastauksen tarkistus ja pelin uudelleenkäynnistys

### Database

Rakenne sisältää luokan Database, jossa on listassa kaikki pelin kysymykset(lista vaihtuu .csv tiedostoksi)

Tämän lisäksi rakenteeseen tallennetaan high_scores.txt tiedosto, kun pelaaja ensimmäisen kerran tallentaa tuloksensa. Ensimmäisen tallennuksen jälkeen tulokset tallennetaan olemassa olevaan tiedostoon.

## Sekvenssikaavio
Kaavio kuvaa kun käyttäjä aloittaa pelin ja vastaa kysymykseen oikein

![Untitled](https://user-images.githubusercontent.com/128143830/234311845-0356e312-8f6e-4963-8fb1-30f90e2b2e85.png)

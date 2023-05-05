# Arkkitehtuurikuvaus

## Rakenne

Pelin pakkaurakenne:

![IMG_3538 Small](https://user-images.githubusercontent.com/128143830/236457932-f6ff7f80-af64-4156-8a2e-45d8d6d1236f.png)

Rakenne koostuu kolmesta osasta. Ui sisältää pelin käyttöliittymän, Logic logiikan ja Database pelin kysymykset ja tallennetetut tulokset.


### Käyttöliittymä

Käyttöliittymällä on on viisi erillaista näkymää:

-Aloitusnäkymä
-Kysymys-näkymä
-Pelin loppu-näkymä
-Pisteiden talletus-näkymä
-Tulostaulu -näkymä

Kaikki näkymät löytyvät [Views](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/ui/views.py)-luokasta. [Userinterface](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/ui/ui.py)-luokka vastaanottaa pelaajan syötteen, sekä yhdistää pelin logiikan ja näkymät.
[Button](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/ui/button.py)-luokka vastaa painikkeista.

### Sovelluslogiikka

Pelin Logiikasta vastaa [Logic](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/logic/logic.py)-luokka. Luokka kuvaa pelin sen hetkistä tilannetta. Tämä sisältää:
- Pisteet
- Vastausajan
- Kysymyksen (joka sisältää myös vastausvaihtoehdot, sekä oikean vastauksen), kysytyt kysymykset
- Tiedon onko peli päättynyt
- Tiedon pelimuodosta 

Luokka sisältää kaikki toiminnallisuudet pelin toimimiseen mm. uusien kysymyksien hakeminen, vastauksen tarkistus ja pelin uudelleenkäynnistys

### Database

Rakenne Database sisältää pelin kysymykset [questions_db.txt](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/database/questions_db.txt) ja  tulokset high_scores.txt. Kysymykset ja tulokset ovat csv-muodossa.

Kysymysten rakenne on ```text,answer1,answer2,answer3,answer4,correct_answer```

Tulosten rakenne on ```name,score,mode```

Rakenne sisältää myös näiden tiedostojen lukemiseen ja kirjoittamiseen tehdyt luokat [question_repository.py](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/database/question_repository.py) ja [score_repository.py](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/database/score_repository.py).

Näiden lisäksi rakenteesta löytyy [Question](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/database/question.py)-luokka, jonka avulla käsitellään kysymysten rakennetta pelissä.

## Sekvenssikaavio
Kaavio kuvaa kun käyttäjä aloittaa pelin ja vastaa kysymykseen oikein

![Untitled](https://user-images.githubusercontent.com/128143830/234311845-0356e312-8f6e-4963-8fb1-30f90e2b2e85.png)

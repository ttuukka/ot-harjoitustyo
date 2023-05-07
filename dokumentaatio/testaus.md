# Testausdokumentti

Ohjelman logiikkaa, sekä kysymysten lukemista ja tulosten tallenusta on yksikkötestattu Unittestilla

## Yksikkötestaus

### Logiikka

`Logic`-luokka testataan [TestLogic](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/tests/logic_test.py) -luokalla. Luokka testaa yksittäisten metodien lisäksi pelitilanteet, joissa pelaaja vastaa kysymyksiin oikein, sekä väärin.

### Repostorio-luokat

`QuestionRepository`-luokkaa testaa [TestQuestionRepository](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/tests/question_repo_test.py) -luokka. Testissä luetaan valmiiksi tehty tiedosto, joka sisältää kolmekysymystä. Tämän jälkeen testaan, että kysymykset on luettu oikein ja lisätty Question-oliona listaan.

`ScoreReposotiry` -luokkaa testaa [TestScoreRepository](https://github.com/ttuukka/ot-harjoitustyo/blob/master/src/tests/score_repo_test.py) - luokka. Testissä annetaan polku, jonne testattava luokka luo uuden tyhjän tiedoston. Testi lisää sinne molempien muotojen tuloksia 11 kappaletta. Tämän jälkeen tarkistetaan, että metodi `get_top10_scores()` palauttaa oikeanlaiset listat tuloksista.

### Testauskattavuus 

Testauksen haarautumakattavuus on 85%. Käyttöliittymää ei ole testattu.

![image](https://user-images.githubusercontent.com/128143830/236680303-c5691a62-061d-4d8f-8a18-9c8fb053aafb.png)

## Järjestätestaus

Peli on järjestelmätestattu manuaalisesti

### Asennus ja käynnistäminen

Peli on asennettu ja peltta [käyttöohjeiden](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) mukaisesti. MacOs- ja Linux-käyttöjärjestelmillä.

### Toiminallisuudet 

Kaikki [vaatimusmäärittelyn](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) sisältämät toiminnallisuudet on käyty läpi. 

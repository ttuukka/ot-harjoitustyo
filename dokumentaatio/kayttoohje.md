# Käyttöohje

Lataa projektin uusin [release](https://github.com/ttuukka/ot-harjoitustyo/releases) "Source code" kohdasta.

## Pelin käynnistäminen

Aluksi asennenna vaaditut riippuvuudet komennolla:

```bash
poetry install
```

Tämän jälkeen voit käynnistää pelin komennolla:

```bash
poetry run invoke start
```

## Pelin aloittaminen

Peli aukeaa aloitusnäkymään, jossa voi aloittaa pelin painamalla Start-painiketta, tai katsoa tulostalukkoa painamalla High Scores-painiketta.

Pelin aloittamisen jälkeen saat kysymyksen ja siihen neljä vastausvaihtoehtoa. Oikeata vastauksia on yksi. Vastaamalla oikein kerrytät pisteitä ja vastamaalla väärin peli loppuu.

## Pelin loppuminen

Pelin loputtua näät keräämäsi pisteet. Voit pelata peliä uudestaan, jolloin pisteet nollaantuu tai voit tallentaa tuloksesi tulostaulukkoon.
Tallentaminen tapahtuu painamalla Save Score -painiketta. Tämän jälkeen voit kirjoittaa nimimerkkisi syötelaatikkoon. Tuloksen tallenminen viedään loppuun painamalla ENTER -näppäintä.
Pelin voit lopettaa painamalla Exit -paniketta, tai vaihtoehtoisesti painamalla ESC -näpääintä milloin vain.

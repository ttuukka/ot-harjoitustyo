# Käyttöohje

Lataa pelin uusin [release](https://github.com/ttuukka/ot-harjoitustyo/releases) "Source code" kohdasta.

## Poetryn asentaminen
Asenna poetry [ohjeiden](https://python-poetry.org/docs/) mukaisesti. Pelin asentaminen vaatii poetryn version 1.4.1.

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

Peli avautuu aloitusnäkymään:
<img width="794" alt="Screenshot 2023-05-05 at 14 39 21" src="https://user-images.githubusercontent.com/128143830/236448214-a21d831b-bec3-4c1b-8397-34658a868b83.png">

Pelaaja kontrolloi pelin paininikkeita hiirellä.
Klikkaamalla "Start Normal" peli käynnistyy normaalissa pelimuodossa. Tällöin kertyy yksi piste jokaisesta oikein vastatusta kysymyksesta.

Klikkaamalla "Start Time" peli käynnistyy aika pelimuodossa. Tällöin pisteitä kertyy sen mukaan, kuinka nopeasti kysymykseen vatataan oikein. vastausaika 10 sekunttia, jonka jälkeen oikeista vastauksista saa nolla pistettä. Mahdolliset pisteet yhdestä kysymyksestä ovat siis 0.00-10.00 pistettä.

Kysymysnäkymä:
<img width="800" alt="Screenshot 2023-05-05 at 14 47 16" src="https://user-images.githubusercontent.com/128143830/236449758-b146b943-9b25-4901-b4ee-23271a6dd712.png">

Pelaaja valitsee vastausvaihtoehdoista mielestään oikean. Oikean vastauksen jälkeen pelaajalle esitetään uusi kysymys. Värää vastaus taas lopettaa pelin.

Pelin loppunäkymä:
<img width="800" alt="Screenshot 2023-05-05 at 14 47 43" src="https://user-images.githubusercontent.com/128143830/236449848-2edefd53-0c56-40d1-83d8-938ebae4c701.png">

Pelin loputtua pelaaja pystyy tallentaamaan pisteensä valitsemalla "Save Score". Tämän jälkeen pelaaja kirjoittaa nimimerkkinsä ja tallettaa sen painamalla ENTER-näppäintä.

Pisteiden talletusnäkymä:
<img width="794" alt="Screenshot 2023-05-05 at 14 55 38" src="https://user-images.githubusercontent.com/128143830/236451865-24e85be9-0bf8-4d86-9ff5-e922921634fa.png">

Pelaaja voi myös katsoa kymmenen parhaan tuloksen taulukkoa, jossa pisteet on eritelty pelimuodon mukaan painamalla "High Scores".

Taulukkonäkymä:
<img width="794" alt="Screenshot 2023-05-05 at 14 55 38" src="https://user-images.githubusercontent.com/128143830/236452336-49319ee3-797d-4b67-a1d8-3d9bfa91dcab.png">

Valitsemalla "Restart" pelaaja voi valita uudesta pelimuodon ja käynnistää uuden pelin.

Valitsemalla "Exit" peli sulkeutuu. Pelaaja voi myös lopettaa pelin koska tahansa painamalla ESC-näppäintä.







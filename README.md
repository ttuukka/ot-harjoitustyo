# Tietovisa-peli
Pelissä vastataan erillaisiin kysymyksiin valmiilla vastauksilla ja kerätään oikeista vastauksista pisteitä.

## Dokumentaatio
- [Vaatimuusmäärittely](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Ohjeet

### Asennus
Aluksi asenna tarvittavat riipuvuudet komennolla:
`poetry install`

### Käynnistäminen
Peli käynnistyy kommennolla:
`poetry invoke start`

### Testaus
Testit saat ajettua komennolla:
`poetry run invoke test`

Testikattavuusraporitin muodostaminen onnistuu komennolla:
`poetry run invoke coverage-report`

### Pylint
Pylint-tarkistuksen saa komennolla:
`poetry run invoke lint`


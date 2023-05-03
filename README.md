# Tietovisa-peli
Pelissä valitaan oikea vastaus erillaisiin kysymyksiin ja kerätään oikeista vastauksista pisteitä.

## Dokumentaatio
- [Käyttöohje](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimuusmäärittely](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/ttuukka/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Releaset
[Viikko 6] (https://github.com/ttuukka/ot-harjoitustyo/releases/tag/viikko6)
[Viikko 5](https://github.com/ttuukka/ot-harjoitustyo/releases/tag/viikko5)
## Ohjeet

### Asennus
Aluksi asenna tarvittavat riipuvuudet komennolla:
`poetry install`

### Käynnistäminen
Peli käynnistyy kommennolla:
`poetry run invoke start`

### Testaus
Testit saat ajettua komennolla:
`poetry run invoke test`

Testikattavuusraporitin muodostaminen onnistuu komennolla:
`poetry run invoke coverage-report`

### Pylint
Pylint-tarkistuksen saa komennolla:
`poetry run invoke lint`


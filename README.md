# ShelfJournal :books:
Tietokantasovellus pythonilla Herokuun. Ideana tehdä digitaalinen kirjayhteisö, jossa voi perustaa ryhmiä ja jakaa omien kirjahyllyjen ja arvostelujen tietoja ryhmäläisille.

[ShelfJournalin verkkosivu](https://shelfjournal.herokuapp.com/)

# Sovelluksen toiminta

Sovelluksessa näkyy oma kirjasto, joista voi etsiä tietoa ja lukea arvioita. Käyttäjät jaotellaan peruskäyttäjiin ja ylläpitäjään:heavy_check_mark:
1. Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen. :heavy_check_mark:
2. Käyttäjä voi lisätä kirjoja :heavy_check_mark:
3. Käyttäjä voi etsiä kirjan nimen perusteella :heavy_check_mark:
4. Käyttäjä voi etsiä kirjailijan nimen perusteella :heavy_check_mark:
5. Käyttäjä voi etsiä genren perusteella :heavy_check_mark:
6. Käyttäjä näkee hyllyistä kirjat ja voi painaa kirjasta, jolloin siitä näytetään lisää tietoa (kuten kuvaus ja kirjoittaja, ostovuosi tms.). :heavy_check_mark:
7. Käyttäjällä on oma privaatti näkymä ja erikseen näkymä julkisille kirjoille :heavy_check_mark:
8. Käyttäjä voi antaa arvion (tähdet ja kommentti) kirjasta ja lukea muiden antamia arvioita.:heavy_check_mark:
9. Käyttäjä voi etsiä kaikki kirjat, joiden genressä on annettu sana.:heavy_check_mark:
10. Käyttäjä voi järjestää arviot etsi kirja osiossa, valitsemalla minkä arvosanan listan haluaa nähdä.:heavy_check_mark:
11. Käyttäjä voi tehdä lukuryhmän:heavy_check_mark: ja lisätä ryhmään jäseniä (ryhmän jäsenet liittyvät siihen itse salasanalla).
12. Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion tai korjata kirjan tietoja ja poistaa ryhmiä.
13. Ylläpitäjä voi luoda ryhmiä, joihin kirjoja voi luokitella. Kirja voi kuulua yhteen tai useampaan ryhmään. Esim. dekkarit, tietokirjat, kaunokirjallisuus tms.
14. Oman kirjahyllyn voi jakaa halutessaan valitsemilleen käyttäjille

Toteutan sovellukseen ensiksi oman digitaalisen kirjahyllyn, sitten arvionnin ja lopuksi ryhmät.
# Hahmotelma UI:sta
Tässä on ensimmäinen kaavio sovelluksen toiminnasta [UI luonnos](https://github.com/Mazaalto/ShelfJournal/blob/main/ShelfJournal.pdf).

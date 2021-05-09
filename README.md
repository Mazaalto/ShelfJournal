# ShelfJournal :books:
Tietokantasovellus pythonilla Herokuun. Ideana tehdä digitaalinen kirjayhteisö, johon voi tallentaa oman kirjahyllynsä sisällön sekä tarkastella muiden kirjahyllyjen sisältöä, arvostella kirjoja ja löytää uutta luettavaa.


[ShelfJournalin verkkosivu](https://shelfjournal.herokuapp.com/)

# Sovelluksen toiminta

Sovelluksessa näkyy oma kirjasto, joista voi etsiä tietoa ja lukea arvioita. Käyttäjät jaotellaan peruskäyttäjiin ja ylläpitäjään:heavy_check_mark:
Omaan kirjastoon pääse välilehdeltä Oma kirjahyllysi. Palvelun päänäkymässä voi nähdä kaikki julkiseksi merkatut kirjat listattuna.
1. Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen. :heavy_check_mark:
2. Käyttäjä voi lisätä kirjoja :heavy_check_mark: Tämä tapahtuu palvelussa välilehdeltä Lisää kirja kirjahyllyysi.
3. Käyttäjä voi etsiä kirjan nimen perusteella :heavy_check_mark:
4. Käyttäjä voi etsiä kirjailijan nimen perusteella :heavy_check_mark:
5. Käyttäjä voi etsiä genren perusteella :heavy_check_mark:
6. Käyttäjä näkee hyllyistä kirjat ja voi painaa kirjasta, jolloin siitä näytetään lisää tietoa (kuten kuvaus ja kirjoittaja, ostovuosi tms.). :heavy_check_mark:
7. Käyttäjällä on oma privaatti näkymä ja erikseen näkymä julkisille kirjoille :heavy_check_mark:
8. Käyttäjä voi antaa arvion (tähdet ja kommentti) kirjasta ja lukea muiden antamia arvioita.:heavy_check_mark:
9. Käyttäjä voi etsiä kaikki kirjat, joiden genressä on annettu sana.:heavy_check_mark:
10. Käyttäjä voi järjestää arviot etsi kirja osiossa, valitsemalla minkä arvosanan listan haluaa nähdä.:heavy_check_mark:
11. Käyttäjä voi tehdä lukuryhmän:heavy_check_mark: ja lisätä ryhmään jäseniä (ryhmän jäsenet liittyvät siihen itse salasanalla, ei vielä valmis).
12. Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion tai korjata kirjan tietoja ja poistaa ryhmiä.
13. Ylläpitäjä voi luoda ryhmiä, joihin kirjoja voi luokitella. Kirja voi kuulua yhteen tai useampaan ryhmään. Esim. dekkarit, tietokirjat, kaunokirjallisuus tms.
14. Oman kirjahyllyn voi jakaa halutessaan valitsemilleen käyttäjille:heavy_check_mark: Tämä onnistuu merkkaamalla kirjat julkisiksi.

Toteutan sovellukseen ensiksi oman digitaalisen kirjahyllyn, sitten arvionnin ja lopuksi ryhmät.
# Hahmotelma UI:sta
Tässä on ensimmäinen kaavio sovelluksen toiminnasta [UI luonnos](https://github.com/Mazaalto/ShelfJournal/blob/main/ShelfJournal.pdf).

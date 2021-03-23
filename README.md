# ShelfJournal :books:
Tietokantasovellus pythonilla Herokuun. Ideana tehdä digitaalinen kirjayhteisö, jossa voi perustaa ryhmiä ja jakaa omien kirjahyllyjen ja arvostelujen tietoja ryhmäläisille.

# Sovelluksen toiminta

Sovelluksessa näkyy oma kirjasto, joista voi etsiä tietoa ja lukea arvioita. Käyttäjät jaotellaan peruskäyttäjiin ja ylläpitäjään.
1. Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
2. Käyttäjä näkee hyllyistä kirjat ja voi painaa kirjasta, jolloin siitä näytetään lisää tietoa (kuten kuvaus ja kirjoittaja, ostovuosi tms.).
3. Käyttäjä voi antaa arvion (tähdet ja kommentti) kirjasta ja lukea muiden antamia arvioita.
4. Käyttäjä voi lisätä kirjoja sekä määrittää kirjoista näytettävän arvion.
5. Käyttäjä voi etsiä kaikki kirjat, joiden kuvauksessa on annettu sana.
6. Käyttäjä näkee myös listan, jossa kirjat on järjestetty parhaimmasta huonoimpaan arvioiden mukaisesti.
7. Käyttäjä voi tehdä lukuryhmän ja lisätä ryhmään jäseniä.
8. Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion tai korjata kirjan tietoja ja poistaa ryhmiä.
9. Ylläpitäjä voi luoda ryhmiä, joihin kirjoja voi luokitella. Kirja voi kuulua yhteen tai useampaan ryhmään. Esim. dekkarit, tietokirjat, kaunokirjallisuus tms.
10. Oman kirjahyllyn voi jakaa halutessaan valitsemilleen käyttäjille

Toteutan sovellukseen ensiksi oman digitaalisen kirjahyllyn, sitten arvionnin ja lopuksi ryhmät.
# Hahmotelma UI:sta
Tässä on ensimmäinen kaavio sovelluksen toiminnasta [UI luonnos](https://github.com/Mazaalto/ShelfJournal/blob/main/ShelfJournal.pdf).

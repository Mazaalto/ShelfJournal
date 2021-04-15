# ShelfJournal :books:
Tietokantasovellus pythonilla Herokuun. Ideana tehdä digitaalinen kirjayhteisö, jossa voi perustaa ryhmiä ja jakaa omien kirjahyllyjen ja arvostelujen tietoja ryhmäläisille.

[ShelfJournalin verkkosivu](https://shelfjournal.herokuapp.com/)

# Sovelluksen toiminta

Sovelluksessa näkyy oma kirjasto, joista voi etsiä tietoa ja lukea arvioita. Käyttäjät jaotellaan peruskäyttäjiin ja ylläpitäjään (Ei vielä tehty, kaikilla toistaiseksi samat oikeudet (lisätä ja etsiä kirjoja)).
1. Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen. :heavy_check_mark:
2. Käyttäjä voi lisätä kirjoja :heavy_check_mark:
3. Käyttäjä voi etsiä kirjan nimen perusteella :heavy_check_mark:
4. Käyttäjä voi etsiä kirjailijan nimen perusteella :heavy_check_mark:
5. Käyttäjä voi etsiä genren perusteella :heavy_check_mark:
6. Käyttäjä näkee hyllyistä kirjat ja voi painaa kirjasta, jolloin siitä näytetään lisää tietoa (kuten kuvaus ja kirjoittaja, ostovuosi tms.). :heavy_check_mark:
7. Käyttäjä voi antaa arvion (tähdet ja kommentti) kirjasta ja lukea muiden antamia arvioita.
8. Käyttäjä voi etsiä kaikki kirjat, joiden kuvauksessa on annettu sana.
9. Käyttäjä näkee myös listan, jossa kirjat on järjestetty parhaimmasta huonoimpaan arvioiden mukaisesti.
10. Käyttäjä voi tehdä lukuryhmän ja lisätä ryhmään jäseniä.
11. Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion tai korjata kirjan tietoja ja poistaa ryhmiä.
12. Ylläpitäjä voi luoda ryhmiä, joihin kirjoja voi luokitella. Kirja voi kuulua yhteen tai useampaan ryhmään. Esim. dekkarit, tietokirjat, kaunokirjallisuus tms.
13. Oman kirjahyllyn voi jakaa halutessaan valitsemilleen käyttäjille

Toteutan sovellukseen ensiksi oman digitaalisen kirjahyllyn, sitten arvionnin ja lopuksi ryhmät.
# Hahmotelma UI:sta
Tässä on ensimmäinen kaavio sovelluksen toiminnasta [UI luonnos](https://github.com/Mazaalto/ShelfJournal/blob/main/ShelfJournal.pdf).

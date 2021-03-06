from app import app
import users, books, reviews, clubs
from flask import redirect, render_template, request, session

# Lukupiirin luominen organize_book_club
@app.route("/organize_book_club")
def organize_book_club():
    return render_template("organize_book_club.html")

@app.route("/registered_book_club", methods=["POST"])
def registered_book_club():
    club_title = request.form["club_title"]
    if len(club_title) > 50:
        return render_template("error.html", message = "Kirjoitit liian pitkän nimen kirjaryhmälle")
    club_info = request.form["club_info"]
    if len(club_info) > 40:
        return render_template("error.html", message = "Kirjoitit liian pitkän kuvauksen ryhmälle")    
    club_password = request.form["club_password"]
    if len(club_password) > 40:
        return render_template("error.html", message = "Kirjoitit liian pitkän tunnussanan ryhmälle")
        # tallentuu joko private tai public
    user_id = request.form["id"]
    visibility = "public"
    if clubs.save_club(club_title, club_info, club_password, user_id, visibility):
        return redirect("/")
    else:
        return render_template("error.html",message="Ryhmän tallentaminen ei onnistunut")

# mahdollisuus liittyä lukupiiriin "/join_book_club"
@app.route("/join_book_club", methods=["GET"])
def join_book_club():
    list = clubs.get_clubs_as_a_list()
    return render_template("join_book_club.html", clubs=list)

# Kirjan lisaamista
@app.route("/register_new_book")
def register_new_book():
    return render_template("register_new_book.html")

# tästä mennään kirjan arviointisivulle, joka tallentuu registered reviewn kautta
@app.route("/kirjanarviointi/<int:id>", methods=["GET"])
def book_review(id):
    return render_template("review.html", id=id)
# seuraavaksi toteutan arvion tallentamisen

@app.route("/registered_review", methods=["POST"])
def registered_review():
    book_id = request.form["book_id"]
    stars = request.form["review"]
    text_review = request.form["text_review"]
    if len(text_review) > 100:
        return render_template("error.html", message = "Kirjoitit liian pitkän arvion, yli 100 merkkiä")  
    
    # tallentuu joko private tai public
    visibility = request.form["visibility"]
    if reviews.save_review(book_id, stars, text_review, visibility):
        return redirect("/")
    else:
        return render_template("error.html",message="Arvion tallentaminen ei onnistunut ")
        
# katson kirjantiedot metodista vinkkiä
@app.route("/kirjanarvioinnit/<int:id>", methods=["GET"])
def get_reviews(id):
    list = reviews.get_reviews(id)
    return render_template("reviews2.html", id=id, review=list)

@app.route("/reviews_as_list", methods=["GET"])
def reviews_as_list ():
    list = reviews.get_all_public_reviews_proto_final()
    return render_template("reviews.html", reviews=list)

@app.route("/registered_book", methods=["POST"])
def registered_book():
    book_title = request.form["book_title"]
    if len(book_title) > 50:
        return render_template("error.html", message = "Kirjoitit liian pitkän nimen kirjalle")
    author_name = request.form["author_name"]
    if len(author_name) > 40:
        return render_template("error.html", message = "Kirjoitit liian pitkän nimen kirjailijalle tai kirjailijoille")    
    info = request.form["info"]
    if len(info) > 100:
        return render_template("error.html", message = "Kirjoitit liian pitkän kuvauksen")
        # tallentuu joko private tai public
    visibility = request.form["visibility"]
    user_id = request.form["id"]
    if books.save(book_title, author_name, user_id, info, visibility):
        return redirect("/")
    else:
        return render_template("error.html",message=" Kirjan tallentaminen ei onnistunut ")

@app.route("/")
def index():
    # palauttaa kaikki kirjat, jotka ovat julkisia
    list = books.get_books_as_a_list()
    return render_template("index.html", count=len(list), books=list)

@app.route("/myshelf")
def myshelf():
    # palauttaa kaikki kirjat, jotka ovat käyttäjän omia
    # id = session["user_id"]
    list = books.get_my_books_as_a_list()
    return render_template("myshelf.html", count=len(list), books=list)

# Uuden käyttäjän rekisteröiminen
@app.route("/register_new_user", methods=["GET","POST"])
def register_new_user():
    if request.method == "GET":
        return render_template("register_new_user.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 8 or len(username) > 20:
            return render_template("error.html", message = "Käyttäjätunnus on liian lyhyt(alle 8) tai pitkä (yli 30)")
        password = request.form["password"]
        if len(password) < 8 or len(password) > 20:
            return render_template("error.html", message = "Salasana on liian lyhyt(alle 8) tai pitkä (yli 30)")
            # Tallenetaan kaikki automaattisesti ei admineina
        if users.register_new_user(username,password,0):
            return redirect("/")
        else:
            return render_template("error.html",message="Käyttäjänimi saattaa olla käytössä, kokeile toista nimeä")

# Kirjautuminen sovellukseen
@app.route("/login_to_ShelfJournal", methods=["GET","POST"])
def login_to_ShelfJournal():
    # ohjataan käyttäjä kirjautumaan jos ei vielä kirjautunut
    if request.method == "GET":
        return render_template("login_to_ShelfJournal.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Jos kirjautuminen onnistuu, eli on true, näytetään pääsivu kokonaisuudessaan. Muuten virhesivu
        if users.login_to_ShelfJournal(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana. Ole hyvä ja kokeile uudelleen!")

# Kirjautuminen klubiin
@app.route("/login_to_club", methods=["POST"])
def login_to_club():
    if request.method == "POST":
        clubname = request.form["clubname"]
        password = request.form["password"]
        
        # Jos kirjautuminen onnistuu, eli on true, näytetään pääsivu kokonaisuudessaan. Muuten virhesivu
        if clubs.login_to_club(clubname, password):
            return redirect("/")
        else:
            return render_template("error.html",message="Kirjoititko varmasti salasanan oikein? Voit varmistaa sen klubin vetäjältä")


# Uloskirjautuminen
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

# Kirjan etsiminen
@app.route("/search")
def search():
    return render_template("search.html")

# Tiedon hakutoiminnot, toteutan ensin kirjan nimen perusteella haun
@app.route("/search_result", methods=["GET"])
def search_result():
    query = request.args["query"]
    list = books.search(query)
    return render_template("result.html",books=list)

@app.route("/search_result_from_author", methods=["GET"])
def search_result_from_author():
    query = request.args["query"]
    list = books.search_from_author(query)
    return render_template("result.html",books=list)

@app.route("/search_result_from_genre", methods=["GET"])
def search_result_from_genre():
    query = request.args["query"]
    list = books.search_from_genre(query)
    return render_template("result.html",books=list)

# tähän tulee tähdillä hakeminen    
@app.route("/search_result_with_stars/", methods=["GET"])
def search_result_with_stars():
    query = request.args["query"]
    list = reviews.get_all_public_reviews_with_stars(query)
    return render_template("reviews.html", reviews=list)
    
@app.route("/kirjantiedot/<int:id>", methods=["GET"])
def kirjantiedot(id):
    list = books.get_book(id)
    return render_template("book.html", id=id, book=list)

# Teen toiminnallisuuden näyttämään kirjan saamien arvioiden määrän ja keski-arvon
@app.route("/this_books_reviews/<int:id>", methods=["GET"])
def this_books_reviews(id):
    # kirjan id:llä etsitään sopivat arviot ja tehdään niillä asioita, eli lasketaan määrä ja keskiarvo
    list = reviews.get_amount_of_reviews(id)
    return render_template("books_review.html", id=id, book=list)


@app.route("/books_reviews/<int:id>", methods=["GET"])
def books_reviews(id):
    list = reviews.get_reviews(id)
    return render_template("reviews.html", review=list)



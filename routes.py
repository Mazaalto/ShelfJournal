from app import app
import users, books
from flask import redirect, render_template, request, session


# Kirjan lisaamista
@app.route("/register_new_book")
def register_new_book():
    return render_template("register_new_book.html")
        
# Kirjan tallentamista
# def save(book_title, author_name, user_id, info, visibility):
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
    id = session["user_id"]
    list = get_my_books_as_a_list(id)
    return render_template("myshelf.html", count=len(list), books=list)

#@app.route("/mybooks", methods=["GET"])
#def index2():
#    id = user_id = request.form["id"]
#    list = books.get_my_books_as_a_list(id)
#    return render_template("index.html", count=len(list), books=list)

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

@app.route("/kirjantiedot/<int:id>", methods=["GET"])
def kirjantiedot(id):
    list = books.get_book(id)
    return render_template("book.html", id=id, book=list)

@app.route("/kirjanarviointi/<int:id>", methods=["GET"])
def book_review(id):
    list = books.get_book(id)
    return render_template("review.html", id=id, book=list)

@app.route("/kirjanarvioinnit/<int:id>", methods=["GET"])
def get_book_reviews(id):
    list = books.get_book(id)
    return render_template("reviews.html", id=id, book=list)

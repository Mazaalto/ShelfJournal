from app import app
import users, books
from flask import redirect, render_template, request, session


# Kirjan liaamista
@app.route("/register_new_book")
def register_new_book():
    return render_template("register_new_book.html")
        
# tassa opettelen tallentamaan kirjaa, kuten oppimateriaalissa
@app.route("/registered_book", methods=["POST"])
def registered_book():
    book_title = request.form["book_title"]
    author_name = request.form["author_name"]
    # tahan tulee kategoria, jahka hakutoiminto toimii

    if books.save(book_title, author_name):
        return redirect("/")
    else:
        return render_template("error.html",message=" Kirjan tallentaminen ei onnistunut ")

@app.route("/")
def index():
    list = books.get_books_as_a_list()
    return render_template("index.html", count=len(list), books=list)

# uuden käyttäjän rekisteröiminen
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Käyttäjänimi saattaa olla käytössä, kokeile toista nimeä")

# Kirjautuminen sovellukseen
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana. Ole hyvä ja kokeile uudelleen!")

# Uloskirjautuminen
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

# Tiedon hakutoiminto
@app.route("/search_result", methods=["GET"])
def search_result():
    # query saa arvonsa sivun osoitteesta, sieltä tieto tänne
    # query = request.args["query"]
    # käytetään booksin metodia
    list = books.search()
    return render_template("result.html",books=list)

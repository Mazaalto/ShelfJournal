from app import app
import visits, messages, users
from flask import redirect, render_template, request, session


# Kirjan lisäämistä
@app.route("/register_new_book")
def register_new_book():
    return render_template("register_new_book.html")
        
# tässä opettelen tallentamaan kirjaa, kuten oppimateriaalissa
@app.route("/registered_book", methods=["POST"])
def registered_book():
    book_title = request.form["book_title"]
    author = request.form["author"]

    if books.save(book_title, author):
        print("uuden kirjan tallennus toimii")
        return redirect("/")
    else:
        return render_template("error.html",message="Kirjan tallentaminen ei onnistunut")

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    if messages.send(content):
        return redirect("/")
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")

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
            return render_template("error.html",message="Väärä tunnus tai salasana")

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
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
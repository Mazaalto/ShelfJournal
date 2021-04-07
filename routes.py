from app import app
import visits
from flask import redirect, render_template, request, session

@app.route("/")
def index():
    books = ["Syvä äly","Musashi","foundation"]
    # nyt message myös index.html:ssä
    return render_template("index.html",message="Tervetuloa!",items=books)

# Kirjan lisäämistä
@app.route("/register_new_book")
def register_new_book():
    return render_template("register_new_book.html")

@app.route("/registered_book", methods=["POST"])
def registered_book():
    book_name = request.form["book_name"]
    author_name = request.form["author_name"]
    return render_template("registered_book.html", book_name=book_name, author_name=author_name)

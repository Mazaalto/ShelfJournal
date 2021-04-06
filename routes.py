from app import app
import visits
from flask import redirect, render_template, request, session

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), books=list)


@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    if books.send(content):
        return redirect("/")
    else:
        return render_template("error.html",message="Kirjan tallennus ei onnistunut")

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

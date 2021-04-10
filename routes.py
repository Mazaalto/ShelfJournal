from app import app
import users, books
from flask import redirect, render_template, request, session


# Kirjan lisaamista
@app.route("/register_new_book")
def register_new_book():
    return render_template("register_new_book.html")
        
# Kirjan tallentamista
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
    # tahan tulee kategoria, jahka hakutoiminto toimii

    if books.save(book_title, author_name, info):
        return redirect("/")
    else:
        return render_template("error.html",message=" Kirjan tallentaminen ei onnistunut ")

@app.route("/")
def index():
    list = books.get_books_as_a_list()
    return render_template("index.html", count=len(list), books=list)

# Uuden käyttäjän rekisteröiminen
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 8 or len(username) > 20:
            return render_template("error.html", message = "Käyttäjätunnus on liian lyhyt(alle 8) tai pitkä (yli 30)")
        password = request.form["password"]
        if len(password) < 8 or len(password) > 20:
            return render_template("error.html", message = "Salasana on liian lyhyt(alle 8) tai pitkä (yli 30)")
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

# "/review_a_book" tähän tulee kirjan arvostelusivulle pääsy
@app.route("/review_a_book", methods=["GET"])
def review_a_book():
    return render_template("review_a_book.html)

# Tähän teen toiminnallisuuden listaamaan kaikki arvostelut
@app.route("/reviews_as_list")
def reviews_as_list():
    sql = "SELECT id, topic, created_at FROM review_as_stars ORDER BY id DESC"
    result = db.session.execute(sql)
    polls = result.fetchall()
    return render_template("reviews.html", review_as_stars=review_as_stars)

@app.route("/new")
def new():
    return render_template("new.html")

# tässä luodaan tähtiluokittelu kirjalle, tämä vasta runko
@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    sql = "INSERT INTO review_as_stars (topic, created_at) VALUES (:topic, NOW()) RETURNING id"
    result = db.session.execute(sql, {"topic":topic})
    review_as_stars_id = result.fetchone()[0]
    stars = request.form.getlist("stars")
    for star in stars:
        if star != "":
            sql = "INSERT INTO stars (review_as_stars_id, star) VALUES (:review_as_stars_id, :star)"
            db.session.execute(sql, {"review_as_stars_id":review_as_stars_id, "star":star})
    db.session.commit()
    return redirect("/reviews_as_list")

# Täällä pystyy arvioida kirjan
@app.route("/review_as_stars/<int:id>")
def review_as_stars(id):
    sql = "SELECT topic FROM review_as_stars WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT id, star FROM stars WHERE review_as_stars_id=:id"
    result = db.session.execute(sql, {"id":id})
    stars = result.fetchall()
    return render_template("review.html", id=id, topic=topic, stars=stars)

@app.route("/answer", methods=["POST"])
def answer():
    review_as_stars_id = request.form["id"]
    if "answer" in request.form:
        star_id = request.form["answer"]
        sql = "INSERT INTO reviews (star_id, sent_at) VALUES (:star_id, NOW())"
        db.session.execute(sql, {"star_id":choice_id})
        db.session.commit()
    return redirect("/result/"+str(review_as_stars_id))

@app.route("/result/<int:id>")
def result(id):
    sql = "SELECT topic FROM review_as_stars WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT s.star, COUNT(r.id) FROM stars c LEFT JOIN reviews r " \
          "ON s.id=r.star_id WHERE s.review_as_stars_id=:review_as_stars_id GROUP BY s.id"
    result = db.session.execute(sql, {"poll_id":id})
    stars = result.fetchall()
    return render_template("result.html", topic=topic, stars=stars)


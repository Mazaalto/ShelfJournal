# tähän tulee arvostelujen funktiot
from db import db
import users

# arvostelun lisääminen tietokantaan
def save_review(book_id, stars, text_review, visibility):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO reviews (book_id, stars, text_review, visibility, sent_at, user_id) VALUES (:book_id, :stars, :text_review, :visibility, NOW(), :user_id)"
    db.session.execute(sql, {"book_id":book_id, "stars":stars, "text_review":text_review, "visibility":visibility, "user_id":user_id})
    db.session.commit()
    return True
# tästä saa listauksen kirjan arvioinneista
def get_reviews(id):
    sql = "SELECT book_id, stars, text_review, visibility, sent_at, user_id FROM reviews WHERE book_id=:id"
    result = db.session.execute(sql, {"book_id":id})
    return result.fetchall()

def get_all_public_reviews():
    sql = "SELECT R.book_id, R.stars, R.text_review, R.visibility, R.sent_at, R.user_id FROM reviews R WHERE R.visibility='public' ORDER BY R.stars"
    result = db.session.execute(sql)
    return result.fetchall()

# ehdään yhdistelevä haku erikseen tänne, joka alkuun siis etsii kirjan nimen id:n perustella (seuraavaksi myös käyttäjän)
def get_all_public_reviews_proto():
    sql = "SELECT B.book_title, R.stars, R.text_review, R.visibility, R.sent_at, R.user_id FROM reviews R, books B WHERE R.visibility='public' AND R.book_id=B.id ORDER BY R.stars"
    result = db.session.execute(sql)
    return result.fetchall()

def get_all_public_reviews_proto_final():
    sql = "SELECT B.book_title, R.stars, R.text_review, R.visibility, R.sent_at, U.username FROM reviews R, books B, users U " \
        "WHERE R.visibility='public' AND R.book_id=B.id AND R.user_id=U.id ORDER BY R.stars"
    result = db.session.execute(sql)
    return result.fetchall()

# tehdään haku tähdillä tähän
def get_all_public_reviews_with_stars(query):
    sql = "SELECT B.book_title, R.stars, R.text_review, R.visibility, R.sent_at, U.username FROM reviews R, books B, users U " \
        "WHERE R.visibility='public' AND R.book_id=B.id AND R.user_id=U.id AND R.stars= :query"
    result = db.session.execute(sql, {"query":query})
    return result.fetchall()
    
# palauttaa määrän arvioista tietylle book_id:lle
def get_amount_of_reviews(id):
    sql = "SELECT COUNT(*) FROM reviews R WHERE R.visibility='public' AND R.book_id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

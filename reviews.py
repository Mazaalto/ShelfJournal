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


from db import db
import users

# Kirjat listaksi
def get_books_as_a_list():
    sql = "SELECT B.book_title, B.author_name, U.username, B.sent_at FROM books B, users U WHERE B.user_id=U.id ORDER BY B.id"
    result = db.session.execute(sql)
    return result.fetchall()

# Kirjan lisäys tietokantaan
def save(book_title, author_name):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO books (book_title, author_name, user_id, sent_at) VALUES (:book_title, :author_name, :user_id, NOW())"
    db.session.execute(sql, {"book_title":book_title, "author_name":author_name, "user_id":user_id})
    db.session.commit()
    return True

    #CREATE TABLE books (
    # id SERIAL PRIMARY KEY,
    # book_title TEXT,
    # author TEXT,
    # user_id INTEGER REFERENCES users,
    # sent_at TIMESTAMP

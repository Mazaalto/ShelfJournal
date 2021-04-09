from db import db
import users

# Kirjat listaksi
def get_books_as_a_list():
    sql = "SELECT B.book_title, B.author_name, U.username, B.sent_at FROM books B, users U WHERE B.user_id=U.id ORDER BY B.id"
    result = db.session.execute(sql)
    return result.fetchall()

# Kirjan lisäys tietokantaan
def save(book_title, author_name, info):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO books (book_title, author_name, user_id, sent_at, info) VALUES (:book_title, :author_name, :user_id, NOW(), :info)"
    db.session.execute(sql, {"book_title":book_title, "author_name":author_name, "user_id":user_id, "info":info})
    db.session.commit()
    return True

#Toteutettu kirjan etsintä nimen perusteella
def search(query):
    sql = "SELECT id, book_title, author_name FROM books WHERE book_title LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()

# Kirjan etsintä kirjailijan nimen perusteella
def search_from_author(query):
    sql = "SELECT id, book_title, author_name FROM books WHERE author_name LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()

    

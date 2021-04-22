from db import db
import users

# Kirjat listaksi
def get_books_as_a_list():
    # muutettu hakua niin että tulisi myös id, jotta voitaisiin arvioida kirjoja heti listauksesta ilman turhaa sivua   
    sql = "SELECT B.id, B.book_title, B.author_name, B.sent_at, B.visibility FROM books B, users U WHERE B.user_id=U.id AND B.visibility='public' ORDER BY B.book_title"
    result = db.session.execute(sql)
    return result.fetchall()

def get_my_books_as_a_list(id):
    # Toteutan tähän hakutoiminnallisuuden, missä haetaan vain omat kirjat 
    sql = "SELECT B.id, B.book_title, B.author_name, B.sent_at FROM books B, users U WHERE B.user_id=id ORDER BY B.id"
    result = db.session.execute(sql)
    return result.fetchall()

# Kirjan lisäys tietokantaan
def save(book_title, author_name, user_id, info, visibility):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO books (book_title, author_name, user_id, sent_at, info, visibility) VALUES (:book_title, :author_name, :user_id, NOW(), :info, :visibility)"
    db.session.execute(sql, {"book_title":book_title, "author_name":author_name, "user_id":user_id, "info":info, "visibility":visibility})
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

# Kirjan etsiminen genren perusteella
def search_from_genre(query):
    sql = "SELECT id, book_title, author_name, info FROM books WHERE info LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()

def get_book(id):
    sql = "SELECT id, book_title, author_name, user_id, sent_at, info FROM books WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()
    

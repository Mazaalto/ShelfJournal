from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

#Täällä kaikki käyttäjään liittyvät metodit

def login_to_ShelfJournal(username,password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    # jos käyttäjää ei löydy, palautetaan false
    if user == None:
        return False
    else:
        # werkzeugin valmisfuktio, joka laskee hajautusarvon
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            return True
        else:
            return False

def user_id():
    return session.get("user_id",0)

def logout():
    del session["user_id"]
    
def register_new_user(username,password, admin):
    # tietoturvan takia tallennetaan salasant hash-muodossa, tieto admin oikeudesta on 1 jos admin, muuten 0
    password_as_hash = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)"
        db.session.execute(sql, {"username":username,"password":password_as_hash,"admin":admin})
        db.session.commit()
    except:
        return False
    return login_to_ShelfJournal(username,password)



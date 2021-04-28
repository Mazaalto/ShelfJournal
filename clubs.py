# tähän tulee ryhmien oma tiedosto
from db import db
import users

# Klubin lisäys tietokantaan. Myöhemmin tehdään toisella tietokantataululla jäsenistön hallinta.
def save_club(club_title, club_info, club_password, user_id, visibility):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO clubs (club_title, club_info, club_password, user_id, visibility) VALUES (:club_title, :club_info, :club_password, :user_id, :visibility)"
    db.session.execute(sql, {"club_title":club_title, "club_info":club_info, "club_password":club_password, "user_id":user_id, "visibility":visibility})
    db.session.commit()
    return True

def get_clubs_as_a_list():   
    sql = "SELECT C.id, C.club_title, C.club_info, C.club_password, C.visibility FROM clubs C WHERE C.visibility='public'"
    result = db.session.execute(sql)
    return result.fetchall()
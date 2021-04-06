def get_list():
    sql = "SELECT M.content, U.username, M.sent_at FROM messages M, users U" \
          "WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(sql)
    return result.fetchall()

def send(content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO books (content, user_id, sent_at) VALUES (:content, :user_id, NOW())"
    db.session.execute(sql, {"content":content, "user_id":user_id})
    db.session.commit()
    return True


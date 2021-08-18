from db import db

def get_user_by_username(username):
    result = db.session.execute(
        "SELECT * FROM users WHERE username=:username",
        { "username": username }
    )
    return result.fetchone()

def get_users_like(search):
    if not isinstance(search, str):
        return []

    result = db.session.execute(
        "SELECT * FROM users WHERE username LIKE :search",
        { "search": "%" + search + "%" }
    )
    return result.fetchall()

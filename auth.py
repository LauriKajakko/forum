from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def login(username, password):
    result = db.session.execute(
        "SELECT id, password_hash FROM users WHERE username=:username",
        { "username": username }
    )
    user = result.fetchone()
    if not user:
        return False
    if check_password_hash(user.password_hash, password):
        session["user_id"] = user.id
        return True
    return False

def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]

def register(username, password):
    try:
        db.session.execute(
            "INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)",
            {
                "username": username,
                "password_hash": generate_password_hash(password)
            }
        )
        db.session.commit()
    except:
        return False
    return login(username, password)

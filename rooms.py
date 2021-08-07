from flask import session
from db import db

def get_rooms():
    result = db.session.execute("SELECT name, description, created_at FROM rooms WHERE status='public'")
    return result.fetchall()    

def create_room(name, description, status, user_id):
    try:
        db.session.execute(
            "INSERT INTO rooms (name, description, status, created_at, user_id) "
            + "VALUES (:name, :description, :status, NOW(), :user_id)",
            {
                "name": name,
                "description": description,
                "status": status,
                "user_id": user_id,
            }
        )
        db.session.commit()
    except:
        return False
    return True

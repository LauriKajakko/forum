from db import db

def get_room(room_id):
    try:
        result = db.session.execute(
        "SELECT * FROM rooms WHERE id=:id",
        { "id": room_id }
        )
        return result.fetchone()
    except:
        return None

def get_rooms():
    result = db.session.execute("SELECT * FROM rooms WHERE status='public'")
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

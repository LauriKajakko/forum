from db import db

def create_thread(name, room_id):
    try:
        db.session.execute(
            "INSERT INTO threads(name, room_id) VALUES (:name, :room_id)",
            {
                "name": name,
                "room_id": room_id,
            }
        )
        db.session.commit()
        return True
    except:
        return False

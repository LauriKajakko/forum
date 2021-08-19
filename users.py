from db import db

def get_user_by_username(username):
    result = db.session.execute(
        "SELECT * FROM users WHERE username=:username",
        { "username": username }
    )
    return result.fetchone()

def get_admins_by_room(room_id):
    result = db.session.execute(
        "SELECT DISTINCT users.id, users.username "
        + "FROM users LEFT JOIN room_admins "
        + "ON room_admins.room_id=:room_id",
        { "room_id": room_id }
    )
    return result.fetchall()

def check_admin_status(user_id, room_id):
    result = db.session.execute(
        "SELECT 1 FROM room_admins WHERE user_id=:user_id AND room_id=:room_id",
        {
            "user_id": user_id,
            "room_id": room_id
        }
    )

    return result.fetchone() is not None

def get_users_like(search):
    if not isinstance(search, str):
        return []

    result = db.session.execute(
        "SELECT * FROM users WHERE username LIKE :search",
        { "search": "%" + search + "%" }
    )
    return result.fetchall()

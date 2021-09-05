from db import db


def get_user_by_username(username):
    result = db.session.execute(
        "SELECT u.id, u.username, "
        + "COUNT(DISTINCT m.id) as message_count, "
        + "COUNT(DISTINCT r.id) as room_count, "
        + "COUNT(DISTINCT ra.room_id) as admin_count "
        + "FROM users as u "
        + "LEFT JOIN messages as m "
        + "ON m.user_id=u.id "
        + "LEFT JOIN rooms as r "
        + "ON r.user_id=u.id "
        + "LEFT JOIN room_admins as ra "
        + "ON ra.user_id=u.id "
        + "WHERE username=:username "
        + "GROUP BY u.id",
        {"username": username}
    )
    return result.fetchone()


def get_admins_by_room(room_id):
    result = db.session.execute(
        "SELECT DISTINCT users.id, users.username "
        + "FROM users LEFT JOIN room_admins "
        + "ON room_admins.user_id=users.id "
        + "WHERE room_id=:room_id",
        {"room_id": room_id}
    )
    return result.fetchall()


def check_admin_status(user_id, room_id):
    result = db.session.execute(
        "SELECT 1 FROM room_admins WHERE user_id=:user_id AND room_id=:room_id", {
            "user_id": user_id, "room_id": room_id})
    return result.fetchone() is not None


def get_users_like(search):
    if not isinstance(search, str):
        return []

    result = db.session.execute(
        "SELECT * FROM users WHERE username LIKE :search",
        {"search": "%" + search + "%"}
    )
    return result.fetchall()

from db import db


def get_threads(room_id, skips):
    result = db.session.execute(
        "SELECT t.id, t.name, json_agg(json_build_array(m.content, u.username)) as messages, " +
        "(SELECT COUNT(id) FROM threads WHERE room_id=:room_id) as count " +
        "FROM threads as t " +
        "LEFT JOIN messages as m " +
        "ON m.thread_id=t.id " +
        "LEFT JOIN users as u " +
        "ON m.user_id=u.id " +
        "WHERE room_id=:room_id " +
        "GROUP BY t.id " +
        "OFFSET :skips " +
        "LIMIT 1 ",
        {
            "room_id": room_id,
            "skips": skips
        }
    )
    return result.fetchall()


def create_thread(name, room_id):
    try:
        db.session.execute(
            "INSERT INTO threads (name, room_id, created_at) VALUES (:name, :room_id, NOW())",
            {"name": name, "room_id": room_id, })
        db.session.commit()
        return True
    except:
        return False

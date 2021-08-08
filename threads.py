from db import db

def get_threads(room_id):
    result = db.session.execute(
        "SELECT threads.*, json_agg(json_build_array(messages.content, users.username)) as messages "
        + "FROM threads "
        + "LEFT JOIN messages "
        + "ON messages.thread_id=threads.id "
        + "LEFT JOIN users "
        + "ON messages.user_id=users.id "
        + "WHERE room_id=:room_id "
        + "GROUP BY threads.id ",
        { "room_id": room_id }
    )
    return result.fetchall()

def create_thread(name, room_id):
    try:
        db.session.execute(
            "INSERT INTO threads (name, room_id, created_at) VALUES (:name, :room_id, NOW())",
            {
                "name": name,
                "room_id": room_id,
            }
        )
        db.session.commit()
        return True
    except:
        return False

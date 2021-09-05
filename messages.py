from db import db


def create_message(content, thread_id, user_id):
    try:
        db.session.execute(
            "INSERT INTO messages (content, thread_id, user_id, created_at) "
            + "VALUES (:content, :thread_id, :user_id, NOW())",
            {
                "content": content,
                "thread_id": thread_id,
                "user_id": user_id,
            }
        )
        db.session.commit()
        return True
    except:
        return False

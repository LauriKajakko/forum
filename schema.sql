CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
	password_hash TEXT
);

CREATE TABLE IF NOT EXISTS rooms (
  id SERIAL PRIMARY KEY,
  name TEXT,
  description TEXT,
  status ROOM_STATUS,
  created_at TIMESTAMP,
  user_id INTEGER REFERENCES users
);

CREATE TABLE IF NOT EXISTS room_admins (
  user_id INTEGER REFERENCES users,
  room_id INTEGER REFERENCES rooms
);

CREATE TABLE IF NOT EXISTS threads (
  id SERIAL PRIMARY KEY,
  name TEXT,
  room_id INTEGER REFERENCES rooms,
  created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS messages (
  id SERIAL PRIMARY KEY,
  content TEXT,
  thread_id INTEGER REFERENCES threads,
  user_id INTEGER REFERENCES users,
  created_at TIMESTAMP
);

ALTER TABLE room_admins
ADD CONSTRAINT no_duplicate_admins
UNIQUE (user_id, room_id);
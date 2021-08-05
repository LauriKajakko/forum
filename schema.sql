CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
	password_hash TEXT
);

DO $$ BEGIN
    CREATE TYPE room_status AS ENUM ('public', 'private');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

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
  created_at TIMESTAMP
);
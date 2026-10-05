import sqlite3
from contextlib import closing
from pathlib import Path


def connect_to_db():
    conn = sqlite3.connect(Path(__file__).with_name("database.db"))
    conn.row_factory = sqlite3.Row
    return conn


def create_db_table():
    with closing(connect_to_db()) as conn, conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            )
        """)


def insert_user(user):
    with closing(connect_to_db()) as conn, conn:
        cur = conn.execute(
            "INSERT INTO users (name, email, phone, address, country) "
            "VALUES (?, ?, ?, ?, ?)",
            (user["name"], user["email"], user["phone"],
             user["address"], user["country"]),
        )
        user_id = cur.lastrowid
    return get_user_by_id(user_id)


def get_users():
    with closing(connect_to_db()) as conn:
        rows = conn.execute("SELECT * FROM users").fetchall()
        return [dict(row) for row in rows]


def get_user_by_id(user_id):
    with closing(connect_to_db()) as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row else {}


def update_user(user):
    with closing(connect_to_db()) as conn, conn:
        conn.execute(
            "UPDATE users SET name = ?, email = ?, phone = ?, "
            "address = ?, country = ? WHERE user_id = ?",
            (user["name"], user["email"], user["phone"],
             user["address"], user["country"], user["user_id"]),
        )
    return get_user_by_id(user["user_id"])


def delete_user(user_id):
    try:
        with closing(connect_to_db()) as conn, conn:
            conn.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        return {"status": "User deleted successfully"}
    except sqlite3.Error:
        return {"status": "Cannot delete user"}


if __name__ == "__main__":
    create_db_table()

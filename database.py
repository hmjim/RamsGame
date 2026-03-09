import sqlite3


def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, wins INTEGER DEFAULT 0)'
    )
    conn.close()


def get_top():
    conn = sqlite3.connect('users.db')
    res = conn.execute(
        'SELECT username, wins FROM users ORDER BY wins DESC LIMIT 10'
    ).fetchall()
    conn.close()
    return res


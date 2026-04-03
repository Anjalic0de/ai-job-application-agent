import sqlite3

def get_user():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users LIMIT 1")
    user = cursor.fetchone()

    conn.close()

    return user
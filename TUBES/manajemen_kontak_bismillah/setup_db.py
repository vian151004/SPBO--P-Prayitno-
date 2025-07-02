import sqlite3
from konfigurasi import DB_PATH

def setup_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kontak (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            telepon TEXT NOT NULL,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Database siap!")

if __name__ == "__main__":
    setup_db()

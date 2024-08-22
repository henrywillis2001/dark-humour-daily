import sqlite3

def initialize_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS thoughts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thought TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized with 'thoughts' table.")

if __name__ == "__main__":
    initialize_db()

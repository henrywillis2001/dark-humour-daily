import sqlite3
from datetime import datetime

def update_joke(new_joke):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS thoughts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thought TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert new joke into the table
    cursor.execute('INSERT INTO thoughts (thought) VALUES (?)', (new_joke,))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    joke = input("Enter today's joke: ")
    update_joke(joke)
    print("Joke updated successfully.")

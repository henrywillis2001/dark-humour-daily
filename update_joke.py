import sqlite3

def update_joke(new_joke):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM thoughts')
    c.execute('INSERT INTO thoughts (thought) VALUES (?)', (new_joke,))
    conn.commit()
    conn.close()
    print("Joke updated successfully!")

if __name__ == "__main__":
    new_joke = input("Enter the new joke: ")
    update_joke(new_joke)

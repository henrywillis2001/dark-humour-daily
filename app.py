from flask import Flask, render_template
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    thought = conn.execute('SELECT thought FROM thoughts ORDER BY id DESC LIMIT 1').fetchone()
    conn.close()

    current_date = datetime.now().strftime("%B %d, %Y")

    return render_template('index.html', thought=thought['thought'] if thought else "No joke available!", current_date=current_date)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Use PORT environment variable
    app.run(host='0.0.0.0', port=port, debug=False)  # Bind to all network interfaces

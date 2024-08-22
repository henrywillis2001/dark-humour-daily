from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/update_joke', methods=['POST'])
def update_joke():
    new_joke = request.form['joke']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO thoughts (thought) VALUES (?)', (new_joke,))
    
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


"""https://dark-humour-daily.onrender.com/"""
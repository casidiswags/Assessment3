# In your app.py
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def gym():
    return render_template('gym.html')

@app.route('/powerlift')
def powerlift():
    try:
        with sqlite3.connect('gym.db') as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            # Fetch data from powerlift table
            cur.execute("SELECT * FROM powerlift")
            powerlift_rows = cur.fetchall()
    except sqlite3.Error as e:
        # Handle database error
        return render_template('error.html', error_message=f"Database error: {e}")

    return render_template('powerlift.html', powerlift_rows=powerlift_rows)

@app.route('/meets')
def meets():
    try:
        with sqlite3.connect('gym.db') as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()

            # Fetch data from meets_data table
            cur.execute("SELECT * FROM meets_data")
            meets_data_rows = cur.fetchall()
    except sqlite3.Error as e:
        # Handle database error
        return render_template('error.html', error_message=f"Database error: {e}")

    return render_template('meets.html', meets_data_rows=meets_data_rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect("health_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            weight REAL,
            steps INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect("health_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health_data")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_entry():
    date = request.form["date"]
    weight = request.form["weight"]
    steps = request.form["steps"]

    conn = sqlite3.connect("health_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO health_data (date, weight, steps) VALUES (?, ?, ?)", (date, weight, steps))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
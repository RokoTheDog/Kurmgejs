from flask import Flask, render_template, request, redirect
import sqlite3
import helpers

app = Flask(__name__)

def create_connection():
    conn = sqlite3.connect('users.db')  
    return conn
def create_user_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
def insert_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, password))
    conn.commit()
def retrieve_user(conn, username, password):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username=? AND password=?
    ''', (username, password))
    return cursor.fetchone()

@app.route("/", methods=['GET'])
def index():
    filter = request.args.get('filtertext', default="")
    table = helpers.get_data_gov_lv()
    return render_template("data.html", table=table)
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['register_username']
        password = request.form['register_password']
        print("meginajums")
        conn = create_connection()
        create_user_table(conn)
        insert_user(conn, username, password)
        conn.close()
        return redirect('/')
@app.route("/login", methods=['POST'])
def login():
    username = request.form['login_username']
    password = request.form['login_password']
    conn = create_connection()
    user = retrieve_user(conn, username, password)
    conn.close()
    if user:
        return redirect('/')  
    else:
        return redirect('/register') 
        return render_template("register.html")
@app.route("/favourites")
def favourites():
    return render_template("favourites.html")
@app.route("/about")
def aboutus():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(debug=True)
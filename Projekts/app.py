from flask import Flask, render_template, request, redirect, session
import sqlite3
import helpers

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods=['GET'])
def index():
    if 'username' in session:
        filter = request.args.get('filtertext', default="")
        table = helpers.get_data_gov_lv()
        return render_template("data.html", table=table)
    else:
        return redirect("/register")
q1 = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pass TEXT
        );
    """
q2 = "INSERT INTO users (name, pass) VALUES (?, ?);"
q3 = "SELECT * FROM users WHERE name=?"


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        c.execute(q1)
        c.execute(q2, (username, password) )
        conn.commit()
        conn.close()
        session['username']= username
        return redirect("/")
    user = session.get("username", None)
    return render_template("register.html", user=user)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        c.execute(q3, (username,))
        rows = c.fetchall()
        if len( rows ) > 0:
            #print( rows[0][2] )
            if password==rows[0][2]:
                session['username'] = username
                print("Login success")
                return redirect("/")
            else:
                print("Password does not match")
        else:
            print("User does not exist")
    return render_template("register.html", session=session)
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/register")
@app.route("/favourites")
def favourites():
    return render_template("favourites.html")
@app.route("/about")
def aboutus():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(debug=True, port=8000)
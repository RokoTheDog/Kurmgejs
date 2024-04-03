from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import helpers

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route("/", methods=['GET', 'POST'])
def index():
    if 'username' in session:
        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        if request.method == 'POST':
            if 'clear' in request.form:
                nosaukums = MinWage = MaxWage = Location = ''
                c.execute("UPDATE filters SET nosaukums = ?, MinWage = ?, MaxWage = ?, Location = ? WHERE user_id = (SELECT id FROM users WHERE name = ?);", (nosaukums, MinWage, MaxWage, Location, session['username']))
            else:
                nosaukums = request.form.get('nosaukums')
                MinWage = request.form.get('MinWage')
                MaxWage = request.form.get('MaxWage')
                Location = request.form.get('Location')
                c.execute("UPDATE filters SET nosaukums = ?, MinWage = ?, MaxWage = ?, Location = ? WHERE user_id = (SELECT id FROM users WHERE name = ?);", (nosaukums, MinWage, MaxWage, Location, session['username']))
        elif request.method == 'GET':
            c.execute("SELECT nosaukums, MinWage, MaxWage, Location FROM filters WHERE user_id = (SELECT id FROM users WHERE name = ?);", (session['username'],))
            row = c.fetchone()
            if row:
                nosaukums, MinWage, MaxWage, Location = row
            else:
                nosaukums = MinWage = MaxWage = Location = ''
        conn.commit()
        conn.close()
        table = helpers.get_data_gov_lv(nosaukums, MinWage, MaxWage, Location)
        return render_template("data.html", table=table, nosaukums=nosaukums, MinWage=MinWage, MaxWage=MaxWage, Location=Location)

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
q4 = """
    CREATE TABLE IF NOT EXISTS filters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        nosaukums TEXT,
        MinWage INTEGER,
        MaxWage INTEGER,
        Location TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
"""

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        next_url = request.args.get("next")
        if next_url is not None:
            session["next"] = next_url
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        terms_accepted = request.form.get("terms") == "on"
        if not terms_accepted:
            return render_template("register.html", user=session.get("username", None), error2="You must accept the terms and conditions to register")
        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        c.execute(q1)
        c.execute(q3, (username,))
        user_exists = c.fetchone()
        if user_exists:
            return render_template("register.html", user=session.get("username", None), error2="Username already exists")
        c.execute(q2, (username, password))
        user_id = c.lastrowid  # Get the id of the newly created user
        c.execute(q4)  # Create the filters table if it doesn't exist
        c.execute("INSERT INTO filters (user_id) VALUES (?);", (user_id,))
        conn.commit()
        conn.close()
        session['username']= username
        return redirect(session.get('next', '/'))
    return render_template("register.html", user=session.get("username", None), error2=None)
@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "GET":
        next_url = request.args.get("next")
        if next_url is not None:
            session["next"] = next_url
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conn = sqlite3.connect("login.db")
        c = conn.cursor()
        c.execute(q3, (username,))
        rows = c.fetchall()
        if len( rows ) > 0:
            if password==rows[0][2]:
                session['username'] = username
                return redirect(session.get('next', '/'))
            else:
                error = "Password does not match"
        else:
            error = "User does not exist"
    return render_template("register.html", session=session, error=error)
@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('next', None)
    return redirect(url_for('register', next='/'))
@app.route("/favourites")
def favourites():
    return render_template("favourites.html")

@app.route('/about')
def about():
    if 'username' not in session:
        return redirect(url_for('login', next=request.url))
    else:
        return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True, port=8000)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/favourites")
def favourites():
    return render_template("favourites.html")
@app.route("/about")
def aboutus():
    return render_template("about.html")

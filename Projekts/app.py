from flask import Flask, render_template, request
import helpers

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/favourites")
def favourites():
    return render_template("favourites.html")
@app.route("/about")
def aboutus():
    return render_template("about.html")
@app.route("/data", methods=['GET'])
def data():
    filter = request.args.get('filtertext', default="")
    table = helpers.get_data_gov_lv(filter)
    return render_template("data.html", table=table)
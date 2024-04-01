from flask import Flask, render_template, request

import helpers

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    nosaukums = request.form.get('nosaukums') if request.method == 'POST' else None
    MinWage = request.form.get('MinWage') if request.method == 'POST' else None
    MaxWage = request.form.get('MaxWage') if request.method == 'POST' else None  # fixed typo here
    Location = request.form.get('Location') if request.method == 'POST' else None
    table = helpers.get_data_gov_lv(nosaukums, MinWage, MaxWage, Location)
    return render_template("data.html", table=table)

@app.route("/register")

def register():

    return render_template("register.html")

@app.route("/favourites")

def favourites():

    return render_template("favourites.html")

@app.route("/about")

def aboutus():

    return render_template("about.html")

from flask import Flask, render_template, request

import helpers

app = Flask(__name__)

@app.route("/", methods=['GET'])

def index():

    filter = request.args.get('filtertext', default="")

    table = helpers.get_data_gov_lv()

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
from flask import Flask, render_template, request

import helpers

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nosaukums = request.form.get('nosaukums')
    else:
        nosaukums = None
    
    table = helpers.get_data_gov_lv(nosaukums)

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

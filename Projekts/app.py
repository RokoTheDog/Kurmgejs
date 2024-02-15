from flask import Flask
import json
import requests
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

resp = requests.get("https://data.gov.lv/dati/dataset/cb6831cb-1d89-44a3-b889-b43c411df4fe/resource/7f68f6fc-a0f9-4c31-b43c-770e97a06fda/download/vakances-2024-02-15.csv")
#a = resp.json()
#print(resp)
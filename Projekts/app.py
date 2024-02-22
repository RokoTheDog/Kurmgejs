from flask import Flask, render_template, request
import requests
import csv
from tabulate import tabulate

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
@app.route("/login")
def login():
    return render_template("login.html")



file = requests.get("https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=7f68f6fc-a0f9-4c31-b43c-770e97a06fda&limit=5000")
file = file.json()
records=file['result']['records']
headers=['Vakances nosaukums','Alga no','Alga līdz']
data=[]
for rec in records:
    data.append(rec['Vakances nosaukums'],rec['Alga no'],rec['Alga līdz'])
print(tabulate(data,headers,tablefmt='grid'))

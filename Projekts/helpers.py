import sqlite3
import requests
import json

def get_data_gov_lv():
    url = requests.get('https://data.gov.lv/dati/lv/api/3/action/datastore_search_sql?sql=SELECT * from "7f68f6fc-a0f9-4c31-b43c-770e97a06fda" ORDER BY _id')
    url = url.json()
    records = url["result"]["records"]
    table = "<table><tr><th>ID</th><th>Vakances Nosaukums</th><th>Alga no</th><th>Alga līdz</th><th>Pieteikšanās Termiņš</th><th>Vieta</th><th>Vairāk Informācijas</th></tr>"
    for row in records:
        table += "<tr>"
        table += "<td>"+str(row["_id"])+"</td>"
        table += "<td>"+row["Vakances nosaukums"]+"</td>"
        table += "<td>"+str(row["Alga no"])+"</td>"
        table += "<td>"+str(row["Alga līdz"])+"</td>"
        table += "<td>"+row["Pieteikšanās termiņš"]+"</td>"
        table += "<td>"+row["Vieta"]+"</td>"
        table += "<td><a href="+row["Vakances paplašināts apraksts"]+">More info</td>"
        table += "</tr>"
    table += "</table>"
    return table
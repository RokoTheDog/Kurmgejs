import sqlite3
import requests
import json
from flask import request

def get_data_gov_lv(nosaukums=None):
    #filtrs[]=insert(nosaukums)
    base_url = 'https://data.gov.lv/dati/lv/api/3/action/datastore_search_sql?sql='
    
    if nosaukums is not None:
        # Enclose the nosaukums variable in single quotes
        query = 'SELECT * FROM "7f68f6fc-a0f9-4c31-b43c-770e97a06fda" WHERE "Vakances nosaukums" LIKE \'' + nosaukums + '%' + '\' ORDER BY _id'
        url = base_url + requests.utils.quote(query)
    else:
        query = 'SELECT * FROM "7f68f6fc-a0f9-4c31-b43c-770e97a06fda" ORDER BY _id'
        url = base_url + requests.utils.quote(query)

    #print(url)
    response = requests.get(url)
    #print(response)
    data = response.json()


    records = data['result']['records']
    #print(records)
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
get_data_gov_lv("ATKRITUMU")
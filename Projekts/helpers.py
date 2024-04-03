import sqlite3
import requests
import json
from flask import request

def get_data_gov_lv(nosaukums=None,MinWage=None,MaxWage=None,Location=None):
    start_url = 'https://data.gov.lv/dati/lv/api/3/action/datastore_search_sql?sql=SELECT * FROM "7f68f6fc-a0f9-4c31-b43c-770e97a06fda"'
    end_url = ' ORDER BY _id'
    query = start_url
    conditions = []
    if nosaukums:
        conditions.append(f' LOWER("Vakances nosaukums") LIKE \'%{nosaukums.lower()}%\'')
    if MinWage:
        conditions.append(f' "Alga no" >= {MinWage}')
    if MaxWage:
        conditions.append(f' "Alga līdz" <= {MaxWage}')
    if Location:
        conditions.append(f' LOWER("Vieta") LIKE \'%{Location.lower()}%\'')
    if conditions:
        query += ' WHERE' + ' AND'.join(conditions)
    url = query + end_url
    print(url)
    response = requests.get(url)
    data = response.json()


    records = data['result']['records']
    #print(records)
    table = "<table><tr><th>ID</th><th>Vakances Nosaukums</th><th>Alga no</th><th>Alga līdz</th><th>Pieteikšanās Termiņš</th><th>Vieta</th><th>Vairāk Informācijas</th></tr>"
    for row in records:
        #print(row)Fprint
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
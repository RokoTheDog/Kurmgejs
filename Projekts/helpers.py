import sqlite3
import requests
import csv

def get_data_gov_lv(filter):
    url = "https://data.gov.lv/dati/dataset/cb6831cb-1d89-44a3-b889-b43c411df4fe/resource/7f68f6fc-a0f9-4c31-b43c-770e97a06fda/download/"
    response = requests.get(url)
    response.encoding = 'utf-8'
    lines = response.text.splitlines()
    rows = csv.DictReader( lines )
    print(rows)
    return ""
    table = "<table><tr><th>ID</th><th>Kods</th><th>Nosaukums</th><th>Adrese</th></tr>"
    for row in rows:
        table += "<tr>"
        for i in range(len(row)):
            table += "<td>"+str(row[i])+"</td>"
        table += "</tr>"
    table += "</table>"
    return table
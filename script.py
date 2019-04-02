# script.py
import requests
import ast
import psycopg2
import datetime


def request_rates():
    APP_ID = 'ccde7c3d874247a7a12dd01c4dce5ea2'
    a = requests.get('https://openexchangerates.org/api/latest.json?app_id=' + APP_ID)

    data = ast.literal_eval(a.text)
    rates = data.get('rates')
    return rates


def show_table():
    cur.execute("SELECT * FROM currency_currency")
    rows = cur.fetchall()
    for row in rows:
        print(row)


rates = request_rates()
USD = 1.0
EUR = rates.get('EUR')
CZK = rates.get('CZK')
PLN = rates.get('PLN')
print("costs: ", USD, EUR, PLN, CZK)

conn = psycopg2.connect("dbname=currency_db user=postgres password=1234 host=localhost")
cur = conn.cursor()

cur.execute("""
    INSERT INTO currency_currency (usd_cost, euro_cost, czk_cost, pln_cost, pub_date) VALUES (%s, %s, %s, %s, %s);
    """,
    (USD, EUR, CZK, PLN, datetime.datetime.today() ))

conn.commit()

cur.close()
conn.close()

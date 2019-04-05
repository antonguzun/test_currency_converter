# script2.py
# crontab use this script for update currencies courses
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Date, Float
import requests
import ast
import datetime


def request_rates():
    APP_ID = 'ccde7c3d874247a7a12dd01c4dce5ea2'
    a = requests.get('https://openexchangerates.org/api/latest.json?app_id=' + APP_ID)
    data = ast.literal_eval(a.text)
    rates = data.get('rates')
    return rates


def delete_row(id, conn):
    conn.execute(currency_currency.delete().where(currency_currency.c.id == id))


def show_table(conn):
    stmt = conn.execute(currency_currency.select())
    for row in stmt:
        print(row)


rates = request_rates()
USD = 1.0                   # the base currency
EUR = rates.get('EUR')
CZK = rates.get('CZK')
PLN = rates.get('PLN')

meta = MetaData()
currency_currency = Table(
    'currency_currency', meta,
    Column('id', Integer, primary_key=True),
    Column('usd_cost', Float, nullable=False),
    Column('euro_cost', Float, nullable=False),
    Column('czk_cost', Float, nullable=False),
    Column('pln_cost', Float, nullable=False),
    Column('pub_date', Date, nullable=False)
)

engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/currency_db')
conn = engine.connect()
conn.execute(currency_currency.insert().values(usd_cost=USD,
                                               euro_cost=EUR,
                                               czk_cost=CZK,
                                               pln_cost=PLN,
                                               pub_date=datetime.datetime.today()
                                               )
             )
#show_table(conn)

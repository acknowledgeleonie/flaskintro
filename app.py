from flask import Flask
import pandas as pd
from flask_cors import CORS

import felix
import leonie
import evi
import robert
import tonie
import rasoel

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/cbs/count")
def cbs_api_count():
    df = pd.read_csv("CBS_Detailhandel_omzetontwikkeling.csv")
    return str(len(df))

<<<<<<< HEAD
=======
@app.route("/api/cbs/index/<index>")
def cbs_api_index(index):
    try:
        index = int(index)
    except ValueError:
        return "Vul a.u.b. een geheel getal in"

    df = pd.read_csv("CBS_Detailhandel_omzetontwikkeling.csv")
    
    if index < 0 or index >= len(df):
        return f"Vul a.u.b. een geheel getal in tussen de 0 en {len(df) - 1}"

    return str(df.iloc[index])
>>>>>>> main

@app.route("/felix")
def methodefelix():
    return felix.methodevanfelix()


@app.route("/leonie")
def methodeleonie():
    return leonie.methodevanleonie()

@app.route("/evi")
def methodeevi():
    return evi.methodevanevi()

@app.route("/robert")
def methoderobert():
    return robert.methodevanrobert()

@app.route("/tonie")
def methodetonie():
    return tonie.methodevantonie()

@app.route("/rasoel")
def methoderasoel():
    return rasoel.methodevanrasoel()

@app.route("/freek")
def methodefreek():
    return "Freek"
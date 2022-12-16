from flask import Flask
import pandas as pd
import felix
import leonie
import evi
import robert
import tonie
import rasoel

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/cbs/count")
def cbs_api_count():
    df = pd.read_csv("CBS_Detailhandel_omzetontwikkeling.csv")
    return str(len(df))


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
from flask import Flask, render_template, Markup
from utils import get_outside_temp
from broke_test import hourly_forecast
import pandas as pd


app = Flask(__name__)


@app.route('/')
def hello_world():
    boston_temp = get_outside_temp("7c5e200a31d7dcd5e40cbbf4de0f37e7", 42.3566424, -71.0644743)
    forecast = Markup(hourly_forecast())

    return render_template("dash.html", temp=boston_temp, plot=forecast)

@app.route('/dash')
def render_dash():
    df = pd.read_csv("./hourly_forecast.csv")
    header = df.columns
    data = df.get_values()
    return render_template("dashboard.html", header=header, data=data, plot=Markup(hourly_forecast()))

if __name__ == '__main__':
    app.run()

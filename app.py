import time
import threading

import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, render_template, Markup

from mercury import *
from utils import get_outside_temp
from broke_test import plot_temps

app = Flask(__name__)


@app.before_first_request
def activate_job():
    def run_job():
        while True:
            create_mock_data()
            time.sleep(10)

    thread = threading.Thread(target=run_job)
    thread.start()

# boston_temp = get_outside_temp("7c5e200a31d7dcd5e40cbbf4de0f37e7", 42.3566424, -71.0644743)

@app.route('/')
def render_dash():

    #when you import the mercury package the database is created in the cwd not in the package directory...i think this is okay
    engine = create_engine("sqlite:///temps.db")

    plot = plot_temps("./test_data.csv")

    df = pd.read_sql_query("SELECT * FROM envtemps", engine).sort_values("datetime", ascending=False).head(10)
    header = df.columns
    data = df.get_values()
    return render_template("temp_dash.html", header=header, data=data, plot=Markup(plot))

if __name__ == '__main__':
    app.run()

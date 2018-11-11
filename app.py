import time
import threading

import pandas as pd
from flask import Flask, render_template, Markup

from mercury import *
from broke_test import plot_temps

app = Flask(__name__)


@app.before_first_request
def activate_job():
    def run_job():
        while True:
            get_current_conditions()
            # sleep 30 mins
            time.sleep(1800)

    thread = threading.Thread(target=run_job)
    thread.start()

@app.route('/')
def render_dash():

    #when you import the mercury package the database is created in the cwd not in the package directory...i think this is okay
    engine = create_engine("sqlite:///temps.db")

    temp_data = pd.read_sql_query("SELECT * FROM envtemps", engine)

    plot = plot_temps(temp_data)

    df = temp_data.sort_values("datetime", ascending=False).head(10)
    header = df.columns
    data = df.get_values()
    return render_template("temp_dash.html", header=header, data=data, plot=Markup(plot))

if __name__ == '__main__':
    app.run()

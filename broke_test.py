import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.embed import file_html
from bokeh.resources import CDN



def hourly_forecast():
    df = pd.read_csv("hourly_forecast.csv")

    def datetime(x):
        return np.array(x, dtype=np.datetime64)

    p1 = figure(plot_width=500, plot_height=250, x_axis_type="datetime", title="Hourly Forecast")
    p1.grid.grid_line_alpha = 0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Temp'

    p1.line(datetime(df['date']), df['temp'], color='#FB9A99', legend='Temperature (fahrenheit)')
    p1.legend.location = "top_right"

    return file_html(p1, CDN, "temp.html")

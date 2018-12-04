import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.embed import file_html
from bokeh.resources import CDN

def plot_temps(df, title="Temperature Plot", fig_width=600, fig_height=250):

    def datetime(x):
        return np.array(x, dtype=np.datetime64)

    plot = figure(plot_width=fig_width,
                plot_height=fig_height,
                x_axis_type="datetime",
                title=title)

    plot.sizing_mode = "scale_width"
    plot.grid.grid_line_alpha = 0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Temp'
    plot.legend.location = "top_right"

    colors = ["#FB9A99", "#3282E3", "#32E362", "#D4AC0D", "#7D3C98"]

    for i, col in enumerate(df.columns[1:]):
        plot.line(datetime(df[df.columns[0]]), df[col], color=colors[i], legend='{} (fahrenheit)'.format(col))

    return file_html(plot, CDN, "temp.html")

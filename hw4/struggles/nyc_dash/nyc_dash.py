import pandas as pd
import os.path as osp
from bokeh.plotting import figure
from bokeh.models import Select, ColumnDataSource, Legend
from bokeh.layouts import row, column
from bokeh.io import curdoc

# bokeh serve --address 0.0.0.0 --port 8080 --allow-websocket-origin=3.99.23.98:8080 --auth.module=auth.py nyc_dash.py

df = pd.read_csv("trim_data.csv",
                 index_col=0)
p = figure(title="NYC 2020 Service Requests Average Response Time", width=600, height=400)

months = list(range(1, 13))

menu = list(df.index.values)
menu.sort()

zip1_src = ColumnDataSource()
zip2_src = ColumnDataSource()


def get_zip_avg(zipcode):
    return {'months': months, 'average': list(df.loc[zipcode])}


def update_zip1(attr, old, new): zip1_src.data = get_zip_avg(new)
def update_zip2(attr, old, new): zip2_src.data = get_zip_avg(new)


average_data = {'months': months, 'average': list(df.loc['all'])}

all_average = ColumnDataSource(data=get_zip_avg("all"))


zip1_src.data = get_zip_avg(menu[0])
zip2_src.data = get_zip_avg(menu[1])

# p.add_layout(Legend(), 'left')
# p.legend.location = "top-right"
p.line('months', 'average', source=zip1_src, line_width=2, color="green",
       legend_label="Zipcode 1")
p.line('months', 'average', source=zip2_src, line_width=2, color="red",
       legend_label="Zipcode 2")
p.line(months, list(df.loc['all']), line_width=2, color="blue",
       legend_label="All")
p.xaxis.axis_label = 'Month'
p.yaxis.axis_label = 'Average Response Time'

menu.remove("all")
dropdown1 = Select(title="Zipcode 1",
                   value=menu[0], options=menu, background='green')
dropdown2 = Select(title="Zipcode 2",
                   value=menu[1], options=menu, background='red')
dropdown1.on_change('value', update_zip1)
dropdown2.on_change('value', update_zip2)
# dropdowns = row(dropdown1, dropdown2)
curdoc().add_root(column(dropdown1,dropdown2, p))
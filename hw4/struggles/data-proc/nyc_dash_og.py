import pandas as pd
import os.path as osp
from bokeh.plotting import figure
from bokeh.models import Select, ColumnDataSource, Legend
from bokeh.layouts import row, column
from bokeh.io import curdoc

df = pd.read_csv("trim_data.csv")
df.columns = ["zipcode", "month", "time"]
p = figure()

months = list(range(1, 13))

menu = list(pd.unique(pd['zipcode']))
menu.sort()

zip1_src = ColumnDataSource()
zip2_src = ColumnDataSource()


def get_zip_avg(zipcode):
       temp = df.loc[df['zipcode'] == zipcode]
       return {'months': months, 'average': list(temp[temp.columns[2]])}


def update_zip1(attr, old, new): zip1_src.data = get_zip_avg(new)
def update_zip2(attr, old, new): zip2_src.data = get_zip_avg(new)


average_data = {'months': months, 'average': list(df.loc['all'])}

all_average = ColumnDataSource(data=get_zip_avg("all"))


zip1_src.data = get_zip_avg(menu[0])
zip2_src.data = get_zip_avg(menu[1])

p.add_layout(Legend(), 'right')
p.line('months', 'average', source=zip1_src, color="red",
       legend_label="zipcode 1")
p.line('months', 'average', source=zip2_src, color="blue",
       legend_label="zipcode 2")
p.line(months, list(df.loc['all']), color="black",
       legend_label="all")
p.xaxis.axis_label = 'Month'
p.yaxis.axis_label = 'Avg Response Time'

menu.remove("all")
dropdown1 = Select(title="Zipcode 1",
                   value=menu[0], options=menu, background='red')
dropdown2 = Select(title="Zipcode 2",
                   value=menu[1], options=menu, background='green')
dropdown1.on_change('value', update_zip1)
dropdown2.on_change('value', update_zip2)
dropdowns = row(dropdown1, dropdown2)

curdoc().add_root(column(p, dropdowns))

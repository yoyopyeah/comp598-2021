from bokeh.io import show
from bokeh.models import CustomJS, Dropdown, Select
from bokeh.io import curdoc
from bokeh.plotting import figure
import pandas as pd

# login credentials
# http://X.X.X.X:8080/nyc_dash?username=nyc&password=iheartnyc
# def get_user(request):
#     login_value = request.get_argument('nyc')
#     if login_value == 'iheartnyc':
#         return 1
#     else:
#         return None

# login_url = 'http://3.99.23.98:8080/nyc_dash?username=nyc&password=iheartnyc'

def handler(event):
    print(event.item)

# dropdowns
menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]

dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)
dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

print(d.on_click(handler))

# plot line graph
# df = pd.read_csv('./trim_data.csv')
# df.columns = ["zipcode", "month", "time"]
# df = df[df['zipcode'] == 83]

# source = ColumnDataSource(df)

# p = figure(x_axis_label="Month", y_axis_label="Avg Response Time")
# p.line(x='month', y='time', line_width=2, source=source)

curdoc().title = "nyc_dash"
curdoc().add_root(dropdown)
curdoc().add_root(p)
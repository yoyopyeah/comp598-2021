import pandas as pd
from datetime import datetime
import sys

# format dataframe
df = pd.read_csv(sys.argv[1])
df['time'] = ""

# df['closed date'] = datetime.datetime.strptime(df['closed date'], "%m/%d/%Y %H:%M:%S %p")

# df['month'] = df['closed date'].datetime.month
# df['time']

for index, row in df.iterrows():
    datetime_object1 = datetime.strptime(row[0],'%m/%d/%Y %H:%M:%S %p')
    datetime_object2 = datetime.strptime(row[1],'%m/%d/%Y %H:%M:%S %p')
    datetime_difference = datetime_object2 - datetime_object1
    difference_hours = (datetime_difference.total_seconds())//3600
    row[3] = difference_hours



print(df.iloc[:4])
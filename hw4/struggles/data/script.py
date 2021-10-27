import pandas as pd
from datetime import datetime
import sys

# created time: columns[1]
# Closed date: columns[2]
# zip: columns[8]

# format dataframe
df = pd.read_csv(sys.argv[1])
df = df.iloc[:,[1,2,8]]
df.columns = ["create time", "closed date", "zip"]
df['time'] = ""
df['month'] = ""

# drop NaN
df = df.dropna()

# get 2020 data
df = df[df['create time'].str.contains("2020")]

# reformats
# df['zip'] = pd.to_numeric(df['zip'])
# df['create time'] = pd.to_datetime(df['create time'])
# df['closed date'] = pd.to_datetime(df['closed date'])
# round(0).astype(int)

# get 2020 data & create time < closed date
# df = df[(df['create time'] < df['closed date'])]


# # drop rows with create time later than closed date 
# for index, row in df.iterrows():
#     # row[2] = row[2].strip(".0")
#     if row[0] > row[1]:
#         df = df.drop(index, inplace=True)
# for index, row in df.iterrows():
#     dt1 = datetime.strptime(row[0],'%m/%d/%Y %I:%M:%S %p')
#     dt2 = datetime.strptime(row[1],'%m/%d/%Y %I:%M:%S %p')
#     datetime_difference = dt2 - dt1
#     if (dt1 > dt2):
#         df.drop(index, inplace = True)
#     else:
#         difference_hours = (datetime_difference.total_seconds())//3600
#         row[3] = difference_hours
#         row[4] = dt2.month



# drop events with closed dates later than create time

# df = df.drop(df[df['create time'] > df['closed date']].index)

print(df.iloc[:4])

# check number of lines
print(len(df.index))

df.to_csv('data1.csv', index=False)  
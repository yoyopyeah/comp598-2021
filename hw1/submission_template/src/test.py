import pandas as pd
import numpy as np

# read data
df = pd.read_csv("../data/IRAhandle_tweets_1.csv")

# filter data
df = df.head(1000)[(df["language"] == "English") & (df["content"].str.contains('\?')==False)]

# data annotation
df['trump_mention'] = np.where(df['content'].str.contains(r'[^a-zA-Z0-9]Trump[^a-zA-Z0-9]'), 'T', 'F')

# write filtered & annotated data to new tsv file
header = ["tweet_id", "publish_date", "content", "trump_mention"]
df.to_csv('../data/dataset.tsv', sep = '\t', columns = header)

# analyze and write data to new tsv file
header = ["result", "value"]


# print(df.loc[119:120, ['content', 'trump_mention']])
# print(df['trump_mention'].value_counts())

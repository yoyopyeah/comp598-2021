import pandas as pd

# read data
df = pd.read_csv("../data/IRAhandle_tweets_1.csv")

# filter data
df = df.head(1000)[(df["language"] == "English") & (df["content"].str.contains('?', regex=False)==False)]

# write filtered data to new tsv file
df.to_csv('../data/filtered_tweets.tsv', sep = '\t', index=False)
import pandas as pd
import numpy as np

# read data
df = pd.read_csv("/Users/yoyooolo/Documents/GitHub/comp598-2021/hw1/submission_template/data/IRAhandle_tweets_1.csv")

# filter data
df = df.head(10000)[(df["language"] == "English") & (df["content"].str.contains('\?')==False)]

# data annotation
df['trump_mention'] = np.where(df['content'].str.contains(r'\bTrump\b'), 'T', 'F')

# write filtered & annotated data to new tsv file
header = ["tweet_id", "publish_date", "content", "trump_mention"]
df.to_csv('../test/dataset.tsv', sep = '\t', columns = header, encoding='utf-8')

# analyze and write data to new tsv file
result = {'result': ['frac-trump-mentions'],
          'value': [float('%.3f'%(df["trump_mention"].value_counts(normalize=True)["T"]))]}
result = pd.DataFrame(result, columns = ['result', 'value'])
result.to_csv('../test/results.tsv', sep = '\t')

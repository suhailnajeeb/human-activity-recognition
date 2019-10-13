import pandas as pd
filepath = 'test.tsv'
data = pd.read_csv(filepath, sep = '\t')
data.shape

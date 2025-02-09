import pandas as pd

data = {'Values': [10,20,30,40,50]}

df = pd.DataFrame(data)

df['Normalized'] = (df['Values'] - df['Values'].min()) / (df['Values'].max() - df['Values'].min())

print(df)
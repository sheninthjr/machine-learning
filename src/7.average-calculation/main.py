import pandas as pd

data = {'Values': [10,20,30,40,50,60,70]}

df = pd.DataFrame(data)

df['Rolling_Mean'] = df['Values'].rolling(window=3).mean()

print(df)
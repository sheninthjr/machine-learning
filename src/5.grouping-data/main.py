import pandas as pd

data = {'A':['X','Y','X','Z','Y','Z'],
        'B':[10,20,30,40,50,60]}

df = pd.DataFrame(data)

grouped = df.groupby('A')['B'].sum()

print(grouped)
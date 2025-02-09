import pandas as pd

data = {'Age': [15,22,30,45,60,75]}

df = pd.DataFrame(data)

df['Category'] = pd.cut(df['Age'],bins=[0,18,35,50,100],labels=['Teen','Young','Adult','Senior'])

print(df)
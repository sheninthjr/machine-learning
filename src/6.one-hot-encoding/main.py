import pandas as pd

data = {'Category': ['A','B','A','C','B']}

df = pd.DataFrame(data)

encoded_df = pd.get_dummies(df,columns=['Category'])

print(encoded_df)
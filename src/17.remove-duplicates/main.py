import pandas as pd

data = {'Name': ['Alice','Bob','Alice','Charlie','Bob'],
        'Age': [25,30,25,35,30]}

df = pd.DataFrame(data)

df_unique = df.drop_duplicates()

print(df_unique)
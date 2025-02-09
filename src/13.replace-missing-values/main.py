import pandas as pd
import numpy as np

data = {'A': [10,20,np.nan,40,50,np.nan,70]}

df = pd.DataFrame(data)

df['A'].fillna(df['A'].median(),inplace=True)

print(df)
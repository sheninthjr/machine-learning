import pandas as pd
import numpy as np

data = {'A': [10,20,np.nan,40,50],
        'B': [5,np.nan,np.nan,20,25]}

df = pd.DataFrame(data)

df.fillna(df.mean(), inplace=True)

print(df)
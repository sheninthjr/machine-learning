import pandas as pd
import numpy as np

data = {'Values': [10,12,13,12,12,100,12,11,12,13,10]}

df = pd.DataFrame(data)

Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)

IQR = Q3 - Q1

outliers = df[(df['Values'] < (Q1 - 1.5 * IQR)) | (df['Values'] > (Q3 + 1.5 * IQR))]

print(outliers)
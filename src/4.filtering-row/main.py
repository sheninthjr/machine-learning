import pandas as pd

data = {'A': [10, 20, 30, 40, 50],
        'B': [5, 15, 25, 35, 45]}

df = pd.DataFrame(data)

filter_df = df[df['A'] > 30]

print(filter_df)

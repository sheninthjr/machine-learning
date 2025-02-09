import pandas as pd

data = {'Category': ['A','B','A','C','B','C','C','A','B']}

df = pd.DataFrame(data)

most_frequent = df['Category'].mode()[0]

print(most_frequent)
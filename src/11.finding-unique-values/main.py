import pandas as pd

data = {'Category': ['A','B','A','C','B','C','C','A']}

df = pd.DataFrame(data)

value_counts = df['Category'].value_counts()

print(value_counts)
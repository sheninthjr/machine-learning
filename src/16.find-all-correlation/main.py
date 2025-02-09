import pandas as pd

data = {'A': [1,2,3,4,5],
        'B': [2,4,6,8,10],
        'C': [5,10,15,20,25]}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

print(correlation_matrix)
import pandas as pd

data = {'Sales': [200, 500, 800, 300, 900, 1000, 150]}

df = pd.DataFrame(data)

top_sales = df.nlargest(3, 'Sales')

print(top_sales)

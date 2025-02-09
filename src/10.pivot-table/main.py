import pandas as pd

data = {'Date': ['2025-01-01','2025-01-02','2025-01-03','2025-01-04'],
        'Category': ['A','A','B','B'],
        'Sales': [100,200,150,250]}

df = pd.DataFrame(data)

pivot = df.pivot_table(values='Sales',index='Date',columns='Category',aggfunc='sum')

print(pivot)
import pandas as pd

data = {'Marks': [85,42,75,90,35,60]}

df = pd.DataFrame(data)

def categorize(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 50:
        return "Pass"
    else:
        return 'Fail'
    
df['Result'] = df['Marks'].apply(categorize)

print(df)
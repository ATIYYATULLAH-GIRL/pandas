import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
df['Age+5'] = df['Age'] + 5         
df = df[df['Age'] > 28]              
print(df)
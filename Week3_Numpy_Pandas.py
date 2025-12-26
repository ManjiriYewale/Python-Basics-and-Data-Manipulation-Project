#NumPy Operations
import numpy as np

arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))

#Pandas Data Cleaning
import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [80, 90, None, 70]
}

df = pd.DataFrame(data)
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print(df)

#Grouping & Aggregation (Client Project)
data = {
    'City': ['Pune', 'Pune', 'Mumbai', 'Mumbai'],
    'Sales': [100, 150, 200, 250]
}

df = pd.DataFrame(data)
result = df.groupby('City').mean()
print(result)

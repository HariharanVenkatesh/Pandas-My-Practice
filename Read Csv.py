import pandas as pd

df = pd.read_csv(r'C:\Users\acer\Downloads\sample_data.csv', index_col = "Name")
df.drop(['Occupation', 'Age'], axis = 1, inplace = True)

first = df.loc["Hariharan"]
second = df.loc["Aswin"]
print(first, "\n\n\n", second)
print(df) 


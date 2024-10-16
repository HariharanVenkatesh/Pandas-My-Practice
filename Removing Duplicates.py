import pandas as red
rd = red.read_csv(r'C:\Users\acer\Downloads\data.csv') 
rd.drop_duplicates(inplace = True)
print(rd.duplicated())
print(rd.to_string())
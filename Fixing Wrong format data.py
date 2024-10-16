# Replacing Values

import pandas as Wrd
wd = Wrd.read_csv(r'C:\Users\acer\Downloads\data.csv')
wd.loc[61, 'Duration'] = 60
print(wd.to_string())

for x in wd.index:
    if wd.loc[x, "Duration"]> 60:
        wd.drop(x, inplace= True)

print(wd.to_string())
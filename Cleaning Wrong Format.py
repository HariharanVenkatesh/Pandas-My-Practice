# Data of Wrong Format
# Convert Into a Correct Format
# Pandas has a to_datetime() method for this

import pandas as wrf
wf = wrf.read_csv(r'C:\Users\acer\Downloads\data.csv')
wf['Calories'] = wrf.to_datetime(wf['Calories'])
wf.dropna(subset=['Calories'], inplace = True)
print(wf.to_string())


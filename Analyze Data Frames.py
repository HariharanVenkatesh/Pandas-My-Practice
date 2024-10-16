# Viewing the Data
import pandas as re
Data_F = re.read_csv(r'C:\Users\acer\Downloads\sample_data.csv')
print(Data_F.head())
print(Data_F.tail(2))
print(Data_F.info())


Data = {
    'Name' : ['Hariharan','Aswin','Caleb','Pradeep','Abisheck'],
    'Age' : [23, 23, 24, 24, 24],
    'Address' : ['Nondimedu', 'Kandhal', 'Marrys Hill', 'Bennet Market', 'Kandhal'],
    'Qualification' : ['BE', 'BE', 'BE', 'BE', 'BE']
}

DF = re.DataFrame(Data)
Worktype = ['Remote', 'Hybrid', 'Remote', 'Hybrid', 'Hybrid']
DF['worktype'] = Worktype
print(DF[['Name', 'Address', 'Age', 'Qualification']])
print(DF)

Data_F = re.read_csv(r'C:\Users\acer\Downloads\sample_data.csv')
Data_F.dropna(inplace = True)
perc = [.20, .21, .22, .23]
include = ['object', 'float', 'int']
desc = Data_F.describe(percentiles = perc, include = include)
gesc = Data_F["Name"].describe()
print(gesc)
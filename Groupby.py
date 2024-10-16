import pandas as Grp
Data_F = {
    'Name' : ['Hariharan', 'Aswin', 'Caleb', 'Pradeep', 'Sam Abisheck', 'Dravid', 'Nandha Kumar'],
    'Age' : [23, 23, 24, 24, 24, 23, 24],
    'Address' : ['Nondimedu','Indra Colony', 'Marrys hill', 'Bennet Market', 'Kandhal', 'Kandhal','Nondimedu'],
    'Qualification' : ['BE_ECE', 'BE_ECE', 'BE_ECE', 'BE_EEE', 'BE_EEE','B.Com','B.Ed' ] 
    }

DF = Grp.DataFrame(Data_F)

print(DF)
DF.groupby('Name')                     # Grouping Data with One Key
print(DF.groupby('Name').groups)
DF.groupby(['Name', 'Qualification'])    # Grouping Data with Multiple Key
print(DF.groupby(['Name', 'Qualification']).groups)

# Grouping data by sorting keys : 
import pandas as Grp
Data_F = {
    'Name' : ['Hariharan', 'Aswin', 'Caleb', 'Pradeep', 'Sam Abisheck', 'Dravid', 'Nandha Kumar'],
    'Age' : [23, 23, 24, 24, 24, 23, 24]
    }

DF = Grp.DataFrame(Data_F)
# ndf = DF.groupby(['Name']).sum()
ndf = DF.groupby(['Name'], sort = False).sum()
print(ndf)

grp = DF.groupby('Name')           # Iterating through groups
for name, group in grp:
    print(name)
    print(group)
    print()

# Selecting a groups
grp = DF.groupby('Name')
print(grp.get_group('Aswin'))
grp = DF.groupby(['Name', 'Qualification'])
print(grp.get_group(('Caleb', 'BE_ECE')))

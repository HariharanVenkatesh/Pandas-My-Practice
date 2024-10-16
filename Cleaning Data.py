import pandas as nm
a = nm.read_csv(r'C:\Users\acer\Downloads\data.csv')
b = a.dropna()
a.dropna(inplace = True)
print(a.to_string())
b = a["Salary"].mean()
a.fillna(b, inplace = True)

# Pandas - Cleaning Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

a.dropna(inplace = True)
a.fillna(200, inplace = True)
print(a.to_string())

# Replace Only For Specified Columns
a["Calories"].fillna(200, inplace =True)
print(a.to_string())

# Replace Using Mean, Median, or Mode
c = a["Calories"].mean()
a['Calories'].fillna(c, inplace = True)
print(a.to_string())


d = a["Calories"].median()
a["Calories"].fillna(d, inplace = True)
print(a.to_string())

e = a["Calories"].mode()[0]
a["Calories"].fillna(e, inplace = True)
print(a.to_string())
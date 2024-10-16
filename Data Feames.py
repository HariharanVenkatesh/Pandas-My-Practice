# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as cv

Employee_Details = {
    "Name" : ["Hariharan", "Aswin", "Caleb", "Dravid", "Pradeep", "Abi"],
    "Employers ID" : [63791, 63791, 63793, 63794, 63795, 63796],
    "Salary Details": [20000, 25000, 25000, 15000, 17000, 12000]
}

df = cv.DataFrame(Employee_Details)
df = cv.DataFrame(Employee_Details, index = ["Developer", "Developer", "Database", "Tester", "Admin", "Cloud"])   # Named Indexes
print(df)
print(df.loc[1])       # Locate Row (Pandas use the loc attribute to return one or more specified row(s))
print(df.loc[[1, 4]])
print(df.loc["Developer"])

# Load Files Into a DataFrame

df = cv.read_csv('C:/Users/acer/OneDrive/Desktop/sample_data.csv')   #for example
print(df)





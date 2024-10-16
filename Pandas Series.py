# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type
import pandas as cr

a = [6, 3, 7, 9, 2, 1]

no = cr.Series(a)

print(no)
print(no[2])

# Create Labels

b = [4, 1, 7, 8, 9]

label = cr.Series(b, index = ["v", "w", "x", "y", "z"])
print(label["w"])
print(label)

# Key/Value Objects as Series

calories = {
    "Day 1" : 420,
    "Day 2" : 380,
    "Day 3" : 390
}

a = cr.Series(calories, index = ["Day 1", "Day 2"])
print(a)

# Data Frames

data = {
    "Calories" : [420, 380, 390],
    "Duration" : [50, 40, 45]
}

b = cr.DataFrame(data)
print(b)
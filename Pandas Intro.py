import pandas as mk

my_dataset = {
    'cars' : ["Tata","Mahindra","Nissan","Renault"],
    'Sold out' : [15, 12, 7, 8]
}

a = mk.DataFrame(my_dataset)
print(a)

studends_mark_report = {
    'Stud_Name' : ["Aswin", "Caleb", "Dravid", "Hariharan", "Pradeep","Sam Abisheck"],
    'Total_marks' : [100, 100, 100, 100, 100, 100],
    'Marks obtained' : [91, 88, 71, 75, 77, 81],
    'Grade' : ["A", "B", "C", "C", "C", "D"]
}

result = mk.DataFrame(studends_mark_report)
print(result)

print(mk.__version__)
students = {
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": [
        "Rahul",
        "Amit",
        "Priya",
        "Sneha",
        "Rohan",
        "Prashant"
    ],
    "Class": [5, 6, 7, 5, 8, 9],
    "Marks": [85, 90, 95, 78, 88, 92],
    "City": [
        "Pune",
        "Mumbai",
        "Kolhapur",
        "Nashik",
        "Satara",
        "Pune"
    ]
}

import pandas as pd

df = pd.DataFrame(students)

df.to_excel("students.xlsx", index=False)

print("Updated Excel file created!")

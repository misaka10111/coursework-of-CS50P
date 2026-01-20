import csv


# read
students = []
# with open("...") as ...: auto file.close() after clause is end
# file is a iterable object, which each element is a line in the file opened
with open("s6_students.csv") as file:
    # read in row
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})
    # read in column
    # reader = csv.DictReader(file)
    # for row in reader:
    #     students.append({"name": row["name"], "home": row["home"]})

"""
# write
name = input("What's your name? ")
home = input("Where's your home? ")
# "a" is append mode
with open("students2.csv", "a") as file:
    # write in row
    writer = csv.writer(file)
    writer.writerow([name, home])
    # write in column; fieldnames: columns' header
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writeheader()
    # accept dictionary as input
    writer.writerow({"name": name, "home": home})
"""

# doc of sort(): https://docs.python.org/3/library/functions.html#sorted
# key accept a function as input, the argument of the function is the element of the iterable item (prior parameter, students, in this case)
""" lambda
    grammar: lambda argument: expression
    lambda auto return values
    sample: 
        square = lambda x: x * x
        print(square(5))  # output 25
"""
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
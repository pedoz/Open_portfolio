import csv
import sys


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()

the_list = sys.argv[1]
user_input = sys.argv[2]

try:
    testing = open(the_list)
    testing.close()
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit()


students = []

with open(the_list) as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        last, first = name.rstrip().split(",")
        house = row["house"]
        students.append({"first": first, "last": last, "house": house})

with open(user_input, "w", newline = "\n") as newfile:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(newfile, fieldnames = fieldnames)
    writer.writeheader()
    for student in sorted(students, key = lambda student: student["first"]):
        writer.writerow(student)

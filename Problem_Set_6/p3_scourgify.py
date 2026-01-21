# Scourgify
import csv
import sys


def main():
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    except IndexError:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        raise SystemExit("Too many command-line arguments")
    if file1[-4:] != ".csv" or file2[-4:] != ".csv":
        raise SystemExit("Not CSV file(s)")

    fieldnames = ["first", "last", "house"]
    # stored for writing purpose
    students = [] # list of all lines
    try:
        with open(file1, "r") as raw_file:
            reader = csv.DictReader(raw_file)
            for row in reader:
                last, first = row["name"].split(",")
                first = first.lstrip()
                house = row["house"]
                student = {}  # one line of student info
                student[fieldnames[0]] = first
                student[fieldnames[1]] = last
                student[fieldnames[2]] = house
                students.append(student)
    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(file2, "w") as fin_file:
        writer = csv.DictWriter(fin_file, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            writer.writerow(s)


if __name__ == "__main__":
    main()

# Pizza Py
import sys
from tabulate import tabulate


def main():
    try:
        file_name = sys.argv[1]
        if len(sys.argv) > 2:
            raise SystemExit("Too many command-line arguments")
        if file_name[-4:] != ".csv":
            raise SystemExit("Not a CSV file")
    except IndexError:
        sys.exit("Too few command-line arguments")

    try:
        with open(file_name, "r") as file:
            table = []
            for line in file:
                element = line.strip().split(",")
                table.append(element)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

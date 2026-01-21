# Lines of Code
import sys


def main():
    try:
        file_name = sys.argv[1]
        if len(sys.argv) > 2:
            raise SystemExit("Too many command-line arguments")
        if file_name[-3:] != ".py":
            raise SystemExit("Not a Python file")
    except IndexError:
        sys.exit("Too few command-line arguments")

    count = 0
    try:
        with open(file_name) as file:
            for line in file:
                line = line.strip()
                # "" is False
                if line and not line.startswith("#"):
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

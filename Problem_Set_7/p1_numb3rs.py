# NUMB3RS
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number = r"(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    matches = re.search(rf"^{number}\.{number}\.{number}\.{number}$", ip.strip())
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

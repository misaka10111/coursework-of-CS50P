# Outdated
def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ")
        try:
            format1(date)
            break
        except ValueError:
            try:
                format2(date, months)
                break
            except ValueError:
                print("Wrong format")
                continue

# 12/30/2000 format
def format1(date):
    month, day, year = date.split("/")

    year = int(year)
    month = int(month)
    day = int(day)

    check_date(month, day)
    print(f"{year}-{month:02d}-{day:02d}")
    return


# Dec 30, 2000 format
def format2(date, months):
    month, day, year = date.split(" ")

    # get year
    year = int(year)

    # get month
    if month not in months:
        raise ValueError

    i = 1
    for m in months:
        if month == m:
            month = i
            break
        i += 1

    # get day
    day = int(day[:-1])

    check_date(month, day)
    print(f"{year}-{month:02d}-{day:02d}")
    return


def check_date(month, day):
    if month > 12 or day > 31:
        raise ValueError


main()

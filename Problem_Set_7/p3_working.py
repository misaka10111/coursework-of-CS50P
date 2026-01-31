# Working 9 to 5: convert AM/PM to 24h
import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = r"(([0-9]|1[0-2]):?([0-5][0-9])?\s(AM|PM))"
    match = re.search(rf"{time}\sto\s{time}", s)
    if match:
        start = match.group(1)
        start_hour = int(match.group(2))
        start_min = match.group(3)
        # start_AMPM = match.group(4)
        end = match.group(5)
        end_hour = int(match.group(6))
        end_min = match.group(7)
        # end_AMPM = match.group(8)

        if "AM" in start:
            if start_hour == 12:
                start_hour = "00"
            elif start_hour < 10:
                start_hour = f"0{start_hour}"
        elif "PM" in start:
            if not start_hour == 12:
                start_hour = start_hour + 12

        if not start_min:
            start_min = "00"


        if "AM" in end:
            if end_hour == 12:
                end_hour = "00"
            elif end_hour < 10:
                end_hour = f"0{end_hour}"
        elif "PM" in end:
            if not end_hour == 12:
                end_hour = end_hour + 12

        if not end_min:
            end_min = "00"



        start24 = f"{start_hour}:{start_min}"
        end24 = f"{end_hour}:{end_min}"
        return f"{start24} to {end24}"
    else:
        raise ValueError("Wrong input")

if __name__ == "__main__":
    main()

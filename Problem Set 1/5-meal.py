# Meal Time
def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    hour, minute = time.split(":")
    hour, minute = float(hour), float(minute)
    return hour + minute / 60


if __name__ == "__main__":
    main()

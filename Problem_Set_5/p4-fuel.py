# Reimplement fuel.py
def main():
    while True:
        fraction = input("Fraction: ")
        try:
           print(gauge(convert(fraction)))
           break
        except ValueError:
            print("Value or sign is not correct")
        except ZeroDivisionError:
            print("fuel tank cannot be 0")

def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError()
    if x < 0 or x > y:
        raise ValueError()

    return round(x / y * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

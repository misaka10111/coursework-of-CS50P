# Fuel Gauge
def main():
    while True:
        fraction = input("Fraction: ")

        try:
            numerator, denominator = fraction.split("/")
            numerator, denominator = int(numerator), int(denominator)
            if numerator < 0:
                raise ValueError()
            if denominator == 0:
                raise ZeroDivisionError()
        except ValueError:
            print("Value or sign is not correct")
            continue
        except ZeroDivisionError:
            print("fuel tank cannot be 0")
            continue

        if numerator > denominator:
            print("oil exceeds tank volume")
            continue

        # ending with result
        result = round(numerator / denominator * 100)
        if result >= 99:
            print("F")
            break
        elif result <= 1:
            print("E")
            break
        else:
            print(f"{result}%")
            break


main()

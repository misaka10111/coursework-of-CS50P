# Adieu, Adieu
import inflect


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            inputs = input("Name: ")
            names.append(inputs)
        except EOFError:
            print()
            print(f"Adieu, adieu, to {p.join(names)}")
            break


main()

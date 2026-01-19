# Coke Machine
def main():
    due = 50

    while due > 0:
        print(f"Amount Due: {due}")

        money = int(input("Insert Coin: "))
        if money in [25, 10, 5]:
            due = due - money

        if due <= 0:
            change = abs(due)
            print(f"Change Owed: {change}")


main()

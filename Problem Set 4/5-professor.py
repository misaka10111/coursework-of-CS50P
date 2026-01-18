# Little Professor
import random


def main():
    count, error_count, score = [0,0,0]
    level = get_level()

    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        while True:
            print(f"{x} + {y} = ", end="")
            z = input()
            # repeat if wrong
            try:
                z = int(z)
                if z != answer:
                    error_count += 1
                    raise ValueError
                else:
                    score += 1
                    error_count = 0
                    break
            except ValueError:
                print("EEE")
                # end after wrong x3
                if error_count == 3:
                    print(f"{x} + {y} = {answer}")
                    error_count = 0
                    break

        count += 1

    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            continue

        return level


def generate_integer(level):
    if level == 1:
        ran_int = random.randint(0,9)
    elif level == 2:
        ran_int = random.randint(10,99)
    elif level == 3:
        ran_int = random.randint(100,999)

    return ran_int

# def generate_integer(level):
#     if level == 1:
#         x = random.randint(0,9)
#         y = random.randint(0,9)
#     elif level == 2:
#         x = random.randint(10,99)
#         y = random.randint(10,99)
#     elif level == 3:
#         x = random.randint(100,999)
#         y = random.randint(100,999)
#     return (x, y)


if __name__ == "__main__":
    main()

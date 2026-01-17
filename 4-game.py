# Guessing Game
import random


def main():
    # setting level
    while True:
        level = input("Level: ")

        try:
            level = int(level)
        except ValueError:
            continue

        if level < 1:
            continue

        ran = random.randint(1, level)
        break

    # guessing number
    while True:
        guess = input("Guess: ")

        try:
            guess = int(guess)
        except ValueError:
            continue

        if guess < 1:
            continue

        if guess > ran:
            print("Too large!")
            continue
        elif guess < ran:
            print("Too small!")
            continue
        else:
            print("Just right!")
            return


main()

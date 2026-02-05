# Seasons of Love
from datetime import date, timedelta
import sys
import inflect


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_and_check(cls):
        try:
            birthday = date.fromisoformat(input("Date of Birth (YYYY-MM-DD): "))
        except ValueError:
            sys.exit("Invalid date")
        return cls(birthday)

    def calculate_minutes(self):
        diff = date.today() - self.date
        return diff.days * 24 * 60

    @staticmethod
    def convert_minutes(minutes: int):
        p = inflect.engine()
        words = p.number_to_words(minutes, andword="").capitalize()
        return f"{words} minutes"


def main():
    date = Date.get_and_check()
    print(Date.convert_minutes(Date.calculate_minutes(date)))


if __name__ == "__main__":
    main()

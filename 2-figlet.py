# Frank, Ian and Glen’s Letters
import sys
from pyfiglet import Figlet
from pyfiglet import FigletFont


def main():
    # random font for 0 argv
    if len(sys.argv) == 1:
        text = input("Input: ")
        print(Figlet().renderText(text))

    # specify font for 2 argv
    # argv[1]: argument; argv[2]: font name
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in FigletFont.getFonts():
        text = input("Input: ")
        print(Figlet(sys.argv[2]).renderText(text))

    else:
        sys.exit("Invalid usage")


main()

# Just setting up my twttr
def main():
    text = input("Input: ")
    print("Output: ", end="")

    for t in text:
        if t.lower() in ["a", "e", "i", "o", "u"]:
            continue
        print(t, end="")

    print()


main()

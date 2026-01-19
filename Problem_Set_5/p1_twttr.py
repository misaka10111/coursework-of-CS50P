# Reimplement twttr.py
def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):
    output = ""
    for w in word:
        if w.lower() not in ["a", "e", "i", "o", "u"]:
            output += w
    return output


if __name__ == "__main__":
    main()

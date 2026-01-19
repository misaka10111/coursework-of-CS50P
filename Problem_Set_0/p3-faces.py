# Making Faces
def main():
    output = convert(input("Write some emoticons: "))
    print(output)


def convert(emo):
    emo = emo.replace(":)", "🙂")
    emo = emo.replace(":(", "🙁")
    return emo


main()

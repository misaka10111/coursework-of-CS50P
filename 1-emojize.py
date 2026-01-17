# Emojize
import emoji

def main():
    inputs = input()
    outputs = emoji.emojize(inputs, language='alias')
    print(outputs)


main()

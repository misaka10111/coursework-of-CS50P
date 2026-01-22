# CS50 P-Shirt
from PIL import Image, ImageOps
import sys


def main():
    try:
        pic_before = sys.argv[1].lower()
        pic_after = sys.argv[2].lower()
    except IndexError:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        raise SystemExit("Too many command-line arguments")
    try:
        if not is_valid_suffix(pic_before, pic_after):
            raise SystemExit("Invalid input 1")
    except ValueError:
        sys.exit("Invalid input 2")

    img = Image.open(pic_before)
    shirt = Image.open("shirt.png")
    # resize
    img = ImageOps.fit(img, shirt.size)  # size is tuple
    # overlay
    img.paste(shirt, (0, 0), shirt)
    # save
    img.save(pic_after)


def is_valid_suffix(path1, path2):
    _, suffix1 = path1.split(".")
    _, suffix2 = path2.split(".")

    if suffix1 != suffix2:
        return False

    suffixes = [suffix1, suffix2]
    for suffix in suffixes:
        if suffix not in ["jpg", "jpeg", "png"]:
            return False

    return True


if __name__ == "__main__":
    main()

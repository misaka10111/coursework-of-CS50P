# Vanity Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 2. max 6 char, min 2 char
    if not (2 <= len(s) <= 6):
        return False

    # 1. start with at least two letters
    if not s[0:2].isalpha():
        return False

    had_digit = False
    for char in s:
        # 4. only ascii & number
        if not char.isalnum():
            return False

        # 3. number checks
        if char.isdigit():
            # 3.1. no 0 as number start
            if not had_digit and char == "0":
                return False
            had_digit = True

        # 3.2. number must come at the end if there is any
        if had_digit and char.isalpha():
            return False

    return True


main()

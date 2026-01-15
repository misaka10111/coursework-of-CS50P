# Grocery List
def main():
    grocery = {}
    while True:
        try:
            items = input().lower()
            # count items number
            if items in grocery:
                grocery[items] += 1
            else:
                grocery[items] = 1
        except EOFError:
            # print list
            print()
            for item in sorted(grocery):
                print(f"{grocery[item]} {item.upper()}")
                
            return


main()

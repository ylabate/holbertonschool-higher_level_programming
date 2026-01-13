#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lengh = len(sys.argv) - 1
    i = 1
    print("{} argument{}".format(lengh, "s" if lengh > 1 else ""), end='')
    print("{}".format(":" if lengh > 0 else "."))
    for arg in sys.argv[1:]:
        print("{}: {}".format(i, arg))
        i += 1

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i > 0:
        print("{} arguments:".format(i))
        i = 0
        for arg in argv:
            if i > 0:
                print("{}: {}".format(i, argv[i]))

            i = i + 1
    else:
        print("{} arguments.".format(i))

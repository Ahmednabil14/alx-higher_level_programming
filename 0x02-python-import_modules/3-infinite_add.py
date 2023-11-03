#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summ = 0
    for arg in argv[1:]:
        summ += int(arg)
print(summ)

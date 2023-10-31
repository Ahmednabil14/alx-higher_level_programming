#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number > 0:
    if last > 5:
        print("Last digit of", number, "is", last, "and is greater than 5")
    elif last == 0:
        print("Last digit of", number, "is 0 and is 0")
    else:
        print("Last digit of", number, "is", last, "and is less than 6")
if number < 0:
    if last == 0:
        print("Last digit of", number, "is 0 and is 0")
    else:
        last = -last
        print("Last digit of", number, "is", last, "and is less than 6 and not 0")

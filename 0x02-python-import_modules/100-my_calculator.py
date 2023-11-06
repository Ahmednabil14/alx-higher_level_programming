#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, mul, sub
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] == '+':
        x = add(int(sys.argv[1]), int(sys.argv[3]))
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], x))
    elif sys.argv[2] == '-':
        x = sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], x))
    elif sys.argv[2] == '*':
        x = mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], x))
    elif sys.argv[2] == '/':
        x = div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], x))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

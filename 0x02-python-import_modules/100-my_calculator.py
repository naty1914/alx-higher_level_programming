#!/usr/bin/python3
import sys


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    number_argv = len(sys.argv)

    if number_argv - 1 < 4 and number_argv - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    i = sys.argv[2]
    b = int(sys.argv[3])

    if number_argv - 1 >= 3:
        if i == '+':
            print("{:d} {} {:d} = {:d}".format(a, i, b, add(a, b)))
        elif i == '-':
            print("{:d} {} {:d} = {:d}".format(a, i, b, sub(a, b)))
        elif i == '*':
            print("{:d} {} {:d} = {:d}".format(a, i, b, mul(a, b)))
        elif i == '/':
            print("{:d} {} {:d} = {:d}".format(a, i, b, div(a, b)))
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

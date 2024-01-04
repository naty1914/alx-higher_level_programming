#!/usr/bin/python3
import sys


def add(*args):
    return sum(args)


if __name__ == "__main__":
    num = len(sys.argv)
    if num >= 1:
        numbers = [int(sys.argv[i]) for i in range(1, num)]
        result = add(*numbers)
print(f"{result}")

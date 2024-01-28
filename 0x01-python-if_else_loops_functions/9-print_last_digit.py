#!/usr/bin/python3


def print_last_digit(number):
    last_number = ''
    if isinstance(number, int):
        for num in str(number):
            last_number = num
        print("{}".format(last_number), end='')
        return last_number
    raise Exception

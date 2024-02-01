#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{}".format(value))
            return value
    except:
        return 0

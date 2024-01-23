#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        element = int(x)
    except ValueError:
        print(f"Error: {element} is not a valid integer.")
        return 0

    countNUmber = 0
    for element in my_list[0:element]:
        print(element, end='')
        countNUmber += 1
    print()
    return countNUmber

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    countNumber = 0
    try:
        for element in range(x):
            if isinstance(my_list[element], int):
                print("{:d}".format(my_list[element]), end="")
                countNumber += 1
        print()
        return countNumber
    except IndexError as e:
        print()
        print(f"IndexError: {e}")
        return e

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        element = int(x)
    except ValueError as e:
        print(f"error: {e}")
    countNumber = 0
    for element in my_list[0:x]:
        print(element, end='')
        countNumber = countNumber +1
    print()
    return element
        x = int(x)
    except ValueError:
        print(f"Error: {x} is not a valid integer.")
        return 0

    count = 0
    for element in my_list[0:x]:
        print(element, end='')
        count += 1
    print()
    return count

#!/usr/bin/python3


def uppercase(str):

    string = ''
    for letter in str:
        number = ord(letter)
        if 90 <= number < 123:
            string += chr(number-32)
        else:
            string += letter

    print("{}".format(string))

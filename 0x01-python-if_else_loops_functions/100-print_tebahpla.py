#!/usr/bin/python3


a = 0
for letter in range(90, 64, -1):

    if a % 2 == 0:
        print(chr(letter + 32), end='')
    else:
        print(chr(letter), end='')
    a += 1

#!/usr/bin/python3
for a in range(100):
    end = ", " if a < 99 else "\n"
    print("{:02d}".format(a), end=end)

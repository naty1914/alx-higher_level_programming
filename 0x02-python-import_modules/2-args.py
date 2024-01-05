#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("1 argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    for d in range(1, len(sys.argv)):
        print(f"{d}: {sys.argv[d]}")

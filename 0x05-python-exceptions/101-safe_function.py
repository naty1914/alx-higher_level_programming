#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        resultOfFunction = fct(*args)
        return resultOfFunction
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None

#!/usr/bin/python3


def search_replace(my_list, search, replace):
    replace_list = []
    for x in my_list:
        if x == search:
            replace_list.append(replace)
        else:
            replace_list.append(x)

    return replace_list

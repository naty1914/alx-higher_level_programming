#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list= my_list.copy()
    element= new_list.index(search)
    for x in new_list:
        new_list[element] = replace
        return new_list

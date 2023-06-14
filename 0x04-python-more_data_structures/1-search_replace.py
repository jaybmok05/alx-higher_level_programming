#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = my_list.copy()
    index = 0

    while index < len(new_list):
        if new_list[index] == search:
            new_list[index] = replace
        index += 1
    
    return new_list

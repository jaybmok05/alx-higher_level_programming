#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    index = len(my_list) - 1

    if my_list is None or len(my_list) == 0:
        return None
    else:
        while index >= 0:
            print("{:d}".format(my_list[index]))
            index -= 1

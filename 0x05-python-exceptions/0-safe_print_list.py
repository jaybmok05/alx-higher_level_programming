#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        while index < x:
            print(my_list[index], end="")
            index += 1
        print()
        return index
    except IndexError as err:
        print()
        return index

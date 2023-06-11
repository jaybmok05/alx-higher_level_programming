#!/usr/bin/python3

def no_c(my_string):

    str_no_c = ""
    index = 0

    while index < len(my_string):

        if my_string[index] != 'c' and my_string[index] != 'C':
             str_no_c += my_string[index]

        index += 1

    return str_no_c

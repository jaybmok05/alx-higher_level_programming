#!/usr/bin/python3

def print_list_integer(arr=[]):

    if arr is None or len(arr) == 0:
        return None
    else:
        for nums in arr:
            print("{:d}".format(nums))

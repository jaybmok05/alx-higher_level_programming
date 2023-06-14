#!/usr/bin/python3

def uniq_add(my_list=[]):
    index = 0
    sum_nums = 0

    while index < len(my_list):
        if my_list.count(index) > 1:
            my_list.remove(index)

        sum_nums += my_list[index]
        index += 1

    return sum_nums

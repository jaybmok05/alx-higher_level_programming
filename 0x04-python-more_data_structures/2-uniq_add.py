#!/usr/bin/python3

def uniq_add(my_list=[]):
    index = 0
    sum_nums = 0
    new_list = my_list.copy()

    while index < len(new_list):
        if new_list.count(index) > 1:
            new_list.remove(index)

        sum_nums += new_list[index]
        index += 1

    return sum_nums

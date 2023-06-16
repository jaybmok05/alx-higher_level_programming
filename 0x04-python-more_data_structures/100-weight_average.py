#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    weighted_sum = sum(map(lambda tple_0: tple_0[0] * tple_0[1], my_list))
    total_weight = sum(map(lambda tple_0: tple_0[1], my_list))

    return weighted_sum / total_weight

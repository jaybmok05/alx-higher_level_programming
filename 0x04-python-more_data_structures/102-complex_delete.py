#!/usr/bin/python3

def complex_delete(a_dict, val):
    keys_del = [key for key, key_val in a_dict.items() if key_val is val]

    for key in keys_del:
        del a_dict[key]

    return a_dict

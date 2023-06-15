#!/usr/bin/python3

def best_score(a_dict):

    if a_dict is None or a_dict == {}:
        return None

    max_val = max(a_dict.values())

    for key, value in a_dict.items():
        if value is max_val:
            return key

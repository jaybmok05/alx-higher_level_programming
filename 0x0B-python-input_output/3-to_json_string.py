#!/usr/bin/python3
'''Defining a function that returns JSON'''
import json


def to_json_string(my_obj):
    '''
    a function that returns the JSON representation
    of an object (string).

    Args:
        my_obj(dict): the obect

    Return:
        returns the JSON representation of an object
    '''
    return json.dumps(my_obj)

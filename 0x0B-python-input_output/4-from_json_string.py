#!/usr/bin/python3
'''Defining a function that returns an object'''
import json


def from_json_string(my_obj):
    '''
    a function that returns the JSON representation
    of an object (string).

    Args:
        my_obj(dict): the obect

    Return:
         returns an object (Python data structure)
         represented by a JSON string
    '''
    return json.loads(my_obj)

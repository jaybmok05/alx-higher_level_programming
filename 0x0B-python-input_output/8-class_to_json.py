#!/usr/bin/python3
'''module class_to_json
returns builds a dictionary
'''


def class_to_json(obj):
    '''a function that returns the dictionary
    description with simple data structure
    for JSON serialization of an object

    Args:
        obj(class): an instance of a Class

    Return:
        returns the dictionary description
    '''
    return obj.__dict__

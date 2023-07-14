#!/usr/bin/python3
'''Defining a fucntion
that writes an Object to a text file,
'''
import json


def save_to_json_file(my_obj, filename):
    '''
     a function that writes an Object to
     a text file, using a JSON representation

    Args:
        my_obj(dict): the object
        filename(txt): the name of the file
    '''
    with open(filename, 'w') as fileobj:
        fileobj.write(json.dumps(my_obj))

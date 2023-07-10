#!/usr/bin/python3
'''Defining function is_same_class'''


def is_same_class(obj, a_class):
    '''a function that check the instance of class

    Args:
        obj: the object to check
        a_class: the class the checks against

    Return:
        True if the object is exactly an instance of the specified class
        ; otherwise False
    '''
    return True if type(obj) == a_class else False

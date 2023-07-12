#!/usr/bin/python3
'''Defining a function that reads a file'''


def read_file(filename=""):
    '''
    A function that reads a text file and
    prints to stdout

    Args:
        filename(txt
    '''
    with open(filename, "r", encoding="utf-8") as fileobj:
        fileobj.seek(0)
        print(fileobj.read(), end='')

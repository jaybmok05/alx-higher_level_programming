#!/usr/bin/python3
'''Defining a function that appends text'''


def append_write(filename="", text=""):
    '''
    A function that appends a string at the end of a text
    file.

    Args:
        filename(txt): the file to write to
        text(str): the text to append to the file

    Return:
        returns the number of characters written
    '''
    with open(filename, 'a+', encoding="utf-8") as fileobj:
        return fileobj.write(str(text))

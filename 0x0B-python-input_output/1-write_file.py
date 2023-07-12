#!/usr/bin/python3
'''Defining a function that writes to file'''


def write_file(filename="", text=""):
    '''
    A function tha writes a string to a text
    file and returns the number of characters written

    Args:
        filename(txt): the file to write to
        text(str): the text to write to the file

    Return:
        returns the number of characters written
    '''
    with open(filename, 'w+', encoding="utf-8") as fileobj:
        return fileobj.write(str(text))

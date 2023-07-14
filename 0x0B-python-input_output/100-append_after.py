#!/usr/bin/python3
"""
Function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text after each line containing
    a specific string in the file.

    Args:
        filename (str): The name of the file to be modified.
        search_string (str): The specific string to search for
        in each line of the file.
        new_string (str): The line of text to be inserted after
        each line containing the search_string.

    Raises:
        FileNotFoundError: If the specified file is not found.
    '''

    with open(filename, 'r+') as fileobj:
        lines = fileobj.readlines()
        index = 0

        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(index + 1, new_string)
            index += 1

        fileobj.seek(0)
        fileobj.write("".join(lines))

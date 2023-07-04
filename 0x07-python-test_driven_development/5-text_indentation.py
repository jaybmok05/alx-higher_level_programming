#!/usr/bin/python3
"""
A function that print 2 new line after
., ? and :
"""


def text_indentation(text):
    """
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for index in range(len(text)):
        if text[index] == ' ':
            continue

        print(text[index], end="")

        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")

        for i in range(index+1, len(text)):
            if text[i] != ' ':
                index = i
                break

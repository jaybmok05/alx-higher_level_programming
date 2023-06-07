#!/usr/bin/python3

def uppercase(string):
    uppercase_string = ""

    for char in string:
        ascii_value = ord(char)

        if 97 <= ascii_value <= 122:
            uppercase_char = chr(ascii_value - 32)
        else:
            uppercase_char = char
        uppercase_string += uppercase_char
    print("{:s}".format(uppercase_string))

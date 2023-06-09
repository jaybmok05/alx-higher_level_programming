#!/usr/bin/python3

def remove_char_at(string, n):
    new = ""
    for i in range(len(string)):
        if i != n:
            new += string[i]
    return new

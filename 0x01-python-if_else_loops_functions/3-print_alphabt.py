#!/usr/bin/python3
for char_code in range(ord("a"), ord("z") + 1):
    letter = chr(char_code)
    if letter == "q" or letter == "e":
        continue
    print("{}".format(letter), end="")

#!/usr/bin/python3

number = 0

while number <= 89:
    if number % 10 == 0:
        number += 1 + number // 10

    if number != 89:
        print("{:02d}, ".format(number), end='')
    else:
        print("{:02d}".format(number))
    number += 1

#!/usr/bin/python3

FIZZ = "Fizz"
BUZZ = "Buzz"

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("{}{}".format(FIZZ, BUZZ), end=' ')
        elif number % 3 == 0:
            print("{}".format(FIZZ), end=' ')
        elif number % 5 == 0:
            print("{}".format(BUZZ), end=' ')
        else:
            print("{}".format(number), end=' ')

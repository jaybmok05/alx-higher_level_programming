#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

def sum():
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


sum()
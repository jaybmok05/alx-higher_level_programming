#!/usr/bin/python3

def multiple_returns(sentence):

    return ("None", 0) if len(sentence) == 0 else (len(sentence), sentence[0])

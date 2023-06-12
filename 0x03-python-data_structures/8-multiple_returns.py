#!/usr/bin/python3

def multiple_returns(sentence):

    return (None) if len(sentence) == 0 else (len(sentence), sentence[0])

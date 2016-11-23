#!/usr/bin/env python3

'''Pangram testing exercise'''


# 1st. try, recursion
def is_pangram(sentence, _char=65):
    '''Some men just want to watch the world burn'''
    return chr(_char) in sentence or chr(_char+32) in sentence \
           and is_pangram(sentence, _char+1) or _char is 90


# 2nd. try, faster
from string import ascii_lowercase
def is_pangram(sentence):
    '''Determines if a sentence is a pangram'''
    return set(ascii_lowercase).issubset(set(sentence.lower()))
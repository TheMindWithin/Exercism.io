"""Exercism.io's python "Pangram" exercise"""


# 1st try: recursion [slow]
def is_pangram(sentence, _char=65):
    """Determine if a sentence is a pangram"""
    return chr(_char) in sentence or chr(_char+32) in sentence \
           and is_pangram(sentence, _char+1) or _char is 90


# 2nd try: string [fast]
from string import ascii_lowercase

def is_pangram(sentence):
    """Determine if a sentence is a pangram"""
    return set(ascii_lowercase).issubset(set(sentence.lower()))
#!/usr/bin/env python3

'''RNA transcription exercise'''


# Another idea?
def distance(dna1, dna2):
    '''Calculates the Hamming difference between two DNA strands'''
    if len(dna1) is not len(dna2): raise ValueError()
    return sum(list(dna1)[i] is list(dna2)[i] for i in range(0,len(dna1)))

# No cmp in Python 3
def distance(dna1, dna2):
    '''Calculates the Hamming difference between two DNA strands'''
    if len(dna1) is not len(dna2): raise ValueError()
    return sum(map(abs, map(cmp, dna1, dna2)))

# Lib from scipy
from scipy.spatial.distance import hamming
def distance(dna1, dna2):
    '''Calculates the Hamming difference between two DNA strands'''
    if len(dna1) is not len(dna2): raise ValueError()
    return int(hamming(list(dna1), list(dna2))*len(dna1))
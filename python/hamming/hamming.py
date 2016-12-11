"""Exercism.io's python "Hamming" exercise"""


# 1st try: scipy [slowest]
from scipy.spatial.distance import hamming

def distance(dna1, dna2):
    """Calculate the Hamming difference between two DNA strands"""
    if len(dna1) is not len(dna2): raise ValueError()
    return 0 if len(dna1) == 0 else int(hamming(list(dna1), 
        list(dna2)) *len(dna1))


# 2nd try recursion [slow]
def distance(dna1, dna2):
    """Calculate the Hamming difference between two DNA strands"""
    if len(dna1) is not len(dna2): raise ValueError()
    return 0 if len(dna1) == 0 else int(dna1[0] != dna2[0]) \
        +distance(dna1[1:], dna2[1:])


# 3rd try: lambda [fast]
def distance(dna1, dna2):
    """Calculate the Hamming difference between two DNA strands"""
    if len(dna1) is not len(dna2): raise ValueError()
    return sum(map(lambda base: dna1[base] != dna2[base], range(len(dna1))))


# 4th try: cmp [faster], Python 2
def distance(dna1, dna2):
    """Calculate the Hamming difference between two DNA strands"""
    if len(dna1) is not len(dna2): raise ValueError()
    return sum(map(abs, map(cmp, dna1, dna2)))


# 5th try: for-loop [fastest]
def distance(dna1, dna2):
    """Calculate the Hamming difference between two DNA strands"""
    if len(dna1) is not len(dna2): raise ValueError()
    return sum(dna1[i] != dna2[i] for i in range(len(dna1)))

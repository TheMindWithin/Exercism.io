#!/usr/bin/env python3

'''RNA transcription exercise'''


# 1st try, recursion
def to_rna(dna, _i=0):
    '''Returns RNA complement of a given DNA strand'''
    base = ['U', 'A', 'T', 'G', 'C', 'T']
    return dna if _i > 4 else to_rna(dna.replace(base[_i+1], base[_i]), _i+1) \
        if set(dna).issubset(base[max(1-_i,0):5]) else ''


# 2nd try, much slower
def to_rna(dna):
    '''Returns RNA complement of a given DNA strand'''
    return ''.join({'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}[base] 
        for base in dna) if set(dna).issubset(['G','C','T','A']) else ''


# 3rd try, much faster
def to_rna(dna):
    '''Returns RNA complement of a given DNA strand'''
    return dna.translate(str.maketrans('AGCT', 'UCGA')) \
        if set(dna).issubset(['G','C','T','A']) else ''
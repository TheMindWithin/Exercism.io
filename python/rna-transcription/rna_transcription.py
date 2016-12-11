"""Exercism.io's python "Rna Transcription" exercise"""


# 1st try: recursion [slow]
def to_rna(dna, _i=0):
    """Return the RNA complement of a given DNA strand"""
    base = ['U', 'A', 'T', 'G', 'C', 'T']
    return dna if _i > 4 else to_rna(dna.replace(base[_i+1], base[_i]), _i+1) \
        if set(dna).issubset(base[max(1-_i, 0):5]) else ''


#2nd try: lambda [fast]
def to_rna(dna):
    """Return the RNA complement of a given DNA strand"""
    return ''.join(map(lambda base: {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
        [base], list(dna))) if set(dna).issubset(['G','C','T','A']) else ''


# 3rd try: for-loop [faster]
def to_rna(dna):
    """Return the RNA complement of a given DNA strand"""
    return ''.join({'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}[base] 
        for base in dna) if set(dna).issubset(['G','C','T','A']) else ''


# 4th try: translate [fastest], Python 3
def to_rna(dna):
    """Return the RNA complement of a given DNA strand"""
    return dna.translate(str.maketrans('AGCT', 'UCGA')) \
        if set(dna).issubset(['G','C','T','A']) else ''
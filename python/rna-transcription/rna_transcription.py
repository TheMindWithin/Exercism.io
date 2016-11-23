#!/usr/bin/env python3

'''RNA transcription exercise'''

def to_rna(dna, i=0):
    '''Returns RNA complement of a given DNA strand'''
    nucleo = ['U','A','T','G','C','T']
    return dna if i > 4 else to_rna(dna.replace(nucleo[i+1],nucleo[i]), i+1)

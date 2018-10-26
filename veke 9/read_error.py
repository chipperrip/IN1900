"""
Exercise 6.4: Interpret output from a program
"""

import matplotlib.pyplot as plt

def lnsum_extractor(filename='lnsum.dat'):
    infile = open(filename, 'r')

    for line in infile:
        print(line.strip())

lnsum_extractor()

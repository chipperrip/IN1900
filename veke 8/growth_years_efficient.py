"""
Exercise A.3: Reduce memory usage of difference equations

"""

import numpy as np
import matplotlib.pyplot as plt
import sys

x0 = 100 # initial amount
p = 5 # interest rate
N = 5 # number of years

#fil for utskrift
outfile = open('growth.dat', 'w')
outfile.write('  year  |  amount\n')
outfile.write('    0   |   %g\n' %(x0))

#første n-verdi
i = 1
#forrige ledd i differenslikninga
xp = x0

while i <= N:

	x = xp + (p/100.0)*xp

	outfile.write('    %g   |   %g\n' %(i, x))

	i += 1
	#forrige ledd oppdaterast
	xp = x

outfile.close()

"""
Terminal> python growth_years_efficient.py

Programmet lagar ei fil som inneheld teksten:

  year  |  amount
    0   |   100
    1   |   105
    2   |   110.25
    3   |   115.763
    4   |   121.551
    5   |   127.628

"""
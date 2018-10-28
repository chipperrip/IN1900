"""
Exercise 6.4: Interpret output from a program
"""

import matplotlib.pyplot as plt
import numpy as np

def lnsum_extractor(filename='lnsum.dat'):
    data = []

    # vi les fila og sjekker om linja inneheld epsilon, og legg den til ei liste
    with open(filename, 'r') as infile:

        for line in infile:

        	line = line.strip()
        	if "epsilon" in line:
        		data.append(line)

    return data

data = lnsum_extractor()

epsilon = np.zeros(5)
exact_error = np.zeros(5)
n = np.zeros(5)

i=0
for line in data:

	words = line.split()

	# fyller arrays med tilhøyrande ord frå linja, manipulert med strip()
	epsilon[i] = float(words[1].strip(','))
	exact_error[i] = float(words[4].strip(','))
	n[i] = float(words[-1].strip('n='))

	i = i+1

plt.semilogy(n, epsilon, label='epsilon')
plt.semilogy(n, exact_error, label='exact error')

plt.title('Exercise 6.4')
plt.ylabel('error')
plt.xlabel('n')
plt.grid()
plt.legend()

plt.show()

"""
Terminal> python lnsum.py > lnsum.dat
		  python read_error.py

Vi får ein graf som teiknar linjane for eksakt og tilnærma feil, 
med logaritmisk skala på y-aksen, og n-verdi på x-aksen.
"""

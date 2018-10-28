"""
Frå oppgåveheftet
Exercise A.3. The spreading of a disease
"""

import numpy as np
import matplotlib.pyplot as plt

N = np.linspace(0,50,51)
print(N)
speed = 5/7


def disease(N, speed):
	x = np.zeros(N+1)

	x[0] = 100
	x[1] = 150
	for n in range (2, N+1):
        
		x[n] = (x[n-1]* 1/4) + (x[n-2] * speed)

	return x




plt.plot(N, disease(50, 5/7), label='5/7')
plt.plot(N, disease(50, 3/4), label= '3/4')

plt.legend()
plt.show()

def disease_B(N, speed):
	xpp = 100
	xp = 150
	xn = 0

	for n in range(N+1):
		xn = (xp* 1/4) + (xpp * speed)
		print()

		#uferdig, seint ute. resten av denne oppgåva er triviell uansett



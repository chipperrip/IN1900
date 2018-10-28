"""
Exercise 5.32: Plot Taylor polynomial approximations to sin x

"""

import numpy as np
import matplotlib.pyplot as plt
import math

#funksjon som returnerer ei tilnærming av sin x ved bruk av Taylorpolynom
def S(x, n):
	s = 0

	for j in range (n+1):

		s = s + ((((-1)**j) *  x**((2.0*j)+1.0))/math.factorial((2*j)+1) )

	return s

x = np.linspace(0, 4*np.pi, 201)

sum1 = S(x, 1)
sum2 = S(x, 2)
sum3 = S(x, 3)
sum6 = S(x, 6)
sum12 = S(x, 12)

sinx = np.sin(x)


plt.title('Taylor polinomial approximations to sin x')

plt.plot(x, sum1, label='S(x; 1)')
plt.plot(x, sum2, label='S(x; 2)')
plt.plot(x, sum3, label='S(x; 3)')
plt.plot(x, sum6, label='S(x; 6)')
plt.plot(x, sum12, label='S(x; 12)')
plt.plot(x, sinx, label = 'np.sin(x)')

# begrenser y-aksen slik at vi får sjå den relevante 
# utviklinga i forhold til sin x
plt.ylim(-2,2)

plt.xlabel('x')
plt.grid()
plt.legend()
plt.show()

"""
Terminal> python plot_Taylor_sin.py

Vi får opp ein graf.

Grafen viser at tilnærminga av S(x;n) til sin x er ganske 
dårleg ved låge n-verdiar, men legg seg fint inntil når n aukar.

"""
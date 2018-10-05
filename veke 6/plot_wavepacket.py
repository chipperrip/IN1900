"""
Exercise 5.28: Plot a wave packet

The function 

	f(x,t) = (e**-(x-3t)**2)*sin(3*pi*(x-t))

describes for a fixed value of t a wave localized in space.
Make a program that visualizes this function as a function 
of x on the interval [-4,4] when t = 0
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
	return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

x = np.linspace(-4,4,101)
f_x = f(x,0)

plt.title('Wave packet as function of x on [-4,4] when t=0')
plt.plot(x,f_x)
plt.legend()
plt.grid()
plt.show()

"""
Programmet teiknar ein graf som ser fin ut
"""
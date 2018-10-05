"""
Exercise 5.31: Explore a complicated function graphically

The wave speed c of water surface waves depends on the length lambda of the waves.
The following formula relates c to lambda:

c(lambda) = sqrt( (g*lambda)/(2*pi) * (1 + (s*(4*p**2)/(rho*g*lambda**2)) * tanh ((2*pi*h)/lambda))

"""
import numpy as np
import matplotlib.pyplot as plt

#wave speed c in m/s as function of the length lambda of the waves
def c(l):
	# l = is lambda in m
	g = 9.81 # m/s^2 acceleration of gravity
	s = 7.9e-2 # N/m air-water surface tension
	rho = 1000 # kg/m^3 density of water
	h = 50 # m water depth

	#splitter opp formelen i 3 deler for å gjere den meir oversiktleg
	f1 = (g*l)/(2*np.pi)
	f2 = 1 + s*((4*np.pi**2)/(rho*g*l**2))
	f3 = np.tanh((2*np.pi*h)/l)

	return np.sqrt(f1*f2*f3)

small_lambdas = np.linspace(0.001,0.1, 2001)
large_lambdas = np.linspace(1, 2000)

small_c = c(small_lambdas)
large_c = c(large_lambdas)

plt.title('Water-wave velocity')
plt.plot(small_lambdas, small_c, label = 'l=[0.001,0.1]')
plt.plot(large_lambdas, large_c, 'r-', label = 'l=[1,2000]')
plt.legend()
plt.grid()
plt.show()

"""
Grafen ser grei ut, men ein må zoome in på det lisje intervallet for å sjå
"""
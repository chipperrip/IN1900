"""
From the exercise collection:
Exercise 1.2. Population growth
"""
from math import e

#carrying capacity of the species in the environment
B = 50000

#running time of the experiment in hours
t = 24

#constant k tells us how fast the population grows
k = 0.2

#Population 5000 at t= 0, find C
Nt0 = 5000

C = (B - Nt0)/Nt0

#Growth of a population by logistic function:
Nt = B / (1+C*e**(-k*t))

print('\nThe population after 24 hours is %g.\n'%(Nt))

"""
OUTPUT:

The population after 24 hours is 46552.

"""

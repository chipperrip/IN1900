from math import *

#mass (in grams) of the egg, 67g for large, 47g for small
M = 67.0

#density of the egg in g cm^-3
rho = 1.038

#specific heat capacity in J g^-1 K^-1
c = 3.7

#thermal conductivity in W cm^-1 K^-1
K = 5.4*10**(-3)

#temperature in C of the boiling water
Tw = 100.0

#desired temperature of the egg
Ty = 70.0

#starting temperature of the egg, 4C fridge, 20C room
T0 = 4.0

#formula: time it takes for the center of the yolk to reach Ty in C

t1 = (M**(2.0/3)*c*rho**(1.0/3)) / ( K*pi**2*((4*pi)/3)**(2.0/3) )

t2 = log(0.76*(T0-Tw)/(Ty-Tw))

t = (t1*t2)

print (" t for a large egg from the fridge (4C) is %g seconds."%(t))

T0 = 20

t2 = log(0.76*(T0-Tw)/(Ty-Tw))

t = (t1*t2)

print (" t for a large egg at room temperature (20C) is %.2f seconds."%(t))

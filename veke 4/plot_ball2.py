"""
Exercise 5.10: Plot a formula for several parameters

Make a program that reads a set of v0 values
from the command line and plots the
corresponding curves y(t) = v0t - 1/2g(t^2)
in the same figure, with tE[0.2v0/g] for each curve
set g = 9.81
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

v0_list = [float(v) for v in sys.argv[1:]]
g = 9.81


for v0 in v0_list:
    t_stop = 2*v0/g
    t = np.linspace(0, t_stop, 101)
    y = v0*t -0.5*g*t**2
    plt.plot(t,y)


plt.title('height of ball')
plt.xlabel('time (s)')
plt.ylabel('height (m)')

plt.show()

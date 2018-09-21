"""
Exercise 5.11: Specify the extent of the axes in a plot

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

v0_max = max(v0_list)
t_max = 2*v0_max/g

y_max = 0

for v0 in v0_list:
    t_stop = 2*v0/g
    t = np.linspace(0, t_stop, 101)
    y = v0*t -0.5*g*t**2

    if max(y) > y_max:
        y_max = max(y)
    plt.plot(t,y, label='v0 = %g' %(v0))


plt.title('height of ball')
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.axis([0, t_max, 0, y_max])
plt.grid()
plt.legend()

plt.show()

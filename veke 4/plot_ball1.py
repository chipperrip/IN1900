"""
Exercise 5.9: Plot a formula
Make a plot of the function
y(t) = v0t - 1/2g(t^2)
for v0 = 10, g = 9.81, and tE[0.2v0/g]
set axis labels as time (s) and height (m)
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 10
g = 9.81

t_stop = 2*v0/g

t = np.linspace(0, t_stop, 101)

y = v0*t -0.5*g*t**2
plt.title('height of ball')
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.plot(t,y)
plt.show()

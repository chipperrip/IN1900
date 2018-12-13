import sys
import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt

f = lambda x : eval(sys.argv[1])

x = np.linspace(0,1)
y = f(x)
print (y)

plt.title(sys.argv[1])
plt.plot(x, y)
plt.grid()
plt.show()

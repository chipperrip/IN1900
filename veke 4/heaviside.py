import numpy as np
import matplotlib.pyplot as plt

def H(x):
    if x < 0:
        return 0
    else:
        return 1

def cube(x):
    return x**3

#only if (if:)
#Hv = np.vectorize(H)

def Hv(x):
    return np.where(x<0,0,1)

x = np.linspace(-5,5,101)
y = Hv(x)
plt.plot(x,y)
plt.show()

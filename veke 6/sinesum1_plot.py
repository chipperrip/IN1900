"""
Exercise 5.41: Plot sum-of-sines approximations to a function

Exercise 3.21 defines the approximation S(t;n) to a function f(t)
Plot S(t;1) S(t;3), S(t;20), S(t;200) and the exact f(t) function in the same plot.
Use T = 2*pi
"""

import numpy as np
import matplotlib.pyplot as plt

def f(t,T):
    T = 2*np.pi
    if 0 < t < T/2:
        return 1
    elif t == T/2:
        return 0
    else:
        return -1

def S(t,n,T):

    s = 0
    for i in range (1,n+1):
        s += (1/(2*i - 1)) * np.sin((2*(2*i - 1) * np.pi * t)/T)

    return s *(np.pi/4)

T = 2*pi
N = 100
t_list = np.linspace()

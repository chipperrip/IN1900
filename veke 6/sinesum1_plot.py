"""
Exercise 5.41: Plot sum-of-sines approximations to a function

Exercise 3.21 defines the approximation S(t;n) to a function f(t)
Plot S(t;1) S(t;3), S(t;20), S(t;200) and the exact f(t) function in the same plot.
Use T = 2*pi
"""

import numpy as np
import matplotlib.pyplot as plt

def f(t,T=(2*np.pi)):

    if 0 < t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2 < t < T:
        return -1

def S(t,n,T=(2*np.pi)):

    s = 0
    for i in range (1,n+1):
        s += (1/(2*i - 1)) * np.sin((2*(2*i - 1) * np.pi * t)/T)

    return s *(4/np.pi)


t_list = np.linspace(0, 4*np.pi,20000)
s_list_1 = S(t_list,1)
s_list_3 = S(t_list,3)
s_list_20 = S(t_list, 20)
s_list_200 = S(t_list, 200)
f_list = np.asarray([f(t) for t in t_list])
print(type(f_list))
print(len(t_list),len(f_list))
#T = 2*np.pi
#f_list = np.piecewise(t_list, [(0<t_list<T/2),(t_list==T/2),(T/2 <t_list< T)], [1,0,-1])

plt.title('Plot of sum-of-sines approximations to a function')
plt.plot(t_list, s_list_1, label='S(t,1)')
plt.plot(t_list, s_list_3, label='S(t,3)')
plt.plot(t_list, s_list_20, label='S(t,20)')
plt.plot(t_list, s_list_200, label='S(t,200)')
plt.plot(t_list, f_list, label='f(t)')
plt.xlabel('t')
plt.legend()
plt.show()
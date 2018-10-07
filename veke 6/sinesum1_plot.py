"""
Exercise 5.41: Plot sum-of-sines approximations to a function

Exercise 3.21 defines the approximation S(t;n) to a function f(t)
Plot S(t;1) S(t;3), S(t;20), S(t;200) and the exact f(t) function in the same plot.
Use T = 2*pi
"""

import numpy as np
import matplotlib.pyplot as plt

# Nøyaktig verdi som S(t;n) forsøker å nå
def f(t,T=(2*np.pi)):
    
    #trengs for å gjere funksjonen periodisk
    t = t % T
    
    if 0 < t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2 < t < T:
        return -1

#Fourier sum
def S(t,n,T=(2*np.pi)):
    s = 0
    for i in range (1,n+1):
        s += (1/(2*i - 1)) * np.sin((2*(2*i - 1) * np.pi * t)/T)

    return s *(4/np.pi)

# lagar mange element slik at eg får fine kurver ved høg zoom
t_list = np.linspace(0, 4*np.pi,20001)

s_list_1 = S(t_list,1)
s_list_3 = S(t_list,3)
s_list_20 = S(t_list, 20)
s_list_200 = S(t_list, 200)

#brukar list comprehension til å konstruere denne.
#kunne og ha brukt numpy sin piecewise funksjon,
#eller tatt inn t_list i f(t) og jobba med den der.
f_list = np.asarray([f(t) for t in t_list])


plt.title('Plot of sum-of-sines approximations to a function')

plt.plot(t_list, s_list_1, label='S(t,1)')
plt.plot(t_list, s_list_3, label='S(t,3)')
plt.plot(t_list, s_list_20, label='S(t,20)')
plt.plot(t_list, s_list_200, label='S(t,200)')

plt.plot(t_list, f_list, label='f(t)')
plt.xlabel('t')
plt.legend()
plt.show()

"""
Programmet teiknar alle grafane som forventa.
"""
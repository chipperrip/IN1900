"""
Exercise A.5: Solve a system of difference equations

Solve (A.32)–(A.33) in a Python function and plot the xn sequence.

"""
import numpy as np
import matplotlib.pyplot as plt

def development(x0, c0, I , p, n):
    x = np.zeros(n+1)
    
    x[0] = x0
    cp = c0
    
    for i in range (1,n+1):
        
        x[i] = x[i-1] + (p/100)*x[i-1] - cp
        c = cp + (I/100)*cp

        cp = c
        
    return x

F  = 1000000 # starting amount
p  = 5 # interest
I  = 3 # inflation
n  = 35 # years
q  = 80 # percent of interest

c0 =  ((p*q)/(1e4)) * F # consumption for the first year


yearly_results = development(F, c0, I, p, n)

plt.plot(yearly_results, label='Amount after x years')
plt.xlabel('years')
plt.ylabel('amount')
plt.grid()
plt.show() 

"""
Terminal> python fortune_and_inflation1.py

Programmet teiknar ein graf som syner korleis pengebeholdningen vil
forandre seg etter kvart som forbruket justert for inflasjon aukar
"""
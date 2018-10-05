"""
Exercise 5.12: Plot exact and inexact Fahrenheit-Celsius conversion formulas

A simple rule to quickly compute the Celsius temperature from the Fahrenheit degrees
is to subtract 30 and then divide by 2: C = (F-30)/2. Compare this curve
against the exact curve C =(F-32)*5/9 in a plot. Let F vary between -20 and 120.
"""
import numpy as np
import matplotlib.pyplot as plt

F = np.linspace(-20,121)
C_exact = ((F-32)*5)/9
C_approx = (F-30)/2

plt.title('Celsius as a function of Fahrenheit')
plt.plot(F, C_exact, label='C_exact = (F-32)*5/9')
plt.plot(F, C_approx,'r+', label='C_approx = (F-30)/2')
plt.xlabel('F')
plt.ylabel('C')
plt.legend()

plt.show()


""" 
Programmet teiknar to grafar som ser korrekte ut.
"""

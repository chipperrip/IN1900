"""
Frå boka

Exercise 9.11: Implement a new subclass for differentiation
"""
import numpy as np

class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

class Backward1(Diff):
    def __call__(self, x):
        f = self.f
        h = self.h

        return (f(x) - f(x-h))/h

class Backward2(Diff):
	def __call__(self, x):
		f = self.f
		h = self.h

		return (f(x-2*h) - 4*f(x-h) + 3*f(x))  /  (2*h)

t = 0
h = 2
n = 14

b1 = Backward1(np.exp)
b2 = Backward2(np.exp)

print('\nDifference between backward1 and backward2 results for D[g(%g)]' %(t))
for k in range(0, n+1):
    b1.h = h**(-k)
    b2.h = h**(-k)
    
    comparison = abs(b1(-t)-b2(-t))
    print('k =%2.0f:  %g' %(k,comparison))


"""
Terminal> python Backward2.py

Difference between backward1 and backward2 results for D[g(0)]
k = 0:  0.199788
k = 1:  0.154818
k = 2:  0.0978582
k = 3:  0.0552279
k = 4:  0.0293662
k = 5:  0.0151455
k = 6:  0.00769153
k = 7:  0.00387587
k = 8:  0.00194551
k = 9:  0.000974657
k =10:  0.000487805
k =11:  0.000244021
k =12:  0.000122041
k =13:  6.10277e-05
k =14:  3.05157e-05

Vi ser ein halvering av feilen for kvart inkrement av k.
"""
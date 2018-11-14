"""
Frå boka

Exercise 9.11: Implement a new subclass for differentiation
"""
import numpy as np

class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def error (self, x, exact):
        return abs(exact - self(x))

class Backward1(Diff):
    def __call__(self, x):
        f = self.f
        h = self.h

        return (f(x) - f(x-h))/h

class Backward2(Diff):
	def __call__(self, x):
		f = self.f
		h = self.h

		return (f(x-(2*h)) - 4*f(x-h) + 3*f(x))  /  (2*h)

t = 0
h = 2
n = 14

#vi må lage ein funksjon som fortel backward at den må gjere f(x) til f(-x)
def negative_exp_arg(t):
    return np.exp(-t)

b1 = Backward1(negative_exp_arg)
b2 = Backward2(negative_exp_arg)

print('\nDifference between backward1 and backward2 results for D[g(%g)]' %(t))
for k in range(0, n+1):
    b1.h = h**(-k)
    b2.h = h**(-k)
    
    comparison = abs(b1.error(t,-1)-b2.error(t, -1))

    print('k =%2.0f: b1-b2: %e\t b1e = %e\t b2e = %e'  \
        %(k,comparison, (b1.error(t,-1)), (b2.error(t,-1))))


"""
Terminal> python Backward2.py

Difference between backward1 and backward2 results for D[g(0)]
k = 0: b1-b2: 3.968256e-02       b1e = 7.182818e-01      b2e = 7.579644e-01
k = 1: b1-b2: 1.740458e-01       b1e = 2.974425e-01      b2e = 1.233967e-01
k = 2: b1-b2: 1.108625e-01       b1e = 1.361017e-01      b2e = 2.523921e-02
k = 3: b1-b2: 5.946121e-02       b1e = 6.518762e-02      b2e = 5.726418e-03
k = 4: b1-b2: 3.054640e-02       b1e = 3.191134e-02      b2e = 1.364939e-03
k = 5: b1-b2: 1.545578e-02       b1e = 1.578904e-02      b2e = 3.332627e-04
k = 6: b1-b2: 7.771009e-03       b1e = 7.853350e-03      b2e = 8.234088e-05
k = 7: b1-b2: 3.895978e-03       b1e = 3.916442e-03      b2e = 2.046470e-05
k = 8: b1-b2: 1.950569e-03       b1e = 1.955671e-03      b2e = 5.101191e-06
k = 9: b1-b2: 9.759252e-04       b1e = 9.771986e-04      b2e = 1.273430e-06
k =10: b1-b2: 4.881221e-04       b1e = 4.884402e-04      b2e = 3.181244e-07
k =11: b1-b2: 2.441009e-04       b1e = 2.441804e-04      b2e = 7.950166e-08
k =12: b1-b2: 1.220604e-04       b1e = 1.220802e-04      b2e = 1.987246e-08
k =13: b1-b2: 6.103267e-05       b1e = 6.103764e-05      b2e = 4.969479e-09
k =14: b1-b2: 3.051696e-05       b1e = 3.051820e-05      b2e = 1.236913e-09

Etter dei første k verdiane, ser vi at forskjellen mellom dei to metodane blir
halvert for kvar verdi av k.

Backwards 2 har ein større multiplikator av h, og dermed vert feilen mindre raskare.
"""
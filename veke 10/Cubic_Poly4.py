"""
Frå boka:

Exercise 9.2: Make polynomial subclasses of parabolas
"""

class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
    
    def __call__(self, x):
        res = self.c0 + self.c1*x
        print ('Line call: %g' %(res))
        return res
    
    def table(self, L, R, n): #Return a table with n points for L <= x <= R.
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += ('%12g %12g\n' %( x, y))
        return s

#for the inheritance to create more complex polynomials we simply
#incorporate the parent's constructor and call methods

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1) # let Line store c0 and c1
        self.c2 = c2
    
    def __call__(self, x):
        res = Line.__call__(self, x)+self.c2*x**2
        print('Parabola call: %g' %(res))
        return res


class Cubic(Parabola):
    def __init__ (self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2) #let Parabola store c0-c2
        self.c3 = c3
    
    def __call__(self, x):
        res = Parabola.__call__(self, x)+self.c3*x**3
        print('Cubic call: %g' %(res))
        return res


class Poly4(Cubic):
    def __init__ (self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3) # let Cubic store c0-c3
        self.c4 = c4
    
    def __call__(self, x):
        res = Cubic.__call__(self, x)+self.c4*x**4
        print ('Poly4 call: %g' %(res))
        return res

C = Cubic(1,2,3,4)
P4 = Poly4(1,2,3,4,5)

print ('\nCalling from Cubic, coefficients c0-c3 1,2,3,4,   x=10:\n')
C(10)

print ('\nCalling from Poly4, coefficients c0-c4 1,2,3,4,5, x=10:\n')
P4(10)

"""
Terminal> python Cubic_Poly4.py

Calling from Cubic, coefficients c0-c3 1,2,3,4,   x=10:

Line call: 21
Parabola call: 321
Cubic call: 4321

Calling from Poly4, coefficients c0-c4 1,2,3,4,5, x=10:

Line call: 21
Parabola call: 321
Cubic call: 4321
Poly4 call: 54321
"""
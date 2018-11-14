"""
Frå boka:

Exercise 7.5: Make a class for quadratic functions
"""
import numpy as np
import math
import cmath

class Quadratic:

    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def value (self, x):
        return self.a*x**2+self.b*x+self.c
    
    
    def table (self, L, R, n):
        #frå sin_plus_quadratic.py
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in np.linspace(L, R, n):
            y = self.value(x)
            s += ('%12g %12g\n' % (x, y))
        return s
    
    def roots (self):
        a = self.a
        b = self.b
        c = self.c
        roots = []
        discriminant = (b**2) - (4*a*c)

        #reelle røter
        if discriminant > 0:
            roots.append((-b-math.sqrt(discriminant))/(2*a))
            roots.append((-b+math.sqrt(discriminant))/(2*a))
            return roots

        #complekse røter
        elif discriminant < 0:
            roots.append((-b-cmath.sqrt(discriminant))/(2*a))
            roots.append((-b+cmath.sqrt(discriminant))/(2*a))
            return roots

        #ei reell rot
        else:
            roots.append((-b+math.sqrt(discriminant))/(2*a))
            return roots

    @staticmethod
    def test_value():
        quad_real = Quadratic(2,5,3) # ei av røtene er -1.5
        assert quad_real.value(-1.5) == 0, 'Quadratic.value() does not work properly!'

    @staticmethod
    def test_roots():
        quad_real = Quadratic(2,5,3)    # har røter -1.5, -1.0
        quad_imag = Quadratic(1,4,5)    # har røter (-2+1j), (-2-1j)
        quad_one  = Quadratic(-4,12,-9) # har rot 1.5

        assert quad_real.roots() == [-1.5, -1.0],       'The real roots are incorrect!'
        assert quad_imag.roots() == [(-2-1j), (-2+1j)], 'The imaginary roots are incorrect!'
        assert quad_one.roots()  == [1.5],              'The root is incorrect!'

    @staticmethod
    def table_demo():
        test_quad = Quadratic(2,5,3)
        s = '           x     |     y\n'
        print(s + test_quad.table(-10,10,21))

"""
All testing blir utført i Quadratic_demo.py. Her er output frå den fila:

Terminal> python Quadratic_demo.py

We are demonstrating the Quadratic class/module:
Table demonstration:
           x     |     y
         -10          153
          -9          120
          -8           91
          -7           66
          -6           45
          -5           28
          -4           15
          -3            6
          -2            1
          -1            0
           0            3
           1           10
           2           21
           3           36
           4           55
           5           78
           6          105
           7          136
           8          171
           9          210
          10          253

value() test:
roots() test:
tests completed successfully
"""
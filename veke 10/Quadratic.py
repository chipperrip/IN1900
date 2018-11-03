"""
Frå boka:

Exercise 7.5: Make a class for quadratic functions
"""
import numpy as np

class Quadratic:

    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def value (self, x):

        return self.a*x**2+self.b*x+self.c
    
    
    #def table (self, x, n):
    
    def roots (self):
        
        a = self.a
        b = self.b
        c = self.c
        roots = []
        """
        if b**2 < 4*a*c:
            roots.append((-b+1jsqrt((4*a*c)-b**2))/2*a)
            roots.append((-b-1jsqrt((4*a*c)-b**2))/2*a)
            return roots
        """
        roots.append((-b-np.sqrt(b**2-(4*a*c)))/(2*a))
        roots.append((-b+np.sqrt(b**2-(4*a*c)))/(2*a))
        return roots


def test_roots():

    quad_real = Quadratic(2,5,3)
    quad_imag = Quadratic(1,4,5)

    print(quad_real.roots())
    print(np.roots([2,5,3]))

    assert quad_real.roots() == np.roots([2,5,3])

test_roots()
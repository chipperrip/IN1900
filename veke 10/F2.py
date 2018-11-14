"""
Frå boka:

Exercise 7.11: Implement special methods in a class

"""

from numpy import exp, sin

class F:
	def __init__(self, a, w):
		self.a = a
		self.w = w

	# Lagrar funksjonen som strengrepresentasjonen av klassa
	def __str__(self):
		return 'exp(-a*x)*sin(w*x)'

	# finn funksjonsverdien ved å ta eval på strengrepresentasjonen
	def __call__(self, x):
		a = self.a
		w = self.w
		return eval(self.__str__())

"""
Terminal> python

>>> from F2 import F
>>> f = F(a=1.0, w=0.1)
>>> from math import pi
>>> print (f(x=pi))
0.013353835137
>>> f.a = 2
>>> print (f(pi))
0.00057707154012
>>> print (f)
exp(-a*x)*sin(w*x)

alt køyrde som det skulle.
"""
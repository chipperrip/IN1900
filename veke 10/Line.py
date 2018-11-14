"""
Frå boka:

Exercise 7.6: Make a class for straight lines
"""

class Line:

	def __init__ (self, p1, p2):

		self.x0 = p1[0]
		self.y0 = p1[1]
		self.x1 = p2[0]
		self.y1 = p2[1]

	
	def value (self, x):
		"""
		Compute the coefficients a and b in the mathematical
		expression for a straight line y = a*x + b that goes
		through two points (x0, y0) and (x1, y1).
		x0, y0: a point on the line (floats).
		x1, y1: another point on the line (floats).
		return: the value y = a*x+b.
		"""

		a = (self.y1 - self.y0)/(self.x1 - self.x0)
		b = self.y0 - a*self.x0
		return a*x+b


def test_Line():
	#tester same verdiar frå eksempelet i oppgåva:
	line = Line((0,-1), (2,4))
	assert (line.value(0.5) == 0.25) and (line.value(0) == -1.0) and (line.value(1) == 1.5), \
	'Values are wrong!'


"""
Terminal> python

>>> from Line import Line, test_Line
>>> line = Line((0,-1), (2,4))
>>> print (line.value(0.5), line.value(0), line.value(1))
0.25 -1.0 1.5
>>> test_Line()

Alt gjekk som det skulle.
"""
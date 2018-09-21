"""
From the exercise collection:
Exercise 4.1. Quadratic with user input

Consider the usual formula for computing solutions to the quadratic equation
ax2 + bx + c = 0 given by

x = -b +- sqrt(b^2-4ac)/2a
"""
import math

print('\nPlease input values for a quadratic equation: \n')

#user input for a,b,c values
a = float(input('a  = ? '))
b = float(input('b  = ? '))
c = float(input('c  = ? '))

"""
function for calculating the quadratic equation given a,b,c
returns a list with two elements
x[0] is the positive sqrt variant x+
x[1] is the negative sqrt variant x-
"""
def quad_eq(a, b, c):

	x = []

	x.append((-b + math.sqrt((b**2)-(4*a*c)))/(2*a))
	x.append((-b - math.sqrt((b**2)-(4*a*c)))/(2*a))

	return x

x = quad_eq(a, b, c)

print()
print('x+ = %5.2f \nx- = %5.2f' %(x[0], x[1]))
print()

"""
Terminal> python quadratic_roots_input.py

Please input values for a quadratic equation:

a  = ? 1
b  = ? 3
c  = ? -4

x+ =  1.00
x- = -4.00

"""
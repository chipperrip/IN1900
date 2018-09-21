"""
From the exercise collection:
Exercise 4.2. Quadratic with exceptions

Modify the program in Problem 4.1 to read values for a,b, and c from the
command line. Use exceptions (IndexError) to handle missing arguments.

Consider the usual formula for computing solutions to the quadratic equation
ax2 + bx + c = 0 given by

x = -b +- sqrt(b^2-4ac)/2a
"""
import math
import sys

print('\nExercise 4.2 Quadratic with exceptions: \n')

try:
	#cml input for a,b,c values
	values = [float(v) for v in sys.argv[1:]]
	a = values[0]
	b = values[1]
	c = values[2]
	print('a  = %5.2f' %(a))
	print('b  = %5.2f' %(b))
	print('c  = %5.2f' %(c))

except IndexError as error:
	print('Error, missing arguments!\n')
	print('Please input values for a quadratic equation: \n')

	#user input for a,b,c values
	a = float(input('a  = ? '))
	b = float(input('b  = ? '))
	c = float(input('c  = ? '))




"""
function for calculating the quadratic equation given a,b,c
returns a list with two elements
x[0] is the +sqrt variant x+
x[1] is the -sqrt variant x-
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
Terminal> python quadratic_roots_error.py 1 3 -4

Exercise 4.2 Quadratic with exceptions:

a  =  1.00
b  =  3.00
c  = -4.00

x+ =  1.00
x- = -4.00

Terminal> python quadratic_roots_error.py 

Exercise 4.2 Quadratic with exceptions:

Error, missing arguments!

Please input values for a quadratic equation:

a = ? 1
b = ? 3
c = ? -4

x+ =  1.00
x- = -4.00

"""
"""
From the exercise collection:
Exercise 4.3. Quadratic fixed

Consider the program from Problem 4.2. Not all inputs yield valid real solutions
(e.g. a = 1, b = 1, c = 1). Modify the program using exceptions or if-tests to
handle invalid input and provide a suitable message for the user.

Consider the usual formula for computing solutions to the quadratic equation
ax2 + bx + c = 0 given by

x = -b +- sqrt(b^2-4ac)/2a
"""
import math
import sys

print('\nExercise 4.3 Quadratic fixed: \n')

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

except ValueError as error:

	print('Error, non-number input detected.\n')
	print('Please input values for a quadratic equation:\n')

	#user input for a,b,c values
	a = float(input('a  = ? '))
	b = float(input('b  = ? '))
	c = float(input('c  = ? '))

# Check if our values give real roots
numberIsComplex = ((b**2)-(4*a*c)) < 0

if numberIsComplex:
	print ('\nGiven a, b, c values result in complex solutions! Aborting...\n')
	quit()


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
Terminal> python quadratic_roots_error2.py 1 1 1

Exercise 4.3 Quadratic fixed:

a  =  1.00
b  =  1.00
c  =  1.00

Given a, b, c values result in complex solutions! Aborting...
 
Terminal> python quadratic_roots_error2.py 1 3 e

Exercise 4.3 Quadratic fixed:

Error, non-number input detected.

Please input values for a quadratic equation:

a  = ? 1
b  = ? 3
c  = ? -4

x+ =  1.00
x- = -4.00

"""
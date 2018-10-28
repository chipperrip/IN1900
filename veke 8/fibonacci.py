"""
Frå oppgåveheftet:

Exercise A.2. Solve a difference equation numerically
"""

n = 15
x0 = 1
x1 = x0

print('\nFibonacci sequence where n = 15\n')
print('x0 = 1')
print('x1 = 1')



xpp = x0
xp  = x1

for i in range(2, n+1):

	# fibonacci-likninga
	x = xp + xpp

	xpp = xp
	xp = x
	print('x%g = %g' %(i,x))

print()

"""
Terminal> python fibonacci.py

Fibonacci sequence where n = 15

x0 = 1
x1 = 1
x2 = 2
x3 = 3
x4 = 5
x5 = 8
x6 = 13
x7 = 21
x8 = 34
x9 = 55
x10 = 89
x11 = 144
x12 = 233
x13 = 377
x14 = 610
x15 = 987

"""
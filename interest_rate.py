"""
Exercise 1.6: Compute the growth of money in a bank
"""


#initial money
A = 1000

#percent interest rate
p = 5

#years running
n = 3

#final value after years of interest
growth = A*(1+(p/100))**n

print ("\nThe initial sum is %g euros. After %g years at %g percent interest rate, we end up with %g euros.\n" %(A, n, p, growth))

"""
OUTPUT:

The initial sum is 1000 euros. After 3 years at 5 percent interest rate, we end up with 1157.63 euros.

"""

"""
Exercise 2.11: Compute a mathematical sum

In this exercise we're supposed to find 3 errors in the following code:

s = 0; k = 1; M = 100
    while k < M:
    s += 1/k
print s

1) The loop index doesn't increment, causing an endless loop

2) The upper bound of the loop doesn't include the upper limit of summation

3) If the exercise was written for Python 3, then the print statement is
missing parentheses

4) If the exercise was written for Python 2, then the sum operation uses
integer division, which isn't practical, as it will
lead to huge rounding errors.
"""

#Altered program:
s = 0; k = 1; M = 100

#included the upper bound in the while condition
while k <= M:
    #python 3 always uses true division for the / operator
    s += 1/k

    #print statement for checking intermediate results:
    #print("k: %g sum: %f" %(k, s))

    #added incrementation of index
    k += 1
#added parentheses to the print function
print (s)

"""
OUTPUT:
5.187377517639621
"""

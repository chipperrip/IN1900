"""
Exercise 2.9: Store values from a formula in lists

In this exercise we're working with the following formula:

y(t) = v0*t - (1/2)*g*t^2

y(t)    is the height of an object in m as a function of time
t       is time in seconds
v0      is initial velocity in m/s
g       is gravitational accelleration in m/s^2
"""

#number of t values for this exercise
n = 10

#initial velocity in m/s
v0 = 5.0

#standard gravity in m/s^2
g = 9.81

#time until y = 0
t_stop = 2*v0/g

# n uniformly spaced t intervals from start till y = 0
dt = t_stop/n

#lists for t and y values
tList = []
yList = []

#populate the t and y lists
for i in range(n+1):
    #time in seconds as a function of the sum of i intervals
    t = i * dt
    tList.append(t)
    yList.append(v0 * t - 0.5 * g * t**2)

#print list by columns
print ('  t    y(t)')
for t, y in zip(tList, yList):
    print ('%.2fs %.2fm' %(t,y))

"""
OUTPUT:
  t    y(t)
0.00s 0.00m
0.10s 0.46m
0.20s 0.82m
0.31s 1.07m
0.41s 1.22m
0.51s 1.27m
0.61s 1.22m
0.71s 1.07m
0.82s 0.82m
0.92s 0.46m
1.02s 0.00m
"""

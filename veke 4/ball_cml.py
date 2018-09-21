"""
Exercise 4.10: Read parameters in a formula from the command line

Modify the program listed in Exercise 4.9 such that v0 and t are
read from the command line.
"""
import sys

g = 9.81

# program modified to assign t, v0 to cml args
# args are strings; convert to floats
t, v0 = [float(x) for x in sys.argv[1:]]

y = v0*t - 0.5*g*t**2
print ('%g' %(y))

"""
Terminal>   python ball_cml.py 0.6 3
0.0342
"""
